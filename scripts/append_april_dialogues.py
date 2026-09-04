#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次建立 4 月份生活對話 (04-01 至 04-30，共 30 篇)
涵蓋愚人節幽默、清明節連假與潤餅傳統、兒童節、世界衛生日、期中考前複習與心理調適、
穀雨節氣、世界地球日綠色生活、世界閱讀日、螢火蟲季、初夏前瞻等豐富主題！
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'dialogues.json')
JS_FILE = os.path.join(BASE_DIR, 'js', 'data.js')

APRIL_DIALOGUES = [
  # 04-01 [國小中高]
  {
    "id": "dialogue-0401",
    "date": "04-01",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "趣味節日",
    "topic": {
      "en": "April Fools' Day: Harmless Pranks & Chuckles",
      "zh": "愚人節的幽默：無傷大雅的玩笑與歡笑"
    },
    "situation": "4月1日愚人節早晨，Kevin 神秘兮兮地指著 Emma 的球鞋，Emma 識破了這個經典小惡作劇。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0401.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "👦", "en": "Emma, look down quickly! There is a neon green frog resting right on your shoe!", "zh": "Emma，快往下看！有一隻螢光綠的青蛙正好停在你的球鞋上！", "keywords": ["neon", "frog", "shoe"] },
      { "id": 2, "speaker": "Emma", "avatar": "👧", "en": "Nice try, Kevin, but you cannot fool me today. It is April first!", "zh": "想得美，Kevin，但你今天騙不到我。今天可是四月一號！", "keywords": ["fool", "April"] },
      { "id": 3, "speaker": "Kevin", "avatar": "👦", "en": "Aww, you got me! April Fools' Day is always full of playful tricks.", "zh": "哎呀，被你識破了！愚人節總是充滿了好玩的鬼點子與惡作劇。", "keywords": ["playful", "tricks"] },
      { "id": 4, "speaker": "Emma", "avatar": "👧", "en": "I love harmless jokes as long as nobody gets scared or hurt.", "zh": "只要沒有人受驚嚇或受傷，我也很喜歡這種無傷大雅的玩笑。", "keywords": ["harmless", "scared", "hurt"] },
      { "id": 5, "speaker": "Kevin", "avatar": "👦", "en": "Agreed! Let's see if our science teacher brings a funny riddle to class today.", "zh": "沒錯！我們來看看自然老師今天會不會在課堂上帶有趣的謎題來考大家。", "keywords": ["science", "riddle"] }
    ],
    "vocabulary": [
      { "word": "prank", "phonetic": "/præŋk/", "pos": "n.", "zh": "惡作劇、玩笑", "example": "He played a harmless prank on his roommate." },
      { "word": "harmless", "phonetic": "/ˈhɑːrm.ləs/", "pos": "adj.", "zh": "無害的、無傷大雅的", "example": "It was just a harmless little joke to cheer everyone up." },
      { "word": "riddle", "phonetic": "/ˈrɪd.əl/", "pos": "n.", "zh": "謎語、難題", "example": "Can you solve this tricky riddle?" }
    ],
    "dailyPhrase": { "en": "Nice try!", "zh": "想得美！/ 差點就上當了！（表示看穿別人的嘗試或玩笑）" },
    "cultureTip": "在西方文化中，愚人節（April Fools' Day）有著數百年傳統，大家會互相開善意且無害的玩笑（harmless pranks），揭穿時會大喊一聲「April Fools!」。"
  },

  # 04-02 [國小初階]
  {
    "id": "dialogue-0402",
    "date": "04-02",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "春日穿搭",
    "topic": {
      "en": "Spring Breezes & Light Cardigans",
      "zh": "春風吹拂：穿上舒適透氣的薄開衫"
    },
    "situation": "四月初早晚氣溫仍有微涼，Lucas 和 Mia 正在校門口討論今天合適的春季穿著。",
    "speakers": {
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0402.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lucas", "avatar": "👦", "en": "Good morning, Mia! I see you are wearing a cozy knit cardigan today.", "zh": "早安，Mia！我看到你今天穿了一件舒服的針織開衫外套呢。", "keywords": ["cardigan", "cozy", "knit"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "Yes, spring mornings can still be breezy, even when the afternoon turns quite warm.", "zh": "是呀，春天早晨還是挺涼風陣陣的，即使午後會變得很溫暖。", "keywords": ["breezy", "afternoon", "warm"] },
      { "id": 3, "speaker": "Lucas", "avatar": "👦", "en": "That is so true! Layering your clothes makes it easy to stay comfortable.", "zh": "確實如此！洋蔥式多層次穿搭能讓人整天都保持舒服自在。", "keywords": ["layering", "comfortable"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "I can take off this cardigan when we run outside during recess.", "zh": "下課我們去操場跑步時，我就可以把這件開衫脫下來放椅子上。", "keywords": ["recess", "run", "outside"] },
      { "id": 5, "speaker": "Lucas", "avatar": "👦", "en": "Smart choice! Let's head inside before the morning bell rings.", "zh": "聰明的選擇！趁早自習鐘聲響起前我們趕快進教室吧。", "keywords": ["smart", "bell", "rings"] }
    ],
    "vocabulary": [
      { "word": "cardigan", "phonetic": "/ˈkɑːr.dɪ.ɡən/", "pos": "n.", "zh": "開襟羊毛衫、針織開衫", "example": "She buttoned up her blue cardigan against the chill." },
      { "word": "layering", "phonetic": "/ˈleɪ.ɚ.ɪŋ/", "pos": "n.", "zh": "多層穿搭、分層", "example": "Layering is essential when traveling in variable weather." },
      { "word": "recess", "phonetic": "/ˈriː.ses/", "pos": "n.", "zh": "課間休息、下課時間", "example": "The children bolted toward the swings during recess." }
    ],
    "dailyPhrase": { "en": "Smart choice!", "zh": "聰明的選擇！/ 明智之舉！" },
    "cultureTip": "春天的天氣常被形容為「unpredictable（難以預測）」，多層次穿法（layering）是歐美和台灣春天最推薦的實用穿著策略。"
  },

  # 04-03 [國中挑戰]
  {
    "id": "dialogue-0403",
    "date": "04-03",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "節慶家庭",
    "topic": {
      "en": "Planning the Tomb Sweeping Break: Family Gatherings & Travel",
      "zh": "清明連假規劃：返鄉祭祖與家族溫馨聚會"
    },
    "situation": "清明連假即將展開，David 和 Chloe 在午休時間交流各自家庭假期的安排與傳統。",
    "speakers": {
      "David": { "role": "David", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0403.mp3",
    "dialogue": [
      { "id": 1, "speaker": "David", "avatar": "👦", "en": "The four-day long weekend starts tomorrow! What are your family's plans, Chloe?", "zh": "四天連續假期明天就要開始了！Chloe，你們家有什麼安排嗎？", "keywords": ["four-day", "weekend", "plans"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "We are driving down to Changhua early in the morning to beat the highway traffic and visit our ancestral shrine.", "zh": "我們一早要開車南下彰化避開國道車潮，並前往祖先宗祠與墓園祭拜。", "keywords": ["highway", "traffic", "ancestral", "shrine"] },
      { "id": 3, "speaker": "David", "avatar": "👦", "en": "Leaving early is wise. We are taking the High-Speed Rail to Tainan to visit my grandparents.", "zh": "提早出發很明智。我們則打算搭高鐵回台南看爺爺奶奶。", "keywords": ["wise", "High-Speed Rail", "grandparents"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "My grandmother always prepares huge platters of fillings for rolling fresh runbing wraps.", "zh": "我奶奶每次都會準備好幾大盤餡料，讓全家族一起包新鮮現捲的潤餅。", "keywords": ["platters", "fillings", "runbing", "wraps"] },
      { "id": 5, "speaker": "David", "avatar": "👦", "en": "That sounds delicious! The peanut powder and savory pork slices are the ultimate combination.", "zh": "聽起來太好吃了！香濃的花生粉配上鹹香的豬肉絲簡直是絕配。", "keywords": ["peanut powder", "savory", "combination"] },
      { "id": 6, "speaker": "Chloe", "avatar": "👧", "en": "Definitely! It is wonderful having quality time with extended family across generations.", "zh": "真的！能和跨世代的親戚大家庭相聚共度美好時光，感覺格外溫馨。", "keywords": ["extended family", "generations"] }
    ],
    "vocabulary": [
      { "word": "ancestral", "phonetic": "/ænˈses.trəl/", "pos": "adj.", "zh": "祖先的、世代相傳的", "example": "They visited their ancestral hometown in the countryside." },
      { "word": "savory", "phonetic": "/ˈseɪ.vɚ.i/", "pos": "adj.", "zh": "鹹香的、可口的", "example": "The bakery serves both sweet pastries and savory pies." },
      { "word": "extended family", "phonetic": "/ɪkˌsten.dɪd ˈfæm.əl.i/", "pos": "n.", "zh": "大家庭（包括祖父母、姑叔等）", "example": "During festivals, our extended family always gathers for dinner." }
    ],
    "dailyPhrase": { "en": "Beat the traffic.", "zh": "避開車潮、搶先出發避開堵車。" },
    "cultureTip": "清明節（Tomb Sweeping Day）是華人世界慎終追遠的重要傳統，常合併兒童節形成春季連假，許多家庭會闔家返鄉掃墓並包潤餅（Runbing / Spring roll）共享天倫。"
  },

  # 04-04 [國小初階]
  {
    "id": "dialogue-0404",
    "date": "04-04",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "快樂童年",
    "topic": {
      "en": "Children's Day Joy: Outdoor Kite Flying and Bubbles",
      "zh": "兒童節快樂：綠茵草地放風箏與七彩泡泡"
    },
    "situation": "4月4日兒童節，Leo 和 Sophie 在河濱公園的大草皮上奔跑放風箏，享受專屬於兒童的快樂假期。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Sophie": { "role": "Sophie", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0404.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Happy Children's Day, Sophie! Look at my giant eagle kite soaring in the sky!", "zh": "兒童節快樂，Sophie！你看我的老鷹大風箏在藍天上翱翔！", "keywords": ["Children's Day", "eagle", "kite", "soaring"] },
      { "id": 2, "speaker": "Sophie", "avatar": "👧", "en": "Wow, it is flying so high! Watch out for the big willow tree over there.", "zh": "哇，它飛得好高呀！小心那邊那棵大柳樹喔。", "keywords": ["high", "willow tree"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Don't worry, the wind is steady. What kind of bubble wand do you have?", "zh": "別擔心，現在風向很穩定。你帶了什麼樣的泡泡棒？", "keywords": ["steady", "bubble wand"] },
      { "id": 4, "speaker": "Sophie", "avatar": "👧", "en": "It is a rainbow wand! When I swing it, hundreds of shiny bubbles dance in the air.", "zh": "這是一根彩虹泡泡棒！當我一揮動，數百個閃閃發光的泡泡就在空中起舞。", "keywords": ["rainbow", "shiny", "bubbles", "dance"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Running around under the warm sun is the best celebration ever!", "zh": "在溫暖的陽光下奔跑追逐，真是最棒的兒童節慶祝方式！", "keywords": ["warm sun", "celebration"] }
    ],
    "vocabulary": [
      { "word": "soar", "phonetic": "/sɔːr/", "pos": "v.", "zh": "高飛、翱翔", "example": "The kite soared gracefully above the park." },
      { "word": "steady", "phonetic": "/ˈsted.i/", "pos": "adj.", "zh": "穩定的、平穩的", "example": "A steady breeze kept the sailboats gliding smoothly." },
      { "word": "celebration", "phonetic": "/ˌsel.əˈbreɪ.ʃən/", "pos": "n.", "zh": "慶祝活動、慶典", "example": "The community held a colorful street celebration." }
    ],
    "dailyPhrase": { "en": "Watch out for...", "zh": "小心……、留意……。" },
    "cultureTip": "台灣的兒童節定在4月4日，學校與各文化園區通常會舉辦豐富的親子體驗活動與免費參觀，鼓勵孩子們走出戶外擁抱自然。"
  },

  # 04-05 [國中挑戰]
  {
    "id": "dialogue-0405",
    "date": "04-05",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "民俗節氣",
    "topic": {
      "en": "Qingming Traditions: Cold Foods, Runbing, and Remembering Ancestors",
      "zh": "清明節俗：寒食潤餅包裹的追思與民俗內涵"
    },
    "situation": "清明節當天，Ethan 和 Grace 一邊幫忙長輩分裝潤餅皮與餡料，一邊探討寒食節與清明掃墓的由來。",
    "speakers": {
      "Ethan": { "role": "Ethan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Grace": { "role": "Grace", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0405.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ethan", "avatar": "👦", "en": "Grace, pass me another thin wrap, please. I am loading mine with shredded cabbage and eggs.", "zh": "Grace，請再遞給我一張潤餅薄皮。我打算在裡面多包一些炒高麗菜絲和蛋絲。", "keywords": ["wrap", "cabbage", "eggs"] },
      { "id": 2, "speaker": "Grace", "avatar": "👧", "en": "Here you go! Do you know why eating cold foods like runbing is associated with Qingming?", "zh": "給你！你知道為什麼像潤餅這種冷食會跟清明節聯結在一起嗎？", "keywords": ["cold foods", "associated", "Qingming"] },
      { "id": 3, "speaker": "Ethan", "avatar": "👦", "en": "My history teacher mentioned it originated from the ancient Cold Food Festival commemorating Jie Zitui.", "zh": "我歷史老師提過，這源於古代紀念介子推的寒食節，當時人們禁火吃冷食。", "keywords": ["Cold Food Festival", "commemorating", "history"] },
      { "id": 4, "speaker": "Grace", "avatar": "👧", "en": "Exactly! Over centuries, the customs of the Cold Food Festival merged with the Qingming solar term.", "zh": "沒錯！經過數百年的演變，寒食節的習俗逐漸與清明節氣融合為一。", "keywords": ["customs", "merged", "solar term"] },
      { "id": 5, "speaker": "Ethan", "avatar": "👦", "en": "Beyond the delicious food, visiting the gravesite and sweeping away fallen leaves really deepens our respect for heritage.", "zh": "除了享用美食，到墓園慎終追遠、清掃落葉雜草，也真正深化了我們對祖先血脈的敬重。", "keywords": ["gravesite", "heritage", "respect"] },
      { "id": 6, "speaker": "Grace", "avatar": "👧", "en": "I agree. It is a heartfelt reminder of where we came from and the sacrifices our forebears made.", "zh": "我很贊同。這提醒了我們根源所在，也感念先人一路走來的付出與犧牲。", "keywords": ["forebears", "sacrifices", "reminder"] }
    ],
    "vocabulary": [
      { "word": "commemorate", "phonetic": "/kəˈmem.ə.reɪt/", "pos": "v.", "zh": "紀念、緬懷", "example": "The monument was built to commemorate the fallen heroes." },
      { "word": "heritage", "phonetic": "/ˈher.ɪ.t̬ɪdʒ/", "pos": "n.", "zh": "遺產、文化傳承", "example": "Preserving cultural heritage is essential for future generations." },
      { "word": "forebear", "phonetic": "/ˈfɔːr.ber/", "pos": "n.", "zh": "先祖、祖先", "example": "They spoke with reverence about the wisdom of their forebears." }
    ],
    "dailyPhrase": { "en": "Over centuries.", "zh": "歷經數個世紀、歷時千百年。" },
    "cultureTip": "清明節與寒食節密不可分。閩南與台灣傳統中，包「潤餅（薄餅）」吃冷食正是保留寒食精神的最佳例證，鹹甜配料由每個人自由搭配，極具家庭凝聚力。"
  },

  # 04-06 [國小中高]
  {
    "id": "dialogue-0406",
    "date": "04-06",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "生活節奏",
    "topic": {
      "en": "Post-Holiday Adjustment: Shaking Off Fatigue & Regaining Rhythm",
      "zh": "收假身心調適：擺脫假期疲憊與重拾日常節奏"
    },
    "situation": "清明連假結束後的第一天校園早晨，Justin 和 Bella 互相打氣，調整作息準備迎接充實的學習。",
    "speakers": {
      "Justin": { "role": "Justin", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Bella": { "role": "Bella", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0406.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Justin", "avatar": "👦", "en": "Phew, waking up at six thirty this morning felt like moving a mountain after four days off.", "zh": "呼，休了四天假之後，今天早上六點半起床感覺像在搬一座大山一樣吃力。", "keywords": ["waking up", "mountain", "days off"] },
      { "id": 2, "speaker": "Bella", "avatar": "👧", "en": "I know what you mean! The post-holiday blues can make us feel sluggish at first.", "zh": "我完全懂！收假症候群一開始確實很容易讓人覺得提不起勁、懶洋洋的。", "keywords": ["blues", "sluggish", "post-holiday"] },
      { "id": 3, "speaker": "Justin", "avatar": "👦", "en": "How do you shake off that sleepy feeling and get back on track?", "zh": "你通常都怎麼甩掉這種瞌睡感，讓自己趕快重回正軌呢？", "keywords": ["shake off", "track", "sleepy"] },
      { "id": 4, "speaker": "Bella", "avatar": "👧", "en": "Drinking a glass of lukewarm lemon water and writing down today's to-do list helps my brain wake up.", "zh": "喝一杯溫檸檬水，然後動手寫下今天的代辦清單，能讓我的大腦迅速開機清醒。", "keywords": ["lukewarm", "to-do list", "brain"] },
      { "id": 5, "speaker": "Justin", "avatar": "👦", "en": "Great idea. Once we finish morning reading, our normal momentum will be right back!", "zh": "好點子。等我們完成晨讀，平時專注向前的動力一定馬上就回來了！", "keywords": ["momentum", "reading"] }
    ],
    "vocabulary": [
      { "word": "sluggish", "phonetic": "/ˈslʌɡ.ɪʃ/", "pos": "adj.", "zh": "緩慢的、怠惰的、無精打采的", "example": "He felt sluggish after eating a heavy lunch." },
      { "word": "momentum", "phonetic": "/moʊˈmen.t̬əm/", "pos": "n.", "zh": "動力、衝勁、動量", "example": "The team gained momentum and won three games in a row." },
      { "word": "lukewarm", "phonetic": "/ˌluːkˈwɔːrm/", "pos": "adj.", "zh": "微溫的、溫熱的", "example": "Wash the sensitive fabric in lukewarm water." }
    ],
    "dailyPhrase": { "en": "Get back on track.", "zh": "重回正軌、恢復正常秩序。" },
    "cultureTip": "英文中的「post-holiday blues」就是我們常說的「收假症候群」。心理學家建議在收假前一晚稍微提早半小時上床，並在隔天早晨透過清淡水分與深呼吸來緩解過渡期的不適。"
  },

  # 04-07 [高中進階]
  {
    "id": "dialogue-0407",
    "date": "04-07",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "健康公民",
    "topic": {
      "en": "World Health Day: Balancing Mental Wellness and Physical Activity",
      "zh": "世界衛生日：現代學子的心理健康與體能自律"
    },
    "situation": "4月7日世界衛生日，高中生 Ryan 和 Claire 在自習室走廊深入探討學生族群如何在繁重課業中維持身心平衡。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Claire": { "role": "Claire", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0407.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "Claire, today marks World Health Day. The World Health Organization is highlighting equal access to comprehensive healthcare.", "zh": "Claire，今天是世界衛生日。世界衛生組織正強調人人享有全面健康照護的公平權利。", "keywords": ["World Health Day", "healthcare", "comprehensive"] },
      { "id": 2, "speaker": "Claire", "avatar": "👩‍🎓", "en": "That is vital globally. But even at a personal level, high schoolers frequently neglect mental wellness under intense academic pressure.", "zh": "這在全球層面極具重要性。但就個人層面而言，高中生在沈重升學壓力下也常忽視心理健康。", "keywords": ["wellness", "academic", "neglect"] },
      { "id": 3, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "Precisely. Many students equate being healthy merely with the absence of illness, ignoring chronic sleep deprivation and anxiety.", "zh": "確實如此。許多人僅把健康等同於「沒生病」，卻忽略了慢性睡眠不足與潛伏焦慮的殺傷力。", "keywords": ["equate", "deprivation", "chronic"] },
      { "id": 4, "speaker": "Claire", "avatar": "👩‍🎓", "en": "True wellbeing requires holistic care—regular aerobic exercise, nutritious meals, and the courage to voice our stress.", "zh": "真正的健康需要全面性的關照——規律的有氧運動、均衡營養，以及勇於傾訴壓力的勇氣。", "keywords": ["holistic", "aerobic", "wellbeing"] },
      { "id": 5, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "Taking a thirty-minute brisk walk after school releases endorphins that genuinely clear the mind for evening studies.", "zh": "放學後快走三十分鐘能釋放腦內啡，這能讓思緒變得格外清晰，更有助於晚間複習。", "keywords": ["endorphins", "brisk walk", "clear"] },
      { "id": 6, "speaker": "Claire", "avatar": "👩‍🎓", "en": "Let's commit to that routine starting today. Sustainable academic excellence stems from a resilient body and mind.", "zh": "我們今天就下定決心養成這習慣吧。可持續的卓越學業表現，本就奠基於強韌的身心體魄。", "keywords": ["sustainable", "resilient", "commit"] }
    ],
    "vocabulary": [
      { "word": "comprehensive", "phonetic": "/ˌkɑːm.prəˈhen.sɪv/", "pos": "adj.", "zh": "全方位的、詳盡包羅萬象的", "example": "The hospital offers comprehensive physical examinations." },
      { "word": "deprivation", "phonetic": "/ˌdep.rəˈveɪ.ʃən/", "pos": "n.", "zh": "匱乏、剝奪", "example": "Sleep deprivation severely impairs cognitive function." },
      { "word": "holistic", "phonetic": "/hoʊˈlɪs.tɪk/", "pos": "adj.", "zh": "整體的、全面的", "example": "Doctors advocate a holistic approach to patient recovery." }
    ],
    "dailyPhrase": { "en": "Stem from...", "zh": "源自於……、起因於……。" },
    "cultureTip": "每年4月7日是世界衛生組織（WHO）設立的世界衛生日（World Health Day）。現代醫學與健康觀念早已從「單純沒有疾病」擴展至「生理、心理與社會適應的完滿狀態（Holistic Wellbeing）」"
  },

  # 04-08 [國小中高]
  {
    "id": "dialogue-0408",
    "date": "04-08",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "學業準備",
    "topic": {
      "en": "Midterm Countdown: Structuring an Effective Study Schedule",
      "zh": "期中考倒數複習：規劃有條不紊的讀書行事曆"
    },
    "situation": "距離國小期中考只剩下一週，Nathan 和 Zoe 坐在圖書館討論如何分配複習進度。",
    "speakers": {
      "Nathan": { "role": "Nathan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0408.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Nathan", "avatar": "👦", "en": "Look at the classroom calendar! Only seven days remain until our spring midterm exams begin.", "zh": "你看教室的行事曆！距離我們的春季期中考只剩下最後七天了。", "keywords": ["calendar", "midterm", "seven days"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Don't panic! If we divide each subject into smaller chunks, reviewing won't feel overwhelming.", "zh": "別慌張！如果我們把每個考科拆分成小單元複習，就不會感到不知所措了。", "keywords": ["panic", "chunks", "overwhelming"] },
      { "id": 3, "speaker": "Nathan", "avatar": "👦", "en": "Good strategy. I plan to tackle math fractions tonight and save social studies for tomorrow afternoon.", "zh": "好策略。我打算今晚專攻數學分數單元，把社會科留到明天下午再讀。", "keywords": ["strategy", "fractions", "tackle"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Remember to leave forty minutes for science formulas and plant life cycles too.", "zh": "也別忘了留四十分鐘給自然科的實驗公式與植物生長週期喔。", "keywords": ["formulas", "life cycles", "science"] },
      { "id": 5, "speaker": "Nathan", "avatar": "👦", "en": "Writing down exact time blocks on my planner keeps me accountable and calm.", "zh": "在手帳上把確切的時間區塊規劃寫下來，能讓我保持自律且內心篤定。", "keywords": ["time blocks", "planner", "accountable"] }
    ],
    "vocabulary": [
      { "word": "overwhelming", "phonetic": "/ˌoʊ.vɚˈwel.mɪŋ/", "pos": "adj.", "zh": "難以承受的、勢不可擋的", "example": "The workload seemed overwhelming until we created a plan." },
      { "word": "strategy", "phonetic": "/ˈstræt̬.ə.dʒi/", "pos": "n.", "zh": "策略、對策", "example": "She devised a smart strategy to complete the project on time." },
      { "word": "accountable", "phonetic": "/əˈkaʊn.t̬ə.bəl/", "pos": "adj.", "zh": "負有責任的、能自我要求的", "example": "Study partners help each other stay accountable." }
    ],
    "dailyPhrase": { "en": "Tackle a task.", "zh": "著手處理難題、全力對付任務。" },
    "cultureTip": "教育學者推薦「Time Blocking（時間塊學習法）」，即將每天的時間切分成 25~40 分鐘的專注區間，每段專注於單一科目，能有效提升記憶效率並降低考試焦慮。"
  },

  # 04-09 [國小初階]
  {
    "id": "dialogue-0409",
    "date": "04-09",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "校園自然",
    "topic": {
      "en": "Exciting Science Experiments: Observing Plant Photosynthesis",
      "zh": "自然實驗課的驚奇：觀察植物光合作用的小氣泡"
    },
    "situation": "自然課上，Tyler 和 Amy 正在用燒杯和水蘊草進行光合作用實驗，觀察陽光下的微小氣泡。",
    "speakers": {
      "Tyler": { "role": "Tyler", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Amy": { "role": "Amy", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0409.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tyler", "avatar": "👦", "en": "Amy, come look into this glass beaker under the bright lamp!", "zh": "Amy，快來看這只擺在亮光檯燈下的玻璃燒杯！", "keywords": ["beaker", "lamp", "glass"] },
      { "id": 2, "speaker": "Amy", "avatar": "👧", "en": "Oh, tiny silvery bubbles are forming on the water plant's green leaves!", "zh": "噢，水生植物的綠葉表面正在冒出銀白色的小氣泡呢！", "keywords": ["bubbles", "silvery", "leaves"] },
      { "id": 3, "speaker": "Tyler", "avatar": "👦", "en": "Our teacher said those bubbles are pure oxygen produced by photosynthesis.", "zh": "老師說那些小氣泡就是植物進行光合作用所產生的純氧氣喔。", "keywords": ["oxygen", "photosynthesis", "produced"] },
      { "id": 4, "speaker": "Amy", "avatar": "👧", "en": "Nature is amazing! Plants take in sunlight and give us fresh air to breathe.", "zh": "大自然真是太奇妙了！植物吸收陽光並給予我們呼吸所需的新鮮空氣。", "keywords": ["sunlight", "fresh air", "breathe"] },
      { "id": 5, "speaker": "Tyler", "avatar": "👦", "en": "Let's record the bubble count in our lab notebook right away.", "zh": "我們趕快把氣泡的數量記錄在實驗筆記本上吧。", "keywords": ["record", "notebook"] }
    ],
    "vocabulary": [
      { "word": "beaker", "phonetic": "/ˈbiː.kɚ/", "pos": "n.", "zh": "燒杯", "example": "Pour fifty milliliters of water into the beaker." },
      { "word": "photosynthesis", "phonetic": "/ˌfoʊ.t̬oʊˈsɪn.θə.sɪs/", "pos": "n.", "zh": "光合作用", "example": "Green plants produce glucose through photosynthesis." },
      { "word": "oxygen", "phonetic": "/ˈɑːk.sɪ.dʒən/", "pos": "n.", "zh": "氧氣", "example": "Trees release oxygen into the atmosphere during daytime." }
    ],
    "dailyPhrase": { "en": "Right away.", "zh": "立刻、馬上。" },
    "cultureTip": "光合作用（Photosynthesis）由 photo（光）和 synthesis（合成）組成，是小學至高中自然科學的核心概念。透過水蘊草實驗直觀觀察氧氣氣泡，是極具啟發性的科學實作體驗。"
  },

  # 04-10 [國小中高]
  {
    "id": "dialogue-0410",
    "date": "04-10",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "社區閱讀",
    "topic": {
      "en": "An Afternoon at the Community Library: Focused Study",
      "zh": "社區圖書館的午後：沉浸在專注自習與知識寶庫"
    },
    "situation": "考前倒數的週三下午，Sam 和 Olivia 相約到社區圖書館的自習室，安靜高效地準備考試。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0410.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Finding these quiet corner seats next to the big window was so lucky!", "zh": "能在這扇大落地窗旁邊找到這處安靜的角落座位真是太幸運了！", "keywords": ["corner seats", "window", "lucky"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👧", "en": "Whisper softly, Sam. The library has a strict quiet policy so everyone can concentrate.", "zh": "Sam，說話要小聲點。圖書館有嚴格的安靜規定，這樣大家才能集中精神。", "keywords": ["whisper", "policy", "concentrate"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Sorry about that! Being surrounded by bookshelves filled with thousands of books is inspiring.", "zh": "不好意思！被成千上萬本書籍的書架圍繞，感覺整個人都充滿了求知動力。", "keywords": ["bookshelves", "inspiring"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👧", "en": "I brought my colored highlighters to mark key terms in my history notes.", "zh": "我帶了彩色螢光筆，準備把歷史筆記裡的核心名詞重點標記出來。", "keywords": ["highlighters", "terms", "history"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Let's study silently for one hour, then take a ten-minute water break outside.", "zh": "那我們先專注安靜自習一小時，然後再去外面喝水休息十分鐘。", "keywords": ["silently", "break"] }
    ],
    "vocabulary": [
      { "word": "concentrate", "phonetic": "/ˈkɑːn.sən.treɪt/", "pos": "v.", "zh": "專注、集中精神", "example": "Noise outside made it difficult to concentrate on reading." },
      { "word": "inspiring", "phonetic": "/ɪnˈspaɪr.ɪŋ/", "pos": "adj.", "zh": "令人振奮的、激勵人心的", "example": "The guest speaker delivered an inspiring talk." },
      { "word": "highlighter", "phonetic": "/ˈhaɪˌlaɪ.t̬ɚ/", "pos": "n.", "zh": "螢光筆", "example": "Use a yellow highlighter for main vocabulary words." }
    ],
    "dailyPhrase": { "en": "Whisper softly.", "zh": "輕聲低語、放低音量說話。" },
    "cultureTip": "圖書館自習室常標註「Quiet Zone（靜音區）」。在公共學習場所維持輕聲細語、將手機轉為震動或靜音，是國際通用的基本公民素養。"
  },

  # 04-11 [國中挑戰]
  {
    "id": "dialogue-0411",
    "date": "04-11",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "學習策略",
    "topic": {
      "en": "Crafting Flashcards and Mind Maps for Better Retention",
      "zh": "手繪心智圖與單字卡：提高記憶深度與統整效率"
    },
    "situation": "國中期中考前夕，Julian 和 Hannah 在教室探討如何用心智圖（Mind Maps）整理龐雜的理化與歷史重點。",
    "speakers": {
      "Julian": { "role": "Julian", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Hannah": { "role": "Hannah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0411.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Julian", "avatar": "👦", "en": "Hannah, look at this complex physics chapter on forces and motion. I feel like my brain is spinning!", "zh": "Hannah，你看這章關於力和運動的複雜理化單元。我覺得我的腦袋都快轉不動了！", "keywords": ["physics", "motion", "spinning"] },
      { "id": 2, "speaker": "Hannah", "avatar": "👧", "en": "Instead of re-reading the dense textbook paragraphs, why don't you draw a mind map?", "zh": "與其反覆死讀課本上密密麻麻的段落，你何不試著畫一張心智圖呢？", "keywords": ["dense", "paragraphs", "mind map"] },
      { "id": 3, "speaker": "Julian", "avatar": "👦", "en": "How does visual mapping improve memory retention compared to ordinary rote memorization?", "zh": "比起一般死記硬背，這種視覺化圖像在提高記憶保留率上有什麼優勢？", "keywords": ["retention", "rote", "memorization"] },
      { "id": 4, "speaker": "Hannah", "avatar": "👧", "en": "It branches out from a central theme, connecting formulas to real-world examples with colors and arrows.", "zh": "它從核心主題向外延伸分支，用顏色與箭頭將抽象公式與生活實例直接串聯起來。", "keywords": ["branches", "central", "arrows"] },
      { "id": 5, "speaker": "Julian", "avatar": "👦", "en": "I can also write key definitions on two-sided flashcards for quick active recall sessions.", "zh": "我還可以在雙面單字卡上寫下關鍵定義，方便隨時進行主動提取複習。", "keywords": ["flashcards", "definitions", "active recall"] },
      { "id": 6, "speaker": "Hannah", "avatar": "👧", "en": "Active recall and spaced repetition are proven science-backed study techniques. You will do great!", "zh": "主動回憶與間隔重複是經科學證實極有效的讀書技巧。你一定能考得超棒！", "keywords": ["spaced repetition", "techniques", "science-backed"] }
    ],
    "vocabulary": [
      { "word": "retention", "phonetic": "/rɪˈten.ʃən/", "pos": "n.", "zh": "記憶保持、保留", "example": "Visual aids significantly improve information retention." },
      { "word": "repetition", "phonetic": "/ˌrep.əˈtɪʃ.ən/", "pos": "n.", "zh": "重複、反覆練習", "example": "Language fluency requires constant practice and repetition." },
      { "word": "dense", "phonetic": "/dens/", "pos": "adj.", "zh": "稠密的、資訊量密集的", "example": "The dense legal document took hours to unravel." }
    ],
    "dailyPhrase": { "en": "Branch out from...", "zh": "從……向外延伸、拓展延伸。" },
    "cultureTip": "認知科學研究顯示，相較於被動畫底線（passive highlighting），「Active Recall（主動提取）」搭配「Spaced Repetition（間隔重複）」能將長期記憶效果提升數倍，是全球頂尖學生的核心讀書心法。"
  },

  # 04-12 [國小初階]
  {
    "id": "dialogue-0412",
    "date": "04-12",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "春季園藝",
    "topic": {
      "en": "Planting Seedlings in the Balcony Garden",
      "zh": "陽台小花園：親手播下向日葵與香草種子"
    },
    "situation": "四月中旬春光正好，Ben 和 Lily 在陽台整理花盆，一起親手把種子埋入肥沃的泥土中。",
    "speakers": {
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Lily": { "role": "Lily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0412.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ben", "avatar": "👦", "en": "Lily, I filled these small ceramic pots with moist, dark potting soil.", "zh": "Lily，我已經在這些陶瓷小花盆裡裝滿了濕潤肥沃的培養土。", "keywords": ["ceramic", "pots", "soil"] },
      { "id": 2, "speaker": "Lily", "avatar": "👧", "en": "Awesome! I have sunflower seeds and sweet basil seeds right here.", "zh": "太棒了！我這裡有向日葵種子和甜羅勒香草種子。", "keywords": ["sunflower", "basil", "seeds"] },
      { "id": 3, "speaker": "Ben", "avatar": "👦", "en": "Poke a small hole with your pinky finger and drop two seeds inside.", "zh": "用你的小拇指戳一個小洞，然後把兩顆種子放進去。", "keywords": ["pinky finger", "hole", "drop"] },
      { "id": 4, "speaker": "Lily", "avatar": "👧", "en": "Cover them gently with soil, and then sprinkle some water using the spray bottle.", "zh": "輕輕用泥土把種子覆蓋好，再用噴霧瓶噴灑適量的水分。", "keywords": ["gently", "sprinkle", "spray bottle"] },
      { "id": 5, "speaker": "Ben", "avatar": "👦", "en": "With enough sunlight, we will see little green sprouts in just a few days!", "zh": "只要有充足的陽光，短短幾天我們就能看見翠綠的小嫩芽冒出來了！", "keywords": ["sprouts", "sunlight", "green"] }
    ],
    "vocabulary": [
      { "word": "seedling", "phonetic": "/ˈsiːd.lɪŋ/", "pos": "n.", "zh": "幼苗、小苗", "example": "Protect the fragile seedlings from harsh winds." },
      { "word": "sprinkle", "phonetic": "/ˈsprɪŋ.kəl/", "pos": "v.", "zh": "灑、噴灑", "example": "Sprinkle a pinch of salt over the sliced tomatoes." },
      { "word": "sprout", "phonetic": "/spraʊt/", "pos": "n.", "zh": "新芽、嫩芽", "example": "Green sprouts poked through the damp garden soil." }
    ],
    "dailyPhrase": { "en": "In just a few days.", "zh": "只要短短幾天之內。" },
    "cultureTip": "春季園藝（Spring Gardening）在許多英美國家是家家戶戶的傳統樂趣。即使住在公寓，在陽台（balcony）種植小盆香草（如羅勒 basil、薄荷 mint）也是極佳的生活療癒方式。"
  },

  # 04-13 [高中進階]
  {
    "id": "dialogue-0413",
    "date": "04-13",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "心理調節",
    "topic": {
      "en": "Managing Academic Pressure: Practical Strategies for Test Anxiety",
      "zh": "化解考試焦慮：正念呼吸與壓力轉化的心態技巧"
    },
    "situation": "期中考前一天晚上，高二學生 Sean 和 Melody 透過通話交流如何面對緊張情緒，將焦慮轉化為專注力。",
    "speakers": {
      "Sean": { "role": "Sean", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Melody": { "role": "Melody", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0413.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sean", "avatar": "👨‍🎓", "en": "Melody, to be candid, my stomach is in knots thinking about tomorrow's advanced calculus exam.", "zh": "Melody，老實說，一想到明天的高級微積分期中考，我的胃就緊張得揪成一團。", "keywords": ["candid", "calculus", "knots"] },
      { "id": 2, "speaker": "Melody", "avatar": "👩‍🎓", "en": "That physiological reaction is totally natural, Sean. Test anxiety is simply adrenaline preparing your body to perform.", "zh": "那種生理反應完全是正常的，Sean。考試焦慮本質上只是腎上腺素在調動身體準備全力以赴。", "keywords": ["physiological", "adrenaline", "anxiety"] },
      { "id": 3, "speaker": "Sean", "avatar": "👨‍🎓", "en": "I worry that if I blank out on the first difficult problem, my composure will unravel completely.", "zh": "我擔心如果卡在第一題難題腦袋一片空白，我的沉著冷靜就會徹底崩潰。", "keywords": ["blank out", "composure", "unravel"] },
      { "id": 4, "speaker": "Melody", "avatar": "👩‍🎓", "en": "If that happens, practice diaphragmatic breathing: inhale for four seconds, hold for four, and exhale slowly.", "zh": "如果發生這種情況，練習腹式深呼吸：吸氣四秒、屏息四秒，然後緩緩吐氣。", "keywords": ["diaphragmatic", "breathing", "inhale", "exhale"] },
      { "id": 5, "speaker": "Sean", "avatar": "👨‍🎓", "en": "That deliberate grounding technique actually resets the nervous system, doesn't it?", "zh": "這種有意識的著陸接地放鬆法確實能重設自律神經系統，對吧？", "keywords": ["grounding", "deliberate", "nervous system"] },
      { "id": 6, "speaker": "Melody", "avatar": "👩‍🎓", "en": "Exactly. Reframe the test not as a judgment of your worth, but simply as a benchmark of what you have mastered so far.", "zh": "正是如此。將考試重新定義：它不是對你個人價值的審判，而只是檢視你目前所學掌握度的一個基準指標而已。", "keywords": ["reframe", "benchmark", "mastered"] }
    ],
    "vocabulary": [
      { "word": "composure", "phonetic": "/kəmˈpoʊ.ʒɚ/", "pos": "n.", "zh": "鎮靜、沉著", "example": "She maintained her composure despite the unexpected crisis." },
      { "word": "reframe", "phonetic": "/ˌriːˈfreɪm/", "pos": "v.", "zh": "重新建構、換個角度看待", "example": "Cognitive therapy helps patients reframe negative thoughts." },
      { "word": "benchmark", "phonetic": "/ˈbentʃ.mɑːrk/", "pos": "n.", "zh": "基準、標準指標", "example": "This semester's scores will serve as a useful benchmark." }
    ],
    "dailyPhrase": { "en": "In knots.", "zh": "（胃或神經）緊張得揪成一團。" },
    "cultureTip": "運動員與心理學家常用「Reframing（認知重塑）」將壓力信號（心跳加速、掌心出汗）詮釋為「興奮就緒（excited & ready）」而非「恐懼崩潰」，能大幅提升臨場發揮與抗壓表現。"
  },

  # 04-14 [國小初階]
  {
    "id": "dialogue-0414",
    "date": "04-14",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "考試應援",
    "topic": {
      "en": "First Day of Midterm Exams: Mutual Encouragement",
      "zh": "期中考第一天：給彼此一個擊掌與滿滿信心"
    },
    "situation": "4月14日期中考首日早晨，Leo 和 Ruby 在教室門口互道加油，拿出文具準備應考。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Ruby": { "role": "Ruby", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0414.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Today is the big day, Ruby! Are you all set for Mandarin and English?", "zh": "Ruby，關鍵的大日子到了！國語和英語科目你都準備好了嗎？", "keywords": ["big day", "set", "English"] },
      { "id": 2, "speaker": "Ruby", "avatar": "👧", "en": "Yes! I double-checked my pencil case. I have two sharp 2B pencils and a soft eraser.", "zh": "準備好囉！我仔細檢查了鉛筆盒，裡面有兩支削尖的 2B 鉛筆和一塊柔軟好擦的橡皮擦。", "keywords": ["pencil case", "eraser", "sharp"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Great! My mom reminded me to read every single question carefully before writing answers.", "zh": "太好了！我媽媽提醒我，寫答案之前一定要把每個題目從頭到尾看清楚。", "keywords": ["question", "carefully", "reminded"] },
      { "id": 4, "speaker": "Ruby", "avatar": "👧", "en": "That is the golden rule. Give me a high five! We are going to do our absolute best.", "zh": "那是考試的黃金準則。跟我擊個掌吧！我們一定會全力以赴發揮得超棒。", "keywords": ["golden rule", "high five", "best"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "High five! Take a deep breath and smile. Good luck!", "zh": "擊掌！深呼吸，保持微笑。祝我們考試順利！", "keywords": ["smile", "good luck"] }
    ],
    "vocabulary": [
      { "word": "pencil case", "phonetic": "/ˈpen.səl keɪs/", "pos": "n.", "zh": "鉛筆盒、筆袋", "example": "She organized her pens neatly inside her pencil case." },
      { "word": "eraser", "phonetic": "/ɪˈreɪ.sɚ/", "pos": "n.", "zh": "橡皮擦", "example": "He rubbed out the smudge with a soft rubber eraser." },
      { "word": "absolute", "phonetic": "/ˈæb.sə.luːt/", "pos": "adj.", "zh": "絕對的、完全的", "example": "She performed with absolute confidence." }
    ],
    "dailyPhrase": { "en": "Give me a high five!", "zh": "跟我擊個掌！/ 來擊掌鼓勵一下！" },
    "cultureTip": "在歐美校園文化中，「High five（擊掌）」是最普及且充滿正能量的肢體語言，象徵夥伴間的激勵（encouragement）與同心協力。"
  },

  # 04-15 [國小中高]
  {
    "id": "dialogue-0415",
    "date": "04-15",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "考後心態",
    "topic": {
      "en": "Decompressing After the Math Exam: Looking Forward",
      "zh": "考完數學之後：放下糾結、專注明天的挑戰"
    },
    "situation": "難度頗高的期中考數學科剛敲鐘交卷，Max 和 Grace 坐在走廊長凳上談論如何及時調整心情。",
    "speakers": {
      "Max": { "role": "Max", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Grace": { "role": "Grace", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0415.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Max", "avatar": "👦", "en": "Whew, that last geometry problem on the test paper really made my head ache!", "zh": "呼，考卷上最後那一題幾何應用題真的讓我傷透腦筋、頭昏腦脹！", "keywords": ["geometry", "head ache", "test paper"] },
      { "id": 2, "speaker": "Grace", "avatar": "👧", "en": "I know! The calculation involved tricky steps, but whatever is done is done.", "zh": "我知道！那個計算步驟真的很刁鑽，但考完就考完了，過去的就讓它過去吧。", "keywords": ["calculation", "tricky", "done"] },
      { "id": 3, "speaker": "Max", "avatar": "👦", "en": "Some classmates are already arguing about option B versus option C outside.", "zh": "外面走廊已經有一些同學在爭論到底是選 B 還是選 C 了。", "keywords": ["arguing", "option"] },
      { "id": 4, "speaker": "Grace", "avatar": "👧", "en": "Debating answers right after an exam only creates unnecessary stress. It won't change our scores.", "zh": "剛考完立刻對答案只會造成不必要的焦慮與壓力。這根本無法改變卷面分數。", "keywords": ["debating", "stress", "scores"] },
      { "id": 5, "speaker": "Max", "avatar": "👦", "en": "You are right. Let's eat our lunch, drink some water, and focus our energy on tomorrow's science test.", "zh": "你說得對。我們好好吃午餐、補充水分，把所有精力集中在明天的自然科吧。", "keywords": ["energy", "lunch", "science"] }
    ],
    "vocabulary": [
      { "word": "geometry", "phonetic": "/dʒiˈɑː.mə.tri/", "pos": "n.", "zh": "幾何學、幾何圖形", "example": "We learned how to calculate the area of triangles in geometry." },
      { "word": "calculation", "phonetic": "/ˌkæl.kjəˈleɪ.ʃən/", "pos": "n.", "zh": "計算、推算", "example": "A simple calculation error ruined the whole proof." },
      { "word": "unnecessary", "phonetic": "/ʌnˈnes.ə.ser.i/", "pos": "adj.", "zh": "不必要的、多餘的", "example": "Avoid unnecessary arguments and stay calm." }
    ],
    "dailyPhrase": { "en": "What is done is done.", "zh": "木已成舟、過去的就別再糾結。" },
    "cultureTip": "英語名言說「Don't cry over spilt milk（覆水難收）」。考試結束後立即對答案容易引發「Post-Exam Stress」，將注意力轉向下一個科目才是成熟學習者的良好心態。"
  },

  # 04-16 [國中挑戰]
  {
    "id": "dialogue-0416",
    "date": "04-16",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "校園喜悅",
    "topic": {
      "en": "Midterm Exams Concluded: Relief and Ice Cream Treats",
      "zh": "期中考圓滿落幕：如釋重負與犒賞自己的冰淇淋"
    },
    "situation": "最後一節考試鐘聲敲響，Dylan 和 Chloe 踏出校門，享受考完後輕鬆愜意的午後時光。",
    "speakers": {
      "Dylan": { "role": "Dylan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0416.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Dylan", "avatar": "👦", "en": "Listen to that final bell! It sounds like the sweet sound of ultimate freedom!", "zh": "聽聽那最後一聲鐘聲！這簡直是象徵終極自由的甜美旋律！", "keywords": ["final bell", "freedom", "sweet"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "I feel a colossal weight being lifted off my shoulders. We survived two intense exam days.", "zh": "我覺得肩膀上龐大的重擔終於被卸下來了。我們順利挺過這兩天緊繃的考試！", "keywords": ["colossal", "weight", "survived"] },
      { "id": 3, "speaker": "Dylan", "avatar": "👦", "en": "We certainly worked hard during those late-night study sessions. We deserve a celebration.", "zh": "那些深夜苦讀的時光我們真的付出很多努力。我們絕對值得好好慶祝一下。", "keywords": ["deserve", "celebration", "study"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "How about heading over to that new gelato parlor down the street for a double-scoop cone?", "zh": "不如我們走到街角那家新開的義式冰淇淋店，買一支配兩球的大甜筒怎麼樣？", "keywords": ["gelato", "double-scoop", "cone"] },
      { "id": 5, "speaker": "Dylan", "avatar": "👦", "en": "Count me in! I am definitely getting dark chocolate combined with fresh mango.", "zh": "算我一份！我一定要點濃郁黑巧克力搭配新鮮芒果口味。", "keywords": ["dark chocolate", "mango", "count me in"] },
      { "id": 6, "speaker": "Chloe", "avatar": "👧", "en": "After that, we can finally enjoy an afternoon of guilt-free video games and leisure reading!", "zh": "吃完冰之後，我們終於可以毫無罪惡感地享受打電動和閱讀休閒小說的悠閒午後了！", "keywords": ["guilt-free", "leisure", "video games"] }
    ],
    "vocabulary": [
      { "word": "colossal", "phonetic": "/kəˈlɑː.səl/", "pos": "adj.", "zh": "巨大的、龐大的", "example": "The team made a colossal effort to finish before the deadline." },
      { "word": "gelato", "phonetic": "/dʒəˈlɑː.toʊ/", "pos": "n.", "zh": "義式冰淇淋", "example": "Italian gelato has a denser, smoother texture than regular ice cream." },
      { "word": "guilt-free", "phonetic": "/ˈɡɪlt.friː/", "pos": "adj.", "zh": "毫無愧疚感或罪惡感的", "example": "After finals, she enjoyed a guilt-free weekend binge-watching shows." }
    ],
    "dailyPhrase": { "en": "Count me in!", "zh": "算我一份！/ 我一定要加入！" },
    "cultureTip": "在學生文化中，期中考或期末考結束稱為「Exams are over!」，犒賞自己吃頓好的或吃冰淇淋稱為「treat oneself」，適度慶祝有助於心理重設與建立學習成就感。"
  },

  # 04-17 [高中進階]
  {
    "id": "dialogue-0417",
    "date": "04-17",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "自我成長",
    "topic": {
      "en": "Post-Exam Reflection: Analyzing Mistakes to Foster True Growth",
      "zh": "考後訂正省思：從錯題分析中汲取真正的進步養分"
    },
    "situation": "高中期中考後試卷發回，Kevin 和 Audrey 拿著錯題本討論如何系統化歸納解題盲點。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Audrey": { "role": "Audrey", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0417.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "👨‍🎓", "en": "Audrey, our chemistry and history scores were just posted. I scored lower than I had anticipated on organic reactions.", "zh": "Audrey，化學和歷史成績剛公告了。我在有機化學反應題上的分數比我預期的還要低。", "keywords": ["chemistry", "organic", "anticipated"] },
      { "id": 2, "speaker": "Audrey", "avatar": "👩‍🎓", "en": "I understand the initial disappointment, Kevin, but a raw test score merely highlights diagnostic feedback.", "zh": "我理解最初的失落感，Kevin，但未經修飾的分數本質上只是提供具診斷價值的回饋而已。", "keywords": ["disappointment", "diagnostic", "feedback"] },
      { "id": 3, "speaker": "Kevin", "avatar": "👨‍🎓", "en": "You are right. Instead of brooding over the numbers, I should categorize whether my mistakes stemmed from conceptual gaps or careless calculation.", "zh": "你說得對。與其為數字悶悶不樂，我更應該分類我的錯誤究竟是源自於概念盲點還是粗心計算。", "keywords": ["brooding", "categorize", "conceptual"] },
      { "id": 4, "speaker": "Audrey", "avatar": "👩‍🎓", "en": "Exactly. I maintain an error log where I re-solve flawed questions from scratch and annotate the underlying rationale.", "zh": "完全沒錯。我一直維持著做錯題筆記的習慣，從零開始重解錯題，並在一旁註解底層邏輯。", "keywords": ["error log", "annotate", "rationale"] },
      { "id": 5, "speaker": "Kevin", "avatar": "👨‍🎓", "en": "Documenting why the wrong choice seemed plausible at the time reveals cognitive blind spots.", "zh": "記錄下為什麼當時那個錯誤選項看起來很合理，能精準揭露我們的認知盲區。", "keywords": ["plausible", "blind spots", "cognitive"] },
      { "id": 6, "speaker": "Audrey", "avatar": "👩‍🎓", "en": "Precisely. True academic growth does not come from perfection; it flourishes when we transform blunders into wisdom.", "zh": "精闢。真正的學術成長從來不是來自於一開始的完美，而是在我們把失誤轉化為智慧時蓬勃綻放。", "keywords": ["perfection", "flourishes", "blunders"] }
    ],
    "vocabulary": [
      { "word": "diagnostic", "phonetic": "/ˌdaɪ.əɡˈnɑː.stɪk/", "pos": "adj.", "zh": "診斷的、分析判斷的", "example": "The practice test provided valuable diagnostic insight." },
      { "word": "plausible", "phonetic": "/ˈplɑː.zə.bəl/", "pos": "adj.", "zh": "看似合理的、貌似可信的", "example": "His explanation sounded plausible, but turned out inaccurate." },
      { "word": "rationale", "phonetic": "/ˌræʃ.əˈnæl/", "pos": "n.", "zh": "根本原因、邏輯依據", "example": "The principal explained the educational rationale behind the new policy." }
    ],
    "dailyPhrase": { "en": "From scratch.", "zh": "從零開始、白手起家。" },
    "cultureTip": "教育學中的「Metacognition（後設認知 / 認知自省）」強調對自身思考過程的反省。建立「Error Log（錯題本）」並進行錯題訂正分析，是將短期記憶轉化為穩固深層理解的最強工具。"
  },

  # 04-18 [國小中高]
  {
    "id": "dialogue-0418",
    "date": "04-18",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "週末踏青",
    "topic": {
      "en": "Weekend Hiking: Listening to Forest Birds and Brooks",
      "zh": "週末登山步道：傾聽潺潺溪流與翠鳥鳴囀"
    },
    "situation": "考後的第一個週末早晨，Jason 和 Maya 跟著家人一起走進近郊森林步道，享受大自然負離子。",
    "speakers": {
      "Jason": { "role": "Jason", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Maya": { "role": "Maya", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0418.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Jason", "avatar": "👦", "en": "Take a deep breath, Maya! The damp scent of pine trees and moss here is so refreshing.", "zh": "Maya，深吸一口氣！這裡松樹與青苔濕潤的芬芳氣息真的好令人心曠神怡。", "keywords": ["pine trees", "moss", "refreshing"] },
      { "id": 2, "speaker": "Maya", "avatar": "👧", "en": "Listen closely! Beside that bubbling mountain brook, I can hear a bird singing sweet musical notes.", "zh": "仔細聽！在那條淙淙流淌的山澗小溪旁，我聽到一隻小鳥正唱著清脆悠揚的音符呢。", "keywords": ["bubbling", "brook", "musical"] },
      { "id": 3, "speaker": "Jason", "avatar": "👦", "en": "Look up on that low oak branch! It has bright blue feathers. Could that be a kingfisher?", "zh": "看那根低垂的橡樹枝頭！它長著亮藍色的羽毛，會不會是一隻翠鳥呀？", "keywords": ["branch", "feathers", "kingfisher"] },
      { "id": 4, "speaker": "Maya", "avatar": "👧", "en": "Yes, it looks exactly like one! Hiking in the mountains really clears all the fatigue from our heads.", "zh": "沒錯，看起來一模一樣！在山林裡健行真的把我們腦袋裡所有的疲勞都一掃而空。", "keywords": ["hiking", "fatigue", "mountains"] },
      { "id": 5, "speaker": "Jason", "avatar": "👦", "en": "Let's reach the viewing platform before noon to enjoy our picnic sandwiches with a panoramic view.", "zh": "我們在中午前爬到觀景平台吧，一邊眺望全景一邊享用我們的野餐三明治。", "keywords": ["viewing platform", "picnic", "panoramic"] }
    ],
    "vocabulary": [
      { "word": "brook", "phonetic": "/brʊk/", "pos": "n.", "zh": "小溪、小河", "example": "Clear cold water flowed gently down the stony brook." },
      { "word": "kingfisher", "phonetic": "/ˈkɪŋˌfɪʃ.ɚ/", "pos": "n.", "zh": "翠鳥", "example": "The kingfisher dove swiftly to snatch a small fish." },
      { "word": "panoramic", "phonetic": "/ˌpæn.əˈræm.ɪk/", "pos": "adj.", "zh": "全景的、俯瞰全貌的", "example": "The mountain peak provides a stunning panoramic vista." }
    ],
    "dailyPhrase": { "en": "Listen closely!", "zh": "仔細聽！/ 留神細聽！" },
    "cultureTip": "森林浴（Forest Bathing，源自日文 Shinrin-yoku）在歐美深受自然愛好者推崇。走進森林接收芬多精（phytoncides）與負離子，能顯著降低人體壓力賀爾蒙並提升專注力。"
  },

  # 04-19 [國中挑戰]
  {
    "id": "dialogue-0419",
    "date": "04-19",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "節氣文化",
    "topic": {
      "en": "Guyu Solar Term: Spring Rain Nourishing the Sprouting Crops",
      "zh": "穀雨節氣：暮春時節的潤澤甘霖與採茶時光"
    },
    "situation": "時值二十四節氣中的「穀雨」，Leo 和 Jessica 漫步在春雨後的植物園，探討節氣農耕與茶文化。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Jessica": { "role": "Jessica", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0419.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "A fine drizzle has been falling since dawn. Everything in the garden looks extra vibrant and lush.", "zh": "從破曉時分起就下著綿綿細雨。花園裡的一切看起來都格外生機盎然、翠綠欲滴。", "keywords": ["drizzle", "vibrant", "lush"] },
      { "id": 2, "speaker": "Jessica", "avatar": "👧", "en": "Today marks Guyu, or 'Grain Rain', the sixth and final solar term of the spring season.", "zh": "今天正是「穀雨」，也就是春天的第六個、也是最後一個節氣。", "keywords": ["Guyu", "Grain Rain", "solar term"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "The name itself is poetic: 'rain gives birth to hundreds of grains,' replenishing soil for young crops.", "zh": "這個名稱本身就很富有詩意：「雨生百穀」，豐沛的雨水滋養了土壤中茁壯的幼苗糧食。", "keywords": ["poetic", "grains", "replenishing"] },
      { "id": 4, "speaker": "Jessica", "avatar": "👧", "en": "My grandfather also told me that Guyu is the prime season for harvesting delicate spring tea leaves.", "zh": "我爺爺還告訴我，穀雨是採摘細緻嫩芽『穀雨春茶』的最佳黃金時節。", "keywords": ["harvesting", "delicate", "tea leaves"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Tea picked during this period is famous for its mellow fragrance and sweet lingering aftertaste.", "zh": "在這個時節採摘烘焙的茶葉，向來以醇厚的清香與甘甜悠長的喉韻聞名。", "keywords": ["mellow", "fragrance", "aftertaste"] },
      { "id": 6, "speaker": "Jessica", "avatar": "👧", "en": "Traditional agricultural wisdom truly captures the rhythm of nature with remarkable precision.", "zh": "傳統的農耕智慧真的以令人驚嘆的精準度，捕捉到了大自然生息運轉的節奏。", "keywords": ["agricultural", "precision", "wisdom"] }
    ],
    "vocabulary": [
      { "word": "replenish", "phonetic": "/rɪˈplen.ɪʃ/", "pos": "v.", "zh": "補充、滋養、充實", "example": "The gentle rain replenished the dried reservoir." },
      { "word": "mellow", "phonetic": "/ˈmel.oʊ/", "pos": "adj.", "zh": "醇厚的、柔和圓潤的", "example": "The aged tea has a smooth and mellow flavor." },
      { "word": "aftertaste", "phonetic": "/ˈæf.tɚ.teɪst/", "pos": "n.", "zh": "回甘、餘味", "example": "High mountain oolong leaves a delightfully sweet aftertaste." }
    ],
    "dailyPhrase": { "en": "Give birth to...", "zh": "孕育出……、促成……的誕生。" },
    "cultureTip": "穀雨（Grain Rain）取自「雨生百穀」之意。民諺有「穀雨穀雨，採茶對雨」，傳說穀雨這天採收的茶葉富含維生素與胺基酸，香氣特別清甜醇厚，稱為「穀雨春茶」。"
  },

  # 04-20 [國小中高]
  {
    "id": "dialogue-0420",
    "date": "04-20",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "戶外休閒",
    "topic": {
      "en": "Riverside Bicycle Ride: Spring Wind and Sunbeams",
      "zh": "河濱單車逍遙遊：春風吹拂與沿途的春日暖陽"
    },
    "situation": "週日下午，Daniel 和 Emily 牽著剛檢查完胎壓的自行車，在平整寬敞的河濱自行車道暢快奔馳。",
    "speakers": {
      "Daniel": { "role": "Daniel", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emily": { "role": "Emily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0420.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Daniel", "avatar": "👦", "en": "Did you check your bike tires and brakes before we set off, Emily?", "zh": "Emily，我們出發前你有仔細檢查過腳踏車輪胎胎壓和煞車嗎？", "keywords": ["tires", "brakes", "set off"] },
      { "id": 2, "speaker": "Emily", "avatar": "👧", "en": "I did! I pumped both tires to forty-five psi, and my safety helmet is securely fastened.", "zh": "我有檢查！我把前後輪都充氣到了 45 psi，安全帽也已經牢固扣好了。", "keywords": ["pumped", "safety helmet", "fastened"] },
      { "id": 3, "speaker": "Daniel", "avatar": "👦", "en": "Great safety habit! The dedicated riverside bike path has virtually no car traffic.", "zh": "很好的安全好習慣！這條專用的河濱自行車道幾乎完全沒有汽機車干擾。", "keywords": ["dedicated", "traffic", "safety"] },
      { "id": 4, "speaker": "Emily", "avatar": "👧", "en": "Pedaling along the glittering water with yellow cosmos blooming on both sides feels so liberating.", "zh": "沿著閃閃發光的河畔踩著踏板前進，兩旁開滿了黃波斯菊，感覺真是無比自由自在。", "keywords": ["pedaling", "glittering", "liberating"] },
      { "id": 5, "speaker": "Daniel", "avatar": "👦", "en": "Let's cycle up to the suspension bridge rest area and grab some cold barley tea.", "zh": "那我們一路騎到吊橋休息區，買瓶冰涼的麥茶解解渴吧。", "keywords": ["suspension bridge", "barley tea", "cycle"] }
    ],
    "vocabulary": [
      { "word": "fasten", "phonetic": "/ˈfæs.ən/", "pos": "v.", "zh": "繫緊、扣上", "example": "Please fasten your seatbelts before takeoff." },
      { "word": "liberating", "phonetic": "/ˈlɪb.ə.reɪ.t̬ɪŋ/", "pos": "adj.", "zh": "令人感到自由釋放的", "example": "Swimming in the open ocean was an exhilarating and liberating experience." },
      { "word": "pedal", "phonetic": "/ˈped.əl/", "pos": "v.", "zh": "踩踏板、騎自行車", "example": "She pedaled briskly uphill despite the steep slope." }
    ],
    "dailyPhrase": { "en": "Set off.", "zh": "出發、動身起程。" },
    "cultureTip": "騎乘自行車時配戴符合安全標準的安全帽（safety helmet）能降低 85% 的頭部撞擊受傷風險。台灣多數城市擁有完善的河濱自行車道（Riverside Bikeways），是春季全家戶外運動的最佳去處。"
  },

  # 04-21 [國小初階]
  {
    "id": "dialogue-0421",
    "date": "04-21",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "夏夜奇景",
    "topic": {
      "en": "Firefly Watching in the Twilight: Magical Lanterns",
      "zh": "暮色初顯時賞螢：林間閃爍的夏夜綠色小精靈"
    },
    "situation": "暮色降臨的郊外溪谷步道旁，Tim 和 Chloe 屏住呼吸，看見成群結隊的螢火蟲在草叢間發出柔和黃綠色光芒。",
    "speakers": {
      "Tim": { "role": "Tim", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0421.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tim", "avatar": "👦", "en": "Chloe, look over there by the shallow creek! Do you see those flickering lights?", "zh": "Chloe，看那邊淺水溪流旁邊！你有看見那些閃爍跳動的光芒嗎？", "keywords": ["shallow", "flickering", "creek"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "Yes! They look like tiny magical fairies glowing gently in the dark.", "zh": "看見了！它們就像在黑暗中溫柔發光的微小神奇小精靈一樣。", "keywords": ["magical", "fairies", "glowing"] },
      { "id": 3, "speaker": "Tim", "avatar": "👦", "en": "Those are fireflies! Remember to cover our flashlight with red cellophane paper.", "zh": "那些是螢火蟲！記得把我們的手電筒罩上紅色玻璃紙喔。", "keywords": ["fireflies", "flashlight", "cellophane"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "Right. Red light does not hurt their sensitive eyes or disrupt their flashing signals.", "zh": "對的。紅光不會傷害它們敏感的眼睛，也不會干擾它們求偶的光信號。", "keywords": ["sensitive", "signals", "disrupt"] },
      { "id": 5, "speaker": "Tim", "avatar": "👦", "en": "Watching them float through the cool night air is like stepping into a fairy tale.", "zh": "看著它們在清涼的夜空中飄浮飛舞，就像走進了童話故事裡一樣夢幻。", "keywords": ["float", "fairy tale"] }
    ],
    "vocabulary": [
      { "word": "firefly", "phonetic": "/ˈfaɪr.flaɪ/", "pos": "n.", "zh": "螢火蟲", "example": "Dozens of fireflies illuminated the humid meadow." },
      { "word": "flicker", "phonetic": "/ˈflɪk.ɚ/", "pos": "v.", "zh": "閃爍、搖曳", "example": "Candles flickered gently across the dining room." },
      { "word": "cellophane", "phonetic": "/ˈsel.ə.feɪn/", "pos": "n.", "zh": "玻璃紙", "example": "Wrap the red cellophane around the torch lens." }
    ],
    "dailyPhrase": { "en": "Step into...", "zh": "踏入……、走進……之中。" },
    "cultureTip": "每年四月中旬至五月中旬是台灣的螢火蟲旺季。賞螢守則包含「三不一要」：不捕捉、不喧嘩、不拿強光直射，以及「要」為手電筒貼上紅色玻璃紙，愛護珍貴的生態奇觀。"
  },

  # 04-22 [高中進階]
  {
    "id": "dialogue-0422",
    "date": "04-22",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "地球環境",
    "topic": {
      "en": "Earth Day 2026: Sustainable Living and Zero-Waste School Initiatives",
      "zh": "世界地球日：推動零廢棄校園與永續綠色實踐"
    },
    "situation": "4月22日世界地球日，高中環保社社長 Alex 和副社長 Brenda 正在籌辦校園減塑與自備餐具倡議活動。",
    "speakers": {
      "Alex": { "role": "Alex", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Brenda": { "role": "Brenda", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0422.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Alex", "avatar": "👨‍🎓", "en": "Brenda, as Earth Day arrives today, our environmental club needs to move beyond mere symbolic slogans and foster tangible behavioral shifts.", "zh": "Brenda，今天是世界地球日，我們的環保社不能僅停留在象徵性的口號，更要促成實質的行為轉變。", "keywords": ["Earth Day", "symbolic", "tangible"] },
      { "id": 2, "speaker": "Brenda", "avatar": "👩‍🎓", "en": "I wholeheartedly agree. Single-use plastic waste generated from lunch takeout is one of our school's most glaring issues.", "zh": "我完全贊同。午餐外帶所產生的一次性塑膠垃圾，正是目前我們學校最刺眼的環保痛點之一。", "keywords": ["single-use", "takeout", "glaring"] },
      { "id": 3, "speaker": "Alex", "avatar": "👨‍🎓", "en": "Starting this week, we are collaborating with cafeteria vendors to offer discounts to students bringing reusable containers and tumblers.", "zh": "從這週開始，我們正與學生餐廳店家合作，為自備環保餐盒與保溫隨行杯的同學提供專屬折價優惠。", "keywords": ["collaborating", "reusable", "tumblers"] },
      { "id": 4, "speaker": "Brenda", "avatar": "👩‍🎓", "en": "Economic incentives work wonders. We are also setting up composting bins for organic food scraps beside the garden.", "zh": "經濟誘因往往能創造奇效。我們同時也在花園旁設置堆肥箱，用來回收果皮與廚餘殘渣。", "keywords": ["incentives", "composting", "organic"] },
      { "id": 5, "speaker": "Alex", "avatar": "👨‍🎓", "en": "Transforming waste into nutrient-rich soil for our campus green space beautifully illustrates the circular economy.", "zh": "將廢棄物轉化為滋養校園綠地的肥沃土壤，正是循環經濟理念最美麗生動的實踐體現。", "keywords": ["nutrient-rich", "circular economy"] },
      { "id": 6, "speaker": "Brenda", "avatar": "👩‍🎓", "en": "Every micro habit counts. When hundreds of students make mindful choices daily, the collective ecological footprint shrinks drastically.", "zh": "每一個微小的習慣都至關重要。當數百名學子每天都做出友善環境的自覺選擇，整體的生態足跡便會大幅縮減。", "keywords": ["mindful", "ecological footprint", "drastically"] }
    ],
    "vocabulary": [
      { "word": "tangible", "phonetic": "/ˈtæn.dʒə.bəl/", "pos": "adj.", "zh": "實質的、具體有形的", "example": "We need tangible results, not vague promises." },
      { "word": "incentive", "phonetic": "/ɪnˈsen.tɪv/", "pos": "n.", "zh": "誘因、獎勵措施", "example": "Tax incentives encouraged families to install solar panels." },
      { "word": "ecological", "phonetic": "/ˌek.əˈlɑː.dʒɪ.kəl/", "pos": "adj.", "zh": "生態的、環境保護的", "example": "Deforestation poses a catastrophic ecological crisis." }
    ],
    "dailyPhrase": { "en": "Work wonders.", "zh": "創造奇蹟、產生不可思議的絕佳效果。" },
    "cultureTip": "4月22日是全球公認的世界地球日（Earth Day），源於1970年美國大規模環境保護抗議。現今倡導「循環經濟（Circular Economy）」與「減塑零廢棄（Zero Waste）」，強調個人微行動能凝聚巨大的環境變革力量。"
  },

  # 04-23 [高中進階]
  {
    "id": "dialogue-0423",
    "date": "04-23",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "文學與閱讀",
    "topic": {
      "en": "World Book and Copyright Day: Celebrating the Magic of Reading",
      "zh": "世界閱讀與版權日：沉浸在文學世界的心靈啟迪"
    },
    "situation": "4月23日世界閱讀日，校園圖書館舉辦換書沙龍，Victor 和 Irene 分享一本深刻影響自己世界觀的小說。",
    "speakers": {
      "Victor": { "role": "Victor", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Irene": { "role": "Irene", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0423.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Victor", "avatar": "👨‍🎓", "en": "Irene, what book did you bring to today's World Book Day exchange salon?", "zh": "Irene，你今天帶了哪一本書來參加世界閱讀日的換書沙龍呢？", "keywords": ["exchange salon", "World Book Day"] },
      { "id": 2, "speaker": "Irene", "avatar": "👩‍🎓", "en": "I brought Harper Lee's classic novel, 'To Kill a Mockingbird'. It deeply shaped my perspective on empathy and moral integrity.", "zh": "我帶了哈波李的經典小說《梅岡城故事》。它深深塑造了我對同理心與道德誠信的看法。", "keywords": ["Mockingbird", "empathy", "integrity"] },
      { "id": 3, "speaker": "Victor", "avatar": "👨‍🎓", "en": "A masterpiece indeed! In our digital era dominated by fifteen-second short clips, deep reading has become an endangered art.", "zh": "確實是一部不朽名作！在當今充斥著十五秒短影音的數位時代，深度閱讀幾乎成了一種瀕危的藝術。", "keywords": ["masterpiece", "digital era", "endangered"] },
      { "id": 4, "speaker": "Irene", "avatar": "👩‍🎓", "en": "Precisely. Scrolling provides transient dopamine hits, whereas reading a book allows you to inhabit someone else's mind across centuries and borders.", "zh": "精闢。滑手機只會提供短暫的多巴胺刺激，但讀一本書卻能讓你跨越世紀與國界，走進另一個靈魂的心靈世界。", "keywords": ["transient", "dopamine", "inhabit"] },
      { "id": 5, "speaker": "Victor", "avatar": "👨‍🎓", "en": "I brought Orwell's '1984' in return. Engaging with challenging prose sharpens our critical thinking against misinformation.", "zh": "我則帶了歐威爾的《1984》作為交換。閱讀深邃有挑戰性的散文著作，能磨礪我們抵抗假訊息的思辨力。", "keywords": ["prose", "misinformation", "sharpens"] },
      { "id": 6, "speaker": "Irene", "avatar": "👩‍🎓", "en": "A quote from George R.R. Martin says it best: 'A reader lives a thousand lives before he dies; the man who never reads lives only one.'", "zh": "作家喬治馬丁的名言說得最貼切：『讀書的人在死前能活過一千種人生；而不讀書的人，一輩子只能活一次。』", "keywords": ["thousand lives", "quote"] }
    ],
    "vocabulary": [
      { "word": "empathy", "phonetic": "/ˈem.pə.θi/", "pos": "n.", "zh": "同理心、感同身受", "example": "Literature helps young minds develop deep empathy for others." },
      { "word": "transient", "phonetic": "/ˈtræn.zi.ənt/", "pos": "adj.", "zh": "短暫的、轉瞬即逝的", "example": "Online fame is often superficial and transient." },
      { "word": "inhabit", "phonetic": "/ɪnˈhæb.ɪt/", "pos": "v.", "zh": "居住於、棲息於、進駐入", "example": "Great actors inhabit their characters completely." }
    ],
    "dailyPhrase": { "en": "Shape one's perspective.", "zh": "塑造某人的世界觀與思考角度。" },
    "cultureTip": "4月23日是聯合國教科文組織設立的「世界圖書與版權日（World Book and Copyright Day）」，這一天正是大文豪莎士比亞（William Shakespeare）與塞萬提斯（Miguel de Cervantes）的逝世紀念日。在西班牙加泰隆尼亞，傳統上這天男女會互贈玫瑰與書籍。"
  },

  # 04-24 [國小中高]
  {
    "id": "dialogue-0424",
    "date": "04-24",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "社區跳蚤市場",
    "topic": {
      "en": "Community Charity Flea Market: Giving Old Toys New Life",
      "zh": "社區公益跳蚤市場：賦予舊玩具與書籍全新生命"
    },
    "situation": "週末社區活動中心前舉辦二手跳蚤市集，Sammy 和 Noah 佈置好自己的小攤位，販賣保存完好的繪本與積木玩具。",
    "speakers": {
      "Sammy": { "role": "Sammy", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Noah": { "role": "Noah", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0424.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sammy", "avatar": "👧", "en": "Noah, our folding table looks so organized with handwritten price tags on every item!", "zh": "Noah，我們的折疊桌擺得好整齊，每樣物品上都貼著手寫的可愛標價卡呢！", "keywords": ["folding table", "price tags", "organized"] },
      { "id": 2, "speaker": "Noah", "avatar": "👦", "en": "I wiped down all the wooden puzzle blocks and board games until they shone like new.", "zh": "我把所有的木質拼圖積木和桌遊都擦得乾乾淨淨，亮得跟新的一樣。", "keywords": ["wooden", "puzzles", "board games"] },
      { "id": 3, "speaker": "Sammy", "avatar": "👧", "en": "Look, a mother and her young daughter are walking over to check out our illustrated fairy tale books.", "zh": "你看，一位媽媽和她的小女兒正好走過來翻看我們的童話繪本呢。", "keywords": ["illustrated", "fairy tale", "daughter"] },
      { "id": 4, "speaker": "Noah", "avatar": "👦", "en": "Good morning! These picture books are twenty dollars each, or three for fifty dollars!", "zh": "早安！這些精美繪本一本二十元，買三本只要五十元喔！", "keywords": ["picture books", "dollars"] },
      { "id": 5, "speaker": "Sammy", "avatar": "👧", "en": "Pass on pre-loved treasures instead of dumping them in landfills. It feels so rewarding!", "zh": "把珍愛過的二手寶物傳承下去，而不是丟進垃圾掩埋場，這種感覺真有成就感！", "keywords": ["pre-loved", "landfills", "rewarding"] }
    ],
    "vocabulary": [
      { "word": "flea market", "phonetic": "/ˈfliː ˌmɑːr.kɪt/", "pos": "n.", "zh": "跳蚤市場、二手市集", "example": "We found vintage comic books at the weekend flea market." },
      { "word": "pre-loved", "phonetic": "/ˌpriːˈlʌvd/", "pos": "adj.", "zh": "二手但保存完好的、曾被珍愛過的", "example": "She opened an online boutique selling pre-loved clothes." },
      { "word": "rewarding", "phonetic": "/rɪˈwɔːr.dɪŋ/", "pos": "adj.", "zh": "有意義的、令人有成就感的", "example": "Volunteering at the shelter is deeply rewarding work." }
    ],
    "dailyPhrase": { "en": "Wipe down.", "zh": "徹底擦拭乾淨。" },
    "cultureTip": "西方文化廣泛使用「Pre-loved（二手但滿載愛心與回憶）」取代帶有陳舊感的「second-hand」，在跳蚤市場中傳遞物件的生命力與環保減廢理念。"
  },

  # 04-25 [國小初階]
  {
    "id": "dialogue-0425",
    "date": "04-25",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "春日手作",
    "topic": {
      "en": "Weekend Baking Fun: Fresh Strawberry Tarts",
      "zh": "週末烘焙時光：酸甜可口的手作草莓水果塔"
    },
    "situation": "週六午後，Mason 和 Ella 在廚房跟著媽媽一起做春日草莓水果小甜點塔。",
    "speakers": {
      "Mason": { "role": "Mason", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Ella": { "role": "Ella", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0425.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mason", "avatar": "👦", "en": "Ella, the baked tart crusts just came out of the oven. They smell so buttery!", "zh": "Ella，剛烤好的塔皮出爐囉。聞起來奶油香氣好濃郁呀！", "keywords": ["crusts", "oven", "buttery"] },
      { "id": 2, "speaker": "Ella", "avatar": "👧", "en": "Let them cool for ten minutes first. I finished whipping the vanilla custard cream.", "zh": "先讓它們放涼十分鐘。我剛剛已經把香草卡士達醬打得綿滑細緻了。", "keywords": ["cool", "custard", "whipping"] },
      { "id": 3, "speaker": "Mason", "avatar": "👦", "en": "I carefully washed and sliced these sweet, ruby-red strawberries.", "zh": "我仔細把這些香甜如紅寶石般的草莓清洗乾淨並切成薄片了。", "keywords": ["ruby-red", "strawberries", "sliced"] },
      { "id": 4, "speaker": "Ella", "avatar": "👧", "en": "Let's pipe the cream inside each crust and arrange strawberry slices in a flower pattern!", "zh": "我們把卡士達擠進每個塔皮裡，然後把草莓片排成盛開花朵的圖案吧！", "keywords": ["pipe", "arrange", "pattern"] },
      { "id": 5, "speaker": "Mason", "avatar": "👦", "en": "Dust a little powdered sugar on top! It looks like a dessert from a fancy French café!", "zh": "最後在頂部灑上一層糖粉！這看起來簡直就像高級法國咖啡館賣的精緻甜點！", "keywords": ["powdered sugar", "dessert", "French café"] }
    ],
    "vocabulary": [
      { "word": "crust", "phonetic": "/krʌst/", "pos": "n.", "zh": "塔皮、派皮、麵包脆皮", "example": "The pie crust was golden and exceptionally flaky." },
      { "word": "custard", "phonetic": "/ˈkʌs.tɚd/", "pos": "n.", "zh": "卡士達醬、蛋奶凍", "example": "Warm vanilla custard pairs beautifully with berry tarts." },
      { "word": "dust", "phonetic": "/dʌst/", "pos": "v.", "zh": "撒上粉末", "example": "Dust the chocolate cake with icing sugar." }
    ],
    "dailyPhrase": { "en": "Come out of the oven.", "zh": "剛從烤箱新鮮出爐。" },
    "cultureTip": "春季是草莓季尾聲，手作烘焙（Home Baking）是美式與歐式家庭極受歡迎的親子週末活動，藉由量秤原料與裝飾甜點培養孩子的專注力與美感。"
  },

  # 04-26 [國中挑戰]
  {
    "id": "dialogue-0426",
    "date": "04-26",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "感恩心意",
    "topic": {
      "en": "Secretly Preparing a Mother's Day Card and Gift",
      "zh": "悄悄籌劃母親節禮物：手作賀卡與感恩驚喜"
    },
    "situation": "距離五月的母親節只剩兩週，Oliver 和 Maya 在文具店挑選水彩紙與緞帶，策劃一場溫馨的驚喜。",
    "speakers": {
      "Oliver": { "role": "Oliver", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Maya": { "role": "Maya", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0426.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Oliver", "avatar": "👦", "en": "Mother's Day is coming up in two weeks, Maya. Have you thought of a surprise for your mom?", "zh": "Maya，再過兩週就是母親節了。你想好要給你媽媽什麼驚喜了嗎？", "keywords": ["Mother's Day", "surprise", "weeks"] },
      { "id": 2, "speaker": "Maya", "avatar": "👧", "en": "I am designing a handmade pop-up card featuring a bouquet of carnations and warm gratitude messages.", "zh": "我正在設計一張手工立體卡片，裡面會有一束立體的康乃馨花束和溫暖的感謝詞。", "keywords": ["pop-up card", "carnations", "gratitude"] },
      { "id": 3, "speaker": "Oliver", "avatar": "👦", "en": "That is so touching! Store-bought gifts are convenient, but handmade crafts carry unique warmth.", "zh": "那太感人了！買現成的禮物固然方便，但親手做的手作工藝卻擁有無可替代的溫度。", "keywords": ["store-bought", "handmade", "warmth"] },
      { "id": 4, "speaker": "Maya", "avatar": "👧", "en": "My brother and I also decided to secretly clean the entire house and cook breakfast on Mother's Day morning.", "zh": "我和我哥哥還決定，要在母親節那天早晨偷偷把整間屋子打掃乾淨，並親手做早餐給媽媽吃。", "keywords": ["secretly", "breakfast", "clean"] },
      { "id": 5, "speaker": "Oliver", "avatar": "👦", "en": "Relieving mothers of their daily chores is truly the greatest gift of all.", "zh": "幫媽媽分擔卸下平時繁瑣的家務勞動，真的是最棒、最貼心的母親節禮物了。", "keywords": ["chores", "relieving", "gift"] },
      { "id": 6, "speaker": "Maya", "avatar": "👧", "en": "Let's pick out some pastel watercolor paper and silk ribbons to start crafting right away!", "zh": "那我們趕快挑選一些柔和色調的水彩紙和絲綢緞帶，今天就開始動手做吧！", "keywords": ["pastel", "ribbons", "watercolor"] }
    ],
    "vocabulary": [
      { "word": "carnation", "phonetic": "/kɑːrˈneɪ.ʃən/", "pos": "n.", "zh": "康乃馨", "example": "Pink carnations symbolize unconditional motherly love." },
      { "word": "gratitude", "phonetic": "/ˈɡræt̬.ə.tuːd/", "pos": "n.", "zh": "感激、感恩之情", "example": "She expressed heartfelt gratitude to her supportive family." },
      { "word": "pastel", "phonetic": "/pæsˈtel/", "pos": "adj.", "zh": "粉彩的、柔和淡雅的", "example": "The nursery was painted in soft pastel shades." }
    ],
    "dailyPhrase": { "en": "Carry unique warmth.", "zh": "帶有獨一無二的溫度。" },
    "cultureTip": "每年五月的第二個星期日是母親節（Mother's Day）。安娜·賈維斯（Anna Jarvis）推廣康乃馨（Carnation）作為象徵，粉色與紅色康乃馨象徵對母親的感恩與祝福。"
  },

  # 04-27 [高中進階]
  {
    "id": "dialogue-0427",
    "date": "04-27",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "藝術與美感",
    "topic": {
      "en": "Visiting the Modern Art Exhibition: Interpreting Visual Language",
      "zh": "參觀現代藝術特展：品味色彩與當代視覺語言的交會"
    },
    "situation": "週日午後，高中生 Ethan 和 Natalie 漫步於市立美術館的當代藝術特展，欣賞抽象表現主義畫作。",
    "speakers": {
      "Ethan": { "role": "Ethan", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Natalie": { "role": "Natalie", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0427.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ethan", "avatar": "👨‍🎓", "en": "Natalie, observe this massive abstract canvas. The bold, sweeping strokes of crimson juxtaposed with deep indigo are electrifying.", "zh": "Natalie，看看這幅巨大的抽象油畫畫布。鮮紅大膽的粗獷筆觸與深邃靛藍並列對比，視覺衝擊力十足。", "keywords": ["canvas", "juxtaposed", "crimson", "electrifying"] },
      { "id": 2, "speaker": "Natalie", "avatar": "👩‍🎓", "en": "It is mesmerizing. Many visitors find abstract art baffling because they look for literal representation instead of emotional resonance.", "zh": "真令人著迷。很多參觀者覺得抽象藝術令人費解，是因為他們執著於尋找具象實物，而不是去體會情感共鳴。", "keywords": ["mesmerizing", "baffling", "resonance"] },
      { "id": 3, "speaker": "Ethan", "avatar": "👨‍🎓", "en": "Well stated. Art doesn't merely replicate reality like a camera; it translates inner subconscious states into texture and rhythm.", "zh": "說得真好。藝術絕非像相機一樣單純複製現實，而是將內在潛意識狀態轉譯為質地與節奏。", "keywords": ["replicate", "subconscious", "texture"] },
      { "id": 4, "speaker": "Natalie", "avatar": "👩‍🎓", "en": "The museum's curator noted that this artist painted during a transitional era of rapid urbanization.", "zh": "美術館策展人在導覽中特別提到，這位藝術家是在城市化劇烈轉型的動盪時期創作此作品的。", "keywords": ["curator", "transitional", "urbanization"] },
      { "id": 5, "speaker": "Ethan", "avatar": "👨‍🎓", "en": "Knowing that context transforms chaotic splatters into a poignant commentary on modern isolation and vitality.", "zh": "了解了時代背景之後，眼前看似混亂的顏料潑灑，瞬間昇華為對現代孤獨與生命力深刻的哲學詰問。", "keywords": ["splatters", "poignant", "commentary"] },
      { "id": 6, "speaker": "Natalie", "avatar": "👩‍🎓", "en": "Art broadens our intellectual horizons by challenging us to embrace ambiguity rather than demanding immediate answers.", "zh": "藝術之所以能開拓我們的心靈視野，正是因為它引導我們擁抱曖昧與留白，而非急於索求唯一的標準答案。", "keywords": ["intellectual", "horizons", "ambiguity"] }
    ],
    "vocabulary": [
      { "word": "juxtapose", "phonetic": "/ˌdʒʌk.stəˈpoʊz/", "pos": "v.", "zh": "並置、把……並列以形成對比", "example": "The exhibition juxtaposes classical sculptures with modern neon lights." },
      { "word": "mesmerizing", "phonetic": "/ˈmez.mə.raɪ.zɪŋ/", "pos": "adj.", "zh": "令人著迷的、引人入勝的", "example": "Her mesmerizing performance captivated the entire auditorium." },
      { "word": "poignant", "phonetic": "/ˈpɔɪ.njənt/", "pos": "adj.", "zh": "深刻感人的、令人心酸震撼的", "example": "The documentary ended with a poignant reflection on world peace." }
    ],
    "dailyPhrase": { "en": "Broaden one's horizons.", "zh": "開闊眼界、拓展視野。" },
    "cultureTip": "欣賞當代藝術（Contemporary Art）講求「Open Interpretation（開放式詮釋）」。不同於古典寫實畫派，現代藝術著重激發觀者的情感觸動與哲學思辨，提供超越語言的視角碰撞。"
  },

  # 04-28 [國小初階]
  {
    "id": "dialogue-0428",
    "date": "04-28",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "活力校園",
    "topic": {
      "en": "Friendly Badminton Match After School: Energetic Rally",
      "zh": "放學後的友誼羽球賽：揮灑汗水與歡笑的激烈對打"
    },
    "situation": "春日放學後，Ryan 和 Jenny 來到活動中心羽球場，進行一場活力充沛的友誼單打對抗。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Jenny": { "role": "Jenny", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0428.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "👦", "en": "Jenny, are you ready for our three-set badminton match? I have my favorite carbon racket!", "zh": "Jenny，準備好我們的三局羽球賽了嗎？我帶了我最喜歡的碳纖維球拍喔！", "keywords": ["badminton", "racket", "match"] },
      { "id": 2, "speaker": "Jenny", "avatar": "👧", "en": "You bet! Let me serve first. Watch out for my high backhand serve!", "zh": "當然囉！由我先發球。小心我又高又深的反手發球！", "keywords": ["serve", "backhand"] },
      { "id": 3, "speaker": "Ryan", "avatar": "👦", "en": "Nice hit! Here comes a quick smash right over the net!", "zh": "擊得好！看我越過球網的迅猛扣殺！", "keywords": ["smash", "net", "hit"] },
      { "id": 4, "speaker": "Jenny", "avatar": "👧", "en": "Got it! Wow, that was an intense twenty-shot rally! My heart is pounding with excitement.", "zh": "接到了！哇，這波二十球來回對打太激烈了！我的心臟興奮得撲通撲通狂跳。", "keywords": ["intense", "rally", "pounding"] },
      { "id": 5, "speaker": "Ryan", "avatar": "👦", "en": "Exercising with good friends after school is the absolute best way to stay healthy and energetic.", "zh": "放學後跟好朋友一起盡情運動，絕對是維持健康與滿滿活力的最棒方式。", "keywords": ["exercising", "energetic", "healthy"] }
    ],
    "vocabulary": [
      { "word": "racket", "phonetic": "/ˈræk.ɪt/", "pos": "n.", "zh": "球拍", "example": "He re-strung his tennis racket before the tournament." },
      { "word": "smash", "phonetic": "/smæʃ/", "pos": "n./v.", "zh": "扣殺、猛力擊球", "example": "Her winning smash landed right on the baseline." },
      { "word": "rally", "phonetic": "/ˈræl.i/", "pos": "n.", "zh": "（球賽中）連續對打、來回對攻", "example": "Spectators gasped at the breathtaking thirty-shot rally." }
    ],
    "dailyPhrase": { "en": "You bet!", "zh": "那是當然！/ 一點也沒錯！" },
    "cultureTip": "羽毛球（Badminton）起源於英國伯明頓莊園，在亞洲尤其是台灣非常普及。羽毛球運動能同時訓練眼手協調、敏捷度與心肺耐力，是最受歡迎的全民運動之一。"
  },

  # 04-29 [國中挑戰]
  {
    "id": "dialogue-0429",
    "date": "04-29",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "春夜星空",
    "topic": {
      "en": "Spring Night Sky: Identifying the Big Dipper and Arcturus",
      "zh": "春季夜空觀星指南：尋找北斗七星與大角星的璀璨軌跡"
    },
    "situation": "春末晴朗無雲的涼爽夜晚，Tony 和 Clara 坐在學校操場看台上，拿著星圖認辨春季大三角與星座。",
    "speakers": {
      "Tony": { "role": "Tony", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Clara": { "role": "Clara", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0429.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tony", "avatar": "👦", "en": "Look up, Clara! The night sky is crystal clear tonight without a single cloud obstructing our view.", "zh": "Clara，抬頭看！今晚的夜空澄澈如水晶，連一朵遮擋視野的烏雲都沒有呢。", "keywords": ["crystal clear", "obstructing", "night sky"] },
      { "id": 2, "speaker": "Clara", "avatar": "👧", "en": "High overhead, the seven bright stars of the Big Dipper form a distinctive gigantic ladle shape.", "zh": "在頭頂正上方，北斗七星的七顆明亮恆星排列成一個醒目的巨大湯杓形狀。", "keywords": ["Big Dipper", "ladle", "overhead"] },
      { "id": 3, "speaker": "Tony", "avatar": "👦", "en": "Do you know how to find the Spring Great Arc? Follow the graceful curve of the ladle handle outwards.", "zh": "你知道怎麼找『春季大曲線』嗎？順著勺柄那條優雅的弧線向外延伸。", "keywords": ["Spring Great Arc", "ladle handle", "curve"] },
      { "id": 4, "speaker": "Clara", "avatar": "👧", "en": "Oh, it leads straight to that blazing orange-red star! That must be Arcturus in Boötes!", "zh": "哇，弧線筆直指引到那顆閃耀著橙紅色光芒的亮星！那一定就是牧夫座的大角星！", "keywords": ["Arcturus", "Boötes", "orange-red"] },
      { "id": 5, "speaker": "Tony", "avatar": "👦", "en": "Bingo! Continue the arc further down, and you will hit Spica, the blue-white diamond star in Virgo.", "zh": "答對了！順著弧線繼續往下延伸，你就會看見室女座如藍白鑽石般閃爍的角宿一星。", "keywords": ["Spica", "Virgo", "diamond"] },
      { "id": 6, "speaker": "Clara", "avatar": "👧", "en": "Tracing cosmic patterns in the celestial expanse makes our worldly troubles feel so insignificant.", "zh": "在浩瀚無垠的星空中描繪宇宙的軌跡，真的會讓我們平時世俗的煩惱顯得微不足道。", "keywords": ["celestial", "expanse", "insignificant"] }
    ],
    "vocabulary": [
      { "word": "ladle", "phonetic": "/ˈleɪ.dəl/", "pos": "n.", "zh": "長柄湯勺", "example": "The Big Dipper resembles a cosmic celestial ladle." },
      { "word": "celestial", "phonetic": "/səˈles.tʃəl/", "pos": "adj.", "zh": "天體的、天空的、宇宙神聖的", "example": "Astronomers study celestial bodies through optical telescopes." },
      { "word": "insignificant", "phonetic": "/ˌɪn.sɪɡˈnɪf.ə.kənt/", "pos": "adj.", "zh": "微不足道的、無關緊要的", "example": "Our personal worries seemed insignificant under the vast galaxy." }
    ],
    "dailyPhrase": { "en": "Crystal clear.", "zh": "如水晶般澄澈剔透、一清二楚。" },
    "cultureTip": "春季星空的代表就是「春季大曲線（Spring Great Arc）」：從北斗七星（Big Dipper）勺柄延伸，依序經過牧夫座「大角星（Arcturus）」與室女座「角宿一（Spica）」，再連到烏鴉座，是初學者必學的觀星口訣。"
  },

  # 04-30 [國小中高]
  {
    "id": "dialogue-0430",
    "date": "04-30",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "告別迎新",
    "topic": {
      "en": "Saying Goodbye to April: Welcoming the Vitality of May",
      "zh": "告別四月：迎向充滿生機與初夏微熱的五月"
    },
    "situation": "四月份的最後一天放學時刻，Eric 和 Mia 站在校門口的大榕樹下，回顧四月的收穫並期待初夏五月。",
    "speakers": {
      "Eric": { "role": "Eric", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0430.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Eric", "avatar": "👦", "en": "Can you believe today is already the last day of April, Mia? Time really flies!", "zh": "Mia，你能相信今天已經是四月的最後一天了嗎？時間過得真飛快！", "keywords": ["April", "time flies", "last day"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "It certainly does! We weathered our midterm exams and had so many fun outdoor adventures.", "zh": "真的！我們順利挺過了期中考試，也經歷了許多有趣的戶外冒險探索。", "keywords": ["weathered", "adventures", "midterms"] },
      { "id": 3, "speaker": "Eric", "avatar": "👦", "en": "The air already feels noticeably warmer, and cicadas will soon start singing in the trees.", "zh": "空氣已經能明顯感覺到溫暖微熱了，樹上的蟬鳴很快也要響起了呢。", "keywords": ["cicadas", "warmer", "singing"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "May will bring Mother's Day, vibrant dragon boat races preparations, and early summer vibes.", "zh": "五月將帶來溫馨的母親節、熱鬧的端午龍舟賽籌備，還有初夏明朗的氣息。", "keywords": ["dragon boat", "summer vibes", "Mother's Day"] },
      { "id": 5, "speaker": "Eric", "avatar": "👦", "en": "Farewell, gentle April! Let's greet sunny May with open arms and big smiles!", "zh": "再見了，溫柔的四月！讓我們張開雙臂與燦爛笑容，迎接陽光普照的五月吧！", "keywords": ["farewell", "greet", "smiles"] }
    ],
    "vocabulary": [
      { "word": "weather", "phonetic": "/ˈweð.ɚ/", "pos": "v.", "zh": "經受住、平安度過（考驗或風浪）", "example": "The resilient community weathered the fierce storm successfully." },
      { "word": "cicada", "phonetic": "/sɪˈkeɪ.də/", "pos": "n.", "zh": "蟬、知了", "example": "Loud buzzing cicadas signaled the arrival of hot summer." },
      { "word": "farewell", "phonetic": "/ˌferˈwel/", "pos": "n./int.", "zh": "告別、再會", "example": "They bade a fond farewell to their exchange students." }
    ],
    "dailyPhrase": { "en": "With open arms.", "zh": "熱情地、竭誠歡迎地。" },
    "cultureTip": "英語格言常說「April showers bring May flowers（四月微雨催開五月繁花）」，寓意暫時的困難與耕耘必將迎來美好豐碩的成果。四月終曲象徵暮春落幕與初夏起點。"
  }
]

def main():
    print(f"載入既有對話資料: {DATA_FILE}")
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        existing_data = json.load(f)

    existing_ids = {d['id'] for d in existing_data}
    print(f"目前對話篇數: {len(existing_data)}")

    # 檢查有無重複
    added_count = 0
    for d in APRIL_DIALOGUES:
        if d['id'] in existing_ids:
            print(f"警告: {d['id']} 已存在，覆蓋更新。")
            existing_data = [item if item['id'] != d['id'] else d for item in existing_data]
        else:
            existing_data.append(d)
            added_count += 1

    # 依月份及日期自然排序
    def sort_key(item):
        date_str = item.get('date', '00-00')
        return date_str

    existing_data.sort(key=sort_key)

    # 寫入 dialogues.json
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, indent=2)
    print(f"成功將 4 月份對話寫入 {DATA_FILE}！總篇數更新為: {len(existing_data)} (新增 {added_count} 篇)")

    # 同步更新 js/data.js
    with open(JS_FILE, 'w', encoding='utf-8') as f:
        f.write("// 365 每日生活美語對話資料庫 (全年度)\n")
        f.write("const DIALOGUES_DATA = ")
        f.write(json.dumps(existing_data, ensure_ascii=False, indent=2))
        f.write(";\n")
    print(f"成功同步更新 {JS_FILE}！")

if __name__ == '__main__':
    main()
