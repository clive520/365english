# 每日對話練習 - GitHub Pages 發佈與學校網站整合指南

本專案採用**純前端靜態架構**，無須租用任何伺服器與資料庫，可直接免費託管於 **GitHub Pages**，並以最簡單的方式嵌入學校官方網站！

---

## 🚀 第一部分：上傳至 GitHub 並啟用免費網站（約 3 分鐘）

### 步驟 1：在 GitHub 建立新儲存庫 (Repository)
1. 登入您的 [GitHub 帳號](https://github.com/)。
2. 點擊右上角的 **「+」** 號，選擇 **「New repository」**。
3. **Repository name**：輸入專案名稱（建議輸入 `daily-english` 或 `365english`）。
4. 選擇 **Public**（公開，GitHub Pages 免費版需為公開倉庫）。
5. ⚠️ 下方的「Add a README file」**不要勾選**（因為本機已經建立好）。
6. 點擊綠色的 **「Create repository」** 按鈕。

---

### 步驟 2：將本機程式碼推送到 GitHub
打開您的終端機（PowerShell 或 CMD），在專案目錄下依序執行以下 3 行指令（請將 `<您的GitHub帳號>` 與 `<專案名稱>` 替換為您的實際名稱）：

```bash
git branch -M main
git remote add origin https://github.com/<您的GitHub帳號>/daily-english.git
git push -u origin main
```

*(提示：第一次 push 可能會跳出瀏覽器要求授權登入 GitHub，點擊授權確認即可)*

---

### 步驟 3：在 GitHub 開啟免費網站託管 (GitHub Pages)
1. 進入您剛建立的 GitHub 專案頁面。
2. 點擊上方的 **「Settings」**（齒輪圖示）。
3. 在左側選單中找到並點擊 **「Pages」**。
4. 在 **「Build and deployment」** 區塊：
   - **Source**：選擇 `Deploy from a branch`。
   - **Branch**：選擇 `main` 分支，後面的資料夾保持 `/ (root)`。
5. 點擊右側的 **「Save」** 按鈕。
6. 稍候約 **1 ~ 2 分鐘**，重新整理頁面，最上方會出現綠色勾勾，並顯示專屬網址：
   👉 **`https://<您的GitHub帳號>.github.io/daily-english/`**

---

## 🏫 第二部分：嵌入學校網站的三種方案

網站上線後，學校可以依照實際需求選擇以下任一種方式整合：

### 方案 A：直接以 `<iframe>` 嵌入學校官網頁面（最推薦、一體化體驗）
在學校網站後台編輯器（如英語教學專區、晨光自習專區）的 HTML 原始碼處貼上以下語法：

```html
<!-- 每日對話練習 嵌入代碼 -->
<div style="width: 100%; max-width: 1100px; margin: 0 auto;">
  <iframe 
    src="https://<您的GitHub帳號>.github.io/daily-english/" 
    style="width: 100%; height: 900px; border: none; border-radius: 18px; box-shadow: 0 6px 24px rgba(0,0,0,0.08);"
    title="每日對話練習 - 校園英語聽說平台"
    allow="microphone"
    loading="lazy">
  </iframe>
</div>
```
> **重要小叮嚀**：代碼中的 `allow="microphone"` 非常重要！它能讓學生在學校網站內直接使用「**🎤 錄音跟讀比對**」功能。

---

### 方案 B：於學校官網首頁放置「精美橫幅 Banner」
若希望首頁保持簡潔，點擊後以新分頁開啟全螢幕練習：

```html
<a href="https://<您的GitHub帳號>.github.io/daily-english/" 
   target="_blank" 
   rel="noopener noreferrer" 
   style="display: inline-flex; align-items: center; gap: 10px; background: linear-gradient(135deg, #f59e0b, #ea580c); color: #ffffff; padding: 12px 24px; border-radius: 999px; text-decoration: none; font-weight: bold; font-size: 1.15rem; box-shadow: 0 4px 14px rgba(245, 158, 11, 0.35);">
  <span>☀️</span>
  <span>進入「每日對話練習」英語學習平台</span>
  <span style="font-size: 0.9rem; opacity: 0.9;">➔</span>
</a>
```

---

### 方案 C：班級觸控電子白板專用捷徑
在教室大螢幕的瀏覽器中，將該網址加到「我的最愛」或設為桌面捷徑，上課時按快速鍵 **F11** 全螢幕顯示，再點選網頁右上角的 **「🔍 大字體模式」**，字體大、發音清晰，非常適合全班晨讀或課前 5 分鐘跟讀！

---

## ✍️ 第三部分：日後天天新增對話的 2 步驟 SOP

日後英語科老師想天天新增對話，完全不需要懂寫網頁，只要 2 步驟：

### 步驟 1：打開 `data/dialogues.json` 加入新文字
依照現有的格式複製一組對話貼上，寫入主題、句子與中文翻譯。

### 步驟 2：執行一鍵合成與推送指令
在終端機輸入：
```bash
python scripts/generate_audio.py
git add .
git commit -m "add: 新增每日對話教材"
git push
```
**系統會全自動為您：**
- 產生咬字清晰、語速平穩的美語 MP3 音檔。
- 自動標記每句話的起訖時間。
- 自動上傳更新到 GitHub Pages，學校網站即刻同步！
