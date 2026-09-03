# 每日對話練習 (Daily English Dialogue)

專為國小、國中至高中學生精心設計的校園英語日常聽說練習平台。
具備**活潑親切的卡片風格**、**0.75x~1.5x 變速自訂播放器**、**清晰美語母語發音 MP3**、**單句跟讀連動**與**自主錄音對比**功能。

---

## 🌟 平台特色

1. **每天三大核心要素**：
   - **對話主題**：結合校園社交、趣味生活、同儕互動、科技時事等生動話題。
   - **對話內容**：中英對照、生詞卡、實用句型，支援「隱藏中文」練英聽、「隱藏英文」練口譯。
   - **高音質對話 MP3**：採用微軟 Neural TTS 人聲合成，咬字清晰、語速平穩，可即時切換 **0.75x 慢速、1.0x 正常、1.25x 稍快、1.5x 挑戰**。
2. **直覺親切的視覺設計**：
   - 暖陽黃、薄荷綠、晴空藍等溫暖色彩，生動角色頭像與氣泡對話框。
   - 支援電腦、平板、智慧手機與教室觸控電子白板（內建「大字體模式」）。
3. **沉浸式口語練習**：
   - **單句點擊發音**：點擊對話中任一句，播放器立即精確跳轉朗讀。
   - **錄音跟讀對照**：學生可開啟麥克風錄製自己的聲音，即時播放對比母語發音。
4. **純靜態架構 (Zero Server Cost)**：
   - 支援直接以本機瀏覽器開啟 (`file://`) 或一鍵託管於 **GitHub Pages**。
   - 學校無須負擔伺服器租金與維護成本。

---

## 📂 專案架構目錄

```text
365english/
├── index.html              # 平台首頁（含播放器、對話泡泡、單字卡、學習錦囊）
├── css/
│   └── style.css           # 活潑童趣主題樣式表（含 RWD 響應式與電子白板模式）
├── js/
│   ├── app.js              # 應用程式邏輯（分級篩選、篇章切換、錄音對比）
│   ├── player.js           # 雙語變速播放器核心（變速、時間軸高亮、TTS備援）
│   └── data.js             # 預載對話資料庫（支援純靜態/離線載入）
├── data/
│   └── dialogues.json      # 每日對話資料原始檔 (JSON 格式)
├── audio/                  # 高音質 MP3 音訊儲存目錄
│   ├── dialogue-elem-01.mp3
│   ├── dialogue-elem-02.mp3
│   ├── dialogue-jun-01.mp3
│   └── dialogue-sen-01.mp3
├── scripts/
│   └── generate_audio.py   # 自動化語音合成與時間軸標記 Python 管線
└── README.md               # 專案說明書與學校整合指引
```

---

## 🚀 部署至 GitHub Pages 教學

1. **建立 GitHub 儲存庫**：
   - 登入 GitHub，建立一個公開儲存庫（例如命名為 `daily-english`）。
2. **上傳本專案檔案**：
   ```bash
   git init
   git add .
   git commit -m "feat: 建立每日對話練習平台首發版"
   git branch -M main
   git remote add origin https://github.com/<你的帳號>/daily-english.git
   git push -u origin main
   ```
3. **啟用 GitHub Pages**：
   - 進入儲存庫頁面點擊 **Settings** -> **Pages**。
   - 在 **Build and deployment** 下方的 **Source** 選擇 `Deploy from a branch`。
   - **Branch** 選擇 `main` 分支與 `/ (root)` 目錄，點擊 **Save**。
   👉 正式專屬網址：
   **https://clive520.github.io/365english/**

---

## 🏫 學校網站整合指南

### 方式一：直接以 `<iframe>` 嵌入學校網站頁面（最推薦）
在學校官網的英文科教學專區或晨光活動頁面貼上以下代碼：

```html
<iframe 
  src="https://clive520.github.io/365english/" 
  style="width: 100%; height: 850px; border: none; border-radius: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.08);"
  title="每日對話練習 - 英語學習平台"
  allow="microphone">
</iframe>
```
*(注意：`allow="microphone"` 可讓學生在學校網站內直接使用錄音跟讀功能)*

### 方式二：於學校首頁設立「每日對話練習」超連結橫幅
```html
<a href="https://clive520.github.io/365english/" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 8px; background: #f59e0b; color: #fff; padding: 10px 20px; border-radius: 999px; text-decoration: none; font-weight: bold; font-size: 1.1rem; box-shadow: 0 4px 12px rgba(245,158,11,0.3);">
  ☀️ 進入「每日對話練習」平台
</a>
```

---

## ✍️ 日常如何新增對話與合成 MP3

當老師或管理員想新增一則新對話時，只需簡單 2 個步驟：

### 步驟 1：編輯 `data/dialogues.json`
在陣列中加入新的對話物件，例如：
```json
{
  "id": "dialogue-elem-03",
  "date": "2026-09-05",
  "level": "elementary_basic",
  "levelName": "國小初階 (A1)",
  "levelBadgeColor": "#22c55e",
  "category": "美味食物",
  "topic": {
    "en": "Let's Make Pancakes!",
    "zh": "我們來做鬆餅吧！"
  },
  "situation": "週六早晨，哥哥和妹妹在廚房準備美味的早餐鬆餅。",
  "speakers": {
    "Tom": { "role": "哥哥 Tom", "avatar": "👦", "gender": "male" },
    "Lily": { "role": "妹妹 Lily", "avatar": "👧", "gender": "female" }
  },
  "dialogue": [
    { "id": 1, "speaker": "Tom", "avatar": "👦", "en": "Do we have eggs and milk in the fridge?", "zh": "冰箱裡有雞蛋和牛奶嗎？", "keywords": ["eggs", "milk"] },
    { "id": 2, "speaker": "Lily", "avatar": "👧", "en": "Yes, we do! And here is the sweet honey!", "zh": "有的！而且這裡還有甜甜的蜂蜜！", "keywords": ["sweet", "honey"] }
  ],
  "vocabulary": [
    { "word": "pancake", "phonetic": "/ˈpæn.keɪk/", "pos": "n.", "zh": "美式鬆餅、薄煎餅", "example": "I like warm pancakes with syrup." }
  ],
  "dailyPhrase": { "en": "Yes, we do!", "zh": "有的！（肯定簡答）" },
  "cultureTip": "在西方家庭，週末早餐吃鬆餅是全家人一起享受烹飪樂趣的溫馨傳統喔！"
}
```

### 步驟 2：執行自動語音合成腳本
在終端機執行：
```bash
python scripts/generate_audio.py
```
腳本將**全自動**：
1. 為新增對話合成咬字清楚、節奏穩定的男女聲 MP3 音檔存至 `audio/`。
2. 自動量測每句起始與結束秒數，精準寫回 `data/dialogues.json` 與 `js/data.js`。
3. 提交並 Push 到 GitHub，網站即可自動更新上線！
