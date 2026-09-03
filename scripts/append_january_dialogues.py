#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次建立 1 月份生活對話 (01-01 至 01-31，共 31 篇)
涵蓋元旦日出、期末大考衝刺、寒假展開、年貨大街、除夕圍爐與發紅包！
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'dialogues.json')

JANUARY_DIALOGUES = [
  # 01-01 [國小初階]
  {
    "id": "dialogue-0101",
    "date": "01-01",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "新年元旦",
    "topic": {
      "en": "Watching the First Sunrise of the New Year",
      "zh": "迎接新年的第一道燦爛曙光"
    },
    "situation": "1月1日清晨，Toby 和妹妹 Zoe 穿著厚羽絨外套站在陽台，迎接新年的第一道金色晨光。",
    "speakers": {
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0101.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Toby", "avatar": "👦", "en": "Zoe, look toward the eastern mountains! The deep night sky is turning peach and gold!", "zh": "Zoe，往東邊的山頭看！深黑的夜空正在轉成粉桃色和耀眼金色！", "keywords": ["mountains", "eastern", "peach"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Here comes the sun! It peeks out like a giant blazing orange coin!", "zh": "太陽出來了！它像一枚巨大的燃燒金幣一樣探出頭來！", "keywords": ["blazing", "coin", "peeks"] },
      { "id": 3, "speaker": "Toby", "avatar": "👦", "en": "Happy New Year! Today is January first, the very first morning of a brand new calendar!", "zh": "新年快樂！今天是元月一日，全新日曆上的第一個早晨！", "keywords": ["January", "calendar", "Happy New Year"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "The warm morning sunlight feels gentle on my cold nose.", "zh": "溫暖的晨光照在我冰涼的鼻尖上好舒服喔。", "keywords": ["gentle", "sunlight"] },
      { "id": 5, "speaker": "Toby", "avatar": "👦", "en": "Close your eyes and make a fresh wish. May this new year bring endless joy and healthy smiles!", "zh": "閉上眼睛許個新願望吧。願這新的一年帶來滿滿的快樂與健康的微笑！", "keywords": ["wish", "endless"] }
    ],
    "vocabulary": [
      { "word": "blazing", "phonetic": "/ˈbleɪ.zɪŋ/", "pos": "adj.", "zh": "熾熱燃燒的、耀眼奪目的", "example": "The blazing morning sun climbed over the horizon." },
      { "word": "calendar", "phonetic": "/ˈkæl.ən.dɚ/", "pos": "n.", "zh": "日曆、月曆", "example": "Hang the new scenic calendar on the wall." },
      { "word": "gentle", "phonetic": "/ˈdʒen.t̬əl/", "pos": "adj.", "zh": "溫和的、輕柔的", "example": "A gentle morning breeze ruffled the curtains." }
    ],
    "dailyPhrase": { "en": "A brand new start.", "zh": "嶄新的開始、全新的起點。" },
    "cultureTip": "元旦清晨觀看「First Sunrise（新年第一道曙光）」在多國文化中象徵洗滌過去一年的疲憊，迎來生機盎然的吉祥好彩頭。"
  },

  # 01-02 [國小中高]
  {
    "id": "dialogue-0102",
    "date": "01-02",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "新年目標",
    "topic": {
      "en": "Writing My New Year's Resolution List",
      "zh": "在日記本寫下我的新年新希望"
    },
    "situation": "新年假期第二天下午，Lucas 和媽媽在書桌前打開嶄新的筆記本，用心寫下今年想培養的好習慣。",
    "speakers": {
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mom": { "role": "媽媽", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0102.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lucas", "avatar": "👦", "en": "Mom, I bought a new royal blue journal! How many New Year's resolutions should I set?", "zh": "媽媽，我買了一本寶藍色新日記本！我應該訂幾個新年新希望比較好呢？", "keywords": ["journal", "resolutions"] },
      { "id": 2, "speaker": "Mom", "avatar": "👩", "en": "Quality is far better than quantity, Lucas. Picking three specific, achievable goals is much wiser than twenty vague wishes.", "zh": "質遠比量重要喔 Lucas。挑選三個具體、做得到的目標，比列出二十個空泛的願望明智得多。", "keywords": ["achievable", "quantity"] },
      { "id": 3, "speaker": "Lucas", "avatar": "👦", "en": "Goal number one: practice conversational English for ten minutes every single morning before school.", "zh": "第一個目標：每天早自習前堅持練習十分鐘生活英語對話。", "keywords": ["conversational", "practice"] },
      { "id": 4, "speaker": "Mom", "avatar": "👩", "en": "Excellent and measurable! How about one physical habit and one kindness habit?", "zh": "非常棒而且可量化！那再加一個運動習慣和一個日行一善的習慣如何？", "keywords": ["measurable", "kindness"] },
      { "id": 5, "speaker": "Lucas", "avatar": "👦", "en": "Goal two: shoot fifty free throws after homework. Goal three: help clear the dinner table every evening!", "zh": "第二：寫完作業練投五十顆罰球。第三：每天晚餐後主動幫忙收拾洗碗盤！", "keywords": ["free throws", "dinner table"] }
    ],
    "vocabulary": [
      { "word": "resolution", "phonetic": "/ˌrez.əˈluː.ʃən/", "pos": "n.", "zh": "決心、決議、新年新希望", "example": "She made a firm resolution to exercise regularly." },
      { "word": "achievable", "phonetic": "/əˈtʃiː.və.bəl/", "pos": "adj.", "zh": "可達成的、切實可行的", "example": "Break large projects into small, achievable milestones." },
      { "word": "measurable", "phonetic": "/ˈmeʒ.ɚ.ə.bəl/", "pos": "adj.", "zh": "可衡量的、可量化的", "example": "Set measurable targets to track your real progress." }
    ],
    "dailyPhrase": { "en": "Quality over quantity.", "zh": "重質不重量（做事與設定目標的智慧法則）" },
    "cultureTip": "管理學著名的「SMART Principles」強調目標必須具體（Specific）、可量化（Measurable）、可達成（Achievable），成功率才會提升八倍以上！"
  },

  # 01-03 [國中挑戰]
  {
    "id": "dialogue-0103",
    "date": "01-03",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "考試準備",
    "topic": {
      "en": "Final Exam Countdown: Conquering Geometry",
      "zh": "期末考倒數：攻克幾何證明題"
    },
    "situation": "放學後的圖書館自習室裡，Mark 和 Kelly 攤開圓規與三角板，討論幾何圖形輔助線的解題盲點。",
    "speakers": {
      "Mark": { "role": "Mark", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Kelly": { "role": "Kelly", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0103.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mark", "avatar": "🧑", "en": "Kelly, our semester final exams start next Tuesday! I'm completely stuck on this circle geometry proof.", "zh": "Kelly，我們第一學期期末考下週二就要登場了！我卡在這道圓形幾何證明題完全動不了。", "keywords": ["semester final", "geometry"] },
      { "id": 2, "speaker": "Kelly", "avatar": "👧", "en": "Let me look. Ah, you need to draw an auxiliary construction line connecting the circle center to the tangent point.", "zh": "讓我看看。啊，你需要在圓心和切點之間畫一條輔助線。", "keywords": ["auxiliary", "tangent", "construction"] },
      { "id": 3, "speaker": "Mark", "avatar": "🧑", "en": "Wait, because a radius is always strictly perpendicular to the tangent line at the point of contact?", "zh": "等等，因為圓半徑永遠垂直於切點上的切線？", "keywords": ["perpendicular", "radius"] },
      { "id": 4, "speaker": "Kelly", "avatar": "👧", "en": "Bingo! That immediately creates a pair of congruent right triangles. Pythagorean theorem unlocks the rest.", "zh": "答對了！那樣立刻就造出了一對全等直角三角形，接下來用畢氏定理就能秒解了。", "keywords": ["Pythagorean", "congruent"] },
      { "id": 5, "speaker": "Mark", "avatar": "🧑", "en": "Brilliant insight! Once the auxiliary line is placed, the whole proof unravels like clockwork.", "zh": "精闢的點撥！輔助線一畫上去，整個證明過程瞬間迎刃而解！", "keywords": ["unravels", "clockwork"] }
    ],
    "vocabulary": [
      { "word": "auxiliary", "phonetic": "/ɑːɡˈzɪl.i.er.i/", "pos": "adj.", "zh": "輔助的、備用的", "example": "Draw an auxiliary line to bisect the angle." },
      { "word": "perpendicular", "phonetic": "/ˌpɝː.pənˈdɪk.jə.lɚ/", "pos": "adj.", "zh": "垂直的、正交的", "example": "The flagpole stands perpendicular to the level ground." },
      { "word": "congruent", "phonetic": "/ˈkɑːŋ.ɡru.ənt/", "pos": "adj.", "zh": "（幾何）全等的", "example": "The two triangles are congruent in side length and angles." }
    ],
    "dailyPhrase": { "en": "Like clockwork.", "zh": "有條不紊、順利精準地運轉解開。" },
    "cultureTip": "「Pythagorean Theorem（勾股定理／畢氏定理）」是國中幾何的最核心基石，幾何證明題中畫出合適的「Auxiliary Line（輔助線）」往往是破題的關鍵靈魂。"
  },

  # 01-04 [高中進階]
  {
    "id": "dialogue-0104",
    "date": "01-04",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "行為科學",
    "topic": {
      "en": "Why New Year's Resolutions Fail by February",
      "zh": "行為科學解密：為什麼新年目標總在二月破功？"
    },
    "situation": "高中生自習室裡，Ryan 和 Olivia 探討為何高達 80% 的新年目標在一個月內夭折，以及《原子習慣》微小改變的心理機制。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0104.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "🧑", "en": "Olivia, statistical surveys show roughly eighty percent of New Year resolutions collapse by the second week of February. Why the recurring failure?", "zh": "Olivia，統計調查顯示大約百分之八十的新年決心在二月第二週前就全面崩盤。為什麼這種失敗年年重演？", "keywords": ["statistical", "collapse"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👩", "en": "People rely on fleeting bursts of initial motivation rather than redesigning their underlying environment and habit architecture.", "zh": "因為大家總是依賴短暫燃燒的初始動力，而不是去重新設計自己的底層環境與習慣架構。", "keywords": ["fleeting", "motivation", "architecture"] },
      { "id": 3, "speaker": "Ryan", "avatar": "🧑", "en": "James Clear's 'Atomic Habits' insight: you do not rise to the level of your goals; you fall to the level of your systems.", "zh": "這正是《原子習慣》作者的洞見：你不會達到你設定的目標高度，而是會跌落到你日常系統的水平。", "keywords": ["Atomic Habits", "systems"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👩", "en": "Exactly. Massive radical overhauls trigger neural resistance, whereas friction-free micro-habits—like reading just one page—bypass psychological friction.", "zh": "正是。大刀闊斧的激進改變會引發大腦神經抗拒，而無摩擦的微習慣——比如每天只讀一頁書——能巧妙繞過心理阻力。", "keywords": ["overhauls", "resistance", "friction"] },
      { "id": 5, "speaker": "Ryan", "avatar": "🧑", "en": "Make it tiny, make it obvious, and make it rewarding. Systemic design always triumphs over fragile willpower.", "zh": "讓它微小、顯而易見且富有獎勵感。系統化的設計永遠能戰勝脆弱的意志力。", "keywords": ["triumphs", "willpower"] }
    ],
    "vocabulary": [
      { "word": "fleeting", "phonetic": "/ˈfliː.t̬ɪŋ/", "pos": "adj.", "zh": "短暫的、轉瞬即逝的", "example": "Motivation is fleeting, but discipline creates lasting legacy." },
      { "word": "overhaul", "phonetic": "/ˈoʊ.vɚ.hɑːl/", "pos": "n./v.", "zh": "徹底改革、全面檢修", "example": "The school undertook a complete overhaul of its curriculum." },
      { "word": "willpower", "phonetic": "/ˈwɪlˌpaʊ.ɚ/", "pos": "n.", "zh": "意志力、自制力", "example": "Relying purely on willpower is an exhausting strategy." }
    ],
    "dailyPhrase": { "en": "Fall to the level of your systems.", "zh": "跌落到你的系統水平（習慣決定成敗）" },
    "cultureTip": "行為心理學中著名的「The False Hope Syndrome（虛假希望綜合徵）」指出，人們常對改變自我抱有不切實際的過度樂觀，唯有透過環境設計與微步前進才能打破死循環。"
  },

  # 01-05 [國小初階]
  {
    "id": "dialogue-0105",
    "date": "01-05",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "冬日戶外",
    "topic": {
      "en": "Sledding Down the Snowy Hill",
      "zh": "坐上紅色滑雪盆從小雪坡滑下"
    },
    "situation": "週日午後在社區公園的小雪坡上，Mia 和哥哥 Leo 輪流坐上塑膠滑雪板，享受風馳電掣的俯衝快感。",
    "speakers": {
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0105.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mia", "avatar": "👧", "en": "Leo, this snowy hill is packed smooth by all the neighborhood kids! Can I ride front seat?", "zh": "Leo，這座小雪坡被社區裡的小朋友踩得好平好滑喔！我可以坐前座嗎？", "keywords": ["snowy hill", "smooth"] },
      { "id": 2, "speaker": "Leo", "avatar": "👦", "en": "Hop on the red plastic sled, Mia! Grip the side rope handles tight and tuck your feet in.", "zh": "跳上紅色塑膠雪橇吧 Mia！緊緊抓牢側邊繩子把手，把腳收進來。", "keywords": ["sled", "handles", "tuck"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Ready? Giving us a big push... Three, two, one, blast off!", "zh": "準備好了嗎？我要在後面用力推一把囉…三、二、一，衝啊！", "keywords": ["blast off", "push"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "Whoosh! The cold wind is roaring past my ears! Snow spray is splashing everywhere!", "zh": "呼呼！寒風在我的耳邊呼嘯而過！白雪花花濺得到處都是！", "keywords": ["whoosh", "roaring", "splashing"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "We slid all the way to the park bench at the bottom! That was lightning fast! Let's hike back up!", "zh": "我們一路滑到了底部的公園長椅！簡直像閃電一樣快！我們再爬上去玩一次！", "keywords": ["lightning fast", "bench"] }
    ],
    "vocabulary": [
      { "word": "sled", "phonetic": "/sled/", "pos": "n./v.", "zh": "雪橇、滑雪盆、乘雪橇滑雪", "example": "Children pulled their wooden sleds up the hill." },
      { "word": "tuck", "phonetic": "/tʌk/", "pos": "v.", "zh": "塞入、捲起、收攏肢體", "example": "Tuck your elbows in during gymnastics." },
      { "word": "whoosh", "phonetic": "/wuːʃ/", "pos": "n./v.", "zh": "颼的一聲、呼嘯飛馳聲", "example": "The bullet train whooshed past the platform." }
    ],
    "dailyPhrase": { "en": "Lightning fast.", "zh": "快如閃電、神速飛馳。" },
    "cultureTip": "「Sledding（滑雪橇／滑雪盆）」是下雪地區孩子們冬天最平民、最刺激的戶外遊戲，只需要一個幾塊錢的塑膠雪盆，就能在任何坡道玩上一整個下午！"
  },

  # 01-06 [國小中高]
  {
    "id": "dialogue-0106",
    "date": "01-06",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "趣味物理",
    "topic": {
      "en": "Why Do Ponds Freeze from the Top Down?",
      "zh": "為什麼池塘結冰是從水面開始而不是水底？"
    },
    "situation": "自然課觀察校園生態池時，Sam 和 Emily 發現水面結了一層薄冰，而水底的金魚依然在游動。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emily": { "role": "Emily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0106.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Emily, look at our school pond! The surface is frozen hard, but the goldfish are swimming underneath!", "zh": "Emily，看我們學校的生態池！水面結了一層硬冰，但是水底的金魚居然還在游動！", "keywords": ["frozen", "underneath"] },
      { "id": 2, "speaker": "Emily", "avatar": "👧", "en": "Isn't water amazing? Most liquids become denser as they get colder and sink to the bottom.", "zh": "水真的很神奇對吧？大部分液體越冷密度越大，會直接沉到底部。", "keywords": ["denser", "liquids"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Right, but water has a unique superpower: it reaches maximum density at four degrees Celsius!", "zh": "對，但水有一項獨特的超能力：它在攝氏四度時密度達到最大！", "keywords": ["density", "superpower", "Celsius"] },
      { "id": 4, "speaker": "Emily", "avatar": "👧", "en": "When water drops below four degrees and turns into ice at zero, it expands and becomes lighter!", "zh": "當水溫降到四度以下、並在零度結成冰時，它反而會膨脹而且變得更輕！", "keywords": ["expands", "lighter"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "So floating ice acts like an insulating thermal blanket, keeping deep water warm enough for aquatic life to survive!", "zh": "所以浮在水面的冰塊就像一條保溫隔熱毯，讓底層深水維持在足夠溫度，讓水生生物順利存活！", "keywords": ["insulating", "aquatic", "blanket"] }
    ],
    "vocabulary": [
      { "word": "density", "phonetic": "/ˈden.sə.t̬i/", "pos": "n.", "zh": "密度、稠密度", "example": "Oil floats on water because it has lower density." },
      { "word": "insulate", "phonetic": "/ˈɪn.sə.leɪt/", "pos": "v.", "zh": "隔熱、隔音、絕緣", "example": "Thick wool insulates our bodies from bitter cold." },
      { "word": "aquatic", "phonetic": "/əˈkwæt̬.ɪk/", "pos": "adj.", "zh": "水生的、水中的", "example": "Coral reefs provide habitats for diverse aquatic animals." }
    ],
    "dailyPhrase": { "en": "A thermal blanket.", "zh": "保溫毯、隔熱防護層。" },
    "cultureTip": "水的「反常膨脹（Anomalous Expansion）」是地球生命演化最不可思議的奇蹟。如果冰比水重而從水底開始結冰，全世界的河流海洋早就凍成死水了！"
  },

  # 01-07 [國中挑戰]
  {
    "id": "dialogue-0107",
    "date": "01-07",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "考試後放鬆",
    "topic": {
      "en": "The Last Exam Bell Rings: Freedom!",
      "zh": "期末考最後一節鐘聲響起：放假啦！"
    },
    "situation": "週五下午最後一堂期末考鐘聲響起，Ethan 和同學 Zoe 走出試場，整個人如釋重負，迎接寒假到來。",
    "speakers": {
      "Ethan": { "role": "Ethan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0107.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ethan", "avatar": "👦", "en": "Hear that final bell, Zoe? Put your pens down! The semester is officially wrapped up!", "zh": "聽見那最後一節鐘聲了嗎 Zoe？停筆！這學期正式圓滿結束啦！", "keywords": ["wrapped up", "final bell"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Sweet freedom! No more quadratic equations, historical timelines, or pop quizzes for three whole weeks!", "zh": "甜蜜的自由！接下來整整三個星期，再也沒有一元二次方程式、歷史年代線，或是突擊小考了！", "keywords": ["freedom", "equations"] },
      { "id": 3, "speaker": "Ethan", "avatar": "👦", "en": "My brain feels like a sponge that has been squeezed dry. What's your immediate celebration plan?", "zh": "我的大腦感覺像一塊被擠得乾乾的海綿。妳等一下第一時間要怎麼慶祝？", "keywords": ["sponge", "squeezed"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Sleep in tomorrow until eleven, then binge-watch my favorite fantasy anime with a giant tub of butter popcorn!", "zh": "明天先睡到自然醒到十一點，然後抱著一大桶奶油爆米花追我最愛的奇幻動漫！", "keywords": ["binge-watch", "sleep in"] },
      { "id": 5, "speaker": "Ethan", "avatar": "👦", "en": "Count me in for movie night! We survived the semester, Zoe; high five!", "zh": "電影之夜算我一份！我們成功熬過這學期了 Zoe，擊掌！", "keywords": ["survived", "high five"] }
    ],
    "vocabulary": [
      { "word": "freedom", "phonetic": "/ˈfriː.dəm/", "pos": "n.", "zh": "自由、解脫", "example": "Holiday bells sounded the sweet chime of freedom." },
      { "word": "binge", "phonetic": "/bɪndʒ/", "pos": "v./n.", "zh": "狂看、連續狂做（如追劇、狂吃）", "example": "We binged the entire detective series in one weekend." },
      { "word": "sponge", "phonetic": "/spʌndʒ/", "pos": "n.", "zh": "海綿、吸收力強的人", "example": "Young minds absorb foreign languages like a sponge." }
    ],
    "dailyPhrase": { "en": "Sleep in.", "zh": "睡到自然醒、睡懶覺（放假最幸福的事）" },
    "cultureTip": "「Binge-watch」是《牛津字典》近年收錄的熱門詞，形容一口氣連續觀看好幾集甚至一整季電視影集或動漫的狂歡追劇行為。"
  },

  # 01-08 [高中進階]
  {
    "id": "dialogue-0108",
    "date": "01-08",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "文化思辨",
    "topic": {
      "en": "Solar New Year vs. Lunar New Year Celebrations",
      "zh": "陽曆跨年與農曆春節：兩種截然不同的時間美學"
    },
    "situation": "高中跨文化交流社課堂上，Alex 和 Sophia 就西方陽曆跨年（Solar New Year）與東亞農曆春節（Lunar New Year）的文化意涵進行對比剖析。",
    "speakers": {
      "Alex": { "role": "Alex", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Sophia": { "role": "Sophia", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0108.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Alex", "avatar": "🧑", "en": "Sophia, we just celebrated January first with parties and fireworks, yet in East Asia, the true monumental holiday is Lunar New Year in late January or February.", "zh": "Sophia，我們剛以派對和煙火慶祝了元旦，但在東亞，真正最隆重盛大的節慶是落在一月下旬或二月的農曆春節。", "keywords": ["monumental", "Lunar New Year"] },
      { "id": 2, "speaker": "Sophia", "avatar": "👩", "en": "The psychological distinction is fascinating. Western New Year feels forward-looking, individualistic, and centered on ambitious personal resolutions.", "zh": "兩者的心理意涵截然不同。西方跨年給人向前看、強調個人主義且著重於立下雄心勃勃的個人目標。", "keywords": ["individualistic", "distinction"] },
      { "id": 3, "speaker": "Alex", "avatar": "🧑", "en": "Whereas Lunar New Year is deeply cyclical, ancestral, and communal—revolving around intergenerational homecoming and honoring roots.", "zh": "而農曆新年則深深植根於循環時序、祖蔭與宗族共同體——核心在於跨世代的千里返鄉團聚與飲水思源。", "keywords": ["ancestral", "communal", "intergenerational"] },
      { "id": 4, "speaker": "Sophia", "avatar": "👩", "en": "Precisely. The massive travel phenomenon known as 'Chunyun' reflects a sacred cultural obligation: returning to the family hearth regardless of distance.", "zh": "正是。被稱為『春運』的龐大人潮遷徙現象反映了一種神聖的文化承諾：無論路途多遙遠，都要回到家族溫暖的灶前團圓。", "keywords": ["Chunyun", "obligation"] },
      { "id": 5, "speaker": "Alex", "avatar": "🧑", "en": "One celebrates linear progress of chronological time; the other honors cyclical renewal of human bonds. Both enrich humanity's temporal wisdom.", "zh": "一種慶祝時間軸的線性前進，另一種頌揚人際情感的週期性再生。兩者共同豐富了人類對時間深邃的哲學智慧。", "keywords": ["chronological", "temporal"] }
    ],
    "vocabulary": [
      { "word": "communal", "phonetic": "/kəˈmjuː.nəl/", "pos": "adj.", "zh": "群體的、社區共有的、公眾的", "example": "The harvest feast was a joyous communal affair." },
      { "word": "obligation", "phonetic": "/ˌɑː.bləˈɡeɪ.ʃən/", "pos": "n.", "zh": "義務、責任、承諾", "example": "Fulfilling filial obligations is deeply revered in Asian traditions." },
      { "word": "temporal", "phonetic": "/ˈtem.pɚ.əl/", "pos": "adj.", "zh": "時間的、世俗光陰的", "example": "Music creates spatial architecture within temporal flow." }
    ],
    "dailyPhrase": { "en": "Honor your roots.", "zh": "不忘本、尋根感恩。" },
    "cultureTip": "「Chunyun（春運）」被金氏世界紀錄列為人類地表最大規模的年度週期性人口遷徙，數億人跨越千山萬水只為吃上一頓除夕夜的家鄉年夜飯。"
  },

  # 01-09 [國小初階]
  {
    "id": "dialogue-0109",
    "date": "01-09",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "冬日美食",
    "topic": {
      "en": "Steaming Hot Roasted Sweet Potatoes",
      "zh": "熱氣騰騰香甜的現烤地瓜"
    },
    "situation": "放學走過街角，Ruby 和 Lucas 被路邊傳統紅鐵桶烤地瓜攤飄出的焦糖蜜香吸引。",
    "speakers": {
      "Ruby": { "role": "Ruby", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0109.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ruby", "avatar": "👧", "en": "Lucas, smell that caramelized aroma in the chilly air! The street vendor is pulling roasted sweet potatoes out of the big iron drum!", "zh": "Lucas，聞聞冷空氣裡那個焦糖香味！路邊攤阿伯正從大鐵桶裡夾出烤地瓜耶！", "keywords": ["caramelized", "sweet potatoes", "aroma"] },
      { "id": 2, "speaker": "Lucas", "avatar": "👦", "en": "Let's buy a big plump one to share! Hold the paper bag carefully; it's piping hot!", "zh": "我們買一顆大顆飽滿的平分吃吧！紙袋要小心拿喔，剛出爐燙得很！", "keywords": ["piping hot", "plump"] },
      { "id": 3, "speaker": "Ruby", "avatar": "👧", "en": "Break it in half with both hands... Whoosh! Look at that golden yellow steam!", "zh": "用雙手把它掰成兩半…呼！看那金黃色的熱氣冒出來！", "keywords": ["golden yellow", "steam"] },
      { "id": 4, "speaker": "Lucas", "avatar": "👦", "en": "The flesh is sweet, velvety, and oozing natural honey syrup near the charred skin!", "zh": "地瓜肉又香甜又綿密，靠近焦香外皮的地方還流出天然蜜汁呢！", "keywords": ["velvety", "oozing", "charred"] },
      { "id": 5, "speaker": "Ruby", "avatar": "👧", "en": "Blowing on a hot sweet potato on a freezing January day warms your hands and your belly!", "zh": "在一月寒風中吹著熱呼呼的烤地瓜，暖了手心也暖了肚皮！", "keywords": ["freezing", "belly"] }
    ],
    "vocabulary": [
      { "word": "piping hot", "phonetic": "/ˌpaɪ.pɪŋ ˈhɑːt/", "pos": "adj.", "zh": "滾燙熱騰騰的（剛出爐食物）", "example": "Serve the mushroom soup piping hot." },
      { "word": "ooze", "phonetic": "/uːz/", "pos": "v.", "zh": "緩緩滲出、流出蜜汁", "example": "Melted dark chocolate oozed from the warm lava cake." },
      { "word": "charred", "phonetic": "/tʃɑːrd/", "pos": "adj.", "zh": "烤焦的、有炭烤微焦香氣的", "example": "The pizza had a deliciously charred crust." }
    ],
    "dailyPhrase": { "en": "Piping hot.", "zh": "滾燙熱騰騰（形容剛烤好或剛煮熟冒熱氣的美味佳餚）" },
    "cultureTip": "傳統炭烤地瓜（Roasted Sweet Potatoes）在台灣與東亞是冬日最溫暖的街頭庶民美食，手捧熱熱紙袋邊吹邊吃是幾代人的集體溫馨記憶。"
  },

  # 01-10 [國小中高]
  {
    "id": "dialogue-0110",
    "date": "01-10",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "新年掃除",
    "topic": {
      "en": "Spring Cleaning: Dusting the Ceilings",
      "zh": "年前大掃除：掃除天花板蜘蛛網"
    },
    "situation": "寒假第一個週末，Ben 和 Tina 在家裡挽起袖子、戴上紙口罩，幫忙進行過年前的大掃除。",
    "speakers": {
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Tina": { "role": "Tina", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0110.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ben", "avatar": "👦", "en": "Tina, hand me that long extendable feather duster! I'm sweeping down cobwebs from the ceiling corners.", "zh": "Tina，把那支長長的伸縮除塵撢遞給我！我來掃掉天花板角落的蜘蛛網。", "keywords": ["extendable", "duster", "ceiling"] },
      { "id": 2, "speaker": "Tina", "avatar": "👧", "en": "Make sure to wear your mask so you don't sneeze from the falling dust particles.", "zh": "一定要戴好口罩喔，才不會被落下來的灰塵嗆到打噴嚏。", "keywords": ["sneeze", "particles"] },
      { "id": 3, "speaker": "Ben", "avatar": "👦", "en": "Why do we always clean the entire house from top to bottom before the Lunar New Year?", "zh": "為什麼我們農曆年前一定要由上到下把整間屋子徹底大掃除呢？", "keywords": ["top to bottom", "clean"] },
      { "id": 4, "speaker": "Tina", "avatar": "👧", "en": "Cultural tradition says sweeping out old dust sweeps away all lingering misfortune, making room for good luck!", "zh": "文化傳統說掃掉舊灰塵能掃除過去一年所有殘留的厄運，騰出空間迎接好運到來！", "keywords": ["misfortune", "lingering", "luck"] },
      { "id": 5, "speaker": "Ben", "avatar": "👦", "en": "Now the walls are spotless and gleaming! Bring on the auspicious new year!", "zh": "現在牆角一塵不染、閃閃發亮！吉祥的新年快快到來吧！", "keywords": ["spotless", "auspicious"] }
    ],
    "vocabulary": [
      { "word": "extendable", "phonetic": "/ɪkˈsten.də.bəl/", "pos": "adj.", "zh": "可伸長伸縮的", "example": "An extendable ladder reached the attic." },
      { "word": "spotless", "phonetic": "/ˈspɑːt.ləs/", "pos": "adj.", "zh": "一塵不染的、潔淨無瑕的", "example": "The kitchen counter was wiped spotless." },
      { "word": "auspicious", "phonetic": "/ɑːˈspɪʃ.əs/", "pos": "adj.", "zh": "吉祥的、吉利的、大吉大利的", "example": "Red is considered an auspicious color in Chinese culture." }
    ],
    "dailyPhrase": { "en": "From top to bottom.", "zh": "從頭到尾、從上到下徹底清理。" },
    "cultureTip": "華人習俗在農曆十二月二十四日「送神」後開始「清屯（大掃除）」，但到了大年初一到初五則忌諱掃地倒垃圾，象徵把財氣掃出門外。"
  },

  # 01-11 [國中挑戰]
  {
    "id": "dialogue-0111",
    "date": "01-11",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "寒假志工",
    "topic": {
      "en": "Volunteering at the Animal Shelter in Winter",
      "zh": "寒冬前往動物收容所當毛小孩志工"
    },
    "situation": "寒假平日上午，Mark 和 Kelly 穿著防寒防水工作服，來到流浪動物之家幫忙鋪毛毯與餵食小狗。",
    "speakers": {
      "Mark": { "role": "Mark", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Kelly": { "role": "Kelly", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0111.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kelly", "avatar": "👧", "en": "Mark, grab that stack of clean donated fleece blankets! We need to line the puppy kennels.", "zh": "Mark，拿那疊乾淨的愛心捐贈羊羔絨毛毯！我們要把幼犬狗舍鋪暖活。", "keywords": ["fleece", "kennels"] },
      { "id": 2, "speaker": "Mark", "avatar": "🧑", "en": "Concrete kennel floors get icy cold in January. Thick blankets keep their joints warm and comfortable.", "zh": "一月份水泥狗舍地面冰涼刺骨。厚毛毯能保護牠們的關節溫暖舒適。", "keywords": ["concrete", "joints"] },
      { "id": 3, "speaker": "Kelly", "avatar": "👧", "en": "Look at that rescue beagle wagging his tail! He's leaning against the kennel door begging for a head scratch.", "zh": "看那隻收容米格魯正狂搖尾巴呢！牠把頭貼在狗舍門邊討摸摸。", "keywords": ["beagle", "wagging", "rescue"] },
      { "id": 4, "speaker": "Mark", "avatar": "🧑", "en": "Animals need social affection and emotional warmth just as much as physical food and shelter.", "zh": "動物對陪伴關愛和情感溫暖的渴望，一點也不亞於對食物與遮蔽處的需求。", "keywords": ["affection", "shelter"] },
      { "id": 5, "speaker": "Kelly", "avatar": "👧", "en": "Spending our winter break volunteering here brings more genuine satisfaction than any video game ever could.", "zh": "寒假來這裡當志工陪伴牠們，帶來的真實踏實成就感遠超任何電玩遊戲。", "keywords": ["satisfaction", "volunteering"] }
    ],
    "vocabulary": [
      { "word": "kennel", "phonetic": "/ˈken.əl/", "pos": "n.", "zh": "狗舍、犬舍", "example": "The boarding kennel was clean and heated." },
      { "word": "fleece", "phonetic": "/fliːs/", "pos": "n.", "zh": "羊羔絨、抓絨布料", "example": "A fleece jacket traps body heat effectively." },
      { "word": "affection", "phonetic": "/əˈfek.ʃən/", "pos": "n.", "zh": "喜愛、深厚關愛", "example": "Children showering affection on their rescue puppy." }
    ],
    "dailyPhrase": { "en": "Wag one's tail.", "zh": "（小狗）高興地搖尾巴。" },
    "cultureTip": "近年許多中學提倡「Service Learning（服務學習）」，寒假參與流浪動物收容照護，培養學生同理心與終身愛護生命的動保意識。"
  },

  # 01-12 [高中進階]
  {
    "id": "dialogue-0112",
    "date": "01-12",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "生物生理學",
    "topic": {
      "en": "Brown Adipose Tissue and Cold Adaptation",
      "zh": "人體禦寒黑科技：棕色脂肪如何燃脂產熱？"
    },
    "situation": "高中生物醫學讀書會上，Ryan 與 Olivia 探討人體在低溫刺激下如何激活「棕色脂肪組織（BAT）」進行非顫抖性產熱。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0112.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "🧑", "en": "Olivia, I read that regular exposure to cold weather can actually enhance metabolic health through brown fat activation.", "zh": "Olivia，我讀到定期接觸適度低溫環境，居然能藉由激活體內的棕色脂肪來改善代謝健康。", "keywords": ["metabolic", "activation"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👩", "en": "Yes! Unlike ordinary white adipose tissue that stores surplus calories as lipid droplets, brown adipose tissue burns energy directly.", "zh": "是的！不同於一般儲存多餘卡路里的白色脂肪組織，棕色脂肪組織（BAT）會直接燃燒能量。", "keywords": ["adipose", "calories", "droplets"] },
      { "id": 3, "speaker": "Ryan", "avatar": "🧑", "en": "Because its cells are densely packed with iron-rich mitochondria that express uncoupling protein 1?", "zh": "因為它的細胞內富含大量的含鐵粒線體，並且高表現解偶聯蛋白 1（UCP1）？", "keywords": ["mitochondria", "uncoupling"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👩", "en": "Precisely. Instead of generating ATP, UCP1 short-circuits the proton gradient, dissipating energy purely as thermal heat to defend body temperature.", "zh": "正是如此。UCP1 不合成 ATP，而是短路質子梯度，將能量純粹轉化為熱能發散出來維持體溫。", "keywords": ["gradient", "dissipating", "thermal"] },
      { "id": 5, "speaker": "Ryan", "avatar": "🧑", "en": "So shivering isn't the body's only defense; non-shivering thermogenesis is an elegant evolutionary bio-heater.", "zh": "所以發抖打顫並不是人體禦寒的唯一手段，非顫抖性產熱更是一套精巧的生物演化電熱器。", "keywords": ["shivering", "thermogenesis"] }
    ],
    "vocabulary": [
      { "word": "adipose", "phonetic": "/ˈæd.ə.poʊs/", "pos": "adj.", "zh": "脂肪的、脂肪組織的", "example": "Adipose tissue acts as both energy reserve and endocrine organ." },
      { "word": "mitochondria", "phonetic": "/ˌmaɪ.toʊˈkɑːn.dri.ə/", "pos": "n.", "zh": "粒線體（細胞的能量工廠）", "example": "Mitochondria produce ATP necessary for cellular activity." },
      { "word": "dissipate", "phonetic": "/ˈdɪs.ə.peɪt/", "pos": "v.", "zh": "消散、耗散（熱能或氣體）", "example": "The heatsink dissipates excess computer processing heat." }
    ],
    "dailyPhrase": { "en": "Energy reserve.", "zh": "能量儲備、熱量庫存。" },
    "cultureTip": "成人體內仍保留少量棕色脂肪（主要分佈在鎖骨與頸後）。近年科學家研究「Cold Therapy（冷水浴與低溫適應）」正是著眼於其提升胰島素敏感度與燃脂潛力。"
  },

  # 01-13 [國小初階]
  {
    "id": "dialogue-0113",
    "date": "01-13",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "春節文化",
    "topic": {
      "en": "Writing Chinese Calligraphy Spring Couplets",
      "zh": "沾紅墨水手寫新春吉祥春聯"
    },
    "situation": "書法文化營上，Toby 和妹妹 Zoe 穿上圍裙，拿毛筆在喜氣的大紅灑金宣紙上寫下「春」和「福」。",
    "speakers": {
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0113.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Toby", "avatar": "👦", "en": "Zoe, dip your soft brush gently into black ink! Keep your wrist upright and relaxed.", "zh": "Zoe，毛筆輕輕沾一點黑墨汁！手腕要懸空立直、放輕鬆。", "keywords": ["wrist", "ink", "brush"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "I'm writing the Chinese character 'Fu' for good fortune on this square red paper with golden specks!", "zh": "我在這張帶金箔碎屑的正方形紅紙上寫一個『福』字！", "keywords": ["fortune", "specks"] },
      { "id": 3, "speaker": "Toby", "avatar": "👦", "en": "Why do people paste the 'Fu' character upside down on their front doors?", "zh": "為什麼大家都要把『福』字倒過來貼在大門上呢？", "keywords": ["upside down", "doors"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Because in Mandarin, 'upside down' sounds identical to 'arrived'! Pasting it upside down means fortune has arrived!", "zh": "因為在中文裡，『倒』跟『到』發音一模一樣！倒過來貼代表『福氣到家門』囉！", "keywords": ["identical", "arrived"] },
      { "id": 5, "speaker": "Toby", "avatar": "👦", "en": "What a brilliant wordplay tradition! May good fortune arrive at everyone's doorstep!", "zh": "好巧妙的諧音字雙關傳統喔！願滿滿的福氣降臨在每個人的家門口！", "keywords": ["wordplay", "doorstep"] }
    ],
    "vocabulary": [
      { "word": "fortune", "phonetic": "/ˈfɔːr.tʃuːn/", "pos": "n.", "zh": "福氣、好運、財富", "example": "May the new year bring health and good fortune." },
      { "word": "wordplay", "phonetic": "/ˈwɝːd.pleɪ/", "pos": "n.", "zh": "文字遊戲、雙關語", "example": "Puns and wordplay make the story amusing." },
      { "word": "speck", "phonetic": "/spek/", "pos": "n.", "zh": "微小斑點、碎屑", "example": "Golden specks glittered on the crimson paper." }
    ],
    "dailyPhrase": { "en": "Fortune has arrived!", "zh": "福到了！好運到家！" },
    "cultureTip": "貼春聯（Spring Couplets）是農曆新年的靈魂習俗，將「福」字倒貼取「福倒（到）」的吉祥諧音，祈願新的一年五福臨門。"
  },

  # 01-14 [國中挑戰]
  {
    "id": "dialogue-0114",
    "date": "01-14",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "春節年貨",
    "topic": {
      "en": "Bustling Crowds at the Lunar New Year Market",
      "zh": "熱鬧滾滾的年貨大街試吃採買"
    },
    "situation": "週日午後，Sarah 和 Jake 跟隨父母走進熙熙攘攘的年貨大街，紅布棚下攤商熱情叫賣試吃。",
    "speakers": {
      "Sarah": { "role": "Sarah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Jake": { "role": "Jake", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0114.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sarah", "avatar": "👧", "en": "Jake, stay close in the crowd! The whole festive market is shoulder-to-shoulder under bright red paper lanterns!", "zh": "Jake，在人群裡跟緊點！在明亮大紅燈籠下整條年貨大街擠得摩肩接踵！", "keywords": ["festive", "lanterns", "shoulder-to-shoulder"] },
      { "id": 2, "speaker": "Jake", "avatar": "👦", "en": "Listen to the vendor chant: 'Free samples of roasted pistachios and dried mango slices! Sweet and crunchy!'", "zh": "聽攤商熱情叫賣：『現烤開心果和芒果乾免費試吃！又香又脆甜！』", "keywords": ["vendor", "samples", "pistachios"] },
      { "id": 3, "speaker": "Sarah", "avatar": "👧", "en": "Try this pistachio, Jake! Pistachios are called 'happy fruit' because their cracked shells look like grinning smiles.", "zh": "嚐一顆開心果 Jake！開心果被稱為開心果是因為裂開的果殼看起來像笑瞇瞇的笑臉。", "keywords": ["pistachio", "grinning"] },
      { "id": 4, "speaker": "Jake", "avatar": "👦", "en": "And Mom is buying sweet candied winter melon strips and sesame peanut brittle for our living room candy tray.", "zh": "媽媽正在買甜甜的冬瓜糖和花生芝麻脆糖，要擺在客廳的春節全盒糖果盤裡呢。", "keywords": ["peanut brittle", "sesame"] },
      { "id": 5, "speaker": "Sarah", "avatar": "👧", "en": "The sights, smells, and cheerful laughter capture the authentic essence of holiday anticipation!", "zh": "這些色彩、香氣與歡樂笑聲，最能展現迎接過年最道地濃郁的期盼氛圍！", "keywords": ["anticipation", "authentic"] }
    ],
    "vocabulary": [
      { "word": "pistachio", "phonetic": "/pɪˈstæʃ.i.oʊ/", "pos": "n.", "zh": "開心果", "example": "Bowls of roasted salted pistachios were served to guests." },
      { "word": "brittle", "phonetic": "/ˈbrɪt̬.əl/", "pos": "n./adj.", "zh": "易碎硬糖（如花生糖）、脆弱的", "example": "Peanut brittle is a classic crunchy holiday sweet." },
      { "word": "anticipation", "phonetic": "/ænˌtɪs.əˈpeɪ.ʃən/", "pos": "n.", "zh": "期盼、期待", "example": "The children waited in eager anticipation for the fireworks." }
    ],
    "dailyPhrase": { "en": "Shoulder-to-shoulder.", "zh": "摩肩接踵、人山人海。" },
    "cultureTip": "年貨大街（New Year Market）如台北迪化街，農曆年前擺滿乾果零食、臘味乾貨，熱鬧免費試吃是體驗傳統年味的最佳現場。"
  },

  # 01-15 [國小中高]
  {
    "id": "dialogue-0115",
    "date": "01-15",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "春節美食",
    "topic": {
      "en": "Steaming Sweet Nian Gao",
      "zh": "蒸出甜蜜軟糯的年糕象徵步步高升"
    },
    "situation": "廚房大蒸籠冒出騰騰熱氣，Leo 和媽媽正在蒸紅糖紅豆年糕，準備年節甜點。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mom": { "role": "媽媽", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0115.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Mom, steam is puffing out from the bamboo steamer tiers! Is the sweet Nian Gao ready?", "zh": "媽媽，竹蒸籠一層層正冒出大團大團熱氣！甜年糕蒸熟了嗎？", "keywords": ["steamer", "Nian Gao"] },
      { "id": 2, "speaker": "Mom", "avatar": "👩", "en": "Poke a clean wooden chopstick into the center; if it comes out clean without wet batter, it's done!", "zh": "拿一根乾淨木筷子戳進正中心；如果拔出來乾乾淨淨沒有生粉漿，就是蒸透熟了！", "keywords": ["chopstick", "batter"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "It comes out completely clean! Why must every family eat Nian Gao during the New Year?", "zh": "拔出來完全乾淨！為什麼過年每家每戶都一定要吃年糕呢？", "keywords": ["family", "New Year"] },
      { "id": 4, "speaker": "Mom", "avatar": "👩", "en": "'Nian Gao' sounds exactly like 'year higher'! It carries the wish of growing taller, wiser, and more prosperous year after year.", "zh": "『年糕』發音跟『年高』完全一樣！寓意一年比一年長得更高、更有智慧、步步高升！", "keywords": ["prosperous", "higher"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Tomorrow let's dip slices in whisked egg and pan-fry them until the crust is crispy and chewy inside!", "zh": "明天我們切片沾蛋液下鍋煎，煎到外皮金黃酥脆、裡面軟糯拉絲！", "keywords": ["pan-fry", "crispy", "chewy"] }
    ],
    "vocabulary": [
      { "word": "steamer", "phonetic": "/ˈstiː.mɚ/", "pos": "n.", "zh": "蒸籠、蒸鍋", "example": "Bamboo steamers infuse buns with subtle woody aroma." },
      { "word": "batter", "phonetic": "/ˈbæt̬.ɚ/", "pos": "n.", "zh": "麵糊、粉漿", "example": "Whisk pancake batter until smooth and lump-free." },
      { "word": "prosperous", "phonetic": "/ˈprɑː.spɚ.əs/", "pos": "adj.", "zh": "繁榮富足的、興旺發達的", "example": "We wish you a healthy and prosperous new year." }
    ],
    "dailyPhrase": { "en": "Year after year.", "zh": "年復一年、歲歲年年。" },
    "cultureTip": "年糕（Nian Gao / Year Cake）以糯米粉和紅糖蒸製而成，取其諧音「年年高陞」，寓意學業進步、事業步步高升。"
  },

  # 01-16 [國中挑戰]
  {
    "id": "dialogue-0116",
    "date": "01-16",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "趣味民俗",
    "topic": {
      "en": "The Legend of the Monster Nian",
      "zh": "年獸傳說：為什麼過年要穿紅衣放鞭炮？"
    },
    "situation": "英文話劇排練時，Hannah 和 Max 討論農曆年傳說中遠古怪獸「年獸」害怕紅色、火光與巨響的由來故事。",
    "speakers": {
      "Hannah": { "role": "Hannah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Max": { "role": "Max", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0116.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Hannah", "avatar": "👧", "en": "Max, how did the ancient legend of the monster Nian shape all our Chinese New Year traditions?", "zh": "Max，遠古年獸的傳說到底是如何塑造出我們今天所有的春節習俗呢？", "keywords": ["legend", "monster Nian"] },
      { "id": 2, "speaker": "Max", "avatar": "👦", "en": "Mythology says Nian was a fierce horned beast that emerged from the deep sea at the end of every lunar year to terrorize villages.", "zh": "神話說年獸是一隻頭長尖角的兇猛怪獸，每到歲末除夕夜就會從深海爬上岸來襲擾村莊。", "keywords": ["mythology", "horned", "terrorize"] },
      { "id": 3, "speaker": "Hannah", "avatar": "👧", "en": "Until villagers discovered Nian's three mortal weaknesses: fear of the bright color red, crackling fire, and deafening noises!", "zh": "直到村民發現年獸有三大致命弱點：害怕鮮紅顏色、怕燃燒的火光，還有震耳欲聾的巨大聲響！", "keywords": ["weaknesses", "crackling", "deafening"] },
      { "id": 4, "speaker": "Max", "avatar": "👦", "en": "So people pasted red banners on doors, wore crimson garments, and lit bamboo firecrackers to scare Nian back into the ocean depths!", "zh": "所以大家在大門貼紅聯、穿鮮紅衣裳、燃放竹節爆竹，把年獸嚇回了大海深處！", "keywords": ["firecrackers", "crimson", "garments"] },
      { "id": 5, "speaker": "Hannah", "avatar": "👧", "en": "And when everyone survived safely, they congratulated each other: 'Guo Nian'—overcoming the beast! That's brilliant cultural storytelling!", "zh": "而隔天大家平安無事相聚慶祝，互道『過年』——戰勝度過年關！這文化神話故事編得太精彩了！", "keywords": ["congratulated", "Guo Nian"] },
      { "id": 6, "speaker": "Max", "avatar": "👦", "en": "Next time you wear a red sweater and hear firecrackers, remember you're carrying on thousands of years of heroic triumph!", "zh": "下次你穿紅毛衣、聽見劈啪鞭炮聲時，記住你正在傳承數千年來英雄擊退困難的勇氣象徵！", "keywords": ["sweater", "heroic"] }
    ],
    "vocabulary": [
      { "word": "mythology", "phonetic": "/mɪˈθɑː.lə.dʒi/", "pos": "n.", "zh": "神話、神話學", "example": "Greek and Chinese mythology both personify nature." },
      { "word": "firecracker", "phonetic": "/ˈfaɪrˌkræk.ɚ/", "pos": "n.", "zh": "鞭炮、爆竹", "example": "Firecrackers crackled loudly in the midnight street." },
      { "word": "garment", "phonetic": "/ˈɡɑːr.mənt/", "pos": "n.", "zh": "（一件）衣服、服裝", "example": "Wear red garments to celebrate joyous festivities." }
    ],
    "dailyPhrase": { "en": "Guo Nian.", "zh": "過年（度過年獸難關、辭舊迎新）" },
    "cultureTip": "「過年（Guo Nian）」字面含義為「度過年關」，因此大年初一見面第一句話說「恭喜恭喜」，最早是恭賀彼此平安度過年獸劫難與寒冬！"
  },

  # 01-17 [國小初階]
  {
    "id": "dialogue-0117",
    "date": "01-17",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "春節手作",
    "topic": {
      "en": "Folding Red Envelopes with Golden Dragon Stamps",
      "zh": "動手折喜氣洋洋的燙金紅包袋"
    },
    "situation": "美勞角裡，Sam 和 Eric 拿著大紅紙和金箔轉印貼紙，自己動手折疊準備放壓歲錢的紅包袋。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Eric": { "role": "Eric", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0117.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Eric, let's fold handmade red envelopes for our grandparents!", "zh": "Eric，我們來動手折手工紅包袋送給爺爺奶奶吧！", "keywords": ["red envelopes", "handmade"] },
      { "id": 2, "speaker": "Eric", "avatar": "👦", "en": "Fold the sides inward, glue the bottom flap, and tuck the top curve into the slot!", "zh": "兩側往內折、底端塗上膠水黏牢，然後把上蓋弧形塞進卡槽裡！", "keywords": ["flap", "slot", "tuck"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Now rub this shiny golden foil dragon transfer onto the front!", "zh": "現在把這個閃亮亮的金色金箔神龍轉印貼紙擦在正面上！", "keywords": ["dragon", "foil"] },
      { "id": 4, "speaker": "Eric", "avatar": "👦", "en": "Peel away the clear film... Wow! A majestic golden dragon gleaming on bright red paper!", "zh": "撕掉透明薄膜…哇！一條威風凜凜的金龍在大紅紙上閃閃發光！", "keywords": ["majestic", "gleaming"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Red represents good luck, and gold represents prosperity. Grandparents will cherish our handmade love!", "zh": "紅色代表好運，金色代表吉祥富貴。爺爺奶奶一定會珍藏我們親手做的滿滿心意！", "keywords": ["prosperity", "cherish"] }
    ],
    "vocabulary": [
      { "word": "flap", "phonetic": "/flæp/", "pos": "n.", "zh": "（信封或盒子的）封蓋、活頁", "example": "Moisten the envelope flap to seal it shut." },
      { "word": "majestic", "phonetic": "/məˈdʒes.tɪk/", "pos": "adj.", "zh": "威風凜凜的、雄偉壯麗的", "example": "The snow-capped mountains presented a majestic view." },
      { "word": "slot", "phonetic": "/slɑːt/", "pos": "n.", "zh": "狹縫、開槽、投幣口", "example": "Drop the gold coin into the piggy bank slot." }
    ],
    "dailyPhrase": { "en": "Red and gold.", "zh": "紅金相映（春節最具代表性的富貴喜慶配色）" },
    "cultureTip": "「Red Envelope（紅包／壓歲錢）」在廣東話稱「利是（Lai See）」，長輩給晚輩紅包有壓制邪祟、保佑孩子在新的一年平平安安長大的祝福寓意。"
  },

  # 01-18 [高中進階]
  {
    "id": "dialogue-0118",
    "date": "01-18",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "飲食人類學",
    "topic": {
      "en": "Symbolic Gastronomy in Lunar New Year Feasts",
      "zh": "舌尖上的年味：年菜料理中的象徵符號學"
    },
    "situation": "高中文化人類學研討課上，Grace 和 Leo 剖析年夜飯桌上「魚不吃完」、「長年菜」與「發菜」背後深刻的飲食語言學與吉祥心理投射。",
    "speakers": {
      "Grace": { "role": "Grace", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" },
      "Leo": { "role": "Leo", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0118.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Grace", "avatar": "👩", "en": "Leo, every dish served at a traditional Lunar New Year banquet is meticulously laden with linguistic puns and auspicious metaphors.", "zh": "Leo，傳統年夜飯餐桌上的每一道菜餚，都極其精緻地承載著語言學雙關諧音與吉祥隱喻。", "keywords": ["linguistic", "metaphors", "banquet"] },
      { "id": 2, "speaker": "Leo", "avatar": "🧑", "en": "Most iconic is the whole steamed fish. In Mandarin, 'fish' (yu) is homophonous with 'surplus'. Leaving the head and tail uneaten symbolizes abundance year after year.", "zh": "最標誌性的就是那整條清蒸魚。中文裡『魚』與『餘』同音。餐桌上特意留下魚頭魚尾不吃完，象徵年年有餘、豐饒常在。", "keywords": ["homophonous", "surplus", "iconic"] },
      { "id": 3, "speaker": "Grace", "avatar": "👩", "en": "And uncut mustard greens—known as 'longevity vegetables'—must be consumed from stem to leaf in one piece to signify long, continuous life.", "zh": "還有不能切斷的整株芥菜——被稱為『長年菜』——必須整根從根吃到葉，象徵生命長壽延綿不絕。", "keywords": ["mustard greens", "longevity"] },
      { "id": 4, "speaker": "Leo", "avatar": "🧑", "en": "It's culinary semiotics: dinner ceases to be mere biological sustenance and transforms into a participatory ritual of communal hope.", "zh": "這正是飲食符號學的精髓：吃年夜飯不再只是單純填飽肚子的生理攝取，而是轉化為一場全民共同參與祈求希望的集體儀式。", "keywords": ["semiotics", "sustenance", "participatory"] },
      { "id": 5, "speaker": "Grace", "avatar": "👩", "en": "Food becomes language; taste becomes blessing. What an enduring testament to the cultural elevation of everyday life.", "zh": "食物成了語言，味道化作祝福。這真是文化將日常生活昇華為藝術的永恆見證。", "keywords": ["testament", "elevation"] }
    ],
    "vocabulary": [
      { "word": "homophonous", "phonetic": "/hoʊˈmɑː.fə.nəs/", "pos": "adj.", "zh": "同音的、同音異義的", "example": "Many Chinese lucky symbols stem from homophonous wordplay." },
      { "word": "semiotics", "phonetic": "/ˌsem.iˈɑː.tɪks/", "pos": "n.", "zh": "符號學（研究符號與象徵意義的學問）", "example": "Semiotics explores how culture encodes meaning into visual arts." },
      { "word": "sustenance", "phonetic": "/ˈsʌs.tən.əns/", "pos": "n.", "zh": "養分、生計、維持生命的食物", "example": "Clean water and simple grains provided basic sustenance." }
    ],
    "dailyPhrase": { "en": "Food becomes language.", "zh": "食物化作語言、料理承載情感。" },
    "cultureTip": "年夜飯必有全魚且「頭尾完整」，取「有頭有尾」善始善終之意，且除夕夜不可全吃光，代表「年年有餘（魚）」。"
  },

  # 01-19 [國小中高]
  {
    "id": "dialogue-0119",
    "date": "01-19",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "春節美食",
    "topic": {
      "en": "Wrapping Golden Ingot Dumplings",
      "zh": "全家圍坐包白白胖胖的元寶水餃"
    },
    "situation": "除夕前夕在客廳大餐桌上，Ken 和媽媽正熟練地包餃子，在餃皮裡放入鮮甜白菜豬肉餡並捏出漂亮波浪摺邊。",
    "speakers": {
      "Ken": { "role": "Ken", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mom": { "role": "媽媽", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0119.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ken", "avatar": "👦", "en": "Mom, look at my dumpling! I spooned pork filling in the middle and moistened the circular wrapper edge.", "zh": "媽媽看我的水餃！我舀了一匙豬肉餡放中間，在圓形餃子皮邊緣抹了一圈水。", "keywords": ["dumpling", "wrapper"] },
      { "id": 2, "speaker": "Mom", "avatar": "👩", "en": "Now fold it in half, pinch the center firmly, and pleat five neat ripples along both sides.", "zh": "現在對折，中心用力捏緊，然後在兩邊捏出五個整整齊齊的小摺子。", "keywords": ["pleat", "ripples"] },
      { "id": 3, "speaker": "Ken", "avatar": "👦", "en": "When you curve the two ends together, it looks just like an ancient silver or gold ingot!", "zh": "把兩頭往中間輕輕彎攏捏緊，看起來就像古時候的銀元寶或金元寶一樣耶！", "keywords": ["ingot", "ancient"] },
      { "id": 4, "speaker": "Mom", "avatar": "👩", "en": "Exactly. Eating dumplings at midnight ushers in prosperity for the upcoming year.", "zh": "沒錯。除夕子時吃水餃元寶，寓意在新的一年招財進寶、大吉大利。", "keywords": ["prosperity", "upcoming"] },
      { "id": 5, "speaker": "Ken", "avatar": "👦", "en": "Did you hide a clean coin in one of the dumplings? Whoever bites into it gets super good fortune!", "zh": "媽媽妳有在一顆水餃裡藏洗乾淨的金幣嗎？誰幸運咬到誰今年就會大發好運！", "keywords": ["coin", "bites"] }
    ],
    "vocabulary": [
      { "word": "pleat", "phonetic": "/pliːt/", "pos": "v./n.", "zh": "打褶、捏出摺痕、百褶", "example": "Pleat the edges of the pastry neatly." },
      { "word": "ingot", "phonetic": "/ˈɪŋ.ɡət/", "pos": "n.", "zh": "元寶、金條、鑄錠", "example": "Ancient merchants traded with silver ingots." },
      { "word": "wrapper", "phonetic": "/ˈræp.ɚ/", "pos": "n.", "zh": "餃子皮、包裝皮", "example": "Dust the dumpling wrappers with cornstarch." }
    ],
    "dailyPhrase": { "en": "Shaped like an ingot.", "zh": "形如金元寶（水餃象徵財富的招牌外觀）" },
    "cultureTip": "北方習俗在除夕夜子時（深夜 11 點到 1 點）吃水餃，取「更歲交子」之意（水餃諧音交子），代表歲更交替、除舊迎新。"
  },

  # 01-20 [國中挑戰]
  {
    "id": "dialogue-0120",
    "date": "01-20",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "春節除夕",
    "topic": {
      "en": "New Year's Eve Reunion Dinner with Family",
      "zh": "除夕夜圍爐：全家團聚年夜飯"
    },
    "situation": "除夕夜，圓圓的大餐桌中央放著熱氣騰騰的火鍋，Kevin 和表姐 Zoe 陪同長輩圍坐，共享年夜飯溫馨時刻。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "🧑", "gender": "male", "voice": "en-US-ChristopherNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0120.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "🧑", "en": "Zoe, all three generations of our family are sitting around this big round rotating dinner table!", "zh": "Zoe，我們家祖孫三代今晚全都圍坐在這張大大的圓形轉盤餐桌旁了！", "keywords": ["reunion", "generations"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Look at the centerpiece hot pot simmering with tiger prawns, scallops, and golden egg dumplings!", "zh": "看桌子正中央的圍爐熱火鍋，正滾煮著大草蝦、干貝和金黃色蛋餃呢！", "keywords": ["hot pot", "scallops", "simmering"] },
      { "id": 3, "speaker": "Kevin", "avatar": "🧑", "en": "The round shape of the table and the circular hot pot symbolize harmony, completion, and familial unity.", "zh": "圓桌和圓圓的火鍋象徵著團圓圓滿、家庭和樂與親族團結。", "keywords": ["harmony", "unity", "circular"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Grandpa is raising his tea cup for the opening toast: 'To health, peace, and joyous laughter across every home!'", "zh": "爺爺正端起茶杯主持開場乾杯：『祝大家身體健康、歲歲平安、闔家歡樂！』", "keywords": ["toast", "peace"] },
      { "id": 5, "speaker": "Kevin", "avatar": "🧑", "en": "Cheers! No matter how far family members travel during the year, reunion dinner brings all hearts home.", "zh": "乾杯！無論這一年大家在外面奔波走得多遠，年夜飯總能把所有人的心帶回家。", "keywords": ["reunion dinner", "cheers"] }
    ],
    "vocabulary": [
      { "word": "reunion", "phonetic": "/ˌriːˈjuː.njən/", "pos": "n.", "zh": "團聚、重逢、團圓", "example": "The family reunion dinner is the cornerstone of Lunar New Year." },
      { "word": "unity", "phonetic": "/ˈjuː.nə.t̬i/", "pos": "n.", "zh": "團結、和諧統一", "example": "Community unity overcame neighborhood hardships." },
      { "word": "toast", "phonetic": "/toʊst/", "pos": "n./v.", "zh": "舉杯祝酒、乾杯敬酒", "example": "The host proposed a heartfelt toast to the guests." }
    ],
    "dailyPhrase": { "en": "Reunion dinner.", "zh": "團圓飯、年夜飯（除夕夜最重要的家庭盛宴）" },
    "cultureTip": "除夕夜圍爐吃年夜飯（Reunion Dinner），全家不論平日散居何處皆盡力趕回，圍坐象徵「圓滿吉祥」，是華人社會最具凝聚力的文化核心。"
  },

  # 01-21 [國小初階]
  {
    "id": "dialogue-0121",
    "date": "01-21",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "除夕守歲",
    "topic": {
      "en": "Staying Up Late on New Year's Eve",
      "zh": "除夕夜陪爺爺奶奶守歲祈福"
    },
    "situation": "除夕吃完年夜飯後，客廳燈火通明，Anna 和弟弟 Tim 喝著冬瓜茶，陪長輩看電視聊天守歲。",
    "speakers": {
      "Anna": { "role": "Anna", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Tim": { "role": "Tim", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0121.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tim", "avatar": "👦", "en": "Anna, it's already eleven o'clock at night! Why are all the lights in the house still blazing bright?", "zh": "Anna，已經晚上十一點了！為什麼家裡所有的電燈還全都開得通亮？", "keywords": ["blazing", "bright"] },
      { "id": 2, "speaker": "Anna", "avatar": "👧", "en": "It's the ancient tradition of 'Shousui'—staying up late on New Year's Eve!", "zh": "這是古老的傳統『守歲』——在除夕夜通宵不睡覺！", "keywords": ["Shousui", "tradition"] },
      { "id": 3, "speaker": "Tim", "avatar": "👦", "en": "Are we allowed to stay awake past midnight?", "zh": "那我們今天真的可以過了午夜十二點還不用上床睡覺嗎？", "keywords": ["midnight", "awake"] },
      { "id": 4, "speaker": "Anna", "avatar": "👧", "en": "Yes! Tradition says when children stay up late on New Year's Eve, it blesses parents and grandparents with long, healthy lives!", "zh": "沒錯！傳統說孩子在除夕夜守歲不睡，是在為父母和爺爺奶奶祈求健康長壽喔！", "keywords": ["blesses", "long life"] },
      { "id": 5, "speaker": "Tim", "avatar": "👦", "en": "Then I'm staying awake all the way until dawn! Long and happy lives for everyone in our family!", "zh": "那我一定要一直清醒守到天亮！祝我們全家人都健康長壽、幸福美滿！", "keywords": ["dawn", "awake"] }
    ],
    "vocabulary": [
      { "word": "dawn", "phonetic": "/dɑːn/", "pos": "n.", "zh": "黎明、破曉、拂曉", "example": "Birds burst into song at the crack of dawn." },
      { "word": "bless", "phonetic": "/bles/", "pos": "v.", "zh": "祝福、保佑、賜福", "example": "May peace bless your warm home." },
      { "word": "awake", "phonetic": "/əˈweɪk/", "pos": "adj.", "zh": "清醒的、未睡著的", "example": "Excitement kept the young boy awake all night." }
    ],
    "dailyPhrase": { "en": "Stay up late.", "zh": "熬夜不睡（除夕夜特指孝順守歲祈求長輩長壽）" },
    "cultureTip": "「守歲（Shou Sui）」是指除夕夜燈火通宵不熄，既是對如水歲月的惜別留戀，年輕一代為長輩守歲更有為父母延年益壽的孝道寓意。"
  },

  # 01-22 [國中挑戰]
  {
    "id": "dialogue-0122",
    "date": "01-22",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "春節大年初一",
    "topic": {
      "en": "Receiving Red Envelopes: Gong Xi Fa Cai!",
      "zh": "大年初一拜年領紅包：恭喜發財！"
    },
    "situation": "大年初一清晨，Tyler 和 Zoe 換上紅色新衣服，向端坐在客廳沙發上的祖父母恭敬鞠躬拜年。",
    "speakers": {
      "Tyler": { "role": "Tyler", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0122.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tyler", "avatar": "👦", "en": "Good morning Grandma and Grandpa! Happy Lunar New Year! Wishing you vibrant health and abundant joy!", "zh": "爺爺奶奶早安！新年快樂！祝您二老身體健康、萬事如意、福壽雙全！", "keywords": ["Happy Lunar New Year", "vibrant"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Gong Xi Fa Cai! May everything go smoothly and all your days be filled with peaceful laughter!", "zh": "恭喜發財！祝您二老歲歲平安、諸事順心、天天笑逐顏開！", "keywords": ["Gong Xi Fa Cai", "smoothly"] },
      { "id": 3, "speaker": "Tyler", "avatar": "👦", "en": "Grandpa is smiling ear-to-ear, handing each of us a thick crimson red envelope with both hands!", "zh": "爺爺笑得合不攏嘴，用雙手遞給我們每人一個厚厚的大紅包！", "keywords": ["crimson", "envelope"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Remember the etiquette: accept the envelope with two respectful hands and immediately say 'Thank you, Grandpa!'", "zh": "記住禮貌：一定要用恭敬的雙手接過紅包，並立刻說『謝謝爺爺！』", "keywords": ["etiquette", "respectful"] },
      { "id": 5, "speaker": "Tyler", "avatar": "👦", "en": "And never open the envelope right in front of the giver; that's proper cultural manners!", "zh": "而且絕對不能當著長輩的面把紅包拆開看，這才是最有教養的傳統禮節！", "keywords": ["manners", "cultural"] }
    ],
    "vocabulary": [
      { "word": "etiquette", "phonetic": "/ˈet̬.ɪ.kɪt/", "pos": "n.", "zh": "禮儀、社交規矩", "example": "Dining etiquette varies significantly across global cultures." },
      { "word": "vibrant", "phonetic": "/ˈvaɪ.brənt/", "pos": "adj.", "zh": "充滿生機活力的、矍鑠的", "example": "Grandfather maintains vibrant health through daily tai chi." },
      { "word": "respectful", "phonetic": "/rɪˈspekt.fəl/", "pos": "adj.", "zh": "畢恭畢敬的、充滿尊重的", "example": "Address your elders in a polite, respectful tone." }
    ],
    "dailyPhrase": { "en": "Smile ear-to-ear.", "zh": "笑得合不攏嘴、開心極了。" },
    "cultureTip": "接長輩紅包切記用「雙手承接」，並不可當場拆看金額（Opening gifts in private is polite in Chinese custom），以示對長輩祝福本意的尊重。"
  },

  # 01-23 [國小初階]
  {
    "id": "dialogue-0123",
    "date": "01-23",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "春節初二",
    "topic": {
      "en": "Visiting Relatives with Tangerines",
      "zh": "大年初二回娘家：送上大吉大利金柑橘"
    },
    "situation": "初二早晨，Sam 幫媽媽提著一籃黃澄澄、葉子翠綠的新鮮大椪柑，出發去外公外婆家拜年。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mom": { "role": "媽媽", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0123.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Mom, this gift box of shiny orange tangerines with green leaves looks so handsome!", "zh": "媽媽，這盒帶綠葉、金黃色發亮的大柑橘禮盒看起來好體面喔！", "keywords": ["tangerines", "gift box"] },
      { "id": 2, "speaker": "Mom", "avatar": "👩", "en": "Today is the second day of the Lunar New Year, when married daughters return to visit their parents.", "zh": "今天是農曆大年初二，是已婚女兒回娘家探望父母的日子。", "keywords": ["parents", "return"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Why do we always bring pairs of tangerines as greeting gifts?", "zh": "為什麼我們拜年總是會帶成雙成對的柑橘當伴手禮呢？", "keywords": ["pairs", "greeting"] },
      { "id": 4, "speaker": "Mom", "avatar": "👩", "en": "Because in Cantonese and Mandarin, 'tangerine' sounds like 'luck', and its golden hue symbolizes wealth and prosperity!", "zh": "因為在廣東話和國語裡，『橘』諧音『吉』，金黃色澤更象徵大吉大利、招財富足！", "keywords": ["wealth", "prosperity", "hue"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Double tangerines mean double the fortune and double the sweetness for Grandma!", "zh": "一對金橘代表雙倍的好運和大吉大利送給外婆！", "keywords": ["double", "sweetness"] }
    ],
    "vocabulary": [
      { "word": "tangerine", "phonetic": "/ˌtæn.dʒəˈriːn/", "pos": "n.", "zh": "柑橘、椪柑、蜜柑", "example": "Sweet juicy tangerines symbolize good fortune." },
      { "word": "hue", "phonetic": "/hjuː/", "pos": "n.", "zh": "色調、色彩", "example": "The golden hue of autumn leaves brightened the path." },
      { "word": "prosperity", "phonetic": "/prɑːˈsper.ə.t̬i/", "pos": "n.", "zh": "興旺、繁榮發達", "example": "Hard work and integrity bring lasting prosperity." }
    ],
    "dailyPhrase": { "en": "Great luck and prosperity.", "zh": "大吉大利、萬事亨通。" },
    "cultureTip": "初二回娘家送禮講究「成雙成對（In pairs）」，絕不送單數，送金橘互換代表「換吉（互道好運大吉大利）」。"
  },

  # 01-24 [高中進階]
  {
    "id": "dialogue-0124",
    "date": "01-24",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "民俗學",
    "topic": {
      "en": "The Art and Acrobatics of Lion Dance",
      "zh": "力與美的結合：舞獅技藝中的非遺武術美學"
    },
    "situation": "高中武術社春節廟會觀摩後，Marcus 與 Bella 探討南獅（醒獅）梅花樁高難度騰挪跳躍背後的武術功底與文化生命力。",
    "speakers": {
      "Marcus": { "role": "Marcus", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Bella": { "role": "Bella", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0124.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Marcus", "avatar": "🧑", "en": "Bella, watching the Southern Lion performers leap across towering steel poles two meters high took my breath away!", "zh": "Bella，看南獅醒獅隊員在兩公尺高的高聳梅花樁上飛躍騰挪，看得我屏住呼吸心跳狂飆！", "keywords": ["performers", "steel poles"] },
      { "id": 2, "speaker": "Bella", "avatar": "👩", "en": "It's an extraordinary fusion of martial arts, gymnastics, and animal mimetic expression. The head and tail performers require telepathic synchrony.", "zh": "這是武術、體操與動物擬態神態表現的絕妙融合。獅頭與獅尾表演者需要近乎心電感應般的默契配合。", "keywords": ["mimetic", "synchrony", "telepathic"] },
      { "id": 3, "speaker": "Marcus", "avatar": "🧑", "en": "The blinking eyelids, shaking mane, and hesitating paw steps capture the emotional range of a living beast waking up.", "zh": "眨動的眼皮、抖動的獅鬃，還有試探性的腳步，傳神捕捉了一頭猛獸初醒時豐富的情感神態。", "keywords": ["eyelids", "mane", "hesitating"] },
      { "id": 4, "speaker": "Bella", "avatar": "👩", "en": "And the climax ritual—'Cai Qing' (plucking the green)—where the lion overcomes obstacles to ingest lettuce and spit out blessings, is pure allegorical theater.", "zh": "而高潮儀式『採青』——獅子克服萬難吞下生菜並吐出祝福——更是充滿了象徵迎祥納福的生動戲劇隱喻。", "keywords": ["climax", "allegorical", "lettuce"] },
      { "id": 5, "speaker": "Marcus", "avatar": "🧑", "en": "Preserving these intangible heritage traditions keeps cultural vitality beating loudly like those celebratory drums.", "zh": "傳承這些非物質文化遺產，讓深厚的文化生命力就像那澎湃的鼓點一樣鏗鏘有力、歷久彌新。", "keywords": ["intangible", "heritage", "vitality"] }
    ],
    "vocabulary": [
      { "word": "mimetic", "phonetic": "/mɪˈmet̬.ɪk/", "pos": "adj.", "zh": "擬態的、模仿生動的", "example": "Dancers mastered mimetic movements of graceful crane birds." },
      { "word": "allegorical", "phonetic": "/ˌæl.əˈɡɔːr.ɪ.kəl/", "pos": "adj.", "zh": "寓言式的、諷喻象徵的", "example": "The story holds an allegorical message about honesty." },
      { "word": "intangible", "phonetic": "/ɪnˈtæn.dʒə.bəl/", "pos": "adj.", "zh": "非物質的、無形的（如文化遺產）", "example": "Traditional folklore is UNESCO intangible cultural heritage." }
    ],
    "dailyPhrase": { "en": "Take one's breath away.", "zh": "美到讓人屏息、令人嘆為觀止。" },
    "cultureTip": "醒獅「採青」中的青通常為「生菜」，諧音「生財」，獅子咬破生菜並灑向四方，寓意「遍地生財、大展鴻圖」。"
  },

  # 01-25 [國小中高]
  {
    "id": "dialogue-0125",
    "date": "01-25",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "節慶走春",
    "topic": {
      "en": "Spring Outing and Flying Big Kites",
      "zh": "春節走春踏青：在草地上放五彩大風箏"
    },
    "situation": "大年初四陽光明媚，Lucas 和爸爸在河濱草地上解開長長的風箏線，準備放飛色彩斑斕的長尾龍風箏。",
    "speakers": {
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Dad": { "role": "爸爸", "avatar": "👨", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0125.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lucas", "avatar": "👦", "en": "Dad, look at how many families are out on the lawn today for their Spring Outing!", "zh": "爸爸，看今天草地上有好多全家出動出來『走春』踏青的人喔！", "keywords": ["Spring Outing", "lawn"] },
      { "id": 2, "speaker": "Dad", "avatar": "👨", "en": "Walking in nature on a crisp sunny day during the holiday clears the mind and invites fresh vitality.", "zh": "在連假晴朗的日子到大自然散散步，能讓頭腦清新、迎來滿滿的元氣活力。", "keywords": ["vitality", "crisp"] },
      { "id": 3, "speaker": "Lucas", "avatar": "👦", "en": "Let's launch our colorful dragon kite! The long ribbon tail stretches ten meters behind it!", "zh": "我們來放這隻七彩大龍風箏吧！後面那條長長的彩帶尾巴有整整十公尺長耶！", "keywords": ["ribbon tail", "launch"] },
      { "id": 4, "speaker": "Dad", "avatar": "👨", "en": "Hold the spool, watch for the steady updraft, and let the line feed through your fingertips gently.", "zh": "拿好線輪，感覺平穩的上升氣流，然後讓風箏線從指尖緩緩放出去。", "keywords": ["updraft", "spool"] },
      { "id": 5, "speaker": "Lucas", "avatar": "👦", "en": "It's soaring high above the clouds! Soaring higher and higher, just like our hopes for this new year!", "zh": "它高高飛到雲朵上了！越飛越高，就像我們對新一年的無限期許一樣！", "keywords": ["soaring", "hopes"] }
    ],
    "vocabulary": [
      { "word": "updraft", "phonetic": "/ˈʌp.dræft/", "pos": "n.", "zh": "上升氣流", "example": "The eagle caught a warm updraft and soared effortlessly." },
      { "word": "spool", "phonetic": "/spuːl/", "pos": "n.", "zh": "（放線用的）線軸、線輪", "example": "Unwind the string smoothly from the wooden spool." },
      { "word": "vitality", "phonetic": "/vaɪˈtæl.ə.t̬i/", "pos": "n.", "zh": "生命力、蓬勃生機", "example": "Spring sunshine restores youthful energy and vitality." }
    ],
    "dailyPhrase": { "en": "Spring outing.", "zh": "走春、春季郊遊踏青。" },
    "cultureTip": "春節「走春（踏青）」源於傳統農耕社會，選吉時走向大自然呼吸新鮮空氣，拜訪親友廟宇，寓意整年迎來好氣場與生機。"
  },

  # 01-26 [國中挑戰]
  {
    "id": "dialogue-0126",
    "date": "01-26",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "年節開工",
    "topic": {
      "en": "Welcoming the God of Wealth on the Fifth Day",
      "zh": "初五開工迎財神：破五送窮喜迎祥瑞"
    },
    "situation": "初五早晨，商店紛紛開門營業並燃放歡樂鞭炮，Kevin 和 Zoe 走在街上，看到店門口供奉著鳳梨與金元寶。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "🧑", "gender": "male", "voice": "en-US-ChristopherNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0126.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "🧑", "en": "Zoe, all the retail shops and restaurants are reopening their doors today with festive firecrackers!", "zh": "Zoe，所有店家和餐廳今天都紛紛燃放歡樂鞭炮、開工開市囉！", "keywords": ["reopening", "firecrackers"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Today is the fifth day of the new year, traditionally celebrated as the birthday of the God of Wealth!", "zh": "今天是初五，傳統上被視為財神的誕辰吉日呢！", "keywords": ["God of Wealth", "fifth day"] },
      { "id": 3, "speaker": "Kevin", "avatar": "🧑", "en": "Look at the offering tables outside the shopfronts: golden pineapples, lucky radish cakes, and sweet oranges.", "zh": "看店家門口的開工供桌：有象徵好運旺來的金鳳梨、發財蘿蔔糕和吉利橘子。", "keywords": ["pineapples", "radish cakes", "shopfronts"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "In Taiwanese, 'pineapple' sounds like 'prosperity arriving' (ong-lai), inviting booming business and thriving success.", "zh": "在台語裡，『鳳梨』發音為『旺來』，象徵生意興隆、好運滾滾來。", "keywords": ["prosperity", "booming"] },
      { "id": 5, "speaker": "Kevin", "avatar": "🧑", "en": "The holiday feast wraps up, and everyone returns to their workstations energized and hopeful for a fruitful year ahead!", "zh": "過年大假告一段落，大家精神飽滿回到工作崗位，滿懷希望迎接收穫豐碩的新一年！", "keywords": ["workstations", "fruitful"] }
    ],
    "vocabulary": [
      { "word": "shopfront", "phonetic": "/ˈʃɑːp.frʌnt/", "pos": "n.", "zh": "店面、店家門前", "example": "Festive red banners adorned every downtown shopfront." },
      { "word": "booming", "phonetic": "/ˈbuː.mɪŋ/", "pos": "adj.", "zh": "繁榮興旺的、蓬勃發展的", "example": "The tech sector experienced booming job growth." },
      { "word": "fruitful", "phonetic": "/ˈfruːt.fəl/", "pos": "adj.", "zh": "收穫豐碩的、卓有成效的", "example": "We had a highly fruitful semester of collaborative study." }
    ],
    "dailyPhrase": { "en": "Booming business.", "zh": "生意興隆、業績長紅。" },
    "cultureTip": "初五又稱「破五」，意味著初一到初四的各項年節禁忌正式解除，商號於當天舉行「開工迎財神」儀式，祈求整年客源廣進。"
  },

  # 01-27 [國小初階]
  {
    "id": "dialogue-0127",
    "date": "01-27",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "寒假遊戲",
    "topic": {
      "en": "Playing Chinese Dominoes and Board Games",
      "zh": "寒假午後玩五子棋與益智桌遊"
    },
    "situation": "午後客廳地毯上，Lily 和 Toby 圍坐在一起下黑白五子棋，開動腦筋互不相讓。",
    "speakers": {
      "Lily": { "role": "Lily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0127.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lily", "avatar": "👧", "en": "Toby, it's your turn! Black stones move first on the wooden grid board.", "zh": "Toby，換你下囉！在木質網格棋盤上黑棋先走。", "keywords": ["grid", "stones"] },
      { "id": 2, "speaker": "Toby", "avatar": "👦", "en": "Click! I place my black stone right in the center star point.", "zh": "卡嗒！我把我的黑棋下在正中央天元星位上。", "keywords": ["star point", "center"] },
      { "id": 3, "speaker": "Lily", "avatar": "👧", "en": "I block your diagonal line with my white marble stone!", "zh": "我用我的白色大理石棋子擋住你的對角線！", "keywords": ["diagonal", "block"] },
      { "id": 4, "speaker": "Toby", "avatar": "👦", "en": "Aha, but look across the horizontal row: one, two, three, four, five! Five in a row! I win!", "zh": "哈哈，但看這一條橫排：一、二、三、四、五！五顆連成一線！我贏囉！", "keywords": ["horizontal", "five in a row"] },
      { "id": 5, "speaker": "Lily", "avatar": "👧", "en": "Great eye, Toby! Playing board games together during winter break exercises our brains so much fun!", "zh": "好敏銳的眼力喔 Toby！寒假一起玩桌遊動動腦真的太好玩了！", "keywords": ["great eye", "exercises"] }
    ],
    "vocabulary": [
      { "word": "diagonal", "phonetic": "/daɪˈæɡ.ən.əl/", "pos": "adj./n.", "zh": "對角線的、斜線的", "example": "Draw a diagonal line from top left to bottom right." },
      { "word": "horizontal", "phonetic": "/ˌhɔːr.ɪˈzɑːn.t̬əl/", "pos": "adj.", "zh": "水平的、橫排的", "example": "Keep the spirit level perfectly horizontal." },
      { "word": "grid", "phonetic": "/ɡrɪd/", "pos": "n.", "zh": "網格、格子棋盤", "example": "The city streets follow an organized grid pattern." }
    ],
    "dailyPhrase": { "en": "Five in a row!", "zh": "五子連線！（五子棋獲勝歡呼）" },
    "cultureTip": "五子棋（Gomoku / Five in a Row）起源於中國古代，規則簡單卻極度考驗空間預判與專注力，是老少咸宜的經典益智棋類。"
  },

  # 01-28 [高中進階]
  {
    "id": "dialogue-0128",
    "date": "01-28",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "理財教育",
    "topic": {
      "en": "Financial Literacy: What to Do with Red Envelope Money?",
      "zh": "青少年理財第一步：壓歲錢該如何妥善規劃？"
    },
    "situation": "高中生 Marcus 與 Bella 在圖書館研討室整理過年收到的壓歲錢，交流如何將零用錢轉化為長期複利投資或教育儲蓄。",
    "speakers": {
      "Marcus": { "role": "Marcus", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Bella": { "role": "Bella", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0128.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Marcus", "avatar": "🧑", "en": "Bella, when we were kids, parents always said 'let me hold your red envelope money for safekeeping', and it mysteriously disappeared.", "zh": "Bella，小時候爸媽總是說『紅包錢媽媽先幫你存起來』，然後那些錢就神秘失蹤了。", "keywords": ["safekeeping", "mysteriously"] },
      { "id": 2, "speaker": "Bella", "avatar": "👩", "en": "Haha, the universal childhood myth! But as teenagers, managing our holiday funds is a prime opportunity to build genuine financial literacy.", "zh": "哈哈，全世界小孩共通的童年迷因！但身為高中生，管理這筆壓歲錢正是培養真實理財素養的絕佳契機。", "keywords": ["literacy", "myth"] },
      { "id": 3, "speaker": "Marcus", "avatar": "🧑", "en": "I'm allocating twenty percent for recreational books and hobby gear, and placing eighty percent into a broad-market index ETF fund.", "zh": "我打算撥出百分之二十買想讀的課外書和興趣器材，剩下的百分之八十存入大盤指數型 ETF 基金。", "keywords": ["allocating", "index fund"] },
      { "id": 4, "speaker": "Bella", "avatar": "👩", "en": "Smart asset allocation. The miraculous power of compound interest works best over vast time horizons starting in youth.", "zh": "聰明的資產配置。複利那不可思議的奇蹟力量，最需要在年輕時就展開漫長的時間跨度來發酵。", "keywords": ["compound interest", "miraculous"] },
      { "id": 5, "speaker": "Marcus", "avatar": "🧑", "en": "Financial freedom isn't about conspicuous consumption, but acquiring autonomy over your future time and life choices.", "zh": "真正的財務自由不在於盲目炫耀性消費，而在於掌握對自己未來時間與人生選擇的自主權。", "keywords": ["autonomy", "conspicuous"] }
    ],
    "vocabulary": [
      { "word": "allocation", "phonetic": "/ˌæl.əˈkeɪ.ʃən/", "pos": "n.", "zh": "配置、分配", "example": "Prudent asset allocation balances risk and return." },
      { "word": "conspicuous", "phonetic": "/kənˈspɪk.ju.əs/", "pos": "adj.", "zh": "顯眼的、炫耀性的", "example": "He avoided conspicuous displays of personal wealth." },
      { "word": "autonomy", "phonetic": "/ɑːˈtɑː.nə.mi/", "pos": "n.", "zh": "自主權、獨立自主", "example": "Financial literacy grants greater career autonomy." }
    ],
    "dailyPhrase": { "en": "Conspicuous consumption.", "zh": "炫耀性消費（為了展示財富而非實際需要的消費行為）" },
    "cultureTip": "股神巴菲特（Warren Buffett）名言：複利就像滾雪球，關鍵在於找到很濕的雪和很長的坡道；在高中階段養成儲蓄投資觀念，是青少年受用一生的財商教育。"
  },

  # 01-29 [國小中高]
  {
    "id": "dialogue-0129",
    "date": "01-29",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "寒假充電",
    "topic": {
      "en": "Visiting the Science Museum Planetarium",
      "zh": "參觀科學博物館星象劇場球幕電影"
    },
    "situation": "寒假週四，Emma 和哥哥 Lucas 來到了國立科學博物館，躺在星象館圓頂穹頂下仰望立體星際銀河。",
    "speakers": {
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0129.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Emma", "avatar": "👧", "en": "Lucas, lean your seat back! The whole gigantic ceiling is a 360-degree domed projection screen!", "zh": "Lucas，把座椅往後躺平！整個巨大天花板就是一個 360 度的圓頂球幕投影螢幕！", "keywords": ["domed", "projection"] },
      { "id": 2, "speaker": "Lucas", "avatar": "👦", "en": "The theater lights are dimming... Whoa! Millions of crystal stars are sparkling right above our foreheads!", "zh": "劇場燈光漸漸暗下來了…哇！數百萬顆晶瑩剔透的恆星就在我們額頭正上方閃閃發亮！", "keywords": ["sparkling", "dimming"] },
      { "id": 3, "speaker": "Emma", "avatar": "👧", "en": "Look at the rings of Saturn! They are composed of countless chunks of ice and rocky debris orbiting in unison!", "zh": "看土星的光環！是由無數繞著軌道整齊運轉的冰塊碎屑與岩石碎片組成的！", "keywords": ["Saturn", "orbiting", "debris"] },
      { "id": 4, "speaker": "Lucas", "avatar": "👦", "en": "It feels like we are aboard a starship drifting silently through the Andromeda galaxy.", "zh": "感覺我們好像正搭乘一艘星際飛船，無聲無息穿梭在仙女座大星系之中。", "keywords": ["starship", "galaxy", "drifting"] },
      { "id": 5, "speaker": "Emma", "avatar": "👧", "en": "Seeing how vast the cosmos is makes our daily worries feel so tiny and insignificant.", "zh": "看見宇宙如此宏大浩瀚，讓我們日常的小小煩惱瞬間變得微不足道。", "keywords": ["cosmos", "insignificant"] }
    ],
    "vocabulary": [
      { "word": "projection", "phonetic": "/prəˈdʒek.ʃən/", "pos": "n.", "zh": "投影、放映", "example": "The digital projection cast crisp images on the dome." },
      { "word": "cosmos", "phonetic": "/ˈkɑːz.moʊs/", "pos": "n.", "zh": "宇宙、大自然秩序", "example": "Astronomers peer deep into the ancient cosmos." },
      { "word": "debris", "phonetic": "/dəˈbriː/", "pos": "n.", "zh": "碎片、殘骸（字母 s 不發音）", "example": "Space debris orbits high above the Earth." }
    ],
    "dailyPhrase": { "en": "In the grand cosmos.", "zh": "在浩瀚無垠的宇宙之中。" },
    "cultureTip": "星象儀（Planetarium）透過高流明雷射投影在半球型圓頂上，重現任何經緯度與歷史年代的逼真夜空，是寒假最受歡迎的親子科普聖地。"
  },

  # 01-30 [國中挑戰]
  {
    "id": "dialogue-0130",
    "date": "01-30",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "寒假作業",
    "topic": {
      "en": "Tackling Winter Vacation Homework Early",
      "zh": "告別開學前趕作業：提前搞定寒假作業"
    },
    "situation": "一月倒數第二天下午，Leo 和 Zoe 坐在自習室裡，打勾清點各自的寒假作業清單，杜絕開學前夕抱佛腳趕工的惡夢。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0130.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Zoe, look at my planner! I just checked off my science project and history book report!", "zh": "Zoe，看我的手帳行事曆！我的自然專題實驗和歷史讀書心得剛剛全都打勾完成了！", "keywords": ["checked off", "planner"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Impressive discipline! In previous years, I used to procrastinate until the final frantic night before school resumed.", "zh": "令人佩服的自律！以前幾年，我總是一路拖延到開學前一晚才在那邊慌忙通宵狂趕。", "keywords": ["frantic", "procrastinate"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "That last-minute panic ruins the entire end of the holiday with sleepless anxiety.", "zh": "那種最後一刻的焦慮恐慌，會帶著失眠與心驚肉跳把整個假期的美好心情毀得一乾二淨。", "keywords": ["panic", "anxiety"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "By finishing assignments systematically in January, February becomes purely relaxing and carefree!", "zh": "在一月份有計畫地搞定所有作業，二月份的假期就能真正無憂無慮、輕鬆享受了！", "keywords": ["systematically", "carefree"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Work hard first, then play with peace of mind. That is the ultimate secret of low-stress students!", "zh": "先苦後甘，玩得心安理得。這正是低壓力學霸最高明的秘密！", "keywords": ["peace of mind", "secret"] }
    ],
    "vocabulary": [
      { "word": "frantic", "phonetic": "/ˈfræn.tɪk/", "pos": "adj.", "zh": "慌亂發狂的、手忙腳亂的", "example": "There was a frantic search for the lost car keys." },
      { "word": "carefree", "phonetic": "/ˈker.friː/", "pos": "adj.", "zh": "無憂無慮的、輕鬆自在的", "example": "Summer vacations should be happy and carefree." },
      { "word": "systematic", "phonetic": "/ˌsɪs.təˈmæt̬.ɪk/", "pos": "adj.", "zh": "有條理的、成體系系統化的", "example": "Adopt a systematic approach to problem solving." }
    ],
    "dailyPhrase": { "en": "With peace of mind.", "zh": "心安理得、問心無愧地。" },
    "cultureTip": "教育心理學研究發現，將長假作業按週分配並提早完成的學生，開學時出現「假期後症候群（Post-vacation blues）」的比例降低超過 70%。"
  },

  # 01-31 [高中進階]
  {
    "id": "dialogue-0131",
    "date": "01-31",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "月結與展望",
    "topic": {
      "en": "January Wrap-Up: Building Habit Momentum for the Year",
      "zh": "一月月結：把年初的好習慣轉化為全年的強勁動能"
    },
    "situation": "一月的最後一天傍晚，高中好友 Henry 和 Claire 漫步在迎春燈火的街角，回顧新的一年第一個月的學習執行力，為即將到來的二月蓄滿動能。",
    "speakers": {
      "Henry": { "role": "Henry", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Claire": { "role": "Claire", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0131.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Henry", "avatar": "🧑", "en": "Claire, today is January thirty-first. One-twelfth of this new year is already in the history books.", "zh": "Claire，今天是一月三十一日。新的一年十二分之一的篇章已經寫入歷史了。", "keywords": ["January", "history books"] },
      { "id": 2, "speaker": "Claire", "avatar": "👩", "en": "Time accelerates, but unlike previous years, our daily dialogue practice didn't fizzle out after week two.", "zh": "時間過得飛快，但不同於以往幾年，我們的每日英語對話好習慣並沒有在第二週就無疾而終。", "keywords": ["accelerates", "fizzle out"] },
      { "id": 3, "speaker": "Henry", "avatar": "🧑", "en": "By keeping the friction low—listening while getting ready in the morning—it seamlessly fused into our identity.", "zh": "透過降低啟動阻力——早晨一邊梳洗一邊聽——它已經無縫融入了我們的日常生活習慣與身分認同。", "keywords": ["seamlessly", "identity"] },
      { "id": 4, "speaker": "Claire", "avatar": "👩", "en": "February will bring Lantern Festival celebrations, the launch of the second semester, and brand new learning horizons.", "zh": "二月份即將迎來元宵燈節、第二學期新起點，以及嶄新的知識學習地平線。", "keywords": ["Lantern Festival", "semester"] },
      { "id": 5, "speaker": "Henry", "avatar": "🧑", "en": "A habit practiced for thirty-one consecutive days builds unshakable momentum. Let's march proudly into February!", "zh": "連續實踐三十一天的習慣，已經築起了堅不可摧的強大動能。讓我們昂首闊步邁向二月吧！", "keywords": ["momentum", "unshakable"] }
    ],
    "vocabulary": [
      { "word": "fizzle", "phonetic": "/ˈfɪz.əl/", "pos": "v.", "zh": "逐漸落空、無疾而終、虎頭蛇尾", "example": "The ambitious project unfortunately fizzled out." },
      { "word": "seamlessly", "phonetic": "/ˈsiːm.ləs.li/", "pos": "adv.", "zh": "無縫地、自然流暢地", "example": "The new feature integrated seamlessly into the app." },
      { "word": "unshakable", "phonetic": "/ʌnˈʃeɪ.kə.bəl/", "pos": "adj.", "zh": "堅定不移的、不可動搖的", "example": "True leaders maintain unshakable integrity in crises." }
    ],
    "dailyPhrase": { "en": "Build unshakable momentum.", "zh": "築起堅定不移、勢如破竹的強勁動能。" },
    "cultureTip": "習慣養成研究指出：堅持 30 天足以跨越「習慣阻力期（Resistance Phase）」，進入自動化反射階段，為整整一年的目標達成奠定最堅實的基石。"
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
    for new_item in JANUARY_DIALOGUES:
        if new_item['date'] not in existing_dates:
            existing.append(new_item)
            existing_dates.add(new_item['date'])
            added_count += 1

    # 按照 MM-DD 排序（01-01 會排在最前面，接著到 12-31）
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

    print(f"成功新增 1 月份共 {added_count} 篇對話！目前資料庫總計共有 {len(existing)} 篇對話 (涵蓋 1月、9月、10月、11月、12月共 153 天)。")

if __name__ == '__main__':
    main()
