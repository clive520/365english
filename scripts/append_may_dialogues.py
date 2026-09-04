#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次建立 5 月份生活對話 (05-01 至 05-31，共 31 篇)
涵蓋勞動節、立夏節氣、母親節溫馨感恩、小滿節氣、國際生物多樣性日、
世界海龜日、防汛防災演練、手洗愛玉甜品、端午龍舟鼓點、世界無菸日等豐富主題！
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'dialogues.json')
JS_FILE = os.path.join(BASE_DIR, 'js', 'data.js')

MAY_DIALOGUES = [
  # 05-01 [國小中高]
  {
    "id": "dialogue-0501",
    "date": "05-01",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "感恩奉獻",
    "topic": {
      "en": "Labor Day: Honoring Campus & Community Workers",
      "zh": "五一勞動節：感謝校園與社區默默奉獻的工作者"
    },
    "situation": "5月1日勞動節早晨，Justin 和 Bella 在校門口向警衛叔叔和清潔阿姨親切問好並送上感謝卡片。",
    "speakers": {
      "Justin": { "role": "Justin", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Bella": { "role": "Bella", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0501.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Justin", "avatar": "👦", "en": "Good morning, Bella! Did you remember to bring our handmade thank-you cards today?", "zh": "早安，Bella！你今天有記得帶我們親手做的感謝卡片嗎？", "keywords": ["thank-you cards", "handmade", "morning"] },
      { "id": 2, "speaker": "Bella", "avatar": "👧", "en": "Yes! Today is International Labor Day, a wonderful occasion to honor essential workers.", "zh": "有呀！今天是國際勞動節，正是向所有辛勞付出基層工作者致敬的最好節日。", "keywords": ["Labor Day", "occasion", "workers"] },
      { "id": 3, "speaker": "Justin", "avatar": "👦", "en": "Mr. Lin, our campus security guard, greets every student with a cheerful smile regardless of rainy or scorching weather.", "zh": "我們學校的警衛林叔叔，不論颳風下雨還是烈日當空，總是帶著溫暖親切的微笑迎接每位同學。", "keywords": ["security guard", "scorching", "cheerful"] },
      { "id": 4, "speaker": "Bella", "avatar": "👧", "en": "And the janitors work tirelessly to keep our hallways and restrooms clean and hygienic.", "zh": "還有清潔阿姨們不知疲倦地辛勤打掃，維持走廊與洗手間的乾淨衛生。", "keywords": ["janitors", "tirelessly", "hygienic"] },
      { "id": 5, "speaker": "Justin", "avatar": "👦", "en": "Saying a sincere thank you and sorting our trash properly is the best way to show our deep appreciation.", "zh": "發自內心向他們說聲謝謝，並且在日常做好垃圾分類，就是表達我們真摯感謝的最好方式。", "keywords": ["sincere", "sorting", "appreciation"] }
    ],
    "vocabulary": [
      { "word": "tirelessly", "phonetic": "/ˈtaɪr.ləs.li/", "pos": "adv.", "zh": "不知疲倦地、孜孜不倦地", "example": "Volunteers worked tirelessly through the night after the earthquake." },
      { "word": "hygienic", "phonetic": "/haɪˈdʒiː.nɪk/", "pos": "adj.", "zh": "衛生的、清潔無害的", "example": "Food must be prepared in clean, hygienic conditions." },
      { "word": "scorching", "phonetic": "/ˈskɔːr.tʃɪŋ/", "pos": "adj.", "zh": "灼熱的、烈日炎炎的", "example": "We rested under a shady gazebo during the scorching noon heat." }
    ],
    "dailyPhrase": { "en": "Regardless of...", "zh": "不管……、無論……情況如何。" },
    "cultureTip": "5月1日是國際勞動節（International Workers' Day），源自1886年美國芝加哥勞工爭取每日八小時工作制的奮鬥。全世界許多國家都在這天向各行各業默默付出的勞動者表達敬意。"
  },

  # 05-02 [國小初階]
  {
    "id": "dialogue-0502",
    "date": "05-02",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "換季穿搭",
    "topic": {
      "en": "Summer Wardrobe Switch: Short Sleeves & Breathable Cotton",
      "zh": "初夏衣櫥整理：換上涼爽舒適的純棉短袖"
    },
    "situation": "五月初氣溫明顯上升，Leo 和 Mia 正在整理抽屜，把冬天的厚毛衣收好，換上輕便的短袖衣服。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0502.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Mia, feel the sunshine today! It is definitely warm enough to wear short sleeves.", "zh": "Mia，感受一下今天的陽光！天氣絕對暖和到可以穿短袖囉。", "keywords": ["sunshine", "short sleeves", "warm"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "I agree! I packed away my heavy knitted sweaters in storage boxes yesterday.", "zh": "我贊成！我昨天已經把厚重的針織毛衣通通收進收納箱裡了。", "keywords": ["sweaters", "storage boxes", "packed away"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "I love soft cotton T-shirts. They are lightweight and soak up sweat easily.", "zh": "我最喜歡柔軟的純棉 T 恤了。又輕便而且很容易吸汗。", "keywords": ["cotton", "lightweight", "sweat"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "Don't forget to put on a wide-brim hat when we play outdoors at noon.", "zh": "中午在戶外操場玩耍時，也別忘了戴上一頂寬邊遮陽帽喔。", "keywords": ["wide-brim hat", "outdoors", "noon"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Sunscreen and water bottles are packed too. Summer vibes are here!", "zh": "防曬乳和水壺也都帶齊了。初夏的活力氣息真的來了！", "keywords": ["sunscreen", "summer vibes"] }
    ],
    "vocabulary": [
      { "word": "lightweight", "phonetic": "/ˈlaɪt.weɪt/", "pos": "adj.", "zh": "輕巧的、輕量的", "example": "Pack a lightweight jacket for the summer evening breeze." },
      { "word": "sunscreen", "phonetic": "/ˈsʌn.skriːn/", "pos": "n.", "zh": "防曬乳、防曬霜", "example": "Apply sunscreen generously before heading to the beach." },
      { "word": "soak up", "phonetic": "/soʊk ʌp/", "pos": "phr. v.", "zh": "吸收、吸取（液體或汗水）", "example": "Cotton towels soak up water quickly." }
    ],
    "dailyPhrase": { "en": "Pack away.", "zh": "收拾整理妥當並收納儲藏。" },
    "cultureTip": "初夏換季被稱為「Seasonal wardrobe switch」。在日照增強的五月，選擇透氣純棉（breathable cotton）材質、隨身攜帶水壺與防曬乳（sunscreen），是維持夏日活力的健康必修課。"
  },

  # 05-03 [國中挑戰]
  {
    "id": "dialogue-0503",
    "date": "05-03",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "週末休閒",
    "topic": {
      "en": "Planning a Weekend Cycling Picnic: Homemade Cold Brew Lemon Tea",
      "zh": "初夏單車野餐趣：親手沖調冰鎮薄荷檸檬紅茶"
    },
    "situation": "週五放學時，David 和 Chloe 相約週六沿著水岸綠道騎車野餐，並分工準備野餐便當與冷飲。",
    "speakers": {
      "David": { "role": "David", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0503.mp3",
    "dialogue": [
      { "id": 1, "speaker": "David", "avatar": "👦", "en": "The weather forecast predicts clear blue skies with moderate humidity tomorrow. Perfect for our riverside cycling tour!", "zh": "氣象預報說明天會是晴空萬里且濕度適中。正是我們水岸單車之旅的絕佳好日子！", "keywords": ["forecast", "humidity", "cycling tour"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "Fantastic! I am prepping a large insulated flask filled with homemade cold brew black tea, fresh lemon slices, and garden mint.", "zh": "太棒了！我正打算準備一大個保溫瓶，裝滿親手做的冷萃紅茶，再丟幾片新鮮檸檬薄片與現摘薄荷葉。", "keywords": ["insulated flask", "cold brew", "mint", "lemon"] },
      { "id": 3, "speaker": "David", "avatar": "👦", "en": "That sounds incredibly refreshing. I will bring whole-wheat turkey sandwiches and crunchy apple slices.", "zh": "那聽起來絕對消暑解渴極了。我會準備全麥火雞肉三明治和香脆的現切蘋果片。", "keywords": ["refreshing", "whole-wheat", "sandwiches"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "Let's spread our picnic mat under the big banyan tree by the lake around eleven thirty.", "zh": "那我們大約十一點半在湖畔那棵大榕樹下的蔭涼處鋪開野餐墊吧。", "keywords": ["picnic mat", "banyan tree", "lake"] },
      { "id": 5, "speaker": "David", "avatar": "👦", "en": "Remember to strap a portable Bluetooth speaker onto your handlebar so we can enjoy some acoustic tunes.", "zh": "記得在你的龍頭把手上固定一台便攜藍牙喇叭，這樣沿路就能聽點輕快的木吉他音樂了。", "keywords": ["handlebar", "acoustic", "speaker"] },
      { "id": 6, "speaker": "Chloe", "avatar": "👧", "en": "Cycling and good music in early summer breeze—it doesn't get much better than that!", "zh": "在初夏微風中騎單車伴隨好音樂——人生最愜意的事莫過於此了！", "keywords": ["breeze", "early summer"] }
    ],
    "vocabulary": [
      { "word": "insulated", "phonetic": "/ˈɪn.sə.leɪ.t̬ɪd/", "pos": "adj.", "zh": "保溫的、隔熱的", "example": "The insulated travel mug kept the coffee steaming hot." },
      { "word": "refreshing", "phonetic": "/rɪˈfreʃ.ɪŋ/", "pos": "adj.", "zh": "清涼解渴的、令人神清氣爽的", "example": "A cold shower was immensely refreshing after rugby practice." },
      { "word": "handlebar", "phonetic": "/ˈhæn.dəl.bɑːr/", "pos": "n.", "zh": "（自行車）把手、龍頭", "example": "Keep both hands firmly on the handlebar while riding downhill." }
    ],
    "dailyPhrase": { "en": "It doesn't get much better than this.", "zh": "再好也不過如此了 / 沒有比這更棒的了。" },
    "cultureTip": "自製冷萃茶（Cold Brew Tea）以常溫或冷水浸泡茶葉數小時，能萃取出茶葉的清甜芳香，同時大幅降低苦澀味與單寧酸釋出，是夏日健康解熱的低卡新風尚。"
  },

  # 05-04 [國小中高]
  {
    "id": "dialogue-0504",
    "date": "05-04",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "流行文化",
    "topic": {
      "en": "Star Wars Day: May the Fourth Be with You & Inspiring Creativity",
      "zh": "星際大戰日：願原力與你同在！激發無窮想像力"
    },
    "situation": "5月4日「星際大戰日」，Kevin 和 Emma 在美勞角用紙筒和玻璃紙製作彩色光劍道具。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0504.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "👦", "en": "May the Fourth be with you, Emma! Today is the unofficial worldwide Star Wars Day!", "zh": "Emma，願原力與你同在！今天可是全球非官方的星際大戰日喔！", "keywords": ["May the Fourth", "Star Wars", "worldwide"] },
      { "id": 2, "speaker": "Emma", "avatar": "👧", "en": "May the Force be with you too! That pun based on 'May fourth' and 'May the Force' is pure genius.", "zh": "願原力也與你同在！那個用『五月四號』和『願原力』諧音做成的雙關語真是太天才了。", "keywords": ["Force", "pun", "genius"] },
      { "id": 3, "speaker": "Kevin", "avatar": "👦", "en": "Look at my DIY lightsaber. I used a sturdy cardboard tube wrapped in shiny silver foil and blue paper.", "zh": "你看我的自製光劍。我用了一根結實的紙筒，外面裹上閃亮的銀色錫箔紙與藍色紙。", "keywords": ["lightsaber", "cardboard tube", "silver foil"] },
      { "id": 4, "speaker": "Emma", "avatar": "👧", "en": "Mine has a bright green crystal core, just like Master Yoda's weapon.", "zh": "我的光劍則配有翠綠色的能量水晶核心，就像尤達大師的武器一樣帥氣。", "keywords": ["crystal core", "Master Yoda", "weapon"] },
      { "id": 5, "speaker": "Kevin", "avatar": "👦", "en": "Science fiction movies make us wonder about space travel and the mysteries of deep galaxies.", "zh": "科幻電影真的總能激發我們對太空旅行和遙遠銀河奧秘的無窮好奇心。", "keywords": ["science fiction", "galaxies", "mysteries"] }
    ],
    "vocabulary": [
      { "word": "pun", "phonetic": "/pʌn/", "pos": "n.", "zh": "雙關語、諧音梗", "example": "Dad loves telling cheesy puns that make everyone groan." },
      { "word": "lightsaber", "phonetic": "/ˈlaɪtˌseɪ.bɚ/", "pos": "n.", "zh": "光劍（科幻武器）", "example": "The Jedi ignited his glowing lightsaber in the dark hall." },
      { "word": "galaxy", "phonetic": "/ˈɡæl.ək.si/", "pos": "n.", "zh": "銀河、星系", "example": "The Hubble telescope captured images of distant spiral galaxies." }
    ],
    "dailyPhrase": { "en": "May the Force be with you.", "zh": "願原力與你同在。（經典祝福與激勵語句）" },
    "cultureTip": "每年5月4日是全球知名的「Star Wars Day（星際大戰日）」，源自電影名言「May the Force be with you（願原力與你同在）」與「May the Fourth be with you（五月四日伴隨你）」的趣味英式諧音雙關。"
  },

  # 05-05 [國中挑戰]
  {
    "id": "dialogue-0505",
    "date": "05-05",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "節氣智慧",
    "topic": {
      "en": "Lixia Solar Term: Welcoming Summer, Savoring Green Beans & Beating the Heat",
      "zh": "立夏節氣：告別春天、迎接初夏熱情與綠豆消暑"
    },
    "situation": "時逢二十四節氣中的「立夏」，Ethan 和 Grace 在烹飪教室談論傳統立夏習俗與初夏生理保養。",
    "speakers": {
      "Ethan": { "role": "Ethan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Grace": { "role": "Grace", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0505.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ethan", "avatar": "👦", "en": "Grace, today on the lunar calendar is Lixia, the Start of Summer! Spring has officially passed the baton.", "zh": "Grace，今天是農曆節氣中的『立夏』！春天已經正式把接力棒交給夏天了。", "keywords": ["Lixia", "Start of Summer", "baton"] },
      { "id": 2, "speaker": "Grace", "avatar": "👧", "en": "Indeed. 'Li' means commencement; crops will grow with vigorous speed fueled by abundant sunshine and rainfall.", "zh": "確實。『立』代表開始；農作物在充足的陽光與雨水滋潤下，將以旺盛的速度拔節生長。", "keywords": ["commencement", "vigorous", "abundant"] },
      { "id": 3, "speaker": "Ethan", "avatar": "👦", "en": "In ancient lore, people held 'weighing ceremonies' on Lixia to monitor health and ward off summer illness.", "zh": "古代民間在立夏這天有『秤人』的傳統，透過記錄體重來祈求整個夏季平安健朗、不消瘦。", "keywords": ["weighing", "ceremonies", "ward off"] },
      { "id": 4, "speaker": "Grace", "avatar": "👧", "en": "My family also simmers a pot of mung bean soup with barley to soothe internal heat and stay hydrated.", "zh": "我們家立夏也會熬一鍋綠豆薏仁湯，用來清熱降火解毒，讓身體隨時補足水分。", "keywords": ["simmers", "mung bean", "hydrated"] },
      { "id": 5, "speaker": "Ethan", "avatar": "👦", "en": "Traditional Chinese medicine emphasizes that summer is associated with the heart, making calm emotional balance crucial.", "zh": "中醫也強調『夏氣與心氣相通』，所以在初夏炎熱之際保持內心寧靜平和格外重要。", "keywords": ["medicine", "associated", "crucial"] },
      { "id": 6, "speaker": "Grace", "avatar": "👧", "en": "Staying cool-headed when temperatures rise is ancient wisdom that never loses its relevance.", "zh": "當氣溫節節攀升時保持冷靜從容，這份古老智慧在現代依然歷久彌新。", "keywords": ["cool-headed", "relevance", "ancient wisdom"] }
    ],
    "vocabulary": [
      { "word": "commencement", "phonetic": "/kəˈmens.mənt/", "pos": "n.", "zh": "開始、起始、畢業典禮", "example": "The solar term marks the commencement of the hot agricultural season." },
      { "word": "vigorous", "phonetic": "/ˈvɪɡ.ɚ.əs/", "pos": "adj.", "zh": "充滿活力的、強健有力的", "example": "Young plants display vigorous growth under bright daylight." },
      { "word": "cool-headed", "phonetic": "/ˌkuːlˈhed.ɪd/", "pos": "adj.", "zh": "沉著冷靜的、不慌不亂的", "example": "A good captain stays cool-headed during a maritime crisis." }
    ],
    "dailyPhrase": { "en": "Pass the baton.", "zh": "交棒、交接傳承責任或時序。" },
    "cultureTip": "立夏是夏季的第一個節氣，意味著春天的結束與盛夏的啟程。江南傳統有「立夏嘗三鮮、立夏秤人」的習俗，飲食上強調清熱健脾，多食綠豆（mung beans）、苦瓜等清涼食材。"
  },

  # 05-06 [國小初階]
  {
    "id": "dialogue-0506",
    "date": "05-06",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "健康晨光",
    "topic": {
      "en": "Morning Jog Around the Campus Track: Energizing the Day",
      "zh": "晨光運動：操場晨跑與呼吸微熱的新鮮空氣"
    },
    "situation": "早自習前，Lucas 和 Lily 繫緊鞋帶，在學校紅色 PU 跑道上輕鬆慢跑兩圈，喚醒身心。",
    "speakers": {
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Lily": { "role": "Lily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0506.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lucas", "avatar": "👦", "en": "Good morning, Lily! Let's jog two laps around the running track before homeroom.", "zh": "早安，Lily！在早自習開始前，我們去操場慢跑兩圈吧。", "keywords": ["running track", "jog", "laps"] },
      { "id": 2, "speaker": "Lily", "avatar": "👧", "en": "Great idea! Morning air in May feels crisp, and dew is still sparkling on the grass.", "zh": "好點子！五月的晨風很清爽，草地上還閃爍著晶瑩的露珠呢。", "keywords": ["crisp", "dew", "sparkling"] },
      { "id": 3, "speaker": "Lucas", "avatar": "👦", "en": "Keep a steady pace. Breathe in through your nose and breathe out through your mouth.", "zh": "保持穩定的步伐。用鼻子深吸氣，再用嘴巴緩慢吐氣。", "keywords": ["steady pace", "breathe"] },
      { "id": 4, "speaker": "Lily", "avatar": "👧", "en": "Running makes my heart pump faster and shakes away all my morning sleepiness.", "zh": "跑步讓我的心臟更有力地跳動，把早上的睏意全趕跑了。", "keywords": ["sleepiness", "pump"] },
      { "id": 5, "speaker": "Lucas", "avatar": "👦", "en": "We crossed the finish line! Now my brain is wide awake and ready for classes.", "zh": "我們跑過終點線了！現在我的大腦完全清醒，準備好迎接今天的課堂了。", "keywords": ["finish line", "wide awake"] }
    ],
    "vocabulary": [
      { "word": "lap", "phonetic": "/læp/", "pos": "n.", "zh": "（跑道或泳池的一）圈", "example": "He ran three laps around the school oval every morning." },
      { "word": "dew", "phonetic": "/duː/", "pos": "n.", "zh": "露水、露珠", "example": "Morning dew gleamed like diamonds on spiderwebs." },
      { "word": "wide awake", "phonetic": "/ˌwaɪd əˈweɪk/", "pos": "adj.", "zh": "完全清醒的、毫無睡意的", "example": "A cold washcloth left him wide awake." }
    ],
    "dailyPhrase": { "en": "Wide awake.", "zh": "完全清醒、精神奕奕。" },
    "cultureTip": "運動生理學證實，早晨進行 10~15 分鐘的中低強度有氧慢跑（aerobic jog），能刺激多巴胺與血清素釋放，提升全天的注意力集中度與學習情緒。"
  },

  # 05-07 [高中進階]
  {
    "id": "dialogue-0507",
    "date": "05-07",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "深度學習",
    "topic": {
      "en": "Digital Discipline & Overcoming Post-Exam Slump: Restoring Focus",
      "zh": "數位自律與專注力重構：克服考後鬆懈倦怠與維持步調"
    },
    "situation": "期中考放榜兩週後，高二學生 Ryan 和 Claire 討論許多同學陷入怠惰拖延的現象，並分享如何重建專注節奏。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Claire": { "role": "Claire", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0507.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "Claire, have you noticed that classroom energy has hit an alarming slump now that midterm grades are finalized?", "zh": "Claire，你有注意到期中考成績結算後，班上整體學習氛圍出現了令人擔憂的集體低迷嗎？", "keywords": ["slump", "finalized", "alarming"] },
      { "id": 2, "speaker": "Claire", "avatar": "👩‍🎓", "en": "Definitely. It is the classic post-exam psychological valley—the relief of finishing causes students to indulge in frictionless smartphone scrolling.", "zh": "確實如此。這是典型的考後心理低谷期——考完後的解脫感讓人容易放縱在無摩擦的手機短影音刷屏中。", "keywords": ["psychological valley", "frictionless", "scrolling"] },
      { "id": 3, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "Short-form content hijack our prefrontal cortex through intermittent reinforcement, making deep reading feel unbearable.", "zh": "短影音透過間歇性獎勵機制劫持我們的前額葉皮質，讓耗費心力的深度閱讀變得難以忍受。", "keywords": ["hijack", "prefrontal cortex", "reinforcement"] },
      { "id": 4, "speaker": "Claire", "avatar": "👩‍🎓", "en": "To counter that, I instituted a mandatory 'device-free zone' from eight to ten in the evening at my study desk.", "zh": "為了對抗這種情況，我給自己設立了硬性規定：每晚八點到十點在書桌實施『無電子設備區』。", "keywords": ["mandatory", "device-free", "instituted"] },
      { "id": 5, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "Physical isolation of temptation is infinitely more reliable than relying on raw, depleting willpower alone.", "zh": "把誘惑在物理空間上隔絕開來，比起單純依賴容易消耗殆盡的個人意志力，要可靠幾百倍。", "keywords": ["isolation", "temptation", "willpower"] },
      { "id": 6, "speaker": "Claire", "avatar": "👩‍🎓", "en": "Consistent incremental progress beats frantic cramming every time. We need to stay anchored for finals.", "zh": "持之以恆的每日漸進累積，永遠勝過考前抱佛腳的臨時抱佛腳。我們必須為六月的期末考穩住陣腳。", "keywords": ["incremental", "cramming", "anchored"] }
    ],
    "vocabulary": [
      { "word": "frictionless", "phonetic": "/ˈfrɪk.ʃən.ləs/", "pos": "adj.", "zh": "無摩擦阻力的、毫不費力的", "example": "Algorithmic apps are engineered for frictionless continuous consumption." },
      { "word": "mandatory", "phonetic": "/ˈmæn.də.tɔːr.i/", "pos": "adj.", "zh": "強制的、義務性的", "example": "Wearing safety helmets is mandatory by local law." },
      { "word": "incremental", "phonetic": "/ˌɪŋ.krəˈmen.t̬əl/", "pos": "adj.", "zh": "漸進的、逐步增加的", "example": "Small incremental habits accumulate into extraordinary outcomes." }
    ],
    "dailyPhrase": { "en": "Hit a slump.", "zh": "陷入低谷、陷入低潮倦怠期。" },
    "cultureTip": "行為心理學中著名的「Friction Design（摩擦力設計）」指出：要戒除壞習慣，只需增加其行動難度（例如將手機放在不同房間）；要建立好習慣，則減少其摩擦力（如桌上只放當前要讀的課本）。"
  },

  # 05-08 [國小初階]
  {
    "id": "dialogue-0508",
    "date": "05-08",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "手工獻禮",
    "topic": {
      "en": "Handmade Clay Carnations: Forever Blooms for Mom",
      "zh": "母親節前夕的手工花藝：用輕黏土製作永不凋謝的粉色康乃馨"
    },
    "situation": "母親節前夕的美術課上，Ben 和 Ruby 用超輕黏土捏製精緻的花瓣，做一朵獻給媽媽的康乃馨。",
    "speakers": {
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Ruby": { "role": "Ruby", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0508.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ben", "avatar": "👦", "en": "Ruby, look at my soft pink lightweight clay. It is so easy to knead and mold!", "zh": "Ruby，看我的粉紅色超輕黏土。捏起來好柔軟好塑形呀！", "keywords": ["clay", "knead", "mold"] },
      { "id": 2, "speaker": "Ruby", "avatar": "👧", "en": "Pinch the edges with a clay tool to make frilly flower petals like a real carnation.", "zh": "用黏土雕刻工具把邊緣捏出褶皺，這樣花瓣看起來就像真正的康乃馨了。", "keywords": ["frilly", "petals", "carnation"] },
      { "id": 3, "speaker": "Ben", "avatar": "👦", "en": "I layered eight little petals around a green floral wire stem.", "zh": "我在一根綠色花藝鐵絲花莖周圍，一層層疊上了八片小花瓣。", "keywords": ["floral wire", "stem", "layered"] },
      { "id": 4, "speaker": "Ruby", "avatar": "👧", "en": "Tie a silky purple bow at the bottom. Real flowers wilt, but our clay flowers last forever!", "zh": "在底部繫上一條優雅的紫色絲帶。鮮花會枯萎，但我們的黏土花永遠不會凋謝！", "keywords": ["wilt", "bow", "last forever"] },
      { "id": 5, "speaker": "Ben", "avatar": "👦", "en": "My mom will love putting this on her bedside nightstand.", "zh": "我媽媽一定會非常喜歡把它擺在她床頭櫃上的。", "keywords": ["nightstand", "bedside"] }
    ],
    "vocabulary": [
      { "word": "frilly", "phonetic": "/ˈfrɪl.i/", "pos": "adj.", "zh": "有褶邊的、波浪邊的", "example": "Carnation petals have delicate frilly borders." },
      { "word": "wilt", "phonetic": "/wɪlt/", "pos": "v.", "zh": "枯萎、凋謝", "example": "Without regular watering, the flowers wilted rapidly." },
      { "word": "nightstand", "phonetic": "/ˈnaɪt.stænd/", "pos": "n.", "zh": "床頭櫃", "example": "She placed an alarm clock on her wooden nightstand." }
    ],
    "dailyPhrase": { "en": "Last forever.", "zh": "歷久彌新、永遠長存不衰。" },
    "cultureTip": "康乃馨（Carnation）的花瓣邊緣帶有天然的鋸齒波紋（frilly edges）。手作永生花（forever blooms）因蘊含孩子親手雕塑的時間與心意，已成為母親節極受家長珍藏的禮物。"
  },

  # 05-09 [國中挑戰]
  {
    "id": "dialogue-0509",
    "date": "05-09",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "感恩企劃",
    "topic": {
      "en": "Mother's Day Eve: Secretly Preparing a Hearty Breakfast Menu",
      "zh": "母親節前夕秘密大作戰：全家人策劃暖心早餐菜單"
    },
    "situation": "週六傍晚，Nathan 和 Zoe 關上房門，悄悄核對明天清晨為媽媽準備「驚喜早餐床頭端送」的食材清單。",
    "speakers": {
      "Nathan": { "role": "Nathan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0509.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Nathan", "avatar": "👦", "en": "Keep your voice down, Zoe! Mom is reading in the living room. Let's finalize tomorrow's Mother's Day breakfast plan.", "zh": "聲音小聲點，Zoe！媽媽正在客廳看書。我們趕快把明天的母親節早餐計畫定案下來吧。", "keywords": ["finalize", "living room", "breakfast"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "All right. Dad agreed to wake up at six thirty to brew hazelnut coffee and fry crispy bacon.", "zh": "好的。爸爸已經同意早上六點半起床煮香濃榛果咖啡，並煎香脆培根。", "keywords": ["hazelnut coffee", "crispy bacon", "brew"] },
      { "id": 3, "speaker": "Nathan", "avatar": "👦", "en": "I will handle the scrambled eggs with creamy melted cheddar and chopped scallions.", "zh": "那我就負責炒滑嫩的美式嫩蛋，裡面加濃郁切達起司和切碎的青蔥。", "keywords": ["scrambled eggs", "cheddar", "scallions"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "And I will toast golden sourdough bread and arrange strawberries into a cute heart shape on the plate.", "zh": "我負責烤金黃酥脆的酸種麵包，並把新鮮草莓在盤子裡排成一顆可愛的愛心形狀。", "keywords": ["sourdough", "heart shape", "toast"] },
      { "id": 5, "speaker": "Nathan", "avatar": "👦", "en": "We will serve everything on a wooden tray with our handmade card before Mom even steps out of bed.", "zh": "在媽媽還沒起床下床前，我們就用木質托盤端著早餐與手寫卡片送進她房間！", "keywords": ["wooden tray", "handmade card", "bed"] },
      { "id": 6, "speaker": "Zoe", "avatar": "👧", "en": "Breakfast in bed will give Mom the royal pampering she genuinely deserves after working so hard all year.", "zh": "『床上享用愛心早餐』能讓媽媽享受皇后般的尊榮寵愛，她整年辛苦付出絕對值得這樣的待遇。", "keywords": ["pampering", "royal", "deserves"] }
    ],
    "vocabulary": [
      { "word": "scallion", "phonetic": "/ˈskæl.jən/", "pos": "n.", "zh": "青蔥、青香蔥", "example": "Garnish the steamed fish with finely sliced scallions." },
      { "word": "pampering", "phonetic": "/ˈpæm.pɚ.ɪŋ/", "pos": "n.", "zh": "悉心寵愛、貼心呵護", "example": "Mom enjoyed a day of spa pampering on her milestone birthday." },
      { "word": "finalize", "phonetic": "/ˈfaɪ.nəl.aɪz/", "pos": "v.", "zh": "最後敲定、敲定定案", "example": "The committee met to finalize the graduation schedule." }
    ],
    "dailyPhrase": { "en": "Breakfast in bed.", "zh": "床上早餐（西方家庭給母親或壽星的經典貼心驚喜禮遇）。" },
    "cultureTip": "在美加文化中，「Breakfast in bed（在床上端送早餐）」是母親節最經典的家庭傳統，孩子與伴侶負責包辦廚房所有烹調與洗碗工作，讓母親徹底放鬆睡到自然醒。"
  },

  # 05-10 [國小初階]
  {
    "id": "dialogue-0510",
    "date": "05-10",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "溫馨節日",
    "topic": {
      "en": "Happy Mother's Day! Thank You for Your Endless Love and Hugs",
      "zh": "母親節快樂！媽媽，謝謝您無微不至的愛與溫暖擁抱"
    },
    "situation": "母親節早晨，Tyler 拿著卡片和康乃馨走進媽媽房間，給媽媽一個大大的擁抱並大聲說出愛。",
    "speakers": {
      "Tyler": { "role": "Tyler", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Amy": { "role": "Amy", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0510.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tyler", "avatar": "👦", "en": "Happy Mother's Day, Mom! Here is a lovely bouquet of pink carnations for you!", "zh": "媽媽，母親節快樂！這一束美麗的粉紅色康乃馨是送給您的！", "keywords": ["Mother's Day", "bouquet", "carnations"] },
      { "id": 2, "speaker": "Amy", "avatar": "👧", "en": "Oh Tyler, they are gorgeous! Come here and let me give you a giant warm hug.", "zh": "噢 Tyler，它們太漂亮了！快過來讓媽媽給你一個大大的溫暖擁抱。", "keywords": ["gorgeous", "hug", "warm"] },
      { "id": 3, "speaker": "Tyler", "avatar": "👦", "en": "I wrote a poem inside this card thanking you for packing my lunch and cheering at my soccer games.", "zh": "我在卡片裡寫了一首小詩，感謝您每天為我做愛心便當，還在足球比賽時為我大聲加油。", "keywords": ["poem", "lunch", "soccer games"] },
      { "id": 4, "speaker": "Amy", "avatar": "👧", "en": "Seeing you grow kind, curious, and healthy is the greatest happiness a mom could ever ask for.", "zh": "看著你健康、善良、充滿好奇心地茁壯長大，就是媽媽能期盼的最大幸福了。", "keywords": ["curious", "healthy", "happiness"] },
      { "id": 5, "speaker": "Tyler", "avatar": "👦", "en": "Today you don't have to lift a finger. Sit back and let us take care of everything!", "zh": "今天您完全不用動手做家事。好好坐著休息，一切交給我們全包了！", "keywords": ["lift a finger", "take care"] }
    ],
    "vocabulary": [
      { "word": "gorgeous", "phonetic": "/ˈɡɔːr.dʒəs/", "pos": "adj.", "zh": "極漂亮的、華美絢爛的", "example": "The sunset over the ocean looked absolutely gorgeous." },
      { "word": "curious", "phonetic": "/ˈkjʊr.i.əs/", "pos": "adj.", "zh": "充滿好奇心的、好學求知的", "example": "Curious students ask thoughtful questions during class." },
      { "word": "bouquet", "phonetic": "/buˈkeɪ/", "pos": "n.", "zh": "花束", "example": "He ordered a vibrant bouquet of fresh spring blossoms." }
    ],
    "dailyPhrase": { "en": "Not lift a finger.", "zh": "什麼家事都不必動手、好好歇著享福。" },
    "cultureTip": "每年五月的第二個星期日是國際母親節。一句溫暖的「You don't have to lift a finger today（今天您什麼家事都不用動手）」是孩子表達孝心與體貼最常說的英文暖心佳句。"
  },

  # 05-11 [國小中高]
  {
    "id": "dialogue-0511",
    "date": "05-11",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "自然觀察",
    "topic": {
      "en": "Observing Summer Insects: Rhinoceros Beetles & Stag Beetles",
      "zh": "初夏昆蟲記：光臘樹上的獨角仙與鍬形蟲覓食"
    },
    "situation": "校園生態池後方的光臘樹旁，Sam 和 Olivia 拿著放大鏡，觀察樹幹上正在吸食樹汁的獨角仙。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0511.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Olivia, check out the ash tree bark! A shiny dark brown rhinoceros beetle is crawling upward.", "zh": "Olivia，快看光臘樹的樹皮！一隻油亮黑褐色的獨角仙正在往上爬呢。", "keywords": ["rhinoceros beetle", "ash tree", "bark"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👧", "en": "Wow, look at its magnificent Y-shaped horn! It looks like a brave miniature samurai knight.", "zh": "哇，看它雄偉壯觀的 Y 字型大角！簡直像一位英勇無畏的迷你武士盔甲騎士。", "keywords": ["magnificent", "horn", "samurai"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Right beside it, a stag beetle with giant pincer-like jaws is sipping sweet tree sap.", "zh": "就在它旁邊，還有一隻長著巨大鉗狀大顎的鍬形蟲，正津津有味吸食甜甜的樹汁呢。", "keywords": ["stag beetle", "pincer", "tree sap"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👧", "en": "Remember our teacher's guideline: observe them gently with our eyes and never capture or hurt them.", "zh": "要記得老師提醒我們的生態守則：用眼睛溫柔觀察就好，絕對不要捕捉或傷害它們。", "keywords": ["guideline", "observe", "capture"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Definitely! Protecting their natural habitat lets these amazing armored creatures flourish every summer.", "zh": "當然！保護好它們的天然棲地，才能讓這些披著堅固盔甲的神奇小精靈年年夏天生生不息。", "keywords": ["habitat", "armored", "flourish"] }
    ],
    "vocabulary": [
      { "word": "magnificent", "phonetic": "/mæɡˈnɪf.ə.sənt/", "pos": "adj.", "zh": "壯麗的、宏偉極佳的", "example": "The snow-capped mountains presented a magnificent sight." },
      { "word": "pincer", "phonetic": "/ˈpɪn.sɚ/", "pos": "n.", "zh": "鉗子、大螯、大鉗爪", "example": "Crabs defend themselves with sharp pincers." },
      { "word": "armored", "phonetic": "/ˈɑːr.mɚd/", "pos": "adj.", "zh": "披甲的、裝甲防護的", "example": "Beetles have tough armored exoskeletons." }
    ],
    "dailyPhrase": { "en": "Check out...", "zh": "瞧瞧、查看一下……。" },
    "cultureTip": "獨角仙（Rhinoceros Beetle）與鍬形蟲（Stag Beetle）是夏日最具代表性的昆蟲。台灣光臘樹（Griffith's Ash）分泌的汁液是牠們的最愛。推廣「只觀察不捕捉（Catch and release / Observation only）」是現代環境保育的核心素養。"
  },

  # 05-12 [高中進階]
  {
    "id": "dialogue-0512",
    "date": "05-12",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "人文關懷",
    "topic": {
      "en": "International Nurses Day: Honoring the Compassion of Healthcare Workers",
      "zh": "國際護理師節：向白衣天使致敬與同理醫護奉獻"
    },
    "situation": "5月12日國際護師節，高三醫學社社長 Julian 和社員 Hannah 共同策劃校內醫護職業座談與感恩特展。",
    "speakers": {
      "Julian": { "role": "Julian", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Hannah": { "role": "Hannah", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0512.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Julian", "avatar": "👨‍🎓", "en": "Hannah, today is International Nurses Day, commemorating Florence Nightingale's revolutionary founding of modern professional nursing.", "zh": "Hannah，今天是國際護理師節，紀念南丁格爾開創現代專業護理體系的革命性貢獻。", "keywords": ["Nurses Day", "commemorating", "revolutionary"] },
      { "id": 2, "speaker": "Hannah", "avatar": "👩‍🎓", "en": "Her legacy transcends statistics and sanitization. Nursing embodies the rare intersection of rigorous clinical expertise and radical human empathy.", "zh": "她的遺產遠超越衛生統計數字。護理專業體現了嚴謹臨床醫學專長與極致人文同理心的罕見交會。", "keywords": ["transcends", "clinical", "empathy"] },
      { "id": 3, "speaker": "Julian", "avatar": "👨‍🎓", "en": "Yet society frequently romanticizes their sacrifice as mere 'angels' while turning a blind eye to chronic understaffing and burnout.", "zh": "然而社會往往將他們的奉獻過度浪漫化為純粹的『白衣天使』，卻常常忽視了護理體系長期的缺工過勞與身心倦怠。", "keywords": ["romanticizes", "understaffing", "burnout"] },
      { "id": 4, "speaker": "Hannah", "avatar": "👩‍🎓", "en": "True gratitude necessitates advocating for equitable nurse-to-patient ratios and providing institutional psychological support.", "zh": "真正的感謝必須落實在制度保障上：積極倡議合理護病比，並提供體制內的心理諮商與支持資源。", "keywords": ["equitable", "institutional", "ratios"] },
      { "id": 5, "speaker": "Julian", "avatar": "👨‍🎓", "en": "When a patient faces agonizing uncertainty in an intensive care unit, a nurse's soothing voice is often the steady beacon of hope.", "zh": "當病患在加護病房面對病痛與未知恐懼時，護理師溫和堅定的聲音往往是支撐生命希望的最穩燈塔。", "keywords": ["agonizing", "beacon", "uncertainty"] },
      { "id": 6, "speaker": "Hannah", "avatar": "👩‍🎓", "en": "Let our exhibition illuminate both the immense dignity of this profession and the urgent systemic reforms it deserves.", "zh": "希望我們的展覽既能展現這份職業崇高無比的尊嚴，也能喚起大眾對改善護理勞動環境體制改革的重視。", "keywords": ["dignity", "reforms", "systemic"] }
    ],
    "vocabulary": [
      { "word": "transcend", "phonetic": "/trænˈsend/", "pos": "v.", "zh": "超越、超出……的界線", "example": "Great works of art transcend national boundaries and time." },
      { "word": "burnout", "phonetic": "/ˈbɝːn.aʊt/", "pos": "n.", "zh": "身心耗竭、職業倦怠", "example": "Workplace burnout among frontline nurses requires systemic reform." },
      { "word": "beacon", "phonetic": "/ˈbiː.kən/", "pos": "n.", "zh": "燈塔、指引明燈、象徵", "example": "The lighthouse stood as a beacon of safety for stormy vessels." }
    ],
    "dailyPhrase": { "en": "Turn a blind eye to...", "zh": "視而不見、對問題故意閉上眼睛。" },
    "cultureTip": "5月12日是現代護理學先驅「提燈天使」佛羅倫斯·南丁格爾（Florence Nightingale）的誕辰，定為「國際護師節（International Nurses Day）」，推動改善護理執業環境與保障護理人員尊嚴。"
  },

  # 05-13 [國小初階]
  {
    "id": "dialogue-0513",
    "date": "05-13",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "水花歡樂",
    "topic": {
      "en": "Water Balloon Fun: Cool Splashes & Laughter on a Sunny Afternoon",
      "zh": "初夏水球大作戰：清涼水花與陽光下的歡笑聲"
    },
    "situation": "炎熱的週三下午，Daniel 和 Chloe 在自家後院草坪灌滿了五彩繽紛的小水球，準備展開一場清涼的水戰遊戲。",
    "speakers": {
      "Daniel": { "role": "Daniel", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0513.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Daniel", "avatar": "👦", "en": "Chloe, I attached the garden hose to this filler nozzle and made thirty water balloons in two minutes!", "zh": "Chloe，我把花園水管接上快速注水噴頭，兩分鐘就灌好了三十顆小水球！", "keywords": ["garden hose", "water balloons", "nozzle"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "They look like squishy colorful eggs floating in the bucket. Ready, aim, splash!", "zh": "它們看起來就像泡在水桶裡軟綿綿的彩色蛋。預備，瞄準，潑水！", "keywords": ["squishy", "bucket", "splash"] },
      { "id": 3, "speaker": "Daniel", "avatar": "👦", "en": "Direct hit on my shirt! Wow, that cold water feels so refreshing under the blazing sun!", "zh": "直接命中我的上衣！哇，在火辣辣的太陽下，這冰涼的水花感覺太舒暢了！", "keywords": ["direct hit", "blazing", "refreshing"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "Here comes another yellow balloon arching through the air. Catch it if you can!", "zh": "又有一顆黃色水球在空中劃過一道弧線飛過去囉。能抓到的話就接住吧！", "keywords": ["arching", "catch"] },
      { "id": 5, "speaker": "Daniel", "avatar": "👦", "en": "After our water fight, let's pick up every broken rubber piece so the birds won't eat them.", "zh": "打完水球仗之後，我們要把地上的每一片破氣球橡膠皮撿乾淨，以免小鳥誤食。", "keywords": ["rubber", "birds", "clean up"] }
    ],
    "vocabulary": [
      { "word": "squishy", "phonetic": "/ˈskwɪʃ.i/", "pos": "adj.", "zh": "軟綿綿的、易壓扁的", "example": "The ripe peach was deliciously sweet and squishy." },
      { "word": "blazing", "phonetic": "/ˈbleɪ.zɪŋ/", "pos": "adj.", "zh": "炙熱的、烈日炎炎的", "example": "The athletes jogged despite the blazing afternoon heat." },
      { "word": "nozzle", "phonetic": "/ˈnɑː.zəl/", "pos": "n.", "zh": "噴嘴、管口", "example": "Twist the nozzle to adjust the water spray pattern." }
    ],
    "dailyPhrase": { "en": "Ready, aim, splash!", "zh": "預備，瞄準，發射水花！" },
    "cultureTip": "水球大戰（Water Balloon Fight）是美式文化中夏日派對的經典活動。遊戲後主動撿拾氣球碎片（broken rubber pieces）避免野生動物誤食，是戶外活動重要的環保責任。"
  },

  # 05-14 [國小中高]
  {
    "id": "dialogue-0514",
    "date": "05-14",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "校園健康",
    "topic": {
      "en": "Campus Mosquito Prevention Poster: Keeping Classrooms Safe & Tidy",
      "zh": "校園防蚊大作戰：宣導清除積水容器與登革熱防護"
    },
    "situation": "夏初氣溫攀升梅雨季前夕，衛生股長 Jason 和副衛生股長 Maya 繪製宣傳海報，教導大家杜絕病媒蚊滋生。",
    "speakers": {
      "Jason": { "role": "Jason", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Maya": { "role": "Maya", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0514.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Jason", "avatar": "👦", "en": "Maya, our teacher asked us to design a colorful safety poster about preventing dengue fever.", "zh": "Maya，老師請我們設計一張色彩鮮艷的宣導海報，宣導預防登革熱病媒蚊。", "keywords": ["poster", "dengue fever", "preventing"] },
      { "id": 2, "speaker": "Maya", "avatar": "👧", "en": "Great project. As summer approaches, mosquitoes multiply rapidly in stagnant puddles and discarded cups.", "zh": "很棒的任務。隨著夏季來臨，蚊子會在積水水窪與廢棄紙杯中大量繁殖。", "keywords": ["mosquitoes", "multiply", "stagnant"] },
      { "id": 3, "speaker": "Jason", "avatar": "👦", "en": "Let's highlight the golden four-step rule: inspecting, flipping, clearing, and brushing containers.", "zh": "我們把關鍵的『巡、倒、清、刷』四步驟做成醒目的大圖示標記出來吧。", "keywords": ["inspecting", "brushing", "containers"] },
      { "id": 4, "speaker": "Maya", "avatar": "👧", "en": "I will draw a cross over flowerpot saucers holding murky rainwater to show potential breeding sites.", "zh": "我會在積滿混濁雨水的花盆底盤上打一個大大的紅叉，提醒大家那是潛在的蚊卵孳生溫床。", "keywords": ["saucers", "murky", "breeding"] },
      { "id": 5, "speaker": "Jason", "avatar": "👦", "en": "A clean campus protects every student from itchy bites and infectious diseases.", "zh": "乾淨清爽的校園環境能保護每一位同學免於發癢叮咬與傳染病威脅。", "keywords": ["infectious", "protects", "bites"] }
    ],
    "vocabulary": [
      { "word": "stagnant", "phonetic": "/ˈstæɡ.nənt/", "pos": "adj.", "zh": "停滯不動的、死水汙濁的", "example": "Mosquito larvae thrive in stagnant ditch water." },
      { "word": "saucer", "phonetic": "/ˈsɑː.sɚ/", "pos": "n.", "zh": "小碟子、花盆底托盤", "example": "Empty standing water from flowerpot saucers weekly." },
      { "word": "infectious", "phonetic": "/ɪnˈfek.ʃəs/", "pos": "adj.", "zh": "傳染性的、具感染力的", "example": "Washing hands reduces the transmission of infectious viruses." }
    ],
    "dailyPhrase": { "en": "Multiply rapidly.", "zh": "快速繁殖、成倍倍增。" },
    "cultureTip": "登革熱（Dengue fever）由埃及斑蚊與白線斑蚊傳播。台灣衛福部疾管署推廣的「巡、倒、清、刷（inspect, empty, clean, scrub）」是國際公認杜絕病媒蚊孳生源最有效且低成本的防護方法。"
  },

  # 05-15 [國中挑戰]
  {
    "id": "dialogue-0515",
    "date": "05-15",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "家庭情感",
    "topic": {
      "en": "International Day of Families: Meaningful Dinner Conversations Across Generations",
      "zh": "國際家庭日：放下手機，重拾圍坐餐桌的深層交流"
    },
    "situation": "5月15日國際家庭日當晚，Leo 和 Jessica 討論各自家庭推行的「晚餐免手機專注時刻」。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Jessica": { "role": "Jessica", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0515.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Jessica, today is the United Nations International Day of Families. Did your household do anything special?", "zh": "Jessica，今天是聯合國國際家庭日。你們家有做什麼特別的安排嗎？", "keywords": ["International Day of Families", "household"] },
      { "id": 2, "speaker": "Jessica", "avatar": "👧", "en": "Yes! We initiated a 'phone basket' ritual before dinner—everyone deposits their gadgets in a wicker basket until dessert finishes.", "zh": "有呀！我們在開飯前啟動了『手機籃儀式』——每個人都把手機放進編織竹籃裡，直到吃完甜點前都不准拿。", "keywords": ["phone basket", "wicker basket", "gadgets"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "That is admirable. So often family members sit at the same table yet stare blankly at their respective screens.", "zh": "太令人佩服了。常常看見家人雖然圍坐同張餐桌，眼神卻各自茫然盯著自己的發光螢幕。", "keywords": ["admirable", "respective", "screens"] },
      { "id": 4, "speaker": "Jessica", "avatar": "👧", "en": "Without notifications chiming, we actually listened to my grandfather recount anecdotes from his childhood fishing village.", "zh": "沒有了叮咚響的通訊推播干擾，我們認真聽了爺爺講述他小時候在漁村長大的童年冒險趣事。", "keywords": ["anecdotes", "notifications", "childhood"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Shared storytelling builds deep empathy and strengthens emotional bonds across generations far more than texting.", "zh": "共同分享回憶故事所凝聚的同理心與代際情感連結，遠遠勝過冰冷的文字傳訊。", "keywords": ["empathy", "emotional bonds", "storytelling"] },
      { "id": 6, "speaker": "Jessica", "avatar": "👧", "en": "Quality presence is truly the rarest and most precious gift we can offer our loved ones.", "zh": "專注而真誠的陪伴，確實是我們能給予至親至愛最罕見也最珍貴的無價禮物。", "keywords": ["presence", "precious", "loved ones"] }
    ],
    "vocabulary": [
      { "word": "anecdote", "phonetic": "/ˈæn.ɪk.doʊt/", "pos": "n.", "zh": "趣聞、軼事、生活小故事", "example": "Uncle Joe delighted the dinner guests with funny travel anecdotes." },
      { "word": "respective", "phonetic": "/rɪˈspek.tɪv/", "pos": "adj.", "zh": "各自的、分別的", "example": "Students returned quietly to their respective homerooms." },
      { "word": "presence", "phonetic": "/ˈprez.əns/", "pos": "n.", "zh": "出席、在場、全心陪伴", "example": "Your supportive presence meant the world to her during the audition." }
    ],
    "dailyPhrase": { "en": "Across generations.", "zh": "跨越世代、兩代或三代之間。" },
    "cultureTip": "5月15日是聯合國訂定的「國際家庭日（International Day of Families）」。近年家庭教育專家大力倡導「Unplugged Dinner（無插電餐桌時光）」，藉由收起智慧型裝置，讓家人重新凝視彼此的雙眼與對話。"
  },

  # 05-16 [國小中高]
  {
    "id": "dialogue-0516",
    "date": "05-16",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "在地當季",
    "topic": {
      "en": "Visiting the Local Farmers' Market: Fresh Summer Watermelons & Mangoes",
      "zh": "初夏農夫市集尋寶：品嘗在地香甜西瓜與金黃愛文芒果"
    },
    "situation": "週六上午，Eric 和 Mia 陪媽媽來到社區農夫市集，空氣中飄散著熟成熱帶水果的濃郁果香。",
    "speakers": {
      "Eric": { "role": "Eric", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0516.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Eric", "avatar": "👦", "en": "Mia, smell that incredible sweet aroma in the air! Summer tropical fruits have arrived!", "zh": "Mia，聞聞空氣中那股令人垂涎的香甜果香！夏天的熱帶水果正式登場了！", "keywords": ["aroma", "tropical fruits", "arrived"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "Look at these pyramids of ripe Irwin mangoes! Their skin is a blend of ruby red and sunset gold.", "zh": "看這些堆成金字塔般的小山愛文芒果！果皮呈現紅寶石與夕陽金黃交織的色澤呢。", "keywords": ["mangoes", "pyramids", "sunset gold"] },
      { "id": 3, "speaker": "Eric", "avatar": "👦", "en": "The friendly farmer tapped a giant striped watermelon with his knuckles. It produced a deep hollow thump.", "zh": "親切的果農阿伯用指節輕敲一顆巨大的條紋西瓜，發出低沉渾厚的咚咚聲。", "keywords": ["knuckles", "hollow", "watermelon"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "That sound means it is bursting with crisp red flesh and sweet cold juice.", "zh": "那種沉沉的聲音代表裡面的紅果肉飽滿爽脆、多汁香甜！", "keywords": ["crisp", "bursting", "sweet"] },
      { "id": 5, "speaker": "Eric", "avatar": "👦", "en": "Buying produce directly from local farmers reduces food miles and guarantees unmatched freshness.", "zh": "直接向在地小農購買當季蔬果，既能大幅減少食物里程，又能享受到無可比擬的新鮮美味。", "keywords": ["food miles", "freshness", "local farmers"] }
    ],
    "vocabulary": [
      { "word": "knuckle", "phonetic": "/ˈnʌk.əl/", "pos": "n.", "zh": "指關節、指節", "example": "He rapped gently on the wooden door with his knuckles." },
      { "word": "hollow", "phonetic": "/ˈhɑː.loʊ/", "pos": "adj.", "zh": "空心的、低沉迴響的", "example": "A ripe watermelon makes a resonant, hollow sound when tapped." },
      { "word": "food miles", "phonetic": "/ˈfuːd ˌmaɪlz/", "pos": "n.", "zh": "食物里程（運送路程）", "example": "Shopping locally shortens food miles and cuts carbon emissions." }
    ],
    "dailyPhrase": { "en": "Burst with...", "zh": "充滿、洋溢著……。" },
    "cultureTip": "挑選西瓜時以指節敲擊（tapping with knuckles），若聲音如拍打胸膛般沉渾有彈性（hollow sound），表示水份充盈熟度適中。購買在地當季水果（local seasonal produce）能大幅縮短食物里程（food miles）。"
  },

  # 05-17 [高中進階]
  {
    "id": "dialogue-0517",
    "date": "05-17",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "數位公民",
    "topic": {
      "en": "World Telecommunication Day: Data Privacy & Digital Literacy in the AI Era",
      "zh": "世界電信與資訊社會日：AI 時代的數據隱私與數位素養"
    },
    "situation": "5月17日世界電信日，高二電腦資訊研究社社員 Alex 和 Brenda 正在辯論演算法推送與大數據隱私外洩風險。",
    "speakers": {
      "Alex": { "role": "Alex", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Brenda": { "role": "Brenda", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0517.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Alex", "avatar": "👨‍🎓", "en": "Brenda, on this World Telecommunication Day, global networks have evolved from simple telephone cables into hyper-connected AI systems.", "zh": "Brenda，在世界電信日這天回顧，全球網路已從早期的銅線電話線路，演進為無所不在的高度互聯 AI 智慧系統。", "keywords": ["Telecommunication", "hyper-connected", "networks"] },
      { "id": 2, "speaker": "Brenda", "avatar": "👩‍🎓", "en": "The technological leap is breathtaking, yet many young netizens blithely surrender biometric and behavioral data for temporary digital convenience.", "zh": "科技的躍進固然令人讚嘆，但許多青年網友卻為了短暫的數位便利，毫無戒心就交出自己的生物辨識與行為軌跡隱私。", "keywords": ["blithely", "biometric", "convenience"] },
      { "id": 3, "speaker": "Alex", "avatar": "👨‍🎓", "en": "When a cloud service or recommendation app is seemingly free, the user's personal attention and predictive data profile is invariably the true product.", "zh": "當一項雲端服務或推薦演算法看似完全免費時，使用者的個人專注力與預測性行為輪廓，無疑才是被明碼標價的真正商品。", "keywords": ["predictive", "profile", "invariably"] },
      { "id": 4, "speaker": "Brenda", "avatar": "👩‍🎓", "en": "Digital literacy today extends beyond basic coding; it encompasses critical skepticism toward algorithmic bias and deepfake synthetic media.", "zh": "當今的數位素養早已超越了基礎寫程式；它更涵蓋對演算法偏見以及深偽（Deepfake）合成多媒體保持批判性的審視意識。", "keywords": ["deepfake", "skepticism", "synthetic"] },
      { "id": 5, "speaker": "Alex", "avatar": "👨‍🎓", "en": "Enabling two-factor authentication and auditing app tracking permissions are non-negotiable hygiene habits in cyberspace.", "zh": "開啟雙重身分驗證（2FA）並定期審視應用程式的追蹤授權，是每個人在虛擬網路空間不可或缺的基本安全衛生習慣。", "keywords": ["authentication", "permissions", "non-negotiable"] },
      { "id": 6, "speaker": "Brenda", "avatar": "👩‍🎓", "en": "Technological sovereignty starts with conscious autonomy. We must be conscious curators of our digital lives, not passive data batteries.", "zh": "科技自主權始於清醒的自我意志。我們必須成為自身數位生活清醒的策展人，而不是被動提供數據養分的電池。", "keywords": ["sovereignty", "autonomy", "curators"] }
    ],
    "vocabulary": [
      { "word": "blithely", "phonetic": "/ˈblaɪð.li/", "pos": "adv.", "zh": "無憂無慮地、漫不經心地、盲目地", "example": "He walked blithely past warning signs toward the crumbling cliff." },
      { "word": "invariably", "phonetic": "/ɪnˈver.i.ə.bli/", "pos": "adv.", "zh": "總是、不變地、無一例外地", "example": "Punctual people invariably arrive five minutes ahead of schedule." },
      { "word": "sovereignty", "phonetic": "/ˈsɑːv.rən.ti/", "pos": "n.", "zh": "主權、自主權", "example": "Individuals must maintain sovereignty over their personal identifiable data." }
    ],
    "dailyPhrase": { "en": "Non-negotiable.", "zh": "不容商榷的、必須遵守的底線原則。" },
    "cultureTip": "5月17日是世界電信和資訊社會日（World Telecommunication and Information Society Day）。矽谷名言「If you are not paying for the product, you are the product（如果你沒為產品付費，你本身就是商品）」深刻揭示了現代免費大數據演算法背後的隱私代價。"
  },

  # 05-18 [高中進階]
  {
    "id": "dialogue-0518",
    "date": "05-18",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "文化美學",
    "topic": {
      "en": "International Museum Day: How Immersive Technology Transforms Heritage Preservation",
      "zh": "國際博物館日：沉浸式科技如何重新定義文化遺產參訪體驗？"
    },
    "situation": "5月18日國際博物館日，Victor 和 Irene 參觀結合虛擬實境與全息投影的歷史特展後走出展廳。",
    "speakers": {
      "Victor": { "role": "Victor", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Irene": { "role": "Irene", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0518.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Victor", "avatar": "👨‍🎓", "en": "Irene, walking through that digitally reconstructed Tang Dynasty palace was mind-bending. The architectural details felt so palpable!", "zh": "Irene，漫步在數位全息重建的唐代宮殿光影中，太震撼了。那些木構建築細節逼真得彷彿觸手可及！", "keywords": ["reconstructed", "architectural", "palpable"] },
      { "id": 2, "speaker": "Irene", "avatar": "👩‍🎓", "en": "It marks a paradigm shift for International Museum Day. Museums are no longer dusty mausoleums of static artifacts behind glass.", "zh": "這標誌著國際博物館日的一次典範轉移。博物館不再只是把靜態古物冰冷陳列在玻璃櫥窗後的古老陵墓了。", "keywords": ["paradigm shift", "mausoleums", "artifacts"] },
      { "id": 3, "speaker": "Victor", "avatar": "👨‍🎓", "en": "Interactive haptic exhibits allow visitors to touch virtual three-dimensional scans of delicate bronze vessels without causing deterioration.", "zh": "互動觸覺感應展覽讓參觀者能夠『撫摸』脆弱青銅古文物的虛擬 3D 掃描模型，卻不會造成任何實體磨損裂化。", "keywords": ["haptic", "deterioration", "bronze"] },
      { "id": 4, "speaker": "Irene", "avatar": "👩‍🎓", "en": "However, we must ensure flashy multimedia doesn't eclipse historical authenticity or trivialise profound civilizational narratives.", "zh": "然而，我們也必須警惕：過度炫目的多媒體聲光效果，絕不能掩蓋歷史本真的沉靜力量，或將深刻的文明敘事扁平娛樂化。", "keywords": ["authenticity", "trivialise", "narratives"] },
      { "id": 5, "speaker": "Victor", "avatar": "👨‍🎓", "en": "Well observed. Technology serves as a bridge, inviting contemporary audiences to converse with ancestors across millennia.", "zh": "觀察很深刻。科技應當是一座引路橋樑，引導當代觀眾跨越數千年時空，與古老先哲展開深層靈魂對話。", "keywords": ["contemporary", "millennia", "bridge"] },
      { "id": 6, "speaker": "Irene", "avatar": "👩‍🎓", "en": "When ancient relics evoke empathetic resonance, history stops being cold facts and transforms into living collective memory.", "zh": "當千年古文物喚醒內心深處的同理共鳴時，歷史便不再是冰冷枯燥的課本考題，而是化為鮮活流動的集體記憶。", "keywords": ["resonance", "relics", "collective memory"] }
    ],
    "vocabulary": [
      { "word": "palpable", "phonetic": "/ˈpæl.pə.bəl/", "pos": "adj.", "zh": "可感知的、易察覺的、觸手可及的", "example": "The tension in the debate hall was almost palpable." },
      { "word": "mausoleum", "phonetic": "/ˌmɔː.zəˈliː.əm/", "pos": "n.", "zh": "陵墓、沉悶幽閉的大建築", "example": "The historic monument looked solemn like an imperial mausoleum." },
      { "word": "deterioration", "phonetic": "/dɪˌtɪr.i.əˈreɪ.ʃən/", "pos": "n.", "zh": "惡化、損耗、變質", "example": "Proper humidity control prevents parchment deterioration." }
    ],
    "dailyPhrase": { "en": "Paradigm shift.", "zh": "思維範式轉移、根本性的觀念革新。" },
    "cultureTip": "每年5月18日是由國際博物館協會（ICOM）發起的世界博物館日（International Museum Day）。近年主題聚焦於「科技賦能博物館（Museums, Technology & Innovation）」，透過 VR 與元宇宙技術讓沉睡的文化瑰寶活起來。"
  },

  # 05-19 [國小初階]
  {
    "id": "dialogue-0519",
    "date": "05-19",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "自然天氣",
    "topic": {
      "en": "Summer Afternoon Thunderstorm: Splashing Drops & the Brilliant Rainbow",
      "zh": "初夏午後雷陣雨：豆大雨點與雨後放晴的大彩虹"
    },
    "situation": "午後三點天空突然烏雲密布，傾盆雷雨過後放晴，Mason 和 Ella 跑到教室走廊欄杆旁看天邊的彩虹。",
    "speakers": {
      "Mason": { "role": "Mason", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Ella": { "role": "Ella", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0519.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mason", "avatar": "👦", "en": "Ella, listen to that loud thunder rolling across the dark clouds! Boom!", "zh": "Ella，聽滾滾烏雲間傳來隆隆的打雷聲！轟隆！", "keywords": ["thunder", "clouds", "loud"] },
      { "id": 2, "speaker": "Ella", "avatar": "👧", "en": "Big raindrops are splashing loudly on the glass windows like popcorn popping.", "zh": "豆大的雨滴劈劈啪啪打在玻璃窗上，好像爆米花在鍋裡跳動一樣。", "keywords": ["raindrops", "popcorn", "splashing"] },
      { "id": 3, "speaker": "Mason", "avatar": "👦", "en": "Summer afternoon thundershowers always come quickly and leave just as fast.", "zh": "初夏的午後西北雨總是來得快，走得也一樣匆匆。", "keywords": ["thundershowers", "afternoon", "quickly"] },
      { "id": 4, "speaker": "Ella", "avatar": "👧", "en": "Look outside now! The sun broke through, and a double rainbow is arching across the sky!", "zh": "現在看窗外！太陽穿透雲層照射出來了，天空掛著一道壯觀的雙彩虹呢！", "keywords": ["rainbow", "arching", "sun"] },
      { "id": 5, "speaker": "Mason", "avatar": "👦", "en": "Red, orange, yellow, green, blue, indigo, and violet! The rain cooled down the heat completely.", "zh": "紅橙黃綠藍靛紫！這場雨把夏日的悶熱完全沖刷得清涼舒適了。", "keywords": ["violet", "cooled down", "heat"] }
    ],
    "vocabulary": [
      { "word": "thundershower", "phonetic": "/ˈθʌn.dɚˌʃaʊ.ɚ/", "pos": "n.", "zh": "雷陣雨、午後西北雨", "example": "A sudden thundershower caught pedestrians without umbrellas." },
      { "word": "indigo", "phonetic": "/ˈɪn.dɪ.ɡoʊ/", "pos": "n./adj.", "zh": "靛藍色、深青藍色", "example": "Indigo dye gives denim jeans their iconic dark shade." },
      { "word": "violet", "phonetic": "/ˈvaɪə.lət/", "pos": "n./adj.", "zh": "紫羅蘭色、藍紫色", "example": "The innermost band of a rainbow shines in soft violet." }
    ],
    "dailyPhrase": { "en": "Cool down.", "zh": "降溫、冷卻涼爽下來。" },
    "cultureTip": "初夏台灣常見俗稱「西北雨」的午後對流雷陣雨（convective thundershowers），通常持續不到一小時，雨過天青後因空氣中水氣豐沛，常在東方天際形成鮮豔奪目的彩虹（Rainbow）甚至霓虹（Double rainbow）。"
  },

  # 05-20 [國中挑戰]
  {
    "id": "dialogue-0520",
    "date": "05-20",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "溫馨語彙",
    "topic": {
      "en": "The '520' Phenomenon: Expressing Gratitude and Appreciation to Friends & Family",
      "zh": "「520」諧音文化：向身邊珍視的同儕與家人大方表達感激與愛"
    },
    "situation": "5月20日午後，Oliver 和 Maya 在圖書館自習室互傳小便利貼，探討數字諧音背後的暖心文化。",
    "speakers": {
      "Oliver": { "role": "Oliver", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Maya": { "role": "Maya", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0520.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Oliver", "avatar": "👦", "en": "Maya, check out social media today. People are posting cute cards and messages with the number 520 everywhere.", "zh": "Maya，你看今天的社群動態。大家到處都在轉發寫著數字 520 的可愛卡片和文字呢。", "keywords": ["social media", "messages", "520"] },
      { "id": 2, "speaker": "Maya", "avatar": "👧", "en": "That is because the Mandarin pronunciation of 'five-two-zero' sounds just like 'I love you'!", "zh": "那是因為中文裡『五二零』的發音，聽起來就跟『我愛你』非常像呀！", "keywords": ["pronunciation", "I love you", "Mandarin"] },
      { "id": 3, "speaker": "Oliver", "avatar": "👦", "en": "Number homophones are fascinating in modern pop culture, like 1314 meaning 'forever and ever.'", "zh": "現代流行文化裡的數字諧音真的很巧妙，就像 1314 代表『一生一世』一樣。", "keywords": ["homophones", "forever and ever", "pop culture"] },
      { "id": 4, "speaker": "Maya", "avatar": "👧", "en": "Beyond romantic relationships, today is an uplifting excuse to voice gratitude to supportive best friends and parents.", "zh": "除了情侶之間，今天其實也是向一路力挺自己的摯友和爸媽大方表達感謝的絕佳契機。", "keywords": ["gratitude", "supportive", "uplifting"] },
      { "id": 5, "speaker": "Oliver", "avatar": "👦", "en": "Many people find saying 'I love you' awkward in everyday life, so a playful digital pun softens the barrier.", "zh": "很多人平時當面說『我愛你』會覺得難為情，這種俏皮好玩的數字雙關語剛好降低了開口的尷尬防線。", "keywords": ["awkward", "barrier", "softens"] },
      { "id": 6, "speaker": "Maya", "avatar": "👧", "en": "Never hesitate to tell the people who uplift you how much you truly cherish them!", "zh": "永遠別吝嗇向那些支持鼓勵你的人說出：你有多麼珍視有他們相伴的日子！", "keywords": ["cherish", "uplift", "hesitate"] }
    ],
    "vocabulary": [
      { "word": "homophone", "phonetic": "/ˈhɑː.mə.foʊn/", "pos": "n.", "zh": "同音詞、同音字、諧音詞", "example": "'Flour' and 'flower' are classic English homophones." },
      { "word": "cherish", "phonetic": "/ˈtʃer.ɪʃ/", "pos": "v.", "zh": "珍愛、珍視、銘記在心", "example": "I will forever cherish our golden middle school memories." },
      { "word": "uplifting", "phonetic": "/ʌpˈlɪf.tɪŋ/", "pos": "adj.", "zh": "令人振奮的、激勵人心的", "example": "Her uplifting speech motivated the entire graduating class." }
    ],
    "dailyPhrase": { "en": "Never hesitate to...", "zh": "絕不要猶豫去……、大方勇敢地去……。" },
    "cultureTip": "華語網路文化發展出獨特的「數字諧音文化（numerical wordplay）」，如 520（我愛你）、1314（一生一世）、88（拜拜）。5月20日被年輕世代視為「網路情人節」與感恩互道溫暖的非官方佳節。"
  },

  # 05-21 [國中挑戰]
  {
    "id": "dialogue-0521",
    "date": "05-21",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "節氣思辨",
    "topic": {
      "en": "Xiaoman Solar Term: Grain Buds, Nature's Abundance & the Philosophy of Moderation",
      "zh": "小滿節氣：麥粒漸滿、萬物繁茂的謙遜與「小得盈滿」哲學"
    },
    "situation": "二十四節氣迎來「小滿」，Ethan 和 Natalie 在校園花園長椅探討節氣背後蘊含的東方中庸之道哲理。",
    "speakers": {
      "Ethan": { "role": "Ethan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Natalie": { "role": "Natalie", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0521.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ethan", "avatar": "👦", "en": "Natalie, today is Xiaoman, or 'Grain Buds,' the eighth solar term in the twenty-four solar terms cycle.", "zh": "Natalie，今天正是『小滿』，二十四節氣當中的第八個節氣。", "keywords": ["Xiaoman", "Grain Buds", "cycle"] },
      { "id": 2, "speaker": "Natalie", "avatar": "👧", "en": "The name refers to grain seeds beginning to plump up and swell, though they are not completely ripe yet.", "zh": "這個名字代表田裡的穀物種子已經開始日漸飽滿鼓起，不過尚未到達完全熟透的金黃階段。", "keywords": ["plump up", "swell", "ripe"] },
      { "id": 3, "speaker": "Ethan", "avatar": "👦", "en": "Did you notice that while we have Lesser Cold and Greater Cold, or Minor Heat and Major Heat, there is no 'Daman' or 'Major Fullness'?", "zh": "你有發現二十四節氣中有小寒大寒、小暑大暑，卻唯獨只有『小滿』，從來沒有『大滿』嗎？", "keywords": ["Lesser Cold", "Minor Heat", "Major Fullness"] },
      { "id": 4, "speaker": "Natalie", "avatar": "👧", "en": "Yes! Ancient philosophy holds that when the moon is full, it begins to wane; when water overflows, it spills.", "zh": "沒錯！古代東方哲學認為『月滿則虧，水滿則溢』，物極必反。", "keywords": ["wane", "overflows", "philosophy"] },
      { "id": 5, "speaker": "Ethan", "avatar": "👦", "en": "So 'Xiaoman'—being slightly plump but leaving room for modest growth—is considered the ideal state in life.", "zh": "因此『小滿』——也就是將滿未滿、保有適度謙遜進步餘裕的狀態，被視為人生最圓滿安定的至高境界。", "keywords": ["modest", "ideal state", "growth"] },
      { "id": 6, "speaker": "Natalie", "avatar": "👧", "en": "Cultivating contentment with what we have while striving for self-improvement is timeless wisdom.", "zh": "對眼前擁有的知足感恩，同時又保有一顆踏實追求自我進步的心，這正是歷久彌新的智慧。", "keywords": ["contentment", "striving", "timeless wisdom"] }
    ],
    "vocabulary": [
      { "word": "plump", "phonetic": "/plʌmp/", "pos": "v./adj.", "zh": "豐滿、飽滿、脹圓", "example": "The blueberries plumped up sweetly after recent rain." },
      { "word": "wane", "phonetic": "/weɪn/", "pos": "v.", "zh": "（月亮）虧缺、衰退減弱", "example": "Public enthusiasm for the trend began to wane." },
      { "word": "contentment", "phonetic": "/kənˈtent.mənt/", "pos": "n.", "zh": "知足、滿意、安泰", "example": "True contentment comes from meaningful connections, not material riches." }
    ],
    "dailyPhrase": { "en": "Leave room for...", "zh": "為……預留彈性與進步空間。" },
    "cultureTip": "小滿（Grain Buds）在二十四節氣中獨具哲思。古人講求「小得盈滿，大滿則溢」。「二十四節氣唯有小滿，無大滿」體現了中華文化追求中庸（moderation）與謙遜知足的最高處世美學。"
  },

  # 05-22 [高中進階]
  {
    "id": "dialogue-0522",
    "date": "05-22",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "生態保育",
    "topic": {
      "en": "International Day for Biological Diversity: Safeguarding Endemic Species & Coral Reefs",
      "zh": "國際生物多樣性日：守護珊瑚礁與台灣特有種生態網絡"
    },
    "situation": "5月22日國際生物多樣性日，生物研習社社長 Kevin 和副社長 Audrey 正在整理墾丁珊瑚礁與台灣黑熊保育調查報告。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Audrey": { "role": "Audrey", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0522.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "👨‍🎓", "en": "Audrey, today marks the International Day for Biological Diversity. Our island boasts astonishing biodiversity despite covering merely zero point zero two percent of Earth's landmass.", "zh": "Audrey，今天是國際生物多樣性日。我們這座島嶼雖然僅占全球陸地面積的萬分之二，卻孕育了令人驚嘆的生物多樣性密度。", "keywords": ["Biological Diversity", "landmass", "astonishing"] },
      { "id": 2, "speaker": "Audrey", "avatar": "👩‍🎓", "en": "From the subtropical lowlands to high alpine peaks, our endemic species like the Formosan black bear and Mikado pheasant are global ecological treasures.", "zh": "從亞熱帶平原一路延伸到三千公尺高山苔原，台灣黑熊與帝雉等特有種是全球矚目的生態寶藏。", "keywords": ["subtropical", "endemic species", "treasures"] },
      { "id": 3, "speaker": "Kevin", "avatar": "👨‍🎓", "en": "However, ocean warming caused widespread coral bleaching off the southern coast, threatening marine nurseries.", "zh": "然而近年海水持續異常升溫，導致南海岸爆發大規模珊瑚白化危機，重創了海洋生物最核心的育苗庇護所。", "keywords": ["bleaching", "nurseries", "coral"] },
      { "id": 4, "speaker": "Audrey", "avatar": "👩‍🎓", "en": "Coral reefs support a quarter of all marine life. When symbiotic algae detach due to thermal stress, entire trophic cascades collapse.", "zh": "珊瑚礁支撐著全球四分之一的海洋生物。當共生藻因熱壓力而脫離時，整個食物鏈營養級連鎖反應都會崩解。", "keywords": ["symbiotic", "algae", "trophic cascades"] },
      { "id": 5, "speaker": "Kevin", "avatar": "👨‍🎓", "en": "Biodiversity isn't merely scenic wallpaper; it is our planetary life-support system purifying water, cycling carbon, and pollinating agriculture.", "zh": "生物多樣性絕非僅是風景桌布；它實質上是為我們淨化水源、循環碳素、為農業授粉的地球核心維生系統。", "keywords": ["life-support", "pollinating", "wallpaper"] },
      { "id": 6, "speaker": "Audrey", "avatar": "👩‍🎓", "en": "Preserving nature's intricate web requires designating marine protected areas and eliminating habitat fragmentation before it is irreversibly severed.", "zh": "守護自然這張錯綜複雜的生命之網，迫切需要劃設海洋保護區並終止棲地破碎化，免得生態鏈遭受不可逆的斷裂。", "keywords": ["fragmentation", "irreversibly", "protected areas"] }
    ],
    "vocabulary": [
      { "word": "endemic", "phonetic": "/enˈdem.ɪk/", "pos": "adj.", "zh": "特有的、地方特產的（生物）", "example": "The Formosan blue magpie is endemic to the mountain forests of Taiwan." },
      { "word": "bleaching", "phonetic": "/ˈbliː.tʃɪŋ/", "pos": "n.", "zh": "白化、漂白", "example": "Marine biologists recorded severe coral bleaching across the reef." },
      { "word": "fragmentation", "phonetic": "/ˌfræɡ.menˈteɪ.ʃən/", "pos": "n.", "zh": "破碎化、分裂解體", "example": "Road construction causes severe habitat fragmentation for wildlife." }
    ],
    "dailyPhrase": { "en": "Support a quarter of...", "zh": "支撐了……的四分之一（比例）。" },
    "cultureTip": "5月22日是聯合國「國際生物多樣性日（International Day for Biological Diversity）」。台灣因地形垂直高差近四千公尺，單位面積物種豐富度居全球前茅，擁有超過千種特有種生物（Endemic species）。"
  },

  # 05-23 [國小中高]
  {
    "id": "dialogue-0523",
    "date": "05-23",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "海洋保護",
    "topic": {
      "en": "World Turtle Day: Ditching Plastic Straws to Protect Marine Giants",
      "zh": "世界海龜日：拒絕一次性塑膠吸管，守護海龜悠游"
    },
    "situation": "5月23日世界海龜日，Sammy 和 Noah 在自然走廊張貼小琉球綠蠵龜的照片，呼籲大家自備不鏽鋼吸管。",
    "speakers": {
      "Sammy": { "role": "Sammy", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Noah": { "role": "Noah", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0523.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sammy", "avatar": "👧", "en": "Noah, today is World Turtle Day! Look at this breathtaking underwater photo of a green sea turtle gliding through waves.", "zh": "Noah，今天是世界海龜日！看這張令人屏息的水下攝影：一隻綠蠵龜正優雅滑翔在碧藍波浪中。", "keywords": ["World Turtle Day", "green sea turtle", "gliding"] },
      { "id": 2, "speaker": "Noah", "avatar": "👦", "en": "Sea turtles have roamed Earth's oceans for over a hundred million years, surviving the age of dinosaurs!", "zh": "海龜漫遊在地球海洋已經超過一億年了，連恐龍時代的大滅絕牠們都挺過來了！", "keywords": ["roamed", "dinosaurs", "surviving"] },
      { "id": 3, "speaker": "Sammy", "avatar": "👧", "en": "Yet discarded plastic bags floating in water look dangerously identical to delicious jellyfish, their favorite snack.", "zh": "但漂浮在海水裡的廢棄塑膠袋，看起來危險地酷似美味的水母，而水母偏偏是牠們最愛的點心。", "keywords": ["identical", "jellyfish", "discarded"] },
      { "id": 4, "speaker": "Noah", "avatar": "👦", "en": "Plastic debris can block their digestive tracts or trap their flippers, making it impossible to swim or surface for air.", "zh": "塑膠垃圾會堵塞牠們的消化道，甚至纏住牠們的鰭狀肢，導致海龜無法游泳或浮上海面呼吸。", "keywords": ["flippers", "debris", "digestive tracts"] },
      { "id": 5, "speaker": "Sammy", "avatar": "👧", "en": "By carrying our own reusable straws and cloth bags, we give these gentle ocean voyagers a cleaner, safer home.", "zh": "只要我們自備環保環保吸管與環保布袋，就能為這些溫柔的海洋旅人提供一個更乾淨安全的家園。", "keywords": ["reusable straws", "voyagers", "cleaner"] }
    ],
    "vocabulary": [
      { "word": "voyager", "phonetic": "/ˈvɔɪ.ɪ.dʒɚ/", "pos": "n.", "zh": "航海者、遠行者、旅人", "example": "Sea turtles are legendary voyagers traversing vast oceans." },
      { "word": "debris", "phonetic": "/dəˈbriː/", "pos": "n.", "zh": "碎片、殘骸、垃圾廢棄物", "example": "Volunteers collected plastic debris along the sandy shoreline." },
      { "word": "identical", "phonetic": "/aɪˈden.t̬ə.kəl/", "pos": "adj.", "zh": "完全相同的、極其相似的", "example": "The two twins wore identical yellow raincoats." }
    ],
    "dailyPhrase": { "en": "Surface for air.", "zh": "浮上水面呼吸空氣。" },
    "cultureTip": "5月23日是「世界海龜日（World Turtle Day）」，旨在喚醒大眾對海龜與陸龜生存危機的關注。台灣的小琉球是全球著名的綠蠵龜重要棲地，拒絕使用一次性塑膠袋與吸管是守護海龜的關鍵日常行動。"
  },

  # 05-24 [國小初階]
  {
    "id": "dialogue-0524",
    "date": "05-24",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "居家創意",
    "topic": {
      "en": "Building a Living Room Blanket Fort: A Cozy Reading Nook",
      "zh": "假日的秘密基地：在客廳動手搭棉被城堡帳篷"
    },
    "situation": "炎熱的週日午後，Ryan 和 Jenny 把客廳沙發、椅子和薄毯子搭成一個舒適的小小秘密帳篷基地。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Jenny": { "role": "Jenny", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0524.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "👦", "en": "Jenny, pull that soft blue fleece blanket across between the armchair and the sofa!", "zh": "Jenny，把那條柔軟的藍色毛毯拉平，跨在扶手椅和沙發中間！", "keywords": ["armchair", "blanket", "fleece"] },
      { "id": 2, "speaker": "Jenny", "avatar": "👧", "en": "I secured both corners with two wooden clothes pins so the roof won't collapse.", "zh": "我用兩個木質曬衣夾把兩邊角落牢牢夾住了，這樣城堡屋頂就不會塌下來啦。", "keywords": ["clothes pins", "collapse", "roof"] },
      { "id": 3, "speaker": "Ryan", "avatar": "👦", "en": "Toss in three fluffy pillows and our favorite illustrated fantasy storybooks.", "zh": "再丟進三個蓬鬆的抱枕，還有我們最喜歡的奇幻童話繪本。", "keywords": ["pillows", "fantasy", "fluffy"] },
      { "id": 4, "speaker": "Jenny", "avatar": "👧", "en": "Turn on this warm fairy light string! It feels like our own magical glowing cave.", "zh": "打開這串溫暖的星光小燈串！感覺就像我們專屬的發光夢幻小山洞一樣。", "keywords": ["fairy light", "magical", "glowing"] },
      { "id": 5, "speaker": "Ryan", "avatar": "👦", "en": "Crawling inside our secret fort to read on a hot Sunday afternoon is pure fun.", "zh": "在炎熱的週日午後鑽進秘密基地裡看書，真是單純又無比快樂的享受。", "keywords": ["secret fort", "crawling", "pure fun"] }
    ],
    "vocabulary": [
      { "word": "collapse", "phonetic": "/kəˈlæps/", "pos": "v.", "zh": "塌陷、倒塌", "example": "The makeshift cardboard tent collapsed in the breeze." },
      { "word": "fleece", "phonetic": "/fliːs/", "pos": "n.", "zh": "抓絨布、羊毛絨毯", "example": "Wrap yourself in a warm fleece throw during movie night." },
      { "word": "nook", "phonetic": "/nʊk/", "pos": "n.", "zh": "隱密角落、舒適小天地", "example": "She created a cozy reading nook beside the bedroom window." }
    ],
    "dailyPhrase": { "en": "Pure fun.", "zh": "純粹的樂趣、單純快樂的享受。" },
    "cultureTip": "搭棉被城堡帳篷（Building a Blanket Fort）是英美家庭極具代表性的童年室內創意遊戲。利用沙發靠墊（cushions）、床單與抱枕搭建秘密基地（secret fort），能激發孩子的空間想像力與動手能力。"
  },

  # 05-25 [國小中高]
  {
    "id": "dialogue-0525",
    "date": "05-25",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "防災安全",
    "topic": {
      "en": "School Flood & Typhoon Safety Drill: Emergency Preparedness Steps",
      "zh": "校園防汛防颱演練：熟記汛期防災避難黃金步驟"
    },
    "situation": "梅雨與颱風季節即將到來，Tony 和 Clara 參加學校舉辦的防汛疏散演練，檢視防災緊急避難包。",
    "speakers": {
      "Tony": { "role": "Tony", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Clara": { "role": "Clara", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0525.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tony", "avatar": "👦", "en": "Clara, our school is conducting a typhoon and flood drill today ahead of the plum rain season.", "zh": "Clara，在梅雨季來臨前，我們學校今天正在舉行防颱防汛疏散演練呢。", "keywords": ["typhoon", "drill", "plum rain"] },
      { "id": 2, "speaker": "Clara", "avatar": "👧", "en": "It is so important. When heavy torrential downpours strike, urban drainage systems can easily get overwhelmed.", "zh": "這太重要了。當暴雨狂瀉襲來時，城市的排水系統很容易會難以負荷。", "keywords": ["torrential", "downpours", "drainage"] },
      { "id": 3, "speaker": "Tony", "avatar": "👦", "en": "The fire department demonstrated how stacking sandbags in an interlocking herringbone pattern prevents basement flooding.", "zh": "消防隊員向我們示範了如何用『人字形交錯法』堆疊沙包，這樣能最有效地阻擋雨水灌入地下室。", "keywords": ["sandbags", "interlocking", "flooding"] },
      { "id": 4, "speaker": "Clara", "avatar": "👧", "en": "Did your family check your emergency 'go-bag' with fresh drinking water, batteries, and first-aid gauze?", "zh": "你們家有檢查過防災避難包嗎？裡面要有瓶裝飲用水、備用乾電池以及急救紗布喔。", "keywords": ["emergency", "go-bag", "gauze"] },
      { "id": 5, "speaker": "Tony", "avatar": "👦", "en": "Being prepared beforehand ensures we stay calm and secure when intense tropical storms roll in.", "zh": "事前做好萬全準備，才能在強烈熱帶風暴來臨時保持沉著鎮定、化險為夷。", "keywords": ["prepared", "tropical storms", "secure"] }
    ],
    "vocabulary": [
      { "word": "torrential", "phonetic": "/tɔːˈren.ʃəl/", "pos": "adj.", "zh": "如傾盆大雨的、狂瀉暴雨的", "example": "Torrential rain triggered sudden flash floods in the valley." },
      { "word": "drainage", "phonetic": "/ˈdreɪ.nɪdʒ/", "pos": "n.", "zh": "排水系統、排水設施", "example": "City crews cleared clogged grates to improve street drainage." },
      { "word": "sandbag", "phonetic": "/ˈsænd.bæɡ/", "pos": "n.", "zh": "沙袋、沙包", "example": "Volunteers stacked heavy sandbags along the river bank." }
    ],
    "dailyPhrase": { "en": "Ahead of...", "zh": "在……之前、提前做好準備。" },
    "cultureTip": "每年五月至六月是東亞特有的「梅雨季（Plum Rain Season）」，隨後進入夏秋颱風季。消防與防災機構倡導家家戶戶備妥「緊急避難包（Emergency Go-Bag）」並熟知沙包堆疊與防汛避難指引。"
  },

  # 05-26 [國中挑戰]
  {
    "id": "dialogue-0526",
    "date": "05-26",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "民俗體育",
    "topic": {
      "en": "Dragon Boat Team Training: Finding the Drumming Rhythm & Sync",
      "zh": "端午龍舟隊備戰集訓：鼓點節奏與全員同心的默契划槳"
    },
    "situation": "距離端午節不到一個月，校園龍舟隊的 Dylan 和 Chloe 在河道碼頭練習划槳配合，領會鼓手的核心指揮作用。",
    "speakers": {
      "Dylan": { "role": "Dylan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0526.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Dylan", "avatar": "👦", "en": "Phew, that two-kilometer training sprint was exhausting! My forearms are burning from paddling against the current.", "zh": "呼，剛剛那兩公里的衝刺訓練太拼了！逆水划槳讓我的小臂肌肉痠痛得像在燃燒一樣。", "keywords": ["sprint", "paddling", "exhausting"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural", "en": "You did great, Dylan! In our second run, all twenty paddlers finally synchronized our strokes perfectly with the drumbeats.", "zh": "你划得超棒，Dylan！在第二趟衝刺中，我們二十位划手終於把划槳動作與鼓聲節奏完美同步了。", "keywords": ["synchronized", "strokes", "drumbeats"] },
      { "id": 3, "speaker": "Dylan", "avatar": "👦", "en": "The drummer really dictates the soul of the dragon boat. When the rhythm accelerates, everyone digs their blades deeper simultaneously.", "zh": "鼓手真的掌握了整艘龍舟的靈魂。當鼓點節奏一加快，所有人同時把槳葉深深扎進水裡發力。", "keywords": ["drummer", "blades", "simultaneously"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "Individual strength matters, but flawless cohesion and timing propel the boat across the finish line fastest.", "zh": "個人臂力固然重要，但天衣無縫的團隊凝聚力與節奏一致性，才是推動龍舟最快衝過終點線的關鍵。", "keywords": ["cohesion", "propel", "timing"] },
      { "id": 5, "speaker": "Dylan", "avatar": "👦", "en": "The steersman also shouted commands to keep our narrow keel tracking dead straight without wobbling.", "zh": "站在船尾的舵手也一直在大聲喊口令，確保我們修長狹窄的龍舟龍骨筆直平穩破浪，不產生搖晃。", "keywords": ["steersman", "wobbling", "keel"] },
      { "id": 6, "speaker": "Chloe", "avatar": "👧", "en": "One boat, one beat, one unified heartbeat. We are definitely bringing home the championship trophy next month!", "zh": "同舟共濟，同一鼓點，同一顆心。下個月我們一定能把冠軍獎盃抱回家！", "keywords": ["championship", "unified", "trophy"] }
    ],
    "vocabulary": [
      { "word": "synchronize", "phonetic": "/ˈsɪŋ.krə.naɪz/", "pos": "v.", "zh": "使同步、動作協調一致", "example": "Swimmers synchronized their graceful arm movements." },
      { "word": "cohesion", "phonetic": "/koʊˈhiː.ʒən/", "pos": "n.", "zh": "凝聚力、團結力", "example": "Team cohesion was the decisive factor in their championship win." },
      { "word": "propel", "phonetic": "/prəˈpel/", "pos": "v.", "zh": "推進、驅使前進", "example": "Powerful strokes propelled the sleek canoe across the finish line." }
    ],
    "dailyPhrase": { "en": "One beat, one unified heartbeat.", "zh": "同頻共振、同舟共濟的團結精神。" },
    "cultureTip": "端午龍舟競渡（Dragon Boat Racing）強調高度的團隊協作（team cohesion）。船首鼓手（drummer）掌控航速節奏，划手（paddlers）需做到零秒差的「整齊劃一（synchronized strokes）」，象徵同舟共濟的力量。"
  },

  # 05-27 [國小初階]
  {
    "id": "dialogue-0527",
    "date": "05-27",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "在地美食",
    "topic": {
      "en": "Homemade Summer Treat: Hand-washing Wild Aiyu Jelly with Fresh Lemon",
      "zh": "廚房消暑甜品：動手做手洗天然檸檬愛玉凍"
    },
    "situation": "初夏午後廚房裡，Ben 和 Lily 圍在裝滿冷開水的水盆旁，一起揉搓布袋裡的愛玉子製作晶瑩果凍。",
    "speakers": {
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Lily": { "role": "Lily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0527.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ben", "avatar": "👦", "en": "Lily, I put tiny dried aiyu seeds into this clean cotton filter pouch.", "zh": "Lily，我已經把乾燥的小愛玉子裝進這個乾淨的純棉濾袋裡了。", "keywords": ["aiyu seeds", "filter pouch", "cotton"] },
      { "id": 2, "speaker": "Lily", "avatar": "👧", "en": "Submerge it into the bowl of mineral water and knead it gently with clean hands.", "zh": "把它浸入裝滿礦泉水的水盆裡，然後用洗乾淨的雙手輕柔地搓揉它。", "keywords": ["submerge", "knead", "mineral water"] },
      { "id": 3, "speaker": "Ben", "avatar": "👦", "en": "Look! The water is turning golden and slimy. The natural plant pectin is coming out!", "zh": "你看！水慢慢變成金黃色而且滑滑的了。天然的植物果膠跑出來了！", "keywords": ["slimy", "pectin", "golden"] },
      { "id": 4, "speaker": "Lily", "avatar": "👧", "en": "Chill it in the refrigerator for thirty minutes until it sets into a wobbly jelly.", "zh": "放進冰箱冷藏三十分鐘，它就會凝結成 Q 彈晃動的果凍囉。", "keywords": ["refrigerator", "wobbly", "jelly"] },
      { "id": 5, "speaker": "Ben", "avatar": "👦", "en": "Top it with fresh lemon juice and honey drizzle. It is the ultimate cool summer dessert!", "zh": "最後淋上新鮮檸檬汁和少許香醇蜂蜜。這簡直是夏日終極消暑甜點！", "keywords": ["lemon juice", "honey", "dessert"] }
    ],
    "vocabulary": [
      { "word": "submerge", "phonetic": "/səbˈmɝːdʒ/", "pos": "v.", "zh": "浸入水中、沒入液體中", "example": "Submerge the eggs into boiling water for six minutes." },
      { "word": "pectin", "phonetic": "/ˈpek.tɪn/", "pos": "n.", "zh": "果膠（天然植物凝固成分）", "example": "Apples are rich in natural pectin used for making jam." },
      { "word": "wobbly", "phonetic": "/ˈwɑː.bli/", "pos": "adj.", "zh": "搖晃的、Q彈晃動的", "example": "The gelatine pudding was delicious and delightfully wobbly." }
    ],
    "dailyPhrase": { "en": "Top it with...", "zh": "在頂部淋上……或撒上配料。" },
    "cultureTip": "愛玉（Aiyu Jelly）是台灣特有的天然消暑甜品，由愛玉子（aiyu seeds）在含有鈣鎂礦物質的涼水中搓洗釋放果膠凝結而成。搭配現擠檸檬汁與蜂蜜（lemon & honey），熱量低且清涼潤喉。"
  },

  # 05-28 [國小中高]
  {
    "id": "dialogue-0528",
    "date": "05-28",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "暑前閱讀",
    "topic": {
      "en": "Summer Reading List: Picking Thrilling Adventure Books from the Library",
      "zh": "挑選暑前閱讀書單：在圖書館遇見冒險與科普好書"
    },
    "situation": "五月底放學後，Nathan 和 Zoe 來到市立圖書館，在書架前討論挑選即將到來的夏日閱讀清單。",
    "speakers": {
      "Nathan": { "role": "Nathan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0528.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Nathan", "avatar": "👦", "en": "Zoe, the librarian just put up the 'Summer Reading Quest' showcase near the entrance!", "zh": "Zoe，圖書館館員剛剛在門口附近佈置好了『夏日閱讀探索任務』的精選特展呢！", "keywords": ["librarian", "showcase", "Summer Reading"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Awesome! I am looking for exciting mystery adventure novels with puzzles and secret codes.", "zh": "太棒了！我正在尋找充滿謎題與解密暗號的精彩懸疑冒險小說。", "keywords": ["mystery", "adventure", "secret codes"] },
      { "id": 3, "speaker": "Nathan", "avatar": "👦", "en": "I picked out an illustrated encyclopedia about deep-sea marine exploration and sunken shipwrecks.", "zh": "我挑了一本關於深海深潛探索與古老沉船探秘的彩色圖解百科全書。", "keywords": ["encyclopedia", "shipwrecks", "deep-sea"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Our library card allows us to borrow up to ten books for a month at a time.", "zh": "我們的借書證一次可以借多達十本書，而且能借整整一個月呢。", "keywords": ["library card", "borrow", "books"] },
      { "id": 5, "speaker": "Nathan", "avatar": "👦", "en": "Diving into thrilling stories during lazy summer afternoons is like traveling across galaxies for free.", "zh": "在悠閒的夏日午後沉浸在扣人心弦的故事裡，就像不用花半毛錢就能暢遊不同星系一樣。", "keywords": ["thrilling", "galaxies", "traveling"] }
    ],
    "vocabulary": [
      { "word": "shipwreck", "phonetic": "/ˈʃɪp.rek/", "pos": "n.", "zh": "沉船、船難殘骸", "example": "Divers explored the coral-encrusted shipwreck on the ocean floor." },
      { "word": "encyclopedia", "phonetic": "/ɪnˌsaɪ.kləˈpiː.di.ə/", "pos": "n.", "zh": "百科全書", "example": "The astronomy encyclopedia contains detailed planetary maps." },
      { "word": "showcase", "phonetic": "/ˈʃoʊ.keɪs/", "pos": "n./v.", "zh": "展示櫃、展示特陳", "example": "The science museum created a showcase of renewable energy models." }
    ],
    "dailyPhrase": { "en": "Dive into a book.", "zh": "沉浸在書本的精彩世界裡。" },
    "cultureTip": "歐美公共圖書館每年夏初都會舉辦「Summer Reading Challenge（夏日閱讀挑戰）」，設計閱讀集章卡與徽章獎勵，鼓勵孩子在長假期間維持閱讀習慣（prevent summer slide）。"
  },

  # 05-29 [國中挑戰]
  {
    "id": "dialogue-0529",
    "date": "05-29",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "夜市文化",
    "topic": {
      "en": "Sunset Jogging along the Embankment: Night Market Snacks & Summer Vibes",
      "zh": "傍晚河堤慢跑與夜市偶遇：晚風中的青春活力與消暑小吃"
    },
    "situation": "初夏傍晚微風徐徐，Julian 和 Hannah 沿著河堤慢跑結束後，順道走進夜市點了清爽的綜合豆花。",
    "speakers": {
      "Julian": { "role": "Julian", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Hannah": { "role": "Hannah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0529.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Julian", "avatar": "👦", "en": "The twilight sky over the river looks like a watercolor painting blending violet and apricot hues.", "zh": "河面上的暮色天空看起來就像一幅水彩畫，交融著紫羅蘭與杏黃色的夢幻色調。", "keywords": ["twilight", "watercolor", "apricot"] },
      { "id": 2, "speaker": "Hannah", "avatar": "👧", "en": "That five-kilometer jog felt so liberating with the evening river breeze cooling our foreheads.", "zh": "那趟五公里的慢跑感覺好舒暢自由，傍晚的河畔晚風把我們額頭上的熱汗都吹涼了。", "keywords": ["liberating", "river breeze", "foreheads"] },
      { "id": 3, "speaker": "Julian", "avatar": "👦", "en": "Listen to the distant cheerful chatter. The weekend night market across the pedestrian bridge is buzzing!", "zh": "聽聽遠處熱鬧歡樂的喧鬧聲。人行景觀橋另一端的週末夜市已經人聲鼎沸了！", "keywords": ["chatter", "night market", "buzzing"] },
      { "id": 4, "speaker": "Hannah", "avatar": "👧", "en": "How about grabbing a bowl of iced tofu pudding topped with chewy taro balls and boba pearls?", "zh": "不如我們去吃一碗冰豆花吧，上面加 Q 彈的芋圓和黑糖珍珠粉圓怎麼樣？", "keywords": ["tofu pudding", "taro balls", "boba pearls"] },
      { "id": 5, "speaker": "Julian", "avatar": "👦", "en": "Count me in! A splash of sweet brown sugar syrup over crushed shaved ice is heaven after a good workout.", "zh": "算我一份！在滿滿的碎剉冰上淋上一勺香甜黑糖糖水，在暢快運動後簡直就是天堂般的享受。", "keywords": ["shaved ice", "brown sugar", "workout"] },
      { "id": 6, "speaker": "Hannah", "avatar": "👧", "en": "Exercising hard and then enjoying delicious local street food with great friends embodies summer youth.", "zh": "盡情揮灑汗水運動，再跟好朋友一起品嘗在地街頭美食，這正是夏日青春最純粹的寫照。", "keywords": ["youth", "street food", "embodies"] }
    ],
    "vocabulary": [
      { "word": "twilight", "phonetic": "/ˈtwaɪ.laɪt/", "pos": "n.", "zh": "暮光、黃昏、薄暮", "example": "Streetlights flickered on as twilight settled over the city." },
      { "word": "taro", "phonetic": "/ˈter.oʊ/", "pos": "n.", "zh": "芋頭", "example": "Chewy purple taro balls are a favorite Taiwanese dessert topping." },
      { "word": "pedestrian", "phonetic": "/pəˈdes.tri.ən/", "pos": "n./adj.", "zh": "行人、步行的", "example": "The pedestrian bridge offers a safe route across the busy avenue." }
    ],
    "dailyPhrase": { "en": "Buzz with energy.", "zh": "充滿生機活力、熱鬧沸騰。" },
    "cultureTip": "夜市（Night Market）與河濱慢跑道是台灣初夏極具活力的生活縮影。運動後享用一碗冰鎮黑糖豆花（Iced Tofu Pudding with Taro Balls），是結合在地美食與休閒運動的經典消暑日常。"
  },

  # 05-30 [高中進階]
  {
    "id": "dialogue-0530",
    "date": "05-30",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "轉型前瞻",
    "topic": {
      "en": "Bridging May and June: Preparing for Final Exams and Graduation Reflections",
      "zh": "告別五月、迎向六月：期末考衝刺倒數與畢業季的青春省思"
    },
    "situation": "五月倒數第二天傍晚，高二學生 Sean 和 Melody 走在林蔭大道上，回顧五月的充實並為即將到來的六月期末考與學長姐畢業季做準備。",
    "speakers": {
      "Sean": { "role": "Sean", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Melody": { "role": "Melody", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0530.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sean", "avatar": "👨‍🎓", "en": "Melody, tomorrow will be the final day of May. The golden shower trees on campus are already bursting into yellow blossoms.", "zh": "Melody，明天就是五月的最後一天了。校園裡的阿勃勒樹已經開滿了一串串如黃金雨般的繁花呢。", "keywords": ["golden shower", "blossoms", "campus"] },
      { "id": 2, "speaker": "Melody", "avatar": "👩‍🎓", "en": "Those vibrant yellow cascades signal the bittersweet arrival of June—the season of senior graduations and comprehensive final exams.", "zh": "那耀眼的金黃花瀑標誌著六月的到來——這是一個既欣喜又帶著感傷的季節：高三學長姐即將畢業，而我們也即將面臨期末總複習考驗。", "keywords": ["bittersweet", "cascades", "graduations"] },
      { "id": 3, "speaker": "Sean", "avatar": "👨‍🎓", "en": "Watching the seniors rehearse their commencement ceremony reminds me that our high school journey is hurtling forward at breakneck speed.", "zh": "看著學長姐排練畢業典禮，提醒了我：我們的高中時光也正以飛快的速度向前奔馳。", "keywords": ["rehearse", "breakneck", "commencement"] },
      { "id": 4, "speaker": "Melody", "avatar": "👩‍🎓", "en": "That makes living intentionally even more imperative. We cannot afford to drift aimlessly through these formative years.", "zh": "這讓帶著自覺與目標生活顯得更加迫切。在這些奠定人生基礎的關鍵塑造期，我們絕不能漫無目的地隨波逐流。", "keywords": ["intentionally", "formative", "drift"] },
      { "id": 5, "speaker": "Sean", "avatar": "👨‍🎓", "en": "Let's structure our final exam review timetable tonight, leaving ample cushion for challenging physics and literature modules.", "zh": "我們今晚就先把期末考的複習行事曆排定好，為難度較高的物理與文學單元預留充裕的時間緩衝。", "keywords": ["timetable", "cushion", "modules"] },
      { "id": 6, "speaker": "Melody", "avatar": "👩‍🎓", "en": "Step into June with clear focus and courage. Finish this semester on an unforgettably triumphant note!", "zh": "懷抱清晰的專注力與勇氣邁入六月吧。讓我們用無懈可擊的亮麗成果，為這個學期畫下最精彩的句點！", "keywords": ["triumphant", "courage", "unforgettably"] }
    ],
    "vocabulary": [
      { "word": "bittersweet", "phonetic": "/ˌbɪt̬.ɚˈswiːt/", "pos": "adj.", "zh": "苦樂參半的、喜憂交集的", "example": "Graduation is a bittersweet milestone filled with nostalgia and anticipation." },
      { "word": "formative", "phonetic": "/ˈfɔːr.mə.t̬ɪv/", "pos": "adj.", "zh": "形成期的、具有決定性塑造影響的", "example": "High school represents a formative phase for personality and values." },
      { "word": "triumphant", "phonetic": "/traɪˈʌm.fənt/", "pos": "adj.", "zh": "勝利的、凱旋而歸的、成功的", "example": "The orchestra concluded the symphony on a triumphant final chord." }
    ],
    "dailyPhrase": { "en": "At breakneck speed.", "zh": "以極快的速度、飛快狂飆。" },
    "cultureTip": "每年五月底至六月初，台灣校園常見的「阿勃勒（Golden Shower Tree）」盛開金黃花串，隨風飄落被稱為「黃金雨」，與鳳凰花一同象徵畢業季（Graduation season）與學期總結的到來。"
  },

  # 05-31 [高中進階]
  {
    "id": "dialogue-0531",
    "date": "05-31",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "健康公民",
    "topic": {
      "en": "World No Tobacco Day: Youth Resistance to Vaping & Promoting Respiratory Health",
      "zh": "世界無菸日：拒絕電子煙誘惑，擁抱清新純淨肺部與健康人生"
    },
    "situation": "5月31日世界無菸日，校園春暉健康社幹部 Kevin 和 Audrey 在朝會宣導電子煙防制與呼吸系統健康科學。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Audrey": { "role": "Audrey", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0531.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "👨‍🎓", "en": "Audrey, today marks World No Tobacco Day. The World Health Organization is warning about insidious marketing targeting youth.", "zh": "Audrey，今天是世界無菸日。世界衛生組織正嚴正警告菸草與電子煙產業針對青少年暗中開展的包裝行銷伎倆。", "keywords": ["World No Tobacco Day", "insidious", "marketing"] },
      { "id": 2, "speaker": "Audrey", "avatar": "👩‍🎓", "en": "Indeed. E-cigarette manufacturers aggressively promote sleek devices disguised as high-tech USB drives with fruity flavorings.", "zh": "確實如此。電子煙製造商極具侵略性地推廣偽裝成高科技隨身碟的時尚裝置，並加入水果香甜口味來降低戒心。", "keywords": ["disguised", "e-cigarette", "flavorings"] },
      { "id": 3, "speaker": "Kevin", "avatar": "👨‍🎓", "en": "Many teens fallaciously assume vapor is merely harmless water mist, ignoring toxic heavy metals, formaldehyde, and addictive nicotine.", "zh": "許多青少年錯誤地以為煙霧只是無害的水蒸氣，卻全然無視其中深藏的重金屬毒素、甲醛以及具強烈成癮性的高濃度尼古丁。", "keywords": ["fallaciously", "formaldehyde", "nicotine"] },
      { "id": 4, "speaker": "Audrey", "avatar": "👩‍🎓", "en": "Pulmonary specialists have demonstrated that inhaling these heated aerosolized chemicals causes severe lung inflammation and irreversible scarring.", "zh": "胸腔科專科醫師已證實，吸入這些加熱霧化的化學成分會導致嚴重的急性肺部發炎與不可逆的肺纖維化疤痕。", "keywords": ["pulmonary", "aerosolized", "irreversible"] },
      { "id": 5, "speaker": "Kevin", "avatar": "👨‍🎓", "en": "True rebellion is not succumbing to manipulative commercial addiction; it is having the independent intellect to say no.", "zh": "真正的青春叛逆與酷，絕不是屈服於商業操弄的成癮陷阱；而是擁有獨立自主的思辨力，堅定大聲說不。", "keywords": ["rebellion", "manipulative", "intellect"] },
      { "id": 6, "speaker": "Audrey", "avatar": "👩‍🎓", "en": "Protect our lungs and breathe clean air freely. Clean breathing is the absolute foundation of lifelong athletic vitality and clear cognition.", "zh": "捍衛我們的肺部健康，自由呼吸純淨的空氣。清新呼吸正是終身充沛運動活力與敏銳思維認知的最根本基石。", "keywords": ["cognition", "vitality", "foundation"] }
    ],
    "vocabulary": [
      { "word": "insidious", "phonetic": "/ɪnˈsɪd.i.əs/", "pos": "adj.", "zh": "潛伏暗藏的、不知不覺間為害的", "example": "High blood pressure is an insidious condition with few early warning signs." },
      { "word": "fallaciously", "phonetic": "/fəˈleɪ.ʃəs.li/", "pos": "adv.", "zh": "錯誤地、基於謬誤地", "example": "He fallaciously assumed online rumors were verified facts." },
      { "word": "pulmonary", "phonetic": "/ˈpʊl.mə.ner.i/", "pos": "adj.", "zh": "肺部的、呼吸器官的", "example": "Regular aerobic jogging enhances cardiovascular and pulmonary capacity." }
    ],
    "dailyPhrase": { "en": "Say no to...", "zh": "堅定對……說不、拒絕……的誘惑。" },
    "cultureTip": "每年5月31日是世界衛生組織（WHO）設立的「世界無菸日（World No Tobacco Day）」。近年重點鎖定防制「電子煙（Vaping/E-cigarettes）」對青少年的毒害與成癮陷阱，推廣拒菸無菸校園環境。"
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
    for d in MAY_DIALOGUES:
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
    print(f"成功將 5 月份對話寫入 {DATA_FILE}！總篇數更新為: {len(existing_data)} (新增 {added_count} 篇)")

    # 同步更新 js/data.js
    with open(JS_FILE, 'w', encoding='utf-8') as f:
        f.write("// 365 每日生活美語對話資料庫 (全年度)\n")
        f.write("const DIALOGUES_DATA = ")
        f.write(json.dumps(existing_data, ensure_ascii=False, indent=2))
        f.write(";\n")
    print(f"成功同步更新 {JS_FILE}！")

if __name__ == '__main__':
    main()
