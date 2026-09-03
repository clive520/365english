#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次建立 9 月份擴充對話 (09-09 至 09-30，共 22 篇)
涵蓋國小初階、國小中高、國中、高中的生活化主題。
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'dialogues.json')

NEW_DIALOGUES = [
  # 09-09 [國小初階]
  {
    "id": "dialogue-0909",
    "date": "09-09",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "色彩與美術",
    "topic": {
      "en": "My Favorite Rainbow Color",
      "zh": "我最喜歡的彩虹顏色"
    },
    "situation": "美術課上，Lucas 和 Ruby 正在用水彩畫彩虹，彼此分享最喜歡的顏色。",
    "speakers": {
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Ruby": { "role": "Ruby", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0909.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lucas", "avatar": "👦", "en": "Look at my rainbow! Which color do you like best?", "zh": "看我的彩虹！你最喜歡哪一個顏色？", "keywords": ["rainbow", "color"] },
      { "id": 2, "speaker": "Ruby", "avatar": "👧", "en": "I love bright yellow! It shines like the warm morning sun.", "zh": "我最愛亮黃色！它就像溫暖的晨陽一樣閃亮。", "keywords": ["bright", "shines"] },
      { "id": 3, "speaker": "Lucas", "avatar": "👦", "en": "My favorite is purple. Can you pass me the blue paint?", "zh": "我最喜歡紫色。你可以把藍色顏料遞給我嗎？", "keywords": ["purple", "paint"] },
      { "id": 4, "speaker": "Ruby", "avatar": "👧", "en": "Here you go! Mix blue and red, and you get purple!", "zh": "拿去吧！把藍色和紅色混在一起，就會變成紫色囉！", "keywords": ["mix"] },
      { "id": 5, "speaker": "Lucas", "avatar": "👦", "en": "Magic! Our rainbow painting looks amazing!", "zh": "太神奇了！我們的彩虹畫看起來棒極了！", "keywords": ["magic", "amazing"] }
    ],
    "vocabulary": [
      { "word": "rainbow", "phonetic": "/ˈreɪn.boʊ/", "pos": "n.", "zh": "彩虹", "example": "A colorful rainbow appeared after the rain." },
      { "word": "paint", "phonetic": "/peɪnt/", "pos": "n.", "zh": "顏料、油漆", "example": "We need more green paint." },
      { "word": "mix", "phonetic": "/mɪks/", "pos": "v.", "zh": "混合、調配", "example": "Mix yellow and blue to make green." }
    ],
    "dailyPhrase": { "en": "Here you go!", "zh": "拿去吧！給你！（遞東西給別人時最常用的親切說法）" },
    "cultureTip": "在美語教室中，當同學開口借文具，回答「Here you go!」或「Here you are!」是最自然有禮貌的表達方式。"
  },

  # 09-10 [國小中高]
  {
    "id": "dialogue-0910",
    "date": "09-10",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "校園生活",
    "topic": {
      "en": "The Lost and Found Box",
      "zh": "學務處失物招領箱奇遇"
    },
    "situation": "下課時間，Ben 弄丟了鉛筆盒，和班長 Tina 到學務處的大木箱尋找。",
    "speakers": {
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Tina": { "role": "Tina", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0910.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ben", "avatar": "👦", "en": "Oh no, Tina! I can't find my red dinosaur pencil box anywhere!", "zh": "糟糕了 Tina！我到處都找不到我的紅色恐龍鉛筆盒！", "keywords": ["dinosaur", "anywhere"] },
      { "id": 2, "speaker": "Tina", "avatar": "👧", "en": "Don't panic. Let's check the school lost and found box near the office.", "zh": "別慌張，我們去辦公室旁邊的學校失物招領箱找找看吧。", "keywords": ["panic", "lost and found"] },
      { "id": 3, "speaker": "Ben", "avatar": "👦", "en": "There are so many water bottles and jackets in here!", "zh": "這裡面有好多水壺和外套喔！", "keywords": ["jackets", "bottles"] },
      { "id": 4, "speaker": "Tina", "avatar": "👧", "en": "Wait, is this red zipper yours? Look at the dinosaur sticker!", "zh": "等等，這個紅色拉鍊是你的嗎？看上面的恐龍貼紙！", "keywords": ["zipper", "sticker"] },
      { "id": 5, "speaker": "Ben", "avatar": "👦", "en": "Yes, that's mine! What a relief! Thank you so much, Tina!", "zh": "沒錯，那就是我的！真是鬆了一大口氣！太感謝妳了 Tina！", "keywords": ["relief"] }
    ],
    "vocabulary": [
      { "word": "panic", "phonetic": "/ˈpæn.ɪk/", "pos": "v.", "zh": "驚慌、恐慌", "example": "Stay calm and don't panic." },
      { "word": "zipper", "phonetic": "/ˈzɪp.ɚ/", "pos": "n.", "zh": "拉鍊", "example": "The zipper on my jacket is stuck." },
      { "word": "relief", "phonetic": "/rɪˈliːf/", "pos": "n.", "zh": "寬心、如釋重負", "example": "It was a great relief to hear the good news." }
    ],
    "dailyPhrase": { "en": "What a relief!", "zh": "真是鬆了一口氣！謝天謝地！" },
    "cultureTip": "西方學校幾乎每所都有「Lost and Found」（失物招領區），學期末沒人認領的衣物常會清洗乾淨後捐贈給慈善機構喔！"
  },

  # 09-11 [國中挑戰]
  {
    "id": "dialogue-0911",
    "date": "09-11",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "同儕合作",
    "topic": {
      "en": "Group Project Headache",
      "zh": "分組報告的分工煩惱"
    },
    "situation": "歷史課分組討論時，Mark 與 Kelly 正在溝通專案報告的投影片製作與資料蒐集分工。",
    "speakers": {
      "Mark": { "role": "Mark", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Kelly": { "role": "Kelly", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0911.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mark", "avatar": "🧑", "en": "Kelly, our history presentation deadline is next Wednesday. We need to split the tasks.", "zh": "Kelly，我們歷史簡報的截止日是下週三，我們得好好分工了。", "keywords": ["deadline", "tasks"] },
      { "id": 2, "speaker": "Kelly", "avatar": "👧", "en": "I agree. How about I research the background information, and you design the slides?", "zh": "我同意。不然我來查背景資料，你負責設計投影片怎麼樣？", "keywords": ["research", "slides"] },
      { "id": 3, "speaker": "Mark", "avatar": "🧑", "en": "I'm good with slides, but who will be the main speaker during the presentation?", "zh": "做投影片我很拿手，但是發表時誰來當主要報告人呢？", "keywords": ["main speaker", "presentation"] },
      { "id": 4, "speaker": "Kelly", "avatar": "👧", "en": "Why don't we share the speaking time equally? Three minutes for each of us.", "zh": "我們平分上台時間如何？每個人講三分鐘。", "keywords": ["equally"] },
      { "id": 5, "speaker": "Mark", "avatar": "🧑", "en": "That takes the pressure off! Let's set up a shared document right now.", "zh": "這真減輕了不少壓力！我們現在就開個共享雲端文件吧。", "keywords": ["pressure", "shared document"] }
    ],
    "vocabulary": [
      { "word": "deadline", "phonetic": "/ˈded.laɪn/", "pos": "n.", "zh": "截止期限", "example": "We must submit the report before the deadline." },
      { "word": "equally", "phonetic": "/ˈiː.kwə.li/", "pos": "adv.", "zh": "平均地、平等地", "example": "They divided the prize money equally." },
      { "word": "pressure", "phonetic": "/ˈpreʃ.ɚ/", "pos": "n.", "zh": "壓力", "example": "Exercise helps release mental pressure." }
    ],
    "dailyPhrase": { "en": "That takes the pressure off!", "zh": "這真減輕了不少壓力！" },
    "cultureTip": "國外中學非常注重 Group Project（小組專案），老師評分時不只看成果，還會看同儕互評（Peer Evaluation）與團隊合作度！"
  },

  # 09-12 [高中進階]
  {
    "id": "dialogue-0912",
    "date": "09-12",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "身心健康",
    "topic": {
      "en": "Managing Screen Time and Digital Detox",
      "zh": "數位排毒與專注力管理"
    },
    "situation": "高中生 Ryan 與 Olivia 在自習室休息時，聊到手機社群軟體帶來的焦慮與螢幕使用時間過長的問題。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0912.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "🧑", "en": "Olivia, I checked my weekly screen time report today, and I was shocked. Six hours a day!", "zh": "Olivia，我今天看了每週螢幕使用時間報告，嚇了一大跳，每天居然有六個小時！", "keywords": ["screen time", "shocked"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👩", "en": "It's so easy to fall into endless scrolling on short videos without realizing how fast time flies.", "zh": "看短影音不知不覺就會一直往下滑，根本沒意識到時間過得有多快。", "keywords": ["endless scrolling", "time flies"] },
      { "id": 3, "speaker": "Ryan", "avatar": "🧑", "en": "Exactly. It completely shatters my attention span when I try to read academic articles.", "zh": "正是如此。每當我試圖靜下心讀學術長文時，注意力就被切得支離破碎。", "keywords": ["shatters", "attention span"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👩", "en": "I started practicing digital detox by putting my phone in another room after nine o'clock every evening.", "zh": "我開始嘗試數位排毒，每晚九點後就把手機放在別的房間。", "keywords": ["digital detox", "practicing"] },
      { "id": 5, "speaker": "Ryan", "avatar": "🧑", "en": "That takes discipline, but my mental clarity would definitely benefit from it. I'll give it a shot tonight.", "zh": "那真需要自律，但這絕對對我的思緒清晰有幫助。我今晚就來試試看。", "keywords": ["discipline", "mental clarity"] }
    ],
    "vocabulary": [
      { "word": "detox", "phonetic": "/ˈdiː.tɑːks/", "pos": "n.", "zh": "排毒、戒斷習慣", "example": "A digital detox helps restore focus." },
      { "word": "attention span", "phonetic": "/əˈten.ʃən spæn/", "pos": "n.", "zh": "專注力持續時間", "example": "Constant notifications shorten our attention span." },
      { "word": "discipline", "phonetic": "/ˈdɪs.ə.plɪn/", "pos": "n.", "zh": "自律、紀律", "example": "Success requires dedication and self-discipline." }
    ],
    "dailyPhrase": { "en": "I'll give it a shot.", "zh": "我來試試看吧！（面對新挑戰時的積極口語）" },
    "cultureTip": "現代英語中流行「Digital Detox（數位排毒）」，意思是在特定時間刻意遠離 3C 科技產品，重新專注於閱讀、睡眠與人際真實交流。"
  },

  # 09-13 [國小初階]
  {
    "id": "dialogue-0913",
    "date": "09-13",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "校園生活",
    "topic": {
      "en": "Let's Clean Up the Classroom!",
      "zh": "放學前的大掃除時間"
    },
    "situation": "週五放學鐘聲響起，Mia 和 Toby 一起分配打掃工作，準備乾淨過週末。",
    "speakers": {
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0913.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mia", "avatar": "👧", "en": "The final bell rang! Time to tidy up our classroom.", "zh": "放學鐘聲響了！該把我們的教室整理乾淨囉。", "keywords": ["tidy up", "classroom"] },
      { "id": 2, "speaker": "Toby", "avatar": "👦", "en": "I can sweep the floor with the big broom.", "zh": "我可以用大掃把來掃地板。", "keywords": ["sweep", "broom"] },
      { "id": 3, "speaker": "Mia", "avatar": "👧", "en": "Great! I will wipe the blackboards and align all the desks.", "zh": "太好了！我來擦黑板，並把所有桌子排整齊。", "keywords": ["wipe", "align"] },
      { "id": 4, "speaker": "Toby", "avatar": "👦", "en": "Don't forget to empty the paper recycling bin!", "zh": "別忘了去倒紙類回收桶喔！", "keywords": ["recycling bin"] },
      { "id": 5, "speaker": "Mia", "avatar": "👧", "en": "All done! Everything is sparkling clean. Have a great weekend!", "zh": "搞定囉！所有東西都閃閃發亮。祝你週末愉快！", "keywords": ["sparkling"] }
    ],
    "vocabulary": [
      { "word": "sweep", "phonetic": "/swiːp/", "pos": "v.", "zh": "打掃、清掃", "example": "Please sweep the kitchen floor." },
      { "word": "broom", "phonetic": "/bruːm/", "pos": "n.", "zh": "掃把、掃帚", "example": "Grab the broom from the corner." },
      { "word": "sparkling", "phonetic": "/ˈspɑːr.klɪŋ/", "pos": "adj.", "zh": "閃閃發亮的、潔淨的", "example": "The windows are sparkling clean." }
    ],
    "dailyPhrase": { "en": "Tidy up!", "zh": "收拾整理乾淨！" },
    "cultureTip": "日本與台灣學校由學生輪流打掃教室；而在歐美學校，教室多由專業 Custodian（校工人員）維護，但學生下課前仍需自律將個人桌面與椅子收拾整齊。"
  },

  # 09-14 [國中挑戰]
  {
    "id": "dialogue-0914",
    "date": "09-14",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "週末休閒",
    "topic": {
      "en": "Baking Cookies on Saturday",
      "zh": "週六下午烤巧克力餅乾"
    },
    "situation": "週六下午，姊弟倆 Sarah 和 Jake 在廚房按照食譜動手烘烤巧克力脆片餅乾。",
    "speakers": {
      "Sarah": { "role": "Sarah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Jake": { "role": "Jake", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0914.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sarah", "avatar": "👧", "en": "Jake, preheat the oven to 350 degrees while I measure the flour and butter.", "zh": "Jake，在我量麵粉和奶油時，請先把烤箱預熱到 350 度。", "keywords": ["preheat", "oven"] },
      { "id": 2, "speaker": "Jake", "avatar": "👦", "en": "Done! Can we add extra chocolate chips? The more, the merrier!", "zh": "弄好了！我們可以多加點巧克力豆嗎？越多越開心！", "keywords": ["chocolate chips", "merrier"] },
      { "id": 3, "speaker": "Sarah", "avatar": "👧", "en": "Sure, but mix the dough gently so the cookies stay soft and chewy.", "zh": "當然可以，但麵團要輕輕拌勻，餅乾烤出來才會鬆軟有嚼勁。", "keywords": ["dough", "chewy"] },
      { "id": 4, "speaker": "Jake", "avatar": "👦", "en": "The timer just beeped! Wow, the kitchen smells heavenly.", "zh": "計時器響了！哇，整個廚房聞起來簡直像天堂一樣香。", "keywords": ["heavenly", "timer"] },
      { "id": 5, "speaker": "Sarah", "avatar": "👧", "en": "Let them cool on the wire rack for five minutes before we take a bite.", "zh": "先讓它們在鐵網架上放涼五分鐘，我們再開動嚐嚐看吧。", "keywords": ["cool", "wire rack"] }
    ],
    "vocabulary": [
      { "word": "preheat", "phonetic": "/ˌpriːˈhiːt/", "pos": "v.", "zh": "預熱（烤箱）", "example": "Preheat the oven before baking." },
      { "word": "dough", "phonetic": "/doʊ/", "pos": "n.", "zh": "麵團", "example": "Knead the cookie dough carefully." },
      { "word": "chewy", "phonetic": "/ˈtʃuː.i/", "pos": "adj.", "zh": "有嚼勁的、軟糯的", "example": "I love freshly baked chewy cookies." }
    ],
    "dailyPhrase": { "en": "The more, the merrier!", "zh": "越多越好！越熱鬧越好！" },
    "cultureTip": "食譜中的「350 degrees」在美國通常指華氏 350°F（約攝氏 175°C），這是烘烤多數美式餅乾的黃金標準溫度。"
  },

  # 09-15 [國小中高]
  {
    "id": "dialogue-0915",
    "date": "09-15",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "戶外探險",
    "topic": {
      "en": "A Picnic and Flying Kites in the Park",
      "zh": "週末公園野餐與放風箏"
    },
    "situation": "週日陽光明媚，Leo 和媽媽在草地上鋪開野餐墊，微風徐徐正適合放風箏。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mom": { "role": "媽媽", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0915.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Mom, the sky is crystal clear today! Can we fly my eagle kite first?", "zh": "媽媽，今天天空好清澈喔！我們可以先放我的老鷹風箏嗎？", "keywords": ["crystal clear", "kite"] },
      { "id": 2, "speaker": "Mom", "avatar": "👩", "en": "Let's unpack our picnic blanket first. I packed egg sandwiches and juicy grapes.", "zh": "我們先把野餐墊鋪好，我準備了雞蛋三明治和多汁的葡萄。", "keywords": ["unpack", "blanket"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Yum! Feel that breeze? It's blowing toward the pond.", "zh": "太棒了！感受到微風了嗎？風正朝著池塘吹過去呢。", "keywords": ["breeze", "blowing"] },
      { "id": 4, "speaker": "Mom", "avatar": "👩", "en": "Hold the spool tightly and run against the wind!", "zh": "緊緊握住線軸，迎著風往前跑！", "keywords": ["tightly", "wind"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Look! It is soaring high above the tree tops! This is awesome!", "zh": "快看！它在樹梢上飛得好高喔！太酷了！", "keywords": ["soaring"] }
    ],
    "vocabulary": [
      { "word": "breeze", "phonetic": "/briːz/", "pos": "n.", "zh": "微風、和風", "example": "A cool breeze ruffled the leaves." },
      { "word": "soar", "phonetic": "/sɔːr/", "pos": "v.", "zh": "翱翔、高飛", "example": "The eagle soared into the clouds." },
      { "word": "tightly", "phonetic": "/ˈtaɪt.li/", "pos": "adv.", "zh": "緊緊地、堅固地", "example": "Hold my hand tightly across the street." }
    ],
    "dailyPhrase": { "en": "Crystal clear.", "zh": "非常清澈、一清二楚。" },
    "cultureTip": "放風箏（Kite Flying）是世界各地的傳統戶外活動。英文常說「Run against the wind」，意思是逆著風跑，風箏才能藉由空氣浮力順利升空。"
  },

  # 09-16 [國中挑戰]
  {
    "id": "dialogue-0916",
    "date": "09-16",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "圖書閱讀",
    "topic": {
      "en": "Borrowing Books from the Library",
      "zh": "在學校圖書館借奇幻小說"
    },
    "situation": "午休時間，Ethan 在圖書館尋找英語課外讀物，請圖書館志工同學 Zoe 推薦。",
    "speakers": {
      "Ethan": { "role": "Ethan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0916.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ethan", "avatar": "👦", "en": "Hi Zoe! I'm looking for a gripping fantasy novel for our book report. Any suggestions?", "zh": "嗨 Zoe！我在找一本扣人心弦的奇幻小說來寫讀書心得，有推薦的嗎？", "keywords": ["gripping", "fantasy"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "You should definitely read this one! It's about young wizards solving a palace riddle.", "zh": "你一定要讀這本！內容是關於年輕巫師解開王宮謎題的故事。", "keywords": ["wizards", "riddle"] },
      { "id": 3, "speaker": "Ethan", "avatar": "👦", "en": "Sounds thrilling! How long can I keep the book checked out?", "zh": "聽起來很刺激！這本書我可以借閱多久呢？", "keywords": ["thrilling", "checked out"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "The loan period is two weeks, and you can renew it online once if nobody reserves it.", "zh": "借期是兩週，如果沒人預約的話，你還可以在線上續借一次。", "keywords": ["loan period", "renew"] },
      { "id": 5, "speaker": "Ethan", "avatar": "👦", "en": "Awesome! I'll scan my student ID card at the front desk right now.", "zh": "太好了！我現在就去服務台刷學生證借書。", "keywords": ["scan"] }
    ],
    "vocabulary": [
      { "word": "gripping", "phonetic": "/ˈɡrɪp.ɪŋ/", "pos": "adj.", "zh": "扣人心弦的、引人入勝的", "example": "The detective novel was gripping." },
      { "word": "renew", "phonetic": "/rɪˈnuː/", "pos": "v.", "zh": "續借（圖書）、延期", "example": "Can I renew this book for another week?" },
      { "word": "thrilling", "phonetic": "/ˈθrɪl.ɪŋ/", "pos": "adj.", "zh": "令人興奮刺激的", "example": "The roller coaster ride was thrilling." }
    ],
    "dailyPhrase": { "en": "Any suggestions?", "zh": "有什麼好建議或推薦嗎？" },
    "cultureTip": "圖書館術語中，「check out」是借書，「return」是還書，「renew」是續借，逾期未還收取的罰款叫做「overdue fine」。"
  },

  # 09-17 [國小初階]
  {
    "id": "dialogue-0917",
    "date": "09-17",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "寵物世界",
    "topic": {
      "en": "What Pet Do You Want?",
      "zh": "你想養小貓還是金魚？"
    },
    "situation": "下課聊天時，Lily 和 Max 正在興奮地討論各自夢想中的家庭小寵物。",
    "speakers": {
      "Lily": { "role": "Lily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Max": { "role": "Max", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0917.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lily", "avatar": "👧", "en": "If you could adopt any pet, what would you choose?", "zh": "如果你能領養任何寵物，你會選什麼？", "keywords": ["adopt", "choose"] },
      { "id": 2, "speaker": "Max", "avatar": "👦", "en": "I want a ginger kitten! They are playful and purr so softly.", "zh": "我想要一隻橘色小貓！牠們愛玩又會輕輕發出咕嚕聲。", "keywords": ["kitten", "purr"] },
      { "id": 3, "speaker": "Lily", "avatar": "👧", "en": "Cats are lovely, but I prefer a bowl of shiny goldfish.", "zh": "貓咪好可愛，但我比較想要一缸閃閃發亮的金魚。", "keywords": ["goldfish", "shiny"] },
      { "id": 4, "speaker": "Max", "avatar": "👦", "en": "Why fish? You can't cuddle or hug a fish!", "zh": "為什麼是魚？你不能抱魚也不能摸魚耶！", "keywords": ["cuddle"] },
      { "id": 5, "speaker": "Lily", "avatar": "👧", "en": "Because watching them swim peacefully calms me down!", "zh": "因為看著牠們安靜游來游去，會讓我心情很平靜呀！", "keywords": ["peacefully", "calms"] }
    ],
    "vocabulary": [
      { "word": "kitten", "phonetic": "/ˈkɪt̬.ən/", "pos": "n.", "zh": "小貓咪", "example": "The little kitten drank warm milk." },
      { "word": "purr", "phonetic": "/pɝː/", "pos": "v.", "zh": "（貓咪）舒服發出呼嚕聲", "example": "The happy cat began to purr." },
      { "word": "cuddle", "phonetic": "/ˈkʌd.əl/", "pos": "v.", "zh": "摟抱、依偎擁抱", "example": "Children love to cuddle soft teddy bears." }
    ],
    "dailyPhrase": { "en": "Calm down.", "zh": "平靜下來、放輕鬆。" },
    "cultureTip": "在美語日常中，貓咪舒服時喉嚨發出的震動聲音叫做「purr」，這是貓咪感到安全、放鬆與滿足的標誌。"
  },

  # 09-18 [高中進階]
  {
    "id": "dialogue-0918",
    "date": "09-18",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "永續環保",
    "topic": {
      "en": "Fast Fashion vs. Sustainable Living",
      "zh": "快時尚與綠色永續生活思辨"
    },
    "situation": "公民論壇課前，高中生 Grace 和 Leo 就廉價快時尚成衣對環境資源造成的沉重代價展開探討。",
    "speakers": {
      "Grace": { "role": "Grace", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" },
      "Leo": { "role": "Leo", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0918.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Grace", "avatar": "👩", "en": "Leo, did you know that the fashion industry accounts for nearly ten percent of global carbon emissions?", "zh": "Leo，你知道時尚產業佔了全球將近百分之十的碳排放量嗎？", "keywords": ["carbon emissions", "fashion"] },
      { "id": 2, "speaker": "Leo", "avatar": "🧑", "en": "That statistic is eye-opening. Fast fashion makes trendy clothes cheap, but the environmental toll is devastating.", "zh": "那個數據真令人大開眼界。快時尚讓流行衣服變便宜，但環境代價卻極其慘重。", "keywords": ["statistic", "devastating"] },
      { "id": 3, "speaker": "Grace", "avatar": "👩", "en": "Exactly. Mountains of synthetic fabrics end up in landfills after being worn just a handful of times.", "zh": "沒錯，堆積如山的人造合成纖維衣服穿沒幾次就被丟進垃圾掩埋場。", "keywords": ["landfills", "synthetic"] },
      { "id": 4, "speaker": "Leo", "avatar": "🧑", "en": "I've started thrift shopping and purchasing quality basics that last for years instead of chasing micro-trends.", "zh": "我現在開始逛二手古著店，並且買耐穿好幾年有品質的基本款，不再盲目追逐短暫微潮流。", "keywords": ["thrift shopping", "micro-trends"] },
      { "id": 5, "speaker": "Grace", "avatar": "👩", "en": "Voting with our wallets is the most tangible way consumers can drive corporate accountability.", "zh": "用我們的荷包投票，正是消費者推動企業落實社會責任最切實有效的方式。", "keywords": ["accountability", "tangible"] }
    ],
    "vocabulary": [
      { "word": "emissions", "phonetic": "/iˈmɪʃ.ənz/", "pos": "n.", "zh": "氣體排放物", "example": "Electric cars produce zero tailpipe emissions." },
      { "word": "landfill", "phonetic": "/ˈlænd.fɪl/", "pos": "n.", "zh": "垃圾掩埋場", "example": "Plastic takes hundreds of years to decompose in a landfill." },
      { "word": "tangible", "phonetic": "/ˈtæn.dʒə.bəl/", "pos": "adj.", "zh": "切實可見的、實質的", "example": "We need tangible results, not just promises." }
    ],
    "dailyPhrase": { "en": "Vote with your wallet.", "zh": "用荷包投票（用消費選擇表達價值立場）" },
    "cultureTip": "「Vote with your wallet」是現代永續消費的核心口號，倡導消費者透過支持環保永續品牌，迫使高污染企業轉型。"
  },

  # 09-19 [國小中高]
  {
    "id": "dialogue-0919",
    "date": "09-19",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "科學探索",
    "topic": {
      "en": "The Science Fair Volcano",
      "zh": "自然科展的彩色小火山實驗"
    },
    "situation": "自然教室裡，Ken 和 Emma 正在用紙黏土做火山模型，準備進行小蘇打與檸檬酸的冒泡爆發實驗。",
    "speakers": {
      "Ken": { "role": "Ken", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0919.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ken", "avatar": "👦", "en": "Emma, is the clay volcano completely dry? The science fair starts this afternoon!", "zh": "Emma，黏土火山完全乾了嗎？科學展覽會今天下午就要開始了耶！", "keywords": ["clay", "science fair"] },
      { "id": 2, "speaker": "Emma", "avatar": "👧", "en": "Yes, rock solid! Now let's measure two spoons of baking soda and red food coloring.", "zh": "乾透了，硬得跟石頭一樣！現在我們來量兩匙小蘇打粉和紅色食用色素。", "keywords": ["baking soda", "coloring"] },
      { "id": 3, "speaker": "Ken", "avatar": "👦", "en": "Red food coloring will make the bubbling foam look like realistic molten lava!", "zh": "加紅色食用色素會讓冒出來的泡泡看起來超像真正的滾燙熔岩！", "keywords": ["molten lava", "foam"] },
      { "id": 4, "speaker": "Emma", "avatar": "👧", "en": "Ready? Pour the vinegar slowly into the crater.", "zh": "準備好了嗎？慢慢把醋倒進火山口裡面。", "keywords": ["vinegar", "crater"] },
      { "id": 5, "speaker": "Ken", "avatar": "👦", "en": "Whoa! Look at it fizz and erupt! Chemical reactions are super cool!", "zh": "哇！看它嘶嘶作響爆發出來了！化學反應真的超酷的！", "keywords": ["fizz", "erupt"] }
    ],
    "vocabulary": [
      { "word": "erupt", "phonetic": "/ɪˈrʌpt/", "pos": "v.", "zh": "（火山）爆發、噴發", "example": "The volcano erupted with smoke and ash." },
      { "word": "fizz", "phonetic": "/fɪz/", "pos": "v.", "zh": "嘶嘶作響冒泡", "example": "Soda fizzes when you open the can." },
      { "word": "crater", "phonetic": "/ˈkreɪ.t̬ɚ/", "pos": "n.", "zh": "火山口、坑洞", "example": "Steam rose from the volcanic crater." }
    ],
    "dailyPhrase": { "en": "Chemical reaction.", "zh": "化學反應（亦可比喻人與人之間擦出有趣的火花）" },
    "cultureTip": "「Baking Soda Volcano（小蘇打火山實驗）」是全美中小學最經典的科學展覽實驗（Science Fair Project），幾乎每個學生都親手做過！"
  },

  # 09-20 [國中挑戰]
  {
    "id": "dialogue-0920",
    "date": "09-20",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "美食日常",
    "topic": {
      "en": "Ordering at a Fast Food Counter",
      "zh": "美式速食店點餐與特製薯條"
    },
    "situation": "週五放學後，Jason 和同學 Eric 在速食店櫃檯排隊點餐。",
    "speakers": {
      "Jason": { "role": "Jason", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Cashier": { "role": "店員", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0920.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Cashier", "avatar": "👩", "en": "Welcome to Burger Hub! What can I get started for you today?", "zh": "歡迎光臨漢堡工坊！今天想為您準備點什麼呢？", "keywords": ["welcome", "order"] },
      { "id": 2, "speaker": "Jason", "avatar": "👦", "en": "Hi! Can I get a cheeseburger combo with curly fries and an iced lemon tea?", "zh": "您好！我要一份起司漢堡套餐，配螺旋脆薯和一杯冰檸檬茶。", "keywords": ["combo", "curly fries"] },
      { "id": 3, "speaker": "Cashier", "avatar": "👩", "en": "Certainly! Would you like to upgrade your drink to large for fifty cents?", "zh": "沒問題！飲料需要加五十美分升級成大杯嗎？", "keywords": ["upgrade", "large"] },
      { "id": 4, "speaker": "Jason", "avatar": "👦", "en": "No thank you, regular size is plenty. Also, could I have no pickles on the burger?", "zh": "不用了謝謝，中杯就很夠了。另外漢堡可以不要加酸黃瓜嗎？", "keywords": ["pickles", "regular"] },
      { "id": 5, "speaker": "Cashier", "avatar": "👩", "en": "Got it, no pickles. Will that be for here or to go?", "zh": "收到，不要酸黃瓜。請問內用還是外帶？", "keywords": ["for here", "to go"] }
    ],
    "vocabulary": [
      { "word": "combo", "phonetic": "/ˈkɑːm.boʊ/", "pos": "n.", "zh": "速食套餐", "example": "I ordered the chicken burger combo." },
      { "word": "pickle", "phonetic": "/ˈpɪk.əl/", "pos": "n.", "zh": "醃黃瓜、酸菜", "example": "Some people dislike sour pickles." },
      { "word": "upgrade", "phonetic": "/ʌpˈɡreɪd/", "pos": "v.", "zh": "升級、加大份量", "example": "You can upgrade to a larger size." }
    ],
    "dailyPhrase": { "en": "For here or to go?", "zh": "內用還是外帶？（出國旅行點餐最高頻實用句）" },
    "cultureTip": "在美語速食店點餐時，店員結帳前一定會問「For here or to go?」（內用或外帶）。若是外帶，店員會用牛皮紙袋幫你裝好喔！"
  },

  # 09-21 [國小初階]
  {
    "id": "dialogue-0921",
    "date": "09-21",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "趣味遊戲",
    "topic": {
      "en": "Playing Board Games on a Rainy Day",
      "zh": "下雨天的室內桌遊時光"
    },
    "situation": "週六外面下起傾盆大雨，Anna 和弟弟 Tim 決定在客廳地毯上玩大富翁擲骰子。",
    "speakers": {
      "Anna": { "role": "Anna", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Tim": { "role": "Tim", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0921.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Anna", "avatar": "👧", "en": "It is pouring outside! Let's play Monopoly on the living room rug.", "zh": "外面雨下得好大喔！我們在客廳地毯上玩大富翁吧。", "keywords": ["pouring", "Monopoly"] },
      { "id": 2, "speaker": "Tim", "avatar": "👦", "en": "Awesome! I choose the little silver race car token.", "zh": "好耶！我選銀色小賽車的代表棋子。", "keywords": ["token", "race car"] },
      { "id": 3, "speaker": "Anna", "avatar": "👧", "en": "Your turn first, Tim! Roll the two dice.", "zh": "換你先開始，Tim！擲那兩顆骰子吧。", "keywords": ["dice", "roll"] },
      { "id": 4, "speaker": "Tim", "avatar": "👦", "en": "Double sixes! Twelve steps forward! I land on Boardwalk!", "zh": "雙六！往前走十二步！我停在大道上了！", "keywords": ["double", "land on"] },
      { "id": 5, "speaker": "Anna", "avatar": "👧", "en": "Lucky roller! Playing board games beats a rainy afternoon anytime.", "zh": "真是手氣超好的幸運星！下雨天玩桌遊真是太棒了。", "keywords": ["lucky"] }
    ],
    "vocabulary": [
      { "word": "pour", "phonetic": "/pɔːr/", "pos": "v.", "zh": "傾瀉、下傾盆大雨", "example": "It started to pour on our way home." },
      { "word": "dice", "phonetic": "/daɪs/", "pos": "n.", "zh": "骰子（單複數同形）", "example": "Roll the dice to see who starts." },
      { "word": "token", "phonetic": "/ˈtoʊ.kən/", "pos": "n.", "zh": "（遊戲）棋子、代幣", "example": "Each player picks a distinct token." }
    ],
    "dailyPhrase": { "en": "It is pouring outside!", "zh": "外面正在下傾盆大雨！" },
    "cultureTip": "英文中下大雨除了「raining cats and dogs」，更口語生動的說法是「It's pouring!」（雨像用水倒的一樣）。"
  },

  # 09-22 [高中進階]
  {
    "id": "dialogue-0922",
    "date": "09-22",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "音樂與成長",
    "topic": {
      "en": "The Journey of Learning Acoustic Guitar",
      "zh": "學習彈木吉他的挫折與成就"
    },
    "situation": "吉他社下課後，高中生 Evan 向社長 Maya 請教如何克服壓封閉和弦時指尖劇痛的瓶頸。",
    "speakers": {
      "Evan": { "role": "Evan", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Maya": { "role": "Maya", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0922.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Evan", "avatar": "🧑", "en": "Maya, I'm genuinely struggling with the F chord. My fingertips hurt, and the strings buzz horribly.", "zh": "Maya，我真的被 F 和弦卡住了。我指尖痛得要命，琴弦還發出可怕的雜音。", "keywords": ["struggling", "buzz"] },
      { "id": 2, "speaker": "Maya", "avatar": "👩", "en": "Every beginner goes through that ordeal! Calluses take a couple of weeks to develop properly.", "zh": "每個初學者都經歷過那種折磨！指尖的厚繭需要兩三週才能長出來。", "keywords": ["ordeal", "calluses"] },
      { "id": 3, "speaker": "Evan", "avatar": "🧑", "en": "Sometimes it feels like my fingers simply aren't long enough to bar all six strings.", "zh": "有時候我覺得根本是我的手指不夠長，才壓不住整整六條琴弦。", "keywords": ["strings"] },
      { "id": 4, "speaker": "Maya", "avatar": "👩", "en": "It's all about leverage and wrist posture rather than pure brute strength. Try rolling your index finger slightly to the side.", "zh": "那靠的是槓桿支點和手腕姿勢，而不是用蠻力。試著把食指稍微側轉一點點壓弦。", "keywords": ["leverage", "posture"] },
      { "id": 5, "speaker": "Evan", "avatar": "🧑", "en": "Whoa, that sounds so much clearer! Muscle memory really is a game of patience.", "zh": "哇，聲音清脆多了！肌肉記憶果然是一場考驗耐心的遊戲。", "keywords": ["muscle memory", "patience"] }
    ],
    "vocabulary": [
      { "word": "callus", "phonetic": "/ˈkæl.əs/", "pos": "n.", "zh": "老繭、厚皮", "example": "Guitar players develop calluses on their fingertips." },
      { "word": "posture", "phonetic": "/ˈpɑːs.tʃɚ/", "pos": "n.", "zh": "姿勢、儀態", "example": "Good sitting posture prevents back pain." },
      { "word": "patience", "phonetic": "/ˈpeɪ.ʃəns/", "pos": "n.", "zh": "耐心、忍耐力", "example": "Mastering any craft demands endless patience." }
    ],
    "dailyPhrase": { "en": "Muscle memory.", "zh": "肌肉記憶（反覆練習形成的熟練身體反射）" },
    "cultureTip": "彈吉他按弦初期的疼痛被樂手戲稱為「Rites of Passage（必經成人禮）」，長出 calluses（厚繭）後按弦就會變得輕鬆自如。"
  },

  # 09-23 [國小中高]
  {
    "id": "dialogue-0923",
    "date": "09-23",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "大自然美景",
    "topic": {
      "en": "Autumn Leaves and Crispy Air",
      "zh": "秋天的落葉與微涼微風"
    },
    "situation": "九月下旬的清晨，Maya 和媽媽漫步在校園步道上，踩在金黃落葉上發出清脆沙沙聲。",
    "speakers": {
      "Maya": { "role": "Maya", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Mom": { "role": "媽媽", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0923.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Maya", "avatar": "👧", "en": "Mom, feel the chilly air this morning! Autumn is definitely here.", "zh": "媽媽，今天早晨空氣涼涼的！秋天真的來了耶。", "keywords": ["chilly", "autumn"] },
      { "id": 2, "speaker": "Mom", "avatar": "👩", "en": "Yes, notice how the maple leaves are transforming into amber and crimson?", "zh": "對呀，有注意到楓樹的葉子正悄悄轉變成琥珀金和深紅色了嗎？", "keywords": ["maple", "amber", "crimson"] },
      { "id": 3, "speaker": "Maya", "avatar": "👧", "en": "Listen to that crunch sound every time we step on the dry leaves!", "zh": "每次我們踩在乾枯落葉上時，聽那個卡滋卡滋的聲音！", "keywords": ["crunch"] },
      { "id": 4, "speaker": "Mom", "avatar": "👩", "en": "Let's collect five unique leaves to press inside your heavy art notebook.", "zh": "我們來挑五片造型獨特的落葉，夾進妳厚厚的美術筆記本做標本吧。", "keywords": ["collect", "notebook"] },
      { "id": 5, "speaker": "Maya", "avatar": "👧", "en": "I found a star-shaped golden leaf! Autumn is truly my favorite season.", "zh": "我找到一片星星形狀的金色楓葉！秋天真的是我最愛的季節。", "keywords": ["golden", "season"] }
    ],
    "vocabulary": [
      { "word": "chilly", "phonetic": "/ˈtʃɪl.i/", "pos": "adj.", "zh": "涼颼颼的、寒冷的", "example": "The morning breeze felt delightfully chilly." },
      { "word": "crunch", "phonetic": "/krʌntʃ/", "pos": "n./v.", "zh": "嘎吱作響聲、咬碎脆裂聲", "example": "Leaves crunched beneath our boots." },
      { "word": "crimson", "phonetic": "/ˈkrɪm.zən/", "pos": "adj./n.", "zh": "深紅色的、緋紅", "example": "The sunset bathed the sky in crimson." }
    ],
    "dailyPhrase": { "en": "Autumn is in the air.", "zh": "秋意漸濃（空氣中已嗅到秋天的氣息）" },
    "cultureTip": "在北美，秋天採集落葉壓製成書籤（Leaf Pressing）是深受小學生喜愛的自然人文美育活動。"
  },

  # 09-24 [國中挑戰]
  {
    "id": "dialogue-0924",
    "date": "09-24",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "校園運動",
    "topic": {
      "en": "Planning the School Relay Race",
      "zh": "校慶大隊接力的棒次戰術"
    },
    "situation": "體育課下課後，體育股長 Tyler 和同學 Chris 在跑道旁手握碼表討論大隊接力賽的棒次戰術。",
    "speakers": {
      "Tyler": { "role": "Tyler", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chris": { "role": "Chris", "avatar": "👦", "gender": "male", "voice": "en-US-ChristopherNeural" }
    },
    "audioSrc": "audio/dialogue-0924.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tyler", "avatar": "👦", "en": "Chris, Sports Day is next Friday! We need to finalize our four-by-one-hundred relay roster.", "zh": "Chris，運動會就在下週五了！我們得確定四乘一百接力賽的名單和棒次。", "keywords": ["relay", "roster"] },
      { "id": 2, "speaker": "Chris", "avatar": "👦", "en": "I think David should take the opening leg because his starting explosive burst is unmatched.", "zh": "我認為 David 應該跑第一棒，因為他的起跑爆發力無人能敵。", "keywords": ["explosive", "opening leg"] },
      { "id": 3, "speaker": "Tyler", "avatar": "👦", "en": "Agreed. And you have the best stamina on curves, so you'll anchor the third leg.", "zh": "贊成。而你在過彎處的耐力最好，所以你負責守住第三棒彎道。", "keywords": ["stamina", "curves"] },
      { "id": 4, "speaker": "Chris", "avatar": "👦", "en": "Sounds tactical! But smooth baton passing is what truly decides the champion.", "zh": "聽起來很有戰術！但傳接棒順不順才是真正決定冠軍的關鍵。", "keywords": ["baton", "champion"] },
      { "id": 5, "speaker": "Tyler", "avatar": "👦", "en": "Let's practice blind handoffs right after the final bell. Gold medal, here we come!", "zh": "放學鐘聲一響我們就來練盲傳接棒。金牌，我們來啦！", "keywords": ["handoffs", "gold medal"] }
    ],
    "vocabulary": [
      { "word": "relay", "phonetic": "/ˈriː.leɪ/", "pos": "n.", "zh": "接力賽跑", "example": "Our class won the 400-meter relay race." },
      { "word": "baton", "phonetic": "/bəˈtɑːn/", "pos": "n.", "zh": "（接力賽）接力棒", "example": "Never drop the baton during the exchange." },
      { "word": "stamina", "phonetic": "/ˈstæm.ə.nə/", "pos": "n.", "zh": "耐力、持久力", "example": "Long-distance runners need extraordinary stamina." }
    ],
    "dailyPhrase": { "en": "Gold medal, here we come!", "zh": "金牌，我們來啦！（鼓舞士氣的自信歡呼）" },
    "cultureTip": "接力賽中最後一棒壓軸跑者稱為「Anchor Leg」（錨棒），通常由全隊衝刺速度最快、心理素質最強的選手擔任。"
  },

  # 09-25 [國小初階]
  {
    "id": "dialogue-0925",
    "date": "09-25",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "日常生活技能",
    "topic": {
      "en": "Can You Teach Me to Tie My Shoes?",
      "zh": "你可以教我怎麼綁鞋帶嗎？"
    },
    "situation": "體育課換球鞋時，小一生 Sam 鞋帶鬆開了，三年級的大哥哥 Eric 耐心教他綁鞋帶方法。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Eric": { "role": "Eric", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0925.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Eric, my shoelaces came untied, and I keep tripping! Can you help?", "zh": "Eric，我的鞋帶鬆掉了，我一直被絆倒！你能幫我嗎？", "keywords": ["shoelaces", "tripping"] },
      { "id": 2, "speaker": "Eric", "avatar": "👦", "en": "Sure thing, Sam! I'll teach you the easy bunny ears trick.", "zh": "沒問題 Sam！我來教你超簡單的『兔子耳朵小口訣』。", "keywords": ["bunny ears", "trick"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Bunny ears? That sounds like fun! What do I do first?", "zh": "兔子耳朵？聽起來好好玩！我第一步要做什麼？", "keywords": ["fun"] },
      { "id": 4, "speaker": "Eric", "avatar": "👦", "en": "Cross the laces, pull tight, then make two loops like bunny ears and tie them together!", "zh": "把兩條鞋帶交叉拉緊，然後捏出兩個像兔子耳朵的小圈圈，綁在一起打個結！", "keywords": ["loops", "cross"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Look! A perfect double bow knot! I tied my shoes all by myself!", "zh": "你看！一個完美的蝴蝶結！我自己把鞋帶綁好啦！", "keywords": ["knot", "perfect"] }
    ],
    "vocabulary": [
      { "word": "shoelace", "phonetic": "/ˈʃuː.leɪs/", "pos": "n.", "zh": "鞋帶", "example": "Tie your shoelaces before running." },
      { "word": "loop", "phonetic": "/luːp/", "pos": "n.", "zh": "圈環、環狀圈", "example": "Make a small loop with the ribbon." },
      { "word": "knot", "phonetic": "/nɑːt/", "pos": "n.", "zh": "繩結、蝴蝶結", "example": "Pull the knot firmly so it won't slip." }
    ],
    "dailyPhrase": { "en": "Sure thing!", "zh": "當然沒問題！樂意效勞！" },
    "cultureTip": "歐美國家教幼童綁鞋帶最著名的兒歌口訣是「Bunny Ears Trick」（兔子耳朵法）：捏出兩隻兔耳朵、交叉鑽洞抱一抱，鞋帶就綁牢了！"
  },

  # 09-26 [高中進階]
  {
    "id": "dialogue-0926",
    "date": "09-26",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "生涯與職場",
    "topic": {
      "en": "First Job Interview and Money Habits",
      "zh": "第一份打工面試與理財觀"
    },
    "situation": "高中三年級的 Marcus 和 Bella 在咖啡廳喝飲料，交流週末到社區書店打工面試的經歷與金錢規劃。",
    "speakers": {
      "Marcus": { "role": "Marcus", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Bella": { "role": "Bella", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0926.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Marcus", "avatar": "🧑", "en": "Bella, I just passed my interview for a weekend barista position at the local bookstore!", "zh": "Bella，我剛通過社區書店週末咖啡師兼職的面試了！", "keywords": ["interview", "barista"] },
      { "id": 2, "speaker": "Bella", "avatar": "👩", "en": "Congratulations Marcus! What do you plan to do with your first paycheck?", "zh": "太恭喜你了 Marcus！拿到第一筆薪水你打算怎麼規劃？", "keywords": ["paycheck", "congratulations"] },
      { "id": 3, "speaker": "Marcus", "avatar": "🧑", "en": "My dad advised me to allocate fifty percent to my college savings fund, thirty percent for living expenses, and twenty for leisure.", "zh": "我爸爸建議我把百分之五十存入大學教育基金，三十用作生活開銷，剩下的二十當作娛樂。", "keywords": ["allocate", "savings"] },
      { "id": 4, "speaker": "Bella", "avatar": "👩", "en": "That's the classic 50-30-20 budget rule! Establishing financial literacy early prevents unnecessary impulse buying.", "zh": "那是經典的 50-30-20 預算法則！及早建立理財素養能避免衝動消費。", "keywords": ["financial literacy", "budget"] },
      { "id": 5, "speaker": "Marcus", "avatar": "🧑", "en": "Earning money with my own labor certainly makes me appreciate its true value much more.", "zh": "用自己的勞力賺錢，真的讓我更加體會到每一分錢的真正價值。", "keywords": ["labor", "value"] }
    ],
    "vocabulary": [
      { "word": "paycheck", "phonetic": "/ˈpeɪ.tʃek/", "pos": "n.", "zh": "薪資支票、薪水", "example": "She deposited her weekly paycheck in the bank." },
      { "word": "allocate", "phonetic": "/ˈæl.ə.keɪt/", "pos": "v.", "zh": "分配、劃撥（預算）", "example": "Allocate time wisely between study and rest." },
      { "word": "literacy", "phonetic": "/ˈlɪt̬.ɚ.ə.si/", "pos": "n.", "zh": "素養、知能、識字率", "example": "Financial literacy is essential for modern youths." }
    ],
    "dailyPhrase": { "en": "Impulse buying.", "zh": "衝動性購物、盲目消費。" },
    "cultureTip": "「The 50/30/20 Rule」是歐美著名理財法則：收入 50% 投入必要生活支出（Needs）、30% 彈性願望（Wants）、20% 儲蓄或投資（Savings）。"
  },

  # 09-27 [國小中高]
  {
    "id": "dialogue-0927",
    "date": "09-27",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "校園感恩",
    "topic": {
      "en": "A Secret Surprise Card for Teacher",
      "zh": "給老師的秘密驚喜卡片"
    },
    "situation": "教師節前一天放學，班長 Emma 召集全班同學在黑板前秘密手繪一張巨大的感恩愛心大卡片。",
    "speakers": {
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0927.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Emma", "avatar": "👧", "en": "Hurry, everyone! Mr. Clark is in the teachers' lounge, so we have fifteen minutes to sign this giant card!", "zh": "大家快點！Clark 老師在教師休息室，我們有十五分鐘可以在這張大卡片上簽名！", "keywords": ["surprise", "lounge"] },
      { "id": 2, "speaker": "Lucas", "avatar": "👦", "en": "I brought metallic glitter markers! Let's write 'Best English Teacher Ever' across the top banner.", "zh": "我帶了金屬亮粉馬克筆！我們在頂端橫幅寫上『史上最棒的英文老師』吧。", "keywords": ["glitter", "banner"] },
      { "id": 3, "speaker": "Emma", "avatar": "👧", "en": "Perfect! Leave enough space in the center so all thirty classmates can pen their gratitude.", "zh": "太棒了！中間要留出足夠的空間，讓全班三十位同學都能寫下感謝的心裡話。", "keywords": ["gratitude"] },
      { "id": 4, "speaker": "Lucas", "avatar": "👦", "en": "I'll draw a cartoon owl wearing graduation glasses in the corner.", "zh": "我會在角落畫一隻戴著學士眼鏡的可愛智慧貓頭鷹卡通圖案。", "keywords": ["cartoon", "glasses"] },
      { "id": 5, "speaker": "Emma", "avatar": "👧", "en": "Mr. Clark is going to be so touched tomorrow morning! Shh, someone is coming down the hallway!", "zh": "明天早自習老師一定會超級感動！噓，走廊那頭好像有人走過來了！", "keywords": ["touched", "hallway"] }
    ],
    "vocabulary": [
      { "word": "gratitude", "phonetic": "/ˈɡræt̬.ə.tuːd/", "pos": "n.", "zh": "感激、感恩之心", "example": "We express deep gratitude to our mentors." },
      { "word": "glitter", "phonetic": "/ˈɡlɪt̬.ɚ/", "pos": "n.", "zh": "閃光粉、金蔥", "example": "The craft card was covered in silver glitter." },
      { "word": "touched", "phonetic": "/tʌtʃt/", "pos": "adj.", "zh": "受感動的", "example": "She was deeply touched by their kindness." }
    ],
    "dailyPhrase": { "en": "Best teacher ever!", "zh": "史上最棒的老師！" },
    "cultureTip": "在台灣，9月28日是至聖先師孔子的誕辰紀念日，也是法定教師節（Teacher's Day）；在歐美，多數學校則會在五月第一週慶祝「Teacher Appreciation Week」。"
  },

  # 09-28 [國中挑戰]
  {
    "id": "dialogue-0928",
    "date": "09-28",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "感恩節慶",
    "topic": {
      "en": "Happy Teacher's Day!",
      "zh": "教師節快樂！感念師恩"
    },
    "situation": "9月28日教師節早自習，班長 Leo 與副班長 Zoe 在教室門口代表全班向班導師獻花與朗讀英文感謝卡。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Teacher": { "role": "林老師", "avatar": "👩‍🏫", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0928.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Attention class, please stand! Happy Teacher's Day, Ms. Lin!", "zh": "全班注意，起立！祝林老師教師節快樂！", "keywords": ["Happy Teacher's Day", "stand"] },
      { "id": 2, "speaker": "Teacher", "avatar": "👩‍🏫", "en": "Oh my goodness! What a magnificent bouquet of sunflowers! Thank you all so much!", "zh": "天啊！好大一束燦爛的向日葵！真的太謝謝大家了！", "keywords": ["magnificent", "bouquet"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Thank you for your infinite patience and for always encouraging us whenever we make mistakes.", "zh": "謝謝老師無限的耐心，每當我們犯錯時，您總是給予最溫暖的鼓勵與指引。", "keywords": ["patience", "encouraging"] },
      { "id": 4, "speaker": "Teacher", "avatar": "👩‍🏫", "en": "Seeing each of you grow and find your passion is the absolute greatest reward any teacher could ask for.", "zh": "看著你們每個人不斷進步、找到自己的熱情，就是身為老師最無可比擬的最高榮譽。", "keywords": ["reward", "passion"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "We promise to study hard and make you proud throughout the year!", "zh": "我們保證今年一定會全力以赴、認真學習，讓老師為我們感到驕傲！", "keywords": ["proud", "promise"] }
    ],
    "vocabulary": [
      { "word": "bouquet", "phonetic": "/boʊˈkeɪ/", "pos": "n.", "zh": "花束", "example": "He gave her a lovely bouquet of red roses." },
      { "word": "infinite", "phonetic": "/ˈɪn.fə.nət/", "pos": "adj.", "zh": "無限的、無窮盡的", "example": "Teaching requires infinite patience and love." },
      { "word": "reward", "phonetic": "/rɪˈwɔːrd/", "pos": "n.", "zh": "回報、獎勵、成果", "example": "Knowledge is its own greatest reward." }
    ],
    "dailyPhrase": { "en": "Make you proud.", "zh": "讓您感到驕傲與欣慰。" },
    "cultureTip": "教師節送向日葵（Sunflowers）寓意「沈默的愛、光明與希望」，象徵老師像溫暖陽光一般照耀指引學生茁壯成長。"
  },

  # 09-29 [國小初階]
  {
    "id": "dialogue-0929",
    "date": "09-29",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "天文夜空",
    "topic": {
      "en": "Star Gazing in the Backyard",
      "zh": "夜晚庭院抬頭數星星"
    },
    "situation": "涼爽的週日夜晚，妹妹 Lily 和哥哥 Toby 坐在庭院野餐椅上，抬頭觀察閃爍星空。",
    "speakers": {
      "Lily": { "role": "Lily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0929.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lily", "avatar": "👧", "en": "Toby, look up! The night sky is full of tiny twinkling diamonds!", "zh": "Toby，抬頭看！夜空中滿是閃爍的微小鑽石耶！", "keywords": ["twinkling", "diamonds"] },
      { "id": 2, "speaker": "Toby", "avatar": "👦", "en": "Those are stars millions of miles away! Can you spot the Big Dipper?", "zh": "那些都是好幾百萬英里外的恆星喔！妳能找到北斗七星嗎？", "keywords": ["Big Dipper", "spot"] },
      { "id": 3, "speaker": "Lily", "avatar": "👧", "en": "Is it the group that looks like a giant soup spoon?", "zh": "是長得像一支大湯匙的那組星星嗎？", "keywords": ["spoon", "group"] },
      { "id": 4, "speaker": "Toby", "avatar": "👦", "en": "Spot on! And if you follow the two pointer stars, they point straight to the North Star.", "zh": "完全正確！只要順著湯匙邊緣的兩顆指標星往外看，就會直直指向北極星。", "keywords": ["North Star", "pointer"] },
      { "id": 5, "speaker": "Lily", "avatar": "👧", "en": "I see it! It shines so steadily. The universe is truly magical.", "zh": "我看見了！它發出的光好平穩安靜喔。宇宙真的太不可思議了。", "keywords": ["universe", "magical"] }
    ],
    "vocabulary": [
      { "word": "twinkle", "phonetic": "/ˈtwɪŋ.kəl/", "pos": "v.", "zh": "閃爍、閃亮", "example": "Stars twinkle brightly in the crisp dark sky." },
      { "word": "universe", "phonetic": "/ˈjuː.nə.vɝːs/", "pos": "n.", "zh": "宇宙、萬物", "example": "The universe holds countless mysterious galaxies." },
      { "word": "spoon", "phonetic": "/spuːn/", "pos": "n.", "zh": "湯匙、匙子", "example": "The constellation resembles a giant spoon." }
    ],
    "dailyPhrase": { "en": "Spot on!", "zh": "完全正確！說得太準了！" },
    "cultureTip": "世界最知名的英語兒歌《Twinkle, Twinkle, Little Star》（小星星）寫於 1806 年，至今仍是全世界孩子探索夜空宇宙的第一首歌。"
  },

  # 09-30 [高中進階]
  {
    "id": "dialogue-0930",
    "date": "09-30",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "自我成長",
    "topic": {
      "en": "September Wrap-up and Goal Setting",
      "zh": "九月月結回顧與十月新目標"
    },
    "situation": "九月的最後一天放學後，高中好友 Henry 與 Claire 在操場看台回顧開學第一個月的學習節奏，並為即將到來的十月訂定具體目標。",
    "speakers": {
      "Henry": { "role": "Henry", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Claire": { "role": "Claire", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0930.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Henry", "avatar": "🧑", "en": "Can you believe September is already over, Claire? Time felt like a blur this month.", "zh": "Claire，妳敢相信九月居然已經過完了嗎？這個月時間過得像一陣風一樣快。", "keywords": ["blur", "September"] },
      { "id": 2, "speaker": "Claire", "avatar": "👩", "en": "I know! Transitioning into a heavier academic workload while balancing club duties was quite intense.", "zh": "真的！要適應更繁重的課業量，同時還要兼顧社團幹部職責，確實滿高壓緊湊的。", "keywords": ["workload", "intense"] },
      { "id": 3, "speaker": "Henry", "avatar": "🧑", "en": "How did you do with your daily English habit goal? Did you stick to practicing five minutes every morning?", "zh": "妳的每日英語好習慣目標進行得如何？有堅持每天早自習練習五分鐘嗎？", "keywords": ["habit", "practicing"] },
      { "id": 4, "speaker": "Claire", "avatar": "👩", "en": "I hit twenty-five days out of thirty! For October, I aim to add fifteen minutes of reading English editorials.", "zh": "三十天裡我做到了二十五天！十月份我的目標是每天再加十五分鐘閱讀英文社論。", "keywords": ["editorials", "aim"] },
      { "id": 5, "speaker": "Henry", "avatar": "🧑", "en": "Consistent small steps compound into extraordinary achievements. Let's keep this momentum going into October!", "zh": "堅持每天微小的一步，將會複利累積成驚人的成就。讓我們把這股動能延續到十月吧！", "keywords": ["momentum", "compound"] }
    ],
    "vocabulary": [
      { "word": "workload", "phonetic": "/ˈwɝːk.loʊd/", "pos": "n.", "zh": "工作量、課業負擔", "example": "Senior high students carry a substantial workload." },
      { "word": "compound", "phonetic": "/kɑːmˈpaʊnd/", "pos": "v.", "zh": "複利累積、加劇", "example": "Small daily habits compound over time into huge success." },
      { "word": "momentum", "phonetic": "/moʊˈmen.t̬əm/", "pos": "n.", "zh": "動能、氣勢、衝勁", "example": "Maintain momentum until your goals are achieved." }
    ],
    "dailyPhrase": { "en": "Keep the momentum going!", "zh": "保持這股衝勁！繼續堅持前進！" },
    "cultureTip": "心理學著名的「21/90 Rule」指出：建立一個新習慣需要 21 天，而堅持 90 天則會將其內化為終生受用的生活方式。"
  }
]

def main():
    if not os.path.exists(DATA_FILE):
        print("Data file not found.")
        return

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        existing = json.load(f)

    # 取得現有的 date 清單
    existing_dates = {item['date'] for item in existing}

    added_count = 0
    for new_item in NEW_DIALOGUES:
        if new_item['date'] not in existing_dates:
            existing.append(new_item)
            existing_dates.add(new_item['date'])
            added_count += 1

    # 按照 MM-DD 排序
    existing.sort(key=lambda x: x['date'])

    # 寫入 dialogues.json
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    # 寫入 js/data.js
    js_data_path = os.path.join(BASE_DIR, 'js', 'data.js')
    with open(js_data_path, 'w', encoding='utf-8') as f:
        f.write("// 預載每日對話資料庫（支援本地離線與 GitHub Pages 靜態環境）\n")
        f.write("window.DAILY_DIALOGUES = ")
        json.dump(existing, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    print(f"成功新增 {added_count} 篇對話！目前 9 月份總計共有 {len(existing)} 篇對話 (涵蓋 09-01 至 09-30)。")

if __name__ == '__main__':
    main()
