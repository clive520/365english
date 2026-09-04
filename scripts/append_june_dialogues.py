#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次建立 6 月份生活對話 (06-01 至 06-30，共 30 篇)
涵蓋端午包粽與立蛋、世界環境日、世界海洋日、芒種與夏至節氣、畢業典禮與驪歌送別、
期末總複習衝刺、費曼學習法、期末考圓滿交卷、教室大掃除、結業式與暑假生活展望等豐富主題！
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'dialogues.json')
JS_FILE = os.path.join(BASE_DIR, 'js', 'data.js')

JUNE_DIALOGUES = [
  # 06-01 [國小初階]
  {
    "id": "dialogue-0601",
    "date": "06-01",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "初夏序曲",
    "topic": {
      "en": "Welcoming June: Cicada Songs & Blooming Flame Trees",
      "zh": "迎接六月：初夏蟬鳴與校園鳳凰花開"
    },
    "situation": "六月第一天早晨，Leo 和 Mia 走進校門，看見校園角落的鳳凰木開滿了火紅的花朵。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0601.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Mia, look up at the tall flame trees by the school gate! They are covered in fiery orange blossoms!", "zh": "Mia，抬頭看校門口高大的鳳凰木！上面開滿了一簇簇如火焰般鮮紅的繁花！", "keywords": ["flame trees", "fiery", "blossoms"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "And listen! The loud, buzzing cicadas in the branches are singing together like a summer choir.", "zh": "而且你聽！樹枝間響亮鳴叫的蟬兒正齊聲合唱，就像一支夏日合唱團一樣熱鬧。", "keywords": ["cicadas", "buzzing", "choir"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "June is officially here. It brings warm sunshine, juicy watermelons, and the countdown to summer break.", "zh": "六月正式來臨囉。它帶來溫暖明亮的陽光、多汁清甜的西瓜，還有暑假倒數的興奮心情。", "keywords": ["countdown", "watermelons", "sunshine"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "Before vacation begins, we still have our final exams and graduation farewells to prepare for.", "zh": "在放暑假之前，我們還有期末考複習和畢業歡送會要好好準備呢。", "keywords": ["vacation", "graduation", "farewells"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Let's work hard and make every sunny day in June count!", "zh": "讓我們全力以赴，把六月的每一個晴朗日子都過得充實精彩！", "keywords": ["make count", "sunny day"] }
    ],
    "vocabulary": [
      { "word": "fiery", "phonetic": "/ˈfaɪr.i/", "pos": "adj.", "zh": "火紅的、如火燃燒般的", "example": "The sunset painted the evening clouds a fiery crimson." },
      { "word": "choir", "phonetic": "/kwaɪr/", "pos": "n.", "zh": "合唱團、歌詠隊", "example": "The school choir sang melodious hymns during morning assembly." },
      { "word": "countdown", "phonetic": "/ˈkaʊnt.daʊn/", "pos": "n.", "zh": "倒數計時", "example": "The exciting countdown to the rocket launch began." }
    ],
    "dailyPhrase": { "en": "Make every day count.", "zh": "讓每一天都過得充實有意義、不虛度光陰。" },
    "cultureTip": "在台灣，鳳凰木（Royal Poinciana / Flame Tree）火紅綻放與初夏第一聲蟬鳴（cicada songs），正是六月畢業季（graduation season）與盛夏到來的標誌性自然象徵。"
  },

  # 06-02 [國小中高]
  {
    "id": "dialogue-0602",
    "date": "06-02",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "趣味手作",
    "topic": {
      "en": "Making Teru Teru Bozu Dolls: Wishing for Sunny Recess",
      "zh": "動手做晴天娃娃：祈禱梅雨放晴與戶外體育課"
    },
    "situation": "連綿陰雨的午後，Kevin 和 Emma 在美勞角用紙巾和毛線製作白色的晴天娃娃掛在窗前。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0602.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "👦", "en": "It has been drizzling non-stop for three days, Emma. Our soccer practice was cancelled again!", "zh": "Emma，這細雨已經連綿不絕地下了三天了。我們的足球練習又被迫取消了！", "keywords": ["drizzling", "non-stop", "cancelled"] },
      { "id": 2, "speaker": "Emma", "avatar": "👧", "en": "Let's craft Japanese Teru Teru Bozu dolls out of soft white tissues and hang them by the window!", "zh": "那我們用柔軟的白面紙來做幾個日本晴天娃娃，把它們懸掛在窗邊祈求放晴吧！", "keywords": ["Teru Teru Bozu", "tissues", "window"] },
      { "id": 3, "speaker": "Kevin", "avatar": "👦", "en": "How do we make them? Roll a tissue into a tight round ball for the head, right?", "zh": "要怎麼做呢？先把一張紙巾揉成一顆結實的圓球當作頭部，對吧？", "keywords": ["round ball", "head", "roll"] },
      { "id": 4, "speaker": "Emma", "avatar": "👧", "en": "Exactly! Wrap another flat tissue over it, tie the neck securely with red yarn, and draw a huge smiling face.", "zh": "沒錯！外面再覆蓋一張平整的紙巾，用紅毛線把頸部綁緊，然後畫上大大的笑臉。", "keywords": ["yarn", "securely", "smiling face"] },
      { "id": 5, "speaker": "Kevin", "avatar": "👦", "en": "Look at him swinging in the gentle breeze! May tomorrow bring blue skies and radiant sunshine.", "zh": "看他在微風中輕輕擺動！希望明天就能迎來蔚藍的天空與明媚燦爛的陽光。", "keywords": ["swinging", "radiant", "sunshine"] }
    ],
    "vocabulary": [
      { "word": "drizzle", "phonetic": "/ˈdrɪz.əl/", "pos": "v./n.", "zh": "下毛毛細雨、濛濛雨", "example": "A persistent drizzle forced everyone indoors." },
      { "word": "yarn", "phonetic": "/jɑːrn/", "pos": "n.", "zh": "毛線、紡紗線", "example": "Grandmother knitted cozy wool mittens with colorful yarn." },
      { "word": "radiant", "phonetic": "/ˈreɪ.di.ənt/", "pos": "adj.", "zh": "容光煥發的、明亮燦爛的", "example": "The bride wore a radiant smile on her wedding day." }
    ],
    "dailyPhrase": { "en": "Non-stop.", "zh": "連續不斷地、馬不停蹄地。" },
    "cultureTip": "「Teru Teru Bozu（晴天娃娃）」是日本傳統手作祈晴人偶，常用白布或紙巾捏成光頭和尚造型掛在屋簷下，祈求雨過天晴、戶外活動平安順遂。"
  },

  # 06-03 [國中挑戰]
  {
    "id": "dialogue-0603",
    "date": "06-03",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "節慶美食",
    "topic": {
      "en": "Dragon Boat Festival Eve: Traditional Sticky Rice Dumplings",
      "zh": "端午節前夕：跟長輩學包南部粽與北部粽的傳統工藝"
    },
    "situation": "端午節即將到來，David 和 Chloe 在廚房跟長輩一起摺竹葉、填糯米，探討南部粽與北部粽的風味差異。",
    "speakers": {
      "David": { "role": "David", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0603.mp3",
    "dialogue": [
      { "id": 1, "speaker": "David", "avatar": "👦", "en": "Chloe, the aroma of boiled bamboo leaves and braised pork belly in this kitchen is making my mouth water!", "zh": "Chloe，廚房裡飄著煮透的竹葉清香與燉滷五花肉的香味，真讓我口水直流！", "keywords": ["bamboo leaves", "braised", "mouth water"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "Folding two wide bamboo leaves into a leak-proof cone shape takes real finesse. Watch Grandma's agile hands!", "zh": "把兩片寬竹葉摺成不漏米的漏斗形錐形，真的需要純熟手藝。你看奶奶敏捷俐落的手法！", "keywords": ["cone shape", "finesse", "agile"] },
      { "id": 3, "speaker": "David", "avatar": "👦", "en": "Our family prefers southern-style zongzi, wrapping raw glutinous rice and boiling it until soft and chewy.", "zh": "我們家偏愛南部粽，把生糯米與餡料包好後放進大鍋沸水慢煮，口感特別軟糯香黏。", "keywords": ["glutinous rice", "boiling", "chewy"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "My dad grew up with northern-style zongzi, where sticky rice is stir-fried with fragrant shallot oil before steaming.", "zh": "我爸爸則習慣吃北部粽，糯米會先用香蔥油炒香半熟，再包進竹葉放進蒸籠蒸熟，粒粒分明。", "keywords": ["stir-fried", "shallot oil", "steaming"] },
      { "id": 5, "speaker": "David", "avatar": "👦", "en": "Regardless of the culinary style, tucking in salted egg yolk, shiitake mushrooms, and chestnuts is non-negotiable!", "zh": "不論料理手法如何不同，塞進金黃鹹蛋黃、香菇和香甜栗子，絕對是不可或缺的靈魂配料！", "keywords": ["egg yolk", "shiitake", "chestnuts"] },
      { "id": 6, "speaker": "Chloe", "avatar": "👧", "en": "Binding each dumpling tightly with cotton twine ensures they keep their perfect pyramid shape in the pot.", "zh": "用棉繩緊緊綁好每一顆粽子，能確保它們在滾水中依然維持完美的立體四角錐形。", "keywords": ["twine", "pyramid", "binding"] }
    ],
    "vocabulary": [
      { "word": "finesse", "phonetic": "/fɪˈnes/", "pos": "n.", "zh": "嫻熟手腕、精湛技藝", "example": "Decorating wedding cakes requires immense patience and artistic finesse." },
      { "word": "glutinous", "phonetic": "/ˈɡluː.t̬ən.əs/", "pos": "adj.", "zh": "黏糯的、有黏性的", "example": "Glutinous rice is the foundational ingredient for festive dumplings." },
      { "word": "twine", "phonetic": "/twaɪn/", "pos": "n.", "zh": "細繩、線繩", "example": "Secure the parcel with sturdy brown postal twine." }
    ],
    "dailyPhrase": { "en": "Make one's mouth water.", "zh": "令人垂涎三尺、食指大動。" },
    "cultureTip": "台灣端午粽有「南煮北蒸」的文化特色：南部粽（Southern Zongzi）包生米水煮，口感軟糯黏稠；北部粽（Northern Zongzi）先將米與醬汁炒香再蒸，口感粒粒分明Q彈。"
  },

  # 06-04 [國小初階]
  {
    "id": "dialogue-0604",
    "date": "06-04",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "端午童趣",
    "topic": {
      "en": "Dragon Boat Fun: Standing an Egg at Solar Noon",
      "zh": "端午節趣味習俗：正午立蛋大挑戰"
    },
    "situation": "端午節當天中午十二點整，Tyler 和 Amy 蹲在客廳磁磚地板上，小心翼翼嘗試讓生雞蛋直立不倒。",
    "speakers": {
      "Tyler": { "role": "Tyler", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Amy": { "role": "Amy", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0604.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tyler", "avatar": "👦", "en": "Amy, the clock just struck twelve noon! Bring out the raw eggs from the kitchen!", "zh": "Amy，時鐘剛剛敲響正午十二點整！快把廚房裡的生雞蛋拿出來！", "keywords": ["twelve noon", "raw eggs", "clock"] },
      { "id": 2, "speaker": "Amy", "avatar": "👧", "en": "Here is one with a slightly rough shell. It helps balance on flat tile floors.", "zh": "這一顆蛋殼表面稍微有點粗糙。在平整的磁磚地板上比較容易找到平衡點喔。", "keywords": ["rough shell", "balance", "tile floors"] },
      { "id": 3, "speaker": "Tyler", "avatar": "👦", "en": "Hold your breath and keep your fingertips steady. Don't shake!", "zh": "屏住呼吸，指尖保持平穩。千萬別抖手喔！", "keywords": ["fingertips", "steady", "breath"] },
      { "id": 4, "speaker": "Amy", "avatar": "👧", "en": "Look, I slowly let go... and it is standing upright all on its own!", "zh": "你看，我慢慢把手放開了……它居然自己穩穩地立在地面上直立不倒耶！", "keywords": ["upright", "let go", "standing"] },
      { "id": 5, "speaker": "Tyler", "avatar": "👦", "en": "Hooray! Tradition says standing an egg at noon brings good luck for the whole year!", "zh": "太棒了！民俗傳說在端午正午立蛋成功，能帶來整整一整年的好運氣呢！", "keywords": ["good luck", "tradition", "hooray"] }
    ],
    "vocabulary": [
      { "word": "upright", "phonetic": "/ˈʌp.raɪt/", "pos": "adv./adj.", "zh": "直立地、挺直地", "example": "Keep the delicate glass bottles upright during transit." },
      { "word": "balance", "phonetic": "/ˈbæl.əns/", "pos": "v./n.", "zh": "使平衡、均衡", "example": "Gymnasts learn to balance skillfully on narrow beams." },
      { "word": "shell", "phonetic": "/ʃel/", "pos": "n.", "zh": "蛋殼、外殼", "example": "Crack the egg shell gently on the rim of the bowl." }
    ],
    "dailyPhrase": { "en": "Hold your breath.", "zh": "屏住呼吸（形容緊張專注的時刻）。" },
    "cultureTip": "端午節民間傳說在五月初五正午（solar noon），太陽引力與地心引力形成特殊平衡，此時將生雞蛋直立在地面（egg standing）代表迎來一整年的鴻運當頭。"
  },

  # 06-05 [高中進階]
  {
    "id": "dialogue-0605",
    "date": "06-05",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "地球環境",
    "topic": {
      "en": "World Environment Day: Combating Microplastics in Marine Ecosystems",
      "zh": "世界環境日：循環經濟與對抗微塑膠海洋污染思辨"
    },
    "situation": "6月5日世界環境日，高二環保社社長 Ryan 和 Claire 主持校園論壇，深入探討微塑膠顆粒進入全球食物鏈的嚴峻危機。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Claire": { "role": "Claire", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0605.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "Claire, today is United Nations World Environment Day. The global theme calls for accelerating the end of plastic pollution.", "zh": "Claire，今天是聯合國世界環境日。今年的全球倡議主題呼籲全人類加速終結塑膠污染危機。", "keywords": ["World Environment Day", "plastic pollution", "accelerating"] },
      { "id": 2, "speaker": "Claire", "avatar": "👩‍🎓", "en": "The crisis extends far beyond visible trash floating on shores. Microplastics—particles smaller than five millimeters—have infiltrated polar ice, deep trenches, and human bloodstreams.", "zh": "這場危機遠超越海岸邊肉眼可見的漂浮垃圾。小於五毫米的微塑膠顆粒，早已滲透進極地冰川、萬米海溝甚至人類血液循環系統中。", "keywords": ["microplastics", "infiltrated", "trenches"] },
      { "id": 3, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "Synthetic fibers shed during laundry wash cycles and degrading vehicle tires are ubiquitous primary sources.", "zh": "洗衣機洗滌過程中脫落的合成人造纖維，以及磨損分解的汽車輪胎微粒，正是無所不在的主要污染來源。", "keywords": ["synthetic fibers", "ubiquitous", "degrading"] },
      { "id": 4, "speaker": "Claire", "avatar": "👩‍🎓", "en": "Because plastics adsorb toxic chemical pollutants, zooplankton ingest them, biomagnifying toxins as they move up the trophic pyramid.", "zh": "由於塑膠表面極易吸附有毒化學污染物，浮游動物誤食後，毒素便會隨著食物鏈金字塔層層生物累積放大。", "keywords": ["biomagnifying", "trophic pyramid", "zooplankton"] },
      { "id": 5, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "Downstream recycling is inherently inadequate. We must mandate extended producer responsibility and redesign circular biodegradable packaging at the source.", "zh": "下游單純依賴垃圾回收在本質上是治標不治本。我們必須立法推行生產者延伸責任（EPR），並從源頭全面重構循環可生物分解包裝。", "keywords": ["extended producer responsibility", "biodegradable", "inadequate"] },
      { "id": 6, "speaker": "Claire", "avatar": "👩‍🎓", "en": "Protecting our shared biosphere requires structural legal mandates paired with personal refusal of single-use convenience.", "zh": "捍衛我們共同棲居的地球生物圈，既需要嚴格的法規體制約束，也離不開每個人主動拒絕一次性塑膠便利的自覺行動。", "keywords": ["biosphere", "mandates", "refusal"] }
    ],
    "vocabulary": [
      { "word": "infiltrate", "phonetic": "/ˈɪn.fɪl.treɪt/", "pos": "v.", "zh": "滲透、潛入、滲入", "example": "Chemical runoff infiltrated the subterranean aquifer." },
      { "word": "ubiquitous", "phonetic": "/juːˈbɪk.wə.t̬əs/", "pos": "adj.", "zh": "無所不在的、普遍存在的", "example": "Smartphones have become ubiquitous across modern society." },
      { "word": "biodegradable", "phonetic": "/ˌbaɪ.oʊ.dɪˈɡreɪ.də.bəl/", "pos": "adj.", "zh": "可生物分解的、環保易降解的", "example": "Cornstarch utensils are fully biodegradable and compostable." }
    ],
    "dailyPhrase": { "en": "Extend far beyond...", "zh": "遠遠超越……的範圍或界線。" },
    "cultureTip": "6月5日是聯合國世界環境日（World Environment Day）。當代環境科學重點聚焦「微塑膠（Microplastics）」與「生物放大效應（Biomagnification）」，倡導推動源頭減量與生產者延伸責任制度。"
  },

  # 06-06 [國小中高]
  {
    "id": "dialogue-0606",
    "date": "06-06",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "民俗手作",
    "topic": {
      "en": "Crafting Fragrant Herbal Pouches: Driving Away Mosquitoes",
      "zh": "縫製艾草香包：天然草本驅蚊與端午祈福"
    },
    "situation": "端午節的勞作課上，Justin 和 Bella 正在用五彩絲線縫合錦囊香包，裝滿天然艾草與石菖蒲粉末。",
    "speakers": {
      "Justin": { "role": "Justin", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Bella": { "role": "Bella", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0606.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Justin", "avatar": "👦", "en": "Bella, smell this mixture of dried mugwort, calamus, and lavender. It smells earthy and refreshing!", "zh": "Bella，聞聞這份混合了乾燥艾草、石菖蒲與薰衣草的草本粉末。散發著天然質樸又舒爽的香氣！", "keywords": ["mugwort", "calamus", "refreshing"] },
      { "id": 2, "speaker": "Bella", "avatar": "👧", "en": "Those traditional herbs contain natural essential oils that repel buzzing mosquitoes and gnats.", "zh": "那些傳統中草藥富含天然植物精油，能自然驅趕惱人的嗡嗡蚊蟲與小黑蚊。", "keywords": ["herbs", "essential oils", "mosquitoes"] },
      { "id": 3, "speaker": "Justin", "avatar": "👦", "en": "I folded this embroidered silk pouch into a cute miniature triangular zongzi shape.", "zh": "我把這個繡花絲綢小香囊縫折成一個可愛的小巧三角粽形狀呢。", "keywords": ["embroidered", "pouch", "triangular"] },
      { "id": 4, "speaker": "Bella", "avatar": "👧", "en": "Thread this braided five-color cord through the top loop. The five colors symbolize harmony and good health.", "zh": "把這條編織好的五彩絲線穿過頂端的繩圈。五行五色象徵著陰陽調和與四季平安健康。", "keywords": ["braided", "five-color cord", "harmony"] },
      { "id": 5, "speaker": "Justin", "avatar": "👦", "en": "I will pin this fragrant sachet to my school backpack to ward off summer bugs all season long!", "zh": "我要把這個芬芳的小香包別在我的書包上，讓它整整個夏季都替我驅趕小蟲害！", "keywords": ["sachet", "ward off", "backpack"] }
    ],
    "vocabulary": [
      { "word": "mugwort", "phonetic": "/ˈmʌɡ.wɝːt/", "pos": "n.", "zh": "艾草、艾蒿", "example": "Mugwort leaves are traditionally hung beside doorways during festivals." },
      { "word": "braided", "phonetic": "/ˈbreɪ.dɪd/", "pos": "adj.", "zh": "編織的、辮狀編結的", "example": "She tied her hair with a colorful braided ribbon." },
      { "word": "sachet", "phonetic": "/sæʃˈeɪ/", "pos": "n.", "zh": "香包、香囊、小香袋", "example": "Lavender sachets keep wardrobe closets smelling fresh and pleasant." }
    ],
    "dailyPhrase": { "en": "Ward off bugs.", "zh": "驅趕蟲害、抵禦蚊蟲滋擾。" },
    "cultureTip": "端午節配戴「艾草香包（herbal sachets）」源於古代避五毒、防暑驅疫的習俗。香囊內填裝艾草、菖蒲等辛香草藥，搭配象徵五行的五彩繩（five-color cord），是華人兼具防蚊實用與祝福的美麗工藝。"
  },

  # 06-07 [國中挑戰]
  {
    "id": "dialogue-0607",
    "date": "06-07",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "熱血競渡",
    "topic": {
      "en": "Dragon Boat Championship Finals: Snatching the Victory Flag",
      "zh": "端午龍舟總決賽現場：歡呼聲中奪標手飛身奪旗的榮耀瞬間"
    },
    "situation": "河濱公園碼頭觀禮看台上，Julian 和 Hannah 正屏息注視即將衝過終點線的校際龍舟冠亞軍總決賽。",
    "speakers": {
      "Julian": { "role": "Julian", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Hannah": { "role": "Hannah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0607.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Julian", "avatar": "👦", "en": "Hannah, look at lane three and lane four! Both dragon boats are dead even as they approach the five-hundred-meter mark!", "zh": "Hannah，看第三水道和第四水道！兩艘龍舟在逼近最後五百公尺標竿時幾乎完全並駕齊驅！", "keywords": ["dead even", "lane", "dragon boats"] },
      { "id": 2, "speaker": "Hannah", "avatar": "👧", "en": "The thunderous roar of the war drums is vibrating through our chest bones! The spectators along the bank are going wild!", "zh": "戰鼓如雷鳴般的震撼轟響直撼胸膛！河岸兩旁擠滿的加油群眾全都熱血沸騰、瘋狂吶喊！", "keywords": ["thunderous", "drums", "spectators"] },
      { "id": 3, "speaker": "Julian", "avatar": "👦", "en": "Our school's flag-catcher is already leaning far forward over the ornate carved dragon head, extending his right arm.", "zh": "我們學校的奪標手已經飛身跨在雕刻精美的龍頭正上方向前延伸，全力伸展右臂！", "keywords": ["flag-catcher", "ornate", "leaning"] },
      { "id": 4, "speaker": "Hannah", "avatar": "👧", "en": "One final burst of rapid strokes... and he snatched the red victory flag right out of the buoy buoy!", "zh": "最後一波急促破浪的全力划槳……接到了！他從浮標上瞬間一把奪下了象徵勝利的鮮紅冠軍錦旗！", "keywords": ["snatched", "victory flag", "buoy"] },
      { "id": 5, "speaker": "Julian", "avatar": "👦", "en": "We won by a fraction of a second! The paddlers are splashing river water in pure jubilation!", "zh": "我們以不到半秒的微幅差距贏得勝利！所有划手興奮得在大河中狂潑水花、狂歡慶祝！", "keywords": ["fraction of a second", "jubilation", "paddlers"] },
      { "id": 6, "speaker": "Hannah", "avatar": "👧", "en": "All those grueling sunrise training sessions paid off magnificently. What an unforgettable final!", "zh": "那些清晨頂著晨曦刻苦集訓的汗水，終於得到了最耀眼的回報。這真是一場永生難忘的精彩總決賽！", "keywords": ["grueling", "paid off", "unforgettable"] }
    ],
    "vocabulary": [
      { "word": "spectator", "phonetic": "/spekˈteɪ.t̬ɚ/", "pos": "n.", "zh": "現場觀眾、旁觀者", "example": "Cheering spectators packed the grandstands alongside the track." },
      { "word": "jubilation", "phonetic": "/ˌdʒuː.bəlˈeɪ.ʃən/", "pos": "n.", "zh": "歡呼雀躍、狂喜慶祝", "example": "The stadium erupted in jubilation when the home team scored." },
      { "word": "grueling", "phonetic": "/ˈɡruː.ə.lɪŋ/", "pos": "adj.", "zh": "極其艱辛磨人的、考驗意志的", "example": "Marathon runners endured a grueling climb up the steep hill." }
    ],
    "dailyPhrase": { "en": "Pay off magnificently.", "zh": "付出得到極其耀眼豐碩的成果與回報。" },
    "cultureTip": "台灣的龍舟競賽有一項獨步全球的驚險刺激傳統——「奪標（Flag Snatching）」。每艘龍舟最前方設有「奪標手（Flag-catcher）」，在衝線瞬間需趴伏在龍頭上伸臂精準抓取水面浮標上的錦旗，決定勝負。"
  },

  # 06-08 [高中進階]
  {
    "id": "dialogue-0608",
    "date": "06-08",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "海洋保育",
    "topic": {
      "en": "World Oceans Day: Deep-Sea Hydrothermal Vents & Sustainable Fishing",
      "zh": "世界海洋日：守護深海熱泉生態與終結毀滅性過度捕撈"
    },
    "situation": "6月8日世界海洋日，海洋科學研究社的 Ethan 和 Natalie 正在討論公海保護條約與台灣黑潮海洋生態系。",
    "speakers": {
      "Ethan": { "role": "Ethan", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Natalie": { "role": "Natalie", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0608.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ethan", "avatar": "👨‍🎓", "en": "Natalie, today marks World Oceans Day. The ocean covers over seventy percent of Earth's surface and produces half of our oxygen.", "zh": "Natalie，今天是世界海洋日。浩瀚海洋覆蓋了地球超過百分之七十的表面，更製造了我們呼吸所需一半以上的氧氣。", "keywords": ["World Oceans Day", "surface", "oxygen"] },
      { "id": 2, "speaker": "Natalie", "avatar": "👩‍🎓", "en": "Yet anthropogenic impacts are pushing marine biomes to tipping points—ocean acidification, bottom trawling, and illegal unmonitored fishing.", "zh": "然而人為破壞正將海洋生物圈推向崩潰臨界點——海水酸化、毀滅性底拖網捕撈以及非法未受監管的過度濫捕。", "keywords": ["acidification", "bottom trawling", "tipping points"] },
      { "id": 3, "speaker": "Ethan", "avatar": "👨‍🎓", "en": "Off our eastern coast, the warm Kuroshio Current carries rich pelagic biodiversity, from majestic humpback whales to migratory pelagic fish.", "zh": "在我們東部外海，溫暖澎湃的黑潮洋流孕育了豐富的大洋生態系，從壯麗的座頭鯨到各類迴游性大洋魚類皆賴以生存。", "keywords": ["Kuroshio", "pelagic", "biodiversity"] },
      { "id": 4, "speaker": "Natalie", "avatar": "👩‍🎓", "en": "Furthermore, deep-sea hydrothermal vent systems harbor chemosynthetic organisms that might illuminate the very origin of primordial life.", "zh": "不僅如此，龜山島附近的深海熱泉噴口系統孕育著化學合成微生物與怪蟹，甚至可能揭示地球原始生命的起源奧秘。", "keywords": ["hydrothermal", "chemosynthetic", "primordial"] },
      { "id": 5, "speaker": "Ethan", "avatar": "👨‍🎓", "en": "The newly ratified High Seas Treaty establishing protected corridors is a momentous diplomatic breakthrough for international waters.", "zh": "近期剛獲批準建立公海保護區走廊的《公海條約》，正是國際水域保育史上極具里程碑意義的重大外交突破。", "keywords": ["High Seas Treaty", "corridors", "breakthrough"] },
      { "id": 6, "speaker": "Natalie", "avatar": "👩‍🎓", "en": "We must treat the ocean not as an inexhaustible dumpster or pantry, but as the pulsating blue heart of our living planet.", "zh": "我們絕不能再把海洋視為取之不盡的天然倉庫或垃圾桶，而應當把它視為這顆藍色星球生生不息、跳動的心臟。", "keywords": ["inexhaustible", "pulsating", "blue heart"] }
    ],
    "vocabulary": [
      { "word": "acidification", "phonetic": "/əˌsɪd.ə.fəˈkeɪ.ʃən/", "pos": "n.", "zh": "酸化（海水 pH 值下降）", "example": "Ocean acidification impairs shellfish ability to build calcified shells." },
      { "word": "pelagic", "phonetic": "/pəˈlædʒ.ɪk/", "pos": "adj.", "zh": "遠洋的、大洋深海的", "example": "Tuna and swordfish are renowned pelagic migratory species." },
      { "word": "inexhaustible", "phonetic": "/ˌɪn.ɪɡˈzɑː.stə.bəl/", "pos": "adj.", "zh": "用之不竭的、無窮盡的", "example": "Natural resources are fragile, not inexhaustible treasures." }
    ],
    "dailyPhrase": { "en": "Tipping point.", "zh": "臨界點、不可逆轉的質變點。" },
    "cultureTip": "6月8日為聯合國「世界海洋日（World Oceans Day）」。地球大氣中每兩口呼吸就有一口來自海洋浮游植物（Phytoplankton）的光合作用。台灣推廣「海洋永續海鮮指引」，引導消費者支持友善捕撈漁法。"
  },

  # 06-09 [國小初階]
  {
    "id": "dialogue-0609",
    "date": "06-09",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "清涼夏日",
    "topic": {
      "en": "Beat the Summer Heat: Homemade Watermelon & Kiwi Popsicles",
      "zh": "炎炎夏日的救星：自製天然西瓜奇異果冰棒"
    },
    "situation": "初夏炎熱的週日午後，Ben 和 Lily 在廚房動手把新鮮水果泥倒進冰棒模具裡，做健康的雙色水果冰棒。",
    "speakers": {
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Lily": { "role": "Lily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0609.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ben", "avatar": "👦", "en": "Phew, the thermometer on the wall reads thirty-three degrees Celsius! Let's make fruit popsicles!", "zh": "呼，牆上的溫度計顯示已經三十三度了！我們來動手做天然水果冰棒吧！", "keywords": ["thermometer", "Celsius", "popsicles"] },
      { "id": 2, "speaker": "Lily", "avatar": "👧", "en": "Yay! I blended fresh sweet watermelon chunks into rich red juice.", "zh": "太棒了！我剛剛把新鮮香甜的西瓜切塊打成了濃濃的鮮紅果汁。", "keywords": ["blended", "watermelon", "juice"] },
      { "id": 3, "speaker": "Ben", "avatar": "👦", "en": "Fill each plastic popsicle mold halfway with the red puree, and freeze it for one hour.", "zh": "把塑膠冰棒模具倒進半滿的西瓜果泥，然後放進冷凍庫冰一小時。", "keywords": ["mold", "freeze", "puree"] },
      { "id": 4, "speaker": "Lily", "avatar": "👧", "en": "Then we add a layer of blended green kiwi fruit on top to make it look like a watermelon slice with a green rind!", "zh": "接著我們在上面倒入一層打碎的綠色奇異果泥，這樣做出來就像帶有綠色西瓜皮的可愛切片冰棒了！", "keywords": ["kiwi", "rind", "layer"] },
      { "id": 5, "speaker": "Ben", "avatar": "👦", "en": "Stick in wooden handles. Homemade fruit popsicles have zero artificial colors and taste delicious!", "zh": "插上小木棍。親手做的水果冰棒零人工色素，天然又超級美味！", "keywords": ["wooden handles", "artificial", "delicious"] }
    ],
    "vocabulary": [
      { "word": "popsicle", "phonetic": "/ˈpɑːp.sɪ.kəl/", "pos": "n.", "zh": "冰棒、雪糕", "example": "Children enjoyed chilling homemade strawberry popsicles." },
      { "word": "puree", "phonetic": "/pjʊˈreɪ/", "pos": "n./v.", "zh": "果泥、蔬菜泥", "example": "Blend the steamed carrots into a smooth baby puree." },
      { "word": "rind", "phonetic": "/raɪnd/", "pos": "n.", "zh": "厚果皮（瓜皮或柑橘皮）", "example": "Don't discard the watermelon rind; it can be pickled." }
    ],
    "dailyPhrase": { "en": "Beat the heat.", "zh": "消暑解熱、戰勝盛夏高溫。" },
    "cultureTip": "自製水果冰棒（DIY Fruit Popsicles）是美式家庭在夏日消暑的健康首選。運用西瓜的紅（flesh）搭配奇異果的綠（rind），不加精緻糖即可做出視覺口感雙全的純天然冰品。"
  },

  # 06-10 [國中挑戰]
  {
    "id": "dialogue-0610",
    "date": "06-10",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "節氣智慧",
    "topic": {
      "en": "Mangzhong Solar Term: Grain in Ear & the Summer Solstice Transition",
      "zh": "芒種節氣：晚稻播種與芒刺穀物的初夏農事耕作"
    },
    "situation": "時逢二十四節氣中的「芒種」，Tony 和 Clara 走在校園生態田埂旁，討論農人搶種與氣候轉折特點。",
    "speakers": {
      "Tony": { "role": "Tony", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Clara": { "role": "Clara", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0610.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tony", "avatar": "👦", "en": "Clara, today is Mangzhong, literally meaning 'Grain in Ear,' the ninth solar term of the year.", "zh": "Clara，今天正是『芒種』，字面意思是『有芒的穀物可收穫，有芒的作物該播種』，是一年中的第九個節氣。", "keywords": ["Mangzhong", "Grain in Ear", "solar term"] },
      { "id": 2, "speaker": "Clara", "avatar": "👧", "en": "The name refers to awned cereal crops like barley and wheat ripening, while summer rice seedlings must be planted swiftly.", "zh": "這個名稱指的是大麥、小麥等帶有芒刺的麥穗已經成熟，而夏作水稻幼苗則必須搶時間趕緊插秧播種。", "keywords": ["ripening", "seedlings", "swiftly"] },
      { "id": 3, "speaker": "Tony", "avatar": "👦", "en": "There is an ancient folk proverb: 'If you don't plant during Mangzhong, planting later will be in vain.'", "zh": "古代農諺常說：『芒種芒種，樣樣都種；芒種不種，過後落空』，強調搶抓農時的重要性。", "keywords": ["proverb", "in vain", "plant"] },
      { "id": 4, "speaker": "Clara", "avatar": "👧", "en": "It is also known as the busiest farming period. High temperatures paired with relentless rainfall accelerate crop growth.", "zh": "這也被公認為農民整年中最忙碌的時節。高溫搭配豐沛降雨，極大加速了作物的生長節奏。", "keywords": ["accelerate", "relentless", "temperatures"] },
      { "id": 5, "speaker": "Tony", "avatar": "👦", "en": "Just like farmers seizing the critical seasonal window, we must seize this month to consolidate our school studies before finals.", "zh": "就像農夫緊抓關鍵農時節令一樣，我們也必須把握六月的寶貴光陰，在期末考前紮實鞏固學科知識。", "keywords": ["seasonal window", "consolidate", "finals"] },
      { "id": 6, "speaker": "Clara", "avatar": "👧", "en": "Hard work invested during this busy season will guarantee a fruitful autumn harvest.", "zh": "在這忙碌播種的時節所投入的每一分辛勤汗水，必將迎來金秋沉甸甸的豐碩收成。", "keywords": ["harvest", "invested", "fruitful"] }
    ],
    "vocabulary": [
      { "word": "cereal", "phonetic": "/ˈsɪr.i.əl/", "pos": "n./adj.", "zh": "穀物、穀類的", "example": "Wheat and barley are essential cereal crops." },
      { "word": "in vain", "phonetic": "/ɪn veɪn/", "pos": "idiom", "zh": "徒勞無功、白費心機", "example": "All their rescue efforts were in vain against the storm." },
      { "word": "consolidate", "phonetic": "/kənˈsɑː.lə.deɪt/", "pos": "v.", "zh": "鞏固、強化、統整", "example": "Reviewing notes nightly helps consolidate memory." }
    ],
    "dailyPhrase": { "en": "Seize the critical window.", "zh": "把握關鍵時間窗口、搶抓良機。" },
    "cultureTip": "芒種（Grain in Ear）是農曆夏季的重要節氣。「芒」指帶芒刺的麥類成熟收割，「種」指水稻等作物插秧播種。民諺「芒種忙，忙著種」，體現了天地時節催人奮發的農耕哲學。"
  },

  # 06-11 [國小中高]
  {
    "id": "dialogue-0611",
    "date": "06-11",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "校園回憶",
    "topic": {
      "en": "Campus Graduation Interview: Documenting Cherished Memories",
      "zh": "校園畢業特刊採訪：記錄學長姐的珍貴回憶與感激心聲"
    },
    "situation": "身為校刊小記者的 Sammy 和 Noah，拿著錄音筆和記事本在走廊採訪即將畢業的六年級學長姐。",
    "speakers": {
      "Sammy": { "role": "Sammy", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Noah": { "role": "Noah", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0611.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sammy", "avatar": "👧", "en": "Noah, check your microphone batteries. We are interviewing sixth graders for our graduation issue today!", "zh": "Noah，檢查一下你的麥克風電池。我們今天要為校刊畢業特輯採訪六年級的學長姐囉！", "keywords": ["microphone", "graduation issue", "interviewing"] },
      { "id": 2, "speaker": "Noah", "avatar": "👦", "en": "All set! Here comes Leo, the captain of our school basketball team. Let's ask him our first question.", "zh": "準備就緒！我們學校籃球隊隊長 Leo 正好走過來了。我們來向他提第一個問題吧。", "keywords": ["captain", "basketball team", "question"] },
      { "id": 3, "speaker": "Sammy", "avatar": "👧", "en": "Leo, looking back at six wonderful elementary years, what memory stands out as the most unforgettable?", "zh": "Leo 學長，回顧這六年中學生活，哪一段回憶讓您覺得最刻骨銘心、最難忘呢？", "keywords": ["unforgettable", "elementary", "stands out"] },
      { "id": 4, "speaker": "Noah", "avatar": "👦", "en": "He said winning the citywide tournament after trailing by ten points was pure magic, thanks to his teammates' grit.", "zh": "他說在落後十分的絕境下逆轉奪得全市冠軍最夢幻，這全都要感謝隊友們永不放棄的堅毅鬥志。", "keywords": ["tournament", "grit", "trailing"] },
      { "id": 5, "speaker": "Sammy", "avatar": "👧", "en": "Documenting these heartfelt personal narratives in our school gazette preserves precious history for our campus.", "zh": "把這些真摯動人的個人故事記錄在校刊特輯中，為我們校園留存了最珍貴的集體青春記憶。", "keywords": ["heartfelt", "narratives", "gazette"] }
    ],
    "vocabulary": [
      { "word": "grit", "phonetic": "/ɡrɪt/", "pos": "n.", "zh": "堅毅、不屈不撓的勇氣", "example": "Success requires not just raw talent, but tireless grit." },
      { "word": "narrative", "phonetic": "/ˈner.ə.t̬ɪv/", "pos": "n.", "zh": "敘述、故事記述", "example": "Her autobiography is a compelling personal narrative." },
      { "word": "gazette", "phonetic": "/ɡəˈzet/", "pos": "n.", "zh": "刊物、校刊、公報", "example": "The monthly school gazette published student poetry." }
    ],
    "dailyPhrase": { "en": "Stand out.", "zh": "引人注目、脫穎而出、最為鮮明突出。" },
    "cultureTip": "畢業季期間，校園記者團（School Newspaper / Gazette）常製作「Graduation Issue（畢業專刊）」，透過採訪畢業生代表與回顧經典賽事，凝聚校園向心力與傳承校風精神。"
  },

  # 06-12 [高中進階]
  {
    "id": "dialogue-0612",
    "date": "06-12",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "青春啟程",
    "topic": {
      "en": "Drafting the Valedictorian Address: Embracing the Horizon",
      "zh": "撰寫畢業生致詞講稿：在告別的感傷中勇敢迎向廣闊未知"
    },
    "situation": "畢業典禮前夕，高三畢業生代表 Kevin 和 Audrey 在空蕩的禮堂講台前反覆推敲畢業演說講稿。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Audrey": { "role": "Audrey", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0612.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "👨‍🎓", "en": "Audrey, I have rewritten this valedictory opening four times. Balancing nostalgic tribute with forward-looking inspiration is daunting.", "zh": "Audrey，我把這篇畢業代表致詞的開場白重寫了四次。要同時兼顧對過往回憶的感恩與對未來未知的激勵，著實令人戰戰兢兢。", "keywords": ["valedictory", "nostalgic", "daunting"] },
      { "id": 2, "speaker": "Audrey", "avatar": "👩‍🎓", "en": "Avoid well-worn clichés about 'spreading our wings.' Ground your speech in concrete communal milestones our cohort endured together.", "zh": "避開那些陳腔濫調的『展翅高飛』吧。把演說錨定在我們這一屆同學共同經歷過、真切共患難的具體里程碑上。", "keywords": ["clichés", "communal", "cohort"] },
      { "id": 3, "speaker": "Kevin", "avatar": "👨‍🎓", "en": "Like how we navigated remote learning black screens during pandemics, and then revitalized sports day with fierce passion.", "zh": "就像我們曾在疫情中面對黑屏遠距教學的孤寂摸索，隨後又在校運會上用無比的熱情重新點燃整個校園。", "keywords": ["remote learning", "revitalized", "pandemics"] },
      { "id": 4, "speaker": "Audrey", "avatar": "👩‍🎓", "en": "Precisely. Resilience is our generational defining trait. Commencement is not a final destination, but an inflection point toward greater autonomy.", "zh": "正是如此。強韌抗壓正是我們這一代人最鮮明的印記。畢業典禮從來不是句點，而是邁向自主成人道路的重要轉折點。", "keywords": ["inflection point", "resilience", "autonomy"] },
      { "id": 5, "speaker": "Kevin", "avatar": "👨‍🎓", "en": "I will conclude with a call to remain intellectually curious and fundamentally empathetic in an increasingly polarized world.", "zh": "我打算在結尾呼籲大家：在日益兩極化喧囂的世界中，永遠保持心智的好奇探求，並堅守最純粹的慈悲與同理。", "keywords": ["intellectually curious", "polarized", "empathetic"] },
      { "id": 6, "speaker": "Audrey", "avatar": "👩‍🎓", "en": "Deliver that with conviction. When words emanate from raw authenticity, they resonate powerfully in every listener's heart.", "zh": "帶著堅定的信念說出這番話吧。當言辭源於未經雕飾的真誠，它必將在每位聆聽者心間激起強烈而悠長的回響。", "keywords": ["conviction", "authenticity", "resonate"] }
    ],
    "vocabulary": [
      { "word": "valedictory", "phonetic": "/ˌvæl.əˈdɪk.tɚ.i/", "pos": "adj./n.", "zh": "告別的、畢業致詞的", "example": "She delivered an eloquent valedictory address to the graduating class." },
      { "word": "cliché", "phonetic": "/kliːˈʃeɪ/", "pos": "n.", "zh": "陳腔濫調、老生常談", "example": "The commencement speaker avoided tired motivational clichés." },
      { "word": "conviction", "phonetic": "/kənˈvɪk.ʃən/", "pos": "n.", "zh": "堅定信念、深信不疑", "example": "He spoke with passionate moral conviction." }
    ],
    "dailyPhrase": { "en": "Inflection point.", "zh": "轉折點、重大轉捩點。" },
    "cultureTip": "西方畢業典禮中，成績最頂尖或具代表性的學生稱為「Valedictorian（畢業生致辭代表）」，致詞（Valedictory address）通常著重在感謝師長、回顧集體奮鬥歷程，並激勵同儕勇敢承擔社會責任。"
  },

  # 06-13 [國中挑戰]
  {
    "id": "dialogue-0613",
    "date": "06-13",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "畢業紀念",
    "topic": {
      "en": "Graduation Autograph Books: Signatures on School Uniforms",
      "zh": "畢業紀念冊與校服簽名：青春不散場的儀式感"
    },
    "situation": "國三畢業典禮前最後一個下課，Dylan 和 Chloe 拿著油性奇異筆在白色制服上互相簽名寫下祝福。",
    "speakers": {
      "Dylan": { "role": "Dylan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0613.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Dylan", "avatar": "👦", "en": "Chloe, pass me that black permanent marker, please! Everyone is signing the backs of our white school shirts!", "zh": "Chloe，請把那支黑色油性簽字筆遞給我！大家都在我們白色制服襯衫背後簽名留念呢！", "keywords": ["permanent marker", "signing", "shirts"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "Turn around, Dylan! I am writing 'Friends Forever' across your left shoulder with a smiley doodle.", "zh": "轉過身去，Dylan！我在你左肩膀那邊簽上『友情長存』，還畫了一個可愛的笑臉塗鴉。", "keywords": ["Friends Forever", "doodle", "shoulder"] },
      { "id": 3, "speaker": "Dylan", "avatar": "👦", "en": "My shirt is already covered in colorful autographs, funny nicknames, and quotes from our homeroom teacher.", "zh": "我的制服已經密密麻麻寫滿了五顏六色的簽名、搞笑綽號，還有班導師寫給我的勉勵名言。", "keywords": ["autographs", "nicknames", "quotes"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "Don't forget to fill out my graduation autograph album too. There are prompts for favorite memories and future dreams.", "zh": "也別忘了幫我的畢業紀念留言本填寫一頁喔。裡面有最難忘回憶和未來夢想的問答欄位。", "keywords": ["autograph album", "prompts", "dreams"] },
      { "id": 5, "speaker": "Dylan", "avatar": "👦", "en": "Even when we head to different high schools next semester, this signed shirt will be a priceless relic of our youth.", "zh": "即使下學期我們各自升上不同的高中，這件簽滿名字的校服也將成為我們青春最無價的紀念品。", "keywords": ["priceless", "relic", "different high schools"] },
      { "id": 6, "speaker": "Chloe", "avatar": "👧", "en": "Distance will never dilute true camaraderie. Let's promise to keep in touch and support each other always!", "zh": "空間距離永遠沖淡不了真摯的友誼。讓我們打勾勾約定好：常保聯絡，永遠做彼此最堅實的後盾！", "keywords": ["camaraderie", "dilute", "keep in touch"] }
    ],
    "vocabulary": [
      { "word": "autograph", "phonetic": "/ˈɑː.t̬ə.ɡræf/", "pos": "n./v.", "zh": "親筆簽名", "example": "Fans lined up eagerly to get the author's autograph." },
      { "word": "camaraderie", "phonetic": "/ˌkæm.əˈrɑː.dɚ.i/", "pos": "n.", "zh": "同袍情誼、深厚友誼", "example": "Years of shared struggle forged deep camaraderie among teammates." },
      { "word": "priceless", "phonetic": "/ˈpraɪs.ləs/", "pos": "adj.", "zh": "無價的、珍貴極致的", "example": "Her grandmother gave her a priceless antique pendant." }
    ],
    "dailyPhrase": { "en": "Keep in touch.", "zh": "保持聯絡、互通音訊。" },
    "cultureTip": "在台灣與東亞校園中，畢業生在白色制服（School uniform）上互簽姓名與祝福留言，是一項極具象徵意義的告別儀式，封存純真年華的珍貴回憶。"
  },

  # 06-14 [國小初階]
  {
    "id": "dialogue-0614",
    "date": "06-14",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "畢業驪歌",
    "topic": {
      "en": "Farewell Song Under the Flame Tree: Heartfelt Blessings for Seniors",
      "zh": "鳳凰花開的驪歌：給畢業學長姐的真摯祝福"
    },
    "situation": "畢業典禮當天上午，Leo 和 Ruby 佩戴胸花站在走廊，歡送即將步出校園的六年級學長姐。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Ruby": { "role": "Ruby", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0614.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Ruby, the school auditorium is packed with parents and teachers holding colorful bouquets!", "zh": "Ruby，學校大禮堂裡擠滿了家長和老師，手裡都拿著美麗繽紛的花束呢！", "keywords": ["auditorium", "bouquets", "parents"] },
      { "id": 2, "speaker": "Ruby", "avatar": "👧", "en": "The seniors look so tall and mature with red ribbon corsages pinned to their chests.", "zh": "六年級的學長姐胸前別著紅色鍛帶胸花，看起來好高大又好成熟懂事呀。", "keywords": ["corsages", "mature", "ribbon"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "When the school choir began singing the farewell melody, several students wiped away happy tears.", "zh": "當合唱團唱起悠揚溫柔的驪歌旋律時，好幾位大哥哥大姐姐都忍不住悄悄擦拭眼角的淚水。", "keywords": ["melody", "farewell", "tears"] },
      { "id": 4, "speaker": "Ruby", "avatar": "👧", "en": "We clapped our hands loudly as they walked through the balloon arch into the sunny courtyard.", "zh": "當他們走過氣球拱門踏入灑滿陽光的中庭時，我們大家用最熱烈的掌聲為他們喝采。", "keywords": ["clapped", "balloon arch", "courtyard"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Congratulations to all the graduates! We wish them smooth sailing in junior high school!", "zh": "恭喜所有的畢業生！祝他們在國中新生活裡一帆風順、鵬程萬里！", "keywords": ["graduates", "smooth sailing", "congratulations"] }
    ],
    "vocabulary": [
      { "word": "corsage", "phonetic": "/kɔːrˈsɑːʒ/", "pos": "n.", "zh": "胸花、襟花", "example": "Graduates pinned red carnation corsages to their jackets." },
      { "word": "mature", "phonetic": "/məˈtʊr/", "pos": "adj.", "zh": "成熟的、懂事的", "example": "He handled the difficult decision with a mature attitude." },
      { "word": "melody", "phonetic": "/ˈmel.ə.di/", "pos": "n.", "zh": "旋律、曲調", "example": "The gentle flute melody echoed softly through the chapel." }
    ],
    "dailyPhrase": { "en": "Smooth sailing.", "zh": "一帆風顺、順遂無阻。" },
    "cultureTip": "在台灣國小畢業典禮上，在校生通常會唱驪歌送別畢業生，並排列在「氣球拱門（balloon arch）」兩側列隊鼓掌歡送，祝福學長姐在全新求學階段「Smooth sailing（一帆風順）」"
  },

  # 06-15 [國小中高]
  {
    "id": "dialogue-0615",
    "date": "06-15",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "考前備戰",
    "topic": {
      "en": "Final Exam Countdown: Organizing the Comprehensive Review Timetable",
      "zh": "期末考倒數一週：制定全科統整衝刺清單與時間表"
    },
    "situation": "畢業典禮過後，五六年級在校生迎來期末總考倒數，Max 和 Grace 在教室討論如何有系統地複習一整學期的課本內容。",
    "speakers": {
      "Max": { "role": "Max", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Grace": { "role": "Grace", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0615.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Max", "avatar": "👦", "en": "Grace, only seven days remain until our spring semester final exams begin!", "zh": "Grace，距離我們下學期期末考只剩下最後七天倒數了！", "keywords": ["final exams", "countdown", "semester"] },
      { "id": 2, "speaker": "Grace", "avatar": "👧", "en": "Unlike midterms, final exams cover all units taught across the entire semester, so we need a systematic plan.", "zh": "跟期中考不同，期末考涵蓋了一整學期學過的所有單元，所以我們非常需要系統化的複習計畫。", "keywords": ["systematic", "units", "entire semester"] },
      { "id": 3, "speaker": "Max", "avatar": "👦", "en": "I divided my review into three daily sessions: math word problems before dinner, English grammar at night, and social studies in the morning.", "zh": "我把每天的複習分成三個時段：晚餐前算數學應用題、晚間讀英語文法，早晨頭腦清醒時背社會科。", "keywords": ["sessions", "grammar", "social studies"] },
      { "id": 4, "speaker": "Grace", "avatar": "👧", "en": "Don't forget to review our previous quizzes and midterms. Re-solving our past mistakes saves the most time.", "zh": "也別忘了翻翻看之前的隨堂小考和期中考卷。重新做一遍以前錯過的題目最省時間且成效最好。", "keywords": ["quizzes", "mistakes", "re-solving"] },
      { "id": 5, "speaker": "Max", "avatar": "👦", "en": "Great strategy. Let's finish strong and earn ourselves a completely guilt-free summer holiday!", "zh": "好策略。讓我們全力衝刺有始有終，為自己贏得一個毫無罪惡感、暢快痛快的暑假！", "keywords": ["finish strong", "guilt-free", "summer holiday"] }
    ],
    "vocabulary": [
      { "word": "systematic", "phonetic": "/ˌsɪs.təˈmæt̬.ɪk/", "pos": "adj.", "zh": "有系統的、條理分明的", "example": "She conducted a systematic investigation of the laboratory data." },
      { "word": "session", "phonetic": "/ˈseʃ.ən/", "pos": "n.", "zh": "一段時間、時段、會期", "example": "We scheduled a productive two-hour study session." },
      { "word": "strategy", "phonetic": "/ˈstræt̬.ə.dʒi/", "pos": "n.", "zh": "策略、計策", "example": "Pacing yourself is the winning strategy in long-distance running." }
    ],
    "dailyPhrase": { "en": "Finish strong.", "zh": "全力衝刺到底、善始善終完成最後階段。" },
    "cultureTip": "教育學常用「Finish strong」勉勵學生在學期尾聲（final stretch）堅持到底，不因暑假將至而心浮氣躁，用條理分明的計畫（systematic plan）迎接期末評量。"
  },

  # 06-16 [高中進階]
  {
    "id": "dialogue-0616",
    "date": "06-16",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "高效學習",
    "topic": {
      "en": "The Feynman Technique: Solidifying Complex Physics and Chemistry",
      "zh": "費曼學習法實踐：用極簡語言向他人講解，檢驗深度理解"
    },
    "situation": "高中期末考倒數週，自習室裡 Ryan 和 Claire 運用諾貝爾物理獎得主費曼倡導的學習法，互相抽考電磁學概念。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Claire": { "role": "Claire", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0616.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "Claire, I thought I mastered Faraday's Law of electromagnetic induction, but when I attempted the past exam problems, I stalled completely.", "zh": "Claire，我原本以為自己已經搞懂了法拉第電磁感應定律，但剛剛一試著做歷屆考題，整個人就完全卡住了。", "keywords": ["electromagnetic", "Faraday's Law", "stalled"] },
      { "id": 2, "speaker": "Claire", "avatar": "👩‍🎓", "en": "That reveals the classic 'illusion of explanatory depth.' You recognized the equations passively, but hadn't internalized the underlying physics.", "zh": "這正揭露了典型的『解釋深度假象』。你只是被動地認得那些數學方程式，卻尚未真正內化底層的物理本質。", "keywords": ["illusion", "internalized", "passively"] },
      { "id": 3, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "How does the famous Feynman Technique bridge that gap between superficial recognition and true mastery?", "zh": "那著名的費曼學習法究竟是如何彌補表面認得與真正精通之間的鴻溝呢？", "keywords": ["Feynman Technique", "superficial", "mastery"] },
      { "id": 4, "speaker": "Claire", "avatar": "👩‍🎓", "en": "Explain the concept out loud using plain, jargon-free analogies as if teaching an intelligent twelve-year-old.", "zh": "大聲把這個概念用最通俗直白、毫無專業術語的生動比喻解釋出來，就像是在教一位聰明的十二歲孩子一樣。", "keywords": ["analogies", "jargon-free", "plain"] },
      { "id": 5, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "The moment you resort to complicated textbook jargon, you pinpoint the exact boundary of your conceptual ignorance.", "zh": "每當你詞窮、不得不訴諸課本那些複雜拗口的行話術語時，你就能精準定位出自己概念模糊的知識盲區了。", "keywords": ["jargon", "pinpoint", "ignorance"] },
      { "id": 6, "speaker": "Claire", "avatar": "👩‍🎓", "en": "Exactly. Teaching is the ultimate form of active retrieval. Once you can articulate it simply, it becomes permanently etched in your mind.", "zh": "完全沒錯。教學就是最高階的主動提取形式。一旦你能用最簡單的話語講明白，它就會永久烙印在你的思維框架中了。", "keywords": ["retrieval", "articulate", "etched"] }
    ],
    "vocabulary": [
      { "word": "internalize", "phonetic": "/ɪnˈtɝː.nəl.aɪz/", "pos": "v.", "zh": "使內化、深入吸收轉化", "example": "Through practice, musicians internalize the rhythm effortlessly." },
      { "word": "articulate", "phonetic": "/ɑːrˈtɪk.jə.leɪt/", "pos": "v.", "zh": "清晰地表達、清楚說明", "example": "She articulated her scientific thesis with remarkable clarity." },
      { "word": "pinpoint", "phonetic": "/ˈpɪn.pɔɪnt/", "pos": "v.", "zh": "精確指出、查明", "example": "Diagnostic testing helped pinpoint the software error." }
    ],
    "dailyPhrase": { "en": "Bridge the gap.", "zh": "彌補鴻溝、拉近兩者差距。" },
    "cultureTip": "物理學家理查·費曼（Richard Feynman）倡導「費曼學習法（Feynman Technique）」四步驟：選擇概念、教給外行、發現盲點反覆重查、簡化類比。被譽為全世界最高效的終身學習心法。"
  },

  # 06-17 [國中挑戰]
  {
    "id": "dialogue-0617",
    "date": "06-17",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "理化應試",
    "topic": {
      "en": "Navigating Tricky Math Formulas & Avoiding Calculation Pitfalls",
      "zh": "數學與理化考前刷題：避開粗心計算與單位換算陷阱"
    },
    "situation": "國二晚自習時間，Julian 和 Hannah 對照期末考理化與數學模擬試題，互相提醒容易失分的細節。",
    "speakers": {
      "Julian": { "role": "Julian", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Hannah": { "role": "Hannah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0617.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Julian", "avatar": "👦", "en": "Hannah, I just lost eight points on this physics mock exam purely because I forgot to convert kilometers per hour into meters per second!", "zh": "Hannah，我剛剛在這份理化模擬考卷上丟了整整八分，純粹只是因為我忘了把時速公里換算成每秒公尺！", "keywords": ["convert", "mock exam", "physics"] },
      { "id": 2, "speaker": "Hannah", "avatar": "👧", "en": "Unit conversions are notorious traps set by exam writers. Always circle units in the question prompt with a red pen.", "zh": "單位換算向來是出題老師最愛設的經典陷阱。讀題目時一定要用紅筆把題目裡的單位大圈起來。", "keywords": ["conversions", "notorious", "traps"] },
      { "id": 3, "speaker": "Julian", "avatar": "👦", "en": "And in quadratic equations, forgetting to account for negative root solutions threw off my entire final calculation.", "zh": "而且在解一元二次方程式時，漏掉了負根的解，導致我最後整道大題的計算全軍覆沒。", "keywords": ["quadratic", "negative root", "calculation"] },
      { "id": 4, "speaker": "Hannah", "avatar": "👧", "en": "Before submitting your exam paper, allocate the final ten minutes exclusively for reverse auditing your calculations.", "zh": "在交卷前，一定要留出最後十分鐘，專門用來逆向驗算你的計算過程。", "keywords": ["auditing", "allocate", "submitting"] },
      { "id": 5, "speaker": "Julian", "avatar": "👦", "en": "Checking your work backwards really catches careless sign slips and arithmetic blunders.", "zh": "逆向回推檢查真的能及時揪出正負號寫錯和粗心計算的失誤。", "keywords": ["arithmetic", "blunders", "slips"] },
      { "id": 6, "speaker": "Hannah", "avatar": "👧", "en": "Meticulous execution under time pressure is what separates average marks from top-tier scores.", "zh": "在有限的時間壓力下依然能做到嚴謹細緻，正是平庸分數與頂尖高分之間真正的差距。", "keywords": ["meticulous", "pressure", "top-tier"] }
    ],
    "vocabulary": [
      { "word": "notorious", "phonetic": "/noʊˈtɔːr.i.əs/", "pos": "adj.", "zh": "惡名昭彰的、出名的（多用於貶義或難纏）", "example": "That intersection is notorious for traffic congestion." },
      { "word": "meticulous", "phonetic": "/məˈtɪk.jə.ləs/", "pos": "adj.", "zh": "一絲不苟的、嚴謹細緻的", "example": "The watchmaker performed meticulous repairs under a magnifying glass." },
      { "word": "arithmetic", "phonetic": "/əˈrɪθ.mə.tɪk/", "pos": "n.", "zh": "算術、基礎運算", "example": "Mental arithmetic exercises keep cognitive skills sharp." }
    ],
    "dailyPhrase": { "en": "Throw off...", "zh": "擾亂、使……出錯偏差。" },
    "cultureTip": "應考策略中強調「Reverse Auditing（逆向驗算）」，例如用答案回代檢驗方程式、反向推導單位維度（Dimensional analysis），是避免「Careless mistakes（粗心失分）」的最有效習慣。"
  },

  # 06-18 [國小初階]
  {
    "id": "dialogue-0618",
    "date": "06-18",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "整潔收納",
    "topic": {
      "en": "Clearing Study Desks & Sharpening Pencils for Finals",
      "zh": "整理乾淨書桌與削鉛筆：桌面整潔帶來平靜專注的心"
    },
    "situation": "期末考前夕，Lucas 和 Lily 在各自的書桌前整理抽屜、削好鉛筆，並收納不需要的玩具。",
    "speakers": {
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Lily": { "role": "Lily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0618.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lucas", "avatar": "👦", "en": "Lily, I just sharpened five 2B pencils with my crank sharpener. Look how pointy they are!", "zh": "Lily，我剛用手搖削鉛筆機削好了五支 2B 鉛筆。你看筆尖多麼尖整呀！", "keywords": ["sharpened", "crank sharpener", "pointy"] },
      { "id": 2, "speaker": "Lily", "avatar": "👧", "en": "Good job! I cleared away all the scattered comic books and plastic figurines from my desk.", "zh": "做得好！我也把我書桌上散落的漫畫書和小公仔塑膠模型全都收乾淨了。", "keywords": ["scattered", "figurines", "cleared away"] },
      { "id": 3, "speaker": "Lucas", "avatar": "👦", "en": "A tidy, clutter-free desk really helps our eyes focus only on the study notebook.", "zh": "乾淨整齊、沒有雜物的書桌，真的能讓我們的眼睛專注在眼前要複習的課本筆記上。", "keywords": ["clutter-free", "focus", "notebook"] },
      { "id": 4, "speaker": "Lily", "avatar": "👧", "en": "I put my ruler, clean eraser, and transparent pencil pouch right in front of me.", "zh": "我把直尺、乾淨的橡皮擦和透明筆袋端端正正擺在我的正前方。", "keywords": ["transparent", "ruler", "eraser"] },
      { "id": 5, "speaker": "Lucas", "avatar": "👦", "en": "Clean workspace, clear mind! We are fully prepared for tomorrow's exams.", "zh": "桌面乾乾淨淨，思緒清清爽爽！我們已經為明天的考試做好萬全準備了。", "keywords": ["workspace", "prepared", "clear mind"] }
    ],
    "vocabulary": [
      { "word": "pointy", "phonetic": "/ˈpɔɪn.t̬i/", "pos": "adj.", "zh": "尖銳的、尖尖的", "example": "Be careful with the pointy end of the compass." },
      { "word": "clutter-free", "phonetic": "/ˈklʌt̬.ɚ friː/", "pos": "adj.", "zh": "整潔無雜物的、清爽乾淨的", "example": "A clutter-free bedroom promotes deeper, more restful sleep." },
      { "word": "scattered", "phonetic": "/ˈskæt̬.ɚd/", "pos": "adj.", "zh": "散落的、零散分布的", "example": "Autumn leaves lay scattered across the stone steps." }
    ],
    "dailyPhrase": { "en": "Clean workspace, clear mind.", "zh": "環境整潔，思緒澄明。" },
    "cultureTip": "心理學家指出「Visual clutter（視覺雜亂）」會不自覺消耗大腦的認知資源。在考試前清理書桌（Desk decluttering）、備齊文具，能有效建立儀式感並減輕考試焦慮。"
  },

  # 06-19 [國小中高]
  {
    "id": "dialogue-0619",
    "date": "06-19",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "專注方法",
    "topic": {
      "en": "Pomodoro Technique at the Library: Staying Laser-Focused",
      "zh": "圖書館專注學習：體驗番茄鐘時間管理法"
    },
    "situation": "期末考前最後一個週末，Sam 和 Olivia 在圖書館自習，運用番茄鐘（Pomodoro）維持高效專注力。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0619.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Olivia, I set my desk timer for twenty-five minutes. Our first Pomodoro study session begins now!", "zh": "Olivia，我把書桌計時器設定好二十五分鐘了。我們第一個番茄鐘專注時段現在開始！", "keywords": ["timer", "Pomodoro", "session"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👧", "en": "Remember the golden rule: zero distractions during these twenty-five minutes—no talking, no checking phones.", "zh": "記住黃金守則：在這二十五分鐘裡完全零干擾——不說話、不查看手機通知。", "keywords": ["distractions", "golden rule", "twenty-five"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Ding! The gentle vibration just went off. That twenty-five minutes flew by so quickly!", "zh": "叮！計時器的輕柔震動剛剛響起了。那二十五分鐘過得未免也太飛快了吧！", "keywords": ["vibration", "flew by", "went off"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👧", "en": "Now we earn a strict five-minute break. Stand up, stretch your back, and drink a glass of water.", "zh": "現在我們贏得了紮實的五分鐘休息時間。站起來舒展一下背部筋骨，喝杯水休息一下眼睛。", "keywords": ["break", "stretch", "water"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Studying in short sprint intervals prevents brain fatigue and makes reviewing thick chapters feel totally manageable.", "zh": "用短時間衝刺間隔的方式讀書，能徹底防止大腦疲勞，讓複習厚厚的大單元變得輕鬆可控！", "keywords": ["fatigue", "manageable", "intervals"] }
    ],
    "vocabulary": [
      { "word": "distraction", "phonetic": "/dɪˈstræk.ʃən/", "pos": "n.", "zh": "分心、干擾事物", "example": "Turn off social media alerts to eliminate study distractions." },
      { "word": "manageable", "phonetic": "/ˈmæn.ə.dʒə.bəl/", "pos": "adj.", "zh": "易控制處理的、可駕馭的", "example": "Breaking the project into small tasks made it manageable." },
      { "word": "interval", "phonetic": "/ˈɪn.t̬ɚ.vəl/", "pos": "n.", "zh": "間隔、區間時間", "example": "Trains arrive at regular fifteen-minute intervals." }
    ],
    "dailyPhrase": { "en": "Laser-focused.", "zh": "如雷射般高度聚焦專注、全神貫注。" },
    "cultureTip": "「番茄鐘工作法（Pomodoro Technique）」由義大利人弗朗西斯科·齊里洛（Francesco Cirillo）創立，透過「專注25分鐘 + 休息5分鐘」的節奏循環，大幅提升工作效率並消除拖延症。"
  },

  # 06-20 [高中進階]
  {
    "id": "dialogue-0620",
    "date": "06-20",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "人權關懷",
    "topic": {
      "en": "World Refugee Day: Climate Displacement & Global Humanitarian Empathy",
      "zh": "世界難民日：全球氣候難民危機與跨越國界的人道關懷"
    },
    "situation": "6月20日世界難民日，模擬聯合國社團的 Alex 和 Brenda 在演講廳探討氣候變遷引發的全球難民流離失所難題。",
    "speakers": {
      "Alex": { "role": "Alex", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Brenda": { "role": "Brenda", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0620.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Alex", "avatar": "👨‍🎓", "en": "Brenda, today is World Refugee Day. According to the UN Refugee Agency, over one hundred and twenty million individuals are forcibly displaced worldwide.", "zh": "Brenda，今天是世界難民日。根據聯合國難民署統計，全球已有超過一億兩千萬人被迫流離失所。", "keywords": ["World Refugee Day", "displaced", "forcibly"] },
      { "id": 2, "speaker": "Brenda", "avatar": "👩‍🎓", "en": "That staggering figure represents human souls, not mere statistics. Beyond armed conflict, climate catastrophes are increasingly driving mass migration.", "zh": "那個令人震撼的數字代表著一個個活生生的人類靈魂，而非冰冷數字。除了武裝衝突，極端氣候災難正日益成為大規模人口被迫遷徙的推手。", "keywords": ["staggering", "migration", "catastrophes"] },
      { "id": 3, "speaker": "Alex", "avatar": "👨‍🎓", "en": "Rising sea levels threatening low-lying Pacific island nations create 'climate refugees' who possess no legal status under the 1951 Refugee Convention.", "zh": "海平面上升威脅著低窪太平洋島國的生存，製造了在 1951 年《難民公約》現行法律框架下缺乏正式地位的『氣候難民』。", "keywords": ["Refugee Convention", "low-lying", "status"] },
      { "id": 4, "speaker": "Brenda", "avatar": "👩‍🎓", "en": "International legal definitions must evolve proactively. When drought and salinization destroy subsistence farming, flight becomes an existential necessity.", "zh": "國際法定義必須積極與時俱進。當乾旱與土地鹽鹼化徹底摧毀自給自足的農業，逃離家園就成了生存唯一的迫不得已選擇。", "keywords": ["proactively", "salinization", "existential"] },
      { "id": 5, "speaker": "Alex", "avatar": "👨‍🎓", "en": "Refugee integration is an asset rather than a burden; displaced people bring rich cultural diversity, entrepreneurial spirit, and resilience.", "zh": "接納難民融入社會其實是一項寶貴資產而非單純負擔；離鄉背井的人們帶來了豐富的文化多樣性、創業家精神與強韌毅力。", "keywords": ["integration", "resilience", "entrepreneurial"] },
      { "id": 6, "speaker": "Brenda", "avatar": "👩‍🎓", "en": "Empathy requires recognizing that in a volatile interconnected biosphere, any of us could one day find ourselves seeking refuge.", "zh": "真正的同理心源於深刻認知：在動盪脆弱、休戚與共的地球生物圈中，我們任何人都可能在未來的某一天，成為尋求庇護的一方。", "keywords": ["volatile", "seeking refuge", "biosphere"] }
    ],
    "vocabulary": [
      { "word": "staggering", "phonetic": "/ˈstæɡ.ɚ.ɪŋ/", "pos": "adj.", "zh": "令人震驚的、難以置信的龐大", "example": "The disaster caused a staggering amount of infrastructural damage." },
      { "word": "existential", "phonetic": "/ˌeɡ.zɪˈsten.ʃəl/", "pos": "adj.", "zh": "關乎生存的、生死存亡的", "example": "Climate disruption poses an existential challenge to island habitats." },
      { "word": "volatile", "phonetic": "/ˈvɑː.lə.t̬əl/", "pos": "adj.", "zh": "不穩定的、易動盪多變的", "example": "Commodity markets remained volatile throughout the trade embargo." }
    ],
    "dailyPhrase": { "en": "Seek refuge.", "zh": "尋求庇護、避難尋求安身立命之所。" },
    "cultureTip": "6月20日是聯合國「世界難民日（World Refugee Day）」。現代社會學倡導將難民議題從單純的邊境管制提升至「氣候正義（Climate Justice）」與人道尊嚴的高度，強調沒有人會甘願拋棄故鄉，除非故鄉已成為險境。"
  },

  # 06-21 [國中挑戰]
  {
    "id": "dialogue-0621",
    "date": "06-21",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "夏至天象",
    "topic": {
      "en": "Summer Solstice: The Longest Day of the Year & Sundial Shadows",
      "zh": "夏至節氣：一年中白晝最長的一天與日晷倒影觀測"
    },
    "situation": "二十四節氣迎來「夏至」，地理科學社的 Tony 和 Clara 在校園日晷台旁測量正午時分一年中最短的影子。",
    "speakers": {
      "Tony": { "role": "Tony", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Clara": { "role": "Clara", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0621.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tony", "avatar": "👦", "en": "Clara, look at the brass sundial at noon today! The shadow cast by the gnomon is shorter than on any other day of the entire year!", "zh": "Clara，看今天正午的黃銅日晷！日晷針投射出的影子比整整一年中任何一天都要短得多！", "keywords": ["sundial", "gnomon", "shadow"] },
      { "id": 2, "speaker": "Clara", "avatar": "👧", "en": "That is because today is the Summer Solstice! The sun shines directly over the Tropic of Cancer at twenty-three point five degrees north.", "zh": "那是因為今天正是『夏至』！太陽直射在北緯二十三點五度的北回歸線上。", "keywords": ["Summer Solstice", "Tropic of Cancer", "directly"] },
      { "id": 3, "speaker": "Tony", "avatar": "👦", "en": "In the Northern Hemisphere, today has the longest daylight hours and the briefest night of the entire year.", "zh": "在北半球，今天擁有全年度最漫長的白晝日光照射時數，以及最短暫的黑夜。", "keywords": ["Northern Hemisphere", "daylight hours", "briefest"] },
      { "id": 4, "speaker": "Clara", "avatar": "👧", "en": "In Chiayi and Hualien along the Tropic of Cancer, if you stand outdoors at solar noon, your shadow completely disappears under your shoes!", "zh": "在嘉義與花蓮的北回歸線標線處，如果在正午時分站在戶外，你的影子甚至會完全隱沒在鞋底之下、『立竿無影』呢！", "keywords": ["disappears", "solar noon", "Tropic of Cancer"] },
      { "id": 5, "speaker": "Tony", "avatar": "👦", "en": "Folk wisdom advises: 'Eating noodles on Summer Solstice cools the body.' Let's grab some cold sesame noodles after school!", "zh": "民間俗話說：『冬至餃子夏至麵』。放學後我們一起去吃碗清涼開胃的麻醬涼麵消消暑吧！", "keywords": ["Summer Solstice", "noodles", "folk wisdom"] },
      { "id": 6, "speaker": "Clara", "avatar": "👧", "en": "Count me in! Celebrating seasonal astronomical shifts with tasty traditional food is my favorite pastime.", "zh": "算我一份！用美味的傳統應景美食來慶祝季節天文節氣的轉折，是我最喜歡的樂趣了。", "keywords": ["astronomical", "pastime", "celebrating"] }
    ],
    "vocabulary": [
      { "word": "solstice", "phonetic": "/ˈsɑːl.stɪs/", "pos": "n.", "zh": "至日（夏至或冬至）", "example": "The winter solstice brings the longest night of the year." },
      { "word": "gnomon", "phonetic": "/ˈnoʊ.mɑːn/", "pos": "n.", "zh": "日晷指標、日晷針", "example": "The angled gnomon casts a solar shadow across the hour dial." },
      { "word": "astronomical", "phonetic": "/ˌæs.trəˈnɑː.mɪ.kəl/", "pos": "adj.", "zh": "天文學的、天體的", "example": "Ancient monuments aligned with extraordinary astronomical precision." }
    ],
    "dailyPhrase": { "en": "Disappear under one's shoes.", "zh": "立竿無影、影子完全隱沒在腳底。" },
    "cultureTip": "「夏至（Summer Solstice）」是北半球白晝最長的一天。北回歸線（Tropic of Cancer）正好橫貫台灣嘉義與花蓮，夏至正午太陽直射頭頂，會出現特殊的「立竿無影」奇景。傳統飲食習慣有「冬至湯圓夏至麵（Eating cold noodles）」之說。"
  },

  # 06-22 [國小初階]
  {
    "id": "dialogue-0622",
    "date": "06-22",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "期末應援",
    "topic": {
      "en": "First Day of Finals: Taking a Deep Breath and Reading Carefully",
      "zh": "期末考首日：冷靜沉著、細心讀題作答"
    },
    "situation": "期末考第一天第一節考試鐘聲即將敲響，教室裡 Leo 和 Ruby 坐在各自座位上，互相微笑道加油。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Ruby": { "role": "Ruby", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0622.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Ruby, the teacher is handing out the Mandarin exam papers now. My heart is beating a little fast.", "zh": "Ruby，老師正在分發國語科期末考卷了。我的心跳稍微有點加快呢。", "keywords": ["handing out", "exam papers", "beating fast"] },
      { "id": 2, "speaker": "Ruby", "avatar": "👧", "en": "Take three slow deep breaths with me, Leo. Inhale calm, exhale worry.", "zh": "跟我一起慢慢深呼吸三次，Leo。吸入冷靜，吐出擔憂。", "keywords": ["deep breaths", "inhale", "exhale"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Phew, that really helps relax my shoulders. I will read each question twice before picking an answer.", "zh": "呼，這真的讓我的肩膀放鬆下來了。在選答案前我一定會把每個題目看兩遍。", "keywords": ["relax", "twice", "picking"] },
      { "id": 4, "speaker": "Ruby", "avatar": "👧", "en": "And write your stroke order neatly so the teacher can grade smoothly.", "zh": "還有國字筆畫筆順要寫得工整端正，這樣老師批改起來一目了然。", "keywords": ["stroke order", "neatly", "grade"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "We reviewed diligently all week. Let's do our personal best. Good luck!", "zh": "我們這整週都複習得非常勤奮。發揮出自己的最佳實力吧。祝我們考試順利！", "keywords": ["diligently", "personal best", "good luck"] }
    ],
    "vocabulary": [
      { "word": "inhale", "phonetic": "/ɪnˈheɪl/", "pos": "v.", "zh": "吸氣、吸入", "example": "Inhale deeply through your nose during meditation." },
      { "word": "diligently", "phonetic": "/ˈdɪl.ə.dʒənt.li/", "pos": "adv.", "zh": "勤奮地、孜孜不倦地", "example": "Students studied diligently throughout the exam week." },
      { "word": "neatly", "phonetic": "/ˈniːt.li/", "pos": "adv.", "zh": "整齊地、工整端正地", "example": "She arranged her notebooks neatly inside the backpack." }
    ],
    "dailyPhrase": { "en": "Do one's personal best.", "zh": "發揮出自己的最佳實力。" },
    "cultureTip": "教育心理學提倡「Inhale calm, exhale worry（吸進平靜，吐出擔憂）」的腹式深呼吸技巧，能迅速降低臨場考試交感神經亢奮，讓思維重回理性澄澈狀態。"
  },

  # 06-23 [國小中高]
  {
    "id": "dialogue-0623",
    "date": "06-23",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "沉著應試",
    "topic": {
      "en": "Wrapping Up Science & Social Studies: Looking Forward Calmly",
      "zh": "考完自然與社會科：放下成績焦慮，專注迎戰明天的最終局"
    },
    "situation": "期末考第一天結束放學前，Max 和 Grace 走出考場，談論如何不被已經考完的科目牽絆情緒。",
    "speakers": {
      "Max": { "role": "Max", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Grace": { "role": "Grace", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0623.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Max", "avatar": "👦", "en": "Grace, day one of finals is officially behind us! That science question on circuit boards was quite intricate.", "zh": "Grace，期末考第一天終於正式結束了！自然科考卷上那題電路串並聯題目真的挺複雜精細的。", "keywords": ["day one", "circuit boards", "intricate"] },
      { "id": 2, "speaker": "Grace", "avatar": "👧", "en": "I paused on that one too, but remember: once you turn in the test paper, dwell no more on the score.", "zh": "我也在那題停頓想了很久，但記住：考卷一交出去，就別再去糾結分數了。", "keywords": ["turn in", "dwell no more", "score"] },
      { "id": 3, "speaker": "Max", "avatar": "👦", "en": "Some students are frantically cross-checking answers in the hallway and getting anxious.", "zh": "走廊上已經有一些同學在急切地對答案，結果越對越焦慮煩躁。", "keywords": ["cross-checking", "anxious", "hallway"] },
      { "id": 4, "speaker": "Grace", "avatar": "👧", "en": "Worrying about past answers won't add a single mark, but it will sap your mental energy for tomorrow's math and English.", "zh": "為已經交卷的答案煩惱不會多加任何一分，只會白白消耗你用來準備明天數學與英文的寶貴精力。", "keywords": ["sap", "mental energy", "worrying"] },
      { "id": 5, "speaker": "Max", "avatar": "👦", "en": "Wise advice. Let's go home, enjoy a nutritious dinner, get plenty of sleep, and finish tomorrow with a triumphant smile!", "zh": "充滿智慧的建議。我們回家好好吃一頓營養的晚餐、睡個好覺，明天帶著自信勝利的微笑迎接最後一戰！", "keywords": ["nutritious dinner", "triumphant smile", "sleep"] }
    ],
    "vocabulary": [
      { "word": "intricate", "phonetic": "/ˈɪn.trə.kət/", "pos": "adj.", "zh": "錯綜複雜的、精細的", "example": "The maze had an intricate pattern of dead ends." },
      { "word": "sap", "phonetic": "/sæp/", "pos": "v.", "zh": "消耗、逐漸削弱（精力或元氣）", "example": "Constant anxiety sapped his physical stamina." },
      { "word": "cross-check", "phonetic": "/ˈkrɑːsˌtʃek/", "pos": "v.", "zh": "交叉比對、核對", "example": "Scientists cross-check experimental readings to ensure accuracy." }
    ],
    "dailyPhrase": { "en": "Dwell no more on...", "zh": "不再糾結於……、不再反覆掛懷。" },
    "cultureTip": "教育心理學者指出「Post-exam rumination（考後反芻焦慮）」會嚴重損害認知功能。考完立即對答案無助於成績改變，將專注力迅速移轉至即將面臨的下一個挑戰才是成熟學習者的強韌心態。"
  },

  # 06-24 [國中挑戰]
  {
    "id": "dialogue-0624",
    "date": "06-24",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "如釋重負",
    "topic": {
      "en": "Finals Are Over! Unwinding, Cheering & Infinite Relief",
      "zh": "期末考試交卷那一刻！如釋重負的歡呼與大口喝珍奶"
    },
    "situation": "最後一堂期末考鐘聲悠長敲響，Dylan 和 Chloe 踏出考場長廊，感受整學期課業壓力煙消雲散的無比暢快。",
    "speakers": {
      "Dylan": { "role": "Dylan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0624.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Dylan", "avatar": "👦", "en": "Listen to that final bell chiming, Chloe! Pencils down! The semester exams are officially over!", "zh": "Chloe，聽聽那最後一聲鐘聲敲響！放下鉛筆！這個學期的期末考正式宣告結束囉！", "keywords": ["final bell", "pencils down", "officially over"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "I feel an incredible surge of liberation! It feels as though a hundred-pound boulder evaporated off my chest.", "zh": "我感到一股前所未有的無比解脫！感覺好像胸口上一塊百斤重的巨石瞬間蒸發了一樣輕鬆。", "keywords": ["liberation", "boulder", "evaporated"] },
      { "id": 3, "speaker": "Dylan", "avatar": "👦", "en": "Those sleepless nights reviewing geometry proofs and periodic tables are finally behind us.", "zh": "那些熬夜複習幾何證明題和化學元素週期表的夜晚，終於都成為過去式了。", "keywords": ["periodic tables", "geometry proofs", "sleepless"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "Let's celebrate immediately! How about walking over to the bubble tea shop for brown sugar boba milk with extra ice?", "zh": "我們現在馬上就去慶祝！不如走到街角的珍珠奶茶店，買杯加滿碎冰的黑糖珍珠鮮奶怎麼樣？", "keywords": ["celebrate", "boba milk", "bubble tea"] },
      { "id": 5, "speaker": "Dylan", "avatar": "👦", "en": "Yes! And tonight I am playing cooperative video games with my squad until midnight without a shred of guilt!", "zh": "太贊成了！而且今晚我要跟戰隊隊友連線打協力電玩打到午夜，毫無一絲一毫的罪惡感！", "keywords": ["video games", "midnight", "guilt"] },
      { "id": 6, "speaker": "Chloe", "avatar": "👧", "en": "We fought hard and saw this semester through to the end. Cheers to freedom and the approaching summer vacation!", "zh": "我們堅持拚搏，並有始有終走完了這個學期。為自由與即將到來的盛夏假期乾杯！", "keywords": ["cheers", "freedom", "summer vacation"] }
    ],
    "vocabulary": [
      { "word": "liberation", "phonetic": "/ˌlɪb.əˈreɪ.ʃən/", "pos": "n.", "zh": "解放、解脫、釋放", "example": "Finishing her dissertation gave her a profound sense of liberation." },
      { "word": "evaporate", "phonetic": "/ɪˈvæp.ə.reɪt/", "pos": "v.", "zh": "蒸發、煙消雲散", "example": "Morning fog evaporated quickly under the blazing summer sun." },
      { "word": "boulder", "phonetic": "/ˈboʊl.dɚ/", "pos": "n.", "zh": "巨石、大圓石", "example": "Hikers navigated around giant granite boulders along the path." }
    ],
    "dailyPhrase": { "en": "Without a shred of guilt.", "zh": "毫無一絲一毫的愧疚感。" },
    "cultureTip": "學生在考完期末考那一刻常高喊「Pencils down! Exams are over!」，適度犒賞自己享用最愛的美食甜點或盡情放鬆，有助於身心從高度緊繃的備考狀態平穩過渡。"
  },

  # 06-25 [高中進階]
  {
    "id": "dialogue-0625",
    "date": "06-25",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "自我審計",
    "topic": {
      "en": "Semester-End Self-Audit: Mentally Preparing for Senior High Year Three",
      "zh": "學期總結與自我審計：從高二升上高三的心理調適與長遠規劃"
    },
    "situation": "高中期末考後，高二即將升上高三的 Sean 和 Melody 坐在校園林蔭石桌旁，認真復盤高二一整年的學習與課外活動累積。",
    "speakers": {
      "Sean": { "role": "Sean", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Melody": { "role": "Melody", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0625.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sean", "avatar": "👨‍🎓", "en": "Melody, now that our tenth and eleventh grades are fully complete, the looming reality of being high school seniors is setting in.", "zh": "Melody，高一和高二課業現在已經全數畫下句點，即將升上高三頂峰的現實感油然而生。", "keywords": ["looming", "seniors", "reality"] },
      { "id": 2, "speaker": "Melody", "avatar": "👩‍🎓", "en": "It is a profound transitional juncture. Before diving impulsively into summer break, conducting a holistic self-audit is indispensable.", "zh": "這是一個深刻的重要轉折節點。在貿然放鬆投入暑假前，為自己做一場全方位的深度自我復盤是不可或缺的。", "keywords": ["transitional", "juncture", "self-audit"] },
      { "id": 3, "speaker": "Sean", "avatar": "👨‍🎓", "en": "Looking back over this past academic year, my club leadership and science fair project developed real-world problem-solving abilities.", "zh": "回顧過去這一學年，社團幹部歷練與科展專案確實磨礪了我解決真實世界複雜問題的能力。", "keywords": ["problem-solving", "leadership", "science fair"] },
      { "id": 4, "speaker": "Melody", "avatar": "👩‍🎓", "en": "However, standardized college entrance examinations demand rigorous foundational consistency across literature, math, and foreign languages.", "zh": "然而，大學升學大考需要的是在國英數等核心學科上極其嚴謹穩固的底層基礎與持久一致性。", "keywords": ["standardized", "consistency", "foundational"] },
      { "id": 5, "speaker": "Sean", "avatar": "👨‍🎓", "en": "I plan to utilize the upcoming two-month summer vacation to systematically review all first- and second-year core curricula.", "zh": "我打算善用即將到來的兩個月暑假，把高一高二的核心課綱教材完整、系統化地全面地毯式複習一遍。", "keywords": ["curricula", "vacation", "systematically"] },
      { "id": 6, "speaker": "Melody", "avatar": "👩‍🎓", "en": "He who prepares early triumphs with serenity. Let's enter our final high school chapter with unflinching resolve and clarity of purpose.", "zh": "凡事預則立，早做準備者方能篤定從容。讓我們懷抱堅定不移的決心與清晰目標，邁向高中最後的輝煌篇章！", "keywords": ["serenity", "unflinching", "triumphs"] }
    ],
    "vocabulary": [
      { "word": "juncture", "phonetic": "/ˈdʒʌŋk.tʃɚ/", "pos": "n.", "zh": "特定時刻、重要關頭、轉折點", "example": "At this critical juncture, the board decided to revise the company strategy." },
      { "word": "unflinching", "phonetic": "/ʌnˈflɪn.tʃɪŋ/", "pos": "adj.", "zh": "堅定不移的、毫不退縮畏懼的", "example": "Her unflinching courage inspired the entire emergency rescue squad." },
      { "word": "serenity", "phonetic": "/səˈren.ə.t̬i/", "pos": "n.", "zh": "平靜、從容篤定、寧靜", "example": "She maintained inner serenity amidst the chaotic courtroom proceedings." }
    ],
    "dailyPhrase": { "en": "Clarity of purpose.", "zh": "目標明確清晰、心無旁騖。" },
    "cultureTip": "高中升三年級前的暑假被視為升學備考的「黃金分水嶺（Golden Watershed）」。進行「Self-Audit（個人學習審計復盤）」，誠實盤點學科強弱項，能讓暑期複習計畫精準對焦、事半功倍。"
  },

  # 06-26 [國小初階]
  {
    "id": "dialogue-0626",
    "date": "06-26",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "班級大掃除",
    "topic": {
      "en": "End-of-Semester Classroom Clean-Up: Scrubbing Desks & Emptying Lockers",
      "zh": "教室大掃除與整理儲物櫃：乾乾淨淨放暑假"
    },
    "situation": "考完後的週四下午，全班齊心協力進行學期末大掃除，Ben 和 Ruby 拿著抹布和掃帚分工清潔教室。",
    "speakers": {
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Ruby": { "role": "Ruby", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0626.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ben", "avatar": "👦", "en": "Ruby, dip this cleaning sponge into the soapy water bucket and squeeze it out.", "zh": "Ruby，把這塊清潔海綿浸進肥皂水桶裡，然後用力擰乾。", "keywords": ["sponge", "bucket", "soapy water"] },
      { "id": 2, "speaker": "Ruby", "avatar": "👧", "en": "I am scrubbing away pencil smudges and tape residues from our wooden desks.", "zh": "我正在把木課桌上的鉛筆黑污痕跡和透明膠帶殘膠用力擦洗乾淨呢。", "keywords": ["scrubbing", "smudges", "residues"] },
      { "id": 3, "speaker": "Ben", "avatar": "👦", "en": "Look at our personal lockers! I emptied out all old test papers, craft projects, and my spare gym shoes.", "zh": "你看我們的置物櫃！我把所有舊考卷、美術作品還有備用運動鞋全清空整理好了。", "keywords": ["lockers", "emptied out", "craft projects"] },
      { "id": 4, "speaker": "Ruby", "avatar": "👧", "en": "The classroom floor looks sparkling clean after sweeping and mopping!", "zh": "掃地拖地之後，整間教室的地板看起來亮晶晶、一塵不染！", "keywords": ["sparkling clean", "sweeping", "mopping"] },
      { "id": 5, "speaker": "Ben", "avatar": "👦", "en": "Leaving our classroom neat and tidy is the best way to conclude our school year.", "zh": "把教室整理得乾淨整潔，就是為我們這一學年畫上最棒句點的方式。", "keywords": ["neat and tidy", "conclude", "school year"] }
    ],
    "vocabulary": [
      { "word": "smudge", "phonetic": "/smʌdʒ/", "pos": "n.", "zh": "污漬、污跡、塗抹痕跡", "example": "Wipe away the black pencil smudge with a damp cloth." },
      { "word": "residue", "phonetic": "/ˈrez.ə.duː/", "pos": "n.", "zh": "殘留物、殘膠", "example": "Rubbing alcohol effectively removes sticky sticker residue." },
      { "word": "mop", "phonetic": "/mɑːp/", "pos": "v./n.", "zh": "拖地、拖把", "example": "She mopped the kitchen floor with pine-scented cleaner." }
    ],
    "dailyPhrase": { "en": "Neat and tidy.", "zh": "整齊乾淨、井井有條。" },
    "cultureTip": "學期末大掃除（End-of-semester clean-up）是校園生活的重要傳統。徹底清空個人儲物櫃（lockers）並將桌椅洗刷一新，培養孩子對公共環境的責任感與惜物美德。"
  },

  # 06-27 [國小中高]
  {
    "id": "dialogue-0627",
    "date": "06-27",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "榮譽與成長",
    "topic": {
      "en": "Receiving Report Cards & Certificates of Merit: Celebrating Growth",
      "zh": "領取成績單與榮譽獎狀：肯定一學期的辛勤耕耘與進步"
    },
    "situation": "結業式前夕，班導師頒發期末成績單與進步獎狀，Eric 和 Mia 坐在座位上開心地互相分享評語。",
    "speakers": {
      "Eric": { "role": "Eric", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0627.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Eric", "avatar": "👦", "en": "Mia, our teacher just handed us our sealed semester report cards!", "zh": "Mia，老師剛剛把密封好的學期成績單發到我們手上了！", "keywords": ["report cards", "sealed", "semester"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "Open it gently! Look at your math grade—you jumped from eighty to ninety-five points!", "zh": "輕輕拆開來看看！看你的數學成績——你從八十分大幅躍升到了九十五分呢！", "keywords": ["math grade", "jumped", "points"] },
      { "id": 3, "speaker": "Eric", "avatar": "👦", "en": "And look at your certificate of merit for outstanding peer support and English excellence!", "zh": "還有看你拿到的這張榮譽獎狀：熱心助人模範與英語傑出表現獎！", "keywords": ["certificate of merit", "outstanding", "excellence"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "The teacher's written remarks said: 'Mia consistently demonstrates curiosity and empathy in team activities.'", "zh": "老師在評語欄寫著：『Mia 在團隊活動中始終展現旺盛的好奇心與同理心。』", "keywords": ["remarks", "consistently", "empathy"] },
      { "id": 5, "speaker": "Eric", "avatar": "👦", "en": "Scores are important, but witnessing how much wiser and kinder we have grown this semester is the truest prize.", "zh": "分數固然重要，但見證我們這學期變得多麼懂事、多麼善良有愛，才是最貨真價實的獎賞。", "keywords": ["truest prize", "grown", "wiser"] }
    ],
    "vocabulary": [
      { "word": "certificate", "phonetic": "/sɚˈtɪf.ə.kət/", "pos": "n.", "zh": "證書、獎狀、執照", "example": "He proudly framed his academic achievement certificate." },
      { "word": "merit", "phonetic": "/ˈmer.ɪt/", "pos": "n.", "zh": "優點、功績、值得讚賞之處", "example": "Students received awards based on academic and moral merit." },
      { "word": "remark", "phonetic": "/rɪˈmɑːrk/", "pos": "n./v.", "zh": "評語、評論、話語", "example": "The teacher wrote encouraging remarks on her essay." }
    ],
    "dailyPhrase": { "en": "Certificate of merit.", "zh": "榮譽獎狀、表現優異獎。" },
    "cultureTip": "現代教育強調「Growth Mindset（成長型思維）」，成績單（Report Card）上的「Teacher's Remarks（導師評語）」與多元評量榮譽狀，著重肯定孩子的學習態度、同理心與進步幅度，而非單一排名。"
  },

  # 06-28 [國中挑戰]
  {
    "id": "dialogue-0628",
    "date": "06-28",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "暑假企劃",
    "topic": {
      "en": "Crafting an Inspiring Summer Bucket List: Reading, Sports & New Skills",
      "zh": "擬定充實的暑假心願清單：運動、自主閱讀與解鎖一門新技能"
    },
    "situation": "暑假前最後一個週五下午，David 和 Chloe 在咖啡館各自攤開手帳，認真寫下今年夏天的個人探索清單。",
    "speakers": {
      "David": { "role": "David", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0628.mp3",
    "dialogue": [
      { "id": 1, "speaker": "David", "avatar": "👦", "en": "Chloe, let's establish our official summer bucket lists right now so we don't squander two months in mindless scrolling.", "zh": "Chloe，我們現在就來把正式的暑假心願清單列好，免得這兩個月在漫無目的滑手機中被白白浪費掉。", "keywords": ["bucket list", "squander", "scrolling"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "I completely agree! My top goal is reading eight classic fiction novels and finishing a Python coding basics course online.", "zh": "我完全同意！我的第一目標是閱讀八本經典文學小說，並在線上修完一套 Python 程式設計基礎課程。", "keywords": ["classic fiction", "Python", "coding"] },
      { "id": 3, "speaker": "David", "avatar": "👦", "en": "Awesome. My fitness goal is swimming one kilometer three times a week and learning how to play acoustic guitar fingerstyle.", "zh": "太酷了。我的體能目標是每週游三次一千公尺，並且學會木吉他指彈演奏技巧。", "keywords": ["acoustic guitar", "fingerstyle", "fitness"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "Let's also schedule a weekend hiking expedition to the high mountain trails with our families in mid-July.", "zh": "我們七月中旬也跟家人安排一趟週末高山登山步道探險之旅吧。", "keywords": ["expedition", "trails", "hiking"] },
      { "id": 5, "speaker": "David", "avatar": "👦", "en": "Setting concrete milestones and maintaining mutual accountability guarantees our vacation remains vibrant.", "zh": "設定具體目標節點並互相監督提醒，能確保我們的長假過得充實精彩、活力滿滿。", "keywords": ["accountability", "milestones", "vibrant"] },
      { "id": 6, "speaker": "Chloe", "avatar": "👧", "en": "Summer is the canvas, and we are the artists. Let's make this vacation our masterpiece!", "zh": "夏天就像一張純白的畫布，而我們就是揮毫的畫家。讓我們把這個暑假創造成屬於自己的傑作吧！", "keywords": ["canvas", "artists", "masterpiece"] }
    ],
    "vocabulary": [
      { "word": "squander", "phonetic": "/ˈskwɑːn.dɚ/", "pos": "v.", "zh": "浪費、揮霍、虛度（時間或金錢）", "example": "Don't squander precious holiday mornings sleeping past noon." },
      { "word": "expedition", "phonetic": "/ˌek.spəˈdɪʃ.ən/", "pos": "n.", "zh": "遠征、探險考察", "example": "The scientific expedition explored untouched rainforest caves." },
      { "word": "masterpiece", "phonetic": "/ˈmæs.tɚ.piːs/", "pos": "n.", "zh": "傑作、名作、代表作", "example": "The painting is celebrated worldwide as an artistic masterpiece." }
    ],
    "dailyPhrase": { "en": "Summer bucket list.", "zh": "暑假心願清單、暑期必做計畫。" },
    "cultureTip": "「Bucket List（願望清單）」源於英文俚語。在歐美學生文化中，放暑假前擬定「Summer Bucket List」，將學習、運動、志工、旅行平衡規劃，是培養自主自律（Self-directed learning）的極佳工具。"
  },

  # 06-29 [國小初階]
  {
    "id": "dialogue-0629",
    "date": "06-29",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "暑假啟程",
    "topic": {
      "en": "Closing Ceremony of the Semester: Hello Summer Vacation!",
      "zh": "結業式！收拾書包，暑假我們來囉！"
    },
    "situation": "六月倒數第二天結業式放學鐘聲響起，Tyler 和 Amy 背起書包衝出校門，迎接期待已久的兩個月暑假。",
    "speakers": {
      "Tyler": { "role": "Tyler", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Amy": { "role": "Amy", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0629.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tyler", "avatar": "👦", "en": "Amy, the principal just announced the official dismissal! Summer vacation has begun!", "zh": "Amy，校長剛剛宣布結業式圓滿結束！暑假正式開始啦！", "keywords": ["dismissal", "principal", "summer vacation"] },
      { "id": 2, "speaker": "Amy", "avatar": "👧", "en": "Hooray! No early alarm clocks tomorrow morning! I can wake up naturally to birds singing!", "zh": "萬歲！明天早上再也不用設早起鬧鐘了！我可以聽著小鳥叫聲睡到自然醒！", "keywords": ["alarm clocks", "naturally", "hooray"] },
      { "id": 3, "speaker": "Tyler", "avatar": "👦", "en": "My dad bought tickets for the water park wave pool this coming weekend.", "zh": "我爸爸已經買好了這週末水上樂園造浪池的門票了呢。", "keywords": ["tickets", "water park", "wave pool"] },
      { "id": 4, "speaker": "Amy", "avatar": "👧", "en": "I am going to my grandparents' farm to pick sweet peaches and watch fireflies at night.", "zh": "我要去爺爺奶奶的農場採水蜜桃，晚上還要在院子裡看螢火蟲。", "keywords": ["farm", "peaches", "fireflies"] },
      { "id": 5, "speaker": "Tyler", "avatar": "👦", "en": "Goodbye textbooks, hello sunshine and swimming pools! Have the most wonderful summer ever!", "zh": "再見課本，你好陽光與游泳池！祝我們都有一個世界上最棒的暑假！", "keywords": ["textbooks", "swimming pools", "wonderful summer"] }
    ],
    "vocabulary": [
      { "word": "dismissal", "phonetic": "/dɪsˈmɪs.əl/", "pos": "n.", "zh": "放學、解散、下課時刻", "example": "The school courtyard buzzed with joyful laughter after dismissal." },
      { "word": "naturally", "phonetic": "/ˈnætʃ.ɚ.əl.i/", "pos": "adv.", "zh": "自然而然地、理所當然地", "example": "She woke up naturally as morning sunlight filled the room." },
      { "word": "pool", "phonetic": "/puːl/", "pos": "n.", "zh": "水池、游泳池", "example": "Splashing in the cool swimming pool was the best summer relief." }
    ],
    "dailyPhrase": { "en": "Wake up naturally.", "zh": "睡到自然醒。" },
    "cultureTip": "結業式放學被稱為「Official school dismissal」。漫長的暑假正式開啟，孩子們踏出校門互道「Have a wonderful summer!」，象徵放下繁重書包、盡情擁抱陽光與探索自然的黃金假期。"
  },

  # 06-30 [高中進階]
  {
    "id": "dialogue-0630",
    "date": "06-30",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "年度折返點",
    "topic": {
      "en": "June Reflections: Looking Back at the First Half of the Year with Resolve",
      "zh": "六月終曲：回望上半年奮鬥足跡，以沉靜熱情迎接下半年"
    },
    "situation": "6月30日傍晚，上半年最後一天，高中自習室窗台前，Victor 和 Irene 看著天邊絢爛晚霞，總結過去六個月的成長。",
    "speakers": {
      "Victor": { "role": "Victor", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Irene": { "role": "Irene", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0630.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Victor", "avatar": "👨‍🎓", "en": "Irene, as sunset glazes the horizon today, we officially cross the midpoint of 2026. Exactly half the year has elapsed.", "zh": "Irene，隨著今天夕陽餘暉灑落天際，我們正式跨過了 2026 年的正中折返點。整整半年的時光已經悄然流逝。", "keywords": ["midpoint", "elapsed", "horizon"] },
      { "id": 2, "speaker": "Irene", "avatar": "👩‍🎓", "en": "Time accelerates asymptotically. Reflecting on January's optimistic New Year resolutions, some flourished while others withered quietly.", "zh": "時間總是以驚人的速度悄然流逝。回望一月份許下的樂觀新年新希望，有些目標已枝繁葉茂，有些則在忙碌中悄然擱置了。", "keywords": ["accelerates", "resolutions", "withered"] },
      { "id": 3, "speaker": "Victor", "avatar": "👨‍🎓", "en": "Midyear shouldn't trigger regret; it is a sacred pit stop to recalibrate our trajectory and jettison non-essential baggage.", "zh": "年中的折返點不該引發焦慮懊悔；它是一個神聖的維修進站時刻，讓我們校準人生軌跡，果斷丟棄不必要的包袱雜音。", "keywords": ["recalibrate", "pit stop", "jettison"] },
      { "id": 4, "speaker": "Irene", "avatar": "👩‍🎓", "en": "We navigated rigorous academic terms, forged resilient friendships, and learned that personal growth is rarely linear.", "zh": "我們挺過了極具挑戰的學業考驗，鍛造了堅韌的同窗友誼，也體會到個人成長從來都不是一條單調平滑的直線。", "keywords": ["rigorous", "linear", "growth"] },
      { "id": 5, "speaker": "Victor", "avatar": "👨‍🎓", "en": "July and August offer an expansive sanctuary for deep focus, creative pursuits, and recharging our spiritual batteries.", "zh": "接下來的七月與八月，為我們提供了一處廣闊清幽的心靈庇護所，讓我們專注深耕、追求熱愛，並為精神電池充飽電量。", "keywords": ["sanctuary", "recharging", "expansive"] },
      { "id": 6, "speaker": "Irene", "avatar": "👩‍🎓", "en": "Farewell, eventful first half of the year. Let's greet July with courageous hearts, boundless curiosity, and relentless vitality!", "zh": "再見了，充實跌宕的上半年。讓我們懷抱勇敢的心靈、無垠的好奇心與不竭的生命力，大步迎接七月的到來！", "keywords": ["courageous", "boundless", "vitality"] }
    ],
    "vocabulary": [
      { "word": "elapse", "phonetic": "/iˈlæps/", "pos": "v.", "zh": "（時間）流逝、過去", "example": "Several months elapsed before we heard the test results." },
      { "word": "recalibrate", "phonetic": "/ˌriːˈkæl.ə.breɪt/", "pos": "v.", "zh": "重新校準、微調重設", "example": "The manager recalibrated team milestones after the quarterly review." },
      { "word": "sanctuary", "phonetic": "/ˈsæŋk.tʃu.er.i/", "pos": "n.", "zh": "庇護所、寧靜之所、聖所", "example": "The botanical garden served as a peaceful sanctuary from city clamor." }
    ],
    "dailyPhrase": { "en": "Midyear pit stop.", "zh": "年中的停歇檢修站、沉澱充電時刻。" },
    "cultureTip": "6月30日是一年365天的正中折返點（Midyear checkpoint）。歐美個人成長學家常將這天作為「Midyear Review（年中覆盤日）」，透過檢視年初目標執行率，在踏入下半年前重新校準人生的前進軌跡。"
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
    for d in JUNE_DIALOGUES:
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
    print(f"成功將 6 月份對話寫入 {DATA_FILE}！總篇數更新為: {len(existing_data)} (新增 {added_count} 篇)")

    # 同步更新 js/data.js
    with open(JS_FILE, 'w', encoding='utf-8') as f:
        f.write("// 365 每日生活美語對話資料庫 (全年度)\n")
        f.write("const DIALOGUES_DATA = ")
        f.write(json.dumps(existing_data, ensure_ascii=False, indent=2))
        f.write(";\n")
    print(f"成功同步更新 {JS_FILE}！")

if __name__ == '__main__':
    main()
