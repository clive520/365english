#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次建立 10 月份生活對話 (10-01 至 10-31，共 31 篇)
涵蓋國慶秋假、戶外露營、第一次段考、秋收採蘋果與萬聖節變裝狂歡！
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'dialogues.json')

OCTOBER_DIALOGUES = [
  # 10-01 [國小初階]
  {
    "id": "dialogue-1001",
    "date": "10-01",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "秋天水果",
    "topic": {
      "en": "Crispy Red Apples",
      "zh": "清脆甜美的水果紅蘋果"
    },
    "situation": "十月第一天，Toby 和妹妹 Zoe 在客廳享用剛洗好的新鮮紅蘋果。",
    "speakers": {
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1001.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Toby", "avatar": "👦", "en": "October is here! Look at this bowl of shiny red apples!", "zh": "十月到了！看這一大碗紅通通發亮的新鮮蘋果！", "keywords": ["October", "apples"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Yummy! Can you cut one into slices shaped like rabbits?", "zh": "好好吃的樣子！你可以切一片兔子造型的蘋果給我嗎？", "keywords": ["slices", "rabbits"] },
      { "id": 3, "speaker": "Toby", "avatar": "👦", "en": "Sure thing! Watch this: two little cuts make apple bunny ears!", "zh": "沒問題！看這個：輕輕切兩刀就變成兔子耳朵囉！", "keywords": ["cuts", "bunny"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "So cute! It's sweet, juicy, and super crunchy!", "zh": "好可愛喔！吃起來又甜、又多汁、超級脆！", "keywords": ["juicy", "crunchy"] },
      { "id": 5, "speaker": "Toby", "avatar": "👦", "en": "Fall apples are the absolute best fruit of the season!", "zh": "秋天的蘋果絕對是這個季節最棒的水果！", "keywords": ["fruit", "season"] }
    ],
    "vocabulary": [
      { "word": "slice", "phonetic": "/slaɪs/", "pos": "n.", "zh": "薄片、切片", "example": "Would you like a slice of apple?" },
      { "word": "crunchy", "phonetic": "/ˈkrʌn.tʃi/", "pos": "adj.", "zh": "爽脆的、鬆脆的", "example": "Fresh carrots are very crunchy." },
      { "word": "juicy", "phonetic": "/ˈdʒuː.si/", "pos": "adj.", "zh": "多汁美味的", "example": "The ripe peach was sweet and juicy." }
    ],
    "dailyPhrase": { "en": "Super crunchy!", "zh": "口感超級清脆！" },
    "cultureTip": "十月是歐美「Apple Picking（採蘋果）」的黃金產季，許多家庭會開車到果園採蘋果、喝現榨熱蘋果西打（Apple Cider）。"
  },

  # 10-02 [國小中高]
  {
    "id": "dialogue-1002",
    "date": "10-02",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "戶外休閒",
    "topic": {
      "en": "Setting Up the Campfire",
      "zh": "森林露營搭帳篷與營火"
    },
    "situation": "週末在山林營地，Lucas 和爸爸正在合力搭建露營帳篷與收集枯木生營火。",
    "speakers": {
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Dad": { "role": "爸爸", "avatar": "👨", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1002.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lucas", "avatar": "👦", "en": "Dad, I hammered all four metal stakes into the ground! The tent is sturdy.", "zh": "爸爸，四根金屬營釘我都敲進土裡了！帳篷搭得很穩固喔。", "keywords": ["hammered", "stakes", "tent"] },
      { "id": 2, "speaker": "Dad", "avatar": "👨", "en": "Fantastic job, Lucas! Now let's gather dry pinecones and twigs for our evening campfire.", "zh": "太棒了 Lucas！現在我們去撿些乾燥松果和細樹枝來生今晚的營火。", "keywords": ["pinecones", "campfire"] },
      { "id": 3, "speaker": "Lucas", "avatar": "👦", "en": "I brought a bag of giant marshmallows! Can we roast them on sticks?", "zh": "我帶了一大包大顆棉花糖！我們可以用長竹籤烤棉花糖嗎？", "keywords": ["marshmallows", "roast"] },
      { "id": 4, "speaker": "Dad", "avatar": "👨", "en": "Of course, we will make gooey s'mores with graham crackers and melted chocolate!", "zh": "當然可以，我們要用全麥餅乾夾融化的巧克力做牽絲棉花糖夾心餅！", "keywords": ["gooey", "s'mores"] },
      { "id": 5, "speaker": "Lucas", "avatar": "👦", "en": "Camping in October under the autumn stars is the ultimate weekend adventure!", "zh": "十月在秋夜星空下露營，真的是最頂級的週末冒險！", "keywords": ["adventure"] }
    ],
    "vocabulary": [
      { "word": "sturdy", "phonetic": "/ˈstɝː.di/", "pos": "adj.", "zh": "穩固的、堅實的", "example": "The wooden tent frame is very sturdy." },
      { "word": "roast", "phonetic": "/roʊst/", "pos": "v.", "zh": "烘烤（在火上）", "example": "We roasted marshmallows over the open fire." },
      { "word": "gooey", "phonetic": "/ˈɡuː.i/", "pos": "adj.", "zh": "軟糯黏稠的、牽絲的", "example": "Warm melted cheese is delightfully gooey." }
    ],
    "dailyPhrase": { "en": "Under the stars.", "zh": "在星空下（在戶外過夜的浪漫說法）" },
    "cultureTip": "「S'mores」是北美露營必吃靈魂甜點，名字來自「Some more」（再給我來一點！），用烤熱棉花糖夾進巧克力與餅乾中，融化牽絲極受歡迎。"
  },

  # 10-03 [國中挑戰]
  {
    "id": "dialogue-1003",
    "date": "10-03",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "考試準備",
    "topic": {
      "en": "Preparing for Midterm Exam Week",
      "zh": "第一次段考倒數衝刺"
    },
    "situation": "自習課上，Kevin 和好友 David 面對即將到來的第一次段考，討論彼此的複習時間表。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "🧑", "gender": "male", "voice": "en-US-ChristopherNeural" },
      "David": { "role": "David", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1003.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "🧑", "en": "David, midterm exams are barely ten days away! How is your review schedule holding up?", "zh": "David，離第一次段考只剩不到十天了！你的複習進度還跟得上嗎？", "keywords": ["midterm", "schedule"] },
      { "id": 2, "speaker": "David", "avatar": "👦", "en": "Math formulas are giving me a massive headache, especially quadratic equations.", "zh": "數學公式搞得我頭好痛，尤其是一元二次方程式。", "keywords": ["formulas", "equations"] },
      { "id": 3, "speaker": "Kevin", "avatar": "🧑", "en": "I made color-coded flashcards for formulas. Flashcards make active recall so much quicker.", "zh": "我為公式做了顏色分類的單字卡，抽卡能讓主動回想變得超快。", "keywords": ["flashcards", "recall"] },
      { "id": 4, "speaker": "David", "avatar": "👦", "en": "Brilliant strategy! Let's quiz each other for thirty minutes during study hall today.", "zh": "聰明的策略！我們今天自習課就抽問互相考對方三十分鐘吧。", "keywords": ["quiz", "strategy"] },
      { "id": 5, "speaker": "Kevin", "avatar": "🧑", "en": "Deal! Cramming the night before is exhausting, so consistent pacing wins the race.", "zh": "成交！考前熬夜死背太痛苦了，維持穩健節奏才是致勝之道。", "keywords": ["cramming", "pacing"] }
    ],
    "vocabulary": [
      { "word": "formula", "phonetic": "/ˈfɔːr.mjə.lə/", "pos": "n.", "zh": "公式、方程式", "example": "Memorize the area formula for triangles." },
      { "word": "cram", "phonetic": "/kræm/", "pos": "v.", "zh": "死記硬背、考前抱佛腳", "example": "Don't cram all night before the final test." },
      { "word": "strategy", "phonetic": "/ˈstræt̬.ə.dʒi/", "pos": "n.", "zh": "策略、作法", "example": "A smart study strategy saves valuable hours." }
    ],
    "dailyPhrase": { "en": "Active recall.", "zh": "主動回想記憶法（最高效的科學學習法）" },
    "cultureTip": "英文的「cram for an exam」就是中文的「考前臨時抱佛腳」，科學研究證實間隔重複（Spaced Repetition）遠比熬夜 cramming 更有利長期記憶。"
  },

  # 10-04 [高中進階]
  {
    "id": "dialogue-1004",
    "date": "10-04",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "科技生活",
    "topic": {
      "en": "Are Electric Vehicles Truly Zero-Emission?",
      "zh": "電動車真的百分之百零碳排嗎？"
    },
    "situation": "高二公民專題課後，Jason 和 Chloe 就電動車在全生命週期中的碳足跡與電池製造污染進行客觀思辨。",
    "speakers": {
      "Jason": { "role": "Jason", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1004.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Jason", "avatar": "🧑", "en": "Chloe, EV advertisements boast zero tailpipe emissions, but does that tell the whole environmental story?", "zh": "Chloe，電動車廣告都標榜零尾氣排放，但這真的反映了完整的環境真相嗎？", "keywords": ["advertisements", "emissions"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👩", "en": "Not entirely. If the power grid relies heavily on burning coal, an EV is essentially powered by fossil fuels.", "zh": "不全然。如果電網很大程度上依賴燃煤發電，電動車本質上依然是在消耗化石燃料。", "keywords": ["power grid", "fossil fuels"] },
      { "id": 3, "speaker": "Jason", "avatar": "🧑", "en": "Not to mention lithium and cobalt mining for batteries, which consumes vast water supplies and impacts local ecosystems.", "zh": "更別說開採電池所需的鋰和鈷礦，消耗龐大水資源且衝擊當地生態系。", "keywords": ["ecosystems", "mining"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👩", "en": "Yet studies show that over a full lifespan, EVs still produce significantly less net emissions than traditional gas-guzzlers.", "zh": "不過研究也顯示，就車輛全生命週期而言，電動車的淨排放量仍顯著低於傳統吃油怪獸燃油車。", "keywords": ["lifespan", "gas-guzzlers"] },
      { "id": 5, "speaker": "Jason", "avatar": "🧑", "en": "True. The long-term solution isn't just swapping motors, but accelerating renewable energy infrastructure worldwide.", "zh": "確實如此。長期解方不只是換個馬達，而是加速普及全球綠色再生能源基礎建設。", "keywords": ["renewable", "infrastructure"] }
    ],
    "vocabulary": [
      { "word": "infrastructure", "phonetic": "/ˈɪn.frəˌstrʌk.tʃɚ/", "pos": "n.", "zh": "基礎建設、公共設施", "example": "Investing in green infrastructure is critical." },
      { "word": "essentially", "phonetic": "/ɪˈsen.ʃəl.i/", "pos": "adv.", "zh": "本質上、基本上", "example": "The two proposals are essentially the same." },
      { "word": "accelerate", "phonetic": "/əkˈsel.ɚ.eɪt/", "pos": "v.", "zh": "加速、促進發展", "example": "Technological breakthroughs accelerate progress." }
    ],
    "dailyPhrase": { "en": "Gas-guzzler.", "zh": "耗油量極大的燃油車（吃油怪獸）" },
    "cultureTip": "「Cradle-to-Grave（從搖籃到墳墓）」是現代環境科學評估產品碳足跡（Lifecycle Assessment）的標準視角，評估製造、運輸到回收的全生命週期。"
  },

  # 10-05 [國小初階]
  {
    "id": "dialogue-1005",
    "date": "10-05",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "動物日常",
    "topic": {
      "en": "Squirrels Hiding Acorns",
      "zh": "小松鼠在樹下埋橡實"
    },
    "situation": "下課走過操場邊的大榕樹下，Mia 和 Leo 停下腳步觀察一隻忙碌的小松鼠。",
    "speakers": {
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1005.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mia", "avatar": "👧", "en": "Shh, Leo! Look at that chubby squirrel beside the oak tree!", "zh": "噓，Leo！看橡樹旁邊那隻圓滾滾的小松鼠！", "keywords": ["chubby", "squirrel"] },
      { "id": 2, "speaker": "Leo", "avatar": "👦", "en": "It has an acorn in its mouth! Its cheeks look like two puffy balloons.", "zh": "牠嘴裡叼著一顆橡實耶！兩邊臉頰鼓得像充氣氣球一樣。", "keywords": ["acorn", "cheeks"] },
      { "id": 3, "speaker": "Mia", "avatar": "👧", "en": "Now it's digging a tiny hole in the ground with its front paws!", "zh": "牠現在正用前爪在泥土裡挖一個小小的坑洞！", "keywords": ["digging", "paws"] },
      { "id": 4, "speaker": "Leo", "avatar": "👦", "en": "It's storing snacks for the chilly winter ahead.", "zh": "牠正在為即將到來的寒冬儲存點心呢。", "keywords": ["storing", "winter"] },
      { "id": 5, "speaker": "Mia", "avatar": "👧", "en": "Sometimes squirrels forget where they bury nuts, and those nuts grow into new trees!", "zh": "有時候松鼠會忘記把堅果埋在哪裡，那些堅果就會長成新樹木喔！", "keywords": ["bury", "grow"] }
    ],
    "vocabulary": [
      { "word": "acorn", "phonetic": "/ˈeɪ.kɔːrn/", "pos": "n.", "zh": "橡實、橡子", "example": "The squirrel buried an acorn in the moss." },
      { "word": "bury", "phonetic": "/ˈber.i/", "pos": "v.", "zh": "埋藏、埋入地下", "example": "Dogs love to bury bones in the garden." },
      { "word": "chubby", "phonetic": "/ˈtʃʌb.i/", "pos": "adj.", "zh": "圓滾滾的、胖嘟嘟的", "example": "The chubby kitten fell asleep in the basket." }
    ],
    "dailyPhrase": { "en": "Save for a rainy day.", "zh": "未雨綢繆、存錢以備不時之需。" },
    "cultureTip": "生態學家發現，松鼠埋藏堅果卻忘記挖出的行為，是溫帶森林自然繁衍再生（Seed Dispersal）極為關鍵的生態推手！"
  },

  # 10-06 [國小中高]
  {
    "id": "dialogue-1006",
    "date": "10-06",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "校園生活",
    "topic": {
      "en": "The Science Quiz Champion",
      "zh": "自然小考的搶答冠軍"
    },
    "situation": "自然課的分組競賽上，Sam 和 Emily 靠著默契合作在植物光合作用搶答賽中拿到滿分。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emily": { "role": "Emily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1006.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Emily, high five! Our team won first place in the biology quiz bowl!", "zh": "Emily，擊掌！我們隊在生物搶答競賽拿到了第一名！", "keywords": ["high five", "quiz bowl"] },
      { "id": 2, "speaker": "Emily", "avatar": "👧", "en": "You buzzed in so fast on that question about photosynthesis!", "zh": "關於光合作用的那一題，你按搶答鈴的速度真的太神速了！", "keywords": ["photosynthesis", "buzzed"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "I remembered the trick from our flashcards: plants inhale carbon dioxide and exhale oxygen.", "zh": "我想起了我們單字卡的口訣：植物吸入二氧化碳、吐出新鮮氧氣。", "keywords": ["oxygen", "carbon dioxide"] },
      { "id": 4, "speaker": "Emily", "avatar": "👧", "en": "Teacher awarded our team a golden bookmark ribbon as the prize.", "zh": "老師發給我們隊一條閃亮金色書籤緞帶作為優勝獎品耶。", "keywords": ["ribbon", "prize"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Teamwork makes the dream work! Let's celebrate with fruit popsicles.", "zh": "團隊合作讓夢想成真！我們去吃水果棒冰慶祝一下吧。", "keywords": ["teamwork", "celebrate"] }
    ],
    "vocabulary": [
      { "word": "photosynthesis", "phonetic": "/ˌfoʊ.t̬oʊˈsɪn.θə.sɪs/", "pos": "n.", "zh": "光合作用", "example": "Green plants need sunlight for photosynthesis." },
      { "word": "oxygen", "phonetic": "/ˈɑːk.sɪ.dʒən/", "pos": "n.", "zh": "氧氣", "example": "Humans and animals breathe oxygen." },
      { "word": "ribbon", "phonetic": "/ˈrɪb.ən/", "pos": "n.", "zh": "緞帶、彩帶", "example": "She tied a pink ribbon around the gift box." }
    ],
    "dailyPhrase": { "en": "Teamwork makes the dream work!", "zh": "團隊齊心，其利斷金！（歐美校園最經典勵志金句）" },
    "cultureTip": "「High five（擊掌）」是 1970 年代源自棒球場的慶祝手勢，伸開五指在空中大力拍擊，代表勝利與團隊默契。"
  },

  # 10-07 [國中挑戰]
  {
    "id": "dialogue-1007",
    "date": "10-07",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "天文常識",
    "topic": {
      "en": "Watching the Orionid Meteor Shower",
      "zh": "觀賞十月獵戶座流星雨"
    },
    "situation": "下課時間，Ethan 與天文愛好者同學 Zoe 在教室走廊討論十月中旬即將登場的獵戶座流星雨觀星行程。",
    "speakers": {
      "Ethan": { "role": "Ethan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1007.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ethan", "avatar": "👦", "en": "Zoe, did you read the astronomy club announcement about the Orionid meteor shower?", "zh": "Zoe，妳有看天文社關於獵戶座流星雨的最新公告嗎？", "keywords": ["astronomy", "meteor shower"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Yes! The peak activity happens later this month, with up to twenty shooting stars per hour!", "zh": "有！極大期就落在這個月中旬，估計每小時可見多達二十顆流星！", "keywords": ["shooting stars", "peak"] },
      { "id": 3, "speaker": "Ethan", "avatar": "👦", "en": "Do we need an expensive telescope, or can we observe them with our naked eyes?", "zh": "我們需要昂貴的望遠鏡嗎？還是用肉眼就能直接看呢？", "keywords": ["telescope", "naked eyes"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Naked eyes are actually superior because meteors streak rapidly across a wide field of view.", "zh": "肉眼其實更好！因為流星瞬間劃過夜空的視野範圍非常寬廣。", "keywords": ["superior", "streak"] },
      { "id": 5, "speaker": "Ethan", "avatar": "👦", "en": "Let's bring a warm thermos of cocoa to the countryside hill. I can't wait to make a wish!", "zh": "那我們帶個裝滿熱可可的保溫瓶去郊外小山丘吧，我等不及想許願了！", "keywords": ["thermos", "wish"] }
    ],
    "vocabulary": [
      { "word": "meteor", "phonetic": "/ˈmiː.t̬i.ɔːr/", "pos": "n.", "zh": "流星、隕石", "example": "A brilliant meteor flashed through the midnight sky." },
      { "word": "telescope", "phonetic": "/ˈtel.ə.skoʊp/", "pos": "n.", "zh": "望遠鏡", "example": "We observed Saturn's rings through the telescope." },
      { "word": "thermos", "phonetic": "/ˈθɝː.məs/", "pos": "n.", "zh": "保溫瓶、保溫杯", "example": "Fill the thermos with steaming hot soup." }
    ],
    "dailyPhrase": { "en": "With the naked eye.", "zh": "用肉眼（未藉助望遠鏡或顯微鏡）" },
    "cultureTip": "獵戶座流星雨（Orionids）是由著名的哈雷彗星（Halley's Comet）殘留碎片進入地球大氣層燃燒所產生的年度天文盛事。"
  },

  # 10-08 [高中進階]
  {
    "id": "dialogue-1008",
    "date": "10-08",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "哲學思辨",
    "topic": {
      "en": "Is Failure Really the Mother of Success?",
      "zh": "失敗真的是成功之母嗎？"
    },
    "situation": "高中模擬考成績公佈後，Alex 感到些許沮喪，好友 Sophia 藉由成長型思維與他深入對談失敗的真諦。",
    "speakers": {
      "Alex": { "role": "Alex", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Sophia": { "role": "Sophia", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1008.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Alex", "avatar": "🧑", "en": "Sophia, people always say 'failure is the mother of success', but right now, bombing this mock exam just feels devastating.", "zh": "Sophia，大家總說『失敗為成功之母』，但現在模考考砸了，只覺得充滿挫敗感。", "keywords": ["failure", "devastating"] },
      { "id": 2, "speaker": "Sophia", "avatar": "👩", "en": "Your feelings are valid, Alex. Failure alone doesn't guarantee growth; intentional reflection is the real catalyst.", "zh": "你的沮喪完全正常 Alex。光是經歷失敗並不能保證成長，刻意的反思才是真正的催化劑。", "keywords": ["reflection", "catalyst"] },
      { "id": 3, "speaker": "Alex", "avatar": "🧑", "en": "So you mean without analyzing what went wrong, repeating the same blind mistakes leads nowhere?", "zh": "所以妳的意思是，如果不剖析問題出在哪裡，盲目重複同樣的錯誤根本無濟於事？", "keywords": ["analyzing", "mistakes"] },
      { "id": 4, "speaker": "Sophia", "avatar": "👩", "en": "Precisely. Carol Dweck's growth mindset research shows that treating errors as diagnostic data separates achievers from quitters.", "zh": "正是如此。Carol Dweck 的成長型心態研究表明，把失誤視為診斷數據的人，才能真正突破極限走向卓越。", "keywords": ["growth mindset", "diagnostic"] },
      { "id": 5, "speaker": "Alex", "avatar": "🧑", "en": "That shifts my whole perspective. Instead of dwelling on the score, I'll dissect every incorrect problem tonight.", "zh": "這徹底扭轉了我的視角。與其沉溺在分數的沮喪中，我今晚就來逐題剖析錯題本！", "keywords": ["perspective", "dissect"] }
    ],
    "vocabulary": [
      { "word": "reflection", "phonetic": "/rɪˈflek.ʃən/", "pos": "n.", "zh": "深思、自省、反思", "example": "Quiet reflection promotes personal maturity." },
      { "word": "diagnostic", "phonetic": "/ˌdaɪ.əɡˈnɑː.stɪk/", "pos": "adj.", "zh": "診斷的、判斷病徵的", "example": "Diagnostic tests help identify knowledge gaps." },
      { "word": "dissect", "phonetic": "/daɪˈsekt/", "pos": "v.", "zh": "剖析、細部解剖分析", "example": "Let's dissect the root cause of the error." }
    ],
    "dailyPhrase": { "en": "Growth mindset.", "zh": "成長型思維（相信能力可透過刻意練習持續進步）" },
    "cultureTip": "史丹佛大學心理學教授 Carol Dweck 提出的「Growth Mindset（成長心態）」，強調大腦神經可塑性，將挫折視為學習的契機而非智商的定論。"
  },

  # 10-09 [國小初階]
  {
    "id": "dialogue-1009",
    "date": "10-09",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "生活常識",
    "topic": {
      "en": "Putting on a Cozy Sweater",
      "zh": "天氣變涼穿上毛衣"
    },
    "situation": "早晨出門前，媽媽提醒 Ruby 外面颳起秋風，要套上一件保暖的軟毛衣。",
    "speakers": {
      "Ruby": { "role": "Ruby", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Mom": { "role": "媽媽", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1009.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mom", "avatar": "👩", "en": "Ruby, the temperature dropped overnight! Put on your cozy knit sweater before school.", "zh": "Ruby，昨晚氣溫突然驟降了！上學前先把妳那件暖和的針織毛衣穿上。", "keywords": ["sweater", "temperature"] },
      { "id": 2, "speaker": "Ruby", "avatar": "👧", "en": "Is it the fluffy navy blue one with wooden buttons?", "zh": "是那件有木質鈕扣、毛茸茸的深藍色毛衣嗎？", "keywords": ["buttons", "fluffy"] },
      { "id": 3, "speaker": "Mom", "avatar": "👩", "en": "Yes! It keeps the cold wind from chilling your chest.", "zh": "是的！它可以擋住冷風，不讓胸口受涼。", "keywords": ["chilling", "wind"] },
      { "id": 4, "speaker": "Ruby", "avatar": "👧", "en": "It feels so soft and warm, like receiving a giant bear hug!", "zh": "摸起來好柔軟好暖和喔，就像被大熊緊緊擁抱一樣！", "keywords": ["hug", "soft"] },
      { "id": 5, "speaker": "Mom", "avatar": "👩", "en": "Zip your backpack, and don't forget your warm scarf. Have a wonderful day!", "zh": "拉好書包拉鍊，也別忘了圍上保暖圍巾。祝妳有美好的一天！", "keywords": ["scarf", "wonderful"] }
    ],
    "vocabulary": [
      { "word": "sweater", "phonetic": "/ˈswet̬.ɚ/", "pos": "n.", "zh": "毛衣、針織衫", "example": "Grandma knitted a cozy wool sweater." },
      { "word": "scarf", "phonetic": "/skɑːrf/", "pos": "n.", "zh": "圍巾、披巾", "example": "Wrap a thick scarf around your neck." },
      { "word": "button", "phonetic": "/ˈbʌt̬.ən/", "pos": "n.", "zh": "鈕扣、按鈕", "example": "She fastened the top coat button." }
    ],
    "dailyPhrase": { "en": "A bear hug.", "zh": "熱情大大的緊緊擁抱" },
    "cultureTip": "十月進入歐美的「Sweater Weather（毛衣季）」，這是一個帶有溫馨浪漫氣息的詞彙，象徵著南瓜香料拿鐵、落葉與溫暖針織衣物的季節。"
  },

  # 10-10 [國小中高]
  {
    "id": "dialogue-1010",
    "date": "10-10",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "節慶假期",
    "topic": {
      "en": "Fireworks in the Night Sky",
      "zh": "國慶假期的燦爛夜空煙火"
    },
    "situation": "國慶假日的河濱公園看台上，Tina 和 Ben 滿懷期待地等待倒數計時後的煙火秀。",
    "speakers": {
      "Tina": { "role": "Tina", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1010.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tina", "avatar": "👧", "en": "Ben, look at the countdown clock on the river stage! Ten seconds left!", "zh": "Ben，看河岸舞台上的倒數大時鐘！只剩十秒鐘了！", "keywords": ["countdown", "stage"] },
      { "id": 2, "speaker": "Ben", "avatar": "👦", "en": "Three, two, one... Happy holiday! Wow, boom!", "zh": "三、二、一…節日快樂！哇，磅！", "keywords": ["holiday", "boom"] },
      { "id": 3, "speaker": "Tina", "avatar": "👧", "en": "Look at that golden waterfall cascade! It lights up the entire river surface!", "zh": "看那個金色瀑布煙火傾瀉而下！把整個河面都照耀得通亮！", "keywords": ["waterfall", "surface"] },
      { "id": 4, "speaker": "Ben", "avatar": "👦", "en": "And now purple peony flowers blooming high above the bridge pillars!", "zh": "現在橋墩上方綻放出一朵朵紫色的牡丹煙火花朵！", "keywords": ["blooming", "pillars"] },
      { "id": 5, "speaker": "Tina", "avatar": "👧", "en": "The sparkling reflections in the water are absolutely breathtaking. What a grand show!", "zh": "水中閃爍的倒影真的美到令人窒息。太精彩壯觀的煙火秀了！", "keywords": ["reflections", "grand"] }
    ],
    "vocabulary": [
      { "word": "cascade", "phonetic": "/kæsˈkeɪd/", "pos": "n./v.", "zh": "如瀑布般傾瀉", "example": "Water cascaded gently over the polished rocks." },
      { "word": "reflection", "phonetic": "/rɪˈflek.ʃən/", "pos": "n.", "zh": "水中倒影、鏡像", "example": "Her reflection appeared in the tranquil lake." },
      { "word": "grand", "phonetic": "/ɡrænd/", "pos": "adj.", "zh": "宏偉盛大的、壯麗的", "example": "The stadium hosted a grand opening ceremony." }
    ],
    "dailyPhrase": { "en": "Light up the sky.", "zh": "照亮夜空、大放異彩。" },
    "cultureTip": "煙火藝術（Pyrotechnics）中不同金屬鹽類會產生不同顏色：鍶（Strontium）顯紅色、鋇（Barium）顯綠色、銅（Copper）顯藍色，非常具科學美感！"
  },

  # 10-11 [國中挑戰]
  {
    "id": "dialogue-1011",
    "date": "10-11",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "同儕生活",
    "topic": {
      "en": "Forming an English Study Group",
      "zh": "組成英語自習讀書會"
    },
    "situation": "放學後在速食店安靜角，Kelly 和 Mark 正在起草「段考互助讀書小組」的每週複習進度。",
    "speakers": {
      "Kelly": { "role": "Kelly", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Mark": { "role": "Mark", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1011.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kelly", "avatar": "👧", "en": "Mark, studying alone in my bedroom often makes me procrastinate and check my phone.", "zh": "Mark，自己一個人在房間讀書很容易拖延，忍不住一直看手機。", "keywords": ["procrastinate", "bedroom"] },
      { "id": 2, "speaker": "Mark", "avatar": "🧑", "en": "Same here. That's why peer accountability works wonders. Should we form a study group with four classmates?", "zh": "我也一樣。這就是為什麼同儕督促機制超級神效。我們要找四位同學組個讀書會嗎？", "keywords": ["accountability", "wonders"] },
      { "id": 3, "speaker": "Kelly", "avatar": "👧", "en": "Great idea! We can adopt the Pomodoro Technique: twenty-five minutes of deep focus followed by five minutes of break.", "zh": "好主意！我們可以用番茄鐘工作法：二十五分鐘高度專注，接著休息五分鐘。", "keywords": ["Pomodoro", "focus"] },
      { "id": 4, "speaker": "Mark", "avatar": "🧑", "en": "During the five-minute break, we can quiz each other on vocabulary flashcards.", "zh": "在五分鐘休息時間，我們還可以互相抽考單字卡。", "keywords": ["vocabulary"] },
      { "id": 5, "speaker": "Kelly", "avatar": "👧", "en": "Structure creates productivity! Let's schedule our first session this Thursday afternoon.", "zh": "良好的架構帶來超高效率！我們就約這週四下午展開第一場讀書會吧。", "keywords": ["productivity", "structure"] }
    ],
    "vocabulary": [
      { "word": "procrastinate", "phonetic": "/proʊˈkræs.tə.neɪt/", "pos": "v.", "zh": "拖延、拖拉", "example": "Don't procrastinate until the final evening." },
      { "word": "productivity", "phonetic": "/ˌproʊ.dʌkˈtɪv.ə.t̬i/", "pos": "n.", "zh": "生產力、學習工作效率", "example": "Morning hours often yield the highest productivity." },
      { "word": "accountability", "phonetic": "/əˌkaʊn.t̬əˈbɪl.ə.t̬i/", "pos": "n.", "zh": "責任擔當、互助督促", "example": "A study partner provides helpful accountability." }
    ],
    "dailyPhrase": { "en": "Work wonders.", "zh": "產生奇效、成果驚人！" },
    "cultureTip": "「Pomodoro Technique（番茄工作法）」由 Francesco Cirillo 於 1980 年代發明，以廚房番茄造型定時器命名，已被全球教育界推崇為專注力管理利器。"
  },

  # 10-12 [高中進階]
  {
    "id": "dialogue-1012",
    "date": "10-12",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "社群文化",
    "topic": {
      "en": "The Psychology of Social Media 'Likes'",
      "zh": "社群媒體點讚背後的心理學"
    },
    "situation": "高中心理學微課程下課時，Ryan 與 Olivia 探討社群平台「愛心與讚」如何透過多巴胺回饋機制影響青少年的自我價值感。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1012.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "🧑", "en": "Olivia, I noticed that posting photos online sometimes makes me anxiously refresh the feed every two minutes for likes.", "zh": "Olivia，我發現自己在網路上發照片後，有時候會焦慮地每兩分鐘就重整動態看有沒有人按讚。", "keywords": ["anxiously", "refresh"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👩", "en": "That's variable reward schedule in action. It triggers dopamine surges in our brain, much like a slot machine.", "zh": "那是『隨機變動獎勵機制』在作祟，它會觸發大腦分泌多巴胺，運作原理跟角子老虎機如出一轍。", "keywords": ["dopamine", "reward"] },
      { "id": 3, "speaker": "Ryan", "avatar": "🧑", "en": "It's unsettling how algorithms exploit our biological evolutionary need for social belonging.", "zh": "演算法居然精準利用了我們在生物演化上對群體歸屬感的情感渴望，真讓人不寒而慄。", "keywords": ["algorithms", "belonging"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👩", "en": "The antidote is decoupling our self-worth from digital metrics. Real-world validation comes from meaningful relationships.", "zh": "解藥就是把自我價值與虛擬數據解綁，真實的肯定來自於生活中有意義的人際連結。", "keywords": ["antidote", "metrics", "validation"] },
      { "id": 5, "speaker": "Ryan", "avatar": "🧑", "en": "Well said. We are human beings with rich inner lives, not statistical engagement data.", "zh": "說得太好了。我們是擁有豐沛內在心靈的活生生個體，而不是演算法裡的互動率統計數據。", "keywords": ["statistical", "engagement"] }
    ],
    "vocabulary": [
      { "word": "dopamine", "phonetic": "/ˈdoʊ.pə.miːn/", "pos": "n.", "zh": "多巴胺（傳遞興奮愉悅的神經傳導物質）", "example": "Exercise triggers the healthy release of dopamine." },
      { "word": "antidote", "phonetic": "/ˈæn.t̬i.doʊt/", "pos": "n.", "zh": "解藥、良方、對策", "example": "Humor is often the best antidote to stress." },
      { "word": "validation", "phonetic": "/ˌvæl.əˈdeɪ.ʃən/", "pos": "n.", "zh": "認同感、自我價值確認", "example": "Seek internal peace rather than external validation." }
    ],
    "dailyPhrase": { "en": "Decouple from...", "zh": "與…脫鉤、切斷負面連結。" },
    "cultureTip": "近年 Instagram 與 Facebook 開放用戶選擇隱藏點讚數（Hide Like Counts），就是為了降低青少年因社群比較（Social Comparison）而引發的心理焦慮。"
  },

  # 10-13 [國小初階]
  {
    "id": "dialogue-1013",
    "date": "10-13",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "動物生態",
    "topic": {
      "en": "Birds Flying South for Winter",
      "zh": "候鳥排隊往南飛過冬"
    },
    "situation": "操場體育課休息時，Ruby 指著蔚藍高空，好奇地看著排成 V 字形大雁隊伍。",
    "speakers": {
      "Ruby": { "role": "Ruby", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1013.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ruby", "avatar": "👧", "en": "Lucas, look way up high! A flock of wild geese is flying across the sky!", "zh": "Lucas，往高空看！有一整群野生大雁正在飛過天空耶！", "keywords": ["flock", "geese"] },
      { "id": 2, "speaker": "Lucas", "avatar": "👦", "en": "They are flying in a neat letter V formation! Where are they heading?", "zh": "牠們排成一個整整齊齊的英文字母 V 字隊形！牠們要去哪裡呢？", "keywords": ["formation", "heading"] },
      { "id": 3, "speaker": "Ruby", "avatar": "👧", "en": "They are migrating south where the weather stays warm and food is plentiful.", "zh": "牠們正在往南方遷徙，那裡的天氣比較溫暖、食物也充足。", "keywords": ["migrating", "plentiful"] },
      { "id": 4, "speaker": "Lucas", "avatar": "👦", "en": "Why do they fly in a V shape instead of a straight line?", "zh": "為什麼牠們要排成 V 字形而不是直線呢？", "keywords": ["shape", "straight"] },
      { "id": 5, "speaker": "Ruby", "avatar": "👧", "en": "The V shape cuts the wind resistance, helping the whole flock save energy!", "zh": "V 字形可以減少空氣阻力，幫助整群鳥節省體力喔！", "keywords": ["resistance", "energy"] }
    ],
    "vocabulary": [
      { "word": "flock", "phonetic": "/flɑːk/", "pos": "n.", "zh": "（鳥、羊等）群", "example": "A flock of birds rested on the power lines." },
      { "word": "migrate", "phonetic": "/ˈmaɪ.ɡreɪt/", "pos": "v.", "zh": "（候鳥等季節性）遷徙", "example": "Swallows migrate south before frost arrives." },
      { "word": "resistance", "phonetic": "/rɪˈzɪs.təns/", "pos": "n.", "zh": "阻力、抗拒", "example": "Aerodynamic design reduces wind resistance." }
    ],
    "dailyPhrase": { "en": "Fly in a V formation.", "zh": "排成 V 字形隊列飛行。" },
    "cultureTip": "空氣動力學研究證實，鳥群排成「V Formation（雁行陣）」飛行時，後方鳥兒能利用前方扇動翅膀產生的上升氣流（Upwash），節省高達 70% 的體力！"
  },

  # 10-14 [國中挑戰]
  {
    "id": "dialogue-1014",
    "date": "10-14",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "健康生活",
    "topic": {
      "en": "Why Sleep Is Your Secret Superpower",
      "zh": "睡眠是你的秘密超能力"
    },
    "situation": "晨讀時間，看到隔壁桌同學頻頻打哈欠，Sarah 提醒 Jake 充足睡眠對大腦記憶力的重要性。",
    "speakers": {
      "Sarah": { "role": "Sarah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Jake": { "role": "Jake", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1014.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sarah", "avatar": "👧", "en": "Jake, that's your fourth yawn in ten minutes! Did you pull an all-nighter again?", "zh": "Jake，這已經是你十分鐘內打的第四個哈欠了！你昨晚又熬通宵了嗎？", "keywords": ["yawn", "all-nighter"] },
      { "id": 2, "speaker": "Jake", "avatar": "👦", "en": "Guilty as charged. I stayed up until 2 a.m. gaming and finishing my geography map.", "zh": "被妳抓包了。我熬夜到凌晨兩點打電動順便趕地理地圖作業。", "keywords": ["guilty", "geography"] },
      { "id": 3, "speaker": "Sarah", "avatar": "👧", "en": "Sacrificing sleep is counterproductive. Sleep is when your brain consolidates memories into long-term storage.", "zh": "犧牲睡眠只會適得其反。大腦是在深度睡眠期間，把新記憶鞏固到長期記憶區的。", "keywords": ["consolidates", "counterproductive"] },
      { "id": 4, "speaker": "Jake", "avatar": "👦", "en": "Is that why I completely blanked out on simple vocabulary on yesterday's quiz?", "zh": "這就是為什麼我昨天小考連超簡單的單字都突然腦筋一片空白的原因嗎？", "keywords": ["blanked out", "quiz"] },
      { "id": 5, "speaker": "Sarah", "avatar": "👧", "en": "Exactly! Aim for eight hours tonight. Sleep is your ultimate secret superpower.", "zh": "沒錯！今晚目標睡滿八小時，充足睡眠才是你終極的秘密超能力！", "keywords": ["superpower", "eight hours"] }
    ],
    "vocabulary": [
      { "word": "all-nighter", "phonetic": "/ˌɑːlˈnaɪ.t̬ɚ/", "pos": "n.", "zh": "通宵、熬夜整夜", "example": "Pulling an all-nighter ruins your focus next day." },
      { "word": "consolidate", "phonetic": "/kənˈsɑː.lə.deɪt/", "pos": "v.", "zh": "鞏固、強化結合", "example": "Sleep helps the brain consolidate learned skills." },
      { "word": "counterproductive", "phonetic": "/ˌkaʊn.t̬ɚ.prəˈdʌk.tɪv/", "pos": "adj.", "zh": "適得其反的、徒勞無功的", "example": "Excessive stress is counterproductive to creativity." }
    ],
    "dailyPhrase": { "en": "Guilty as charged!", "zh": "被你說中了！我認罪！（幽默承認小缺點的生動口語）" },
    "cultureTip": "神經科學家 Matthew Walker 在暢銷書《Why We Sleep》中指出：睡眠並不是偷懶，而是大腦清洗代謝廢物（Glymphatic System）與強化神經突觸的關鍵工程。"
  },

  # 10-15 [國小中高]
  {
    "id": "dialogue-1015",
    "date": "10-15",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "自然觀察",
    "topic": {
      "en": "Visiting the Pumpkin Patch",
      "zh": "南瓜田採摘大南瓜"
    },
    "situation": "十月中旬週六，Leo 和媽媽造訪近郊的農場南瓜田，挑選萬聖節雕刻南瓜燈的材料。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mom": { "role": "媽媽", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1015.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Mom, the whole farm field is covered in round orange pumpkins! Look at how big they are!", "zh": "媽媽，整片農地都覆蓋著圓滾滾的橘色南瓜！看它們有多大！", "keywords": ["pumpkin patch", "orange"] },
      { "id": 2, "speaker": "Mom", "avatar": "👩", "en": "Grab a green wheelbarrow, Leo. We need to find a pumpkin with a sturdy green stem.", "zh": "推一台綠色單輪手推車過來吧 Leo，我們要挑一顆帶有結實綠果梗的南瓜。", "keywords": ["wheelbarrow", "stem"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Why is the stem important?", "zh": "為什麼果梗很重要呢？", "keywords": ["important"] },
      { "id": 4, "speaker": "Mom", "avatar": "👩", "en": "A fresh green stem means the pumpkin was harvested recently and won't rot quickly on our porch.", "zh": "新鮮翠綠的果梗表示南瓜是剛採收的，放在我們門廊前就不容易爛掉。", "keywords": ["harvested", "porch", "rot"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "I found the ultimate one! It has a flat bottom so it can sit upright without rolling away!", "zh": "我找到最完美的一顆了！它的底部平平的，可以穩穩坐正不會滾走！", "keywords": ["upright", "rolling"] }
    ],
    "vocabulary": [
      { "word": "patch", "phonetic": "/pætʃ/", "pos": "n.", "zh": "（農作物）一小塊田地", "example": "We spent Sunday afternoon at the pumpkin patch." },
      { "word": "wheelbarrow", "phonetic": "/ˈwiːlˌber.oʊ/", "pos": "n.", "zh": "獨輪手推車", "example": "He loaded the heavy pumpkins into the wheelbarrow." },
      { "word": "upright", "phonetic": "/ˈʌp.raɪt/", "pos": "adj./adv.", "zh": "挺直的、直立地", "example": "Keep the tall glass upright to avoid spills." }
    ],
    "dailyPhrase": { "en": "Sit upright.", "zh": "穩穩直立、坐得端正。" },
    "cultureTip": "造訪「Pumpkin Patch（南瓜田）」並乘坐「Hayride（乾草車）」是北美秋天最經典的傳統家庭戶外活動，挑選心儀南瓜準備萬聖節雕刻。"
  },

  # 10-16 [國中挑戰]
  {
    "id": "dialogue-1016",
    "date": "10-16",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "考試後生活",
    "topic": {
      "en": "Post-Exam Relief and Celebration",
      "zh": "段考交卷後的狂歡與放鬆"
    },
    "situation": "週五下午最後一科鐘聲響起，Hannah 和同學 Max 開心地步出考場，慶祝考期結束。",
    "speakers": {
      "Hannah": { "role": "Hannah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Max": { "role": "Max", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1016.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Hannah", "avatar": "👧", "en": "Pencils down! The final bell officially marks the end of our midterm exams!", "zh": "停筆交卷！最後一節鐘聲響起，正式宣告我們第一次段考結束啦！", "keywords": ["pencils down", "officially"] },
      { "id": 2, "speaker": "Max", "avatar": "👦", "en": "I feel like a weight of ten bricks just lifted off my shoulders!", "zh": "我感覺好像有十塊磚頭的重量瞬間從我肩膀上移開了一樣輕鬆！", "keywords": ["shoulders", "bricks"] },
      { "id": 3, "speaker": "Hannah", "avatar": "👧", "en": "How did you find the natural science test? The physics part was quite tricky.", "zh": "你覺得自然科考得如何？物理計算題那部分滿刁鑽的。", "keywords": ["physics", "tricky"] },
      { "id": 4, "speaker": "Max", "avatar": "👦", "en": "Don't discuss answers now; what's done is done! Let's hit the boba shop for brown sugar milk tea.", "zh": "現在先別對答案了，考完就考完了！我們去手搖飲店喝黑糖珍珠奶茶吧。", "keywords": ["what's done is done", "boba"] },
      { "id": 5, "speaker": "Hannah", "avatar": "👧", "en": "You read my mind! Large cup with extra chewy pearls, please!", "zh": "你完全懂我！大杯、加厚有嚼勁的波霸珍珠，走起！", "keywords": ["read my mind", "pearls"] }
    ],
    "vocabulary": [
      { "word": "officially", "phonetic": "/əˈfɪʃ.əl.i/", "pos": "adv.", "zh": "正式地、官方宣告地", "example": "The sports event has officially commenced." },
      { "word": "tricky", "phonetic": "/ˈtrɪk.i/", "pos": "adj.", "zh": "刁鑽的、複雜難辦的", "example": "The math exam included several tricky word problems." },
      { "word": "chewy", "phonetic": "/ˈtʃuː.i/", "pos": "adj.", "zh": "Q彈的、有嚼勁的", "example": "Boba pearls are famous for their chewy texture." }
    ],
    "dailyPhrase": { "en": "What's done is done.", "zh": "木已成舟、過去的就讓它過去吧（考完不糾結的好心態）" },
    "cultureTip": "「What's done is done」源自莎士比亞名劇《馬克白》，在現代口語中常用來勸慰朋友不要為已經無法改變的事情過度懊惱焦慮。"
  },

  # 10-17 [國小初階]
  {
    "id": "dialogue-1017",
    "date": "10-17",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "健康與衛生",
    "topic": {
      "en": "Washing Hands Before Lunch",
      "zh": "吃午餐前記得把雙手洗乾淨"
    },
    "situation": "午餐打飯前，小組長 Sam 帶著同學 Eric 到洗手台按照洗手七字訣洗手。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Eric": { "role": "Eric", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1017.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Eric, hold on! Before touching your bento box, let's wash our hands.", "zh": "Eric，等等！在摸便當盒之前，我們先去把手洗乾淨。", "keywords": ["bento box", "wash hands"] },
      { "id": 2, "speaker": "Eric", "avatar": "👦", "en": "My hands look clean already. Do I still need to use soap?", "zh": "我的手看起來已經很乾淨了呀，還需要用肥皂嗎？", "keywords": ["soap", "clean"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Yes! Invisible germs and bacteria hide between our fingers after playing in the schoolyard.", "zh": "當然要！在操場玩過之後，看不見的細菌就躲在我們的指縫裡。", "keywords": ["germs", "bacteria"] },
      { "id": 4, "speaker": "Eric", "avatar": "👦", "en": "Rub between fingers, scrub the palms, and sing the Happy Birthday song twice!", "zh": "搓搓指縫、搓搓手心，還要唱兩遍生日快樂歌！", "keywords": ["scrub", "palms"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Rinse clean and dry with a clean paper towel. Now we are ready to eat safely!", "zh": "沖洗乾淨再用紙巾擦乾。現在我們可以安心吃午餐囉！", "keywords": ["rinse", "safely"] }
    ],
    "vocabulary": [
      { "word": "germ", "phonetic": "/dʒɝːm/", "pos": "n.", "zh": "病菌、細菌", "example": "Washing hands with soap washes germs down the drain." },
      { "word": "scrub", "phonetic": "/skrʌb/", "pos": "v.", "zh": "用力擦洗、刷洗", "example": "Scrub your palms thoroughly under warm water." },
      { "word": "rinse", "phonetic": "/rɪns/", "pos": "v.", "zh": "沖洗（泡沫）", "example": "Rinse your hands until all soap residue is gone." }
    ],
    "dailyPhrase": { "en": "Rub and scrub.", "zh": "搓一搓、刷一刷（洗手口訣）" },
    "cultureTip": "美國疾病管制中心（CDC）建議：洗手搓肥皂的時間至少應達 20 秒，相當於哼唱兩遍《Happy Birthday》兒歌的時間，能有效去除 99% 的常見病菌。"
  },

  # 10-18 [高中進階]
  {
    "id": "dialogue-1018",
    "date": "10-18",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "生涯探索",
    "topic": {
      "en": "Specialist vs. Generalist in Future Careers",
      "zh": "未來職場：專才還是通才更具優勢？"
    },
    "situation": "高中模擬聯合國社團活動結束後，Grace 與 Leo 就未來 AI 時代下成為「T型人才」的跨領域優勢進行討論。",
    "speakers": {
      "Grace": { "role": "Grace", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" },
      "Leo": { "role": "Leo", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1018.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Grace", "avatar": "👩", "en": "Leo, when picking university majors, is it smarter to specialize deeply in one narrow field or build a broad skillset?", "zh": "Leo，在挑選大學科系時，深入鑽研單一狹窄領域比較明智，還是培養跨界廣泛技能更吃香？", "keywords": ["specialize", "skillset"] },
      { "id": 2, "speaker": "Leo", "avatar": "🧑", "en": "The modern consensus points toward becoming a T-shaped individual: deep vertical expertise combined with wide horizontal adaptability.", "zh": "現代主流共識傾向成為『T 型人才』：具備縱向深度的專業核心，同時擁有橫向廣泛的跨領域適應力。", "keywords": ["consensus", "expertise", "adaptability"] },
      { "id": 3, "speaker": "Grace", "avatar": "👩", "en": "That makes total sense. Hyper-specialized manual tasks risk being automated by generative AI models.", "zh": "這非常有道理。過於單一狹隘的重複性專業技能，很容易面臨被生成式 AI 演算法自動化取代的風險。", "keywords": ["automated", "hyper-specialized"] },
      { "id": 4, "speaker": "Leo", "avatar": "🧑", "en": "However, broad generalists who connect dots between technology, human empathy, and creative storytelling will remain irreplaceable.", "zh": "然而，能夠在科技邏輯、人文共情與創意敘事之間穿針引線的跨界通才，將始終無可取代。", "keywords": ["empathy", "irreplaceable"] },
      { "id": 5, "speaker": "Grace", "avatar": "👩", "en": "So cultivating lifelong curiosity and cross-disciplinary agility is truly the premier career armor.", "zh": "因此，培養終身好奇心與跨學科敏捷力，正是應對未來職場變局最堅固的鎧甲。", "keywords": ["curiosity", "cross-disciplinary"] }
    ],
    "vocabulary": [
      { "word": "consensus", "phonetic": "/kənˈsen.səs/", "pos": "n.", "zh": "共識、多數意見", "example": "The committee reached a general consensus." },
      { "word": "irreplaceable", "phonetic": "/ˌɪr.ɪˈpleɪ.sə.bəl/", "pos": "adj.", "zh": "不可替代的、無可取代的", "example": "Human compassion is irreplaceable by machines." },
      { "word": "expertise", "phonetic": "/ˌek.spɝːˈtiːz/", "pos": "n.", "zh": "專長、專業知識", "example": "She shared her valuable legal expertise." }
    ],
    "dailyPhrase": { "en": "Connect the dots.", "zh": "觸類旁通、將碎片知識串聯融會貫通。" },
    "cultureTip": "賈伯斯（Steve Jobs）在史丹佛大學著名的畢業演講中提到「Connect the dots」，強調年輕時跨界探索的多元經驗，往往會在未來的某個關鍵節點交織發揮奇效。"
  },

  # 10-19 [國小中高]
  {
    "id": "dialogue-1019",
    "date": "10-19",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "校園活動",
    "topic": {
      "en": "Designing Halloween Costumes",
      "zh": "設計萬聖節變裝造型"
    },
    "situation": "綜合活動課上，Emma 和 Ken 正在繪圖紙上畫草圖，計畫今年萬聖節踩街要打扮的角色。",
    "speakers": {
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Ken": { "role": "Ken", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1019.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Emma", "avatar": "👧", "en": "Halloween is in less than two weeks! Ken, what are you dressing up as this year?", "zh": "萬聖節再不到兩週就到了！Ken，你今年打算裝扮成什麼角色？", "keywords": ["Halloween", "dressing up"] },
      { "id": 2, "speaker": "Ken", "avatar": "👦", "en": "I'm transforming cardboard boxes into a silver astronaut suit with foil helmet antennas!", "zh": "我要用紙箱改造成銀色太空人套裝，上面還要裝鋁箔紙天線安全帽！", "keywords": ["astronaut", "cardboard"] },
      { "id": 3, "speaker": "Emma", "avatar": "👧", "en": "Creative upcycling! I am sewing a wizard cape decorated with glowing felt stars.", "zh": "好有創意的環保改造喔！我正在縫一件巫師披風，上面裝飾著發光的毛氈星星。", "keywords": ["wizard", "cape", "felt"] },
      { "id": 4, "speaker": "Ken", "avatar": "👦", "en": "Are you going to carve a spooky pumpkin bucket for collecting candy?", "zh": "妳會雕刻一個搞怪南瓜提桶來裝要糖果的戰利品嗎？", "keywords": ["spooky", "carve"] },
      { "id": 5, "speaker": "Emma", "avatar": "👧", "en": "Definitely! Homemade costumes are hundred times cooler than store-bought ones!", "zh": "那是一定要的！自己親手做的萬聖節服裝，比去店裡買的酷上一百倍！", "keywords": ["homemade", "store-bought"] }
    ],
    "vocabulary": [
      { "word": "costume", "phonetic": "/ˈkɑː.stuːm/", "pos": "n.", "zh": "化妝服、戲服、變裝服飾", "example": "Children wore creative costumes for the parade." },
      { "word": "cape", "phonetic": "/keɪp/", "pos": "n.", "zh": "披肩、斗篷", "example": "The superhero wore a flowing red cape." },
      { "word": "spooky", "phonetic": "/ˈspuː.ki/", "pos": "adj.", "zh": "陰森搞怪的、神秘幽靈般的", "example": "The haunted maze had spooky music." }
    ],
    "dailyPhrase": { "en": "Dress up as...", "zh": "變裝打扮成某個角色" },
    "cultureTip": "現代萬聖節提倡「DIY Costumes（自己動手做服裝）」，利用家中的舊紙箱、碎布與環保材料改造，既省錢又展現滿滿的個人創意！"
  },

  # 10-20 [國中挑戰]
  {
    "id": "dialogue-1020",
    "date": "10-20",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "休閒娛樂",
    "topic": {
      "en": "Carving a Spooky Jack-o'-Lantern",
      "zh": "雕刻一顆搞怪南瓜燈"
    },
    "situation": "週六下午，Kevin 和 David 在廚房桌上鋪滿報紙，準備把大南瓜雕刻成生動的萬聖節南瓜燈。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "🧑", "gender": "male", "voice": "en-US-ChristopherNeural" },
      "David": { "role": "David", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1020.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "🧑", "en": "Step one: cut a circular lid around the pumpkin stem at an inward angle so it won't fall inside!", "zh": "第一步：在南瓜蒂周圍以向內傾斜的角度切出一個圓形頂蓋，這樣蓋子才不會掉進去！", "keywords": ["circular", "lid", "stem"] },
      { "id": 2, "speaker": "David", "avatar": "👦", "en": "Got it. Now hand me that big metal spoon so I can scoop out the slimy pulp and seeds.", "zh": "收到。現在把大鐵湯匙遞給我，我來把黏答答的南瓜果肉和種子刮乾淨。", "keywords": ["scoop", "slimy", "pulp"] },
      { "id": 3, "speaker": "Kevin", "avatar": "🧑", "en": "Don't throw away the seeds! We can roast them with olive oil and sea salt for a savory snack.", "zh": "別把南瓜子丟掉！我們可以拌橄欖油和海鹽放烤箱烤成香脆小零食。", "keywords": ["roasted", "savory"] },
      { "id": 4, "speaker": "David", "avatar": "👦", "en": "Great idea. I drew a jagged tooth grin and triangle eyes on the front with a washable marker.", "zh": "好主意。我用可洗式彩色筆在正面畫了鋸齒狀咧嘴笑和大三角形眼睛。", "keywords": ["jagged", "grin", "triangle"] },
      { "id": 5, "speaker": "Kevin", "avatar": "🧑", "en": "Let's place a flicker LED tea light inside. Turn off the kitchen lights... Wow, perfectly eerie!", "zh": "我們在裡面放一顆搖曳的 LED 蠟燭燈。關掉廚房燈…哇，超有那種搞怪的萬聖節氛圍！", "keywords": ["eerie", "flicker"] }
    ],
    "vocabulary": [
      { "word": "scoop", "phonetic": "/skuːp/", "pos": "v.", "zh": "用杓子或湯匙舀出、挖出", "example": "Scoop the seeds out of the melon." },
      { "word": "jagged", "phonetic": "/ˈdʒæɡ.ɪd/", "pos": "adj.", "zh": "鋸齒狀的、參差不齊的", "example": "The cliff had sharp jagged edges." },
      { "word": "eerie", "phonetic": "/ˈɪr.i/", "pos": "adj.", "zh": "神秘怪異的、讓人起雞皮疙瘩的", "example": "An eerie green glow lit up the dark hallway." }
    ],
    "dailyPhrase": { "en": "Turn off the lights!", "zh": "把燈關掉！（營造氛圍時的經典台詞）" },
    "cultureTip": "「Jack-o'-lantern（南瓜燈）」傳說源自愛爾蘭民間傳說 Stingy Jack（吝嗇傑克），原本用大頭菜雕刻，傳到盛產南瓜的美洲後改為雕刻大南瓜。"
  },

  # 10-21 [國小初階]
  {
    "id": "dialogue-1021",
    "date": "10-21",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "生活樂趣",
    "topic": {
      "en": "Blowing Giant Soap Bubbles",
      "zh": "在秋天陽光下吹巨大彩色泡泡"
    },
    "situation": "午後公園草地上，Anna 和弟弟 Tim 拿著泡泡水大鐵環，吹出一顆顆在陽光下映照彩虹的巨型泡泡。",
    "speakers": {
      "Anna": { "role": "Anna", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Tim": { "role": "Tim", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1021.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Anna", "avatar": "👧", "en": "Tim, dip this big wand into the bubble mixture and wave your arms gently!", "zh": "Tim，把這個大泡泡環浸進泡泡水裡，然後輕輕揮動雙臂！", "keywords": ["wand", "mixture"] },
      { "id": 2, "speaker": "Tim", "avatar": "👦", "en": "Look at that! It formed a giant bubble as big as a watermelon!", "zh": "快看！它形成了一個跟大西瓜一樣大的超大泡泡耶！", "keywords": ["giant", "watermelon"] },
      { "id": 3, "speaker": "Anna", "avatar": "👧", "en": "Watch the sunlight shining on it! You can see rainbow swirls swirling around.", "zh": "看陽光照在上面的折射！可以看到彩虹色的光澤在上面轉圈圈。", "keywords": ["swirls", "sunlight"] },
      { "id": 4, "speaker": "Tim", "avatar": "👦", "en": "It's floating up towards the tree branches! Pop!", "zh": "它正飄向樹枝高處呢！啪的一聲破掉了！", "keywords": ["floating", "pop"] },
      { "id": 5, "speaker": "Anna", "avatar": "👧", "en": "Chasing bubbles on a breezy afternoon is pure joy!", "zh": "在微風徐徐的午後追泡泡，真的好單純快樂喔！", "keywords": ["chasing", "pure joy"] }
    ],
    "vocabulary": [
      { "word": "wand", "phonetic": "/wɑːnd/", "pos": "n.", "zh": "棒子、魔杖、泡泡圈環", "example": "The magician waved a shiny wand." },
      { "word": "float", "phonetic": "/floʊt/", "pos": "v.", "zh": "漂浮、飄動", "example": "Colorful balloons float gently into the blue sky." },
      { "word": "swirl", "phonetic": "/swɝːl/", "pos": "v./n.", "zh": "旋轉、迴旋光澤", "example": "Leaves swirled around in the autumn gust." }
    ],
    "dailyPhrase": { "en": "Pure joy.", "zh": "純粹無比的快樂。" },
    "cultureTip": "泡泡表面之所以會呈現七彩斑斕的顏色，是因為光波在薄膜內外兩層反射產生了「Thin-Film Interference（薄膜干涉）」物理光學現象。"
  },

  # 10-22 [高中進階]
  {
    "id": "dialogue-1022",
    "date": "10-22",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "科技與倫理",
    "topic": {
      "en": "Ethics of Genetic Editing and CRISPR",
      "zh": "基因編輯技術與生命倫理的邊界"
    },
    "situation": "高中生物奧林匹亞研習營休息時，Jason 和 Chloe 就 CRISPR-Cas9 基因剪刀在消滅遺傳疾病與「訂製嬰兒」疑慮間展開思辨。",
    "speakers": {
      "Jason": { "role": "Jason", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1022.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Jason", "avatar": "🧑", "en": "Chloe, CRISPR technology has reached the point where scientists can precisely splice DNA sequences like editing a text document.", "zh": "Chloe，CRISPR 基因編輯技術已經發展到科學家能像編輯 Word 文件一樣精準剪切 DNA 序列。", "keywords": ["CRISPR", "splice"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👩", "en": "The therapeutic potential is staggering, especially for curing previously untreatable genetic conditions like sickle cell anemia.", "zh": "它在醫療上的潛力驚人，尤其對治癒像鐮刀型貧血症等過去無法根治的遺傳疾病。", "keywords": ["therapeutic", "anemia"] },
      { "id": 3, "speaker": "Jason", "avatar": "🧑", "en": "Yet the boundary blurs when we shift from curing deadly diseases to cosmetic genetic enhancement and designer babies.", "zh": "然而，當我們從治療致死性疾病跨越到非醫療的基因外貌優化和訂製嬰兒時，道德邊界就模糊了。", "keywords": ["enhancement", "designer babies"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👩", "en": "That could exacerbate socioeconomic inequalities, creating biological castes based on who can afford genetic upgrades.", "zh": "那恐將加劇社會經濟不平等，甚至依據誰負擔得起基因升級而形成生物階級分化。", "keywords": ["inequalities", "socioeconomic"] },
      { "id": 5, "speaker": "Jason", "avatar": "🧑", "en": "Scientific capability must never outpace ethical deliberation. Global regulatory frameworks are indispensable.", "zh": "科學能力絕不能走得比倫理思辨更快，健全的全球監管治理框架必不可少。", "keywords": ["deliberation", "frameworks"] }
    ],
    "vocabulary": [
      { "word": "splice", "phonetic": "/splaɪs/", "pos": "v.", "zh": "拼接、剪接（基因或線路）", "example": "Geneticists splice beneficial genes into crop varieties." },
      { "word": "therapeutic", "phonetic": "/ˌθer.əˈpjuː.t̬ɪk/", "pos": "adj.", "zh": "具有療效的、治療性的", "example": "Music therapy has proven therapeutic benefits." },
      { "word": "deliberation", "phonetic": "/dɪˌlɪb.əˈreɪ.ʃən/", "pos": "n.", "zh": "審慎思量、深思熟慮", "example": "The jury reached a unanimous verdict after long deliberation." }
    ],
    "dailyPhrase": { "en": "The boundary blurs.", "zh": "界線逐漸模糊曖昧。" },
    "cultureTip": "CRISPR-Cas9 發現者 Jennifer Doudna 與 Emmanuelle Charpentier 於 2020 年榮獲諾貝爾化學獎，但各國科學界一致強調禁止人類生殖細胞（Germline）的非醫療編輯。"
  },

  # 10-23 [國小中高]
  {
    "id": "dialogue-1023",
    "date": "10-23",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "校園生活",
    "topic": {
      "en": "Running for Class President",
      "zh": "競選班長政見發表會"
    },
    "situation": "班會課上，Emily 在講台上自信發表競選班長的小演講，台下的好友 Sam 熱情鼓掌支持。",
    "speakers": {
      "Emily": { "role": "Emily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1023.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Emily", "avatar": "👧", "en": "Good afternoon, classmates! If elected class president, I promise to set up a peer homework help corner.", "zh": "同學們午安！如果我當選班長，我保證會在班上成立一個同儕課業互助諮詢角。", "keywords": ["president", "elected"] },
      { "id": 2, "speaker": "Sam", "avatar": "👦", "en": "Hear, hear! That would really help us before challenging unit tests!", "zh": "說得好！這對我們在單元大考前真的會非常有幫助！", "keywords": ["hear hear"] },
      { "id": 3, "speaker": "Emily", "avatar": "👧", "en": "I will also organize monthly board game tournaments on Friday afternoons so everyone feels included.", "zh": "我也會安排每個月週五下午舉辦班級桌遊友誼賽，讓每位同學都有歸屬感。", "keywords": ["tournaments", "included"] },
      { "id": 4, "speaker": "Sam", "avatar": "👦", "en": "Her speech was so structured and genuine! She really listens to what our class needs.", "zh": "她的演說有條有理又好真誠喔！她真的有在用心傾聽全班同學的需要。", "keywords": ["genuine", "structured"] },
      { "id": 5, "speaker": "Emily", "avatar": "👧", "en": "Every voice matters. Let's make this semester our most memorable one together!", "zh": "每一個人的聲音都很重要。讓我們一起把這學期變成最難忘的一學期！", "keywords": ["memorable", "voice"] }
    ],
    "vocabulary": [
      { "word": "elect", "phonetic": "/iˈlekt/", "pos": "v.", "zh": "選舉、票選", "example": "The class voted to elect a new captain." },
      { "word": "genuine", "phonetic": "/ˈdʒen.ju.ɪn/", "pos": "adj.", "zh": "真誠的、非虛偽的", "example": "Her warm smile felt completely genuine." },
      { "word": "tournament", "phonetic": "/ˈtʊr.nə.mənt/", "pos": "n.", "zh": "錦標賽、淘汰賽", "example": "Our school basketball tournament begins on Monday." }
    ],
    "dailyPhrase": { "en": "Hear, hear!", "zh": "說得好！贊成！（英國議會與正式演講中表示熱烈贊同的傳統歡呼）" },
    "cultureTip": "「Hear, hear!」源自 17 世紀英國下議院的「Hear him, hear him!」，表示聽眾完全贊成發言者講出的精彩觀點。"
  },

  # 10-24 [國中挑戰]
  {
    "id": "dialogue-1024",
    "date": "10-24",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "日常生活",
    "topic": {
      "en": "Assembling a DIY Bookshelf",
      "zh": "動手組裝自己的三層書櫃"
    },
    "situation": "週六下午在客廳，Tyler 和好友 Chris 按照說明書一起用六角扳手和螺絲組裝新買的木質書架。",
    "speakers": {
      "Tyler": { "role": "Tyler", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chris": { "role": "Chris", "avatar": "👦", "gender": "male", "voice": "en-US-ChristopherNeural" }
    },
    "audioSrc": "audio/dialogue-1024.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tyler", "avatar": "👦", "en": "Chris, my new flat-pack bookshelf arrived from IKEA! Ready to tackle some DIY construction?", "zh": "Chris，我從宜家買的平整包裝新書架送到了！準備好一起來組裝 DIY 傢俱了嗎？", "keywords": ["flat-pack", "bookshelf"] },
      { "id": 2, "speaker": "Chris", "avatar": "👦", "en": "Let's lay out all the wooden panels and hardware on the carpet first to make sure no bolts are missing.", "zh": "我們先把所有木板和五金螺絲倒在地毯上排列好，確認沒有少零件。", "keywords": ["hardware", "bolts"] },
      { "id": 3, "speaker": "Tyler", "avatar": "👦", "en": "Look at diagram step three: insert the wooden dowels into the side rails before tightening the screws.", "zh": "看說明書圖解第三步：鎖緊螺絲之前，要先把木榫塞進側邊導軌裡。", "keywords": ["diagram", "screws"] },
      { "id": 4, "speaker": "Chris", "avatar": "👦", "en": "Pass me the Allen wrench. Remember the golden rule: righty-tighty, lefty-loosey!", "zh": "把六角扳手遞給我。記住黃金口訣：順時針向右旋緊，逆時針向左旋鬆！", "keywords": ["wrench", "tighty"] },
      { "id": 5, "speaker": "Tyler", "avatar": "👦", "en": "It stands completely level and sturdy! Now my comic books and textbooks finally have a neat home.", "zh": "站得超級平整穩固！現在我的漫畫書和課本終於有一個整齊的家了。", "keywords": ["level", "comic books"] }
    ],
    "vocabulary": [
      { "word": "hardware", "phonetic": "/ˈhɑːrd.wer/", "pos": "n.", "zh": "五金零件、螺絲組件", "example": "The kit contains all necessary mounting hardware." },
      { "word": "diagram", "phonetic": "/ˈdaɪ.ə.ɡræm/", "pos": "n.", "zh": "示意圖、圖解說明", "example": "Follow the step-by-step assembly diagram." },
      { "word": "wrench", "phonetic": "/rentʃ/", "pos": "n.", "zh": "扳手、扳鉗", "example": "Tighten the hexagonal bolt with a wrench." }
    ],
    "dailyPhrase": { "en": "Righty-tighty, lefty-loosey.", "zh": "右緊左鬆（歐美日常組裝修理螺絲最實用的順口溜）" },
    "cultureTip": "「Righty-tighty, lefty-loosey」是英文母語人士自幼琅琅上口的口訣，用來記憶絕大多數順時針螺紋（Clockwise to tighten, counterclockwise to loosen）。"
  },

  # 10-25 [國小初階]
  {
    "id": "dialogue-1025",
    "date": "10-25",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "節慶預熱",
    "topic": {
      "en": "Knock Knock! Who Is There?",
      "zh": "敲敲門！是誰在外面？"
    },
    "situation": "下課走廊上，Sam 和 Eric 互相說有趣的萬聖節敲敲門冷笑話（Knock-knock jokes）。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Eric": { "role": "Eric", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1025.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Eric, want to hear a funny Halloween joke? Knock, knock!", "zh": "Eric，想聽一個好笑的萬聖節笑話嗎？敲敲門！", "keywords": ["joke", "knock knock"] },
      { "id": 2, "speaker": "Eric", "avatar": "👦", "en": "Who's there?", "zh": "是誰呀？", "keywords": ["who's there"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Boo!", "zh": "Boo（嚇你一下）！", "keywords": ["boo"] },
      { "id": 4, "speaker": "Eric", "avatar": "👦", "en": "Boo who?", "zh": "Boo 是誰？", "keywords": ["boo who"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Don't cry! It's just a friendly ghost pretending to scare you! Haha!", "zh": "別哭啦（Boo-hoo）！只是一隻友善的小鬼在假裝嚇你而已啦！哈哈！", "keywords": ["ghost", "scare"] }
    ],
    "vocabulary": [
      { "word": "knock", "phonetic": "/nɑːk/", "pos": "v./n.", "zh": "敲擊、敲門", "example": "Knock politely before entering the classroom." },
      { "word": "ghost", "phonetic": "/ɡoʊst/", "pos": "n.", "zh": "幽靈、鬼怪", "example": "A friendly ghost appeared in the cartoon." },
      { "word": "scare", "phonetic": "/sker/", "pos": "v.", "zh": "驚嚇、恐嚇", "example": "Loud thunder scares our pet dog." }
    ],
    "dailyPhrase": { "en": "Knock, knock! Who's there?", "zh": "敲敲門！是誰呀？（英語文化最經典笑話格式）" },
    "cultureTip": "「Knock-knock joke」是英語世界孩子從小聽到大的文字遊戲（Pun）。上面笑話利用「Boo who」聽起來像哭泣聲「Boo-hoo（嗚嗚哭）」的諧音製造笑料。"
  },

  # 10-26 [高中進階]
  {
    "id": "dialogue-1026",
    "date": "10-26",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "影視與文學",
    "topic": {
      "en": "Why Do Humans Love Horror Movies?",
      "zh": "人類為什麼喜愛自討苦吃看恐怖片？"
    },
    "situation": "十月萬聖季即將來臨，高三好友 Marcus 與 Bella 在圖書館研討室探討懸疑恐怖電影對人類心理的獨特安全快感。",
    "speakers": {
      "Marcus": { "role": "Marcus", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Bella": { "role": "Bella", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1026.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Marcus", "avatar": "🧑", "en": "Bella, box office data shows October horror film releases consistently generate immense profit. What makes fear so alluring?", "zh": "Bella，票房數據顯示十月上映的恐怖片總是賺得盆滿缽滿。恐懼到底有什麼吸引人的魅力？", "keywords": ["box office", "alluring"] },
      { "id": 2, "speaker": "Bella", "avatar": "👩", "en": "Psychologists call it 'recreational fear'. It floods our nervous system with adrenaline while our conscious brain knows we are perfectly safe.", "zh": "心理學家稱之為『娛樂性恐懼』。它讓神經系統腎上腺素狂飆，但理性大腦深知自己身處在絕對安全的電影院裡。", "keywords": ["adrenaline", "recreational"] },
      { "id": 3, "speaker": "Marcus", "avatar": "🧑", "en": "So it functions like an emotional roller coaster: safe physical danger without genuine peril.", "zh": "所以它的作用機制就像雲霄飛車一樣：體驗生理上的驚險刺激，卻不用面臨真實的生命危險。", "keywords": ["roller coaster", "peril"] },
      { "id": 4, "speaker": "Bella", "avatar": "👩", "en": "Exactly. Enduring a horror film and walking out unscathed also gives a psychological sense of mastery and catharsis.", "zh": "沒錯，撐過一整部恐怖片並毫髮無傷地走出影廳，還會帶來一種戰勝恐懼的心理掌控感與情緒宣洩宣導。", "keywords": ["catharsis", "unscathed"] },
      { "id": 5, "speaker": "Marcus", "avatar": "🧑", "en": "Fascinating! Let's organize a classic thriller screening with our film club this Friday night.", "zh": "太有意思了！我們這週五晚上就來和電影社辦一場經典懸疑片賞析放映會吧。", "keywords": ["thriller", "screening"] }
    ],
    "vocabulary": [
      { "word": "alluring", "phonetic": "/əˈlʊr.ɪŋ/", "pos": "adj.", "zh": "引人入勝的、誘人的", "example": "The mysterious plot made the story alluring." },
      { "word": "catharsis", "phonetic": "/kəˈθɑːr.sɪs/", "pos": "n.", "zh": "（情感的）宣洩、淨化昇華", "example": "Weeping at a tragedy brings emotional catharsis." },
      { "word": "unscathed", "phonetic": "/ʌnˈskeɪðd/", "pos": "adj.", "zh": "毫髮無損的、未受傷害的", "example": "Miraculously, all passengers escaped unscathed." }
    ],
    "dailyPhrase": { "en": "An emotional roller coaster.", "zh": "情緒起伏極大、如坐雲霄飛車般的波瀾體驗。" },
    "cultureTip": "丹麥奧胡斯大學的「Recreational Fear Lab（娛樂恐懼實驗室）」指出，適度體驗恐怖小說與電影，有助於青年人在安全的沙盒環境中磨練調節焦慮的心理韌性。"
  },

  # 10-27 [國小中高]
  {
    "id": "dialogue-1027",
    "date": "10-27",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "烘焙美食",
    "topic": {
      "en": "Baking Sweet Pumpkin Pie",
      "zh": "廚房烘烤香甜南瓜派"
    },
    "situation": "週日午後，Lucas 和媽媽在廚房揉派皮、拌南瓜泥，為萬聖節聚會準備香濃肉桂南瓜派。",
    "speakers": {
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mom": { "role": "媽媽", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1027.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lucas", "avatar": "👦", "en": "Mom, the cooked pumpkin puree looks so smooth! What spices do we sprinkle in?", "zh": "媽媽，煮熟的南瓜泥看起來好細緻喔！我們要撒哪些香料進去呢？", "keywords": ["pumpkin puree", "spices"] },
      { "id": 2, "speaker": "Mom", "avatar": "👩", "en": "A pinch of fragrant cinnamon, ground nutmeg, and a dash of sweet brown sugar.", "zh": "一小撮芳香肉桂粉、荳蔻粉，還有一點香甜黑糖。", "keywords": ["cinnamon", "nutmeg"] },
      { "id": 3, "speaker": "Lucas", "avatar": "👦", "en": "I love the warm cinnamon smell! Can I crimp the pie crust edges with a fork?", "zh": "我好喜歡溫暖的肉桂香味！我可以用叉子在派皮邊緣壓出波浪花紋嗎？", "keywords": ["crimp", "crust"] },
      { "id": 4, "speaker": "Mom", "avatar": "👩", "en": "Press gently along the rim to seal the pie neatly, just like that!", "zh": "沿著派盤邊緣輕輕壓，把派皮封緊封整齊，就像那樣！", "keywords": ["rim", "seal"] },
      { "id": 5, "speaker": "Lucas", "avatar": "👦", "en": "Into the oven it goes! It will be heavenly topped with vanilla whipped cream!", "zh": "進烤箱烤囉！出爐後擠上一大匙香草鮮奶油一定好吃到飛上天！", "keywords": ["whipped cream", "vanilla"] }
    ],
    "vocabulary": [
      { "word": "cinnamon", "phonetic": "/ˈsɪn.ə.mən/", "pos": "n.", "zh": "肉桂粉、肉桂", "example": "Sprinkle ground cinnamon on hot oatmeal." },
      { "word": "crust", "phonetic": "/krʌst/", "pos": "n.", "zh": "派皮、麵包皮", "example": "The golden pie crust was flaky and buttery." },
      { "word": "puree", "phonetic": "/pjʊrˈeɪ/", "pos": "n.", "zh": "果泥、泥狀食品", "example": "Whisk the pumpkin puree with fresh cream." }
    ],
    "dailyPhrase": { "en": "Flaky and buttery.", "zh": "酥脆可口又充滿奶油香氣（形容烘焙糕點絕佳口感）" },
    "cultureTip": "「Pumpkin Spice（南瓜香料配方）」通常由肉桂、肉豆蔻、生薑粉與丁香調和而成，是歐美十月秋天的招牌經典香氣。"
  },

  # 10-28 [國中挑戰]
  {
    "id": "dialogue-1028",
    "date": "10-28",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "社團活動",
    "topic": {
      "en": "Setting Up the School Haunted Hallway",
      "zh": "佈置校園萬聖節鬼屋走廊"
    },
    "situation": "學生會放學後在舊活動中心走廊拉黑色遮光布、掛棉花蜘蛛網，籌備校園萬聖節鬼屋闖關。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1028.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Zoe, stretch those artificial cobwebs across the doorway! Stretch them thin so they look dusty and ancient.", "zh": "Zoe，把那些人造蜘蛛網拉開跨過門框！拉薄一點看起來才會有陳年積灰的古老逼真感。", "keywords": ["cobwebs", "ancient"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Like this? I placed rubber black spiders right in the center of each web.", "zh": "像這樣嗎？我還在每張網正中央擺了黑色的塑膠玩具蜘蛛。", "keywords": ["spiders", "rubber"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Creepy! Did the audio-visual team test the fog machine and spooky howling sound effects?", "zh": "夠詭異！影音組同學測試過乾冰煙霧機和陰森的狼嚎音效了嗎？", "keywords": ["fog machine", "howling"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Yes! When visitors step on the pressure mat, a green strobe light flashes with a sudden creak!", "zh": "測過了！只要參觀者踩到感應地墊，綠色閃頻燈就會閃爍並伴隨突然的開門嘎吱聲！", "keywords": ["strobe light", "creak"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "The whole school is going to scream their lungs out this Friday! Best event of the semester!", "zh": "這週五全校同學一定會尖叫到破喉嚨！絕對是這學期最炸裂的盛大活動！", "keywords": ["scream", "semester"] }
    ],
    "vocabulary": [
      { "word": "cobweb", "phonetic": "/ˈkɑːb.web/", "pos": "n.", "zh": "蜘蛛網（尤指積灰陳舊的網）", "example": "Dusty cobwebs hung from the attic beams." },
      { "word": "strobe", "phonetic": "/stroʊb/", "pos": "n.", "zh": "閃頻燈、閃光燈", "example": "A strobe light flickered rhythmically in the dark." },
      { "word": "artificial", "phonetic": "/ˌɑːr.t̬əˈfɪʃ.əl/", "pos": "adj.", "zh": "人造的、仿造的", "example": "The artificial plants look surprisingly realistic." }
    ],
    "dailyPhrase": { "en": "Scream your lungs out!", "zh": "聲嘶力竭地尖叫！（形容驚嚇或看演唱會時的瘋狂尖叫）" },
    "cultureTip": "學校或社區舉辦的「Haunted House / Haunted Hallway（萬聖鬼屋）」通常會嚴格設定安全動線與逃生指示燈，在提供驚悚歡樂的同時確保萬無一失。"
  },

  # 10-29 [國小初階]
  {
    "id": "dialogue-1029",
    "date": "10-29",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "節慶文化",
    "topic": {
      "en": "Trick or Treat! Smell My Feet!",
      "zh": "不給糖就搗蛋！萬聖節趣味童謠"
    },
    "situation": "英文課上，Lily 和 Toby 拿著南瓜桶，練習萬聖節挨家挨戶要糖果的傳統逗趣兒歌。",
    "speakers": {
      "Lily": { "role": "Lily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1029.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lily", "avatar": "👧", "en": "Toby, do you remember the classic Halloween rhyme we learned in English class?", "zh": "Toby，你還記得我們英文課學的那首經典萬聖節押韻兒歌嗎？", "keywords": ["rhyme", "classic"] },
      { "id": 2, "speaker": "Toby", "avatar": "👦", "en": "Of course! 'Trick or treat, smell my feet, give me something good to eat!'", "zh": "當然記得！『不給糖就搗蛋，聞聞我的腳丫丫，給我好吃的小點心！』", "keywords": ["trick or treat", "feet"] },
      { "id": 3, "speaker": "Lily", "avatar": "👧", "en": "Haha, and the second line: 'If you don't, I don't care, I'll pull down your underwear!'", "zh": "哈哈，還有第二句：『如果你不給，我也不在乎，我就把你的小內褲扯下來！』", "keywords": ["care", "underwear"] },
      { "id": 4, "speaker": "Toby", "avatar": "👦", "en": "Silly rhymes make everyone giggle! Remember to always say 'Thank you' after getting candy.", "zh": "無厘頭的押韻總是逗得大家咯咯笑！不過要記得拿到糖果後一定要說『謝謝』喔。", "keywords": ["giggle", "thank you"] },
      { "id": 5, "speaker": "Lily", "avatar": "👧", "en": "Polite monsters get the biggest chocolate bars on Halloween night!", "zh": "有禮貌的可愛小怪物，在萬聖夜才能拿到最大條的巧克力棒！", "keywords": ["monsters", "polite"] }
    ],
    "vocabulary": [
      { "word": "rhyme", "phonetic": "/raɪm/", "pos": "n.", "zh": "押韻兒歌、韻文", "example": "Nursery rhymes help young children master phonics." },
      { "word": "giggle", "phonetic": "/ˈɡɪɡ.əl/", "pos": "v.", "zh": "咯咯傻笑、竊笑", "example": "The children giggled at the silly clown." },
      { "word": "polite", "phonetic": "/pəˈlaɪt/", "pos": "adj.", "zh": "有禮貌的、客氣的", "example": "It is polite to hold the door open for others." }
    ],
    "dailyPhrase": { "en": "Trick or treat!", "zh": "不給糖就搗蛋！（萬聖節最重要的通關密語）" },
    "cultureTip": "「Trick or treat, smell my feet...」是全美兒童代代相傳的民間搞笑打油詩，孩子們雖然嘴上唱著，但敲門要糖時依舊會遵守禮貌說 Thank you！"
  },

  # 10-30 [國小中高]
  {
    "id": "dialogue-1030",
    "date": "10-30",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "節慶安全",
    "topic": {
      "en": "Halloween Safety Rules",
      "zh": "萬聖節夜間踩街安全守則"
    },
    "situation": "萬聖節前夕放學前，導師提醒班長 Emma 和 Lucas 晚上外出 Trick-or-Treat 時必須牢記的安全守則。",
    "speakers": {
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1030.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Emma", "avatar": "👧", "en": "Lucas, our teacher reminded us to review safety guidelines before tomorrow night's trick-or-treating.", "zh": "Lucas，老師提醒我們在明晚外出要糖前，一定要把安全守則複習一遍。", "keywords": ["safety", "guidelines"] },
      { "id": 2, "speaker": "Lucas", "avatar": "👦", "en": "Rule number one: always stay with a trusted adult and travel in a group, never alone.", "zh": "第一條：一定要跟信任的家長在一起，並且結伴同行，絕不落單。", "keywords": ["trusted", "group"] },
      { "id": 3, "speaker": "Emma", "avatar": "👧", "en": "Rule two: attach reflective tape to dark costumes and carry a bright flashlight so cars can spot us.", "zh": "第二條：在深色服裝上貼反光貼條，並攜帶明亮手電筒，讓行駛的車輛能看見我們。", "keywords": ["reflective", "flashlight"] },
      { "id": 4, "speaker": "Lucas", "avatar": "👦", "en": "And rule three: never eat unsealed treats until parents inspect all candy at home.", "zh": "還有第三條：包裝沒有密封的糖果千萬不能吃，一定要等回家讓爸媽檢查過才能吃。", "keywords": ["inspect", "unsealed"] },
      { "id": 5, "speaker": "Emma", "avatar": "👧", "en": "Safety first ensures everyone has a fun, spooky, and sweet celebration!", "zh": "安全第一才能確保每個人都擁有一個好玩、搞怪又甜蜜的節慶！", "keywords": ["safety first", "sweet"] }
    ],
    "vocabulary": [
      { "word": "reflective", "phonetic": "/rɪˈflek.tɪv/", "pos": "adj.", "zh": "反光的、反射的", "example": "Cyclists should wear reflective vests at night." },
      { "word": "inspect", "phonetic": "/ɪnˈspekt/", "pos": "v.", "zh": "檢查、審視", "example": "Customs officers inspect luggage at the airport." },
      { "word": "guideline", "phonetic": "/ˈɡaɪd.laɪn/", "pos": "n.", "zh": "準則、指示方針", "example": "Follow all safety guidelines during lab experiments." }
    ],
    "dailyPhrase": { "en": "Safety first.", "zh": "安全第一。（各項戶外活動的首要準則）" },
    "cultureTip": "北美每年萬聖節各警察局和學校都會發放「Halloween Safety Sheet」，提醒孩童「行走在人行道」、「穿反光鞋」以及「只敲門前亮燈有裝飾的人家」。"
  },

  # 10-31 [國中挑戰]
  {
    "id": "dialogue-1031",
    "date": "10-31",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "萬聖狂歡",
    "topic": {
      "en": "Happy Halloween! Costume Party Fun",
      "zh": "萬聖夜變裝派對狂歡"
    },
    "situation": "10月31日萬聖夜，學校體育館正舉辦熱鬧的變裝舞會，Kevin 和 Zoe 拿著滿滿的糖果籃在拍照區留念。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "🧑", "gender": "male", "voice": "en-US-ChristopherNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1031.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "🧑", "en": "Happy Halloween, Zoe! Whoa, your robotic dragon costume with motorized wings is unbelievable!", "zh": "萬聖節快樂 Zoe！哇，妳那套有電動機械雙翼的機器暴龍裝簡直不可思議！", "keywords": ["Happy Halloween", "robotic", "motorized"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Thanks Kevin! And you dressed up as a 1980s retro arcade game character? Spot on!", "zh": "謝謝 Kevin！你打扮成 1980 年代復古街機遊戲角色嗎？傳神極了！", "keywords": ["retro", "arcade"] },
      { "id": 3, "speaker": "Kevin", "avatar": "🧑", "en": "I attached flashing pixel LEDs to my jacket. Let's enter the grand costume contest!", "zh": "我在外套上裝了閃爍的像素 LED 燈。我們一起去報名全校最佳服裝大賽吧！", "keywords": ["contest", "pixel"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "The DJ is playing spooky disco beats, and the photo booth has funny monster props.", "zh": "DJ 正在放超帶感的萬聖迪斯可舞曲，拍照亭那邊還有搞怪小怪獸道具呢。", "keywords": ["props", "disco"] },
      { "id": 5, "speaker": "Kevin", "avatar": "🧑", "en": "October ends on such a joyful high note! Trick or treat, and have a spooktacular night!", "zh": "十月就在這麼歡樂的高潮中劃下句點！不給糖就搗蛋，祝大家萬聖夜大狂歡！", "keywords": ["high note", "spooktacular"] }
    ],
    "vocabulary": [
      { "word": "arcade", "phonetic": "/ɑːrˈkeɪd/", "pos": "n.", "zh": "遊樂場、電子遊戲街機", "example": "We played pinball at the vintage arcade." },
      { "word": "prop", "phonetic": "/prɑːp/", "pos": "n.", "zh": "小道具、舞美配件", "example": "The theater backstage was filled with quirky props." },
      { "word": "motorized", "phonetic": "/ˈmoʊ.t̬ə.raɪzd/", "pos": "adj.", "zh": "電動的、裝有馬達動力的", "example": "The motorized gate opened smoothly." }
    ],
    "dailyPhrase": { "en": "End on a high note.", "zh": "在最高潮中圓滿落幕。" },
    "cultureTip": "「Spooktacular」是結合「Spooky（搞怪驚悚）」與「Spectacular（盛大精彩）」的英文造詞，用來祝福萬聖夜過得精彩熱鬧！"
  }
]

def main():
    if not os.path.exists(DATA_FILE):
        print("Data file not found.")
        return

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        existing = json.load(f)

    existing_dates = {item['date'] for item in existing}

    added_count = 0
    for new_item in OCTOBER_DIALOGUES:
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

    print(f"成功新增 10 月份共 {added_count} 篇對話！目前資料庫總計共有 {len(existing)} 篇對話 (涵蓋 9 月與 10 月共 61 天)。")

if __name__ == '__main__':
    main()
