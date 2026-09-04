#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次建立 7 月份生活對話 (07-01 至 07-31，共 31 篇)
涵蓋暑假生活自律、晨泳與沙灘沙堡、科學夏令營、小暑與大暑節氣、世界人口日、
高山露營觀星、世界青年技能日、阿波羅登月日、無痕山林溪流探索、數位遊牧思辨、
世界肝炎日公衛奇蹟、國際友誼日明信片等豐富主題！
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'dialogues.json')
JS_FILE = os.path.join(BASE_DIR, 'js', 'data.js')

JULY_DIALOGUES = [
  # 07-01 [國小中高]
  {
    "id": "dialogue-0701",
    "date": "07-01",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "暑期自律",
    "topic": {
      "en": "Welcoming July: Morning Routine & Ditching Couch Potato Habits",
      "zh": "迎接七月盛夏：規劃規律作息不當沙發馬鈴薯"
    },
    "situation": "7月1日暑假第一天早晨，Kevin 和 Emma 在社區公園晨跑拉筋，互相約定長假不沉迷手機與電視。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0701.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "👦", "en": "Good morning, Emma! Welcome to the very first official day of July and summer vacation!", "zh": "早安，Emma！歡迎迎來七月份與暑假正式開跑的第一天！", "keywords": ["July", "summer vacation", "official"] },
      { "id": 2, "speaker": "Emma", "avatar": "👧", "en": "Good morning! My mom warned me not to turn into a lazy couch potato staring at television screens all day.", "zh": "早安！我媽媽警告我，絕對不能變成整天癱在沙發上盯著電視螢幕看的懶惰沙發馬鈴薯。", "keywords": ["couch potato", "screens", "warned"] },
      { "id": 3, "speaker": "Kevin", "avatar": "👦", "en": "I made a daily planner: waking up at seven thirty, reading for one hour, and playing sports in the cool afternoon.", "zh": "我做了一份每日作息計畫表：七點半起床、晨讀一小時，然後下午涼爽時出門運動鍛鍊身體。", "keywords": ["planner", "waking up", "sports"] },
      { "id": 4, "speaker": "Emma", "avatar": "👧", "en": "That keeps your brain sharp and your body energetic throughout the two-month break.", "zh": "這樣能讓你在這兩個月的長假裡，大腦隨時保持敏銳清晰，身體也隨時充滿活力。", "keywords": ["sharp", "energetic", "break"] },
      { "id": 5, "speaker": "Kevin", "avatar": "👦", "en": "Let's be mutual accountability partners and check in every Monday morning!", "zh": "那我們就來當互相督促激勵的夥伴，每週一早上互相檢查執行進度吧！", "keywords": ["accountability", "partners", "check in"] }
    ],
    "vocabulary": [
      { "word": "couch potato", "phonetic": "/ˈkaʊtʃ pəˌteɪ.t̬oʊ/", "pos": "n.", "zh": "沙發馬鈴薯、整天坐著看電視的懶人", "example": "Don't be a couch potato all summer; go outdoors and cycle." },
      { "word": "accountability", "phonetic": "/əˌkaʊn.t̬əˈbɪl.ə.t̬i/", "pos": "n.", "zh": "負責任、互相督促問責", "example": "Study groups provide peer accountability." },
      { "word": "energetic", "phonetic": "/ˌen.ɚˈdʒet̬.ɪk/", "pos": "adj.", "zh": "精力充沛的、活力十足的", "example": "The energetic puppy bounded across the yard." }
    ],
    "dailyPhrase": { "en": "Check in on someone.", "zh": "向某人打聽近況、關心進度。" },
    "cultureTip": "「Couch potato（沙發馬鈴薯）」是美式英語中極具生動畫面的俚語，形容假期整天窩在沙發上吃零食看電視不運動的人。專家建議暑假初期訂定每日固定作息（daily routine），能有效預防「暑期退步（summer slide）」。"
  },

  # 07-02 [國小初階]
  {
    "id": "dialogue-0702",
    "date": "07-02",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "水上運動",
    "topic": {
      "en": "Morning Swimming Lessons: Kicking & Breathing Underwater",
      "zh": "晨泳課的清涼水花：學會水中換氣與浮板打水"
    },
    "situation": "炎熱的早晨，Leo 和 Mia 戴好泳鏡和泳帽，跳進市立游泳池跟教練學習自由式打水技巧。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0702.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Mia, dip your toes in! The turquoise water feels so cooling on this scorching morning!", "zh": "Mia，把腳趾頭伸進水裡！在這麼酷熱的早晨，這池清澈碧藍的水感覺太涼爽舒服了！", "keywords": ["turquoise", "cooling", "toes"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "Remember our coach's instruction: hold the kickboard with straight arms and kick from your hips.", "zh": "要記住教練的指導動作：雙臂伸直抓穩浮板，大腿從臀部發力打水。", "keywords": ["kickboard", "straight arms", "instruction"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Splash, splash! Bubble out air gently underwater, and turn your head sideways to breathe in.", "zh": "水花四濺！在水裡用鼻子輕輕吐出泡泡，頭轉向側邊大口吸氣。", "keywords": ["splash", "breathe in", "sideways"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "I did it! I swam across the twenty-five-meter lane without stopping for the first time!", "zh": "我做到了！我第一次中間完全沒停下來，一口氣游完了整條二十五公尺的水道！", "keywords": ["lane", "swam across", "stopping"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "High five! Swimming is definitely the best sport to stay fit and cool during hot July.", "zh": "擊掌！在炎熱的七月天裡，游泳絕對是保持體能健康又消暑的最棒運動了。", "keywords": ["high five", "hot July", "swimming"] }
    ],
    "vocabulary": [
      { "word": "kickboard", "phonetic": "/ˈkɪk.bɔːrd/", "pos": "n.", "zh": "游泳浮板", "example": "Hold the kickboard firmly while practicing flutter kicks." },
      { "word": "turquoise", "phonetic": "/ˈtɝː.kɔɪz/", "pos": "adj./n.", "zh": "綠松石色的、碧藍清澈的", "example": "Tropical islands are famed for their turquoise lagoons." },
      { "word": "sideways", "phonetic": "/ˈsaɪd.weɪz/", "pos": "adv.", "zh": "向側面、橫向地", "example": "Turn your head sideways to catch a breath while swimming freestyle." }
    ],
    "dailyPhrase": { "en": "Dip one's toes in.", "zh": "把腳趾探入水中感受水溫；初次涉足嘗試。" },
    "cultureTip": "游泳（Swimming）是少數運用全身肌肉群且不傷膝蓋關節的低衝擊有氧運動。學會在水中規律吐氣換氣（bilateral breathing）與正確腿部打水，是水上安全自救的關鍵核心技能。"
  },

  # 07-03 [國中挑戰]
  {
    "id": "dialogue-0703",
    "date": "07-03",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "創客夏令營",
    "topic": {
      "en": "Science Summer Camp: Assembling Solar-Powered Rover Cars",
      "zh": "科學夏令營：動手組裝太陽能遙控探測車"
    },
    "situation": "科技館夏令營創客工作坊裡，David 和 Chloe 拿著螺絲起子和光伏面板，組裝一台微型火星探測車模型。",
    "speakers": {
      "David": { "role": "David", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0703.mp3",
    "dialogue": [
      { "id": 1, "speaker": "David", "avatar": "👦", "en": "Chloe, I just fastened the six high-traction rubber wheels onto our miniature rover chassis.", "zh": "Chloe，我剛剛把六顆高抓地力的橡膠越野輪牢牢固定在我們的迷你探測車底盤上了。", "keywords": ["chassis", "traction", "fastened"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "Great! Now let's connect the photovoltaic solar panel to the miniature electric motor with red and black leads.", "zh": "太好了！現在我們用紅黑導線把光伏太陽能面板與微型電動馬達連接起來吧。", "keywords": ["photovoltaic", "solar panel", "leads"] },
      { "id": 3, "speaker": "David", "avatar": "👦", "en": "Make sure the solder joints are clean. Any loose contact will cause an open circuit.", "zh": "確保焊點乾淨牢固。任何接觸不良都會導致電路斷路無法運轉。", "keywords": ["solder joints", "circuit", "loose"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "Let's carry it outside onto the sunny plaza pavement. Look, as soon as direct sun rays hit the cells, the gear spins!", "zh": "我們把它拿到外面灑滿陽光的廣場地面上試車。你看，直射陽光一照到電池晶片，齒輪立刻瘋狂旋轉起來了！", "keywords": ["plaza", "gear spins", "direct sun"] },
      { "id": 5, "speaker": "David", "avatar": "👦", "en": "It is climbing right over that wooden ramp obstacle! Converting clean light energy directly into mechanical propulsion is awesome.", "zh": "它正直接翻越過那個木製斜坡障礙物呢！把純淨光能直接轉換為機械推進力真是太酷炫了。", "keywords": ["obstacle", "propulsion", "converting"] },
      { "id": 6, "speaker": "Chloe", "avatar": "👧", "en": "Hands-on engineering demystifies abstract textbook physics and turns scientific principles into tangible wonders.", "zh": "動手實作工程徹底打破了抽象課本物理的神秘感，把科學原理化為看得見、摸得著的神奇造物。", "keywords": ["demystifies", "hands-on", "tangible"] }
    ],
    "vocabulary": [
      { "word": "chassis", "phonetic": "/ˈʃæs.i/", "pos": "n.", "zh": "（車輛或機器）底盤、車架", "example": "Engineers constructed a lightweight aluminum chassis for the solar racer." },
      { "word": "propulsion", "phonetic": "/prəˈpʌl.ʃən/", "pos": "n.", "zh": "推進、推進力", "example": "Jet engines provide immense forward propulsion." },
      { "word": "demystify", "phonetic": "/ˌdiːˈmɪs.tə.faɪ/", "pos": "v.", "zh": "使通俗易懂、揭開……的神秘面紗", "example": "Science communicators work to demystify quantum mechanics for the public." }
    ],
    "dailyPhrase": { "en": "As soon as...", "zh": "一……就……（引導即時條件子句）。" },
    "cultureTip": "創客教育（Maker Education / STEM Camps）在暑期深受青少年喜愛。利用太陽能光伏元件（Photovoltaic cells）親手製作小型火星探測車（rover），直觀體驗可再生能源與機械工程的奧妙。"
  },

  # 07-04 [國小初階]
  {
    "id": "dialogue-0704",
    "date": "07-04",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "庭院歡樂",
    "topic": {
      "en": "Watermelon Seed Spitting Fun: Juicy Summer Backyard Party",
      "zh": "夏日庭院西瓜派對：比比看誰吐西瓜子吐得遠"
    },
    "situation": "炎熱的週六午後，Tyler 和 Amy 坐在後院涼亭長凳上吃著冰鎮西瓜，進行一場逗趣的吐西瓜子比賽。",
    "speakers": {
      "Tyler": { "role": "Tyler", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Amy": { "role": "Amy", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0704.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tyler", "avatar": "👦", "en": "Amy, this cold watermelon slice is dripping with sweet, ice-cold red juice!", "zh": "Amy，這片冰西瓜正滴著香甜冰涼的鮮紅西瓜汁呢！", "keywords": ["dripping", "watermelon slice", "juice"] },
      { "id": 2, "speaker": "Amy", "avatar": "👧", "en": "Slurp! It is the best antidote to this scorching thirty-four degree afternoon heat.", "zh": "吸溜一口！這簡直是對抗這個高達三十四度酷熱午後的最佳良藥。", "keywords": ["antidote", "slurp", "afternoon heat"] },
      { "id": 3, "speaker": "Tyler", "avatar": "👦", "en": "Look at these slippery black seeds. Let's see who can spit a seed the farthest across the lawn!", "zh": "看這些滑溜溜的黑色西瓜子。我們來比比看誰能把西瓜子吐過草坪吐得最遠！", "keywords": ["slippery", "spit", "lawn"] },
      { "id": 4, "speaker": "Amy", "avatar": "👧", "en": "One, two, three, ptooey! Mine landed near the white daisy flowerbed!", "zh": "一、二、三，呸！我的子飛到了白色小雛菊花圃旁邊耶！", "keywords": ["flowerbed", "daisy", "landed"] },
      { "id": 5, "speaker": "Tyler", "avatar": "👦", "en": "Haha, yours flew three meters! Eating watermelon outdoors in summer is simply the best.", "zh": "哈哈，你的足足飛了三公尺遠！夏天坐在戶外大口吃西瓜真是最純粹的快樂了。", "keywords": ["flew", "outdoors", "simply the best"] }
    ],
    "vocabulary": [
      { "word": "slippery", "phonetic": "/ˈslɪp.ɚ.i/", "pos": "adj.", "zh": "滑溜的、易滑落的", "example": "Wet bathroom tiles become extremely slippery." },
      { "word": "flowerbed", "phonetic": "/ˈflaʊ.ɚ.bed/", "pos": "n.", "zh": "花圃、花壇", "example": "Colorful marigolds blossomed in the circular flowerbed." },
      { "word": "antidote", "phonetic": "/ˈæn.t̬i.doʊt/", "pos": "n.", "zh": "解毒劑、消除不適的良藥", "example": "Laughter is celebrated as the best antidote to stress." }
    ],
    "dailyPhrase": { "en": "Simply the best.", "zh": "簡直是最棒的、無與倫比。" },
    "cultureTip": "吐西瓜子比賽（Watermelon seed spitting contest）是歐美鄉村夏季園遊會的經典傳統趣味活動，參賽者比拼肺活量與角度技巧，既消暑又充滿歡笑。"
  },

  # 07-05 [國小中高]
  {
    "id": "dialogue-0705",
    "date": "07-05",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "社區樂活",
    "topic": {
      "en": "Chilling at the Community Library: Free AC and Good Books",
      "zh": "社區圖書館的消暑時光：享受免費涼爽冷氣與探索知識寶庫"
    },
    "situation": "正午熱浪滾滾，Sam 和 Olivia 帶著環保水壺走進社區圖書館，在安靜清涼的少兒閱讀區閱讀漫畫與科普書。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0705.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Ah, stepping through the library glass door feels like walking into an oasis of cool air!", "zh": "啊，推開圖書館玻璃門的那一刻，簡直就像走進了一座清涼宜人的沙漠綠洲！", "keywords": ["glass door", "oasis", "cool air"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👧", "en": "The outside pavement was literally radiating heat waves off the tarmac.", "zh": "外面的柏油馬路剛剛真的熱到像是都在散發陣陣滾燙的熱浪呢。", "keywords": ["pavement", "radiating", "heat waves"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Instead of blasting expensive electricity at home, studying here is environmentally friendly and cozy.", "zh": "與其在家裡整天狂開昂貴的冷氣浪費電，來這裡安靜看書既節能環保又舒服愜意。", "keywords": ["environmentally friendly", "electricity", "cozy"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👧", "en": "I found a brand new series of illustrated national geographic magazines about polar wildlife.", "zh": "我找到了最新一期關於極地野生動物的全彩國家地理雜誌呢。", "keywords": ["national geographic", "wildlife", "magazines"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Let's read quietly until five in the afternoon, when the sun begins sinking toward the hills.", "zh": "那我們就安靜閱讀到下午五點，等烈日漸漸西斜落到山後再回家吧。", "keywords": ["quietly", "sinking", "afternoon"] }
    ],
    "vocabulary": [
      { "word": "oasis", "phonetic": "/oʊˈeɪ.sɪs/", "pos": "n.", "zh": "綠洲、令人舒適安寧的避風港", "example": "The shaded courtyard was a peaceful oasis amid the bustling city." },
      { "word": "tarmac", "phonetic": "/ˈtɑːr.mæk/", "pos": "n.", "zh": "柏油路面、停機坪", "example": "Heat shimmered visibly above the airport tarmac." },
      { "word": "blast", "phonetic": "/blæst/", "pos": "v.", "zh": "猛力開動、狂吹（冷氣或音響）", "example": "Don't blast the air conditioner at full blast all day." }
    ],
    "dailyPhrase": { "en": "Step into an oasis.", "zh": "踏入綠洲、進入清涼愜意之所。" },
    "cultureTip": "公共圖書館在許多城市被指定為「Cooling Center（避暑中心）」，為社區民眾與學生在極端熱浪期間提供免費冷氣、乾淨飲用水與豐富文化資源，兼具公共衛生與環保節能意義。"
  },

  # 07-06 [國中挑戰]
  {
    "id": "dialogue-0706",
    "date": "07-06",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "挑戰自我",
    "topic": {
      "en": "Dreaming of Cycling Around Taiwan: Route Planning & Gear",
      "zh": "盛夏單車環島夢想：規劃環島路線、裝備清單與安全防護"
    },
    "situation": "國二升國三的暑假，Julian 和 Hannah 在單車店看著台灣全島地圖，興奮討論未來的單車環島成年禮計畫。",
    "speakers": {
      "Julian": { "role": "Julian", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Hannah": { "role": "Hannah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0706.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Julian", "avatar": "👦", "en": "Hannah, look at this Cycling Route 1 map looping around the entire island for nine hundred kilometers!", "zh": "Hannah，你看這張環繞全島整整九百公里的『單車環島 1 號線』路線地圖！", "keywords": ["Cycling Route 1", "looping", "kilometers"] },
      { "id": 2, "speaker": "Hannah", "avatar": "👧", "en": "Cycling around Taiwan is a classic rite of passage for Taiwanese youths. Completing it takes immense physical stamina and mental determination.", "zh": "單車環島是台灣年輕人最經典的成年禮之一。要完成它需要無比充沛的體能耐力與強大的心理毅力。", "keywords": ["rite of passage", "stamina", "determination"] },
      { "id": 3, "speaker": "Julian", "avatar": "👦", "en": "Traveling counter-clockwise is smartest because you ride on the seaward side of coastal highways, keeping ocean vistas right beside you.", "zh": "採逆時針方向騎乘是最聰明的做法，因為這樣能始終騎在靠海那一側的公路邊，壯麗海景就在身旁。", "keywords": ["counter-clockwise", "seaward", "vistas"] },
      { "id": 4, "speaker": "Hannah", "avatar": "👧", "en": "Waterproof pannier bags, puncture repair kits, padded cycling shorts, and high-visibility reflective vests are mandatory gear.", "zh": "防水後馬鞍袋、補胎工具組、減震自行車褲以及高可見度反光背心都是絕對必備的裝備清單。", "keywords": ["pannier", "puncture", "reflective vests"] },
      { "id": 5, "speaker": "Julian", "avatar": "👦", "en": "Pedaling along the rugged cliffs of the east coast and conquering Shouka Pass in Pingtung will test our limits.", "zh": "沿著東海岸壯麗險峻的懸崖絕壁踩踏前進，並征服屏東著名的壽卡鐵馬驛站坡道，將徹底考驗我們的極限。", "keywords": ["rugged cliffs", "Shouka Pass", "limits"] },
      { "id": 6, "speaker": "Hannah", "avatar": "👧", "en": "Experiencing your homeland petal by pedal at human speed creates memories that stay etched in your heart for a lifetime.", "zh": "用雙腳踏板的速度與人性的視角一步一腳印丈量故鄉土地，所烙印在心中的記憶將會相伴一生。", "keywords": ["homeland", "etched", "lifetime"] }
    ],
    "vocabulary": [
      { "word": "rite of passage", "phonetic": "/ˌraɪt əv ˈpæs.ɪdʒ/", "pos": "n.", "zh": "成年禮、人生必經的重要過渡儀式", "example": "Graduating from high school is a universal rite of passage." },
      { "word": "counter-clockwise", "phonetic": "/ˌkaʊn.t̬ɚˈklɑːk.waɪz/", "pos": "adv./adj.", "zh": "逆時針方向地", "example": "Runners circle around the track in a counter-clockwise direction." },
      { "word": "pannier", "phonetic": "/ˈpæn.i.ɚ/", "pos": "n.", "zh": "（自行車後座的）雙側掛袋、馬鞍袋", "example": "Pack the heavy camping stove at the bottom of the bicycle pannier." }
    ],
    "dailyPhrase": { "en": "Rite of passage.", "zh": "人生必經的成年禮或里程碑考驗。" },
    "cultureTip": "台灣單車環島（Cycling around Taiwan）享譽國際。教育部體育署規劃的「單車環島1號線（Cycling Route 1）」全長約 968 公里，多數車友偏好「逆時針騎乘（counter-clockwise）」，享受緊鄰太平洋海景的視覺震撼。"
  },

  # 07-07 [國中挑戰]
  {
    "id": "dialogue-0707",
    "date": "07-07",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "節氣智慧",
    "topic": {
      "en": "Xiaoshu Solar Term: Minor Heat, Cooling Foods & Herbal Traditions",
      "zh": "小暑節氣：溫風至、蟋蟀居壁與初夏消暑三伏貼"
    },
    "situation": "二十四節氣迎來「小暑」，Ethan 和 Grace 走在公園林蔭道下，感受盛夏熱浪帶來的悶熱暖風。",
    "speakers": {
      "Ethan": { "role": "Ethan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Grace": { "role": "Grace", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0707.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ethan", "avatar": "👦", "en": "Grace, today marks Xiaoshu, or 'Minor Heat,' the eleventh solar term. Even the gentle breeze feels warm and humid.", "zh": "Grace，今天正是『小暑』，第十一個節氣。連吹過臉頰的微風都感覺帶著溫熱與濕氣呢。", "keywords": ["Xiaoshu", "Minor Heat", "humid"] },
      { "id": 2, "speaker": "Grace", "avatar": "👧", "en": "Ancient texts observed three phenomena for Xiaoshu: warm winds arrive, crickets move to wall crevices, and young eagles practice hunting.", "zh": "古籍記載小暑有三候：溫風至、蟋蟀居壁、鷹始摯（幼鷹開始展翅練習搏擊獵食）。", "keywords": ["phenomena", "crickets", "crevices"] },
      { "id": 3, "speaker": "Ethan", "avatar": "👦", "en": "Although it is called 'Minor Heat,' it signals that the dog days of summer—the infamous 'Sanfu' period—are beginning.", "zh": "雖然名稱叫『小暑』，但它標誌著一年中最酷熱難耐的『三伏天』大幕已經正式拉開了。", "keywords": ["dog days", "Sanfu", "infamous"] },
      { "id": 4, "speaker": "Grace", "avatar": "👧", "en": "Many people visit traditional Chinese medicine clinics during Sanfu to apply herbal patches for winter respiratory health.", "zh": "許多人會在三伏天前往中醫診所貼敷『三伏貼』，利用冬病夏治的原理調理體質、預防冬季呼吸道過敏。", "keywords": ["respiratory", "herbal patches", "clinics"] },
      { "id": 5, "speaker": "Ethan", "avatar": "👦", "en": "Culinary customs suggest eating lotus root and refreshing melon soup to soothe restlessness caused by sweltering temperatures.", "zh": "食俗上也推薦多吃蓮藕、冬瓜排骨湯等清淡食材，安撫因悶熱高溫引發的心神煩躁。", "keywords": ["lotus root", "sweltering", "restlessness"] },
      { "id": 6, "speaker": "Grace", "avatar": "👧", "en": "Harmonizing our diet and daily routine with nature's seasonal pulse keeps our spirits tranquil through the heat.", "zh": "順應大自然的季節節奏來調和飲食與作息，能讓身心在炎炎盛夏中始終保有一份寧靜安舒。", "keywords": ["harmonizing", "tranquil", "seasonal pulse"] }
    ],
    "vocabulary": [
      { "word": "crevice", "phonetic": "/ˈkrev.ɪs/", "pos": "n.", "zh": "裂縫、縫隙", "example": "Small lizards darted into stone wall crevices." },
      { "word": "sweltering", "phonetic": "/ˈswel.tɚ.ɪŋ/", "pos": "adj.", "zh": "悶熱難受的、酷熱的", "example": "Fans whirred tirelessly in the sweltering greenhouse." },
      { "word": "tranquil", "phonetic": "/ˈtræŋ.kwɪl/", "pos": "adj.", "zh": "寧靜的、安詳平靜的", "example": "The mountain lake was tranquil at dawn." }
    ],
    "dailyPhrase": { "en": "The dog days of summer.", "zh": "三伏天、一年中最悶熱難耐的盛夏時節。" },
    "cultureTip": "小暑（Minor Heat）後緊接著進入「三伏天（Dog days of summer）」，此時是一年中陽氣最旺盛的時節。中醫傳統運用「冬病夏治」理念施打「三伏貼（Sanfu herbal acupoints）」，增強呼吸系統免疫力。"
  },

  # 07-08 [高中進階]
  {
    "id": "dialogue-0708",
    "date": "07-08",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "氣候建築",
    "topic": {
      "en": "Urban Heat Island Effect: Architecture & Climate Adaptation",
      "zh": "盛夏熱浪與都市熱島效應：極端氣候下的人道建築與城市韌性"
    },
    "situation": "高二地理建築研究小組的 Ryan 和 Claire 站在市中心天橋上，用紅外線熱成像儀測量柏油路面與綠地溫差。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Claire": { "role": "Claire", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0708.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "Claire, look at the thermal infrared reading. The sun-baked asphalt over there exceeds fifty-two degrees Celsius, whereas the park lawn is ten degrees cooler.", "zh": "Claire，看看紅外線熱像儀的數值。那邊曝曬的柏油路面溫度居然飆破了攝氏五十二度，而公園草皮卻整整低了十度。", "keywords": ["thermal infrared", "asphalt", "degrees Celsius"] },
      { "id": 2, "speaker": "Claire", "avatar": "👩‍🎓", "en": "That is the Urban Heat Island effect in stark reality. Concrete canyons trap solar radiation while vehicular exhaust and air conditioner compressors spew anthropogenic heat.", "zh": "這正是都市熱島效應最赤裸殘酷的現實。鋼筋水泥大樓形成的都會峽谷困住太陽輻射，而車輛廢氣與冷氣壓縮機又持續噴吐人為廢熱。", "keywords": ["Heat Island", "anthropogenic", "canyons"] },
      { "id": 3, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "This is not merely an inconvenience; extreme prolonged heat waves pose severe cardiovascular health hazards, disproportionately impacting elderly and lower-income residents.", "zh": "這絕不僅僅是不舒服而已；極端持續的熱浪會引發嚴重的心血管健康危機，並對長者與弱勢基層居民造成不成比例的致命衝擊。", "keywords": ["cardiovascular", "disproportionately", "hazards"] },
      { "id": 4, "speaker": "Claire", "avatar": "👩‍🎓", "en": "Urban planners must transition toward climate-resilient architecture: mandate green rooftop gardens, permeable pavements, and urban wind corridors.", "zh": "都市規劃者必須加速向具氣候韌性的綠建築轉型：強制推行綠色屋頂花園、透水鋪面以及打通城市導風廊道。", "keywords": ["climate-resilient", "permeable", "corridors"] },
      { "id": 5, "speaker": "Ryan", "avatar": "👨‍🎓", "en": "Reflective 'cool roofs' coated with titanium dioxide paint can reflect up to eighty percent of sunlight back into outer space.", "zh": "塗有二氧化鈦塗層的反射型『冷屋頂』，甚至能把高達百分之八十的日照熱量直接反射回外太空。", "keywords": ["titanium dioxide", "cool roofs", "reflect"] },
      { "id": 6, "speaker": "Claire", "avatar": "👩‍🎓", "en": "Re-integrating nature into metropolis infrastructure is our only viable safeguard against an increasingly scorching Anthropocene.", "zh": "將大自然生態重新縫合進現代大都會的基礎建設中，是我們抵抗日益灼熱的人類世環境唯一可行的自救屏障。", "keywords": ["Anthropocene", "safeguard", "metropolis"] }
    ],
    "vocabulary": [
      { "word": "anthropogenic", "phonetic": "/ˌæn.θrə.pəˈdʒen.ɪk/", "pos": "adj.", "zh": "由人類活動引起的、人為的", "example": "Scientists documented anthropogenic emissions driving global heating." },
      { "word": "permeable", "phonetic": "/ˈpɝː.mi.ə.bəl/", "pos": "adj.", "zh": "可滲透的、透水的", "example": "Permeable brick sidewalks allow rainwater to recharge the soil." },
      { "word": "Anthropocene", "phonetic": "/ˈæn.θrə.pəˌsiːn/", "pos": "n.", "zh": "人類世（地質年代新名詞）", "example": "Human dominance over planetary cycles defines the Anthropocene epoch." }
    ],
    "dailyPhrase": { "en": "In stark reality.", "zh": "殘酷的現實、歷歷在目的真相。" },
    "cultureTip": "都市熱島效應（Urban Heat Island Effect）造成市中心氣溫顯著高於郊區。現代永續都市設計倡導建立「風廊（wind corridors）」、推廣「透水鋪面（permeable pavements）」與「綠屋頂（green roofs）」，減緩極端高溫衝擊。"
  },

  # 07-09 [國小初階]
  {
    "id": "dialogue-0709",
    "date": "07-09",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "海灘假期",
    "topic": {
      "en": "Building Sandcastles at the Beach: Seashells & Moats",
      "zh": "到海灘堆沙堡：貝殼裝飾與挖防波護城河"
    },
    "situation": "週末的海邊沙灘上，Ben 和 Ruby 拿著黃色塑膠小鏟子和紅水桶，興高采烈地築起一座堅固的沙堡。",
    "speakers": {
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Ruby": { "role": "Ruby", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0709.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ben", "avatar": "👦", "en": "Ruby, pack the damp sand tightly into this castle-shaped plastic bucket!", "zh": "Ruby，把濕潤的沙子緊緊壓進這個城堡形狀的塑膠桶裡！", "keywords": ["damp sand", "tightly", "bucket"] },
      { "id": 2, "speaker": "Ruby", "avatar": "👧", "en": "Flip it upside down... one, two, tap tap! Wow, look at the four sturdy towers!", "zh": "把它倒扣過來……一、二，輕輕敲兩下！哇，你看那四座結實挺立的塔樓！", "keywords": ["upside down", "sturdy", "towers"] },
      { "id": 3, "speaker": "Ben", "avatar": "👦", "en": "I am digging a deep moat around the walls using my yellow shovel to block approaching waves.", "zh": "我正用黃色小鏟子在城牆周圍挖一條深深的護城河，用來阻擋衝上來的小海浪。", "keywords": ["moat", "shovel", "approaching waves"] },
      { "id": 4, "speaker": "Ruby", "avatar": "👧", "en": "I collected shiny spiral seashells and white coral fragments to decorate the castle gates.", "zh": "我撿了許多閃亮的螺旋小貝殼和白色珊瑚碎石，用來裝飾城堡的大門口。", "keywords": ["seashells", "coral", "gates"] },
      { "id": 5, "speaker": "Ben", "avatar": "👦", "en": "Our majestic sand palace is complete! Building things with our own hands on the beach is magical.", "zh": "我們雄偉的沙灘宮殿大功告成啦！親手在海灘上建造城堡的感覺真神奇。", "keywords": ["majestic", "palace", "magical"] }
    ],
    "vocabulary": [
      { "word": "moat", "phonetic": "/moʊt/", "pos": "n.", "zh": "護城河、城壕", "example": "The medieval fortress was guarded by a deep water moat." },
      { "word": "seashell", "phonetic": "/ˈsiː.ʃel/", "pos": "n.", "zh": "貝殼、海貝", "example": "Children combed the shoreline for colorful seashells." },
      { "word": "majestic", "phonetic": "/məˈdʒes.tɪk/", "pos": "adj.", "zh": "雄偉的、莊嚴壯觀的", "example": "The cruise ship glided past majestic snow-capped peaks." }
    ],
    "dailyPhrase": { "en": "Flip it upside down.", "zh": "把它上下倒扣翻轉過來。" },
    "cultureTip": "堆沙堡（Sandcastle building）是全球海灘文化的經典童年體驗。利用略帶水分的濕沙（damp sand）才能靠水分子表面張力黏合出堅固的塔樓（towers）與護城河（moats）。"
  },

  # 07-10 [國小中高]
  {
    "id": "dialogue-0710",
    "date": "07-10",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "健康防護",
    "topic": {
      "en": "Preventing Heatstroke: Hydration and Electrolytes in Summer",
      "zh": "夏日防中暑大作戰：補充電解質與高溫戶外安全守則"
    },
    "situation": "夏令營操場活動中場休息，隊輔志工 Daniel 正在提醒隊員 Emily 正確補充足量水分與電解質，預防熱衰竭。",
    "speakers": {
      "Daniel": { "role": "Daniel", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emily": { "role": "Emily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0710.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Daniel", "avatar": "👦", "en": "Emily, drink some water immediately! Your cheeks are flushed bright red and you are sweating profusely.", "zh": "Emily，快喝點水！你的雙頰曬得通紅，而且汗流浹背呢。", "keywords": ["flushed", "sweating", "profusely"] },
      { "id": 2, "speaker": "Emily", "avatar": "👧", "en": "Phew, running in the midday sun really drained my stamina. My mouth feels as dry as a desert.", "zh": "呼，頂著正午烈日奔跑真的把我的體力榨乾了。我的嘴巴乾得像沙漠一樣。", "keywords": ["drained", "stamina", "desert"] },
      { "id": 3, "speaker": "Daniel", "avatar": "👦", "en": "Don't chug plain water too rapidly. When we sweat heavily, our bodies lose vital minerals and sodium.", "zh": "不要一口氣大口猛灌白開水。當我們大量流汗時，身體同時流失了關鍵的礦物質與鈉離子。", "keywords": ["chug", "sodium", "minerals"] },
      { "id": 4, "speaker": "Emily", "avatar": "👧", "en": "Right. Drinking an electrolyte sports beverage diluted with cold water restores cellular balance faster.", "zh": "對的。喝加水稀釋的電解質運動飲料，能更快速恢復細胞的體液平衡。", "keywords": ["electrolyte", "diluted", "cellular balance"] },
      { "id": 5, "speaker": "Daniel", "avatar": "👦", "en": "Let's rest in this air-conditioned shade for fifteen minutes. Never ignore early warning signals of heat exhaustion.", "zh": "我們在這個有遮蔭通風的地方休息十五分鐘吧。絕對不能輕忽熱衰竭與中暑的早期預警信號。", "keywords": ["heat exhaustion", "signals", "shade"] }
    ],
    "vocabulary": [
      { "word": "profusely", "phonetic": "/prəˈfjuːs.li/", "pos": "adv.", "zh": "大量地、大汗淋漓地", "example": "The marathoner was sweating profusely near the finish." },
      { "word": "chug", "phonetic": "/tʃʌɡ/", "pos": "v.", "zh": "大口咕咚猛灌（液體）", "example": "He chugged a tall glass of iced tea after gym class." },
      { "word": "electrolyte", "phonetic": "/iˈlek.trə.laɪt/", "pos": "n.", "zh": "電解質", "example": "Electrolyte solutions help treat dehydration during fever." }
    ],
    "dailyPhrase": { "en": "Listen to one's body.", "zh": "傾聽身體發出的警訊信號。" },
    "cultureTip": "大量出汗時如果只狂灌純水，容易引發「水中毒（低血鈉症 Hyponatremia）」。運動醫學建議以「少量多次（sip slowly）」方式補充含有鈉、鉀的電解質水（electrolyte drink），並移至蔭涼處（cool shade）散熱。"
  },

  # 07-11 [高中進階]
  {
    "id": "dialogue-0711",
    "date": "07-11",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "全球人口",
    "topic": {
      "en": "World Population Day: Global Aging & Future Labor Dynamics",
      "zh": "世界人口日：全球超高齡社會、少子化與未來勞動力結構思辨"
    },
    "situation": "7月11日世界人口日，公民經濟論壇上，高中生 Jason 和 Maya 就東亞少子化現象與養老金體系展開思辨。",
    "speakers": {
      "Jason": { "role": "Jason", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Maya": { "role": "Maya", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0711.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Jason", "avatar": "👨‍🎓", "en": "Maya, today is United Nations World Population Day. While global population surpassed eight billion, fertility rates across East Asia have plummeted drastically.", "zh": "Maya，今天是聯合國世界人口日。儘管全球總人口已突破八十億大關，但東亞各國的生育率卻面臨斷崖式驟跌。", "keywords": ["World Population Day", "plummeted", "fertility rates"] },
      { "id": 2, "speaker": "Maya", "avatar": "👩‍🎓", "en": "Our society is transitioning into a 'super-aged' demographic where over twenty percent of citizens are senior citizens aged sixty-five or above.", "zh": "我們的社會正迅速步入『超高齡社會』結構：六十五歲以上的長者人口佔比正式突破總人口的百分之二十。", "keywords": ["super-aged", "demographic", "transitioning"] },
      { "id": 3, "speaker": "Jason", "avatar": "👨‍🎓", "en": "The economic ripple effects are monumental—a shrinking working-age demographic strains public healthcare budgets and destabilizes pension solvency.", "zh": "這所引發的經濟骨牌效應是巨大的——勞動年齡人口萎縮，將嚴重吃緊公共健保預算，並衝擊勞退年金體系的財務永續平衡。", "keywords": ["pension solvency", "ripple effects", "destabilizes"] },
      { "id": 4, "speaker": "Maya", "avatar": "👩‍🎓", "en": "Merely offering superficial cash subsidies fails to reverse the trend when prohibitive housing costs and intense career pressures dissuade young adults from starting families.", "zh": "當高昂房價與高壓職場文化讓年輕世代對成家卻步時，單純發放一次性生育補貼顯然難以逆轉趨勢。", "keywords": ["dissuade", "subsidies", "prohibitive"] },
      { "id": 5, "speaker": "Jason", "avatar": "👨‍🎓", "en": "Robotics automation and generative AI may bridge labor gaps in manufacturing and eldercare, but systemic institutional adaptation remains urgent.", "zh": "機器人自動化與生成式 AI 或許能填補製造業與照護領域的勞動力缺口，但體制層面的全方位變革依舊迫在眉睫。", "keywords": ["automation", "eldercare", "systemic"] },
      { "id": 6, "speaker": "Maya", "avatar": "👩‍🎓", "en": "Reimagining retirement not as passive obsolescence, but as active lifelong engagement, will reshape social cohesion for generations ahead.", "zh": "重新定義退休生活：不再將其視為被動的退出舞台，而是作為積極的終身社會參與，將重塑未來世代的凝聚力。", "keywords": ["obsolescence", "cohesion", "engagement"] }
    ],
    "vocabulary": [
      { "word": "plummet", "phonetic": "/ˈplʌm.ɪt/", "pos": "v.", "zh": "暴跌、急劇墜落", "example": "Birth rates plummeted to historic lows during the recession." },
      { "word": "prohibitive", "phonetic": "/proʊˈhɪb.ə.t̬ɪv/", "pos": "adj.", "zh": "令人望而卻步的、過於高昂的（價格）", "example": "The prohibitive cost of housing discourages young buyers." },
      { "word": "obsolescence", "phonetic": "/ˌɑːb.səˈles.əns/", "pos": "n.", "zh": "過時、陳舊淘汰", "example": "Technological advancements accelerate product obsolescence." }
    ],
    "dailyPhrase": { "en": "Ripple effect.", "zh": "連鎖反應、骨牌效應。" },
    "cultureTip": "7月11日是聯合國「世界人口日（World Population Day）」。台灣預計於 2025~2026 年邁入「超高齡社會（Super-aged society）」，人口學家呼籲推動銀髮勞動力活化（Active Aging）與友善托育環境。"
  },

  # 07-12 [國中挑戰]
  {
    "id": "dialogue-0712",
    "date": "07-12",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "高山露營",
    "topic": {
      "en": "Alpine Camping Experience: Pitching Tents & Milky Way Gazing",
      "zh": "高山露營初體驗：搭設雙人帳篷與仰望無光害銀河"
    },
    "situation": "週末在合歡山高海拔露營區，Dylan 和 Chloe 跟隨戶外社團在星空下搭好帳篷，抬頭仰望燦爛的夏季銀河。",
    "speakers": {
      "Dylan": { "role": "Dylan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0712.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Dylan", "avatar": "👦", "en": "Chloe, hammer those aluminum tent pegs deeply into the turf at a forty-five-degree angle against the mountain wind.", "zh": "Chloe，把那些鋁合金營釘以四十五度角深深敲進草皮裡，這樣才能抵禦強勁的高山陣風。", "keywords": ["aluminum", "tent pegs", "mountain wind"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "I secured the rainfly tautly. The elevation here is over two thousand meters, so the night air feels chilly!", "zh": "我把外帳防雨布拉得緊繃牢固了。這裡海拔超過兩千公尺，夜裡的空氣真冷颼颼呀！", "keywords": ["rainfly", "elevation", "chilly"] },
      { "id": 3, "speaker": "Dylan", "avatar": "👦", "en": "Turn off your headlamp and let our eyes adapt to complete darkness for five minutes.", "zh": "關掉你的頭燈，讓我們的眼睛在完全的黑暗中適應五分鐘。", "keywords": ["headlamp", "adapt", "darkness"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "Oh, wow! Look straight up! A luminous, misty river of billions of stars is spanning across the entire zenith!", "zh": "天啊，哇！直接往頭頂看！一條由億萬顆恆星組成的璀璨銀白光霧長河，橫跨在整個夜空天頂中央！", "keywords": ["zenith", "luminous", "Milky Way"] },
      { "id": 5, "speaker": "Dylan", "avatar": "👦", "en": "That is the core of our Milky Way galaxy! In the city, heavy light pollution washes out all these celestial wonders.", "zh": "那就是我們銀河系的璀璨核心！在都市裡，嚴重的光害把所有這些宇宙奇觀全都抹煞遮蔽了。", "keywords": ["Milky Way", "light pollution", "celestial"] },
      { "id": 6, "speaker": "Chloe", "avatar": "👧", "en": "Under this infinite starry canopy, you truly grasp how vast the universe is and how humble we humans are.", "zh": "在浩瀚無垠的星空穹頂之下，你才能真正深刻體會到宇宙有多麼宏大，而我們人類又是多麼謙卑渺小。", "keywords": ["canopy", "humble", "infinite"] }
    ],
    "vocabulary": [
      { "word": "zenith", "phonetic": "/ˈzen.ɪθ/", "pos": "n.", "zh": "天頂、頂點、最高點", "example": "The summer sun reached its zenith directly overhead at noon." },
      { "word": "luminous", "phonetic": "/ˈluː.mə.nəs/", "pos": "adj.", "zh": "發光的、夜光的、燦爛明亮的", "example": "Luminous watch hands glowed green in the dark tent." },
      { "word": "canopy", "phonetic": "/ˈkæn.ə.pi/", "pos": "n.", "zh": "天穹、樹冠層、華蓋", "example": "We slept under an expansive starry canopy of clear alpine sky." }
    ],
    "dailyPhrase": { "en": "Wash out.", "zh": "沖刷掉、掩蓋使失色淡化。" },
    "cultureTip": "合歡山暗空公園（Hehuan Mountain Dark Sky Park）是國際認證的無光害觀星勝地。夏季是觀賞銀河核心（Milky Way Galaxy Core）的最佳時機，壯麗的人馬座與天蠍座橫跨天頂（zenith）。"
  },

  # 07-13 [國小初階]
  {
    "id": "dialogue-0713",
    "date": "07-13",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "春日野餐",
    "topic": {
      "en": "Picnic in the Shade: Chilled Mango Slices & Croissants",
      "zh": "大樹蔭下的野餐：冰鎮芒果切片與香脆可頌麵包"
    },
    "situation": "週日下午，Lucas 和 Lily 在植物園的大樟樹下鋪開紅白格子野餐墊，享用媽媽準備的冰涼芒果和金黃可頌。",
    "speakers": {
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Lily": { "role": "Lily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0713.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lucas", "avatar": "👦", "en": "Lily, spread the red-and-white checkered picnic blanket flat under this giant camphor tree.", "zh": "Lily，把這張紅白格子的野餐墊在這棵大樟樹下鋪平坦吧。", "keywords": ["checkered", "picnic blanket", "camphor tree"] },
      { "id": 2, "speaker": "Lily", "avatar": "👧", "en": "The thick green tree canopy blocks out all harsh sun rays. It feels nice and cool here.", "zh": "茂密翠綠的樹冠把所有刺眼的陽光都擋住了。這裡感覺又涼爽又舒服。", "keywords": ["canopy", "harsh", "cool"] },
      { "id": 3, "speaker": "Lucas", "avatar": "👦", "en": "Open our cooler bag! I packed cold Irwin mango cubes in a glass container.", "zh": "打開我們的保冷袋！我把切成方塊的冰愛文芒果裝在玻璃保鮮盒裡呢。", "keywords": ["cooler bag", "mango cubes", "container"] },
      { "id": 4, "speaker": "Lily", "avatar": "👧", "en": "The mango is so sweet and juicy! Take a buttery croissant; they are still flaky and warm.", "zh": "這芒果太甜太爆汁了！拿一個奶油可頌吧，外皮依然金黃酥脆而且微溫呢。", "keywords": ["flaky", "croissant", "buttery"] },
      { "id": 5, "speaker": "Lucas", "avatar": "👦", "en": "Eating good food with pleasant bird songs above our heads makes summer vacation pure magic.", "zh": "頭頂上有悅耳鳥鳴陪伴，一邊享用美味點心，讓暑假變得像童話一樣美妙。", "keywords": ["bird songs", "magic", "summer vacation"] }
    ],
    "vocabulary": [
      { "word": "checkered", "phonetic": "/ˈtʃek.ɚd/", "pos": "adj.", "zh": "方格圖案的、棋盤格的", "example": "She bought a vintage checkered tablecloth for outdoor dining." },
      { "word": "croissant", "phonetic": "/krwɑːˈsɑːŋ/", "pos": "n.", "zh": "可頌、牛角麵包", "example": "A freshly baked croissant should be crisp outside and airy inside." },
      { "word": "flaky", "phonetic": "/ˈfleɪ.ki/", "pos": "adj.", "zh": "酥脆的、層層起酥的", "example": "The French pastry crust was exceptionally buttery and flaky." }
    ],
    "dailyPhrase": { "en": "Block out...", "zh": "阻擋、遮蔽（陽光或噪音）。" },
    "cultureTip": "夏日野餐（Summer Picnic）講求選在有大樹遮蔽的陰涼處（in the shade）。使用保冷袋（cooler bag）保持當季切塊水果的低溫新鮮，是戶外用餐的安全美味秘訣。"
  },

  # 07-14 [國小中高]
  {
    "id": "dialogue-0714",
    "date": "07-14",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "天文科普",
    "topic": {
      "en": "Scorpius and Antares: The Fiery Red Giant of the Summer Sky",
      "zh": "夏夜星空之王：認識天蠍座的心宿二大火星"
    },
    "situation": "夏夜晴朗無雲，Sam 和 Olivia 在校園天文台的屋頂平台上，拿著星圖認辨南方的天蠍座與紅巨星心宿二。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0714.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Olivia, look low toward the southern horizon! Do you see that dramatic curved hook of bright stars?", "zh": "Olivia，往南方低空的地平線看！你有看到那串排列成醒目大彎鉤的明亮星星嗎？", "keywords": ["southern horizon", "curved hook", "stars"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👧", "en": "Yes! That is Scorpius, the magnificent celestial scorpion of the summer night sky!", "zh": "看到了！那就是天蠍座，夏夜星空中最霸氣雄偉的宇宙巨蠍！", "keywords": ["Scorpius", "celestial", "scorpion"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Look right at the scorpion's heart—there is a prominent star glowing with a fierce reddish-orange hue.", "zh": "看那隻蠍子的心臟位置——有一顆顯眼的恆星正散發著炙熱的橙紅色光芒呢。", "keywords": ["heart", "reddish-orange", "prominent"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👧", "en": "That is Antares, an enormous red supergiant star over seven hundred times larger than our Sun!", "zh": "那就是『心宿二（Antares）』，一顆體積比我們的太陽還要巨大七百倍以上的超巨星！", "keywords": ["Antares", "supergiant", "Sun"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Ancient Chinese astronomers called it the 'Fire Star' because its brilliant redness warned of midsummer heat.", "zh": "中國古代天文學家稱它為『大火星』，因為它璀璨奪目的紅光提醒著人們盛夏嚴熱已至。", "keywords": ["Fire Star", "astronomers", "midsummer"] }
    ],
    "vocabulary": [
      { "word": "prominent", "phonetic": "/ˈprɑː.mə.nənt/", "pos": "adj.", "zh": "顯眼的、突出的、著名的", "example": "The prominent church spire was visible for miles around." },
      { "word": "supergiant", "phonetic": "/ˌsuː.pɚˈdʒaɪ.ənt/", "pos": "n.", "zh": "超巨星（天文學名詞）", "example": "Antares and Betelgeuse are celebrated red supergiants." },
      { "word": "horizon", "phonetic": "/həˈraɪ.zən/", "pos": "n.", "zh": "地平線、視野", "example": "The sun dipped below the ocean horizon at dusk." }
    ],
    "dailyPhrase": { "en": "Warn of...", "zh": "預警……的到來、提醒留意……。" },
    "cultureTip": "天蠍座（Scorpius）是夏季夜空最壯麗的星座。其心臟處的「心宿二（Antares，古希臘語意為『火星的對手』）」在中國古代稱為「大火」，《詩經》名句「七月流火」指的正是盛夏農曆七月大火星西沉、天氣將轉涼的景象。"
  },

  # 07-15 [高中進階]
  {
    "id": "dialogue-0715",
    "date": "07-15",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "青年賦權",
    "topic": {
      "en": "World Youth Skills Day: Irreplaceable Human Skills in the AI Era",
      "zh": "世界青年技能日：AI 浪潮下不可替代的人性軟實力與創造力"
    },
    "situation": "7月15日世界青年技能日，國際青年就業線上論壇上，高中生 Victor 和 Irene 分享科技時代青年應具備的核心競爭力。",
    "speakers": {
      "Victor": { "role": "Victor", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Irene": { "role": "Irene", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0715.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Victor", "avatar": "👨‍🎓", "en": "Irene, on this World Youth Skills Day, generative AI models can synthesize code, draft essays, and analyze balance sheets in seconds.", "zh": "Irene，在世界青年技能日的今天，生成式 AI 已經能在幾秒鐘內編寫程式碼、撰寫論文，甚至分析企業資產負債表。", "keywords": ["World Youth Skills Day", "synthesize", "generative AI"] },
      { "id": 2, "speaker": "Irene", "avatar": "👩‍🎓", "en": "That automated efficiency creates acute anxiety among students. If repetitive technical tasks are automated, what constitutes durable human competence?", "zh": "那種自動化的高效確實引發了廣大青年學子的焦慮。如果重複性的技術任務被機器取代，究竟什麼才是經久不衰的人類核心競爭力？", "keywords": ["automated", "competence", "repetitive"] },
      { "id": 3, "speaker": "Victor", "avatar": "👨‍🎓", "en": "The World Economic Forum highlights critical thinking, complex collaborative negotiation, and ethical judgment as uniquely human faculties.", "zh": "世界經濟論壇特別指出：批判性思維、複雜跨界協商以及道德倫理判斷力，是唯有人類才具備的獨特心智能力。", "keywords": ["collaborative", "ethical judgment", "faculties"] },
      { "id": 4, "speaker": "Irene", "avatar": "👩‍🎓", "en": "AI mimics existing patterns; it cannot generate radical empathetic curiosity or navigate moral dilemmas where all choices carry painful trade-offs.", "zh": "AI 只是在模仿既有的大數據模式；它無法產生富有同理心的人文好奇，也無法在面臨兩難抉擇時體會道德權衡的痛苦深度。", "keywords": ["moral dilemmas", "trade-offs", "empathetic"] },
      { "id": 5, "speaker": "Victor", "avatar": "👨‍🎓", "en": "Youth must cultivate a 'T-shaped' skill profile: deep domain expertise coupled with broad adaptability across interdisciplinary boundaries.", "zh": "青年必須培養『T型人才』的技能輪廓：深耕某一特定專業領域，同時具備跨學科邊界的廣闊適應力。", "keywords": ["T-shaped", "interdisciplinary", "adaptability"] },
      { "id": 6, "speaker": "Irene", "avatar": "👩‍🎓", "en": "Instead of racing against machines, our mission is to wield technology as an amplifier of our fundamental humanity and creativity.", "zh": "與其試圖與機器賽跑，我們新世代的使命應當是把科技化為放大鏡，放大我們最根本的人性溫度與非凡創造力。", "keywords": ["amplifier", "humanity", "creativity"] }
    ],
    "vocabulary": [
      { "word": "competence", "phonetic": "/ˈkɑːm.pə.t̬əns/", "pos": "n.", "zh": "勝任能力、核心競爭力", "example": "Linguistic competence enables seamless cross-cultural diplomacy." },
      { "word": "interdisciplinary", "phonetic": "/ˌɪn.t̬ɚˈdɪs.ə.plɪ.ner.i/", "pos": "adj.", "zh": "跨學科的、跨領域的", "example": "Bioinformatics is a vibrant interdisciplinary research field." },
      { "word": "amplifier", "phonetic": "/ˈæm.plə.faɪ.ɚ/", "pos": "n.", "zh": "放大器、擴大器", "example": "Education acts as a powerful amplifier of personal potential." }
    ],
    "dailyPhrase": { "en": "Race against machines.", "zh": "與機器競爭（引申為在自動化浪潮中尋找人類獨特價值）。" },
    "cultureTip": "7月15日是聯合國「世界青年技能日（World Youth Skills Day）」。在人工智慧快速發展的當下，倡導發展「T-shaped skills（T型技能）」：垂直具備深厚專業底蘊，水平具備同理心、跨域合作與思辨判斷的軟實力。"
  },

  # 07-16 [國小初階]
  {
    "id": "dialogue-0716",
    "date": "07-16",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "水族奇觀",
    "topic": {
      "en": "Aquarium Ocean Tunnel: Manta Rays and Gliding Sea Turtles",
      "zh": "逛水族館海底隧道：近距離看魔鬼魚與海龜滑行"
    },
    "situation": "夏令營參觀國立海洋生物博物館，Tyler 和 Amy 站在透明壓克力海底隧道內，仰望巨型魟魚從頭頂悠然掠過。",
    "speakers": {
      "Tyler": { "role": "Tyler", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Amy": { "role": "Amy", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0716.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tyler", "avatar": "👦", "en": "Amy, look straight above our heads through this curved glass tunnel! An enormous creature is gliding over us!", "zh": "Amy，透過這條弧形玻璃隧道往我們正頭頂上看！一隻巨大的生物正在我們頭頂滑翔過去呢！", "keywords": ["tunnel", "gliding", "creature"] },
      { "id": 2, "speaker": "Amy", "avatar": "👧", "en": "Wow, that is a giant manta ray! Its wide fins flap slowly like underwater bird wings.", "zh": "哇，那是一隻巨大的魔鬼氈魟魚！它寬大的胸鰭慢慢拍動，就像在水下飛翔的鳥類翅膀一樣。", "keywords": ["manta ray", "fins", "underwater"] },
      { "id": 3, "speaker": "Tyler", "avatar": "👦", "en": "And look to your left! A gentle green sea turtle is paddling gracefully beside the coral reef.", "zh": "再看你的左邊！一隻溫柔的綠蠵龜正優雅地在珊瑚礁旁撥水前進呢。", "keywords": ["sea turtle", "coral reef", "paddling"] },
      { "id": 4, "speaker": "Amy", "avatar": "👧", "en": "Being surrounded on all sides by shimmering blue water feels like scuba diving without getting wet.", "zh": "被閃閃發光的碧藍海水全方位包圍，感覺就像沒有弄濕衣服就潛進了深海一樣。", "keywords": ["shimmering", "scuba diving", "wet"] },
      { "id": 5, "speaker": "Tyler", "avatar": "👦", "en": "Let's snap a picture together with the smiling manta ray in the background!", "zh": "我們跟背景裡那隻看似在微笑的魟魚一起拍張合照紀念吧！", "keywords": ["snap a picture", "smiling", "manta ray"] }
    ],
    "vocabulary": [
      { "word": "manta ray", "phonetic": "/ˈmæn.tə reɪ/", "pos": "n.", "zh": "鬼蝠魟、魔鬼魚", "example": "Manta rays filter plankton peacefully in tropical waters." },
      { "word": "shimmering", "phonetic": "/ˈʃɪm.ɚ.ɪŋ/", "pos": "adj.", "zh": "閃爍的、波光粼粼的", "example": "Sunlight danced on the shimmering surface of the bay." },
      { "word": "fin", "phonetic": "/fɪn/", "pos": "n.", "zh": "鰭、魚鰭", "example": "The shark's dorsal fin sliced through the calm water." }
    ],
    "dailyPhrase": { "en": "Snap a picture.", "zh": "拍張照、拍張相片留念。" },
    "cultureTip": "水族館海底隧道（Aquarium Ocean Tunnel）採用高強度厚層壓克力玻璃（acrylic glass）。走在隧道中觀察鬼蝠魟（Manta Ray）與海龜滑行，能建立孩子對海洋生態的珍視與熱愛。"
  },

  # 07-17 [國中挑戰]
  {
    "id": "dialogue-0717",
    "date": "07-17",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "志工服務",
    "topic": {
      "en": "Youth Volunteering: Sorting Surplus Food at the Food Bank",
      "zh": "青年志工體驗：在社區食物銀行整理愛心惜食物資"
    },
    "situation": "暑期志工服務日，David 和 Chloe 在非營利食物銀行倉庫戴著棉手套，分類超市捐贈的蔬菜與罐頭食品。",
    "speakers": {
      "David": { "role": "David", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0717.mp3",
    "dialogue": [
      { "id": 1, "speaker": "David", "avatar": "👦", "en": "Chloe, check the expiration dates on these canned black beans and whole-grain oats before boxing them.", "zh": "Chloe，在把這些黑豆罐頭和全麥燕麥裝箱前，先仔細核對一下有效保存期限喔。", "keywords": ["expiration dates", "canned", "boxing"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👧", "en": "Will do. It is staggering to learn that over thirty percent of edible food is discarded globally while millions experience hunger.", "zh": "好的。得知全球有超過三成的可食用糧食被白白浪費丟棄，而同時卻有數百萬人面臨飢餓，真令人震驚。", "keywords": ["edible", "discarded", "staggering"] },
      { "id": 3, "speaker": "David", "avatar": "👦", "en": "Food banks rescue perfectly fresh produce with slight cosmetic blemishes that grocery stores reject.", "zh": "食物銀行及時搶救了許多只因外觀稍有微小瑕疵、而被一般超市下架淘汰的優質新鮮蔬果。", "keywords": ["cosmetic", "blemishes", "produce"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👧", "en": "We packed forty family relief hampers this morning containing rice, milk powder, cooking oil, and fresh carrots.", "zh": "我們今天上午已經打包好了四十份家庭救助物資箱，裡面有白米、奶粉、食用油以及新鮮紅蘿蔔。", "keywords": ["hampers", "relief", "family"] },
      { "id": 5, "speaker": "David", "avatar": "👦", "en": "Sweating during summer volunteer work feels infinitely more rewarding than lounging aimlessly on the couch.", "zh": "在夏天當志工揮灑汗水，感覺比無所事事癱在沙發上要有意義、有成就感幾萬倍。", "keywords": ["rewarding", "volunteer", "aimlessly"] },
      { "id": 6, "speaker": "Chloe", "avatar": "👧", "en": "Small compassionate gestures weave a stronger social safety net for vulnerable families in our neighborhood.", "zh": "微小而溫暖的善行，能為我們社區裡的弱勢弱勢家庭編織出一張更堅實溫暖的社會安全網。", "keywords": ["compassionate", "safety net", "vulnerable"] }
    ],
    "vocabulary": [
      { "word": "blemish", "phonetic": "/ˈblem.ɪʃ/", "pos": "n.", "zh": "外觀瑕疵、斑點、小缺陷", "example": "Ugly produce with slight surface blemishes is equally nutritious." },
      { "word": "hamper", "phonetic": "/ˈhæm.pɚ/", "pos": "n.", "zh": "大禮物籃、物資箱", "example": "Volunteers delivered food hampers to homebound seniors." },
      { "word": "compassionate", "phonetic": "/kəmˈpæʃ.ən.ət/", "pos": "adj.", "zh": "富有同情心的、慈悲關懷的", "example": "The social worker provided compassionate counsel to the family." }
    ],
    "dailyPhrase": { "en": "Social safety net.", "zh": "社會安全網。" },
    "cultureTip": "食物銀行（Food Bank）推動「食物零浪費（Zero food waste）」，搶救因外表不完美（ugly produce / cosmetic blemishes）但品質無虞的食材轉贈弱勢。青年參與志工服務（Community volunteering）是英美與台灣高中大學申請極重視的公共素養。"
  },

  # 07-18 [國小中高]
  {
    "id": "dialogue-0718",
    "date": "07-18",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "盛夏美食",
    "topic": {
      "en": "Homemade Mango Shaved Ice: Drizzling Sweet Condensed Milk",
      "zh": "自己動手做香甜芒果雪花冰：淋上香濃煉乳與自製黑糖水"
    },
    "situation": "星期天下午，Eric 和 Mia 拿出家裡的電動刨冰機，親手做一碗台式芒果雪花冰招待來訪的朋友。",
    "speakers": {
      "Eric": { "role": "Eric", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0718.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Eric", "avatar": "👦", "en": "Mia, turn on the electric ice shaver! Fine, fluffy snowflakes are cascading into the wide ceramic bowl!", "zh": "Mia，打開電動刨冰機！細緻綿密的雪白刨冰就像瀑布一樣紛紛落進寬口大瓷碗裡了！", "keywords": ["ice shaver", "snowflakes", "cascading"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "Now let's generously pile these chilled golden mango cubes all over the snowy shaved ice mountain.", "zh": "現在我們把這些冰涼的金黃芒果大丁，豪邁地鋪滿整座雪白刨冰山周圍吧。", "keywords": ["generously", "mango cubes", "mountain"] },
      { "id": 3, "speaker": "Eric", "avatar": "👦", "en": "Spoon a giant scoop of creamy vanilla ice cream right onto the snowy peak.", "zh": "在雪山頂端端正放上一大球香濃細緻的香草冰淇淋。", "keywords": ["scoop", "vanilla", "snowy peak"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "And the ultimate finishing touch: drizzle a generous swirl of sweet condensed milk all over!", "zh": "還有最後的終極靈魂點綴：在整座冰山淋上一圈圈香濃甜美的煉乳！", "keywords": ["drizzle", "condensed milk", "finishing touch"] },
      { "id": 5, "speaker": "Eric", "avatar": "👦", "en": "Take a big spoonful! The icy crunch melting with rich tropical sweetness is pure paradise!", "zh": "大口挖一勺送進嘴裡！冰涼爽脆的刨冰搭配濃郁的熱帶果香在舌尖融化，簡直就是人間天堂！", "keywords": ["spoonful", "tropical", "paradise"] }
    ],
    "vocabulary": [
      { "word": "cascade", "phonetic": "/kæsˈkeɪd/", "pos": "v./n.", "zh": "瀑布似地落下、傾瀉", "example": "Shaved ice cascaded smoothly into the waiting glass." },
      { "word": "condensed milk", "phonetic": "/kənˌdenst ˈmɪlk/", "pos": "n.", "zh": "煉乳、濃縮牛奶", "example": "Drizzle sweet condensed milk over shaved ice desserts." },
      { "word": "paradise", "phonetic": "/ˈper.ə.daɪs/", "pos": "n.", "zh": "天堂、樂園", "example": "The secluded sandy cove was a tropical beach paradise." }
    ],
    "dailyPhrase": { "en": "Finishing touch.", "zh": "最後的畫龍點睛之筆。" },
    "cultureTip": "芒果刨冰（Mango Shaved Ice）被 CNN 評選為全球最佳甜品之一。金黃芒果塊（mango cubes）、香草冰淇淋（ice cream scoop）搭配甜煉乳（condensed milk），是台灣聞名全球的夏日美食代表作。"
  },

  # 07-19 [高中進階]
  {
    "id": "dialogue-0719",
    "date": "07-19",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "環境與地緣",
    "topic": {
      "en": "Deep-Sea Mining Dilemma: Energy Transition vs. Marine Ecosystems",
      "zh": "深海採礦爭議：綠色能源轉型金屬需求與深海生態浩劫的兩難"
    },
    "situation": "高二地球科學與國際關係社團中，Sean 和 Melody 針對國際海底管理局（ISA）開放深海錳結核開採的環境倫理展開交鋒。",
    "speakers": {
      "Sean": { "role": "Sean", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Melody": { "role": "Melody", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0719.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sean", "avatar": "👨‍🎓", "en": "Melody, the debate at the International Seabed Authority is intensifying over deep-sea mining of polymetallic nodules.", "zh": "Melody，國際海底管理局針對深海多金屬結核商業開採的辯論正在急劇白熱化。", "keywords": ["Seabed Authority", "polymetallic", "nodules"] },
      { "id": 2, "speaker": "Melody", "avatar": "👩‍🎓", "en": "Mining proponents argue these abyssal potato-sized rocks rich in cobalt, nickel, and manganese are indispensable for electric vehicle batteries and the green transition.", "zh": "開採支持者主張：這些深海深淵中富含鈷、鎳、錳等金屬如馬鈴薯般大小的結核石，是製造電動車電池與推動綠色能源轉型不可或缺的戰略原料。", "keywords": ["abyssal", "cobalt", "indispensable"] },
      { "id": 3, "speaker": "Sean", "avatar": "👨‍🎓", "en": "Yet marine biologists warn that scraping the benthic seabed four thousand meters down will destroy pristine ecosystems that took millions of years to form.", "zh": "但海洋生物學家強烈警告：刮削四千公尺深的深海底棲層，將毀滅歷經數百萬年才演化形成的原始脆弱深海生態系。", "keywords": ["benthic", "scraping", "pristine"] },
      { "id": 4, "speaker": "Melody", "avatar": "👩‍🎓", "en": "The sediment plumes stirred up by heavy dredging machinery could choke midwater filter feeders and disrupt bioluminescent communications across vast ocean expanses.", "zh": "巨型採礦重機械攪起的龐大海底沉積物濁水羽流，會窒息中層水域的濾食性生物，並阻斷廣闊海域中深海生物發光求偶通訊。", "keywords": ["sediment plumes", "bioluminescent", "dredging"] },
      { "id": 5, "speaker": "Sean", "avatar": "👨‍🎓", "en": "It presents a classic planetary paradox: destroying our ocean's deepest sanctuaries in order to decarbonize terrestrial transport.", "zh": "這呈現了一個典型的地球難題悖論：為了解救陸地交通達到脫碳目標，我們卻可能親手摧毀地球最深邃神秘的海洋庇護所。", "keywords": ["paradox", "sanctuaries", "decarbonize"] },
      { "id": 6, "speaker": "Melody", "avatar": "👩‍🎓", "en": "True sustainability cannot come from plundering new frontiers. Developing circular battery chemistry and recycling existing metals must precede irreversible deep-sea destruction.", "zh": "真正的永續絕不能建立在掠奪新邊疆的代價上。全力發展新型循環電池化學材料與既有金屬回收技術，必須優先於對深海造成不可逆的毀滅。", "keywords": ["sustainability", "plundering", "irreversible"] }
    ],
    "vocabulary": [
      { "word": "nodule", "phonetic": "/ˈnɑː.dʒuːl/", "pos": "n.", "zh": "結核、礦結石、小瘤", "example": "Polymetallic nodules resting on the abyssal plain contain rare minerals." },
      { "word": "benthic", "phonetic": "/ˈben.θɪk/", "pos": "adj.", "zh": "水底的、底棲生物的", "example": "Benthic sea cucumbers feed on organic debris drifting from above." },
      { "word": "plunder", "phonetic": "/ˈplʌn.dɚ/", "pos": "v./n.", "zh": "掠奪、瘋狂掠取資源", "example": "Commercial greed plundered ancient forests beyond recovery." }
    ],
    "dailyPhrase": { "en": "Planetary paradox.", "zh": "地球級的難題悖論。" },
    "cultureTip": "「深海採礦（Deep-Sea Mining）」是國際地緣政治與環保最受矚目的爭議。克拉里恩-克利珀頓斷裂帶（CCZ）蘊藏豐富多金屬結核，環保團體發起「暫停開採倡議（Moratorium）」，要求優先推動電池循環回收。"
  },

  # 07-20 [國中挑戰]
  {
    "id": "dialogue-0720",
    "date": "07-20",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "太空探索",
    "topic": {
      "en": "Moon Day: Apollo 11 Legacy & the Artemis Lunar Missions",
      "zh": "人類月球日：阿波羅十一號登月傳奇與重返月球的阿提米絲計畫"
    },
    "situation": "7月20日「國際月球日」，天文觀測社的 Tony 和 Clara 在校園天文鐘前討論人類登月歷史與未來的火星跳板計畫。",
    "speakers": {
      "Tony": { "role": "Tony", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Clara": { "role": "Clara", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0720.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tony", "avatar": "👦", "en": "Clara, on this day in 1969, astronaut Neil Armstrong took his historic first step onto the lunar surface!", "zh": "Clara，在 1969 年的這一天，太空人阿姆斯壯邁出了人類踏上月球表面的歷史性第一步！", "keywords": ["astronaut", "historic", "lunar surface"] },
      { "id": 2, "speaker": "Clara", "avatar": "👧", "en": "His iconic immortal words still echo through history: 'That's one small step for man, one giant leap for mankind.'", "zh": "他那句標誌性的不朽名言至今仍在歷史中迴響：『這是我個人的一小步，卻是全人類的一大步。』", "keywords": ["immortal", "giant leap", "mankind"] },
      { "id": 3, "speaker": "Tony", "avatar": "👦", "en": "Imagine operating the lunar module with computer systems having less processing power than a basic modern pocket calculator.", "zh": "想像一下：當時駕駛登月小艇的電腦運算晶片能力，甚至比現在一具最基礎的口袋型計算機還要微弱呢。", "keywords": ["lunar module", "calculator", "processing power"] },
      { "id": 4, "speaker": "Clara", "avatar": "👧", "en": "Today, NASA's Artemis program is preparing to return humans to the Moon, establishing a permanent base camp near the lunar south pole.", "zh": "而今天，NASA 的阿提米絲（Artemis）計畫正準備讓人踏重返月球，並在月球南極附近建立永久基地營。", "keywords": ["Artemis", "lunar south pole", "base camp"] },
      { "id": 5, "speaker": "Tony", "avatar": "👦", "en": "Harvesting frozen water ice trapped in permanently shadowed craters will supply drinking water and rocket propellant.", "zh": "開採深藏在月球永夜撞擊坑內的冰凍水冰，將能為太空人提供飲用水，更能分解成火箭推進燃料。", "keywords": ["craters", "propellant", "harvesting"] },
      { "id": 6, "speaker": "Clara", "avatar": "👧", "en": "The Moon will serve as humanity's cosmic stepping stone toward Mars and the deeper mysteries of our solar system.", "zh": "月球將成為全人類邁向火星深處、探索太陽系更深奧秘的宇宙跳板踏腳石。", "keywords": ["stepping stone", "solar system", "mysteries"] }
    ],
    "vocabulary": [
      { "word": "immortal", "phonetic": "/ɪˈmɔːr.t̬əl/", "pos": "adj.", "zh": "不朽的、流傳千古的", "example": "Shakespeare's plays achieved immortal cultural renown." },
      { "word": "crater", "phonetic": "/ˈkreɪ.t̬ɚ/", "pos": "n.", "zh": "隕石坑、撞擊坑、火山口", "example": "Telescopes clearly resolve jagged shadows inside lunar craters." },
      { "word": "propellant", "phonetic": "/prəˈpel.ənt/", "pos": "n.", "zh": "推進劑、火箭燃料", "example": "Liquid hydrogen and oxygen serve as high-efficiency rocket propellant." }
    ],
    "dailyPhrase": { "en": "A stepping stone toward...", "zh": "邁向……的墊腳石、前進跳板。" },
    "cultureTip": "7月20日被聯合國指定為「國際月球日（International Moon Day）」，紀念 1969 年阿波羅 11 號登月。阿提米絲計畫（Artemis program）以希臘神話中阿波羅的孿生姐姐命名，象徵新世代深空探索重啟。"
  },

  # 07-21 [國小初階]
  {
    "id": "dialogue-0721",
    "date": "07-21",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "自然參觀",
    "topic": {
      "en": "Insect Museum Tour: Giant Beetles and Camouflaged Stick Insects",
      "zh": "參觀昆蟲博物館：認識世界上最大的甲蟲與偽裝大師竹節蟲"
    },
    "situation": "夏令營參訪昆蟲生態館，Ben 和 Ruby 透過透明玻璃展示箱，驚奇地尋找隱藏在枝葉間的竹節蟲。",
    "speakers": {
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Ruby": { "role": "Ruby", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0721.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ben", "avatar": "👦", "en": "Ruby, peer closely into this terrarium! Can you spot the insect hiding among the green twigs?", "zh": "Ruby，貼近這個玻璃生態箱仔細瞧瞧！你能找出隱藏在綠色樹枝間的昆蟲嗎？", "keywords": ["terrarium", "twigs", "peer"] },
      { "id": 2, "speaker": "Ruby", "avatar": "👧", "en": "Wait... that brown twig with tiny legs is moving! It is a giant walking stick insect!", "zh": "等等……那根長著細長小腳的褐色小樹枝正在動耶！那是一隻巨大的竹節蟲！", "keywords": ["walking stick", "moving", "twig"] },
      { "id": 3, "speaker": "Ben", "avatar": "👦", "en": "Its camouflage is unbelievable! It looks one hundred percent identical to a dried tree branch.", "zh": "它的偽裝技術太不可思議了！看起來百分之百就跟一根乾枯的樹枝一模一樣。", "keywords": ["camouflage", "identical", "branch"] },
      { "id": 4, "speaker": "Ruby", "avatar": "👧", "en": "And look at the next display: the Hercules beetle from the rainforest with a horn as long as my hand!", "zh": "再看隔壁展示櫃：來自雨林、長著跟我的手掌一樣長巨角的長戟大兜蟲！", "keywords": ["Hercules beetle", "horn", "rainforest"] },
      { "id": 5, "speaker": "Ben", "avatar": "👦", "en": "Nature has designed so many bizarre and brilliant survival adaptations.", "zh": "大自然為昆蟲設計了這麼多奇特又聰明的生存演化適應機制，真令人大開眼界。", "keywords": ["bizarre", "adaptations", "survival"] }
    ],
    "vocabulary": [
      { "word": "camouflage", "phonetic": "/ˈkæm.ə.flɑːʒ/", "pos": "n./v.", "zh": "偽裝、保護色", "example": "Chameleons use color-changing camouflage to hide from predators." },
      { "word": "terrarium", "phonetic": "/təˈrer.i.əm/", "pos": "n.", "zh": "玻璃爬蟲箱、玻璃生態缸", "example": "He planted moss and ferns inside a glass terrarium." },
      { "word": "bizarre", "phonetic": "/bəˈzɑːr/", "pos": "adj.", "zh": "古怪奇特的、奇異的", "example": "Deep-sea anglerfish have bizarre bioluminescent lures." }
    ],
    "dailyPhrase": { "en": "Spot something.", "zh": "敏銳發現、看出某個隱藏事物。" },
    "cultureTip": "竹節蟲（Stick insect / Walking stick）展現了動物界極致的「擬態（MIMICRY）」與「偽裝（Camouflage）」。長戟大兜蟲（Hercules beetle）則是世界上體型最長的甲蟲，最長可達 18 公分。"
  },

  # 07-22 [國中挑戰]
  {
    "id": "dialogue-0722",
    "date": "07-22",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "盛夏節氣",
    "topic": {
      "en": "Dashu Solar Term: Major Heat, Sweet Pineapples & Summer Solace",
      "zh": "大暑節氣：一年中最炎熱的一天與吃鳳梨消暑民間習俗"
    },
    "situation": "時逢二十四節氣中的「大暑」，Leo 和 Jessica 坐在傳統冰果室裡，吹著電風扇享用新鮮現切的關廟金鑽鳳梨切片。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Jessica": { "role": "Jessica", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0722.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Jessica, the asphalt outside is practically shimmering in the blazing sun today. It is officially Dashu, or 'Major Heat'!", "zh": "Jessica，今天外面馬路上的柏油在烈日曝曬下簡直都在發燙閃爍。今天正是『大暑』節氣！", "keywords": ["Dashu", "Major Heat", "shimmering"] },
      { "id": 2, "speaker": "Jessica", "avatar": "👧", "en": "Dashu is the twelfth solar term and traditionally recognized as the hottest period of the entire solar calendar.", "zh": "大暑是第十二個節氣，也是農曆節氣中公認全年度氣溫最高、日照最猛烈的最酷熱時節。", "keywords": ["twelfth", "solar calendar", "hottest"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Folk proverbs say: 'Eating pineapple on Dashu brings auspicious luck and cools down internal fire.'", "zh": "民間農諺常說：『大暑吃鳳梨』，不僅因為此時鳳梨最香甜多汁，更取其『旺來』祈求吉祥平順。", "keywords": ["pineapple", "proverbs", "auspicious"] },
      { "id": 4, "speaker": "Jessica", "avatar": "👧", "en": "Pineapples harvested around Dashu are at peak ripeness—bursting with golden sweetness without any mouth-stinging sourness.", "zh": "大暑前後採收的鳳梨熟度達到最巔峰——金黃果肉甜度極高，完全沒有咬舌頭的酸澀感。", "keywords": ["ripeness", "mouth-stinging", "golden sweetness"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "And in ancient times, fishermen floated miniature wooden 'Dashu boats' carrying offerings into the sea to pray for peace and epidemic prevention.", "zh": "古代沿海居民還有在『大暑送大暑船』的民俗，將滿載供品的彩繪小木船送出大海，祈求驅除暑熱疫病、闔家平安。", "keywords": ["offerings", "miniature", "epidemic"] },
      { "id": 6, "speaker": "Jessica", "avatar": "👧", "en": "When heat reaches its absolute extreme, autumn draws near. Nature always moves toward renewal and equilibrium.", "zh": "物極必反，大暑過後，秋天的腳步其實就已悄悄臨近了。大自然始終在循環中邁向新生與平衡。", "keywords": ["equilibrium", "renewal", "extreme"] }
    ],
    "vocabulary": [
      { "word": "auspicious", "phonetic": "/ɑːˈspɪʃ.əs/", "pos": "adj.", "zh": "吉利的、吉祥如意的", "example": "Red lanterns were hung to mark the auspicious festival." },
      { "word": "ripeness", "phonetic": "/ˈraɪp.nəs/", "pos": "n.", "zh": "成熟、熟成度", "example": "The fruits reached optimal sweetness at full ripeness." },
      { "word": "equilibrium", "phonetic": "/ˌek.wəˈlɪb.ri.əm/", "pos": "n.", "zh": "平衡、平穩狀態", "example": "Ecosystems maintain delicate equilibrium through biodiversity." }
    ],
    "dailyPhrase": { "en": "Peak ripeness.", "zh": "達到熟成的最巔峰黃金期。" },
    "cultureTip": "大暑（Major Heat）是一年中最熱的節氣。台灣民諺「大暑吃鳳梨」，此時盛產的金鑽鳳梨（Pineapple）風味最濃郁清甜；同時民間也認為大暑過後便是立秋，「大暑熱不透，大熱在秋後」。"
  },

  # 07-23 [國小中高]
  {
    "id": "dialogue-0723",
    "date": "07-23",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "溪流生態",
    "topic": {
      "en": "Stream Exploration: Catching Shrimp & Practicing Leave No Trace",
      "zh": "戶外野溪探索：觀察溪蝦與實踐無痕山林守則"
    },
    "situation": "週末郊外清涼溪流旁，Jason 和 Maya 捲起褲管站在淺溪鵝卵石上，拿著透明觀察箱觀察溪蝦和小溪哥魚。",
    "speakers": {
      "Jason": { "role": "Jason", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Maya": { "role": "Maya", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0723.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Jason", "avatar": "👦", "en": "Maya, step carefully on these rounded river pebbles. Some green algae rocks can be quite slippery.", "zh": "Maya，踩在這些圓滾滾的溪流鵝卵石上要格外小心。有些長滿綠苔的石頭非常濕滑喔。", "keywords": ["pebbles", "algae", "slippery"] },
      { "id": 2, "speaker": "Maya", "avatar": "👧", "en": "I am wearing non-slip felt-soled river tracing shoes! Look under that submerged flat rock—a tiny freshwater shrimp is swimming backward!", "zh": "我有穿防滑的毛氈底溯溪鞋！你看浸在水底的那塊平坦石頭下——有一隻小溪蝦正在倒退游呢！", "keywords": ["river tracing", "submerged", "shrimp"] },
      { "id": 3, "speaker": "Jason", "avatar": "👦", "en": "I caught it gently in our transparent observation box. Its see-through body and long whiskers are so delicate.", "zh": "我用透明觀察箱輕輕把它撈進來了。它晶瑩剔透的透明身體和細長的觸鬚看起來好精巧脆弱。", "keywords": ["whiskers", "transparent", "delicate"] },
      { "id": 4, "speaker": "Maya", "avatar": "👧", "en": "Let's release it back into the crystal stream pool right away so it can continue thriving in its natural home.", "zh": "我們趕快把它放回這汪清澈的溪潭裡吧，讓它能繼續在天然家園裡自由自在地生活。", "keywords": ["release", "crystal", "thriving"] },
      { "id": 5, "speaker": "Jason", "avatar": "👦", "en": "Take only pictures, leave only ripples, and carry every bit of trash home. That is Leave No Trace!", "zh": "只帶走相片，只留下水波漣漪，並把所有垃圾隨身帶回家。這正是無痕山林的真諦！", "keywords": ["ripples", "Leave No Trace", "trash"] }
    ],
    "vocabulary": [
      { "word": "pebble", "phonetic": "/ˈpeb.əl/", "pos": "n.", "zh": "鵝卵石、圓石", "example": "Smooth river pebbles lined the clear mountain creek." },
      { "word": "whisker", "phonetic": "/ˈwɪs.kɚ/", "pos": "n.", "zh": "（動物的）鬍鬚、觸鬚", "example": "The freshwater shrimp twitched its long sensory whiskers." },
      { "word": "ripple", "phonetic": "/ˈrɪp.əl/", "pos": "n.", "zh": "漣漪、細浪", "example": "A dropped stone created concentric ripples on the lake." }
    ],
    "dailyPhrase": { "en": "Leave No Trace.", "zh": "無痕山林守則（戶外保育核心理念）。" },
    "cultureTip": "無痕山林（Leave No Trace, LNT）七大準則提倡：尊重野生動物、只留回憶不帶走生物、妥善處理垃圾。溪流戲水穿著防滑溯溪鞋（river tracing shoes），既安全又兼顧生態永續。"
  },

  # 07-24 [高中進階]
  {
    "id": "dialogue-0724",
    "date": "07-24",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "未來工作",
    "topic": {
      "en": "Digital Nomadism: Geographical Freedom, Loneliness & Discipline",
      "zh": "數位遊牧與未來工作型態：地理自由背後的時間自律與孤獨思辨"
    },
    "situation": "在青年未來趨勢沙龍上，Alex 和 Brenda 就全球遠端辦公興起、數位遊牧族群（Digital Nomads）的理想與現實展開對話。",
    "speakers": {
      "Alex": { "role": "Alex", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Brenda": { "role": "Brenda", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0724.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Alex", "avatar": "👨‍🎓", "en": "Brenda, social media constantly romanticizes digital nomadism: coding laptops on tropical beaches while traveling perpetually.", "zh": "Brenda，社群媒體經常過度浪漫化數位遊牧生活：抱著筆電在熱帶海灘邊寫程式，一邊環遊世界一邊賺取高薪。", "keywords": ["romanticizes", "digital nomadism", "perpetually"] },
      { "id": 2, "speaker": "Brenda", "avatar": "👩‍🎓", "en": "That polished veneer obscures gritty realities. Glare makes screens unreadable in sunlight, sand destroys keyboards, and precarious Wi-Fi triggers client panics.", "zh": "那層光鮮亮麗的濾鏡掩蓋了骨感的現實。強光讓螢幕在戶外根本無法辨識，細沙會摧毀鍵盤，不穩定的網路更會引發客戶失聯危機。", "keywords": ["veneer", "glare", "precarious"] },
      { "id": 3, "speaker": "Alex", "avatar": "👨‍🎓", "en": "More profoundly, constant relocation severs deep communal roots. Transient friendships across hostels can precipitate chronic existential loneliness.", "zh": "更深層的問題在於，頻繁的流動遷徙會切斷穩固的在地社群歸屬。青年旅館裡萍水相逢的短暫友誼，很容易演化為慢性的存在主義孤獨感。", "keywords": ["relocation", "transient", "loneliness"] },
      { "id": 4, "speaker": "Brenda", "avatar": "👩‍🎓", "en": "True location independence demands relentless self-discipline, meticulous time-zone synchronization, and strict boundary separation between labor and leisure.", "zh": "真正的地理自由背後，需要的是鋼鐵般嚴格的自我自律、精準的跨時區協作，以及在工作勞動與休閒生活之間劃定清晰界線的能力。", "keywords": ["synchronization", "boundary", "self-discipline"] },
      { "id": 5, "speaker": "Alex", "avatar": "👨‍🎓", "en": "Nonetheless, asynchronous distributed work is dismantling the obsolete industrial model of rigid nine-to-five commuter drudgery.", "zh": "儘管如此，非同步的分散式工作模式，確實正在瓦解傳統工業時代僵化打卡通勤、朝九晚五的枯燥模式。", "keywords": ["asynchronous", "drudgery", "obsolete"] },
      { "id": 6, "speaker": "Brenda", "avatar": "👩‍🎓", "en": "Freedom is not the absence of structure; it is the autonomy to build an intentional life architecture aligned with your core values.", "zh": "自由從來不是完全沒有架構拘束；自由是擁有自主權，去建構一套符合自己核心價值觀、帶著清晰自覺的生活建築體系。", "keywords": ["autonomy", "intentional", "architecture"] }
    ],
    "vocabulary": [
      { "word": "veneer", "phonetic": "/vəˈnɪr/", "pos": "n.", "zh": "虛假的外表、光鮮的飾面", "example": "Her calm smile was a thin veneer masking intense stage fright." },
      { "word": "precarious", "phonetic": "/prɪˈker.i.əs/", "pos": "adj.", "zh": "不穩定的、危險的、朝不保夕的", "example": "Freelancers often navigate precarious income fluctuations." },
      { "word": "drudgery", "phonetic": "/ˈdrʌdʒ.ɚ.i/", "pos": "n.", "zh": "繁重單調的苦工、勞碌", "example": "Automation relieved workers of repetitive data-entry drudgery." }
    ],
    "dailyPhrase": { "en": "Location independence.", "zh": "地點獨立性、不受特定辦公地點限制的工作模式。" },
    "cultureTip": "「數位遊牧（Digital Nomadism）」隨著高速星鏈網路與遠端工作普及成為全球新興工作形態。自由工作者（freelancers）與遠距工作者透過「非同步溝通（asynchronous communication）」實現全球旅居，但極度考驗時間自律與心理韌性。"
  },

  # 07-25 [國小初階]
  {
    "id": "dialogue-0725",
    "date": "07-25",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "雨後寧靜",
    "topic": {
      "en": "Sudden Summer Rain: Watching Puddles Ripple from the Porch",
      "zh": "午後雷陣雨的浪漫：在騎樓下靜看雨滴在水窪泛起漣漪"
    },
    "situation": "盛夏午後突然下起傾盆大雨，Leo 和 Mia 站在文具店騎樓下躲雨，靜靜看著街角水窪裡一圈圈擴散的雨波。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0725.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Mia, step under the covered arcade! The sky opened up with a sudden summer downpour!", "zh": "Mia，快跨進騎樓遮雨廊下！天空突然下起了傾盆的盛夏大雨！", "keywords": ["arcade", "downpour", "covered"] },
      { "id": 2, "speaker": "Mia", "avatar": "👧", "en": "Listen to the rain drumming on the tin awning! It sounds like natural percussion music.", "zh": "聽雨水劈劈啪啪打在鐵皮雨棚上的聲音！聽起來真像大自然的打擊樂演奏一樣。", "keywords": ["percussion", "awning", "drumming"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Look at the big puddle on the sidewalk. Each falling raindrop creates expanding concentric rings.", "zh": "看人行道上那個大水窪。每一顆落下的雨滴都在水面上泛起一圈圈向外擴散的同心圓水波呢。", "keywords": ["puddle", "concentric", "raindrop"] },
      { "id": 4, "speaker": "Mia", "avatar": "👧", "en": "The moist air smells so fresh and cool. It washed away all the dust and oppressive heat.", "zh": "濕潤的空氣聞起來好清新涼爽。它把空氣中所有的灰塵和令人窒息的悶熱都沖刷得一乾二淨了。", "keywords": ["oppressive", "moist", "dust"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Pausing our steps to watch a summer rain shower makes you appreciate the quiet rhythm of nature.", "zh": "停下匆忙腳步靜靜看一場夏雨，真能讓人體會到大自然寧靜而美麗的韻律節奏。", "keywords": ["appreciate", "rhythm", "pausing"] }
    ],
    "vocabulary": [
      { "word": "arcade", "phonetic": "/ɑːrˈkeɪd/", "pos": "n.", "zh": "騎樓、拱廊走廊", "example": "Pedestrians walked comfortably sheltered beneath the street arcade." },
      { "word": "concentric", "phonetic": "/kənˈsen.trɪk/", "pos": "adj.", "zh": "同心的（有共同圓心的）", "example": "Ripples spread outward in expanding concentric circles." },
      { "word": "oppressive", "phonetic": "/əˈpres.ɪv/", "pos": "adj.", "zh": "悶熱窒息的、令人壓抑難受的", "example": "The oppressive heat finally broke when evening thunderstorms arrived." }
    ],
    "dailyPhrase": { "en": "The sky opened up.", "zh": "突然下起傾盆大雨、大雨如注。" },
    "cultureTip": "台灣與東南亞建築常見「騎樓（covered arcade / shophouse walkways）」，提供遮陽避雨功能。英文中的「The smell of rain」有一個優美專有名詞「Petrichor（潮土仕 / 雨後泥土芳香）」，由泥土中的放線菌化合物釋放而成。"
  },

  # 07-26 [國小中高]
  {
    "id": "dialogue-0726",
    "date": "07-26",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "戶外輪滑",
    "topic": {
      "en": "Rollerblading & Scootering: Putting on Helmets & Protective Pads",
      "zh": "學騎滑板車與直排輪：戴好安全帽與護肘護膝安全防護"
    },
    "situation": "傍晚陽光不再熾熱，Sammy 和 Noah 在社區體育公園滑輪場穿戴好護具，練習直排輪轉彎平衡技巧。",
    "speakers": {
      "Sammy": { "role": "Sammy", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Noah": { "role": "Noah", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0726.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sammy", "avatar": "👧", "en": "Noah, before we step onto the roller rink, let me inspect your safety gear.", "zh": "Noah，在我們滑進直排輪場地之前，先讓我檢查一下你的防護裝備。", "keywords": ["roller rink", "safety gear", "inspect"] },
      { "id": 2, "speaker": "Noah", "avatar": "👦", "en": "I strapped on my hard plastic knee pads, elbow pads, and wrist guards securely.", "zh": "我的硬質塑膠護膝、護肘還有手腕護具全都緊緊扣好了。", "keywords": ["knee pads", "wrist guards", "strapped"] },
      { "id": 3, "speaker": "Sammy", "avatar": "👧", "en": "Click your helmet chin buckle firmly until it clicks. Safety always comes first!", "zh": "安全帽的下巴扣環也要用力扣上直到聽到『喀噠』一聲。安全永遠排在第一位！", "keywords": ["buckle", "helmet", "safety first"] },
      { "id": 4, "speaker": "Noah", "avatar": "👦", "en": "Watch me glide! Bend your knees slightly forward and push off gently in a V-formation.", "zh": "看我滑行！膝蓋稍微向前微彎，雙腳腳尖微微朝外呈 V 字型輕柔推蹬發力。", "keywords": ["glide", "knees", "V-formation"] },
      { "id": 5, "speaker": "Sammy", "avatar": "👧", "en": "Feel the evening wind whistling past our ears! Gliding smoothly on wheels feels like flying!", "zh": "感受晚風在我們耳邊呼呼吹過！腳踩輪子平穩滑行的感覺簡直就像在低空飛翔一樣痛快！", "keywords": ["whistling", "wheels", "flying"] }
    ],
    "vocabulary": [
      { "word": "buckle", "phonetic": "/ˈbʌk.əl/", "pos": "n./v.", "zh": "扣環、扣緊", "example": "Fasten the buckle on your backpack securely." },
      { "word": "glide", "phonetic": "/ɡlaɪd/", "pos": "v.", "zh": "滑翔、平穩滑行", "example": "Skilled skaters glide effortlessly across smooth concrete." },
      { "word": "rink", "phonetic": "/rɪŋk/", "pos": "n.", "zh": "溜冰場、輪滑場", "example": "The outdoor roller rink was crowded with energetic kids." }
    ],
    "dailyPhrase": { "en": "Safety always comes first.", "zh": "安全永遠第一、安全至上。" },
    "cultureTip": "輪滑運動（Rollerblading / Inline Skating）訓練平衡感與下肢協調性。運動醫學強調配戴「三合一護具（Knee, elbow & wrist guards）」及符合安全規範的安全帽，可預防 90% 以上的擦傷與骨折意外。"
  },

  # 07-27 [國中挑戰]
  {
    "id": "dialogue-0727",
    "date": "07-27",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "創意自媒體",
    "topic": {
      "en": "DIY Claymation Short Film: Storyboarding with a Smartphone",
      "zh": "自製定格動畫短片：用輕黏土與智慧型手機創作童話故事"
    },
    "situation": "暑假創客工作坊裡，Julian 和 Hannah 在客廳書桌架好手機三腳架與補光燈，一格格拍攝自創的太空小怪獸黏土定格動畫。",
    "speakers": {
      "Julian": { "role": "Julian", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Hannah": { "role": "Hannah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0727.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Julian", "avatar": "👦", "en": "Hannah, keep the smartphone tripod completely stationary. If the camera wobbles, the stop-motion effect looks jerky.", "zh": "Hannah，手機三腳架一定要保持絕對靜止不動。如果鏡頭有一絲搖晃，定格動畫看起來就會卡頓突兀。", "keywords": ["tripod", "stationary", "jerky"] },
      { "id": 2, "speaker": "Hannah", "avatar": "👧", "en": "I locked the exposure and manual focus. Now, move the green clay alien's left tentacle by just two millimeters.", "zh": "我已經鎖定好曝光與手動對焦了。現在，把綠色黏土小外星人的左觸手只輕輕移動兩毫米。", "keywords": ["exposure", "tentacle", "millimeters"] },
      { "id": 3, "speaker": "Julian", "avatar": "👦", "en": "Snap! Move two millimeters... snap! Producing one second of smooth animation requires twelve individual frames.", "zh": "拍一張！再移動兩毫米……再拍一張！要做出流暢的一秒鐘動畫，足足需要十二張獨立畫面呢。", "keywords": ["frames", "animation", "smooth"] },
      { "id": 4, "speaker": "Hannah", "avatar": "👧", "en": "It takes immense patience, but watching a lifeless lump of colorful clay miraculously spring to life is pure enchantment.", "zh": "這需要極大的耐心，但看著一團毫無生氣的彩色黏土在螢幕上奇蹟般活靈活現動起來，簡直就像被施了魔法一樣迷人。", "keywords": ["lifeless", "enchantment", "patience"] },
      { "id": 5, "speaker": "Julian", "avatar": "👦", "en": "After shooting the frames, we will import them into an editing app and record funny monster squeaks and laser sound effects.", "zh": "拍攝完畫面之後，我們把照片匯入剪輯軟體，再親自配音怪獸叫聲與雷射光音效。", "keywords": ["editing app", "sound effects", "import"] },
      { "id": 6, "speaker": "Hannah", "avatar": "👧", "en": "Filmmaking blends storytelling, manual sculpting, and technology into a rewarding artistic journey.", "zh": "拍動畫將說故事、手工雕塑與數位科技完美融合為一體，真是充滿成就感的藝術探索旅程。", "keywords": ["sculpting", "storytelling", "filmmaking"] }
    ],
    "vocabulary": [
      { "word": "stationary", "phonetic": "/ˈsteɪ.ʃən.er.i/", "pos": "adj.", "zh": "靜止不動的、固定不變的", "example": "Keep the microscope stationary while focusing on the specimen." },
      { "word": "frame", "phonetic": "/freɪm/", "pos": "n.", "zh": "（動畫或影片的）畫面格、幀", "example": "Cinema film traditionally projects twenty-four frames per second." },
      { "word": "enchantment", "phonetic": "/ɪnˈtʃænt.mənt/", "pos": "n.", "zh": "著迷、陶醉、魔法般的魅力", "example": "The fairy tale forest filled children with wonder and enchantment." }
    ],
    "dailyPhrase": { "en": "Spring to life.", "zh": "突然充滿生機活力、活靈活現躍動起來。" },
    "cultureTip": "定格動畫（Stop-Motion / Claymation，如經典作品《笑笑羊》）利用物體微幅移動拍攝單張影格（frames）。智慧型手機普及讓青少年在家即可低門檻體驗分鏡故事板（Storyboarding）與音效設計的影視創作樂趣。"
  },

  # 07-28 [高中進階]
  {
    "id": "dialogue-0728",
    "date": "07-28",
    "level": "senior_high",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#7c3aed",
    "category": "公衛歷史",
    "topic": {
      "en": "World Hepatitis Day: Taiwan's Historic Universal Vaccination Triumph",
      "zh": "世界肝炎日與公共衛生奇蹟：台灣全面實施B肝疫苗接種的歷史豐碑"
    },
    "situation": "7月28日世界肝炎日，生醫研習社社長 Kevin 和 Audrey 在校園科教館特展海報前，回顧台灣改寫全球肝癌防治史的里程碑。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "👨‍🎓", "gender": "male", "voice": "en-US-GuyNeural" },
      "Audrey": { "role": "Audrey", "avatar": "👩‍🎓", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0728.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "👨‍🎓", "en": "Audrey, today is World Hepatitis Day, honoring the birthday of Nobel laureate Dr. Baruch Blumberg, discoverer of the Hepatitis B virus.", "zh": "Audrey，今天是世界肝炎日，紀念發現B型肝炎病毒的諾貝爾醫學獎得主布隆伯格博士誕辰。", "keywords": ["World Hepatitis Day", "laureate", "Hepatitis B"] },
      { "id": 2, "speaker": "Audrey", "avatar": "👩‍🎓", "en": "Few high schoolers realize that back in 1984, Taiwan launched the world's very first nationwide universal Hepatitis B infant vaccination program.", "zh": "很少有同學知道，早在 1984 年，台灣就率先全球啟動了世界第一個全面的新生兒B型肝炎全面疫苗接種計畫。", "keywords": ["infant", "vaccination", "universal"] },
      { "id": 3, "speaker": "Kevin", "avatar": "👨‍🎓", "en": "Prior to that pioneering public health intervention, nearly twenty percent of our population were chronic carriers, suffering high rates of cirrhosis and liver cancer.", "zh": "在那項開創性的公共衛生重大介入之前，全台近兩成人口是慢性帶原者，長年飽受高發的肝硬化與肝癌折磨。", "keywords": ["cirrhosis", "chronic carriers", "intervention"] },
      { "id": 4, "speaker": "Audrey", "avatar": "👩‍🎓", "en": "By immunizing newborns to block vertical mother-to-child transmission, childhood liver cancer rates plunged by seventy-five percent—a historic triumph in cancer prevention.", "zh": "藉由為新生兒全面接種免疫阻斷母嬰垂直傳播，兒童肝癌發生率驟降了百分之七十五——這成為全球癌症預防史上的空前勝利！", "keywords": ["transmission", "immunizing", "prevention"] },
      { "id": 5, "speaker": "Kevin", "avatar": "👨‍🎓", "en": "That landmark epidemiological achievement proved that prophylactic vaccines can effectively eradicate viral-induced malignancies.", "zh": "那項劃時代的流行病學成就向全世界證實：預防性疫苗能極為有效地消滅病毒誘發的惡性腫瘤癌症。", "keywords": ["epidemiological", "prophylactic", "malignancies"] },
      { "id": 6, "speaker": "Audrey", "avatar": "👩‍🎓", "en": "Public health victories are silent miracles. When prevention succeeds, nothing catastrophic happens—and that quiet protection is medicine's greatest triumph.", "zh": "公共衛生的勝利往往是沉靜的奇蹟。當預防成功時，災難便無聲消弭——而這份默默守護，正是現代醫學最偉大的榮光。", "keywords": ["catastrophic", "miracles", "prevention"] }
    ],
    "vocabulary": [
      { "word": "prophylactic", "phonetic": "/ˌproʊ.fəˈlæk.tɪk/", "pos": "adj.", "zh": "預防性的、防止疾病發生的", "example": "Prophylactic dental cleanings prevent severe periodontal disease." },
      { "word": "cirrhosis", "phonetic": "/səˈroʊ.sɪs/", "pos": "n.", "zh": "肝硬化", "example": "Chronic hepatitis infection can lead to liver cirrhosis." },
      { "word": "malignancy", "phonetic": "/məˈlɪɡ.nən.si/", "pos": "n.", "zh": "惡性腫瘤、惡性疾病", "example": "Early screening detects cellular malignancies before metastasis occurs." }
    ],
    "dailyPhrase": { "en": "Silent miracles.", "zh": "默默守護的奇蹟、潤物細無聲的偉大成就。" },
    "cultureTip": "7月28日是世界衛生組織（WHO）訂定的「世界肝炎日（World Hepatitis Day）」。台灣於1984年領先全球推行新生兒全面施打B肝疫苗（Universal Hepatitis B vaccination），成功將兒童肝癌發生率降低逾七成，被公認為全球公衛防癌典範。"
  },

  # 07-29 [國小中高]
  {
    "id": "dialogue-0729",
    "date": "07-29",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "太空奇境",
    "topic": {
      "en": "Immersive Science Exhibition: Experiencing Black Hole Gravity",
      "zh": "參觀當代科學特展：沉浸式體驗黑洞引力扭曲時空"
    },
    "situation": "國立自然科學博物館的當代天文特展廳裡，Tony 和 Clara 戴上 VR 穿戴裝置，體驗掉入黑洞事件視界的奇幻視覺特效。",
    "speakers": {
      "Tony": { "role": "Tony", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Clara": { "role": "Clara", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0729.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tony", "avatar": "👦", "en": "Clara, look into this immersive projection dome! The simulated black hole is bending starlight into a glowing golden ring!", "zh": "Clara，看這個沉浸式穹頂投影！模擬的黑洞正在把周圍的星光扭曲成一道發光的金黃色光環！", "keywords": ["projection dome", "black hole", "starlight"] },
      { "id": 2, "speaker": "Clara", "avatar": "👧", "en": "That brilliant ring is called the accretion disk, formed by superheated matter swirling inward at nearly light speed.", "zh": "那圈明亮耀眼的光環叫做『吸積盤』，由被加熱到極高溫、以接近光速旋轉吸入的宇宙物質所構成。", "keywords": ["accretion disk", "swirling", "light speed"] },
      { "id": 3, "speaker": "Tony", "avatar": "👦", "en": "The museum guide explained Einstein's General Relativity: gravity is not a mysterious invisible pulling force, but the warping of spacetime itself.", "zh": "館員解說了愛因斯坦的廣義相對論：重力不是神秘無形的拉扯力，而是時空幾何本身的彎曲扭曲現象。", "keywords": ["General Relativity", "warping", "gravity"] },
      { "id": 4, "speaker": "Clara", "avatar": "👧", "en": "Once an object crosses the event horizon boundary, not even speed-of-light photons can ever escape its colossal grip.", "zh": "一旦物體跨過了『事件視界』的邊界，就連宇宙中速度最快的光子也永遠無法逃脫其龐大的引力掌握。", "keywords": ["event horizon", "photons", "escape"] },
      { "id": 5, "speaker": "Tony", "avatar": "👦", "en": "Exploring these mind-blowing cosmic frontiers makes me want to study astrophysics when I grow up!", "zh": "探索這些令人震撼驚嘆的宇宙前沿奧秘，讓我長大後超想去深入研究天體物理學！", "keywords": ["astrophysics", "mind-blowing", "cosmic"] }
    ],
    "vocabulary": [
      { "word": "accretion", "phonetic": "/əˈkriː.ʃən/", "pos": "n.", "zh": "積聚、吸積（天文物質堆積）", "example": "Black holes draw matter into an incandescent accretion disk." },
      { "word": "warp", "phonetic": "/wɔːrp/", "pos": "v.", "zh": "扭曲、使彎曲形變", "example": "Immense gravitational mass warps the fabric of surrounding space." },
      { "word": "photon", "phonetic": "/ˈfoʊ.tɑːn/", "pos": "n.", "zh": "光子（光能量基本粒子）", "example": "Solar panels convert incoming photons directly into electrical current." }
    ],
    "dailyPhrase": { "en": "Mind-blowing.", "zh": "令人震撼無比的、大開眼界的。" },
    "cultureTip": "黑洞（Black Hole）與「事件視界（Event Horizon）」是現代天體物理學的核心。中研院參與的「事件視界望遠鏡（EHT）」國際團隊成功拍攝到人類史上首張黑洞照片，向世人證實了廣義相對論的預測。"
  },

  # 07-30 [國中挑戰]
  {
    "id": "dialogue-0730",
    "date": "07-30",
    "level": "junior_high",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "友誼跨越",
    "topic": {
      "en": "International Day of Friendship: Mailing Photo Postcards to Pen Pals",
      "zh": "國際友誼日：給遠方好友寄一張親手拍攝的美景明信片"
    },
    "situation": "7月30日國際友誼日，Oliver 和 Maya 坐在郵局木桌旁，挑選印有自己拍的高山海景照片的明信片，貼上郵票寄給國外筆友。",
    "speakers": {
      "Oliver": { "role": "Oliver", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Maya": { "role": "Maya", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0730.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Oliver", "avatar": "👦", "en": "Maya, today is the United Nations International Day of Friendship! Have you finished writing your postcards?", "zh": "Maya，今天是聯合國國際友誼日！你的明信片都寫好了嗎？", "keywords": ["International Day of Friendship", "postcards"] },
      { "id": 2, "speaker": "Maya", "avatar": "👧", "en": "Almost! I chose a card featuring our sunset at Kenting beach to mail to my pen pal, Elena, in Madrid.", "zh": "快好了！我挑了一張印有我們在墾丁海邊拍的夕陽剪影明信片，準備寄給我遠在馬德里的筆友 Elena。", "keywords": ["pen pal", "sunset", "Madrid"] },
      { "id": 3, "speaker": "Oliver", "avatar": "👦", "en": "In our age of instant messaging, taking the time to handwrite warm sentiments onto textured paper feels exceptionally meaningful.", "zh": "在當今即時通訊軟體盛行的時代，願意花時間在有質感的紙張上親手寫下溫暖心聲，感覺格外有溫度與誠意。", "keywords": ["instant messaging", "sentiments", "handwrite"] },
      { "id": 4, "speaker": "Maya", "avatar": "👧", "en": "Affixing an airmail stamp and dropping it into the red postbox sends tangible goodwill across continents.", "zh": "貼上一枚航空郵票並投進紅色郵筒，能將實實在在的溫暖祝福跨越大洋陸塊傳遞到遠方。", "keywords": ["airmail stamp", "postbox", "goodwill"] },
      { "id": 5, "speaker": "Oliver", "avatar": "👦", "en": "Cross-cultural friendships dismantle stereotypes and prove that young people worldwide share identical hopes and dreams.", "zh": "跨文化的國際友誼能打破刻板印象偏見，並證明全世界的青年其實都懷抱著相似的希望與夢想。", "keywords": ["stereotypes", "cross-cultural", "dreams"] },
      { "id": 6, "speaker": "Maya", "avatar": "👧", "en": "A loyal friend is like a sturdy anchor in a stormy sea. May our friendships flourish across oceans!", "zh": "忠實的朋友就像狂風暴雨狂瀾中沉著平穩的錨。願我們的跨國友誼如同浩瀚大洋般長久綻放！", "keywords": ["anchor", "flourish", "loyal friend"] }
    ],
    "vocabulary": [
      { "word": "sentiment", "phonetic": "/ˈsen.tə.mənt/", "pos": "n.", "zh": "情思、心聲、真摯情感", "example": "The greeting card expressed genuine heartfelt sentiments." },
      { "word": "affix", "phonetic": "/əˈfɪks/", "pos": "v.", "zh": "貼上、黏貼、附上", "example": "Affix a valid postage stamp to the top right corner." },
      { "word": "stereotype", "phonetic": "/ˈster.i.oʊ.taɪp/", "pos": "n.", "zh": "刻板印象、成見", "example": "Travel helps break down cultural stereotypes and prejudice." }
    ],
    "dailyPhrase": { "en": "Cross-cultural friendship.", "zh": "跨文化友誼、國際同窗情誼。" },
    "cultureTip": "7月30日是聯合國「國際友誼日（International Day of Friendship）」，倡導透過不同文化、國家與族群青年間的真誠交流（cross-cultural understanding），促進全球和平與友愛。"
  },

  # 07-31 [國小初階]
  {
    "id": "dialogue-0731",
    "date": "07-31",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "盛夏回顧",
    "topic": {
      "en": "July Wrap-Up: Cherishing Summer Adventures & Welcoming August",
      "zh": "七月終曲：回顧盛夏的美好冒險，倒數八月新旅程"
    },
    "situation": "7月31日傍晚夕陽西下，Tyler 和 Amy 坐在門前木台階上，一邊吃著芒果冰棒，一邊翻看七月拍的暑期冒險相片。",
    "speakers": {
      "Tyler": { "role": "Tyler", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Amy": { "role": "Amy", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0731.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tyler", "avatar": "👦", "en": "Can you believe today is the very last day of July, Amy? Summer is flying by so fast!", "zh": "Amy，你能相信今天已經是七月的最後一天了嗎？暑假過得未免也太飛快了！", "keywords": ["July", "flying by", "last day"] },
      { "id": 2, "speaker": "Amy", "avatar": "👧", "en": "Look at our photo album! We went swimming, built sandcastles, stargazed, and made delicious homemade popsicles.", "zh": "看我們的相簿！我們去游泳、在沙灘堆沙堡、觀賞銀河星空，還親手做了美味的水果冰棒呢。", "keywords": ["photo album", "sandcastles", "stargazed"] },
      { "id": 3, "speaker": "Tyler", "avatar": "👦", "en": "And we kept our promise to read good books every morning without becoming lazy couch potatoes.", "zh": "而且我們信守了約定，每天早晨都閱讀好書，完全沒有變成懶洋洋的沙發馬鈴薯。", "keywords": ["promise", "couch potatoes", "books"] },
      { "id": 4, "speaker": "Amy", "avatar": "👧", "en": "August will bring Father's Day, fun family camping trips, and the final countdown to our new school semester.", "zh": "八月份將帶來溫馨的父親節、好玩的全家露營，還有新學期開學的最後倒數呢。", "keywords": ["Father's Day", "camping trips", "countdown"] },
      { "id": 5, "speaker": "Tyler", "avatar": "👦", "en": "Goodbye, sunny July! Welcome, August! Let's continue making unforgettable summer memories!", "zh": "再見了，陽光明媚的七月！歡迎你，八月！讓我們繼續創造滿滿難忘的盛夏回憶吧！", "keywords": ["unforgettable", "memories", "August"] }
    ],
    "vocabulary": [
      { "word": "unforgettable", "phonetic": "/ˌʌn.fɚˈɡet̬.ə.bəl/", "pos": "adj.", "zh": "難忘的、令人刻骨銘心的", "example": "The safari trip was an unforgettable childhood adventure." },
      { "word": "stargaze", "phonetic": "/ˈstɑːr.ɡeɪz/", "pos": "v.", "zh": "凝望星空、觀星", "example": "We lay on the grassy hill to stargaze all night." },
      { "word": "album", "phonetic": "/ˈæl.bəm/", "pos": "n.", "zh": "相簿、影集、音樂專輯", "example": "Grandma carefully preserved historic snapshots in a leather album." }
    ],
    "dailyPhrase": { "en": "Keep one's promise.", "zh": "遵守諾言、信守約定。" },
    "cultureTip": "7月31日是暑假的「正中轉折點（Mid-vacation mark）」。歐美教育學家建議家庭在此時與孩子一同回顧七月的目標完成度（July Wrap-Up），並為八月預留戶外探險與自主預習的平衡規劃。"
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
    for d in JULY_DIALOGUES:
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
    print(f"成功將 7 月份對話寫入 {DATA_FILE}！總篇數更新為: {len(existing_data)} (新增 {added_count} 篇)")

    # 同步更新 js/data.js
    with open(JS_FILE, 'w', encoding='utf-8') as f:
        f.write("// 365 每日生活美語對話資料庫 (全年度)\n")
        f.write("const DIALOGUES_DATA = ")
        f.write(json.dumps(existing_data, ensure_ascii=False, indent=2))
        f.write(";\n")
    print(f"成功同步更新 {JS_FILE}！")

if __name__ == '__main__':
    main()
