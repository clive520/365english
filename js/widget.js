/**
 * 365 每日生活美語 - 側邊欄微件核心腳本 (widget.js)
 * 專注於純粹的核心學習體驗：前/後天日期切換、情境引導、單句點擊發音與精簡微型播放器
 */

let allDialogues = [];
let currentDialogue = null;

document.addEventListener('DOMContentLoaded', async () => {
  await loadWidgetData();
  bindWidgetEvents();
  locateInitialDialogue();
});

// 載入全年度對話資料
async function loadWidgetData() {
  if (window.DIALOGUES_DATA && Array.isArray(window.DIALOGUES_DATA)) {
    allDialogues = window.DIALOGUES_DATA;
  } else {
    try {
      const resp = await fetch('data/dialogues.json');
      allDialogues = await resp.json();
    } catch (e) {
      console.error('無法載入對話資料：', e);
    }
  }
}

// 取得今日 MM-DD
function getTodayMMDD() {
  const now = new Date();
  const mm = String(now.getMonth() + 1).padStart(2, '0');
  const dd = String(now.getDate()).padStart(2, '0');
  return `${mm}-${dd}`;
}

// 格式化月日顯示 (例如 09-04 轉為 9月4日)
function formatDisplayDate(mmdd) {
  if (!mmdd) return '';
  const parts = mmdd.split('-');
  if (parts.length === 2) {
    return `${parseInt(parts[0], 10)}月${parseInt(parts[1], 10)}日`;
  }
  return mmdd;
}

// 初始化定位對話（支援 URL 參數 ?date=MM-DD，預設為今日）
function locateInitialDialogue() {
  if (!allDialogues || allDialogues.length === 0) return;

  const urlParams = new URLSearchParams(window.location.search);
  const dateParam = urlParams.get('date');

  let target = null;
  if (dateParam) {
    target = allDialogues.find(d => d.date === dateParam);
  }

  if (!target) {
    const todayMMDD = getTodayMMDD();
    target = allDialogues.find(d => d.date === todayMMDD);
  }

  if (!target) {
    target = allDialogues[0];
  }

  renderWidgetDialogue(target.id);
}

// 渲染特定篇章對話
function renderWidgetDialogue(dialogueId) {
  const target = allDialogues.find(d => d.id === dialogueId);
  if (!target) return;

  currentDialogue = target;

  // 頂部日期看板
  const todayMMDD = getTodayMMDD();
  const isToday = (target.date === todayMMDD);

  const dateBadge = document.getElementById('dialogue-date-badge');
  if (dateBadge) {
    dateBadge.textContent = `📅 ${formatDisplayDate(target.date)}`;
  }

  const todayIndicator = document.getElementById('today-indicator');
  if (todayIndicator) {
    if (isToday) {
      todayIndicator.classList.remove('hidden');
    } else {
      todayIndicator.classList.add('hidden');
    }
  }

  // 學層標籤與主題標籤
  const levelBadge = document.getElementById('dialogue-level-badge');
  if (levelBadge) {
    levelBadge.textContent = target.levelName;
    levelBadge.style.backgroundColor = target.levelBadgeColor || '#0284c7';
    levelBadge.style.color = '#ffffff';
  }

  const categoryBadge = document.getElementById('dialogue-category-badge');
  if (categoryBadge) {
    categoryBadge.textContent = `🏷️ ${target.category}`;
  }

  // 篇名標題
  const titleEn = document.getElementById('topic-title-en');
  if (titleEn) titleEn.textContent = target.topic.en;

  const titleZh = document.getElementById('topic-title-zh');
  if (titleZh) titleZh.textContent = target.topic.zh;

  // 情境引導
  const situationBox = document.getElementById('situation-text');
  if (situationBox) situationBox.textContent = `情境引導：${target.situation}`;

  // 對話泡泡渲染
  const container = document.getElementById('dialogue-bubbles-container');
  if (container) {
    container.innerHTML = target.dialogue.map(item => `
      <div class="sentence-bubble" id="sentence-${item.id}" onclick="window.dialoguePlayer.playSentence(${item.id})">
        <div class="speaker-avatar-wrap">
          <div class="speaker-avatar">${item.avatar || '🗣️'}</div>
          <span class="speaker-name">${item.speaker}</span>
        </div>
        <div class="sentence-content">
          <div class="sentence-en">${highlightKeywords(item.en, item.keywords, target.vocabulary)}</div>
          <div class="sentence-zh">${item.zh}</div>
        </div>
      </div>
    `).join('');
  }

  // 載入音訊到全域播放器
  if (window.dialoguePlayer) {
    window.dialoguePlayer.loadDialogue(target);
  }

  // 更新播放器標題
  const playerTitle = document.getElementById('player-dialogue-title');
  if (playerTitle) {
    playerTitle.textContent = `${formatDisplayDate(target.date)} · ${target.topic.zh}`;
  }
}

// 高亮重點關鍵字 (虛線強調)
function highlightKeywords(enText, keywords, vocabList) {
  if (!keywords && !vocabList) return enText;
  const wordsToHighlight = new Set();
  if (keywords) keywords.forEach(k => wordsToHighlight.add(k.toLowerCase()));
  if (vocabList) vocabList.forEach(v => wordsToHighlight.add(v.word.toLowerCase()));

  const sortedKeywords = Array.from(wordsToHighlight).sort((a, b) => b.length - a.length);
  let highlighted = enText;

  sortedKeywords.forEach(kw => {
    if (!kw || kw.length < 2) return;
    const escaped = kw.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const regex = new RegExp(`\\b(${escaped})\\b`, 'gi');
    highlighted = highlighted.replace(regex, `<span class="vocab-highlight">$1</span>`);
  });

  return highlighted;
}

// 依據天數前後循環切換
function navigateWidgetDay(offset) {
  if (!allDialogues || allDialogues.length === 0 || !currentDialogue) return;

  const currentIndex = allDialogues.findIndex(d => d.id === currentDialogue.id);
  if (currentIndex === -1) return;

  let targetIndex = (currentIndex + offset) % allDialogues.length;
  if (targetIndex < 0) {
    targetIndex = allDialogues.length - 1;
  }

  renderWidgetDialogue(allDialogues[targetIndex].id);
}

// 綁定 UI 事件
function bindWidgetEvents() {
  // 前一天 / 後一天
  const prevBtn = document.getElementById('prev-day-btn');
  if (prevBtn) prevBtn.addEventListener('click', () => navigateWidgetDay(-1));

  const nextBtn = document.getElementById('next-day-btn');
  if (nextBtn) nextBtn.addEventListener('click', () => navigateWidgetDay(1));

  // 點擊今日返回今天
  const todayBtn = document.getElementById('today-day-btn');
  if (todayBtn) {
    todayBtn.addEventListener('click', () => {
      const todayMMDD = getTodayMMDD();
      const target = allDialogues.find(d => d.date === todayMMDD);
      if (target) renderWidgetDialogue(target.id);
    });
  }

  // 主播放按鈕
  const mainPlayBtn = document.getElementById('main-play-btn');
  if (mainPlayBtn) {
    mainPlayBtn.addEventListener('click', () => {
      if (window.dialoguePlayer) window.dialoguePlayer.togglePlay();
    });
  }

  // 倒退 / 快轉 5 秒
  const rewindBtn = document.getElementById('rewind-btn');
  if (rewindBtn) {
    rewindBtn.addEventListener('click', () => {
      if (window.dialoguePlayer) window.dialoguePlayer.seek(-5);
    });
  }

  const forwardBtn = document.getElementById('forward-btn');
  if (forwardBtn) {
    forwardBtn.addEventListener('click', () => {
      if (window.dialoguePlayer) window.dialoguePlayer.seek(5);
    });
  }

  // 倍速按鈕
  document.querySelectorAll('.speed-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const speed = parseFloat(btn.dataset.speed);
      if (window.dialoguePlayer) {
        window.dialoguePlayer.setPlaybackRate(speed);
      }
    });
  });

  // 收合 / 展開播放器
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
}
