/**
 * 每日對話練習 - 自訂雙語變速音訊播放器
 * 支援 MP3 原音播放、語速切換 (0.75x~1.5x)、時間軸連動高亮、單句點擊發音與 Web Speech API 智能備援
 */
class DialoguePlayer {
  constructor() {
    this.audio = new Audio();
    this.currentDialogue = null;
    this.currentSentenceId = null;
    this.playbackRate = 1.0;
    this.isPlaying = false;
    this.isSingleSentenceMode = false;
    this.targetSentenceEnd = null;

    // Web Speech API 語音備援
    this.synth = window.speechSynthesis;
    this.useWebSpeech = false;
    this.availableVoices = [];

    this.initAudioListeners();
    this.initWebSpeech();
  }

  initAudioListeners() {
    this.audio.addEventListener('play', () => {
      this.isPlaying = true;
      this.updatePlayStateUI(true);
    });

    this.audio.addEventListener('pause', () => {
      this.isPlaying = false;
      this.updatePlayStateUI(false);
    });

    this.audio.addEventListener('ended', () => {
      this.isPlaying = false;
      this.updatePlayStateUI(false);
      this.clearHighlight();
    });

    this.audio.addEventListener('timeupdate', () => {
      if (!this.useWebSpeech) {
        const currentTime = this.audio.currentTime;
        this.updateProgressUI(currentTime, this.audio.duration || 1);
        this.syncSentenceHighlight(currentTime);

        // 若為單句播放模式，達到結束時間即自動暫停
        if (this.isSingleSentenceMode && this.targetSentenceEnd && currentTime >= this.targetSentenceEnd) {
          this.pause();
          this.isSingleSentenceMode = false;
          this.targetSentenceEnd = null;
        }
      }
    });

    this.audio.addEventListener('error', (e) => {
      console.warn('MP3 檔案尚未載入或路徑不存在，自動啟用 Web Speech 智慧語音朗讀備援。', e);
      this.useWebSpeech = true;
    });
  }

  initWebSpeech() {
    if ('speechSynthesis' in window) {
      const loadVoices = () => {
        this.availableVoices = this.synth.getVoices();
      };
      loadVoices();
      if (speechSynthesis.onvoiceschanged !== undefined) {
        speechSynthesis.onvoiceschanged = loadVoices;
      }
    }
  }

  loadDialogue(dialogueData) {
    this.stop();
    this.currentDialogue = dialogueData;
    this.currentSentenceId = null;
    this.isSingleSentenceMode = false;
    this.targetSentenceEnd = null;
    this.useWebSpeech = false;

    if (dialogueData.audioSrc) {
      this.audio.src = dialogueData.audioSrc;
      this.audio.playbackRate = this.playbackRate;
      this.audio.load();
    } else {
      this.useWebSpeech = true;
    }

    this.updateProgressUI(0, 1);
    this.clearHighlight();
  }

  togglePlay() {
    if (this.isPlaying) {
      this.pause();
    } else {
      this.play();
    }
  }

  play() {
    if (!this.currentDialogue) return;

    if (this.useWebSpeech) {
      this.playWithWebSpeechAll();
    } else {
      this.audio.playbackRate = this.playbackRate;
      const playPromise = this.audio.play();
      if (playPromise !== undefined) {
        playPromise.catch(() => {
          // 播放失敗（例如本機尚未產生 MP3），無縫切換到語音合成
          this.useWebSpeech = true;
          this.playWithWebSpeechAll();
        });
      }
    }
  }

  pause() {
    if (this.useWebSpeech) {
      if (this.synth) this.synth.cancel();
      this.isPlaying = false;
      this.updatePlayStateUI(false);
    } else {
      this.audio.pause();
    }
  }

  stop() {
    this.pause();
    if (!this.useWebSpeech) {
      this.audio.currentTime = 0;
    }
    this.clearHighlight();
    this.updateProgressUI(0, 1);
  }

  seek(seconds) {
    if (this.useWebSpeech) return;
    const newTime = Math.max(0, Math.min(this.audio.currentTime + seconds, this.audio.duration || 0));
    this.audio.currentTime = newTime;
  }

  seekToPercent(percent) {
    if (this.useWebSpeech || !this.audio.duration) return;
    this.audio.currentTime = this.audio.duration * percent;
  }

  setPlaybackRate(rate) {
    this.playbackRate = parseFloat(rate);
    this.audio.playbackRate = this.playbackRate;
    
    // 更新 UI 語速標記
    document.querySelectorAll('.speed-btn').forEach(btn => {
      const btnRate = parseFloat(btn.dataset.speed);
      if (Math.abs(btnRate - this.playbackRate) < 0.05) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });

    // 若正在使用 Web Speech，重新以新語速朗讀
    if (this.useWebSpeech && this.isPlaying) {
      if (this.currentSentenceId) {
        this.playSentence(this.currentSentenceId);
      } else {
        this.playWithWebSpeechAll();
      }
    }
  }

  playSentence(sentenceId) {
    if (!this.currentDialogue) return;
    const sentence = this.currentDialogue.dialogue.find(s => s.id === sentenceId);
    if (!sentence) return;

    this.currentSentenceId = sentenceId;
    this.highlightSentence(sentenceId);

    if (this.useWebSpeech) {
      this.speakText(sentence.en, sentence.speaker, () => {
        this.isPlaying = false;
        this.updatePlayStateUI(false);
      });
    } else {
      this.isSingleSentenceMode = true;
      this.targetSentenceEnd = sentence.endTime + 0.3; // 稍留餘裕
      this.audio.currentTime = sentence.startTime;
      this.audio.playbackRate = this.playbackRate;
      this.audio.play().catch(() => {
        this.useWebSpeech = true;
        this.playSentence(sentenceId);
      });
    }
  }

  // Web Speech API 整篇逐句朗讀
  playWithWebSpeechAll(startIndex = 0) {
    if (!('speechSynthesis' in window)) {
      alert('您的瀏覽器不支援 Web Speech API 語音合成。');
      return;
    }

    this.synth.cancel();
    const sentences = this.currentDialogue.dialogue;
    if (startIndex >= sentences.length) {
      this.isPlaying = false;
      this.updatePlayStateUI(false);
      this.clearHighlight();
      return;
    }

    this.isPlaying = true;
    this.updatePlayStateUI(true);

    const s = sentences[startIndex];
    this.highlightSentence(s.id);
    this.currentSentenceId = s.id;

    this.speakText(s.en, s.speaker, () => {
      if (this.isPlaying) {
        setTimeout(() => {
          this.playWithWebSpeechAll(startIndex + 1);
        }, 500); // 句與句之間自然停頓
      }
    });
  }

  speakText(text, speakerName, onEndCallback) {
    if (!('speechSynthesis' in window)) return;
    this.synth.cancel();

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en-US';
    utterance.rate = this.playbackRate;

    // 尋找自然美語人聲
    const isFemale = speakerName && ['Mia', 'Emily', 'Chloe', 'Teacher'].includes(speakerName);
    const voices = this.availableVoices.length ? this.availableVoices : this.synth.getVoices();
    const englishVoices = voices.filter(v => v.lang.startsWith('en'));

    if (englishVoices.length > 0) {
      if (isFemale) {
        utterance.voice = englishVoices.find(v => /female|zira|samantha|karen|jenny/i.test(v.name)) || englishVoices[0];
      } else {
        utterance.voice = englishVoices.find(v => /male|david|george|guy|alex/i.test(v.name)) || englishVoices[0];
      }
    }

    utterance.onend = () => {
      if (onEndCallback) onEndCallback();
    };

    utterance.onerror = () => {
      this.isPlaying = false;
      this.updatePlayStateUI(false);
    };

    this.isPlaying = true;
    this.updatePlayStateUI(true);
    this.synth.speak(utterance);
  }

  speakWord(word) {
    if (!('speechSynthesis' in window)) return;
    const utterance = new SpeechSynthesisUtterance(word);
    utterance.lang = 'en-US';
    utterance.rate = 0.85; // 單字以清晰慢速發音示範
    this.synth.speak(utterance);
  }

  syncSentenceHighlight(currentTime) {
    if (!this.currentDialogue) return;
    const sentence = this.currentDialogue.dialogue.find(s => 
      currentTime >= s.startTime && currentTime <= s.endTime + 0.2
    );

    if (sentence) {
      if (this.currentSentenceId !== sentence.id) {
        this.currentSentenceId = sentence.id;
        this.highlightSentence(sentence.id);
      }
    }
  }

  highlightSentence(sentenceId) {
    document.querySelectorAll('.sentence-bubble').forEach(el => {
      el.classList.remove('active-reading');
    });

    const activeEl = document.getElementById(`sentence-${sentenceId}`);
    if (activeEl) {
      activeEl.classList.add('active-reading');

      // 動態精確計算視窗安全區域（頂部避開導覽列，底部根據播放器實際高度自動避開）
      const rect = activeEl.getBoundingClientRect();
      const playerBar = document.getElementById('fixed-player-bar');
      const bottomOffset = playerBar ? playerBar.offsetHeight + 18 : 100;
      const topSafeBoundary = 75;
      const bottomSafeBoundary = window.innerHeight - bottomOffset;

      // 若句子被底部播放器遮擋或超出頂部，自動平滑滾動至視窗正中央
      if (rect.top < topSafeBoundary || rect.bottom > bottomSafeBoundary) {
        activeEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }
  }

  clearHighlight() {
    document.querySelectorAll('.sentence-bubble').forEach(el => {
      el.classList.remove('active-reading');
    });
  }

  updatePlayStateUI(isPlaying) {
    const playIcon = document.getElementById('play-icon');
    const pauseIcon = document.getElementById('pause-icon');
    const playBtn = document.getElementById('main-play-btn');

    if (playIcon && pauseIcon) {
      if (isPlaying) {
        playIcon.classList.add('hidden');
        pauseIcon.classList.remove('hidden');
        if (playBtn) playBtn.classList.add('pulse-playing');
      } else {
        playIcon.classList.remove('hidden');
        pauseIcon.classList.add('hidden');
        if (playBtn) playBtn.classList.remove('pulse-playing');
      }
    }
  }

  updateProgressUI(currentTime, duration) {
    const progressBar = document.getElementById('audio-progress');
    const currentTimeText = document.getElementById('current-time');
    const durationTimeText = document.getElementById('duration-time');

    if (progressBar && duration > 0) {
      const percent = (currentTime / duration) * 100;
      progressBar.value = percent;
      progressBar.style.background = `linear-gradient(to right, #f59e0b 0%, #f59e0b ${percent}%, #e2e8f0 ${percent}%, #e2e8f0 100%)`;
    }

    if (currentTimeText) {
      currentTimeText.textContent = this.formatTime(currentTime);
    }
    if (durationTimeText && !isNaN(duration) && duration > 0) {
      durationTimeText.textContent = this.formatTime(duration);
    }
  }

  formatTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
  }
}

// 建立全域播放器實例
window.dialoguePlayer = new DialoguePlayer();
