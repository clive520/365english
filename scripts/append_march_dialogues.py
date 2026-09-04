#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次建立 3 月份生活對話 (03-01 至 03-31，共 31 篇)
涵蓋春分節氣、驚蟄昆蟲、植樹節、圓周率日、世界水資源日、地球一小時、校外教學與春日自然風光！
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'dialogues.json')

MARCH_DIALOGUES = [
  # 03-01 [國小初階]
  {
    "id": "dialogue-0301",
    "date": "03-01",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "春日自然",
    "topic": {
      "en": "Welcoming March: The Gentle Spring Breeze",
      "zh": "迎接三月：溫暖柔和的春風拂面"
    },
    "situation": "三月第一天早晨，Leo 和 Mia 走在走廊上，推開窗戶感受帶著青草香氣的溫暖春風。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0301.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Mia, open the hallway window! March has officially arrived!", "zh": "Mia，把走廊窗戶推開！三月份正式到來囉！", "keywords": ["March", "window"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "Oh, feel that breeze! It is no longer biting cold; it feels soft like a kitten's fur.", "zh": "噢，感受這陣風！它不再刺骨寒冷，摸起來像小貓的毛一樣柔軟。", "keywords": ["breeze", "kitten", "fur"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Take a deep breath. Can you smell the fresh damp grass outside on the lawn?", "zh": "深深吸一口氣。你能聞到外面草坪上新鮮濕潤青草的香氣嗎？", "keywords": ["breath", "lawn", "grass"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "Yes! The morning sun is painting golden patches on our classroom desks.", "zh": "聞到了！晨光正把金黃色的光斑溫柔灑在我們的教室書桌上。", "keywords": ["golden", "patches", "desks"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Spring is finally in full swing. Let's make this sunny month amazing!", "zh": "春天終於全面展開了。讓我們把這個陽光明媚的月份過得超棒吧！", "keywords": ["in full swing", "amazing"] }
    ],
    "vocabulary": [
      { "word": "breeze", "phonetic": "/briːz/", "pos": "n.", "zh": "微風、和風", "example": "A cooling sea breeze swept across the coast." },
      { "word": "lawn", "phonetic": "/lɑːn/", "pos": "n.", "zh": "草坪、草地", "example": "Children were rolling playfully on the manicured lawn." },
      { "word": "golden", "phonetic": "/ˈɡoʊl.dən/", "pos": "adj.", "zh": "金色的、美好的", "example": "The hills were glowing in the golden afternoon sunlight." }
    ],
    "dailyPhrase": { "en": "In full swing.", "zh": "全面展開、如火如荼進行中。" },
    "cultureTip": "英語諺語常說「March comes in like a lion, and goes out like a lamb（三月來如猛獅，去如溫羊）」，形容三月初氣候仍有春寒，而到了三月底就變得極其溫和宜人。"
  },

  # 03-02 [國小中高]
  {
    "id": "dialogue-0302",
    "date": "03-02",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "節氣智慧",
    "topic": {
      "en": "The Awakening of Insects: Spring Thunder Awakes Nature",
      "zh": "驚蟄：第一聲春雷驚醒沉睡的小昆蟲"
    },
    "situation": "下課時間，Max 和 Ruby 蹲在校園花圃邊，觀察泥土裡探出頭來爬行的七星瓢蟲。",
    "speakers": {
      "Max": { "role": "Max", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Ruby": { "role": "Ruby", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0302.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Max", "avatar": "👦", "en": "Ruby, did you hear that distant rumble of thunder during last night's rain?", "zh": "Ruby，你昨晚下雨時有聽到遠處隆隆的春雷聲嗎？", "keywords": ["rumble", "thunder"] },
      { "id": 2, "speaker": "Ruby", "avatar": "👧", "en": "I did! My grandmother told me it signals the solar term called 'The Awakening of Insects'.", "zh": "有聽到！我奶奶告訴我那是二十四節氣中的「驚蟄」訊號。", "keywords": ["signals", "solar term", "insects"] },
      { "id": 3, "speaker": "Max", "avatar": "👦", "en": "Look down here right by the rose bush! A tiny spotted ladybug is climbing up a blade of grass.", "zh": "看玫瑰花叢旁邊這裡！一隻小小的七星瓢蟲正往草葉上爬呢。", "keywords": ["ladybug", "spotted", "blade"] },
      { "id": 4, "speaker": "Ruby", "avatar": "👧", "en": "Earthworms and friendly beetles are also wriggling through the loosened warm soil.", "zh": "蚯蚓和可愛的甲蟲也都在變得鬆軟溫暖的泥土裡鑽進鑽出。", "keywords": ["earthworms", "beetles", "wriggle"] },
      { "id": 5, "speaker": "Max", "avatar": "👦", "en": "The whole micro-world is bustling with brand new energy. Spring has officially stirred!", "zh": "整個微觀小世界都充滿了全新活力。春天真的徹底動起來了！", "keywords": ["bustling", "energy"] }
    ],
    "vocabulary": [
      { "word": "rumble", "phonetic": "/ˈrʌm.bəl/", "pos": "n./v.", "zh": "隆隆響聲、低沉轟鳴", "example": "We heard a deep rumble of distant thunder." },
      { "word": "ladybug", "phonetic": "/ˈleɪ.di.bʌɡ/", "pos": "n.", "zh": "瓢蟲", "example": "A bright red ladybug rested quietly on the daisy." },
      { "word": "wriggle", "phonetic": "/ˈrɪɡ.əl/", "pos": "v.", "zh": "扭動、蠕動", "example": "The playful puppy wriggled happily in my arms." }
    ],
    "dailyPhrase": { "en": "Bustle with energy.", "zh": "充滿活力熱鬧非凡。" },
    "cultureTip": "「驚蟄（Awakening of Insects）」通常在 3 月 5 日前後，春雷乍動、雨水增多，沉睡一冬的蟄伏生物紛紛破土出動。"
  },

  # 03-03 [國中挑戰]
  {
    "id": "dialogue-0303",
    "date": "03-03",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "多元文化",
    "topic": {
      "en": "Hinamatsuri and Peach Blossoms: Celebrating Growth and Wishes",
      "zh": "日本雛祭女兒節與桃花春信：祈願平安與健康成長"
    },
    "situation": "在國際文化社團課上，Ken 和日語交換生 Yuka 一起展示精緻的階梯人形偶與菱餅。",
    "speakers": {
      "Ken": { "role": "Ken", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Yuka": { "role": "Yuka", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0303.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ken", "avatar": "👦", "en": "Yuka, this tiered crimson stand with porcelain dolls is breathtakingly ornate! What festival is celebrated today?", "zh": "Yuka，這座鋪著深紅毛氈、擺滿瓷器人偶的階梯台架好華麗別緻！今天是慶祝什麼節日呀？", "keywords": ["tiered", "porcelain", "ornate"] },
      { "id": 2, "speaker": "Yuka", "avatar": "👧", "en": "Today is March third, Hinamatsuri, commonly translated as Doll's Day or Girls' Festival in Japan.", "zh": "今天是三月三日雛祭，在傳統日本常被稱為女兒節或人偶節。", "keywords": ["Hinamatsuri", "festival"] },
      { "id": 3, "speaker": "Ken", "avatar": "👦", "en": "I see the imperial emperor and empress at the very top. What is the historical purpose behind displaying them?", "zh": "我看到最頂層坐著宮廷天皇與皇后人偶。擺設這些精美偶人背後的歷史意義是什麼呢？", "keywords": ["emperor", "empress", "historical"] },
      { "id": 4, "speaker": "Yuka", "avatar": "👧", "en": "Originally, dolls were believed to absorb misfortunes and illness. Families pray for girls' healthy growth, happiness, and prosperity.", "zh": "最初人們相信人偶能帶走災病與晦氣。家庭藉此虔誠祈求女兒健康成長、一生幸福富貴。", "keywords": ["misfortunes", "prosperity", "healthy"] },
      { "id": 5, "speaker": "Ken", "avatar": "👦", "en": "Paired with pink peach blossoms and sweet tricolor rice cakes, it's such an aesthetic tribute to spring and family blessings.", "zh": "配上粉嫩盛開的桃花和三色菱餅，真是對春天與家庭祝願極具美感的心意表達。", "keywords": ["peach blossoms", "aesthetic", "blessings"] }
    ],
    "vocabulary": [
      { "word": "ornate", "phonetic": "/ɔːrˈneɪt/", "pos": "adj.", "zh": "華麗裝飾的、精雕細琢的", "example": "The palace doors were covered in ornate golden carvings." },
      { "word": "misfortune", "phonetic": "/ˌmɪsˈfɔːr.tʃuːn/", "pos": "n.", "zh": "厄運、不幸遭遇", "example": "They faced their misfortunes with admirable courage." },
      { "word": "aesthetic", "phonetic": "/esˈθet̬.ɪk/", "pos": "adj./n.", "zh": "美學的、審美的", "example": "The minimalist café has a very clean aesthetic." }
    ],
    "dailyPhrase": { "en": "A tribute to.", "zh": "對…的致敬與讚頌。" },
    "cultureTip": "日本 3 月 3 日雛祭（Hinamatsuri）又稱桃之節句（Momo no Sekku），吃象徵春雪融化、綠芽萌發、桃花初綻的三色菱餅（Hishimochi）。"
  },

  # 03-04 [高中進階]
  {
    "id": "dialogue-0304",
    "date": "03-04",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "社會心理學",
    "topic": {
      "en": "The Broken Windows Theory: Environmental Cues and Classroom Culture",
      "zh": "犯罪學與環境心理學：破窗效應如何塑造班級集體行為？"
    },
    "situation": "高中班會課後，副班長 Ryan 和班長 Olivia 留下來整理白板與散落課桌，探討環境秩序如何潛移默化影響集體心理。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0304.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "Olivia, I noticed that whenever a single discarded milk carton sits on the back shelf, three more appear by midday.", "zh": "Olivia，我發現只要後排架子上出現一個沒丟的空牛奶盒，中午前就會多出三個。", "keywords": ["discarded", "carton"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👩‍🎓", "en": "That is a textbook micro-demonstration of the Broken Windows Theory, first formulated by criminologists Wilson and Kelling.", "zh": "這正是犯罪學家威爾森和凱林提出的「破窗效應」在微觀環境下的教科書級體現。", "keywords": ["demonstration", "criminologists", "formulated"] },
      { "id": 3, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "The premise that visible signs of neglect or disorder signal that nobody cares, subtly lowering the threshold for further dereliction?", "zh": "核心前提在於：可見的忽視與失序信號會傳遞出『沒人在乎』的暗示，從而潛意識降低其他人破壞規矩的心理門檻？", "keywords": ["premise", "neglect", "dereliction", "threshold"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👩‍🎓", "en": "Precisely. If an environment radiates meticulous order and mutual respect, individuals subconsciously self-regulate and maintain civic accountability.", "zh": "完全沒錯。如果一個空間處處展現出一絲不苟的整潔與彼此尊重，個體就會下意識自我規範並維護公民責任。", "keywords": ["meticulous", "self-regulate", "accountability"] },
      { "id": 5, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "So wiping the marker board clean and aligning these desks isn't mere chore-work; it proactively inoculates our culture against chaos.", "zh": "所以把白板擦拭乾淨、排齊課桌椅不只是單純的值日打掃；它實質上是在主動為我們的班級氛圍注入秩序疫苗。", "keywords": ["proactively", "inoculate", "chaos"] }
    ],
    "vocabulary": [
      { "word": "premise", "phonetic": "/ˈprem.ɪs/", "pos": "n.", "zh": "前提、假設", "example": "The argument rested upon a flawed initial premise." },
      { "word": "dereliction", "phonetic": "/ˌder.əˈlɪk.ʃən/", "pos": "n.", "zh": "玩忽職守、怠惰遺棄", "example": "Leaving public equipment unmaintained is a dereliction of duty." },
      { "word": "meticulous", "phonetic": "/məˈtɪk.jə.ləs/", "pos": "adj.", "zh": "嚴謹一絲不苟的", "example": "She carried out meticulous proofreading before publishing." }
    ],
    "dailyPhrase": { "en": "Lower the threshold.", "zh": "降低門檻、削弱心理防線。" },
    "cultureTip": "「破窗效應（Broken Windows Theory）」1982 年提出，主張及時修復破窗、清理塗鴉能有效預防更嚴重的違規甚至犯罪，廣泛應用於班級經營與都市治理。"
  },

  # 03-05 [國小初階]
  {
    "id": "dialogue-0305",
    "date": "03-05",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "植物觀察",
    "topic": {
      "en": "Growing Hyacinths in Water on the Classroom Windowsill",
      "zh": "教室窗台水培紫藍風信子"
    },
    "situation": "自然課上，Leo 和 Mia 拿著透明玻璃瓶，將圓滾滾的風信子種球架在瓶口進行水培栽培。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0305.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Mia, look at my bulb! It looks just like a purple round onion.", "zh": "Mia，看我的種球！看起來長得跟紫色的圓洋蔥一模一樣呢。", "keywords": ["bulb", "onion"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "That is a hyacinth bulb! The teacher said we can grow it without any soil at all.", "zh": "那是風信子的鱗莖球！老師說我們完全不需要泥土就能把它水培長大喔。", "keywords": ["hyacinth", "soil"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "I filled this glass vase with fresh water up to the neck. The base of the bulb barely touches it.", "zh": "我把玻璃花瓶倒滿清水倒到瓶頸處。球莖底部剛剛好輕觸到水面。", "keywords": ["vase", "neck", "touches"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "In a few days, snow-white roots will stretch downward like tangled silk threads.", "zh": "再過幾天，雪白色的根鬚就會像糾纏的絲線一樣往下舒展生長。", "keywords": ["roots", "tangled", "threads"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "And soon, fragrant clusters of violet flowers will bloom right by our sunny window!", "zh": "不久後，一簇簇芬芳的紫羅蘭色小花就會在我們陽光明媚的窗邊盛開！", "keywords": ["fragrant", "clusters", "bloom"] }
    ],
    "vocabulary": [
      { "word": "bulb", "phonetic": "/bʌlb/", "pos": "n.", "zh": "植物球莖、球根；燈泡", "example": "Plant tulip bulbs in well-drained soil." },
      { "word": "fragrant", "phonetic": "/ˈfreɪ.ɡrənt/", "pos": "adj.", "zh": "芳香的、香氣撲鼻的", "example": "The garden was fragrant with blooming jasmine." },
      { "word": "cluster", "phonetic": "/ˈklʌs.tɚ/", "pos": "n./v.", "zh": "串、簇；聚集", "example": "A cluster of stars twinkled in the night sky." }
    ],
    "dailyPhrase": { "en": "In a few days.", "zh": "過幾天、不久之後。" },
    "cultureTip": "水培風信子（Hydroponic Hyacinth）是歐美與亞洲校園極受歡迎的春季自然觀察實驗，透明玻璃容器能讓孩子直接觀察到根系的生長奧祕。"
  },

  # 03-06 [國小中高]
  {
    "id": "dialogue-0306",
    "date": "03-06",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "體育健康",
    "topic": {
      "en": "Perfecting the Long Jump for Spring Sports Day",
      "zh": "春季校園運動會跳遠助跑與起跳技巧"
    },
    "situation": "體育課操場沙坑旁，Sam 和 Kevin 正在互相協助測量助跑步數，準備春季運動會跳遠項目。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Kevin": { "role": "Kevin", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0306.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Kevin, watch my run-up! I always seem to foul by stepping over the wooden take-off board.", "zh": "Kevin，看一下我的助跑！我好像每次都會踩過木製起跳板而犯規。", "keywords": ["run-up", "foul", "board"] },
      { "id": 2, "speaker": "Kevin", "avatar": "👦", "en": "That's because your stride length is inconsistent. Let's count back exactly twelve steady strides from the sandpit.", "zh": "那是因為你的步幅不均勻。我們從沙坑倒退精確量出十二個穩定的步幅吧。", "keywords": ["stride", "inconsistent", "sandpit"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Good idea. The coach told us to accelerate gradually instead of sprinting full speed right from step one.", "zh": "好主意。教練告訴我們要循序漸進加速，而不是第一步就盲目衝刺。", "keywords": ["accelerate", "sprinting"] },
      { "id": 4, "speaker": "Kevin", "avatar": "👦", "en": "Exactly. On your penultimate step, lower your hips slightly, then explode upward with your dominant leg!", "zh": "沒錯。在倒數第二步時略微放低臀部重心，然後用你的主力腳全力向上蹬起爆發！", "keywords": ["penultimate", "hips", "explode"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Here goes! Great speed, solid plant, and soaring over four meters into the soft sand!", "zh": "我要試跳了！速度漂亮、踏板扎實，高高躍起飛過四米穩穩落入鬆軟沙坑！", "keywords": ["solid", "soaring"] }
    ],
    "vocabulary": [
      { "word": "stride", "phonetic": "/straɪd/", "pos": "n./v.", "zh": "大步幅、跨步", "example": "He crossed the track with confident strides." },
      { "word": "accelerate", "phonetic": "/əkˈsel.ɚ.eɪt/", "pos": "v.", "zh": "加速、加快", "example": "The sports car accelerated smoothly onto the highway." },
      { "word": "penultimate", "phonetic": "/pəˈnʌl.tə.mət/", "pos": "adj.", "zh": "倒數第二的", "example": "The penultimate chapter revealed the shocking truth." }
    ],
    "dailyPhrase": { "en": "Here goes!", "zh": "來吧！看我的！開始了！" },
    "cultureTip": "跳遠（Long Jump）是一項結合助跑速度、踏跳爆發力與空中展體協調性的田徑項目，倒數第二步的重心微降能有效將水平速度轉換為向上跳躍力。"
  },

  # 03-07 [國中挑戰]
  {
    "id": "dialogue-0307",
    "date": "03-07",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "感恩教育",
    "topic": {
      "en": "Crafting Heartfelt Cards for International Women's Day",
      "zh": "手作精美賀卡感謝身邊默默付出的女性長輩與師長"
    },
    "situation": "美術教室裡，Alex 和 Maya 正在用乾燥花與壓花貼紙，為媽媽、奶奶和導師親手製作婦女節感恩卡片。",
    "speakers": {
      "Alex": { "role": "Alex", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Maya": { "role": "Maya", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0307.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Alex", "avatar": "👦", "en": "Maya, tomorrow is March eighth, International Women's Day. What thoughtful message did you write on your card?", "zh": "Maya，明天就是三月八日國際婦女節了。你在卡片上寫了什麼暖心的祝詞呀？", "keywords": ["International", "thoughtful"] },
      { "id": 2, "speaker": "Maya", "avatar": "👧", "en": "I wrote to my mom: 'Thank you for your tireless resilience and endless compassion that illuminate our home.'", "zh": "我寫給我媽媽：『感謝您不知疲倦的堅韌與無盡的溫柔包容，照亮了我們整個家。』", "keywords": ["resilience", "compassion", "illuminate"] },
      { "id": 3, "speaker": "Alex", "avatar": "👦", "en": "That's deeply moving. I am creating a pressed-sunflower bookmark for our homeroom teacher, Ms. Lin.", "zh": "太令人感動了。我正在為我們的導師林老師製作一個壓花向日葵書籤。", "keywords": ["bookmark", "homeroom", "moving"] },
      { "id": 4, "speaker": "Maya", "avatar": "👧", "en": "She works relentlessly, tutoring students patiently after school while balancing her own research.", "zh": "她總是無私付出，放學後耐心為同學課後輔導，同時兼顧自己的教學研究。", "keywords": ["relentlessly", "tutoring", "balancing"] },
      { "id": 5, "speaker": "Alex", "avatar": "👦", "en": "Expressing sincere gratitude doesn't require extravagant gifts; heartfelt words carry profound warmth.", "zh": "表達真摯的感謝不需要昂貴奢侈的禮物；發自肺腑的溫暖話語蘊含最深沉的力量。", "keywords": ["extravagant", "heartfelt", "profound"] }
    ],
    "vocabulary": [
      { "word": "resilience", "phonetic": "/rɪˈzɪl.jəns/", "pos": "n.", "zh": "堅韌、復原力", "example": "Her remarkable resilience helped the family through tough times." },
      { "word": "compassion", "phonetic": "/kəmˈpæʃ.ən/", "pos": "n.", "zh": "同理心、憐憫仁愛", "example": "Nurses treat patients with exceptional kindness and compassion." },
      { "word": "extravagant", "phonetic": "/ɪkˈstræv.ə.ɡənt/", "pos": "adj.", "zh": "奢侈的、鋪張昂貴的", "example": "They avoided extravagant spending and saved for college." }
    ],
    "dailyPhrase": { "en": "Heartfelt gratitude.", "zh": "由衷由心出發的感激之情。" },
    "cultureTip": "每年 3 月 8 日國際婦女節（IWD），世界各地學校與社區習慣向辛勤付出的母親、女性教師與各行各業女性致敬，送上鮮花或手寫感謝卡。"
  },

  # 03-08 [高中進階]
  {
    "id": "dialogue-0308",
    "date": "03-08",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "歷史與人權",
    "topic": {
      "en": "International Women's Day: Tracing the Centuries-Old Struggle for Equality",
      "zh": "國際婦女節：回溯女性爭取平權、選票與勞動尊嚴的百年征程"
    },
    "situation": "歷史思辨研討課上，Lucas 和 Sophia 回顧 20 世紀初紐約服裝女工大遊行與女性參政權運動的深遠歷史。",
    "speakers": {
      "Lucas": { "role": "Lucas", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Sophia": { "role": "Sophia", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0308.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lucas", "avatar": "👨‍🎓", "en": "Sophia, today many commercial brands dilute International Women's Day into merely giving discounts on cosmetics.", "zh": "Sophia，如今許多商業品牌把國際婦女節淡化包裝成僅僅是化妝品促銷打折的日子。", "keywords": ["dilute", "discounts", "commercial"] },
      { "id": 2, "speaker": "Sophia", "avatar": "👩‍🎓", "en": "Which entirely obscures its militant roots! It originated from the 1908 garment workers' strike in New York.", "zh": "這徹底模糊了它充滿抗爭與勇氣的歷史根源！它源於 1908 年紐約製衣女工的英勇罷工。", "keywords": ["obscures", "militant", "garment"] },
      { "id": 3, "speaker": "Lucas", "avatar": "👨‍🎓", "en": "Where fifteen thousand courageous women marched demanding shorter hours, equitable compensation, and universal voting rights under the slogan 'Bread and Roses'?", "zh": "當時一萬五千名勇敢女性走上街頭，在『麵包與玫瑰』的口號下爭取縮短工時、合理薪資與普選投票權？", "keywords": ["courageous", "equitable", "compensation", "slogan"] },
      { "id": 4, "speaker": "Sophia", "avatar": "👩‍🎓", "en": "Bread symbolizing economic security and subsistence, while roses encapsulated dignified quality of life and cultural fulfillment.", "zh": "麵包象徵經濟安全與生存尊嚴，而玫瑰則代表有尊嚴的生活品質與精神文化的滋養。", "keywords": ["subsistence", "encapsulated", "fulfillment"] },
      { "id": 5, "speaker": "Lucas", "avatar": "👨‍🎓", "en": "Remembering this legacy reminds us that gender equity is not a decorative courtesy, but a fundamental cornerstone of democratic justice.", "zh": "重溫這段歷史提醒我們：性別平等不是恩賜的裝飾點綴，而是民主正義不可或缺的基石。", "keywords": ["legacy", "equity", "cornerstone"] }
    ],
    "vocabulary": [
      { "word": "equitable", "phonetic": "/ˈek.wə.t̬ə.bəl/", "pos": "adj.", "zh": "公平合理的、公正的", "example": "The committee established an equitable distribution of resources." },
      { "word": "subsistence", "phonetic": "/səbˈsɪs.təns/", "pos": "n.", "zh": "勉強維持生計、生存底線", "example": "Farming families barely produced enough food for subsistence." },
      { "word": "cornerstone", "phonetic": "/ˈkɔːr.nɚ.stoʊn/", "pos": "n.", "zh": "奠基石、核心基石", "example": "Free expression is the cornerstone of an open civil society." }
    ],
    "dailyPhrase": { "en": "Bread and Roses.", "zh": "麵包與玫瑰（象徵生存保障與精神尊嚴雙重權利）。" },
    "cultureTip": "1908 年紐約女性工人的「Bread and Roses」罷工催生了三八婦女節。麵包象徵勞動者的工資與溫飽，玫瑰象徵免於剝削、享有尊嚴與美感生活的權利。"
  },

  # 03-09 [國小初階]
  {
    "id": "dialogue-0309",
    "date": "03-09",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "休閒生活",
    "topic": {
      "en": "Packing Delicious Club Sandwiches for a Sunny Spring Picnic",
      "zh": "陽光草地春日野餐：動手做切邊總匯三明治"
    },
    "situation": "週六早晨廚房裡，Toby 和妹妹 Zoe 正在準備野餐籃，切番茄與水煮蛋製作美味三明治。",
    "speakers": {
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0309.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Toby", "avatar": "👦", "en": "Zoe, look at the clear blue sky! Today is the perfect sunny Saturday for a park picnic!", "zh": "Zoe，看這片晴朗的藍天！今天是去公園野餐的完美陽光星期六！", "keywords": ["picnic", "Saturday"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Yay! I am spreading cream cheese on these fluffy whole wheat bread slices.", "zh": "太棒了！我正在把奶油乳酪抹在這些蓬鬆的全麥吐司切片上。", "keywords": ["spreading", "fluffy", "slices"] },
      { "id": 3, "speaker": "Toby", "avatar": "👦", "en": "I'll layer crisp green lettuce, juicy red tomato slices, and boiled egg rings in between.", "zh": "我會在中間鋪上脆爽的綠萵苣、多汁的紅番茄片和水煮蛋圈。", "keywords": ["crisp", "lettuce", "juicy"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Don't forget to cut them into cute triangles and pack our red-and-white checkered blanket!", "zh": "別忘了把它們對角切成可愛的三角形，還有帶上我們紅白格子野餐墊！", "keywords": ["triangles", "checkered", "blanket"] },
      { "id": 5, "speaker": "Toby", "avatar": "👦", "en": "All tucked neatly into the wicker basket. Let's pedal our bikes to the lawn!", "zh": "全部整整齊齊收進柳條野餐籃裡了。我們騎腳踏車去大草坪吧！", "keywords": ["wicker", "basket", "pedal"] }
    ],
    "vocabulary": [
      { "word": "fluffy", "phonetic": "/ˈflʌf.i/", "pos": "adj.", "zh": "蓬鬆的、鬆軟的", "example": "Freshly baked pancakes were warm and fluffy." },
      { "word": "lettuce", "phonetic": "/ˈlet̬.ɪs/", "pos": "n.", "zh": "萵苣、生菜", "example": "Wash the crunchy lettuce leaves thoroughly under cold water." },
      { "word": "checkered", "phonetic": "/ˈtʃek.ɚd/", "pos": "adj.", "zh": "方格圖案的", "example": "We spread a red checkered cloth on the picnic table." }
    ],
    "dailyPhrase": { "en": "A perfect day for.", "zh": "進行…的完美日子。" },
    "cultureTip": "春季野餐（Spring Picnic）是歐美家庭的經典週末戶外活動，經典標配包括三明治、切片水果與紅白格子野餐墊（Gingham picnic blanket）。"
  },

  # 03-10 [國小中高]
  {
    "id": "dialogue-0310",
    "date": "03-10",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "生態保育",
    "topic": {
      "en": "The Great Spring Migration: Welcoming Migratory Birds Back North",
      "zh": "候鳥北返季：觀察燕子歸來與城市生態綠色走廊"
    },
    "situation": "學校生態社團戶外課，Ben 和 Lily 舉著望遠鏡，在屋簷下與校園樹冠層觀察新築的燕子泥巢。",
    "speakers": {
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Lily": { "role": "Lily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0310.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ben", "avatar": "👦", "en": "Lily, look up at the third-floor roof eaves! A barn swallow is darting through the air!", "zh": "Lily，抬頭看三樓的屋簷！有一隻家燕正在空中靈巧地穿梭俯衝！", "keywords": ["eaves", "swallow", "darting"] },
      { "id": 2, "speaker": "Lily", "avatar": "👧", "en": "Wow, notice its fork-shaped tail feathers! It must have flew thousands of kilometers from the warm south.", "zh": "哇，看它剪刀一般的叉形尾羽！它一定是從溫暖的南方長途飛行了幾千公里回來的。", "keywords": ["feathers", "kilometers"] },
      { "id": 3, "speaker": "Ben", "avatar": "👦", "en": "Look inside the mud nest. The pair is busy carrying wet twigs and soft blades of grass to reinforce their nursery.", "zh": "看泥土築成的小鳥巢裡。這對燕子夫妻正忙著銜濕泥小樹枝和柔軟草葉加固愛巢呢。", "keywords": ["reinforce", "nursery", "twigs"] },
      { "id": 4, "speaker": "Lily", "avatar": "👧", "en": "City buildings can sometimes be dangerous with reflective glass windows that disorient birds.", "zh": "城市裡的高樓有時很危險，反光玻璃帷幕常常讓飛行的鳥兒迷失方向而撞上。", "keywords": ["reflective", "disorient", "dangerous"] },
      { "id": 5, "speaker": "Ben", "avatar": "👦", "en": "That's why our school installed bird-friendly stickers and preserved green tree corridors for safe migration!", "zh": "這就是為什麼我們學校貼了防鳥撞貼紙，並保留綠色樹冠走廊讓候鳥平安遷徙！", "keywords": ["corridors", "migration", "stickers"] }
    ],
    "vocabulary": [
      { "word": "dart", "phonetic": "/dɑːrt/", "pos": "v.", "zh": "飛奔、迅猛穿梭", "example": "A swift hummingbird darted between tropical flowers." },
      { "word": "disorient", "phonetic": "/dɪˈsɔːr.i.ent/", "pos": "v.", "zh": "使迷失方向、使頭暈昏眩", "example": "Dense night fog disoriented the mountain hikers." },
      { "word": "corridor", "phonetic": "/ˈkɔːr.ə.dɚ/", "pos": "n.", "zh": "走廊、通道；生態走廊", "example": "Green corridors allow wild animals to move safely between habitats." }
    ],
    "dailyPhrase": { "en": "Dart through the air.", "zh": "在空中敏捷穿梭疾飛。" },
    "cultureTip": "每年 3 月是北半球候鳥北返（Spring Migration）的關鍵季節。許多城市推動「Bird-friendly Architecture」，利用不反光玻璃避免鳥類撞擊慘劇。"
  },

  # 03-11 [國中挑戰]
  {
    "id": "dialogue-0311",
    "date": "03-11",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "勞動實作",
    "topic": {
      "en": "Prepping Soil and Composting for the School Garden",
      "zh": "校園園藝社春季開墾：堆肥發酵與鬆土除草技巧"
    },
    "situation": "園藝社課後，Ethan 和 Chloe 戴著粗布手套，在校園農園翻土並混入熟成堆肥，為新學期蔬菜種植做準備。",
    "speakers": {
      "Ethan": { "role": "Ethan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0311.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ethan", "avatar": "👦", "en": "Phew, Chloe, this compacted winter soil is remarkably dense! My pitchfork can barely penetrate the top layer.", "zh": "呼，Chloe，歷經冬天的泥土被壓得真緊實！我的園藝鐵叉差點插不進表層土裡。", "keywords": ["compacted", "dense", "penetrate"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "Step on the fork's shoulder to use your body weight. Loosening the hard soil aerates it so young roots can breathe.", "zh": "踩在叉柄肩部運用你的體重。把硬土翻鬆能讓土壤通氣，這樣幼苗根部才能大口呼吸。", "keywords": ["aerates", "loosening"] },
      { "id": 3, "speaker": "Ethan", "avatar": "👦", "en": "Now let's incorporate two wheelbarrows of organic compost from our school bin behind the cafeteria.", "zh": "現在我們把從餐廳後面廚餘堆肥箱熟成好的兩輪手推車有機肥拌進去吧。", "keywords": ["wheelbarrows", "organic", "compost"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "Smell that? It doesn't smell foul at all; it possesses that rich, earthy aroma of healthy decomposing matter.", "zh": "聞到了嗎？一點都不臭；它散發著健康分解有機質特有的濃郁泥土芳香。", "keywords": ["foul", "earthy", "decomposing"] },
      { "id": 5, "speaker": "Ethan", "avatar": "👦", "en": "With abundant nitrogen and minerals replenished, our upcoming cherry tomatoes will thrive vigorously!", "zh": "補充了滿滿的氮肥與礦物質，我們即將播種的小番茄一定會健健康康茁壯成長！", "keywords": ["replenished", "thrive", "vigorously"] }
    ],
    "vocabulary": [
      { "word": "aerate", "phonetic": "/ˈer.eɪt/", "pos": "v.", "zh": "使充氣、使透氣", "example": "Earthworms help aerate compacted garden soil naturally." },
      { "word": "compost", "phonetic": "/ˈkɑːm.poʊst/", "pos": "n./v.", "zh": "堆肥；把…製成堆肥", "example": "Kitchen vegetable peelings make excellent organic compost." },
      { "word": "replenish", "phonetic": "/rɪˈplen.ɪʃ/", "pos": "v.", "zh": "補充、重新裝滿", "example": "Drink plenty of water to replenish lost fluids after sports." }
    ],
    "dailyPhrase": { "en": "Thrive vigorously.", "zh": "生氣蓬勃地茁壯成長。" },
    "cultureTip": "有機堆肥（Composting）將廚餘菜葉與落葉轉化為「黑金（Black Gold）」腐殖質，是校園循環農業與食農教育的重要實踐。"
  },

  # 03-12 [高中進階]
  {
    "id": "dialogue-0312",
    "date": "03-12",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "環境科學",
    "topic": {
      "en": "Arbor Day and Urban Forestry: Why Reforestation Is Essential for Cities",
      "zh": "植樹節與都市林業：行道樹與樹冠層如何對抗城市熱島效應？"
    },
    "situation": "植樹節當天，青年環保倡議社幹部 Eric 和 Natalie 在校園北側苗圃栽種原生樟樹幼苗，深入探討城市樹冠的生態微氣候效益。",
    "speakers": {
      "Eric": { "role": "Eric", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Natalie": { "role": "Natalie", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0312.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Eric", "avatar": "👨‍🎓", "en": "Natalie, hold this camphor sapling upright while I shovel the topsoil into the planting cavity.", "zh": "Natalie，當我把表土鏟進樹坑時，幫我把這株樟樹小樹苗垂直扶正。", "keywords": ["sapling", "upright", "cavity"] },
      { "id": 2, "speaker": "Natalie", "avatar": "👩‍🎓", "en": "Got it. People often perceive tree-planting on Arbor Day as merely symbolic, but urban canopies provide tangible ecological infrastructure.", "zh": "抓穩了。許多人常把植樹節種樹當作純粹的形式象徵，但都市樹冠層實質上提供了實打實的生態基礎設施。", "keywords": ["perceive", "symbolic", "canopies", "infrastructure"] },
      { "id": 3, "speaker": "Eric", "avatar": "👨‍🎓", "en": "Beyond carbon sequestration, evapotranspiration from dense tree leaves can depress localized ambient temperatures by several degrees Celsius.", "zh": "除了固碳吸收二氧化碳，茂密葉片的水分蒸散作用還能讓局部周遭氣溫降低攝氏好幾度。", "keywords": ["sequestration", "evapotranspiration", "ambient"] },
      { "id": 4, "speaker": "Natalie", "avatar": "👩‍🎓", "en": "Significantly mitigating the Urban Heat Island effect caused by asphalt roads and concrete high-rises absorbing solar radiation.", "zh": "大幅緩解柏油路面與混凝土高樓吸收太陽輻射所引發的嚴重『都市熱島效應』。", "keywords": ["mitigating", "asphalt", "radiation"] },
      { "id": 5, "speaker": "Eric", "avatar": "👨‍🎓", "en": "As this young root system anchors into the ground today, we are literally investing in the climate resilience of our city decades down the road.", "zh": "隨著這株小樹苗的根系在今日扎根泥土，我們實質上是在為城市數十年後的氣候韌性做出長遠投資。", "keywords": ["anchors", "resilience", "investing"] }
    ],
    "vocabulary": [
      { "word": "sapling", "phonetic": "/ˈsæp.lɪŋ/", "pos": "n.", "zh": "樹苗、幼樹", "example": "The city planted a hundred oak saplings along the river avenue." },
      { "word": "ambient", "phonetic": "/ˈæm.bi.ənt/", "pos": "adj.", "zh": "周遭的、周圍環境的", "example": "The ambient temperature dropped sharply after sunset." },
      { "word": "mitigate", "phonetic": "/ˈmɪt̬.ə.ɡeɪt/", "pos": "v.", "zh": "緩和、減輕", "example": "Emergency flood walls helped mitigate the storm damage." }
    ],
    "dailyPhrase": { "en": "Down the road.", "zh": "在未來、長遠來看。" },
    "cultureTip": "3 月 12 日為植樹節（Arbor Day）。「Arbor」源於拉丁文「樹」，都市林學（Urban Forestry）現已被世界衛生組織列為降低熱浪傷亡與心理壓力的重要城市資產。"
  },

  # 03-13 [國小初階]
  {
    "id": "dialogue-0313",
    "date": "03-13",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "趣味生活",
    "topic": {
      "en": "Stomping in Puddles with Bright Yellow Rain Boots",
      "zh": "穿上亮黃色雨靴踩水花，帶彩色小雨傘上學"
    },
    "situation": "春雨綿綿的早晨，Leo 和 Mia 穿著雨衣和膠靴，走在校門口的人行道上踩水花嬉戲。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0313.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Mia, look at my bright yellow rain boots! Splish, splash, stomp!", "zh": "Mia，看我的亮黃色雨靴！噗滋、啪嗒、大步踩！", "keywords": ["boots", "splash", "stomp"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "Haha, be careful, Leo! You are splashing raindrops all over your rainbow umbrella!", "zh": "哈哈，小心點啦 Leo！你的水花濺得彩虹雨傘上到處都是水滴了！", "keywords": ["raindrops", "umbrella", "rainbow"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "The puddles on the sidewalk look like little shiny mirrors reflecting the gray sky.", "zh": "人行道上的積水窪看起來就像一面面閃亮的小鏡子，倒映著灰濛濛的天空。", "keywords": ["puddles", "mirrors", "reflecting"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "Listen to the rain drops drumming on our umbrellas: tap-tap-tap, ping-ping-ping!", "zh": "聽雨滴敲打在我們雨傘上的聲音：滴答答、淅瀝瀝！", "keywords": ["drumming", "rain"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Spring rain is like music for the thirsty flowers. Rainy walks to school are so joyful!", "zh": "春雨就像彈給口渴花兒聽的音樂。下雨天上學真是一場歡樂的冒險！", "keywords": ["thirsty", "joyful"] }
    ],
    "vocabulary": [
      { "word": "puddle", "phonetic": "/ˈpʌd.əl/", "pos": "n.", "zh": "水窪、泥水坑", "example": "Ducklings were joyfully swimming in a large rain puddle." },
      { "word": "stomp", "phonetic": "/stɑːmp/", "pos": "v.", "zh": "跺腳、重重踩地", "example": "The children laughed and stomped through the shallow water." },
      { "word": "joyful", "phonetic": "/ˈdʒɔɪ.fəl/", "pos": "adj.", "zh": "歡樂高興的、充滿喜悅的", "example": "A joyful cheer erupted from the winning school team." }
    ],
    "dailyPhrase": { "en": "Splish, splash, stomp!", "zh": "撲通水花大步踩（形容雨天穿雨靴踩水的歡樂狀聲詞）。" },
    "cultureTip": "在許多國家的童年回憶裡，穿著雨靴踩水窪（Puddle Jumping）是一項被兒童心理學家推薦的自然感官探索遊戲，能增強平衡與對自然的親近感。"
  },

  # 03-14 [國小中高]
  {
    "id": "dialogue-0314",
    "date": "03-14",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "數理趣談",
    "topic": {
      "en": "Happy Pi Day: Savoring Sweet Pies and Reciting Decimals",
      "zh": "歡慶 3.14 圓周率日：享用香脆蘋果派與背誦數字遊戲"
    },
    "situation": "數學課下課時間，Max 和 Ruby 圍在黑板前，挑戰誰能背出更多位圓周率小數點，並分享烘烤的蘋果派。",
    "speakers": {
      "Max": { "role": "Max", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Ruby": { "role": "Ruby", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0314.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Max", "avatar": "👦", "en": "Ruby, do you know what international math celebration falls on March fourteenth?", "zh": "Ruby，你知道三月十四日是國際上什麼數學節日嗎？", "keywords": ["international", "celebration"] },
      { "id": 2, "speaker": "Ruby", "avatar": "👧", "en": "It's Pi Day! Because today's date matches 3.14, the most famous mathematical constant in history!", "zh": "是圓周率日（Pi Day）！因為今天的日期剛好對應 3.14，歷史上最著名的數學常數！", "keywords": ["constant", "mathematical"] },
      { "id": 3, "speaker": "Max", "avatar": "👦", "en": "Can you recite beyond three point one four? Let's hear your memory skills!", "zh": "你能在 3.14 之後背出幾位呢？展示一下你的記憶大考驗吧！", "keywords": ["recite", "memory"] },
      { "id": 4, "speaker": "Ruby", "avatar": "👧", "en": "Three point one four one five nine two six five three five eight nine... It's an endless irrational number!", "zh": "3.141592653589… 它是一個永無止境且不循環的無理數！", "keywords": ["irrational", "endless"] },
      { "id": 5, "speaker": "Max", "avatar": "👦", "en": "Bravo! And since Pi sounds exactly like edible 'pie', our math teacher brought freshly baked apple pie for everyone!", "zh": "太厲害了！而且因為 Pi 的發音跟吃的『派』一模一樣，數學老師為大家帶來了現烤的熱蘋果派呢！", "keywords": ["edible", "baked", "Bravo"] }
    ],
    "vocabulary": [
      { "word": "constant", "phonetic": "/ˈkɑːn.stənt/", "pos": "n.", "zh": "常數、恆常不變的值", "example": "In geometry, pi is the ratio constant of circle circumference." },
      { "word": "recite", "phonetic": "/rɪˈsaɪt/", "pos": "v.", "zh": "背誦、朗誦", "example": "She recited the entire Shakespeare sonnet by heart." },
      { "word": "irrational", "phonetic": "/ɪˈræʃ.ən.əl/", "pos": "adj.", "zh": "無理數的；不理性的", "example": "An irrational number cannot be expressed as a simple fraction." }
    ],
    "dailyPhrase": { "en": "By heart.", "zh": "憑記憶背出、牢記在心。" },
    "cultureTip": "3 月 14 日是「國際圓周率日（Pi Day）」，也是物理學大師愛因斯坦的生日。世界各地的學校師生習慣在下午 1 點 59 分吃圓形派（Pie）並舉辦背誦比賽。"
  },

  # 03-15 [國中挑戰]
  {
    "id": "dialogue-0315",
    "date": "03-15",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "公民素養",
    "topic": {
      "en": "World Consumer Rights Day: Smart Shopping and Avoiding Deceptive Marketing",
      "zh": "世界消費者權益日：明智消費、退換貨權益與辨識虛假宣傳"
    },
    "situation": "公民課小組討論時，Jason 和 Emily 正在檢視手邊網購耳機的電子發票與保固條款，探討消費者權益。",
    "speakers": {
      "Jason": { "role": "Jason", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emily": { "role": "Emily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0315.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Jason", "avatar": "👦", "en": "Emily, my sister ordered wireless earbuds online last week, but the left earbud stopped charging after just two days.", "zh": "Emily，我姐姐上週網購了一副無線耳機，但才用兩天左耳機就充不進電了。", "keywords": ["earbuds", "charging"] },
      { "id": 2, "speaker": "Emily", "avatar": "👧", "en": "Did she keep the digital receipt and packaging? Under consumer protection statutes, online purchases come with unconditional cooling-off return rights.", "zh": "她有保留電子發票和包裝盒嗎？根據消費者保護法規，網購享有鑑賞期無條件退換貨權利喔。", "keywords": ["receipt", "statutes", "cooling-off"] },
      { "id": 3, "speaker": "Jason", "avatar": "👦", "en": "Yes, seven days! Today is March fifteenth, World Consumer Rights Day. The seller initially claimed 'clearance items are non-refundable'.", "zh": "對，七天猶豫期！今天正好是 3 月 15 日世界消費者權益日。賣家一開始還宣稱『特價清倉商品概不退款』呢。", "keywords": ["refundable", "clearance"] },
      { "id": 4, "speaker": "Emily", "avatar": "👧", "en": "That merchant clause is unlawful. Sellers cannot arbitrarily void legal statutory rights through vague small print disclaimers.", "zh": "商家的那條約定是無效違法的。賣家不能隨便用模糊的小字免責聲明推翻法定的權利保障。", "keywords": ["unlawful", "arbitrarily", "disclaimers"] },
      { "id": 5, "speaker": "Jason", "avatar": "👦", "en": "She filed an inquiry and received an immediate full refund. Being legally literate is our best shield against deceptive business practices!", "zh": "她提出申訴後立刻拿到了全額退款。懂得法律常識真的是我們對抗不良消費陷阱最好的盾牌！", "keywords": ["refund", "literate", "deceptive"] }
    ],
    "vocabulary": [
      { "word": "statute", "phonetic": "/ˈstætʃ.uːt/", "pos": "n.", "zh": "法令、成文法規", "example": "The consumer rights statute protects shoppers from counterfeit goods." },
      { "word": "arbitrarily", "phonetic": "/ˌɑːr.bəˈtrer.əl.i/", "pos": "adv.", "zh": "任意地、專斷地", "example": "The company arbitrarily canceled customer reward accounts." },
      { "word": "disclaimer", "phonetic": "/dɪˈskleɪ.mɚ/", "pos": "n.", "zh": "免責聲明、卸責告示", "example": "Read the product warranty disclaimer carefully before purchasing." }
    ],
    "dailyPhrase": { "en": "Cooling-off period.", "zh": "反悔冷靜期、鑑賞猶豫期。" },
    "cultureTip": "3 月 15 日為「世界消費者權益日（World Consumer Rights Day）」，紀念 1962 年甘迺迪總統發表著名的消費者四大基本權利演說：安全權、知情權、選擇權與表達意見權。"
  },

  # 03-16 [高中進階]
  {
    "id": "dialogue-0316",
    "date": "03-16",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "認知心理學",
    "topic": {
      "en": "The Myth of Multitasking: Attention Residue and the Power of Deep Work",
      "zh": "認知神經科學：多工處理的迷思、注意力殘留與深度工作之道"
    },
    "situation": "自習課後，準備專題研究的 Ryan 和 Olivia 分享自己在寫代碼與閱讀長文時，如何克服手機即時通訊頻繁中斷造成的專注崩潰。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0316.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "Olivia, I used to take pride in 'multitasking'—listening to a podcast while toggling between three research essays and instant chat.", "zh": "Olivia，我以前總以『多工處理』為傲——一邊聽播客，一邊在三篇論文視窗和即時通訊軟體間來回切換。", "keywords": ["multitasking", "toggling"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👩‍🎓", "en": "Neuroscience conclusively proves that human brains cannot process dual demanding cognitive tasks simultaneously; we are merely task-switching frantically.", "zh": "神經科學已經充分證實人類大腦無法同時處理兩項高認知的複雜任務；我們只不過是在慌亂地頻繁切換而已。", "keywords": ["conclusively", "cognitive", "task-switching"] },
      { "id": 3, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "And every single switch imposes a hefty switching tax known as 'attention residue', where part of your mental bandwidth remains stranded on the previous task.", "zh": "而且每一次切換都要付出巨大的『切換稅』，也就是所謂的『注意力殘留』，部分心智頻寬始終卡在剛才的任務上。", "keywords": ["residue", "bandwidth", "stranded"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👩‍🎓", "en": "Exactly. Dr. Cal Newport's concept of 'Deep Work' shows that profound intellectual breakthroughs require uninterrupted stretches of intense, single-pointed concentration.", "zh": "一點也沒錯。卡爾·紐波特博士在《深度工作力》指出，深刻的心智突破必須仰賴長時間不被打擾、專注於單一目標的深度沉浸。", "keywords": ["uninterrupted", "intellectual", "breakthroughs"] },
      { "id": 5, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "Putting my smartphone into 'Do Not Disturb' and doing ninety-minute focused sprints has doubled my comprehension efficiency.", "zh": "把手機開啟『勿擾模式』並進行九十分鐘的深度專注衝刺，讓我的閱讀理解效率直接翻倍了。", "keywords": ["comprehension", "efficiency", "sprints"] }
    ],
    "vocabulary": [
      { "word": "conclusive", "phonetic": "/kənˈkluː.sɪv/", "pos": "adj.", "zh": "確定性的、無可置疑的", "example": "DNA evidence provided conclusive proof of identity." },
      { "word": "residue", "phonetic": "/ˈrez.ə.duː/", "pos": "n.", "zh": "殘留物、剩餘物", "example": "Oily residue remained on the pan after inadequate washing." },
      { "word": "uninterrupted", "phonetic": "/ˌʌn.ɪn.t̬əˈrʌp.tɪd/", "pos": "adj.", "zh": "連續不中斷的", "example": "He enjoyed eight hours of uninterrupted deep sleep." }
    ],
    "dailyPhrase": { "en": "Attention residue.", "zh": "注意力殘留（心理學概念：從前一項工作切換時殘留的分神現象）。" },
    "cultureTip": "計算機科學家 Cal Newport 提出的「深度工作（Deep Work）」理論指出，現代人在社交媒體碎片化干擾下，具備「長時間不分心深度專注」的能力已成為極具價值的稀缺超能力。"
  },

  # 03-17 [國小初階]
  {
    "id": "dialogue-0317",
    "date": "03-17",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "趣味節日",
    "topic": {
      "en": "St. Patrick's Day: Wearing Emerald Green and Spotting Four-Leaf Clovers",
      "zh": "聖派翠克節：穿上翠綠衣裳與尋找幸運四葉幸運草"
    },
    "situation": "英語情境教室裡，Toby 和 Zoe 身穿鮮綠色衛衣，在假草皮地毯上尋找藏著的四葉草徽章。",
    "speakers": {
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0317.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Toby", "avatar": "👦", "en": "Zoe, look at me! I am wearing green socks, a green hoodie, and a shiny shamrock hat!", "zh": "Zoe，快看我！我穿了綠襪子、綠色帽T，還戴了頂亮晶晶的三葉草帽子！", "keywords": ["shamrock", "hoodie"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Happy St. Patrick's Day! If you don't wear green today, playful leprechauns might give you a gentle pinch!", "zh": "聖派翠克節快樂！如果今天沒穿綠色衣服，調皮的愛爾蘭小精靈可是會輕輕捏你一下的喔！", "keywords": ["leprechauns", "pinch"] },
      { "id": 3, "speaker": "Toby", "avatar": "👦", "en": "Look down here in the clover patch! Most shamrocks have three leaves, but I found one with four!", "zh": "看酢漿草叢這裡！大部分的三葉草都只有三片葉子，但我找到了一朵有四片葉子的！", "keywords": ["clover", "patch"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "A real four-leaf clover! That brings extra good luck and maybe a pot of gold at the rainbow's end!", "zh": "真的四葉幸運草耶！這會帶來滿滿的幸運，說不定彩虹盡頭真藏著一整罐金幣呢！", "keywords": ["rainbow", "gold", "luck"] },
      { "id": 5, "speaker": "Toby", "avatar": "👦", "en": "Let's press it between thick books so we can preserve our lucky green treasure forever.", "zh": "我們把它夾在厚書裡壓平風乾，這樣就能把這份幸運的綠色寶藏永遠留下來啦。", "keywords": ["preserve", "treasure"] }
    ],
    "vocabulary": [
      { "word": "clover", "phonetic": "/ˈkloʊ.vɚ/", "pos": "n.", "zh": "三葉草、車軸草", "example": "Cows grazed contentedly in pastures full of sweet clover." },
      { "word": "pinch", "phonetic": "/pɪntʃ/", "pos": "v./n.", "zh": "捏、掐；一小撮", "example": "Add a tiny pinch of salt to the dough." },
      { "word": "preserve", "phonetic": "/prɪˈzɝːv/", "pos": "v.", "zh": "保存、珍藏", "example": "Museums help preserve precious ancient artifacts." }
    ],
    "dailyPhrase": { "en": "A pot of gold.", "zh": "彩虹盡頭的一桶金（象徵夢想與好運財富）。" },
    "cultureTip": "3 月 17 日是愛爾蘭重要節日「聖派翠克節（St. Patrick's Day）」。人們身著綠衣、配戴三葉草（Shamrock），芝加哥甚至會將整條市區河流染成翠綠色狂歡慶祝。"
  },

  # 03-18 [國小中高]
  {
    "id": "dialogue-0318",
    "date": "03-18",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "健康生活",
    "topic": {
      "en": "National Liver Day: Establishing a Restful Sleep Routine",
      "zh": "守護小心肝：告別熬夜，養成十點入睡的健康作息"
    },
    "situation": "晨會結束後，Sam 和 Kevin 討論健康中心的宣導看板，認識肝臟如何幫助人體排毒與早睡充足睡眠的重要性。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Kevin": { "role": "Kevin", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0318.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Kevin, you look sleepy this morning! Did you stay up late playing video games again?", "zh": "Kevin，你今天早上看起來睡眼惺忪的！你昨晚是不是又熬夜打電動了？", "keywords": ["sleepy", "stay up late"] },
      { "id": 2, "speaker": "Kevin", "avatar": "👦", "en": "Guilty as charged. I lost track of time and didn't fall asleep until almost midnight.", "zh": "被你抓包了。我玩到忘記時間，快半夜十二點才躺下睡覺。", "keywords": ["guilty", "midnight"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "The nurse told us today is National Liver Day! Our liver works like a silent chemical factory.", "zh": "護理師跟我們說今天是全國愛肝日！我們的肝臟就像一座無聲辛勤運轉的化學工廠。", "keywords": ["liver", "chemical", "factory"] },
      { "id": 4, "speaker": "Kevin", "avatar": "👦", "en": "Right, filtering toxins, storing vitamins, and repairing damaged cells while we are in deep slumber.", "zh": "沒錯，在我們深度睡眠時過濾體內毒素、儲存維生素並修復受損細胞。", "keywords": ["filtering", "toxins", "slumber"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "If we sleep past ten thirty consistently, the liver can't rest properly. Tonight, phones away by nine thirty!", "zh": "如果總是拖到十點半以後才睡，肝臟就無法好好休息復原。今晚九點半準時把手機收起來！", "keywords": ["consistently", "properly"] }
    ],
    "vocabulary": [
      { "word": "toxin", "phonetic": "/ˈtɑːk.sɪn/", "pos": "n.", "zh": "毒素、有害物質", "example": "Drinking clean water helps the kidneys flush out toxins." },
      { "word": "slumber", "phonetic": "/ˈslʌm.bɚ/", "pos": "n./v.", "zh": "安眠、睡眠", "example": "The tired baby fell into a peaceful, unbroken slumber." },
      { "word": "consistently", "phonetic": "/kənˈsɪs.tənt.li/", "pos": "adv.", "zh": "持之以恆地、一貫地", "example": "Athletes who practice consistently achieve superior performance." }
    ],
    "dailyPhrase": { "en": "Lost track of time.", "zh": "忘記了時間、不知不覺過得很快。" },
    "cultureTip": "3 月 18 日為「全國愛肝日」。醫學研究表明，晚間 11 點至凌晨 3 點是人體肝膽經絡排毒與細胞修復的黃金時段，充足深層睡眠是保護肝臟最重要的天然良方。"
  },

  # 03-19 [國中挑戰]
  {
    "id": "dialogue-0319",
    "date": "03-19",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "地球科學",
    "topic": {
      "en": "Tracking Sun Altitude and Equalizing Shadows Before Equinox",
      "zh": "春分前夕實測：校園日影長度與太陽高度角變化"
    },
    "situation": "地理地科課正午十二點，Alex 和 Maya 帶著量角器與一米長的木標竿，在司令台前測量竿影長度。",
    "speakers": {
      "Alex": { "role": "Alex", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Maya": { "role": "Maya", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0319.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Alex", "avatar": "👦", "en": "Maya, hold the meter ruler perfectly perpendicular to the concrete ground! Exactly noon local solar time.", "zh": "Maya，把這一米長的標竿垂直立在水泥地上！當地太陽正午時間十二點整到了。", "keywords": ["perpendicular", "noon", "ruler"] },
      { "id": 2, "speaker": "Maya", "avatar": "👧", "en": "Shadow recorded: exactly fifty-seven centimeters long. That's noticeably shorter than our December winter solstice measurement!", "zh": "竿影長度記錄完畢：正好五十七公分長。這明顯比我們十二月冬至時量的影子短太多了！", "keywords": ["measurement", "solstice", "noticeably"] },
      { "id": 3, "speaker": "Alex", "avatar": "👦", "en": "Because the sun's subsolar point is migrating steadily northward across the equator as we approach the Vernal Equinox.", "zh": "因為隨著春分逼近，太陽直射點正朝北回歸線方向穩定由赤道向北移動。", "keywords": ["subsolar", "equator", "migrating"] },
      { "id": 4, "speaker": "Maya", "avatar": "👧", "en": "Using simple trigonometry: tangent of solar elevation angle equals pole height divided by shadow length.", "zh": "用簡單的三角幾何：太陽高度角的正切值就等於標竿高度除以影子長度。", "keywords": ["trigonometry", "tangent", "elevation"] },
      { "id": 5, "speaker": "Alex", "avatar": "👦", "en": "The midday sun is climbing higher each day, and daytime and nighttime are about to become completely equal tomorrow!", "zh": "正午太陽每天都爬得更高，而且明天白天和黑夜的時間就即將完全等長了！", "keywords": ["climbing", "daytime"] }
    ],
    "vocabulary": [
      { "word": "perpendicular", "phonetic": "/ˌpɝː.pənˈdɪk.jə.lɚ/", "pos": "adj.", "zh": "垂直的、成九十度角的", "example": "The tall telephone pole stood perpendicular to the hillside road." },
      { "word": "elevation", "phonetic": "/ˌel.əˈveɪ.ʃən/", "pos": "n.", "zh": "海拔高度；仰角", "example": "Calculate the angle of solar elevation at solar noon." },
      { "word": "trigonometry", "phonetic": "/ˌtrɪɡ.əˈnɑː.mə.tri/", "pos": "n.", "zh": "三角學", "example": "Trigonometry allows surveyors to determine mountain heights remotely." }
    ],
    "dailyPhrase": { "en": "Perpendicular to.", "zh": "與…保持垂直正交。" },
    "cultureTip": "春分前夕，全球太陽高度角迅速抬升。在北半球，白晝時間每天以 2 到 3 分鐘的速度延長，竿影長度逐日縮短，直至夏至達到最短。"
  },

  # 03-20 [高中進階]
  {
    "id": "dialogue-0320",
    "date": "03-20",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "天文科普",
    "topic": {
      "en": "The Vernal Equinox: Celestial Mechanics and the Global Egg-Balancing Legend",
      "zh": "春分節氣：太陽直射赤道的天體力學與全球「立蛋」傳奇真相"
    },
    "situation": "天文社春分科普活動中，社長 Lucas 和社員 Sophia 在實驗室桌上小心翼翼嘗試立起生雞蛋，剖析民間傳奇背後的物理學真偽。",
    "speakers": {
      "Lucas": { "role": "Lucas", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Sophia": { "role": "Sophia", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0320.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lucas", "avatar": "👨‍🎓", "en": "Sophia, steady your breath! I actually got this raw egg to balance upright on its wider end on the flat tabletop!", "zh": "Sophia，屏住呼吸！我真的成功讓這顆生雞蛋較寬的一端在平坦桌面上直立起來了！", "keywords": ["balance", "upright", "tabletop"] },
      { "id": 2, "speaker": "Sophia", "avatar": "👩‍🎓", "en": "Impressive patience! But scientifically speaking, does the Vernal Equinox truly provide magical gravitational alignment for egg-balancing?", "zh": "耐心可嘉！但從科學角度來說，春分真的有提供什麼神奇的天體重力排列讓蛋容易立起來嗎？", "keywords": ["gravitational", "alignment", "equinox"] },
      { "id": 3, "speaker": "Lucas", "avatar": "👨‍🎓", "en": "That's a widespread urban myth. Astronomically, the equinox simply means the sun crosses the celestial equator, resulting in equal twelve-hour day and night across the globe.", "zh": "那是流傳甚廣的都市傳奇。在天文學上，春分僅僅代表太陽穿越天球赤道，使全球各地晝夜均分各十二小時。", "keywords": ["astronomically", "celestial", "equator"] },
      { "id": 4, "speaker": "Sophia", "avatar": "👩‍🎓", "en": "The gravitational pull of the sun is infinitesimal compared to Earth's gravity. Balancing an egg relies solely on surface bumps, a low center of mass, and steady hands.", "zh": "太陽的引力與地球重力相比簡直微乎其微。立蛋純粹取決於蛋殼微小的凹凸接觸點、蛋黃沉降降低重心，以及一雙沉穩的手。", "keywords": ["infinitesimal", "gravity", "bumps"] },
      { "id": 5, "speaker": "Lucas", "avatar": "👨‍🎓", "en": "Still, debunking the myth doesn't ruin the poetry of the day—celebrating cosmic harmony and welcoming the radiant light of spring.", "zh": "不過，破解迷思並無損於這個節氣的浪漫詩意——慶祝宇宙運行和諧平衡，並迎接春日璀璨光明。", "keywords": ["debunking", "cosmic", "harmony"] }
    ],
    "vocabulary": [
      { "word": "alignment", "phonetic": "/əˈlaɪn.mənt/", "pos": "n.", "zh": "成一線、排列、對齊", "example": "The planetary alignment was a spectacular astronomical event." },
      { "word": "infinitesimal", "phonetic": "/ˌɪn.fɪ.nəˈtes.ə.məl/", "pos": "adj.", "zh": "極微小的、無限趨近於零的", "example": "A single dust particle has an infinitesimal weight." },
      { "word": "debunk", "phonetic": "/diːˈbʌŋk/", "pos": "v.", "zh": "揭穿虛假、駁斥偽科學", "example": "The science documentary systematically debunked popular UFO theories." }
    ],
    "dailyPhrase": { "en": "Debunk the myth.", "zh": "破除迷思、揭示科學真相。" },
    "cultureTip": "春分（Vernal Equinox）通常在 3 月 20 或 21 日，太陽直射赤道，全球晝夜等長（拉丁語 Aequus 等同 + Nox 黑夜）。民間「春分立蛋」其實在一年 365 天任何一天只要有耐心都能成功。"
  },

  # 03-21 [國小初階]
  {
    "id": "dialogue-0321",
    "date": "03-21",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "語文童趣",
    "topic": {
      "en": "World Poetry Day: Rhyming Sweet Spring Nursery Rhymes",
      "zh": "世界詩歌日：朗朗上口朗讀可愛春日英語童謠"
    },
    "situation": "圖書館兒童閱讀區裡，Leo 和 Mia 翻閱色彩繽紛的童詩繪本，輪流大聲朗讀押韻童謠。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0321.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Mia, the school librarian said today is World Poetry Day! Let's read poems together!", "zh": "Mia，學校圖書館阿姨說今天是世界詩歌日！我們一起來讀詩吧！", "keywords": ["Poetry", "librarian"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "Listen to this one: 'Little yellow butterfly, flutter flutter in the sky! Up above the grass so high!'", "zh": "聽這首：『黃色小蝴蝶，天空翩翩飛！高高飛舞在綠草坪上面！』", "keywords": ["butterfly", "flutter", "sky"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "The words 'butterfly', 'sky', and 'high' all rhyme together! That sounds so bouncy and fun!", "zh": "單字 butterfly、sky 和 high 尾音全部押韻耶！聽起來輕快又有節奏感！", "keywords": ["rhyme", "bouncy"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "Poems are like musical songs made of colorful words. You can draw pictures with your voice.", "zh": "詩就像是用美麗文字做成的歌。你可以用自己的聲音畫出一幅幅美麗的圖畫。", "keywords": ["musical", "pictures", "voice"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Let's write our own two-line poem about spring sunshine before the afternoon bell rings!", "zh": "在下午下課鐘響前，我們也來合寫一首描寫春日暖陽的兩句小童詩吧！", "keywords": ["sunshine", "bell"] }
    ],
    "vocabulary": [
      { "word": "flutter", "phonetic": "/ˈflʌt̬.ɚ/", "pos": "v.", "zh": "拍翅翩翩飛舞、飄動", "example": "Colorful flags fluttered gently in the stadium breeze." },
      { "word": "rhyme", "phonetic": "/raɪm/", "pos": "v./n.", "zh": "押韻；韻文", "example": "The words 'cat', 'hat', and 'mat' rhyme perfectly." },
      { "word": "bouncy", "phonetic": "/ˈbaʊn.si/", "pos": "adj.", "zh": "有彈性的、活潑歡快的", "example": "The children danced cheerfully to the bouncy tempo." }
    ],
    "dailyPhrase": { "en": "Draw pictures with your voice.", "zh": "用聲音勾勒生動畫面。" },
    "cultureTip": "聯合國教科文組織定 3 月 21 日為「世界詩歌日（World Poetry Day）」，鼓勵人們透過語言的音韻與意象，喚醒跨文化的同理心與想像力。"
  },

  # 03-22 [國小中高]
  {
    "id": "dialogue-0322",
    "date": "03-22",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "資源保護",
    "topic": {
      "en": "World Water Day: The Epic Odyssey of a Water Molecule",
      "zh": "世界水資源日：一滴水的大自然循環與校園省水小妙招"
    },
    "situation": "洗手台旁邊，Ben 和 Lily 在水龍頭上張貼「請隨手關緊水龍頭」節水貼紙，探討每一滴水的珍貴身世。",
    "speakers": {
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Lily": { "role": "Lily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0322.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ben", "avatar": "👦", "en": "Lily, someone left this tap dripping! Drip, drip, drip. Let me twist it tight.", "zh": "Lily，有人忘記把水龍頭關緊了！滴答、滴答、滴答。我來把它轉緊。", "keywords": ["dripping", "twist"] },
      { "id": 2, "speaker": "Lily", "avatar": "👧", "en": "Good catch, Ben! Today is World Water Day. A dripping faucet can waste up to twenty liters of clean water daily.", "zh": "太及時了 Ben！今天是世界水資源日。一個滴水的水龍頭一天就能白白浪費高達二十公升乾淨的水呢。", "keywords": ["faucet", "liters", "waste"] },
      { "id": 3, "speaker": "Ben", "avatar": "👦", "en": "Think about a water molecule's epic journey: evaporating into clouds, falling as mountain rain, and flowing into reservoirs.", "zh": "想想一滴水壯麗的旅程：從海洋蒸發化為雲朵、化成山間春雨飄落，再匯流進水庫裡。", "keywords": ["molecule", "evaporating", "reservoirs"] },
      { "id": 4, "speaker": "Lily", "avatar": "👧", "en": "Billions of people across the planet still lack direct access to safe, sanitized drinking water.", "zh": "世界上還有數十億人日常生活依然缺乏安全、經過消毒過濾的乾淨飲用水。", "keywords": ["sanitized", "access"] },
      { "id": 5, "speaker": "Ben", "avatar": "👦", "en": "Turning the tap off while lathering soap takes zero effort, but safeguards our most precious shared treasure.", "zh": "搓肥皂時隨手關上水龍頭完全不費吹灰之力，卻能守護全人類最珍貴的共享寶藏。", "keywords": ["lathering", "safeguards"] }
    ],
    "vocabulary": [
      { "word": "faucet", "phonetic": "/ˈfɑː.sət/", "pos": "n.", "zh": "水龍頭", "example": "Remember to turn off the bathroom faucet after brushing." },
      { "word": "reservoir", "phonetic": "/ˈrez.ɚ.vwɑːr/", "pos": "n.", "zh": "蓄水庫、蓄水池", "example": "Recent heavy downpours filled the mountain reservoir to capacity." },
      { "word": "lather", "phonetic": "/ˈlæð.ɚ/", "pos": "v./n.", "zh": "起泡沫；塗抹肥皂泡沫", "example": "Lather your hands with antibacterial soap for at least twenty seconds." }
    ],
    "dailyPhrase": { "en": "Takes zero effort.", "zh": "毫不費力、輕而易舉。" },
    "cultureTip": "3 月 22 日為聯合國「世界水資源日（World Water Day）」，倡導水資源永續管理，應對全球淡水匱乏危機與保障基本用水人權。"
  },

  # 03-23 [國中挑戰]
  {
    "id": "dialogue-0323",
    "date": "03-23",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "氣象科學",
    "topic": {
      "en": "World Meteorological Day: Reading Stevenson Screens and Barometers",
      "zh": "世界氣象日：認識校園百葉箱、氣壓計與現代氣象衛星"
    },
    "situation": "校園氣象站前，Ethan 和 Chloe 拿著紀錄板，打開白色百葉箱記錄乾濕球溫度計與氣壓計的即時數值。",
    "speakers": {
      "Ethan": { "role": "Ethan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0323.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ethan", "avatar": "👦", "en": "Chloe, look at this white wooden louvered box on four stilts. Today is World Meteorological Day!", "zh": "Chloe，看這座架在四根腳架上的白色百葉木箱。今天是世界氣象日！", "keywords": ["louvered", "Meteorological"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "That's a classic Stevenson screen! Its double-louvered slats shield sensitive thermometers from direct solar radiation while allowing air to circulate freely.", "zh": "那是經典的百葉箱！它的雙層百葉百葉窗板能保護靈敏溫度計免受陽光直射，同時讓空氣自由流通。", "keywords": ["Stevenson", "slats", "circulate"] },
      { "id": 3, "speaker": "Ethan", "avatar": "👦", "en": "Look at the aneroid barometer: 1013 hectopascals, standard sea-level atmospheric pressure. The pointer has been ticking downward.", "zh": "看空盒氣壓計：1013 百帕，標準海平面大氣壓。指針剛才有一點點往下滑動呢。", "keywords": ["aneroid", "barometer", "hectopascals"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "A sudden drop in atmospheric pressure often heralds an incoming cold front or rainstorm system.", "zh": "氣壓如果迅速下降，往往預示著即將有冷鋒或暴雨天氣系統來襲。", "keywords": ["heralds", "atmospheric", "rainstorm"] },
      { "id": 5, "speaker": "Ethan", "avatar": "👦", "en": "From ground Stevenson screens to geostationary weather satellites in orbit, accurate forecasts protect countless human lives and agriculture daily.", "zh": "從地面的百葉箱到軌道上的地球同步氣象衛星，精準的天氣預報每天都在守護無數人的生命與農業安全。", "keywords": ["geostationary", "satellites", "forecasts"] }
    ],
    "vocabulary": [
      { "word": "circulate", "phonetic": "/ˈsɝː.kjə.leɪt/", "pos": "v.", "zh": "循環、流動", "example": "Open cross-windows to allow fresh air to circulate inside." },
      { "word": "barometer", "phonetic": "/bəˈrɑː.mə.t̬ɚ/", "pos": "n.", "zh": "氣壓計；晴雨表、指標", "example": "Consumer confidence is often regarded as a reliable economic barometer." },
      { "word": "herald", "phonetic": "/ˈher.əld/", "pos": "v./n.", "zh": "預告、預示…的來臨", "example": "Blooming daffodils herald the arrival of early spring." }
    ],
    "dailyPhrase": { "en": "Herald the arrival of.", "zh": "預示…的到來。" },
    "cultureTip": "3 月 23 日為「世界氣象日（World Meteorological Day）」，紀念 1950 年世界氣象組織（WMO）成立公約生效，強調早期預警系統（Early Warning）對極端氣候防減災的重要性。"
  },

  # 03-24 [高中進階]
  {
    "id": "dialogue-0324",
    "date": "03-24",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "生物醫學史",
    "topic": {
      "en": "World Tuberculosis Day: Robert Koch's Discovery and Modern Public Health",
      "zh": "世界結核病日：柯霍發現結核桿菌與現代公共衛生防疫體系"
    },
    "situation": "生物醫學社專題發表會上，Eric 和 Natalie 報告 1882 年羅伯特·柯霍在柏林宣布發現結核分枝桿菌的劃時代歷史，探討當代抗生素抗藥性挑戰。",
    "speakers": {
      "Eric": { "role": "Eric", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Natalie": { "role": "Natalie", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0324.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Eric", "avatar": "👨‍🎓", "en": "Natalie, on this day in 1882, Dr. Robert Koch stood before the Berlin Physiological Society and announced a monumental breakthrough.", "zh": "Natalie，在 1882 年的今天，羅伯特·柯霍醫師站在柏林生理學會前，宣布了一項劃時代的重大醫學突破。", "keywords": ["Physiological", "monumental", "breakthrough"] },
      { "id": 2, "speaker": "Natalie", "avatar": "👩‍🎓", "en": "He successfully isolated Mycobacterium tuberculosis, definitively proving that the terrifying 'White Plague' was caused by a bacterial pathogen, not hereditary weakness.", "zh": "他成功分離出結核分枝桿菌，無可辯駁地證實了奪命無數的『白色瘟疫』是由細菌病原體引起，而非遺傳體弱。", "keywords": ["pathogen", "hereditary", "isolated"] },
      { "id": 3, "speaker": "Eric", "avatar": "👨‍🎓", "en": "Before that discovery, tuberculosis killed one in every seven people in Europe and North America, casting a dreadful shadow over entire generations.", "zh": "在那項發現之前，結核病奪走了歐洲和北美每七個人中一人的生命，在整個世代頭上籠罩著恐怖陰影。", "keywords": ["dreadful", "tuberculosis"] },
      { "id": 4, "speaker": "Natalie", "avatar": "👩‍🎓", "en": "Yet today, despite effective antibiotics, tuberculosis remains a formidable global killer, exacerbated by multi-drug-resistant strains and socio-economic inequality.", "zh": "然而即使在今天擁有抗生素的時代，結核病依舊是強大的全球健康殺手，並因多重抗藥性菌株與社會經濟不平等而雪上加霜。", "keywords": ["formidable", "exacerbated", "multi-drug-resistant"] },
      { "id": 5, "speaker": "Eric", "avatar": "👨‍🎓", "en": "Observing World Tuberculosis Day highlights that public health surveillance, accessible healthcare, and rigorous scientific research are perpetual imperatives.", "zh": "紀念世界結核病日彰顯出：公共衛生監測、普及醫療照顧與嚴謹科學研究是人類永不懈怠的必行使命。", "keywords": ["surveillance", "imperatives", "perpetual"] }
    ],
    "vocabulary": [
      { "word": "pathogen", "phonetic": "/ˈpæθ.ə.dʒən/", "pos": "n.", "zh": "病原體、致病微生物", "example": "Vaccines help our immune system recognize dangerous foreign pathogens." },
      { "word": "exacerbate", "phonetic": "/ɪɡˈzæs.ɚ.beɪt/", "pos": "v.", "zh": "使加劇、使惡化", "example": "Severe air pollution exacerbated his chronic asthma symptoms." },
      { "word": "imperative", "phonetic": "/ɪmˈper.ə.t̬ɪv/", "pos": "n./adj.", "zh": "迫切必要之事；緊迫的", "example": "Ensuring clean drinking water is an absolute humanitarian imperative." }
    ],
    "dailyPhrase": { "en": "A monumental breakthrough.", "zh": "里程碑式的劃時代重大突破。" },
    "cultureTip": "3 月 24 日為「世界結核病日（World TB Day）」，紀念 1882 年德國微生物學家柯霍（Robert Koch）發現結核桿菌，他因此榮獲 1905 年諾貝爾生理學或醫學獎。"
  },

  # 03-25 [國小初階]
  {
    "id": "dialogue-0325",
    "date": "03-25",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "戶外童趣",
    "topic": {
      "en": "Flying a Colorful Diamond Kite at the Riverside Park",
      "zh": "到河濱公園迎風奔跑放飛五彩菱形大風箏"
    },
    "situation": "週六下午微風吹拂，Toby 和 Zoe 帶著一隻長著長長彩帶尾巴的紅色菱形風箏，在河濱公園大草坪上奔跑。",
    "speakers": {
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0325.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Toby", "avatar": "👦", "en": "Zoe, hold the kite up high above your head! Wait until you feel the wind gust against your face!", "zh": "Zoe，把風箏高高舉過頭頂！等感覺到陣風迎面吹拂時再鬆手！", "keywords": ["kite", "gust"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "I feel the breeze picking up now! Ready, steady, go! Run, Toby, run!", "zh": "我感覺到風變強了！預備，穩住，跑！快跑，Toby，快跑！", "keywords": ["steady", "picking up"] },
      { "id": 3, "speaker": "Toby", "avatar": "👦", "en": "I am unspooling the white nylon string! Look, it catches the lift and soars!", "zh": "我正在放開白色尼龍線輪！看，它乘著上升氣流高高升空了！", "keywords": ["unspooling", "lift", "soars"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Its long rainbow ribbons are dancing gracefully like a dragon in the blue sky!", "zh": "它長長的彩虹飄帶在藍天裡優雅舞動，像一條游動的小神龍一樣！", "keywords": ["ribbons", "gracefully"] },
      { "id": 5, "speaker": "Toby", "avatar": "👦", "en": "Tug gently on the spool to keep tension. Flying kites in March is pure magic!", "zh": "輕輕收放線輪保持拉力。三月在春風裡放風箏真是最棒的魔法！", "keywords": ["tension", "spool"] }
    ],
    "vocabulary": [
      { "word": "gust", "phonetic": "/ɡʌst/", "pos": "n.", "zh": "一陣強風、陣風", "example": "A sudden gust of wind blew my hat right off." },
      { "word": "soar", "phonetic": "/sɔːr/", "pos": "v.", "zh": "高飛、凌空翱翔", "example": "The bald eagle soared effortlessly above the canyon." },
      { "word": "tension", "phonetic": "/ˈten.ʃən/", "pos": "n.", "zh": "張力、拉力；緊張", "example": "Maintain proper string tension so the kite remains stable." }
    ],
    "dailyPhrase": { "en": "Picking up.", "zh": "風力增強、漸入佳境。" },
    "cultureTip": "春季放風箏（Kite Flying）已有兩千多年歷史。古人有「放風箏放走晦氣」的民俗寄託，也是春季親近大自然、鍛鍊頸部肌肉舒緩用眼疲勞的絕佳運動。"
  },

  # 03-26 [國小中高]
  {
    "id": "dialogue-0326",
    "date": "03-26",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "生活技能",
    "topic": {
      "en": "Baking Golden Cranberry Scones in Home Economics",
      "zh": "家政料理課：動手揉麵團烘烤金黃酸甜蔓越莓司康"
    },
    "situation": "家政教室烤箱飄出陣陣奶油香氣，Max 和 Ruby 戴著隔熱手套，正在將剛出爐的蔓越莓司康端上冷卻架。",
    "speakers": {
      "Max": { "role": "Max", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Ruby": { "role": "Ruby", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0326.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Max", "avatar": "👦", "en": "Ruby, ding! The oven timer just sounded! Put on your heat-resistant mittens.", "zh": "Ruby，叮！烤箱定時器剛響了！快戴上你的防燙隔熱手套。", "keywords": ["timer", "mittens", "heat-resistant"] },
      { "id": 2, "speaker": "Ruby", "avatar": "👧", "en": "Opening the oven door... Oh, my goodness! What an intoxicating aroma of melted butter and toasted flour!", "zh": "打開烤箱門囉…我的天啊！融化奶油和烤麵粉散發出的香氣太誘人了！", "keywords": ["intoxicating", "aroma", "melted"] },
      { "id": 3, "speaker": "Max", "avatar": "👦", "en": "Look at the crumbly texture and those glorious cracks along the sides—the hallmark of a perfect scone!", "zh": "看這酥鬆的層次和側面漂亮的裂紋——這正是完美司康的正字標記！", "keywords": ["crumbly", "hallmark", "texture"] },
      { "id": 4, "speaker": "Ruby", "avatar": "👧", "en": "The secret was rubbing the cold cubed butter into the flour with our fingertips without over-kneading the dough.", "zh": "秘訣就在於用指尖把冰涼奶油丁搓進麵粉裡，而且絕對不能過度搓揉出筋。", "keywords": ["fingertips", "kneading", "cubed"] },
      { "id": 5, "speaker": "Max", "avatar": "👦", "en": "Studded with ruby-red tart cranberries, these will pair heavenly with warm honey milk!", "zh": "點綴著紅寶石般酸甜的蔓越莓乾，配上一杯熱蜂蜜牛奶簡直是人間美味！", "keywords": ["cranberries", "studded", "heavenly"] }
    ],
    "vocabulary": [
      { "word": "aroma", "phonetic": "/əˈroʊ.mə/", "pos": "n.", "zh": "香氣、濃郁芳香", "example": "The rich aroma of freshly ground coffee filled the bakery." },
      { "word": "crumbly", "phonetic": "/ˈkrʌm.bli/", "pos": "adj.", "zh": "酥脆易碎的、鬆軟可口的", "example": "The homemade shortbread cookie had a wonderfully crumbly crust." },
      { "word": "knead", "phonetic": "/niːd/", "pos": "v.", "zh": "揉捏（麵團）、揉壓", "example": "Knead the bread dough vigorously for ten full minutes." }
    ],
    "dailyPhrase": { "en": "The hallmark of.", "zh": "…的標誌、典型特徵。" },
    "cultureTip": "司康（Scone）是英式下午茶（Afternoon Tea）的靈魂糕點，正統吃法是趁熱橫向掰開，抹上濃縮奶油（Clotted Cream）與草莓或蔓越莓果醬。"
  },

  # 03-27 [國中挑戰]
  {
    "id": "dialogue-0327",
    "date": "03-27",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "校外參訪",
    "topic": {
      "en": "Field Trip to the Natural Science Museum: The Dinosaur Pavilion",
      "zh": "校外教學參訪：在自然科學博物館仰望暴龍骨骼化石"
    },
    "situation": "國中春季校外教學來到自然科學博物館古生物大廳，Jason 和 Emily 站在巨大暴龍骨架下拿著學習單做筆記。",
    "speakers": {
      "Jason": { "role": "Jason", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emily": { "role": "Emily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0327.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Jason", "avatar": "👦", "en": "Emily, look up! Standing beneath this reconstructed Tyrannosaurus rex skeleton gives me literal goosebumps!", "zh": "Emily，抬頭看！站在這具復原的雷克斯暴龍全身骨骼化石底下，真的讓我渾身起雞皮疙瘩！", "keywords": ["Tyrannosaurus", "goosebumps", "skeleton"] },
      { "id": 2, "speaker": "Emily", "avatar": "👧", "en": "Its massive skull alone is over one point five meters long, equipped with serrated, banana-sized teeth designed to crush bone.", "zh": "光是那顆巨大的頭骨就長達一點五公尺，長著鋸齒狀、香蕉大小專門粉碎骨骼的恐怖利齒。", "keywords": ["skull", "serrated", "crush"] },
      { "id": 3, "speaker": "Jason", "avatar": "👦", "en": "Check question four on our museum inquiry worksheet: 'What modern living creatures are the closest evolutionary relatives of theropod dinosaurs?'", "zh": "看一下我們博物館探究學習單的第四題：『現代哪種生物是獸腳類恐龍最親近的演化親戚？』", "keywords": ["worksheet", "evolutionary", "theropod"] },
      { "id": 4, "speaker": "Emily", "avatar": "👧", "en": "Birds! Paleontological discoveries of feathered fossils demonstrate that avian dinosaurs survived the Cretaceous extinction and fly around us every day.", "zh": "鳥類！古生物學對帶羽毛恐龍化石的重大發現證明：鳥類恐龍躲過了白堊紀滅絕，而且每天都在我們身邊飛翔呢。", "keywords": ["Paleontological", "avian", "extinction"] },
      { "id": 5, "speaker": "Jason", "avatar": "👦", "en": "Mind blown! So the tiny sparrows and pigeons chirping outside the museum are technically miniature raptors in disguised feathers!", "zh": "太震撼了！所以博物館外啾啾叫的麻雀和鴿子，本質上就是披著羽毛偽裝的縮小版迅猛龍啊！", "keywords": ["sparrows", "raptors", "disguised"] }
    ],
    "vocabulary": [
      { "word": "serrated", "phonetic": "/səˈreɪ.t̬ɪd/", "pos": "adj.", "zh": "鋸齒狀的", "example": "Use a knife with a sharp serrated blade to slice bread." },
      { "word": "paleontology", "phonetic": "/ˌpeɪ.li.ɑːnˈtɑː.lə.dʒi/", "pos": "n.", "zh": "古生物學", "example": "Advances in paleontology shed new light on prehistoric ecosystems." },
      { "word": "avian", "phonetic": "/ˈeɪ.vi.ən/", "pos": "adj.", "zh": "鳥類的、禽類的", "example": "Avian species possess lightweight hollow bones that facilitate flight." }
    ],
    "dailyPhrase": { "en": "Mind blown!", "zh": "太震撼了！大開眼界！令人驚嘆！" },
    "cultureTip": "現代古生物學界公認鳥類即是「現存的獸腳類恐龍（Living Theropod Dinosaurs）」。始祖鳥化石與中國遼寧帶羽毛恐龍化石徹底重寫了生物演化史課本。"
  },

  # 03-28 [高中進階]
  {
    "id": "dialogue-0328",
    "date": "03-28",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "全球永續",
    "topic": {
      "en": "Earth Hour: Turning Off Lights to Spark Climate Mindfulness",
      "zh": "「地球一小時」熄燈行動：象徵性黑暗如何喚醒全人類氣候意識？"
    },
    "situation": "三月最後一個週六晚間八點半，青年志工 Ryan 和 Olivia 點燃安全大豆香氛蠟燭，在天台上觀看整座城市地標建築熄燈。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0328.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "Olivia, it's eight thirty! Look down at the city skyline—the towering skyscrapers and neon billboards are plunging into darkness simultaneously.", "zh": "Olivia，八點半到了！俯瞰城市天際線——摩天大樓和霓虹看板正在同一瞬間熄滅陷入黑暗。", "keywords": ["skyscrapers", "neon", "simultaneously"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👩‍🎓", "en": "Earth Hour in action. Cynics often dismiss turning off lights for sixty minutes as toothless virtue signaling that saves negligible kilowatt-hours.", "zh": "這就是『地球一小時』的震撼現場。冷眼懷疑者常批評熄燈六十分鐘是不痛不癢的道德作秀，省不了幾度電。", "keywords": ["cynics", "virtue signaling", "negligible"] },
      { "id": 3, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "They miss the psychological power of coordinated ritual. A single light switch off accomplishes little; millions acting in unison creates a potent global statement.", "zh": "他們忽視了集體儀式感帶來的心理震撼。單獨一盞燈熄滅或許微不足道；但全球數億人同心協力行動，就凝聚成震撼全球的宣示。", "keywords": ["coordinated", "ritual", "unison", "potent"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👩‍🎓", "en": "It shifts our sensory relationship with nighttime. Standing beneath the newly visible starry sky forces us to confront our unsustainable energy dependency.", "zh": "它改變了我們與夜色之間的感官連結。重新看見頭頂閃爍的繁星，迫使我們直面不可持續的能源依賴現實。", "keywords": ["sensory", "unsustainable", "dependency"] },
      { "id": 5, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "The goal isn't just saving electricity for one hour tonight, but inspiring systemic policy reform and conscious consumption for all the hours to come.", "zh": "其終極目標絕非僅限於今晚這短短一小時的省電，而是啟發制度性的政策改革，並在往後每一天落實清醒的正念消費。", "keywords": ["systemic", "reform", "consumption"] }
    ],
    "vocabulary": [
      { "word": "cynic", "phonetic": "/ˈsɪn.ɪk/", "pos": "n.", "zh": "憤世嫉俗者、悲觀懷疑者", "example": "Cynics doubted that ordinary citizens could influence climate policy." },
      { "word": "negligible", "phonetic": "/ˈneɡ.lə.dʒə.bəl/", "pos": "adj.", "zh": "微不足道的、可以忽略不計的", "example": "The slight price difference was completely negligible." },
      { "word": "unison", "phonetic": "/ˈjuː.nə.sən/", "pos": "n.", "zh": "齊聲、一致行動", "example": "The audience cheered in unison as the athletes entered the stadium." }
    ],
    "dailyPhrase": { "en": "In unison.", "zh": "齊聲同調、步調一致地。" },
    "cultureTip": "由世界自然基金會（WWF）發起的「地球一小時（Earth Hour）」於每年 3 月最後一個週六晚間 8:30 舉行，包括艾菲爾鐵塔、雪梨歌劇院等全球地標均熄燈一小時。"
  },

  # 03-29 [國小初階]
  {
    "id": "dialogue-0329",
    "date": "03-29",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "生活實踐",
    "topic": {
      "en": "Planting Fresh Herbs on the Balcony: Mint and Sweet Basil",
      "zh": "在陽台盆栽種植清新薄荷與九層塔羅勒"
    },
    "situation": "週日午後，Leo 和 Mia 在陽台花架上，用小鏟子把薄荷和羅勒幼苗移栽到彩繪陶瓷花盆裡。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0329.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Mia, rub this green leaf gently between your fingers, then take a sniff!", "zh": "Mia，用你的手指輕輕揉一揉這片綠葉子，然後聞聞看！", "keywords": ["sniff", "rub"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "Wow, so refreshing and cool! It smells just like peppermint toothpaste and ice cream!", "zh": "哇，好清新好涼爽喔！聞起來跟薄荷牙膏和冰淇淋一模一樣耶！", "keywords": ["refreshing", "peppermint"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "That's spearmint! And this other leafy plant with smooth curved leaves is sweet Italian basil.", "zh": "那是留蘭香薄荷！而旁邊這盆長著平滑圓弧葉片的是義大利甜羅勒。", "keywords": ["spearmint", "basil"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "Mom said we can pick fresh basil leaves to put on our homemade Margherita pizza tonight!", "zh": "媽媽說我們今晚就可以摘幾片新鮮羅勒葉，放在自製的瑪格麗特披薩上烤！", "keywords": ["homemade", "pizza"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "I'll spritz them with fresh water every morning. Having our own mini balcony garden is super fun!", "zh": "我每天早晨都會給它們噴灑乾淨清水。擁有我們自己的陽台小菜園真是太好玩了！", "keywords": ["spritz", "balcony"] }
    ],
    "vocabulary": [
      { "word": "refreshing", "phonetic": "/rɪˈfreʃ.ɪŋ/", "pos": "adj.", "zh": "令人神清氣爽的、清涼的", "example": "A cold glass of lemonade is wonderfully refreshing on hot afternoons." },
      { "word": "basil", "phonetic": "/ˈbeɪ.zəl/", "pos": "n.", "zh": "羅勒、九層塔", "example": "Crush fresh basil leaves with garlic and olive oil to make pesto." },
      { "word": "sniff", "phonetic": "/snɪf/", "pos": "v./n.", "zh": "聞、吸氣聞", "example": "The curious dog sniffed around the front porch." }
    ],
    "dailyPhrase": { "en": "Take a sniff.", "zh": "聞一聞、嗅一下。" },
    "cultureTip": "香草植物（Herbs）如薄荷（Mint）與羅勒（Basil）極易成活，非常適合家庭陽台與教室窗台盆栽，能提供孩子觸覺、嗅覺與味覺的全方位自然啟蒙。"
  },

  # 03-30 [國小中高]
  {
    "id": "dialogue-0330",
    "date": "03-30",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "社會關懷",
    "topic": {
      "en": "Youth Day: Volunteering at the Senior Community Center",
      "zh": "青年節愛心行動：到社區長者日照中心擔任志工講故事"
    },
    "situation": "青年節週末，Sam 和 Kevin 帶著自製的大字體繪本與烏克麗麗，到社區樂齡長者日照中心陪伴爺爺奶奶度過溫馨午後。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Kevin": { "role": "Kevin", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0330.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Kevin, tuning your ukulele? The seniors are gathering in the recreation hall right now.", "zh": "Kevin，烏克麗麗調好音了嗎？爺爺奶奶們現在都聚集在交誼大廳裡囉。", "keywords": ["tuning", "ukulele", "recreation"] },
      { "id": 2, "speaker": "Kevin", "avatar": "👦", "en": "All tuned! Today is Youth Day weekend. Being a responsible young citizen means giving back with warm empathy.", "zh": "全部調好了！今天是青年節週末。作為有責任感的年輕公民，用溫暖的同理心回饋社區就是最棒的實踐。", "keywords": ["citizen", "empathy", "Youth Day"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Grandpa Chen smiled so brightly when I handed him our hand-drawn picture album of local neighborhood landmarks.", "zh": "當我把手繪的社區地標回憶畫冊遞給陳爺爺時，他臉上的笑容好燦爛好溫暖。", "keywords": ["landmarks", "hand-drawn"] },
      { "id": 4, "speaker": "Kevin", "avatar": "👦", "en": "Listening attentively to their youth stories taught me far more than any history textbook ever could.", "zh": "專注傾聽他們年輕時的奮鬥故事，讓我學到了比任何歷史課本更深刻豐富的人生智慧。", "keywords": ["attentively", "textbook"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Let's strum 'You Are My Sunshine' together! Bridging generational gaps with music and laughter feels amazing.", "zh": "讓我們一起彈唱《You Are My Sunshine》吧！用音樂與歡笑搭起世代溝通的橋樑感覺真是太棒了。", "keywords": ["strum", "generational", "laughter"] }
    ],
    "vocabulary": [
      { "word": "empathy", "phonetic": "/ˈem.pə.θi/", "pos": "n.", "zh": "同理心、共情能力", "example": "Practicing empathy helps us understand different viewpoints." },
      { "word": "attentively", "phonetic": "/əˈten.t̬ɪv.li/", "pos": "adv.", "zh": "專心致志地、聚精會神地", "example": "The attentive students listened attentively to the instructions." },
      { "word": "strum", "phonetic": "/strʌm/", "pos": "v.", "zh": "輕彈、漫彈（弦樂器）", "example": "He strummed soft chords on his acoustic guitar around the campfire." }
    ],
    "dailyPhrase": { "en": "Bridge generational gaps.", "zh": "跨越世代隔閡、促進老少代際融合。" },
    "cultureTip": "青年節（Youth Day）提倡青年積極承擔公民責任、投身志工服務（Volunteering）。代際共融（Intergenerational Solidarity）能讓長者感到被重視，並讓青年汲取人生智慧。"
  },

  # 03-31 [國中挑戰]
  {
    "id": "dialogue-0331",
    "date": "03-31",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "春季月結",
    "topic": {
      "en": "March Wrap-Up: Embracing the Gentle Showers of April",
      "zh": "三月月結：春暖花開繁花似錦，欣然迎接四月清風"
    },
    "situation": "三月最後一天的放學路上，夕陽灑滿林蔭大道，Alex 和 Maya 回顧這個月滿滿的學習收穫與對即將到來的四月的期待。",
    "speakers": {
      "Alex": { "role": "Alex", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Maya": { "role": "Maya", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0331.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Alex", "avatar": "👦", "en": "Maya, take a look at our calendar! March thirty-first has arrived. Another glorious month has turned its final page.", "zh": "Maya，看一下我們的月曆！三月三十一日到了。又一個光彩照人的月份即將翻過最後一頁。", "keywords": ["calendar", "glorious"] },
      { "id": 2, "speaker": "Maya", "avatar": "👧", "en": "What a transformative month: from early spring buds and Pi Day pies to observing the equinox and volunteering!", "zh": "多麼收穫滿滿的一個月：從早春的嫩芽與圓周率日蘋果派，到觀測春分日影與志工服務！", "keywords": ["transformative", "equinox", "volunteering"] },
      { "id": 3, "speaker": "Alex", "avatar": "👦", "en": "Azaleas across the school walkway are blooming in spectacular pink, purple, and snowy white fireworks.", "zh": "校園步道兩旁的杜鵑花正以盛大的粉紅、紫紅與雪白煙火般的姿態爭相怒放。", "keywords": ["azaleas", "spectacular", "fireworks"] },
      { "id": 4, "speaker": "Maya", "avatar": "👧", "en": "An old proverb wisely notes: 'March winds and April showers bring forth May flowers.'", "zh": "一句古老的英語諺語說得好：『三月的風與四月的雨，催生出五月繁花似錦。』", "keywords": ["showers", "proverb", "flowers"] },
      { "id": 5, "speaker": "Alex", "avatar": "👦", "en": "Tomorrow brings April, Children's Day, and spring festivals. Let's step forward with curiosity, kindness, and boundless joy!", "zh": "明天就邁入四月、兒童節與春日慶典了。讓我們帶著好奇心、善良與無窮歡喜大步向前走！", "keywords": ["curiosity", "kindness", "boundless"] }
    ],
    "vocabulary": [
      { "word": "transformative", "phonetic": "/trænsˈfɔːr.mə.t̬ɪv/", "pos": "adj.", "zh": "帶來深刻改變的、富於啟發轉變的", "example": "Studying abroad was a truly transformative experience for her." },
      { "word": "spectacular", "phonetic": "/spekˈtæk.jə.lɚ/", "pos": "adj.", "zh": "壯觀引人注目的、驚豔的", "example": "The fireworks display over the harbor was spectacular." },
      { "word": "boundless", "phonetic": "/ˈbaʊnd.ləs/", "pos": "adj.", "zh": "無限的、無窮無盡的", "example": "Her boundless enthusiasm energized the entire volunteer team." }
    ],
    "dailyPhrase": { "en": "April showers bring May flowers.", "zh": "四月春雨換來五月繁花（苦盡甘來、辛勤付出終有收穫）。" },
    "cultureTip": "源自 16 世紀英國的諺語「March winds and April showers bring forth May flowers」，提醒人們忍受三月的大風與四月的連綿陰雨，因為那是為了五月百花齊放所必需的自然孕育。"
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
    for new_item in MARCH_DIALOGUES:
        if new_item['date'] not in existing_dates:
            existing.append(new_item)
            existing_dates.add(new_item['date'])
            added_count += 1

    # 按照 MM-DD 排序（01-01 ~ 03-31, 09-01 ~ 12-31）
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

    print(f"成功新增 3 月份共 {added_count} 篇對話！目前資料庫總計共有 {len(existing)} 篇對話 (涵蓋 1月、2月、3月、9月、10月、11月、12月共 212 天，已突破全年度 58%！)。")

if __name__ == '__main__':
    main()

