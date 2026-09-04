/**
 * 每日對話練習 - 主應用程式核心腳本
 * 負責資料渲染、分級切換、教材導覽、中英對照顯示控制與跟讀錄音比對功能
 */

let allDialogues = [];
let currentDialogue = null;
let currentLevelFilter = 'all';

// 錄音器相關變數
let mediaRecorder = null;
let audioChunks = [];
let recordedAudioUrl = null;

document.addEventListener('DOMContentLoaded', async () => {
  await loadDialoguesData();
  bindUIEvents();
  initRecorder();
  
  // 系統自動判斷今日月-日，導到相對應日期的對話
  locateTodayDialogue();
});

// 取得今日月-日 (格式: MM-DD)
function getTodayMMDD() {
  const now = new Date();
  const mm = String(now.getMonth() + 1).padStart(2, '0');
  const dd = String(now.getDate()).padStart(2, '0');
  return `${mm}-${dd}`;
}

// 格式化月日顯示 (例如 09-03 轉為 9月3日)
function formatDisplayDate(mmdd) {
  if (!mmdd) return '';
  const parts = mmdd.split('-');
  if (parts.length === 2) {
    return `${parseInt(parts[0], 10)}月${parseInt(parts[1], 10)}日`;
  }
  return mmdd;
}

// 自動定位到今日對話
function locateTodayDialogue() {
  if (!allDialogues || allDialogues.length === 0) return;
  const todayMMDD = getTodayMMDD();

  // 優先尋找與今日日期完全相符的篇章
  let target = allDialogues.find(d => d.date === todayMMDD);

  // 若今日篇章未收錄（如在測試階段），優先選取當月或首篇
  if (!target) {
    const currentMonth = todayMMDD.split('-')[0];
    target = allDialogues.find(d => d.date.startsWith(currentMonth)) || allDialogues[0];
  }

  selectDialogue(target.id);
}

// 載入對話資料
async function loadDialoguesData() {
  if (window.DAILY_DIALOGUES && Array.isArray(window.DAILY_DIALOGUES)) {
    allDialogues = window.DAILY_DIALOGUES;
  } else {
    try {
      const response = await fetch('data/dialogues.json');
      allDialogues = await response.json();
    } catch (e) {
      console.error('無法載入對話資料：', e);
    }
  }
  renderDialogueSelector();
}

// 綁定所有 UI 互動事件
function bindUIEvents() {
  // 分級切換按鈕
  document.querySelectorAll('.level-pill').forEach(btn => {
    btn.addEventListener('click', (e) => {
      document.querySelectorAll('.level-pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentLevelFilter = btn.dataset.level;
      renderDialogueSelector();

      // 切換後自動切換至該分級的第一篇對話
      const filtered = getFilteredDialogues();
      if (filtered.length > 0) {
        selectDialogue(filtered[0].id);
      }
    });
  });

  // 中英顯示切換
  const toggleZhBtn = document.getElementById('toggle-zh-btn');
  if (toggleZhBtn) {
    toggleZhBtn.addEventListener('click', () => {
      document.body.classList.toggle('hide-zh');
      const isHidden = document.body.classList.contains('hide-zh');
      toggleZhBtn.classList.toggle('active', isHidden);
      toggleZhBtn.querySelector('span').textContent = isHidden ? '顯示中文' : '隱藏中文';
    });
  }

  // 大字體模式切換
  const toggleFontBtn = document.getElementById('toggle-font-btn');
  if (toggleFontBtn) {
    toggleFontBtn.addEventListener('click', () => {
      document.body.classList.toggle('large-font');
      toggleFontBtn.classList.toggle('active');
    });
  }

  // 隨機抽選一篇練習
  const randomBtn = document.getElementById('random-btn');
  if (randomBtn) {
    randomBtn.addEventListener('click', () => {
      const filtered = getFilteredDialogues();
      if (filtered.length > 0) {
        const randomIndex = Math.floor(Math.random() * filtered.length);
        selectDialogue(filtered[randomIndex].id);
      }
    });
  }

  // 主播放器控制按鈕
  const mainPlayBtn = document.getElementById('main-play-btn');
  if (mainPlayBtn) {
    mainPlayBtn.addEventListener('click', () => {
      window.dialoguePlayer.togglePlay();
    });
  }

  // 播放器收合 / 展開按鈕 (手機極致輕盈模式)
  const collapseBtn = document.getElementById('toggle-player-collapse-btn');
  const playerBar = document.getElementById('fixed-player-bar');
  if (collapseBtn && playerBar) {
    collapseBtn.addEventListener('click', () => {
      const isCollapsed = playerBar.classList.toggle('is-collapsed');
      const iconSpan = collapseBtn.querySelector('.collapse-icon');
      if (iconSpan) {
        iconSpan.textContent = isCollapsed ? '展開 ▴' : '收合 ▾';
      }
    });
  }

  const rewindBtn = document.getElementById('rewind-btn');
  if (rewindBtn) {
    rewindBtn.addEventListener('click', () => window.dialoguePlayer.seek(-5));
  }

  const forwardBtn = document.getElementById('forward-btn');
  if (forwardBtn) {
    forwardBtn.addEventListener('click', () => window.dialoguePlayer.seek(5));
  }

  // 進度滑桿拖動
  const progressBar = document.getElementById('audio-progress');
  if (progressBar) {
    progressBar.addEventListener('input', (e) => {
      const percent = parseFloat(e.target.value) / 100;
      window.dialoguePlayer.seekToPercent(percent);
    });
  }

  // 語速切換按鈕 (0.75x, 1.0x, 1.25x, 1.5x)
  document.querySelectorAll('.speed-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const speed = btn.dataset.speed;
      window.dialoguePlayer.setPlaybackRate(speed);
    });
  });

  // 日期/文章選單下拉變化
  const selectorDropdown = document.getElementById('dialogue-select-dropdown');
  if (selectorDropdown) {
    selectorDropdown.addEventListener('change', (e) => {
      selectDialogue(e.target.value);
    });
  }

  // 錄音彈窗關閉按鈕
  const closeRecordModalBtn = document.getElementById('close-record-modal');
  if (closeRecordModalBtn) {
    closeRecordModalBtn.addEventListener('click', () => {
      document.getElementById('record-modal').classList.add('hidden');
    });
  }

  // 前一天 / 後一天 / 今日 按鈕監聽 (支援全年循環)
  const prevDayBtn = document.getElementById('prev-day-btn');
  if (prevDayBtn) {
    prevDayBtn.addEventListener('click', () => navigateDialogueByDay(-1));
  }

  const nextDayBtn = document.getElementById('next-day-btn');
  if (nextDayBtn) {
    nextDayBtn.addEventListener('click', () => navigateDialogueByDay(1));
  }

  const todayDayBtn = document.getElementById('today-day-btn');
  if (todayDayBtn) {
    todayDayBtn.addEventListener('click', () => locateTodayDialogue());
  }

  // 鍵盤快速鍵支援（課堂電子白板與自主練習超方便）
  window.addEventListener('keydown', (e) => {
    // 若在輸入框內則不觸發
    if (['INPUT', 'SELECT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;

    if (e.code === 'Space') {
      e.preventDefault();
      window.dialoguePlayer.togglePlay();
    } else if (e.code === 'ArrowLeft') {
      e.preventDefault();
      window.dialoguePlayer.seek(-5);
    } else if (e.code === 'ArrowRight') {
      e.preventDefault();
      window.dialoguePlayer.seek(5);
    } else if (e.key === '[' || e.key === 'BracketLeft') {
      navigateDialogueByDay(-1);
    } else if (e.key === ']' || e.key === 'BracketRight') {
      navigateDialogueByDay(1);
    } else if (e.key.toLowerCase() === 't') {
      locateTodayDialogue();
    } else if (e.key === '1') {
      window.dialoguePlayer.setPlaybackRate('0.75');
    } else if (e.key === '2') {
      window.dialoguePlayer.setPlaybackRate('1.0');
    } else if (e.key === '3') {
      window.dialoguePlayer.setPlaybackRate('1.25');
    } else if (e.key === '4') {
      window.dialoguePlayer.setPlaybackRate('1.5');
    } else if (e.key.toLowerCase() === 'h') {
      document.getElementById('toggle-zh-btn')?.click();
    }
  });
}

// 依據天數前後循環切換 (offset: -1 為前一天, +1 為後一天)
function navigateDialogueByDay(offset) {
  if (!allDialogues || allDialogues.length === 0 || !currentDialogue) return;

  const filtered = getFilteredDialogues();
  const listToUse = filtered.length > 0 ? filtered : allDialogues;

  const currentIndex = listToUse.findIndex(d => d.id === currentDialogue.id);
  if (currentIndex === -1) return;

  // 循環索引計算（全年閉環循環）
  let targetIndex = (currentIndex + offset) % listToUse.length;
  if (targetIndex < 0) {
    targetIndex = listToUse.length - 1;
  }

  selectDialogue(listToUse[targetIndex].id);
}

// 取得篩選後的對話清單
function getFilteredDialogues() {
  if (currentLevelFilter === 'all') {
    return allDialogues;
  }
  return allDialogues.filter(d => {
    if (currentLevelFilter === 'junior') {
      return d.level === 'junior' || d.level === 'junior_high';
    }
    if (currentLevelFilter === 'senior') {
      return d.level === 'senior' || d.level === 'senior_high';
    }
    return d.level === currentLevelFilter;
  });
}

// 渲染下拉選單 (簡化文字長度，徹底避免手機版寬度被撐爆)
function renderDialogueSelector() {
  const dropdown = document.getElementById('dialogue-select-dropdown');
  if (!dropdown) return;

  const filtered = getFilteredDialogues();
  dropdown.innerHTML = filtered.map(item => {
    const isSelected = currentDialogue && currentDialogue.id === item.id;
    const dateText = formatDisplayDate(item.date);
    return `<option value="${item.id}" ${isSelected ? 'selected' : ''}>${dateText} · ${item.topic.zh}</option>`;
  }).join('');
}

// 選擇並載入特定對話
function selectDialogue(dialogueId) {
  const target = allDialogues.find(d => d.id === dialogueId);
  if (!target) return;

  currentDialogue = target;

  // 更新下拉選單
  const dropdown = document.getElementById('dialogue-select-dropdown');
  if (dropdown) dropdown.value = dialogueId;

  // 渲染對話主要區塊
  renderDialogueCard(target);

  // 載入播放器
  window.dialoguePlayer.loadDialogue(target);

  // 更新底部播放器正在朗讀標籤 (只顯示日期與純中文篇名，不顯示學層與英文)
  const currentTitleTag = document.getElementById('player-dialogue-title');
  if (currentTitleTag) {
    currentTitleTag.textContent = `${formatDisplayDate(target.date)} · ${target.topic.zh}`;
  }
}

// 渲染整頁對話與學習內容
function renderDialogueCard(data) {
  // 頂部看板日期與今日指示
  const todayMMDD = getTodayMMDD();
  const isToday = (data.date === todayMMDD);

  document.getElementById('dialogue-date-badge').textContent = `📅 ${formatDisplayDate(data.date)}`;
  
  const todayIndicator = document.getElementById('today-indicator');
  if (todayIndicator) {
    if (isToday) {
      todayIndicator.classList.remove('hidden');
    } else {
      todayIndicator.classList.add('hidden');
    }
  }

  const levelBadge = document.getElementById('dialogue-level-badge');
  levelBadge.textContent = data.levelName;
  levelBadge.style.backgroundColor = data.levelBadgeColor || '#22c55e';
  levelBadge.style.color = '#ffffff';

  document.getElementById('dialogue-category-badge').textContent = `🏷️ ${data.category}`;
  document.getElementById('topic-title-en').textContent = data.topic.en;
  document.getElementById('topic-title-zh').textContent = data.topic.zh;
  document.getElementById('situation-text').textContent = `情境引導：${data.situation}`;

  // 對話泡泡
  const dialogueContainer = document.getElementById('dialogue-bubbles-container');
  dialogueContainer.innerHTML = data.dialogue.map(item => `
    <div class="sentence-bubble" id="sentence-${item.id}" onclick="window.dialoguePlayer.playSentence(${item.id})">
      <div class="speaker-avatar-wrap">
        <div class="speaker-avatar">${item.avatar || '🗣️'}</div>
        <span class="speaker-name">${item.speaker}</span>
      </div>
      <div class="sentence-content">
        <div class="sentence-en">${highlightKeywords(item.en, item.keywords, data.vocabulary)}</div>
        <div class="sentence-zh" id="zh-${item.id}">${item.zh}</div>
        <div class="sentence-actions">
          <button class="btn-speak-sentence" onclick="event.stopPropagation(); window.dialoguePlayer.playSentence(${item.id})">
            🔊 點擊播放此句
          </button>
          <button class="btn-speak-sentence btn-peek-zh" onclick="event.stopPropagation(); toggleSingleZh(${item.id})">
            👁️ 查看中文
          </button>
          <button class="btn-speak-sentence" style="color: #ea580c; border-color: #fdba74;" onclick="event.stopPropagation(); openRecordModal(${item.id}, '${escapeQuote(item.en)}', '${escapeQuote(item.zh)}')">
            🎤 錄音跟讀比對
          </button>
        </div>
      </div>
    </div>
  `).join('');

  // 單字卡清單
  const vocabGrid = document.getElementById('vocab-grid-container');
  if (data.vocabulary && data.vocabulary.length > 0) {
    document.getElementById('vocab-section').classList.remove('hidden');
    vocabGrid.innerHTML = data.vocabulary.map(v => `
      <div class="vocab-card">
        <div class="vocab-header">
          <div>
            <span class="vocab-word">${v.word}</span>
            <span class="vocab-phonetic">${v.phonetic || ''}</span>
            <span style="font-size: 0.8rem; color: #f59e0b; font-weight: bold; margin-left: 4px;">${v.pos || ''}</span>
          </div>
          <button class="vocab-speaker-btn" title="聽單字發音" onclick="window.dialoguePlayer.speakWord('${v.word}')">
            🔊
          </button>
        </div>
        <div class="vocab-meaning">${v.zh}</div>
        <div class="vocab-example">例句：${v.example || ''}</div>
      </div>
    `).join('');
  } else {
    document.getElementById('vocab-section').classList.add('hidden');
  }

  // 今日金句與文化小叮嚀
  if (data.dailyPhrase) {
    document.getElementById('phrase-en').textContent = data.dailyPhrase.en;
    document.getElementById('phrase-zh').textContent = data.dailyPhrase.zh;
  }
  if (data.cultureTip) {
    document.getElementById('culture-text').textContent = data.cultureTip;
  }
}

// 輔助函式：高亮關鍵字（支援點擊聽單字發音與懸停提示）
function highlightKeywords(text, keywords, vocabulary) {
  if (!keywords || !keywords.length) return text;
  let result = text;
  const vocabMap = {};
  if (vocabulary && Array.isArray(vocabulary)) {
    vocabulary.forEach(v => {
      vocabMap[v.word.toLowerCase()] = v;
    });
  }

  keywords.forEach(kw => {
    const regex = new RegExp(`\\b(${kw})\\b`, 'gi');
    const vocabInfo = vocabMap[kw.toLowerCase()];
    const tooltipText = vocabInfo ? `${vocabInfo.word} ${vocabInfo.phonetic || ''} [${vocabInfo.pos || ''}]：${vocabInfo.zh}` : `點擊聽發音：${kw}`;
    
    result = result.replace(regex, `<span class="inline-keyword" title="${tooltipText}" onclick="event.stopPropagation(); window.dialoguePlayer.speakWord('$1')">$1</span>`);
  });
  return result;
}

// 單獨切換特定句子的中文翻譯（適合英聽模式挑戰時偷看）
function toggleSingleZh(sentenceId) {
  const zhEl = document.getElementById(`zh-${sentenceId}`);
  if (zhEl) {
    zhEl.classList.toggle('force-show');
  }
}

function escapeQuote(str) {
  return (str || '').replace(/'/g, "\\'");
}

/* ================= 學生自主錄音與發音對比功能 ================= */
function initRecorder() {
  const recordTriggerBtn = document.getElementById('record-action-btn');
  const playUserRecordingBtn = document.getElementById('play-user-recording-btn');

  if (recordTriggerBtn) {
    recordTriggerBtn.addEventListener('click', async () => {
      if (!mediaRecorder || mediaRecorder.state === 'inactive') {
        startRecording();
      } else {
        stopRecording();
      }
    });
  }

  if (playUserRecordingBtn) {
    playUserRecordingBtn.addEventListener('click', () => {
      if (recordedAudioUrl) {
        const userAudio = new Audio(recordedAudioUrl);
        userAudio.play();
      }
    });
  }
}

let activeModalSentenceId = null;

function openRecordModal(sentenceId, enText, zhText) {
  activeModalSentenceId = sentenceId;
  const modal = document.getElementById('record-modal');
  document.getElementById('modal-sentence-en').textContent = enText;
  document.getElementById('modal-sentence-zh').textContent = zhText;
  
  // 重置錄音狀態
  document.getElementById('record-status-text').textContent = '準備好了嗎？點擊「開始錄音」並大聲跟讀！';
  document.getElementById('play-user-recording-btn').classList.add('hidden');
  
  modal.classList.remove('hidden');
}

// 彈窗內聽標準示範
window.playModalOriginalSentence = function() {
  if (activeModalSentenceId) {
    window.dialoguePlayer.playSentence(activeModalSentenceId);
  }
};

async function startRecording() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    audioChunks = [];

    mediaRecorder.ondataavailable = (event) => {
      audioChunks.push(event.data);
    };

    mediaRecorder.onstop = () => {
      const audioBlob = new Blob(audioChunks, { type: 'audio/mp3' });
      recordedAudioUrl = URL.createObjectURL(audioBlob);
      document.getElementById('play-user-recording-btn').classList.remove('hidden');
      document.getElementById('record-status-text').textContent = '🎉 錄音完成！點擊下方按鈕聽聽自己的發音吧！';
    };

    mediaRecorder.start();
    const recordBtn = document.getElementById('record-action-btn');
    recordBtn.textContent = '⏹️ 停止錄音';
    recordBtn.style.background = '#ef4444';
    document.getElementById('record-status-text').textContent = '🎙️ 正在錄音中...請清晰自信地朗讀！';
  } catch (err) {
    alert('無法存取麥克風，請檢查瀏覽器麥克風權限設定。');
    console.error('錄音權限錯誤:', err);
  }
}

function stopRecording() {
  if (mediaRecorder && mediaRecorder.state === 'recording') {
    mediaRecorder.stop();
    const recordBtn = document.getElementById('record-action-btn');
    recordBtn.textContent = '🎙️ 重新錄音';
    recordBtn.style.background = '#10b981';
  }
}
