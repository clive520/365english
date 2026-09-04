#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次建立 8 月份生活對話 (08-01 至 08-31，共 31 篇)
這是全年度 365 天每日美語最後一個月份，達成 365 篇大滿貫！
涵蓋仲夏泳池、樹蔭野餐、夏季大三角、AI 大語言模型、自製雙色冰棒、立秋節氣、
88 父親節手作、沙灘漫步、七夕東方浪漫、指南針野營導航、國際青年日、英仙座流星雨、
美術館抽象畫、綠色隧道單車、沉沒成本謬誤、寵物夏日照護、世界攝影日、成長型思維、
香蕉馬芬烘焙、處暑節氣、數位極簡主義、開學作息調整、返校日、365 天大圓滿總結等豐富主題！
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'dialogues.json')
JS_FILE = os.path.join(BASE_DIR, 'js', 'data.js')

AUGUST_DIALOGUES = [
  # 08-01 [國小中高]
  {
    "id": "dialogue-0801",
    "date": "08-01",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "仲夏生活",
    "topic": {
      "en": "Welcoming August: Midsummer Cicadas and Pool Time",
      "zh": "迎接八月：仲夏的蟬鳴與盛夏游泳池時光"
    },
    "situation": "8月第一天陽光明媚，Kevin 和 Emma 帶著泳具來到社區戶外泳池，聽著響亮的蟬鳴享受清涼。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0801.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "👦", "en": "Can you believe it is already August, Emma? Summer is flying by so quickly!", "zh": "Emma，你能相信現在已經是八月了嗎？夏天過得真是太快了！", "keywords": ["August", "summer", "quickly"] },
      { "id": 2, "speaker": "Emma", "avatar": "👧", "en": "Listen to the cicadas buzzing loudly in the camphor trees. Today is definitely a perfect day for swimming.", "zh": "聽樟樹上蟬鳴得好大聲。今天絕對是去游泳的完美好天氣。", "keywords": ["cicadas", "buzzing", "swimming"] },
      { "id": 3, "speaker": "Kevin", "avatar": "👦", "en": "I brought my new goggles and kicking board. The water looks so crystal clear and inviting.", "zh": "我帶了我的新蛙鏡和打水浮板。池水看起來好清澈、好吸引人呀。", "keywords": ["goggles", "crystal clear", "inviting"] },
      { "id": 4, "speaker": "Emma", "avatar": "👧", "en": "Remember to do a five-minute dynamic stretch before jumping into the deep end.", "zh": "在跳進深水區之前，記得先做五分鐘的動態暖身操喔。", "keywords": ["dynamic", "stretch", "deep end"] },
      { "id": 5, "speaker": "Kevin", "avatar": "👦", "en": "Safety first! Let's dive in and cool off after we finish our stretches.", "zh": "安全第一！等做完熱身伸展，我們就跳進水裡清涼一下吧。", "keywords": ["safety first", "dive in", "cool off"] }
    ],
    "vocabulary": [
      { "word": "cicada", "phonetic": "/sɪˈkeɪ.də/", "pos": "n.", "zh": "蟬、知了", "example": "The loud song of cicadas filled the warm August afternoon." },
      { "word": "crystal clear", "phonetic": "/ˌkrɪs.təl ˈklɪr/", "pos": "adj.", "zh": "清澈見底的、晶瑩剔透的", "example": "The mountain lake was crystal clear and icy cool." },
      { "word": "dynamic", "phonetic": "/daɪˈnæm.ɪk/", "pos": "adj.", "zh": "充滿活力的、動態的", "example": "Dynamic warm-ups help prevent muscle cramps." }
    ],
    "dailyPhrase": { "en": "Cool off.", "zh": "消暑、降溫解熱。" },
    "cultureTip": "在美語日常中，「Fly by（時光飛逝）」常用來感嘆長假或美好時光過得特別快。八月（August）象徵仲夏時節（midsummer），也是歐美家庭進行戶外水上運動與海邊度假的高峰期。"
  },

  # 08-02 [國小初階]
  {
    "id": "dialogue-0802",
    "date": "08-02",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "戶外休閒",
    "topic": {
      "en": "Picnic Under the Oak Tree: Chilled Lemonade & Crackers",
      "zh": "樹蔭下的野餐：冰涼檸檬水與起司餅乾"
    },
    "situation": "午後微風徐徐，Toby 和 Mia 在大橡樹下鋪開野餐墊，分享自製的冰檸檬水與起司蘇打餅。",
    "speakers": {
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0802.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Toby", "avatar": "👦", "en": "This big oak tree gives us such cool shade, Mia.", "zh": "這棵大橡樹給了我們好涼爽的樹蔭喔，Mia。", "keywords": ["oak tree", "shade", "cool"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "I brought a thermos full of icy lemonade. Would you like a cup?", "zh": "我帶了一個裝滿冰檸檬水的保溫瓶。你要來一杯嗎？", "keywords": ["thermos", "lemonade", "cup"] },
      { "id": 3, "speaker": "Toby", "avatar": "👦", "en": "Yes, please! It tastes sweet and wonderfully sour.", "zh": "太好了，謝謝！喝起來甜甜酸酸的，好過癮。", "keywords": ["sweet", "sour", "wonderful"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "Here are some crunchy cheese crackers. Help yourself!", "zh": "這裡還有一些香脆的起司蘇打餅乾。自己拿不要客氣！", "keywords": ["crunchy", "cheese crackers", "help yourself"] },
      { "id": 5, "speaker": "Toby", "avatar": "👦", "en": "Sitting on the soft green grass is pure happiness.", "zh": "坐在柔軟的綠草地上真是單純而美好的幸福。", "keywords": ["grass", "happiness", "soft"] }
    ],
    "vocabulary": [
      { "word": "shade", "phonetic": "/ʃeɪd/", "pos": "n.", "zh": "陰涼處、樹蔭", "example": "We sat in the shade of a weeping willow." },
      { "word": "lemonade", "phonetic": "/ˌlem.əˈneɪd/", "pos": "n.", "zh": "檸檬水", "example": "Fresh lemonade with mint leaves tastes revitalizing." },
      { "word": "crunchy", "phonetic": "/ˈkrʌn.tʃi/", "pos": "adj.", "zh": "香脆的、酥脆可口的", "example": "These crackers stay wonderfully crunchy in the jar." }
    ],
    "dailyPhrase": { "en": "Help yourself!", "zh": "請自便！別客氣，盡情享用！" },
    "cultureTip": "「Help yourself!」是美語中非常熱情親切的待客用語，邀請朋友隨意享用桌上的茶點或飲料。炎炎夏日坐在綠蔭（in the shade）下野餐，是西方家庭最喜愛的週末微度假方式。"
  },

  # 08-03 [國中挑戰]
  {
    "id": "dialogue-0803",
    "date": "08-03",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#16a34a",
    "category": "天文科普",
    "topic": {
      "en": "Stargazing: Locating the Summer Triangle",
      "zh": "仲夏夜觀星：尋找夏季大三角（牛郎星、織女星與天津四）"
    },
    "situation": "晴朗無雲的八月夏夜，Leo 和 Zoe 拿著星圖手電筒在學校操場辨認著名的夏季大三角與銀河。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0803.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Look straight up near the zenith, Zoe. The brightest blue-white star right there is Vega in Lyra.", "zh": "Zoe，直直往天頂附近看。那顆最亮、閃爍藍白色光芒的恆星，就是天琴座的織女星。", "keywords": ["zenith", "brightest", "Vega"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "I see it! And down to the southeast across the faint Milky Way, that shining star must be Altair in Aquila.", "zh": "我看見了！往東南方跨過若隱若現的銀河，那顆明亮星星肯定就是天鷹座的牛郎星。", "keywords": ["Milky Way", "Altair", "southeast"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Exactly! Now spot Deneb at the tail of Cygnus the Swan, and you have connected the Summer Triangle.", "zh": "沒錯！現在只要再找出天鵝座尾巴的天津四，你就連成了著名的「夏季大三角」。", "keywords": ["Deneb", "Cygnus", "Summer Triangle"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "It forms a massive celestial landmark that guides sailors and astronomers across the night sky.", "zh": "它在夜空中形成了一個巨大的天體地標，指引著航海家與天文學家辨識夜空。", "keywords": ["celestial", "landmark", "astronomers"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "It is fascinating how ancient civilizations built entire mythologies around these same three stars.", "zh": "古老文明竟然能圍繞著這三顆星創造出豐富的神話傳說，實在太令人著迷了。", "keywords": ["civilizations", "mythologies", "fascinating"] }
    ],
    "vocabulary": [
      { "word": "zenith", "phonetic": "/ˈzen.ɪθ/", "pos": "n.", "zh": "天頂、最高點、頂點", "example": "The sun reached its scorching zenith at midday." },
      { "word": "celestial", "phonetic": "/sɪˈles.tʃəl/", "pos": "adj.", "zh": "天空的、天體的、神聖的", "example": "Comets are among the most spectacular celestial phenomena." },
      { "word": "mythology", "phonetic": "/mɪˈθɑː.lə.dʒi/", "pos": "n.", "zh": "神話學、神話傳說", "example": "Greek mythology explains constellations through heroic epics." }
    ],
    "dailyPhrase": { "en": "Connect the dots.", "zh": "連結點與點、融會貫通看出全貌。" },
    "cultureTip": "「Summer Triangle（夏季大三角）」由織女星（Vega）、牛郎星（Altair）與天津四（Deneb）組成。在東方文化中，牛郎織女隔著銀河（Milky Way）相望，構成了七夕情人節的浪漫傳奇；在西方天文中則是北半球夏季星空的指路座標。"
  },

  # 08-04 [高中進階]
  {
    "id": "dialogue-0804",
    "date": "08-04",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "人工智慧",
    "topic": {
      "en": "Artificial Intelligence: How LLMs Process Natural Language",
      "zh": "深度學習與科技前沿：大型語言模型如何理解人類語言？"
    },
    "situation": "高二的 Marcus 和 Chloe 在學校電腦教室討論自然語言處理與 Transformer 架構的運作原理。",
    "speakers": {
      "Marcus": { "role": "Marcus", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0804.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Marcus", "avatar": "👦", "en": "When people converse with modern generative AI, many assume the model possesses genuine consciousness and comprehension.", "zh": "當人們與現代生成式 AI 對話時，許多人總會誤以為模型擁有了真正的意識與理解力。", "keywords": ["generative AI", "consciousness", "comprehension"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "In reality, it is fundamentally an extraordinary statistical engine built upon the Transformer architecture and self-attention mechanisms.", "zh": "但事實上，它本質上是一個建構在 Transformer 架構與自注意力機制上的非凡統計預測引擎。", "keywords": ["statistical", "Transformer", "self-attention"] },
      { "id": 3, "speaker": "Marcus", "avatar": "👦", "en": "By converting text into high-dimensional vector embeddings, the model maps intricate semantic relationships across billions of parameters.", "zh": "藉由將文字轉化為高維度的向量嵌入（embeddings），模型在數十億個參數中精確捕捉複雜的語意關聯。", "keywords": ["embeddings", "high-dimensional", "semantic"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "It calculates the conditional probability of the next most plausible token given the preceding context, mimicking human eloquence.", "zh": "它根據前方的上下文情境計算出下一個最合理詞元（token）的條件機率，從而模擬出人類流暢的文采。", "keywords": ["conditional probability", "token", "mimicking"] },
      { "id": 5, "speaker": "Marcus", "avatar": "👦", "en": "Understanding this demystifies the technology. AI is not magic; it is mathematics, computer science, and monumental computational scale.", "zh": "理解這一點揭開了技術的神秘面紗。人工智慧不是魔法；它是數學、電腦科學與龐大運算規模的結晶。", "keywords": ["demystifies", "computational", "monumental"] }
    ],
    "vocabulary": [
      { "word": "comprehension", "phonetic": "/ˌkɑːm.prəˈhen.ʃən/", "pos": "n.", "zh": "理解力、領悟力", "example": "Reading comprehension requires evaluating underlying themes." },
      { "word": "semantic", "phonetic": "/səˈmæn.tɪk/", "pos": "adj.", "zh": "語意的、語意學的", "example": "Search engines use semantic analysis to grasp user intent." },
      { "word": "demystify", "phonetic": "/ˌdiːˈmɪs.tə.faɪ/", "pos": "v.", "zh": "使非神秘化、澄清、闡明", "example": "The science documentary helped demystify quantum physics." }
    ],
    "dailyPhrase": { "en": "Demystify a concept.", "zh": "撥開迷霧、深入淺出地解釋概念。" },
    "cultureTip": "自 2017 年 Google 發布論文《Attention Is All You Need》以來，Transformer 架構已徹底重塑自然語言處理（NLP）。理解「Next-token prediction（下一個詞元預測）」能幫助青年學子具備正確的科技素養，避免過度擬人化（anthropomorphism）。"
  },

  # 08-05 [國小初階]
  {
    "id": "dialogue-0805",
    "date": "08-05",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "生活美食",
    "topic": {
      "en": "At the Supermarket: Choosing Ice Cream Flavors",
      "zh": "去超市買冰淇淋：香草、草莓還是巧克力？"
    },
    "situation": "夏日午後，Ben 和 Lily 站在超市冰品冷凍櫃前，熱烈挑選各自最喜愛的冰淇淋口味。",
    "speakers": {
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Lily": { "role": "Lily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0805.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ben", "avatar": "👦", "en": "Look at all these colorful ice cream tubs, Lily! Which flavor do you want?", "zh": "Lily，你看這些五顏六色的冰淇淋桶！你想要哪一種口味？", "keywords": ["ice cream", "colorful", "flavor"] },
      { "id": 2, "speaker": "Lily", "avatar": "👧", "en": "I love sweet pink strawberry with real fruit chunks inside.", "zh": "我最喜歡甜甜的粉紅色草莓口味，裡面還有真正的水果顆粒呢。", "keywords": ["strawberry", "fruit chunks", "sweet"] },
      { "id": 3, "speaker": "Ben", "avatar": "👦", "en": "I am torn between dark chocolate fudge and classic vanilla bean.", "zh": "我在濃郁黑巧克力軟糖口味和經典香草籽口味之間好猶豫喔。", "keywords": ["dark chocolate", "vanilla bean", "torn"] },
      { "id": 4, "speaker": "Lily", "avatar": "👧", "en": "Why not get the Neapolitan tub? It combines chocolate, vanilla, and strawberry all in one!", "zh": "為什麼不買拿坡里三色冰淇淋呢？它把巧克力、香草和草莓三合一結合在一起喔！", "keywords": ["Neapolitan", "combines", "all in one"] },
      { "id": 5, "speaker": "Ben", "avatar": "👦", "en": "That is a brilliant idea! Best of all three worlds.", "zh": "這點子真是太聰明了！三個願望一次滿足。", "keywords": ["brilliant", "three worlds", "idea"] }
    ],
    "vocabulary": [
      { "word": "flavor", "phonetic": "/ˈfleɪ.vɚ/", "pos": "n.", "zh": "風味、口味", "example": "Mango is my absolute favorite summer ice cream flavor." },
      { "word": "vanilla", "phonetic": "/vəˈnɪl.ə/", "pos": "n.", "zh": "香草", "example": "Pure vanilla extract adds warmth to sweet cookies." },
      { "word": "brilliant", "phonetic": "/ˈbrɪl.jənt/", "pos": "adj.", "zh": "極好的、絕妙的、明亮的", "example": "She came up with a brilliant plan for the talent show." }
    ],
    "dailyPhrase": { "en": "Be torn between two things.", "zh": "在兩者之間左右為難、難以取捨。" },
    "cultureTip": "「Neapolitan ice cream（拿坡里三色冰淇淋）」起源於 19 世紀義大利移民傳入美國，由香草、巧克力與草莓三種經典口味平分裝在同一盒中，是美式家庭聚會中皆大歡喜的代表甜點。"
  },

  # 08-06 [國小中高]
  {
    "id": "dialogue-0806",
    "date": "08-06",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "廚房手作",
    "topic": {
      "en": "DIY Summer Fruit Popsicles: Mango Yogurt & Blueberry",
      "zh": "夏日自製水果冰棒：芒果優格與藍莓雙色冰棒"
    },
    "situation": "週末上午，Mia 和 Alex 在廚房動手攪拌新鮮芒果泥與優格，倒入矽膠模具製作健康的雙色水果冰棒。",
    "speakers": {
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Alex": { "role": "Alex", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0806.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mia", "avatar": "👧", "en": "Store-bought popsicles often have too much artificial food coloring and added sugar.", "zh": "市售的冰棒常常含有太多人工色素和多餘的添加糖分。", "keywords": ["popsicles", "coloring", "sugar"] },
      { "id": 2, "speaker": "Alex", "avatar": "👦", "en": "Let's make our own all-natural version using fresh mango puree and creamy Greek yogurt.", "zh": "我們用新鮮的芒果泥和濃醇的希臘優格，自己動手做純天然版本吧。", "keywords": ["all-natural", "puree", "Greek yogurt"] },
      { "id": 3, "speaker": "Mia", "avatar": "👧", "en": "First, we pour the golden mango layer into the silicone molds and drop in plump blueberries.", "zh": "首先，我們把金黃色的芒果層倒入矽膠模具中，再放進幾顆圓滾滾的藍莓。", "keywords": ["silicone molds", "blueberries", "plump"] },
      { "id": 4, "speaker": "Alex", "avatar": "👦", "en": "Then we top it with honey-sweetened yogurt and gently insert wooden popsicle sticks.", "zh": "接著我們淋上一層加入蜂蜜的優格，並輕輕插上木製冰棒棍。", "keywords": ["honey-sweetened", "wooden sticks", "insert"] },
      { "id": 5, "speaker": "Mia", "avatar": "👧", "en": "Four hours in the freezer, and we will enjoy refreshing, guilt-free frozen popsicles!", "zh": "放進冷凍庫四個小時後，我們就能享用清爽又無負擔的雙色冰棒了！", "keywords": ["freezer", "guilt-free", "refreshing"] }
    ],
    "vocabulary": [
      { "word": "puree", "phonetic": "/pjʊˈreɪ/", "pos": "n.", "zh": "濃泥、果泥", "example": "Baby food made from fresh apple puree is gentle and nutritious." },
      { "word": "silicone", "phonetic": "/ˈsɪl.ə.koʊn/", "pos": "n.", "zh": "矽膠", "example": "Silicone baking mats are flexible and heat-resistant." },
      { "word": "guilt-free", "phonetic": "/ˌɡɪltˈfriː/", "pos": "adj.", "zh": "無罪惡感的、無健康負擔的", "example": "Fresh fruit smoothies provide a guilt-free sweet treat." }
    ],
    "dailyPhrase": { "en": "Guilt-free pleasure.", "zh": "毫無罪惡感的健康樂事。" },
    "cultureTip": "自製冰品（DIY Popsicles）在歐美家庭十分盛行。家長常鼓勵孩童使用希臘優格（Greek yogurt）與當季水果製作無添加（clean eating）小點心，既能避暑消熱，又能培養動手自煮能力。"
  },

  # 08-07 [國中挑戰]
  {
    "id": "dialogue-0807",
    "date": "08-07",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#16a34a",
    "category": "傳統節氣",
    "topic": {
      "en": "Liqiu Solar Term: The Arrival of Autumn & Traditional Wisdom",
      "zh": "立秋節氣：涼風至、白露降與古人對節氣轉折的智慧"
    },
    "situation": "8月7日立秋節氣，Brian 和 Amy 在庭院品嘗西瓜，探討立秋「貼秋膘」與「啃秋」的傳統智慧。",
    "speakers": {
      "Brian": { "role": "Brian", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Amy": { "role": "Amy", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0807.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Brian", "avatar": "👦", "en": "Today marks Liqiu, the thirteenth solar term signifying the beginning of astronomical autumn.", "zh": "今天是立秋，第十三個節氣，象徵天文意義上秋季的開端。", "keywords": ["Liqiu", "thirteenth", "astronomical"] },
      { "id": 2, "speaker": "Amy", "avatar": "👧", "en": "Even though midday is still blazing hot, early morning breezes are already noticeably gentler.", "zh": "雖然正中午依然艷陽高照，但清晨微風吹拂時已經明顯感覺柔和了許多。", "keywords": ["blazing", "breezes", "noticeably"] },
      { "id": 3, "speaker": "Brian", "avatar": "👦", "en": "Ancient folks practiced 'biting autumn' by eating watermelon to ward off seasonal malaria and digestive ailments.", "zh": "古人有「啃秋」的習俗，藉由吃西瓜來預防換季的瘧疾與腸胃不適。", "keywords": ["biting autumn", "ward off", "digestive"] },
      { "id": 4, "speaker": "Amy", "avatar": "👧", "en": "They also weighed family members to see if they lost weight during the scorching summer, calling it 'fleshing out in autumn.'", "zh": "他們還會幫家人稱體重，看看夏天有沒有消瘦，這就是所謂的『貼秋膘』補身呢。", "keywords": ["weighed", "scorching", "fleshing out"] },
      { "id": 5, "speaker": "Brian", "avatar": "👦", "en": "Nature shifts subtly. It reminds us that after strenuous exertion, autumn is a season for gathering and reflection.", "zh": "大自然悄悄轉換節奏。這提醒我們，在夏天的全力揮灑之後，秋天是收穫與沉澱的季節。", "keywords": ["shifts subtly", "strenuous", "reflection"] }
    ],
    "vocabulary": [
      { "word": "signify", "phonetic": "/ˈsɪɡ.nə.faɪ/", "pos": "v.", "zh": "象徵、意味著、預示", "example": "Dark gray storm clouds signify impending heavy showers." },
      { "word": "ward off", "phonetic": "/wɔːrd ɑːf/", "pos": "phr.", "zh": "避開、擋開、防止", "example": "Drinking warm lemon tea helps ward off common colds." },
      { "word": "strenuous", "phonetic": "/ˈstren.ju.əs/", "pos": "adj.", "zh": "費力的、繁重的、竭盡全力的", "example": "Avoid strenuous endurance workouts during peak afternoon heat." }
    ],
    "dailyPhrase": { "en": "A subtle shift in seasons.", "zh": "四季更迭中微妙的轉換。" },
    "cultureTip": "「Liqiu（立秋）」通常在陽曆 8 月 7 日至 9 日之間交節。民間有「秋後有一伏」與「秋老虎（Indian summer）」之說，雖然進入立秋，但真正的涼爽通常要等到處暑之後。古人藉「啃秋」吃瓜咬住秋意，祈求五穀豐登。"
  },

  # 08-08 [國小中高]
  {
    "id": "dialogue-0808",
    "date": "08-08",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "家庭感恩",
    "topic": {
      "en": "Father's Day in Taiwan: Crafting Handmade Cards for Dad",
      "zh": "88 父親節快樂：手作創意刮鬍刀造型賀卡與說出心中的感謝"
    },
    "situation": "8月8日父親節前夕，Kevin 和 Emma 用彩色卡紙和鈕扣製作立體西裝領結賀卡，感謝爸爸平日的辛勤付出。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0808.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "👦", "en": "In Taiwan, August eighth sounds like 'ba-ba,' which is why we celebrate Father's Day today!", "zh": "在台灣，八月八日的諧音聽起來就像『爸爸』，這就是為什麼我們在今天慶祝父親節！", "keywords": ["August eighth", "sounds like", "Father's Day"] },
      { "id": 2, "speaker": "Emma", "avatar": "👧", "en": "I folded a navy blue card into a formal suit with an origami necktie and tiny wooden buttons.", "zh": "我把深藍色厚紙卡折成一套正式西裝，還配上了摺紙領帶和迷你小木鈕扣呢。", "keywords": ["formal suit", "origami", "necktie"] },
      { "id": 3, "speaker": "Kevin", "avatar": "👦", "en": "That looks so classy! What did you write on the inside flap?", "zh": "看起來好有質感喔！你在卡片內頁寫了些什麼呢？", "keywords": ["classy", "inside flap", "write"] },
      { "id": 4, "speaker": "Emma", "avatar": "👧", "en": "I wrote: 'Thank you Dad for always being my pillar of strength and driving me to soccer practice.'", "zh": "我寫著：『謝謝爸爸永遠是我最強大的支柱，每次都載我風雨無阻去足球練球。』", "keywords": ["pillar of strength", "soccer practice", "driving"] },
      { "id": 5, "speaker": "Kevin", "avatar": "👦", "en": "Dad works so hard year-round. Tonight, dinner and clean dishes are totally on us!", "zh": "爸爸一整年工作好辛勞。今晚的端菜和洗碗就徹底包在我們身上吧！", "keywords": ["year-round", "clean dishes", "on us"] }
    ],
    "vocabulary": [
      { "word": "origami", "phonetic": "/ˌɔːr.əˈɡɑː.mi/", "pos": "n.", "zh": "摺紙藝術", "example": "She folded an origami crane as a symbol of peace." },
      { "word": "classy", "phonetic": "/ˈklæs.i/", "pos": "adj.", "zh": "優雅有品味的、高雅的", "example": "The hotel lobby features classy marble flooring." },
      { "word": "pillar", "phonetic": "/ˈpɪl.ɚ/", "pos": "n.", "zh": "支柱、棟樑、頂樑柱", "example": "Grandmother has always been the emotional pillar of our family." }
    ],
    "dailyPhrase": { "en": "A pillar of strength.", "zh": "堅強的支柱、屹立不搖的後盾。" },
    "cultureTip": "許多西方國家的父親節在六月的第三個星期日，而台灣則因為「88」音同「爸爸」，於 1945 年正式將 8 月 8 日訂為父親節。向默默守護家庭的父親表達感恩（gratitude），是跨文化共通的溫情價值。"
  },

  # 08-09 [國小初階]
  {
    "id": "dialogue-0809",
    "date": "08-09",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "海洋探索",
    "topic": {
      "en": "Strolling on the Beach: Collecting Seashells & Watching Crabs",
      "zh": "與家人去沙灘散步：撿拾五彩貝殼與看螃蟹橫著走"
    },
    "situation": "傍晚海風清涼，Leo 和 Mia 在退潮後的沙灘上漫步，觀察小沙蟹在沙灘上快步疾走。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0809.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "The wet sand feels squishy and cool under our bare feet, Mia.", "zh": "Mia，濕濕的沙子踩在光溜溜的腳底板下，感覺軟軟涼涼的。", "keywords": ["wet sand", "squishy", "bare feet"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "Look! That tiny hermit crab is carrying a shiny spiral shell on its back.", "zh": "你看！那隻小寄居蟹背上正背著一個閃亮亮的螺旋小貝殼呢。", "keywords": ["hermit crab", "spiral shell", "shiny"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Over by the rocks, ghost crabs are scurrying sideways into their deep burrows.", "zh": "在礁石那邊，好多隻沙蟹正橫著飛快鑽進牠們深深的洞穴裡。", "keywords": ["ghost crabs", "scurrying", "sideways"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "I found a smooth purple clam shell. Should we take it home?", "zh": "我找到了一個光滑的紫色蛤蜊貝殼。我們要帶它回家嗎？", "keywords": ["smooth", "clam shell", "take home"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Let's leave it on the beach. Little ocean creatures might need it for a cozy home!", "zh": "我們把它留在沙灘上吧。海洋小生物可能需要它來當溫暖的小家呢！", "keywords": ["leave it", "ocean creatures", "cozy home"] }
    ],
    "vocabulary": [
      { "word": "squishy", "phonetic": "/ˈskwɪʃ.i/", "pos": "adj.", "zh": "濕軟的、黏軟舒適的", "example": "The muddy grass was squishy after the heavy shower." },
      { "word": "spiral", "phonetic": "/ˈspaɪr.əl/", "pos": "adj./n.", "zh": "螺旋形的、螺線", "example": "The lighthouse has a narrow spiral staircase leading to the lantern." },
      { "word": "scurry", "phonetic": "/ˈskɝː.i/", "pos": "v.", "zh": "快步急跑、倉皇疾走", "example": "Little mice scurried across the barn floor." }
    ],
    "dailyPhrase": { "en": "Take only pictures, leave only footprints.", "zh": "只留腳印，只帶走照片。" },
    "cultureTip": "「Leave No Trace（無痕山林/海洋）」守則鼓勵大家在海邊漫步時，不隨意帶走貝殼（seashells）或寄居蟹（hermit crabs），因為空貝殼是海洋寄居蟹賴以生存的天然避難所。"
  },

  # 08-10 [高中進階]
  {
    "id": "dialogue-0810",
    "date": "08-10",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "民俗神話",
    "topic": {
      "en": "Qixi Festival: The Cowherd, Weaver Girl & Eastern Romance",
      "zh": "七夕情人節與織女傳說：從東方神話到當代情感連結"
    },
    "situation": "農曆七月初七七夕節，Ethan 和 Hannah 漫步在古色古香的街頭，思索傳統民間神話與現代人對真摯情感的嚮往。",
    "speakers": {
      "Ethan": { "role": "Ethan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Hannah": { "role": "Hannah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0810.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ethan", "avatar": "👦", "en": "Tonight is the Double Seventh Festival, celebrated for over two millennia as Eastern Valentine's Day.", "zh": "今晚是七夕節，兩千多年來被譽為東方的傳統情人節。", "keywords": ["Double Seventh", "millennia", "Valentine's Day"] },
      { "id": 2, "speaker": "Hannah", "avatar": "👧", "en": "The folklore of Niulang and Zhinü meeting once a year across the bridge of magpies resonates with timeless poetic melancholy.", "zh": "牛郎與織女每年在喜鵲搭成的鵲橋上相會一次的民間傳說，洋溢著歷久彌新的詩意與深情哀愁。", "keywords": ["Niulang and Zhinü", "magpies", "melancholy"] },
      { "id": 3, "speaker": "Ethan", "avatar": "👦", "en": "Originally, it was called the Festival to Plead for Skills, where young women prayed for dexterity in weaving and embroidery.", "zh": "它最早被稱為『乞巧節』，年輕女子會在當夜向織女祈求心靈手巧、精通刺繡與織布女紅。", "keywords": ["dexterity", "weaving", "embroidery"] },
      { "id": 4, "speaker": "Hannah", "avatar": "👧", "en": "In our hyper-connected modern era of instant messaging, the patience and steadfast loyalty depicted in the legend feel remarkably rare.", "zh": "在我們即時通訊發達的現代社會裡，傳說中所描繪的那種默默等待與堅定守候，顯得格外彌足珍貴。", "keywords": ["hyper-connected", "steadfast", "remarkable"] },
      { "id": 5, "speaker": "Ethan", "avatar": "👦", "en": "True devotion transcends physical proximity. Distance cannot diminish genuine resonance between two souls.", "zh": "真正的深情超越了物理空間的距離。相隔再遠，也無法沖淡心靈之間的真正共鳴。", "keywords": ["proximity", "resonance", "devotion"] }
    ],
    "vocabulary": [
      { "word": "folklore", "phonetic": "/ˈfoʊk.lɔːr/", "pos": "n.", "zh": "民間傳說、民俗學", "example": "Irish folklore is populated with mischievous fairies and leprechauns." },
      { "word": "dexterity", "phonetic": "/dekˈster.ə.t̬i/", "pos": "n.", "zh": "手巧、靈巧、俐落", "example": "The pianist demonstrated extraordinary manual dexterity." },
      { "word": "steadfast", "phonetic": "/ˈsted.fæst/", "pos": "adj.", "zh": "堅定不移的、牢固的", "example": "Her steadfast dedication inspired the whole non-profit organization." }
    ],
    "dailyPhrase": { "en": "Transcend physical distance.", "zh": "跨越物理距離、心靈相通。" },
    "cultureTip": "七夕節（Qixi Festival / Double Seventh）源於漢代，除了情侶互致情意，古代傳統更重「乞巧」——祈求智巧與好手藝。宋代詞人秦觀名句「兩情若是久長時，又豈在朝朝暮暮」，正是這份超越時空深情的美學體現。"
  },

  # 08-11 [國中挑戰]
  {
    "id": "dialogue-0811",
    "date": "08-11",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#16a34a",
    "category": "野外求生",
    "topic": {
      "en": "Summer Camping Skills: Mastering Compass & Topographic Maps",
      "zh": "盛夏戶外野營：學會使用指南針與看懂等高線地圖"
    },
    "situation": "童軍野營課上，Brian 和 Amy 展開地圖與指南針，練習如何在沒有手機訊號的山林中進行方位定向。",
    "speakers": {
      "Brian": { "role": "Brian", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Amy": { "role": "Amy", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0811.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Brian", "avatar": "👦", "en": "When hiking in remote wilderness, we cannot rely solely on smartphones since phone batteries die and cellular signals vanish.", "zh": "在偏遠荒野健行時，我們絕不能單靠智慧型手機，因為電池會耗盡、手機訊號也會消失。", "keywords": ["wilderness", "batteries", "cellular signals"] },
      { "id": 2, "speaker": "Amy", "avatar": "👧", "en": "That is why traditional orienteering skills with a baseplate compass and a paper topographic map are essential.", "zh": "這就是為什麼使用定向指南針與紙本等高線地圖的傳統野外定位技能無可取代。", "keywords": ["orienteering", "baseplate compass", "topographic"] },
      { "id": 3, "speaker": "Brian", "avatar": "👦", "en": "See how closely spaced these brown contour lines are? That indicates a very steep ridge directly ahead.", "zh": "你看這些棕色的等高線排列得有多緊密？這表示正前方是一座非常陡峭的山脊。", "keywords": ["contour lines", "steep ridge", "indicates"] },
      { "id": 4, "speaker": "Amy", "avatar": "👧", "en": "And when lines spread widely apart, it represents a relatively flat valley where we can safely pitch our tents.", "zh": "而當線條間距拉得很開時，代表那是一片相對平坦的山谷，我們可以安全搭帳篷。", "keywords": ["spread apart", "flat valley", "pitch tents"] },
      { "id": 5, "speaker": "Brian", "avatar": "👦", "en": "Align the magnetic needle with the orienting arrow, and we will never lose our way!", "zh": "把磁針與定向箭頭對齊，我們就絕對不會在山林中迷失方向！", "keywords": ["magnetic needle", "orienting arrow", "lose our way"] }
    ],
    "vocabulary": [
      { "word": "wilderness", "phonetic": "/ˈwɪl.dɚ.nəs/", "pos": "n.", "zh": "荒野、荒原", "example": "The national park preserves untouched alpine wilderness." },
      { "word": "topographic", "phonetic": "/ˌtɑː.pəˈɡræf.ɪk/", "pos": "adj.", "zh": "地形學的、地形圖的", "example": "Topographic surveys illustrate elevation variations clearly." },
      { "word": "contour", "phonetic": "/ˈkɑːn.tʊr/", "pos": "n.", "zh": "等高線、輪廓", "example": "Dense contour lines warn hikers of precipitous cliffs." }
    ],
    "dailyPhrase": { "en": "Find one's bearings.", "zh": "認清方位、弄清局勢。" },
    "cultureTip": "「Orienteering（定向越野）」源於 19 世紀末的北歐軍事訓練，結合了越野跑步與識圖定向能力。掌握等高線（contour lines）與指南針判定，是戶外愛好者進入大自然必備的生命安全防線。"
  },

  # 08-12 [高中進階]
  {
    "id": "dialogue-0812",
    "date": "08-12",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "全球公民",
    "topic": {
      "en": "International Youth Day: Youth Civic Engagement & Climate Action",
      "zh": "國際青年日：青年如何參與社區治理與氣候永續倡議"
    },
    "situation": "8月12日國際青年日，高三學生 Marcus 和 Chloe 籌備一場校際永續論壇，探討青年推動社會實質變革的動能。",
    "speakers": {
      "Marcus": { "role": "Marcus", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0812.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Marcus", "avatar": "👦", "en": "August twelfth is designated by the United Nations as International Youth Day, celebrating young people as catalysts for positive change.", "zh": "八月十二日被聯合國定為國際青年日，表彰青年作為推動社會正面變革的重要催化劑。", "keywords": ["International Youth Day", "United Nations", "catalysts"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "Too often, teenagers are patronized as mere beneficiaries of policy rather than active co-creators of our collective future.", "zh": "以往青少年常被當作政策的被動受益者，而非共同塑造集體未來的積極創造者。", "keywords": ["patronized", "beneficiaries", "co-creators"] },
      { "id": 3, "speaker": "Marcus", "avatar": "👦", "en": "From grassroots climate strikes to community food audits, young leaders consistently display remarkable moral clarity and innovation.", "zh": "從草根氣候倡議到社區剩食稽核，年輕領袖持續展現出非凡的道德洞察力與創新能力。", "keywords": ["grassroots", "audits", "moral clarity"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "Our upcoming youth summit isn't just about sounding idealistic alarms; it provides actionable roadmaps for municipal composting and solar adoption.", "zh": "我們即將舉辦的青年峰會不只是空喊崇高口號，而是為市鎮堆肥與太陽能普及提供具體可行的實踐藍圖。", "keywords": ["idealistic", "actionable", "roadmaps"] },
      { "id": 5, "speaker": "Marcus", "avatar": "👦", "en": "Youth is not an age of passive observation. It is an extraordinary superpower of audacity and constructive idealism.", "zh": "青年絕非被動旁觀的年紀。它是勇敢無畏與建設性理想主義所匯聚的非凡超能力。", "keywords": ["observation", "audacity", "idealism"] }
    ],
    "vocabulary": [
      { "word": "catalyst", "phonetic": "/ˈkæt̬.əl.ɪst/", "pos": "n.", "zh": "催化劑、促成變革的力量", "example": "The passionate youth activist served as a catalyst for environmental reform." },
      { "word": "patronize", "phonetic": "/ˈpeɪ.trə.naɪz/", "pos": "v.", "zh": "以居高臨下的態度對待、自以為高人一等", "example": "Do not patronize young apprentices; respect their fresh insights." },
      { "word": "audacity", "phonetic": "/ɑːˈdæs.ə.t̬i/", "pos": "n.", "zh": "大膽、勇氣、果敢無畏", "example": "They had the audacity to challenge long-standing corporate monopolies." }
    ],
    "dailyPhrase": { "en": "A catalyst for change.", "zh": "引領變革的關鍵催化劑。" },
    "cultureTip": "聯合國自 1999 年起將每年 8 月 12 日訂為「International Youth Day（國際青年日）」。每年皆有特定全球主題（如綠色技能、跨世代團結），鼓勵全球青年跨越年齡藩籬，主動參與公共事務與氣候行動。"
  },

  # 08-13 [國小初階]
  {
    "id": "dialogue-0813",
    "date": "08-13",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "天文奇觀",
    "topic": {
      "en": "The Perseid Meteor Shower: Making Wishes on Shooting Stars",
      "zh": "英仙座流星雨：仰望夜空許下三個願望"
    },
    "situation": "8月中旬深夜，Ben 和 Lily 躺在頂樓陽台的地毯上，等待著名的英仙座流星雨劃過天際。",
    "speakers": {
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Lily": { "role": "Lily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0813.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ben", "avatar": "👦", "en": "Keep your eyes on the northeastern sky, Lily. The meteor shower peaks tonight!", "zh": "Lily，眼睛盯著東北方的天空喔。流星雨今晚達到極大期！", "keywords": ["northeastern", "meteor shower", "peaks"] },
      { "id": 2, "speaker": "Lily", "avatar": "👧", "en": "Whoa! Did you see that green streak of light? It vanished in a split second!", "zh": "哇！你有看到剛才那道綠色的光芒嗎？一瞬間就消失了！", "keywords": ["green streak", "vanished", "split second"] },
      { "id": 3, "speaker": "Ben", "avatar": "👦", "en": "Yes! That was a shooting star! Quick, close your eyes and make a wish.", "zh": "有！那就是一顆流星！快，閉上眼睛許願。", "keywords": ["shooting star", "make a wish", "close eyes"] },
      { "id": 4, "speaker": "Lily", "avatar": "👧", "en": "I wished for my family to stay healthy, and for us to get an adorable puppy.", "zh": "我許了希望全家人身體健康，還有我們能養一隻可愛的小狗狗。", "keywords": ["healthy", "adorable puppy", "wished"] },
      { "id": 5, "speaker": "Ben", "avatar": "👦", "en": "There goes another bright one! Tonight's night sky is putting on a magical show.", "zh": "又來一顆好亮的！今晚的夜空正在上演一場魔法大秀呢。", "keywords": ["bright", "magical show", "night sky"] }
    ],
    "vocabulary": [
      { "word": "meteor", "phonetic": "/ˈmiː.t̬i.ɔːr/", "pos": "n.", "zh": "流星、隕星", "example": "A blazing meteor streak illuminated the midnight meadow." },
      { "word": "streak", "phonetic": "/striːk/", "pos": "n.", "zh": "條紋、一道光線、疾行", "example": "A golden streak of sunrise touched the mountain peaks." },
      { "word": "split second", "phonetic": "/ˌsplɪt ˈsek.ənd/", "pos": "n.", "zh": "一剎那、千分之一秒", "example": "In a split second, the goalie leaped and blocked the ball." }
    ],
    "dailyPhrase": { "en": "Make a wish on a shooting star.", "zh": "對著流星許願。" },
    "cultureTip": "「Perseid Meteor Shower（英仙座流星雨）」是北半球每年八月中旬（通常為 8 月 12-13 日）最壯觀的天象之一，每小時常可見數十顆至上百顆流星。西方民間深信對著劃過夜空的流星（shooting star）許願，願望就會實現。"
  },

  # 08-14 [國小中高]
  {
    "id": "dialogue-0814",
    "date": "08-14",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "藝文美育",
    "topic": {
      "en": "Visiting Modern Art Museum: Imagination in Front of Abstract Art",
      "zh": "參觀現代美術館：在抽象畫前發揮想像力"
    },
    "situation": "夏日週末，Emma 和 Kevin 參觀市立當代美術館，站在巨幅色彩鮮艷的抽象畫作前分享各自看見的奇妙意象。",
    "speakers": {
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Kevin": { "role": "Kevin", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0814.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Emma", "avatar": "👧", "en": "Look at this massive canvas, Kevin. It is filled with bold splashes of red, yellow, and deep ultramarine.", "zh": "Kevin，你看這幅好大的畫布。上面滿滿都是大膽的紅、黃和深群青色塊飛濺。", "keywords": ["canvas", "splashes", "ultramarine"] },
      { "id": 2, "speaker": "Kevin", "avatar": "👦", "en": "At first glance, it looks like spilled paint. What do you think the artist wanted to portray?", "zh": "第一眼看過去，好像不小心打翻顏料一樣。你覺得畫家到底想描繪什麼呢？", "keywords": ["first glance", "spilled paint", "portray"] },
      { "id": 3, "speaker": "Emma", "avatar": "👧", "en": "To me, it looks like a stormy ocean colliding with a fiery sunset over volcanic islands.", "zh": "對我來說，它看起來就像暴風雨中的大海與火山島上烈火般的夕陽劇烈碰撞。", "keywords": ["colliding", "volcanic", "sunset"] },
      { "id": 4, "speaker": "Kevin", "avatar": "👦", "en": "That is fascinating! I see bustling city streetlights reflecting in puddles during a torrential downpour.", "zh": "太神奇了！我看到的卻是大暴雨中，城市繁華街燈倒映在水坑裡的閃爍倒影。", "keywords": ["bustling", "reflecting", "downpour"] },
      { "id": 5, "speaker": "Emma", "avatar": "👧", "en": "That is the magic of abstract art. There are no wrong answers, only boundless imagination.", "zh": "這就是抽象藝術的魔力。沒有標準答案，只有無限奔馳的想像力。", "keywords": ["magic", "abstract art", "boundless"] }
    ],
    "vocabulary": [
      { "word": "canvas", "phonetic": "/ˈkæn.vəs/", "pos": "n.", "zh": "畫布、帆布", "example": "The artist spread white gesso across the raw canvas." },
      { "word": "portray", "phonetic": "/pɔːrˈtreɪ/", "pos": "v.", "zh": "描繪、刻畫、表現", "example": "The documentary faithfully portrays the struggles of frontline workers." },
      { "word": "boundless", "phonetic": "/ˈbaʊnd.ləs/", "pos": "adj.", "zh": "無窮的、無限的、無邊無際的", "example": "Children possess boundless curiosity about the natural world." }
    ],
    "dailyPhrase": { "en": "At first glance.", "zh": "乍看之下、第一眼看來。" },
    "cultureTip": "「Abstract Art（抽象藝術）」不拘泥於重現客觀物體的真實外形，而是透過點、線、面與色彩的情感張力引導觀者共情。參觀美術館（museum etiquette）時，鼓勵孩子發表個人觀點，是培養批判思考與美學素養極佳的方式。"
  },

  # 08-15 [國中挑戰]
  {
    "id": "dialogue-0815",
    "date": "08-15",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#16a34a",
    "category": "戶外休閒",
    "topic": {
      "en": "Cycling Through the Tree-Canopied Green Tunnel",
      "zh": "盛夏騎行綠色隧道：享受林蔭微風與低碳環保"
    },
    "situation": "八月中旬涼爽的早晨，Leo 和 Zoe 騎著變速單車穿行在鄉間綠蔭成蔭的樟樹綠色隧道中。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0815.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Riding underneath these century-old camphor trees feels like entering a naturally air-conditioned oasis.", "zh": "騎在這些百年樟樹下，感覺就像走進了一座自帶天然冷氣的世外綠洲。", "keywords": ["century-old", "air-conditioned", "oasis"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "The intertwined branches form a dense leafy canopy, filtering the harsh sunlight into dancing dappled shadows.", "zh": "交錯的枝椏形成了茂密的樹冠層，把刺眼的陽光過濾成地上跳躍的斑駁光影。", "keywords": ["intertwined", "leafy canopy", "dappled shadows"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Switch your gear to a lower resistance, Zoe. There is a gentle uphill incline approaching ahead.", "zh": "Zoe，把單車變速調低一點。前面有一段微微上坡的緩升路段喔。", "keywords": ["switch gear", "resistance", "incline"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Got it! Cycling is not only fantastic cardiovascular exercise, but also generates zero carbon emissions.", "zh": "收到！騎單車不僅是超讚的心肺有氧運動，而且完全是零碳排呢。", "keywords": ["cardiovascular", "emissions", "zero carbon"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Let's pause at the observation pavilion up ahead to hydrate and breathe in the fresh pine scent.", "zh": "我們在前面的觀景涼亭稍作休息喝口水，深呼吸一下清新的松木香氣吧。", "keywords": ["observation", "pavilion", "hydrate"] }
    ],
    "vocabulary": [
      { "word": "canopy", "phonetic": "/ˈkæn.ə.pi/", "pos": "n.", "zh": "樹冠層、華蓋、罩篷", "example": "Monkeys leaped gracefully through the rainforest canopy." },
      { "word": "dappled", "phonetic": "/ˈdæp.əld/", "pos": "adj.", "zh": "斑駁的、有花斑的", "example": "Dappled sunlight danced on the forest trail." },
      { "word": "cardiovascular", "phonetic": "/ˌkɑːr.di.oʊˈvæs.kjə.lɚ/", "pos": "adj.", "zh": "心血管的", "example": "Aerobic swimming supports optimal cardiovascular endurance." }
    ],
    "dailyPhrase": { "en": "Dappled sunlight.", "zh": "斑駁樹影間灑落的陽光。" },
    "cultureTip": "「Green Tunnel（綠色隧道）」是指兩側行道樹樹冠在空中自然交織相接所形成的林蔭景觀。在台灣與世界各地，許多廢棄鐵道或鄉道被改建為自行車專用道（bikeway），兼具生態保育與低碳休閒（eco-tourism）。"
  },

  # 08-16 [國小初階]
  {
    "id": "dialogue-0816",
    "date": "08-16",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "益智手作",
    "topic": {
      "en": "Building a Block Castle: Stacking a Tall Skyscraper",
      "zh": "下午的積木城堡：動手搭建高高的摩天大樓"
    },
    "situation": "午後炎熱，Toby 和 Mia 坐在客廳地毯上，用木頭積木發揮創意合力蓋一座堅固的高塔大樓。",
    "speakers": {
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0816.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Toby", "avatar": "👦", "en": "Let's build the tallest skyscraper in town with these wooden blocks, Mia!", "zh": "Mia，我們用這些木頭積木來蓋全城最高的摩天大樓吧！", "keywords": ["skyscraper", "wooden blocks", "tallest"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "We must lay a wide, sturdy base first. Otherwise, it will wobble and tumble over.", "zh": "我們先打一個寬寬、穩固的底座。否則它會搖搖晃晃倒下來喔。", "keywords": ["sturdy base", "wobble", "tumble"] },
      { "id": 3, "speaker": "Toby", "avatar": "👦", "en": "Look, I am stacking rectangular blocks in a crisscross pattern for stability.", "zh": "你看，我把長方形積木用十字交錯的方式堆疊起來，這樣比較穩。", "keywords": ["crisscross", "rectangular", "stability"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "Steady hands! Put the red triangular roof right on top.", "zh": "手不要抖喔！把紅色的三角形屋頂輕輕放在最頂端。", "keywords": ["steady hands", "triangular roof", "on top"] },
      { "id": 5, "speaker": "Toby", "avatar": "👦", "en": "Hurray! It is twenty blocks tall, and it stands like a magnificent fortress!", "zh": "太棒了！它有二十個積木那麼高，立起來就像一座雄偉的堡壘！", "keywords": ["magnificent fortress", "blocks tall", "hurray"] }
    ],
    "vocabulary": [
      { "word": "skyscraper", "phonetic": "/ˈskaɪˌskreɪ.pɚ/", "pos": "n.", "zh": "摩天大樓", "example": "The Burj Khalifa is the world's most renowned skyscraper." },
      { "word": "wobble", "phonetic": "/ˈwɑː.bəl/", "pos": "v.", "zh": "搖晃、搖擺不定", "example": "The uneven chair leg wobbled on the hardwood floor." },
      { "word": "stability", "phonetic": "/stəˈbɪl.ə.t̬i/", "pos": "n.", "zh": "穩定性、穩固", "example": "A concrete foundation ensures architectural stability." }
    ],
    "dailyPhrase": { "en": "Steady hands!", "zh": "手拿穩！別發抖！" },
    "cultureTip": "玩積木（building blocks）是兒童發展空間概念（spatial awareness）與精細動作（fine motor skills）的重要遊戲。在美語中，「Crisscross pattern（交錯花紋）」常指結構相互咬合以增強穩定度。"
  },

  # 08-17 [高中進階]
  {
    "id": "dialogue-0817",
    "date": "08-17",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "行為經濟學",
    "topic": {
      "en": "The Sunk Cost Fallacy: Behavioral Economics in Daily Life",
      "zh": "行為經濟學入門：沉沒成本謬誤如何悄悄影響決策？"
    },
    "situation": "圖書館自習室外，Ethan 和 Hannah 在討論一本枯燥的書籍是否該棄讀，展開對「沉沒成本」的心理學辯證。",
    "speakers": {
      "Ethan": { "role": "Ethan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Hannah": { "role": "Hannah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0817.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ethan", "avatar": "👦", "en": "I have spent four grueling hours plowing through this dreadfully repetitive novel, yet I feel compelled to finish it.", "zh": "我已經花了四個小時痛苦地硬啃這本枯燥重複的小說，但我總覺得有強烈義務把它讀完。", "keywords": ["grueling", "compelled", "repetitive"] },
      { "id": 2, "speaker": "Hannah", "avatar": "👧", "en": "You are succumbing to the classic sunk cost fallacy, Ethan. The time invested is unrecoverable regardless of whether you finish.", "zh": "Ethan，你正在向典型的『沉沒成本謬誤』妥協。無論你讀不讀完，投入的時間都已經無法挽回了。", "keywords": ["sunk cost fallacy", "unrecoverable", "succumbing"] },
      { "id": 3, "speaker": "Ethan", "avatar": "👦", "en": "Human psychology is irrationally wired to avert loss. We hate admitting that past effort yielded negligible value.", "zh": "人類心理天生就不理性地排斥損失感。我們討厭承認自己過去的努力只產生了微不足道的價值。", "keywords": ["avert loss", "negligible", "irrationally"] },
      { "id": 4, "speaker": "Hannah", "avatar": "👧", "en": "Rational decision-making evaluates future prospective costs and utility, rather than fixating on historical expenditures.", "zh": "理性的決策應該評估未來的潛在成本與效益，而不是死抓著已發生的歷史支出不放。", "keywords": ["rational", "prospective", "utility"] },
      { "id": 5, "speaker": "Ethan", "avatar": "👦", "en": "You are right. Closing this book frees up time for something genuinely illuminating. Opportunity cost matters more!", "zh": "你說得對。闔上這本書能釋放出時間去讀真正啟迪人心的好書。機會成本才是關鍵！", "keywords": ["illuminating", "opportunity cost", "frees up"] }
    ],
    "vocabulary": [
      { "word": "fallacy", "phonetic": "/ˈfæl.ə.si/", "pos": "n.", "zh": "謬論、謬誤", "example": "The assumption that expensive items are always superior is a logical fallacy." },
      { "word": "unrecoverable", "phonetic": "/ˌʌn.rɪˈkʌv.ɚ.ə.bəl/", "pos": "adj.", "zh": "無法挽回的、無法收回的", "example": "Flooded paper records were deemed unrecoverable." },
      { "word": "prospective", "phonetic": "/prəˈspek.tɪv/", "pos": "adj.", "zh": "未來的、預期的、潛在的", "example": "Universities host open houses for prospective students." }
    ],
    "dailyPhrase": { "en": "Cut one's losses.", "zh": "及時止損、認賠退出。" },
    "cultureTip": "「Sunk Cost Fallacy（沉沒成本謬誤）」由諾貝爾經濟學獎得主康納曼（Daniel Kahneman）等學者深入剖析。人們常因為「捨不得先前投入的金錢、時間或感情」而持續做出不利的決定。學會「Cut one's losses（即時停損）」是現代人重要的思維素養。"
  },

  # 08-18 [國小中高]
  {
    "id": "dialogue-0818",
    "date": "08-18",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "生命教育",
    "topic": {
      "en": "Summer Pet Care: Bathing and Grooming the Family Dog",
      "zh": "寵物照護日記：在炎夏給狗狗洗澡與吹毛"
    },
    "situation": "夏日週末，Alex 和 Mia 在後院花園裡拿著水管和寵物專用洗毛精，幫金毛尋回犬 Lucky 洗澡梳毛。",
    "speakers": {
      "Alex": { "role": "Alex", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0818.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Alex", "avatar": "👦", "en": "Lucky has been panting in the afternoon heat. Giving him a lukewarm bath will make him feel so refreshed.", "zh": "Lucky 在午後高溫下一直吐舌頭喘氣。給他洗個溫水澡會讓他感到好舒爽。", "keywords": ["panting", "lukewarm", "refreshed"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "Watch out! Whenever you turn on the garden hose, he shakes his whole wet body vigorously!", "zh": "小心喔！只要你打開花園水管，他整隻濕漉漉的身體就會大力甩乾呢！", "keywords": ["garden hose", "vigorously", "shakes"] },
      { "id": 3, "speaker": "Alex", "avatar": "👦", "en": "Here is the oatmeal pet shampoo. Rub it into a rich lather to soothe his sensitive skin.", "zh": "這是燕麥配方的寵物洗毛精。搓揉出豐盈的泡泡，可以舒緩他敏感的皮膚。", "keywords": ["oatmeal shampoo", "rich lather", "soothe"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "Now let's towel dry him thoroughly and use the blow dryer on the cool air setting.", "zh": "現在我們用大毛巾徹底擦乾他，再用吹風機的冷風檔慢慢吹乾。", "keywords": ["towel dry", "blow dryer", "cool air"] },
      { "id": 5, "speaker": "Alex", "avatar": "👦", "en": "Look at him wagging his tail happily. A well-groomed dog is a healthy dog!", "zh": "看他開心地搖尾巴。梳理得乾乾淨淨的狗狗，就是健康快樂的狗狗！", "keywords": ["wagging tail", "well-groomed", "healthy"] }
    ],
    "vocabulary": [
      { "word": "pant", "phonetic": "/pænt/", "pos": "v.", "zh": "氣喘吁吁、喘氣", "example": "The marathon runner panted after crossing the finish line." },
      { "word": "vigorously", "phonetic": "/ˈvɪɡ.ɚ.əs.li/", "pos": "adv.", "zh": "精力充沛地、劇烈地、用力地", "example": "Whisk the egg yolks vigorously until frothy." },
      { "word": "groom", "phonetic": "/ɡruːm/", "pos": "v.", "zh": "梳理毛髮、打扮", "example": "Cats spend hours grooming their sleek fur." }
    ],
    "dailyPhrase": { "en": "Wag one's tail.", "zh": "搖尾巴（表示開心與喜愛）。" },
    "cultureTip": "夏季毛孩防暑（Pet Heatstroke Prevention）至關重要。獸醫提醒切勿在高溫正午於滾燙柏油路溜狗，洗澡應避免冰水衝擊以免血管劇烈收縮，吹毛使用冷風檔（cool setting）能有效預防濕疹皮膚病。"
  },

  # 08-19 [國中挑戰]
  {
    "id": "dialogue-0819",
    "date": "08-19",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#16a34a",
    "category": "攝影藝術",
    "topic": {
      "en": "World Photography Day: Framing Light & Stories with Smartphones",
      "zh": "世界攝影日：用手機鏡頭捕捉生活中的光影故事"
    },
    "situation": "8月19日世界攝影日，Brian 和 Amy 在老街街角練習運用「黃金分割三分法」與光影構圖拍攝照片。",
    "speakers": {
      "Brian": { "role": "Brian", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Amy": { "role": "Amy", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0819.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Brian", "avatar": "👦", "en": "Today is World Photography Day, celebrating how visual images preserve fleeting moments in human history.", "zh": "今天是世界攝影日，慶祝視覺影像如何留存人類歷史上稍縱即逝的瞬間。", "keywords": ["World Photography Day", "preserve", "fleeting"] },
      { "id": 2, "speaker": "Amy", "avatar": "👧", "en": "You don't need expensive DSLR gear. Even with a smartphone, understanding light and composition creates masterpieces.", "zh": "不一定非要有昂貴的單眼相機裝備不可。只要懂光線和構圖，手機也能拍出傑作。", "keywords": ["DSLR gear", "composition", "masterpieces"] },
      { "id": 3, "speaker": "Brian", "avatar": "👦", "en": "I always enable the rule-of-thirds grid on my camera app to place key subjects along intersecting lines.", "zh": "我總是在相機 App 裡開啟三分法則格線，把主體放在線條的交叉點上。", "keywords": ["rule-of-thirds", "intersecting", "grid"] },
      { "id": 4, "speaker": "Amy", "avatar": "👧", "en": "And the golden hour right before sunset casts long shadows and warm, flattering honey tones.", "zh": "而且日落前的黃金時刻（golden hour）能拉出長長影子，映照出溫暖柔和的蜜糖色調。", "keywords": ["golden hour", "sunset", "flattering"] },
      { "id": 5, "speaker": "Brian", "avatar": "👦", "en": "Photography is essentially painting with light. Click! We just captured that joyful baker smiling outside his shop.", "zh": "攝影本質上就是用光線作畫。喀嚓！我們剛好捕捉到了麵包師傅在店外微笑的溫馨畫面。", "keywords": ["painting with light", "captured", "joyful"] }
    ],
    "vocabulary": [
      { "word": "fleeting", "phonetic": "/ˈfliː.t̬ɪŋ/", "pos": "adj.", "zh": "短暫的、稍縱即逝的", "example": "Youth is fleeting, so cherish every stage of life." },
      { "word": "composition", "phonetic": "/ˌkɑːm.pəˈzɪʃ.ən/", "pos": "n.", "zh": "構圖、組成、成分", "example": "The landscape painting boasts impeccable compositional balance." },
      { "word": "flattering", "phonetic": "/ˈflæt̬.ɚ.ɪŋ/", "pos": "adj.", "zh": "顯好看的、奉承的、諂媚的", "example": "Soft candle light provides very flattering portraits." }
    ],
    "dailyPhrase": { "en": "Capture a moment.", "zh": "捕捉珍貴的片刻時光。" },
    "cultureTip": "每年 8 月 19 日為「World Photography Day（世界攝影日）」，紀念 1839 年法國政府公開達蓋爾銀版攝影術專利。攝影名言「The best camera is the one that's with you（最好的相機就是你身邊的那一台）」激勵人們隨時捕捉身邊的動人生活。"
  },

  # 08-20 [國小初階]
  {
    "id": "dialogue-0820",
    "date": "08-20",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "生活自理",
    "topic": {
      "en": "Organizing the Bookshelf: Sorting Toys and Books",
      "zh": "整理書架與玩具箱：分類收納的好習慣"
    },
    "situation": "夏日午後，Ben 和 Lily 在臥室裡整理書架，把繪本、漫畫與積木分別貼標籤收納進透明儲物箱。",
    "speakers": {
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Lily": { "role": "Lily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0820.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ben", "avatar": "👦", "en": "Our playroom floor is covered with scattered picture books and toy cars, Lily.", "zh": "Lily，我們的遊戲室地板上到處都是散落的圖畫書和小汽車呢。", "keywords": ["scattered", "picture books", "toy cars"] },
      { "id": 2, "speaker": "Lily", "avatar": "👧", "en": "Let's organize everything into labeled bins before mom comes in!", "zh": "趁媽媽進來之前，我們把所有東西分類收進貼有標籤的儲物箱吧！", "keywords": ["organize", "labeled bins", "before"] },
      { "id": 3, "speaker": "Ben", "avatar": "👦", "en": "I will line up the storybooks on the middle shelf from tallest to shortest.", "zh": "我負責把故事書在中間書架上由高到矮整整齊齊排好。", "keywords": ["line up", "middle shelf", "tallest"] },
      { "id": 4, "speaker": "Lily", "avatar": "👧", "en": "I will place all the plastic action figures and puzzle boxes in this clear container.", "zh": "我把所有的塑膠公仔和拼圖盒子都放進這個透明箱子裡。", "keywords": ["action figures", "puzzle boxes", "clear container"] },
      { "id": 5, "speaker": "Ben", "avatar": "👦", "en": "A place for everything, and everything in its place. Our room looks so clean and cozy!", "zh": "物歸原位、井然有序。我們的房間現在看起來好乾淨、好舒適喔！", "keywords": ["clean and cozy", "everything in its place"] }
    ],
    "vocabulary": [
      { "word": "scattered", "phonetic": "/ˈskæt̬.ɚd/", "pos": "adj.", "zh": "散落的、零散的", "example": "Scattered papers blew across the breezy lawn." },
      { "word": "organize", "phonetic": "/ˈɔːr.ɡən.aɪz/", "pos": "v.", "zh": "整理、組織、籌劃", "example": "She organized her desktop icons alphabetically." },
      { "word": "container", "phonetic": "/kənˈteɪ.nɚ/", "pos": "n.", "zh": "容器、儲存箱", "example": "Store leftover soup in an airtight glass container." }
    ],
    "dailyPhrase": { "en": "A place for everything, and everything in its place.", "zh": "物各有其所，物各在其位（整齊有序的收納黃金法則）。" },
    "cultureTip": "「A place for everything, and everything in its place」是英語中深植家庭教育的著名格言，強調自幼養成收納習慣（tidying up）。分類標籤（labeling bins）有助於孩子培養責任感與條理性。"
  },

  # 08-21 [高中進階]
  {
    "id": "dialogue-0821",
    "date": "08-21",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "心理學與成長",
    "topic": {
      "en": "Resilience & the Growth Mindset: Turning Setbacks into Fuel",
      "zh": "心理韌性：成長型思維如何面對挫折與挑戰？"
    },
    "situation": "在升學模擬考試成績公布後，Marcus 和 Chloe 探討 Carol Dweck 的成長型心態，反思如何將失利轉化為進步的基石。",
    "speakers": {
      "Marcus": { "role": "Marcus", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0821.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Marcus", "avatar": "👦", "en": "My mock exam essay score was disappointingly mediocre. It felt like an indictment of my intellectual capabilities.", "zh": "我的模擬考作文分數令人失望地平庸。感覺就像對我的智力水平進行了一場殘酷的宣判。", "keywords": ["mediocre", "indictment", "intellectual"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "That internal monologue reflects a fixed mindset, Marcus. Psychologist Carol Dweck demonstrated that intelligence is malleable, not static.", "zh": "那種內心獨白正反映了定型心態，Marcus。心理學家卡蘿·杜維克證明了智力是具有高度可塑性的，而非固定不變。", "keywords": ["fixed mindset", "malleable", "static"] },
      { "id": 3, "speaker": "Marcus", "avatar": "👦", "en": "Instead of saying 'I am terrible at analytical rhetoric,' I should reframe it as 'I haven't mastered this argumentative structure yet.'", "zh": "我不該說『我根本不擅長分析性修辭』，而應該重塑為『我只是還沒掌握這種論證結構而已』。", "keywords": ["analytical rhetoric", "reframe", "mastered"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "Exactly! The power of 'yet' alters the neurobiology of motivation. Failure ceases to be an identity; it becomes diagnostic feedback.", "zh": "太精準了！『尚未（yet）』的力量能重構動機的神經生物學機制。失敗不再是一種身份標籤，而是極具診斷價值的反饋。", "keywords": ["power of yet", "neurobiology", "diagnostic feedback"] },
      { "id": 5, "speaker": "Marcus", "avatar": "👦", "en": "Resilience isn't about avoiding falls; it is the iterative grit to deconstruct mistakes and rebuild with greater mastery.", "zh": "心理韌性從來不是為了避免跌倒；而是一種反覆拆解錯誤、以更強掌控力重新站起的堅毅品格。", "keywords": ["resilience", "iterative grit", "mastery"] }
    ],
    "vocabulary": [
      { "word": "malleable", "phonetic": "/ˈmæl.i.ə.bəl/", "pos": "adj.", "zh": "有延展性的、可塑的、易受影響的", "example": "Gold is the most malleable metal known to science." },
      { "word": "reframe", "phonetic": "/ˌriːˈfreɪm/", "pos": "v.", "zh": "重構、從新視角看待", "example": "Therapy helps individuals reframe irrational anxieties constructively." },
      { "word": "iterative", "phonetic": "/ˈɪt̬.ɚ.eɪ.t̬ɪv/", "pos": "adj.", "zh": "反覆的、迭代的", "example": "Software design relies on iterative cycles of user testing." }
    ],
    "dailyPhrase": { "en": "The power of yet.", "zh": "「尚未」的強大力量（留給成長無限空間）。" },
    "cultureTip": "史丹佛大學心理學教授 Carol Dweck 在其著作《心態致勝（Mindset）》中提出「Growth Mindset（成長型思維）」。其中「The Power of Yet（尚未的力量）」倡導在自嘲「我做不到」後面加上一個「Yet（還沒）」，便能瞬間將挫敗轉化為學習的起點。"
  },

  # 08-22 [國小中高]
  {
    "id": "dialogue-0822",
    "date": "08-22",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "烘焙手作",
    "topic": {
      "en": "Baking Warm Banana Muffins: Measuring Spoons & Kitchen Magic",
      "zh": "烘焙香濃香蕉馬芬：廚房裡的量杯與食材魔法"
    },
    "situation": "下雨天待在室內，Emma 和 Kevin 拿著過熟的香蕉，在廚房裡量取麵粉與肉桂粉烘烤熱呼呼的香蕉鬆餅蛋糕。",
    "speakers": {
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Kevin": { "role": "Kevin", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0822.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Emma", "avatar": "👧", "en": "These three overripe bananas on the counter have brown freckles. They are perfect for baking muffins!", "zh": "流理台上這三根熟透的香蕉長滿了褐色斑點。拿來烤馬芬蛋糕再適合不過了！", "keywords": ["overripe", "freckles", "muffins"] },
      { "id": 2, "speaker": "Kevin", "avatar": "👦", "en": "I love using the potato masher to squish them into a smooth, fragrant paste.", "zh": "我好喜歡用壓泥器把牠們壓成滑順又香噴噴的香蕉果泥喔。", "keywords": ["potato masher", "squish", "fragrant paste"] },
      { "id": 3, "speaker": "Emma", "avatar": "👧", "en": "Baking is like a precise chemistry lab: measure two cups of whole-wheat flour and one teaspoon of baking soda.", "zh": "烘焙就像嚴密的化學實驗：精確量取兩杯全麥麵粉和一茶匙小蘇打粉。", "keywords": ["chemistry lab", "whole-wheat", "baking soda"] },
      { "id": 4, "speaker": "Kevin", "avatar": "👦", "en": "A dash of fragrant ground cinnamon gives it that cozy bakery aroma.", "zh": "再撒上一小撮香噴噴的肉桂粉，就能帶出烘焙麵包坊那種溫暖怡人的香氣。", "keywords": ["dash", "cinnamon", "aroma"] },
      { "id": 5, "speaker": "Emma", "avatar": "👧", "en": "Twenty minutes in the oven at three hundred and fifty degrees, and our golden treats will be ready!", "zh": "放進華氏三百五十度的烤箱二十分鐘，我們金黃誘人的馬芬就出爐囉！", "keywords": ["three hundred and fifty", "golden treats", "oven"] }
    ],
    "vocabulary": [
      { "word": "overripe", "phonetic": "/ˌoʊ.vɚˈraɪp/", "pos": "adj.", "zh": "過熟的、熟透的", "example": "Overripe bananas add natural sweetness to morning pancakes." },
      { "word": "teaspoon", "phonetic": "/ˈtiː.spuːn/", "pos": "n.", "zh": "茶匙（容量單位）", "example": "Add half a teaspoon of pure vanilla extract." },
      { "word": "aroma", "phonetic": "/əˈroʊ.mə/", "pos": "n.", "zh": "芳香、香氣", "example": "The comforting aroma of roasted coffee filled the cafe." }
    ],
    "dailyPhrase": { "en": "A dash of something.", "zh": "少許、一小撮（調味料等）。" },
    "cultureTip": "熟透長黑斑的香蕉（brown-speckled bananas）糖分最高，是美式家庭烘焙香蕉麵包（Banana bread）與馬芬（muffins）的首選。料理烘焙也是孩子學習測量單位（cups, teaspoons）與化學反應（baking soda leavening）的最佳生活實驗室。"
  },

  # 08-23 [國中挑戰]
  {
    "id": "dialogue-0823",
    "date": "08-23",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#16a34a",
    "category": "傳統節氣",
    "topic": {
      "en": "Chushu Solar Term: The End of Heat and Welcoming Autumn Breeze",
      "zh": "處暑節氣：炎暑將退、微涼秋意漸生與秋燥養生"
    },
    "situation": "8月23日處暑節氣傍晚，Brian 和 Amy 散步在落日河堤，感受夏熱消退後的微涼晚風。",
    "speakers": {
      "Brian": { "role": "Brian", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Amy": { "role": "Amy", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0823.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Brian", "avatar": "👦", "en": "Today marks Chushu, literally translating to the 'cessation of summer heat.'", "zh": "今天是處暑，字面上的意思就是『酷暑在此打住終結』。", "keywords": ["Chushu", "cessation", "summer heat"] },
      { "id": 2, "speaker": "Amy", "avatar": "👧", "en": "Notice how the evening breeze on the riverside feels crisp rather than sticky and humid?", "zh": "你有注意到河堤邊的傍晚微風吹起來好清爽，不再黏膩潮濕了嗎？", "keywords": ["crisp", "sticky", "humid"] },
      { "id": 3, "speaker": "Brian", "avatar": "👦", "en": "Traditional folklore says that after Chushu, daytime remains sunny while evening temperatures dip significantly.", "zh": "民俗常說處暑之後，白天天氣依舊晴朗，但夜晚氣溫會明顯下降。", "keywords": ["dip significantly", "temperatures", "folklore"] },
      { "id": 4, "speaker": "Amy", "avatar": "👧", "en": "My grandma brewed sweet white fungus and pear soup to nourish the lungs against early autumn dryness.", "zh": "我外婆今天特地燉了冰糖銀耳雪梨湯，潤肺潤喉以防初秋的秋燥呢。", "keywords": ["white fungus", "pear soup", "autumn dryness"] },
      { "id": 5, "speaker": "Brian", "avatar": "👦", "en": "The golden seasonal transition has begun. It is the most delightful time of the year for outdoor excursions.", "zh": "金黃燦爛的換季時節正式開始了。這是一年中出門郊遊最舒適宜人的時光。", "keywords": ["seasonal transition", "excursions", "delightful"] }
    ],
    "vocabulary": [
      { "word": "cessation", "phonetic": "/sesˈeɪ.ʃən/", "pos": "n.", "zh": "中止、停止、終結", "example": "The diplomatic peace treaty called for immediate cessation of hostilities." },
      { "word": "crisp", "phonetic": "/krɪsp/", "pos": "adj.", "zh": "清爽涼爽的、乾脆俐落的", "example": "A crisp October morning breeze invigorated the runners." },
      { "word": "nourish", "phonetic": "/ˈnɝː.ɪʃ/", "pos": "v.", "zh": "滋養、養育、滋潤", "example": "Wholesome organic meals nourish both mind and body." }
    ],
    "dailyPhrase": { "en": "Crisp autumn air.", "zh": "初秋清爽宜人的微涼空氣。" },
    "cultureTip": "「Chushu（處暑）」為二十四節氣之第十四個節氣，處者，止也，代表炎熱暑氣逐漸消退（cessation of heat）。民間有「處暑吃鴨」、「喝百合梨湯」以防「秋燥（autumn dryness）」的飲食養生智慧。"
  },

  # 08-24 [國小初階]
  {
    "id": "dialogue-0824",
    "date": "08-24",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "童年遊樂",
    "topic": {
      "en": "Flying a Kite in Late Summer: Running with the Breeze",
      "zh": "夏末放風箏：迎著微風奔跑看彩鳶高飛"
    },
    "situation": "夏末涼爽的週末下午，Toby 和 Mia 來到河濱大草坪，放飛一隻五彩斑斕的彩虹菱形風箏。",
    "speakers": {
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0824.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Toby", "avatar": "👦", "en": "Hold the kite facing the wind, Mia, while I unwind the string spool.", "zh": "Mia，你迎著風抓好風箏，我來慢慢解開風箏線輪。", "keywords": ["facing the wind", "unwind", "string spool"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "A steady gust is blowing across the lawn! One, two, three, let go!", "zh": "一陣穩定的微風正吹過草坪！一、二、三，放手！", "keywords": ["steady gust", "let go", "lawn"] },
      { "id": 3, "speaker": "Toby", "avatar": "👦", "en": "Run, Toby, run! The rainbow kite is catching the updraft and soaring higher!", "zh": "快跑、快跑！彩虹風箏乘著上升氣流，越飛越高了！", "keywords": ["updraft", "soaring", "rainbow kite"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "Look at its long colorful ribbons dancing like waves against the blue sky.", "zh": "看它長長的彩色緞帶尾巴在藍天中像波浪一樣跳舞。", "keywords": ["colorful ribbons", "dancing", "blue sky"] },
      { "id": 5, "speaker": "Toby", "avatar": "👦", "en": "It looks like a magnificent bird gliding freely among the white clouds.", "zh": "它看起來就像一隻雄偉的大鳥，在白雲之間自由自在地翱翔。", "keywords": ["magnificent bird", "gliding freely", "white clouds"] }
    ],
    "vocabulary": [
      { "word": "spool", "phonetic": "/spuːl/", "pos": "n.", "zh": "線軸、卷筒", "example": "He reeled the heavy nylon line onto the wooden spool." },
      { "word": "gust", "phonetic": "/ɡʌst/", "pos": "n.", "zh": "一陣強風、一陣狂風", "example": "A sudden gust of wind blew her sunhat onto the river." },
      { "word": "soar", "phonetic": "/sɔːr/", "pos": "v.", "zh": "高飛、翱翔、猛增", "example": "Golden eagles soar majestically over alpine peaks." }
    ],
    "dailyPhrase": { "en": "Soar into the sky.", "zh": "一飛沖天、翱翔天際。" },
    "cultureTip": "夏末秋初風力穩定，正是最適合戶外放風箏（kite flying）的時令。在美語中，「Soar（高飛）」常用來象徵夢想騰飛或心靈自由，是孩童戶外活動中最富诗意的片刻。"
  },

  # 08-25 [高中進階]
  {
    "id": "dialogue-0825",
    "date": "08-25",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "數位素養",
    "topic": {
      "en": "Digital Minimalism: Reclaiming Focus from Information Overload",
      "zh": "數位極簡主義：告別資訊過載、找回平靜專注力"
    },
    "situation": "在即將迎來新學年之際，Ethan 和 Hannah 在校園長凳上探討 Cal Newport 的數位極簡概念，反思社群通知對專注力的侵蝕。",
    "speakers": {
      "Ethan": { "role": "Ethan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Hannah": { "role": "Hannah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0825.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ethan", "avatar": "👦", "en": "I checked my screen-time report yesterday and was horrified to discover I averaged five hours daily on short-form video reels.", "zh": "我昨天看了一下手機螢幕使用時間報告，驚恐地發現自己平均每天花五個小時刷短影音。", "keywords": ["screen-time", "horrified", "short-form"] },
      { "id": 2, "speaker": "Hannah", "avatar": "👧", "en": "Those algorithmic feeds are deliberately engineered by neuroscientists to trigger erratic dopamine surges, hijacking our cognitive bandwidth.", "zh": "那些演算法動態牆是神經學家刻意設計來觸發不規則多巴胺激增的，藉此劫持我們的大腦認知頻寬。", "keywords": ["algorithmic feeds", "dopamine surges", "cognitive bandwidth"] },
      { "id": 3, "speaker": "Ethan", "avatar": "👦", "en": "Computer scientist Cal Newport advocates for 'digital minimalism'—treating digital tools with utilitarian intentionality rather than compulsive reactivity.", "zh": "電腦科學家卡爾·紐波特倡導『數位極簡主義』——以目的明確的實用主義對待數位工具，而非強迫性的被動反應。", "keywords": ["digital minimalism", "utilitarian", "intentionality"] },
      { "id": 4, "speaker": "Hannah", "avatar": "👧", "en": "I implemented a strict digital declutter: uninstalling non-essential social apps and turning off all push notifications except for phone calls.", "zh": "我實施了嚴格的數位斷捨離：卸載非必要社交軟體，關閉除電話以外的所有推播通知。", "keywords": ["digital declutter", "push notifications", "uninstalling"] },
      { "id": 5, "speaker": "Ethan", "avatar": "👦", "en": "Silence restores deep focus. Reclaiming our attention is the ultimate act of intellectual sovereignty before the school year commences.", "zh": "寂靜能喚回深度專注。在新學年開始前奪回我們的注意力主權，是最具力量的智力重塑。", "keywords": ["intellectual sovereignty", "deep focus", "commences"] }
    ],
    "vocabulary": [
      { "word": "erratic", "phonetic": "/ɪˈræt̬.ɪk/", "pos": "adj.", "zh": "不穩定的、難以預測的、飄忽不定的", "example": "The stormy wind caused erratic power outages across town." },
      { "word": "intentionality", "phonetic": "/ɪnˌten.ʃənˈæl.ə.t̬i/", "pos": "n.", "zh": "目的性、自覺意向", "example": "Live each day with deliberate moral intentionality." },
      { "word": "sovereignty", "phonetic": "/ˈsɑːv.rən.ti/", "pos": "n.", "zh": "主權、獨立自主權", "example": "Digital privacy laws safeguard individual information sovereignty." }
    ],
    "dailyPhrase": { "en": "Reclaim one's focus.", "zh": "奪回專注力、重掌注意力主權。" },
    "cultureTip": "「Digital Minimalism（數位極簡主義）」由喬治城大學教授 Cal Newport 倡導。在資訊氾濫（information overload）與短影音成癮的時代，青年學子透過關閉推播通知（disabling notifications）與數位斷捨離，重獲沉浸深度學習（Deep Work）的寧靜。"
  },

  # 08-26 [國小中高]
  {
    "id": "dialogue-0826",
    "date": "08-26",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "開學準備",
    "topic": {
      "en": "Resetting Sleep Cycles: Pre-Semester Body Clock Adjustment",
      "zh": "倒數開學收心操：調整鬧鐘、早睡早起好精神"
    },
    "situation": "8月下旬暑假倒數，Kevin 和 Emma 討論開學前的「生理時鐘收心計畫」，提早上床睡覺讓開學不賴床。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0826.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "👦", "en": "Only one week left before school starts, Emma! I have been staying up late reading comic books.", "zh": "Emma，距離開學只剩最後一週了！我最近放假都熬夜看漫畫。", "keywords": ["one week left", "staying up late", "comic books"] },
      { "id": 2, "speaker": "Emma", "avatar": "👧", "en": "If you don't adjust your circadian rhythm now, you will be a groggy zombie on the first day of class.", "zh": "如果你現在不調好生理時鐘，開學第一天你一定會變成昏昏沉沉的瞌睡殭屍喔。", "keywords": ["circadian rhythm", "groggy zombie", "adjust"] },
      { "id": 3, "speaker": "Kevin", "avatar": "👦", "en": "You are totally right. What is your strategy for shifting bedtime earlier?", "zh": "你說得太對了。你把上床睡覺時間提前的策略是什麼呢？", "keywords": ["totally right", "strategy", "bedtime earlier"] },
      { "id": 4, "speaker": "Emma", "avatar": "👧", "en": "I shift my alarm twenty minutes earlier each morning and stop using screens an hour before sleeping.", "zh": "我每天早上把鬧鐘調早二十分鐘，而且睡前一小時絕不碰任何螢幕。", "keywords": ["shift alarm", "screens", "before sleeping"] },
      { "id": 5, "speaker": "Kevin", "avatar": "👦", "en": "Let's reset our clocks together so we feel fully refreshed and energized for the new semester!", "zh": "我們一起重整作息吧，這樣新學期就能精神飽滿、活力充沛！", "keywords": ["reset clocks", "energized", "refreshed"] }
    ],
    "vocabulary": [
      { "word": "circadian", "phonetic": "/sɝːˈkeɪ.di.ən/", "pos": "adj.", "zh": "生理時鐘的、晝夜節律的", "example": "Natural morning sunlight synchronizes our circadian clock." },
      { "word": "groggy", "phonetic": "/ˈɡrɑː.ɡi/", "pos": "adj.", "zh": "昏昏沉沉的、頭腦發沉的", "example": "He felt groggy after taking the allergy medicine." },
      { "word": "semester", "phonetic": "/səˈmes.tɚ/", "pos": "n.", "zh": "學期", "example": "The fall semester introduces chemistry and world history." }
    ],
    "dailyPhrase": { "en": "Reset one's body clock.", "zh": "重整生理時鐘、調整作息。" },
    "cultureTip": "「Circadian rhythm（生理時鐘/晝夜節律）」是調控睡眠與覺醒的核心生理機制。美國兒科學會（AAP）建議開學前 7-10 天逐步以「每天提前 15-20 分鐘」的漸進式調整，避免開學首週發生「社會性時差（social jetlag）」倦怠。"
  },

  # 08-27 [國中挑戰]
  {
    "id": "dialogue-0827",
    "date": "08-27",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#16a34a",
    "category": "開學準備",
    "topic": {
      "en": "Back-to-School Shopping: Durable Backpacks & Stationery",
      "zh": "挑選新學期裝備：耐用雙肩書包與文具清單"
    },
    "situation": "週末文具商場裡，Brian 和 Amy 拿著新學期採購清單，挑選人體工學護脊書包與活頁筆記本。",
    "speakers": {
      "Brian": { "role": "Brian", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Amy": { "role": "Amy", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0827.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Brian", "avatar": "👦", "en": "The back-to-school aisles are bustling with students stocking up on fresh stationery supplies.", "zh": "開學用品專區擠滿了添購全新文具用品的學生呢。", "keywords": ["back-to-school", "aisles", "stationery"] },
      { "id": 2, "speaker": "Amy", "avatar": "👧", "en": "I need an ergonomic backpack with padded shoulder straps and lumbar support to protect my spine.", "zh": "我需要一個有加厚雙肩背帶與護脊支撐的人體工學書包，來保護我的脊椎。", "keywords": ["ergonomic", "lumbar support", "spine"] },
      { "id": 3, "speaker": "Brian", "avatar": "👦", "en": "Check out this water-resistant canvas backpack with multiple compartments for laptops, binders, and water bottles.", "zh": "看看這款防潑水帆布書包，裡面有多個隔層可以放筆電、活頁夾和水壺。", "keywords": ["water-resistant", "compartments", "binders"] },
      { "id": 4, "speaker": "Amy", "avatar": "👧", "en": "I also grabbed five color-coded gel pens, highlighters, and two packs of sticky notes for my study schedule.", "zh": "我還拿了五支不同顏色的中性筆、螢光筆，還有兩包為讀書計畫準備的便利貼。", "keywords": ["color-coded", "gel pens", "sticky notes"] },
      { "id": 5, "speaker": "Brian", "avatar": "👦", "en": "Unwrapping fresh school supplies always gives that crisp, motivating feeling of a brand new beginning.", "zh": "拆開全新文具總能帶來那種神清氣爽、充滿幹勁的全新開端！", "keywords": ["motivating", "brand new beginning", "fresh supplies"] }
    ],
    "vocabulary": [
      { "word": "ergonomic", "phonetic": "/ˌɝː.ɡəˈnɑː.mɪk/", "pos": "adj.", "zh": "符合人體工學的", "example": "An ergonomic desk chair prevents chronic lower back pain." },
      { "word": "compartment", "phonetic": "/kəmˈpɑːrt.mənt/", "pos": "n.", "zh": "隔間、間隔、隔層", "example": "The travel suitcase features a zippered waterproof compartment." },
      { "word": "water-resistant", "phonetic": "/ˈwɑː.t̬ɚ rɪˌzɪs.tənt/", "pos": "adj.", "zh": "防潑水的、抗水的", "example": "This lightweight jacket is water-resistant in light drizzles." }
    ],
    "dailyPhrase": { "en": "Stock up on supplies.", "zh": "備齊用品、囤積物資。" },
    "cultureTip": "「Back-to-School Shopping（開學季採購）」是歐美八月下旬最重要的零售熱潮。家長與青少年挑選書包時最看重「Ergonomic lumbar support（符合人體工學的護脊支撐）」，避免沉重的課本造成姿勢不良。"
  },

  # 08-28 [國小初階]
  {
    "id": "dialogue-0828",
    "date": "08-28",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "成長與生活",
    "topic": {
      "en": "Trying on New School Uniforms: Look, I Grew Taller!",
      "zh": "試穿新學年校服與運動鞋：我又長高了！"
    },
    "situation": "開學前幾天，Leo 和 Mia 在鏡子前試穿新校服與白色球鞋，驚喜發現經過一個暑假自己長高了整整三公分。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0828.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Mia, try on your new school uniform and see if the pleated skirt fits comfortably.", "zh": "Mia，快試穿你的新校服，看看這件百褶裙合不合身。", "keywords": ["school uniform", "pleated skirt", "fits"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "My old school pants from last year are way too short! They barely reach my ankles.", "zh": "我去年舊的制服褲子太短了啦！現在長度幾乎只到腳踝而已。", "keywords": ["barely", "ankles", "too short"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Mom marked our growth chart on the doorframe. You grew three whole centimeters this summer!", "zh": "媽媽在門框上的身高表量了身高。你這個夏天整整長高了三公分呢！", "keywords": ["growth chart", "doorframe", "centimeters"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "Look at my new white sneakers too. They have cushiony soles and shiny silver laces.", "zh": "也看看我的新白球鞋。鞋底軟綿綿的，還有亮晶晶的銀色鞋帶。", "keywords": ["cushiony soles", "sneakers", "silver laces"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "You look so smart and ready. Grade three, here we come!", "zh": "你看起來好精神、準備好了。三年級，我們來囉！", "keywords": ["smart", "ready", "here we come"] }
    ],
    "vocabulary": [
      { "word": "pleated", "phonetic": "/ˈpliː.t̬ɪd/", "pos": "adj.", "zh": "打褶的、有百褶的", "example": "She wore a navy blue pleated skirt for the choir performance." },
      { "word": "ankle", "phonetic": "/ˈæŋ.kəl/", "pos": "n.", "zh": "腳踝", "example": "He wore supportive socks that covered his ankles." },
      { "word": "cushiony", "phonetic": "/ˈkʊʃ.ən.i/", "pos": "adj.", "zh": "柔軟有彈性的、如坐墊般舒服的", "example": "The cushiony insoles made running along the pavement painless." }
    ],
    "dailyPhrase": { "en": "Look smart.", "zh": "看起來神采奕奕、帥氣俐落。" },
    "cultureTip": "英美習慣用「Look smart」形容穿著筆挺校服（neat school uniform）時那種整潔精神的樣貌。門框刻痕記錄身高（Growth chart on the doorframe）是世界各地家庭見證孩子年年成長的溫馨傳統。"
  },

  # 08-29 [國小中高]
  {
    "id": "dialogue-0829",
    "date": "08-29",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "返校校園",
    "topic": {
      "en": "Campus Orientation Day: Catching Up with Friends & New Desks",
      "zh": "返校日：見到親愛的朋友與參觀新教室"
    },
    "situation": "返校日早晨，Kevin 和 Emma 走進新落成的教學大樓，見到兩個月不見的同班好友，熱切分享暑假趣事。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0829.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "👦", "en": "Emma! Over here! It is so wonderful to see all our classmates after two whole months!", "zh": "Emma！這邊這邊！整整兩個月後能再次見到全班同學，真是太開心了！", "keywords": ["classmates", "two whole months", "wonderful"] },
      { "id": 2, "speaker": "Emma", "avatar": "👧", "en": "Kevin! Look how tanned you got! Did you spend your entire summer outdoors on the beach?", "zh": "Kevin！你看起來曬得好黑好健康喔！你整個夏天都在海邊戶外度過嗎？", "keywords": ["tanned", "outdoors", "beach"] },
      { "id": 3, "speaker": "Kevin", "avatar": "👦", "en": "Yes, I learned how to paddleboard and cycle! Look at our new classroom on the second floor.", "zh": "對啊，我學會了立式划槳還有騎單車！看看我們在二樓的新教室。", "keywords": ["paddleboard", "new classroom", "second floor"] },
      { "id": 4, "speaker": "Emma", "avatar": "👧", "en": "The walls have been freshly painted mint green, and our desks have name tags already.", "zh": "牆壁新漆成了薄荷綠色，而且我們的課桌上已經貼好專屬名字牌了耶。", "keywords": ["mint green", "name tags", "freshly painted"] },
      { "id": 5, "speaker": "Kevin", "avatar": "👦", "en": "We are desk neighbors again! This school year is going to be our most epic adventure yet.", "zh": "我們又是坐隔壁的鄰桌了！這個新學年肯定會是我們最精彩的大冒險。", "keywords": ["desk neighbors", "epic adventure", "school year"] }
    ],
    "vocabulary": [
      { "word": "tanned", "phonetic": "/tænd/", "pos": "adj.", "zh": "曬成小麥色的、曬黑健康的", "example": "He returned from the sailing trip with tanned cheeks." },
      { "word": "paddleboard", "phonetic": "/ˈpæd.əl.bɔːrd/", "pos": "n./v.", "zh": "立式划槳、划槳板", "example": "Gliding on a paddleboard requires good core equilibrium." },
      { "word": "epic", "phonetic": "/ˈep.ɪk/", "pos": "adj.", "zh": "史詩般的、極為精彩震撼的", "example": "The school championship game was an epic showdown." }
    ],
    "dailyPhrase": { "en": "Catch up with old friends.", "zh": "與老朋友重聚敘舊、聊聊近況。" },
    "cultureTip": "「Orientation Day / Back-to-School Day（返校日/新生定向日）」讓學生在正式開學前熟悉新教室、領取課本、結識新導師。重逢時互道「Catch up（敘舊）」是西方校園生活最溫馨熱鬧的風景。"
  },

  # 08-30 [國中挑戰]
  {
    "id": "dialogue-0830",
    "date": "08-30",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#16a34a",
    "category": "暑期總結",
    "topic": {
      "en": "Reviewing Summer Assignments: Proudly Sharing Personal Projects",
      "zh": "整理暑假作業與自主專案：自豪展示暑期學習成果"
    },
    "situation": "8月30日暑假最後倒數第二天，Brian 和 Amy 在書房桌前整理各自的暑期專題報告與科學紀錄。",
    "speakers": {
      "Brian": { "role": "Brian", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Amy": { "role": "Amy", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0830.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Brian", "avatar": "👦", "en": "All my summer homework is finally signed, bound, and neatly stacked in my backpack.", "zh": "我所有的暑假作業終於全部簽好名、裝訂整齊，妥妥收在書包裡了。", "keywords": ["signed", "bound", "stacked"] },
      { "id": 2, "speaker": "Amy", "avatar": "👧", "en": "I compiled my sixty-day botanical growth journal with dried flower specimens and watercolor sketches.", "zh": "我把這六十天的植物生長觀察日記整理成冊，裡面貼滿了乾燥花標本和水彩手繪圖。", "keywords": ["compiled", "specimens", "watercolor"] },
      { "id": 3, "speaker": "Brian", "avatar": "👦", "en": "Your botanical portfolio looks like a genuine field naturalist's handbook, Amy!", "zh": "Amy，你的植物專題集看起來就像真正的野外博物學家手冊一樣專業！", "keywords": ["portfolio", "naturalist", "handbook"] },
      { "id": 4, "speaker": "Amy", "avatar": "👧", "en": "And you built an operational miniature solar rover that successfully transmits temperature data.", "zh": "而你還親手組裝了一台能真正運作、成功傳輸溫度數據的微型太陽能探測車呢。", "keywords": ["operational", "miniature", "transmits"] },
      { "id": 5, "speaker": "Brian", "avatar": "👦", "en": "We didn't waste a single day. We transformed this summer into an unforgettable period of self-discovery.", "zh": "我們沒有浪費任何一天。我們把這個夏天變成了一段永生難忘的自我探索之旅。", "keywords": ["waste", "unforgettable", "self-discovery"] }
    ],
    "vocabulary": [
      { "word": "compile", "phonetic": "/kəmˈpaɪl/", "pos": "v.", "zh": "彙編、編輯、整理成冊", "example": "The editor compiled an anthology of modern environmental poetry." },
      { "word": "specimen", "phonetic": "/ˈspes.ə.mɪn/", "pos": "n.", "zh": "標本、樣本", "example": "The geologist inspected rare mineral specimens under a magnifying glass." },
      { "word": "portfolio", "phonetic": "/ˌpɔːrtˈfoʊ.li.oʊ/", "pos": "n.", "zh": "作品集、專案資料夾", "example": "She presented an impressive architectural portfolio during the interview." }
    ],
    "dailyPhrase": { "en": "Self-discovery.", "zh": "自我探索、自我成長發現。" },
    "cultureTip": "現代教育強調「自主學習（Self-directed learning）」，許多學校不再指派機械式重複抄寫作業，而是鼓勵學生完成一份專案研究（Project-based portfolio），如自然觀察日誌、科學手作或志工紀錄。"
  },

  # 08-31 [高中進階]
  {
    "id": "dialogue-0831",
    "date": "08-31",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "年度圓滿",
    "topic": {
      "en": "Grand Finale: Celebrating the 365-Day Journey & Welcoming the New Year",
      "zh": "八月終曲暨 365 天大圓滿：回首全年度英語之旅，迎向全新學年！"
    },
    "situation": "8月31日盛夏最後一夜，Marcus 和 Chloe 迎著初秋晚風，回顧過去一年 365 天每一天的學習軌跡，以無比堅定的自信迎戰高三新篇章。",
    "speakers": {
      "Marcus": { "role": "Marcus", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0831.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Marcus", "avatar": "👦", "en": "Tonight is August thirty-first, the absolute final day of summer vacation and the culmination of our three-hundred-and-sixty-five-day daily English odyssey.", "zh": "今晚是八月三十一日，暑假的最後一天，更是我們全年度 365 天每日美語長征的大圓滿頂點。", "keywords": ["culmination", "odyssey", "August thirty-first"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "From back-to-school jitters in September through holiday feasts, midterm hurdles, and summer expeditions, we have completed a full, magnificent cycle.", "zh": "從九月開學的忐忑憧憬，走過歲末節慶、期中挑戰，再到盛夏的戶外探險，我們完成了一整個圓滿而壯麗的學習閉環。", "keywords": ["jitters", "hurdles", "magnificent cycle"] },
      { "id": 3, "speaker": "Marcus", "avatar": "👦", "en": "Language learning is not a sprint; it is an enduring compounding habit. Consistency over intensity has reshaped our communicative fluency.", "zh": "語言學習從來不是百米衝刺，而是一場持之以恆的複利積累。持之以恆的自律勝過短暫的狂熱，徹底重塑了我們的語言流暢度。", "keywords": ["compounding", "consistency", "communicative fluency"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "Every vocabulary term learned and every cultural nuance grasped has expanded our cognitive horizons and global empathy.", "zh": "我們學過的每一個核心字彙、體會過的每一處文化意蘊，都拓寬了我們的認知視野與跨文化同理心。", "keywords": ["cognitive horizons", "cultural nuance", "empathy"] },
      { "id": 5, "speaker": "Marcus", "avatar": "👦", "en": "Tomorrow begins a brand new academic year. Armed with discipline, curiosity, and steadfast resilience, we are ready to conquer whatever lies ahead!", "zh": "明天就將揭開嶄新學年的序幕。帶著這份自律、好奇心與堅毅韌性，我們已經準備好迎接並征服未來的一切挑戰！", "keywords": ["academic year", "steadfast resilience", "conquer"] }
    ],
    "vocabulary": [
      { "word": "culmination", "phonetic": "/ˌkʌl.məˈneɪ.ʃən/", "pos": "n.", "zh": "頂點、最高潮、終極大成", "example": "The graduation ceremony marked the proud culmination of four years of dedicated research." },
      { "word": "odyssey", "phonetic": "/ˈɑː.də.si/", "pos": "n.", "zh": "長途冒險旅程、艱苦跋涉的征程", "example": "The astronaut described his space exploration as a transformative personal odyssey." },
      { "word": "compounding", "phonetic": "/kəmˈpaʊn.dɪŋ/", "pos": "adj./n.", "zh": "複利積累的、乘數效應的", "example": "Daily ten-minute reading habits yield compounding cognitive benefits." }
    ],
    "dailyPhrase": { "en": "Consistency over intensity.", "zh": "持之以恆勝過短暫狂熱（細水長流的力量）。" },
    "cultureTip": "8月31日是整年度 365 天課表圓滿收官的歷史時刻！從 9月1日開學到隔年 8月31日夏末，365 篇每日生活美語覆蓋了青少年與孩童一年四季的真實生活情境。持之以恆（Consistency）是掌握任何外語最不可撼動的核心力量。"
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
    for d in AUGUST_DIALOGUES:
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
    print(f"成功將 8 月份對話寫入 {DATA_FILE}！總篇數更新為: {len(existing_data)} (新增 {added_count} 篇)")

    # 同步更新 js/data.js
    with open(JS_FILE, 'w', encoding='utf-8') as f:
        f.write("// 365 每日生活美語對話資料庫 (全年度)\n")
        f.write("const DIALOGUES_DATA = ")
        f.write(json.dumps(existing_data, ensure_ascii=False, indent=2))
        f.write(";\n")
    print(f"成功同步更新 {JS_FILE}！")

if __name__ == '__main__':
    main()
