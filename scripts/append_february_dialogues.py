#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次建立 2 月份生活對話 (02-01 至 02-28，共 28 篇)
涵蓋元宵提燈籠猜燈謎、情人節巧克力、寒假收心、新學期返校開學、櫻花初綻與二月曆法歷史！
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'dialogues.json')

FEBRUARY_DIALOGUES = [
  # 02-01 [國小初階]
  {
    "id": "dialogue-0201",
    "date": "02-01",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "春季前奏",
    "topic": {
      "en": "Welcoming February: Finding Early Green Buds",
      "zh": "迎接二月：尋找枝頭冒出的嫩綠小樹芽"
    },
    "situation": "二月的第一天下午，Toby 和妹妹 Zoe 在公園散步，仔細觀察光禿禿樹枝上冒出的微小綠芽。",
    "speakers": {
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0201.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Toby", "avatar": "👦", "en": "Zoe, turn the calendar page! February is officially here!", "zh": "Zoe，把月曆翻頁！二月份正式報到囉！", "keywords": ["February", "calendar"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Even though the winter wind is still chilly, look at this maple branch!", "zh": "雖然冬風吹起來還是涼涼的，但看這根楓樹樹枝！", "keywords": ["branch", "maple"] },
      { "id": 3, "speaker": "Toby", "avatar": "👦", "en": "Tiny, fuzzy bright green buds are poking through the brown bark!", "zh": "微小、毛茸茸的鮮綠色小芽苞正從深褐色樹皮裡探出頭來！", "keywords": ["buds", "fuzzy", "bark"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "They look like baby leaves sleeping under velvet blankets, waiting for spring sunshine.", "zh": "看起來像裹在絲絨毯裡熟睡的葉子寶寶，靜靜等待春天的陽光。", "keywords": ["velvet", "sunshine"] },
      { "id": 5, "speaker": "Toby", "avatar": "👦", "en": "Nature is slowly waking up. Winter won't last forever!", "zh": "大自然正在慢慢甦醒。寒冬不會永遠持續下去的！", "keywords": ["waking up", "spring"] }
    ],
    "vocabulary": [
      { "word": "bud", "phonetic": "/bʌd/", "pos": "n.", "zh": "花蕾、嫩芽、芽苞", "example": "Rose bushes are covered in swollen buds." },
      { "word": "bark", "phonetic": "/bɑːrk/", "pos": "n.", "zh": "樹皮", "example": "The rough bark protected the ancient tree." },
      { "word": "fuzzy", "phonetic": "/ˈfʌz.i/", "pos": "adj.", "zh": "毛茸茸的、起毛的", "example": "A peach skin feels soft and fuzzy." }
    ],
    "dailyPhrase": { "en": "Wake up from winter.", "zh": "從冬眠中甦醒、大地回春。" },
    "cultureTip": "在西方傳統中，二月被視為「The month of awakening（甦醒之月）」，大自然在冰雪下開始孕育嫩芽，象徵漫長冬天的轉折點。"
  },

  # 02-02 [國小中高]
  {
    "id": "dialogue-0202",
    "date": "02-02",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "趣味民俗",
    "topic": {
      "en": "Groundhog Day: Will Winter Last Longer?",
      "zh": "土撥鼠日：冬天還會再延長六週嗎？"
    },
    "situation": "2月2日美勞課上，Lucas 和媽媽聊起北美著名的「土撥鼠日（Groundhog Day）」天氣預報傳奇。",
    "speakers": {
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mom": { "role": "媽媽", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0202.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lucas", "avatar": "👦", "en": "Mom, the news anchor said thousands gathered in Pennsylvania to watch a chubby groundhog named Phil!", "zh": "媽媽，新聞主播說好幾千人聚集在賓州，等著看一隻叫菲爾的胖嘟嘟土撥鼠！", "keywords": ["groundhog", "anchor"] },
      { "id": 2, "speaker": "Mom", "avatar": "👩", "en": "Today is February second, Groundhog Day! Folklore claims the groundhog can forecast the arrival of spring.", "zh": "今天是二月二日土撥鼠日！民間傳說土撥鼠能預測春天的到來喔。", "keywords": ["folklore", "forecast"] },
      { "id": 3, "speaker": "Lucas", "avatar": "👦", "en": "How does a groundhog forecast the weather?", "zh": "一隻土撥鼠要怎麼預測天氣呀？", "keywords": ["weather"] },
      { "id": 4, "speaker": "Mom", "avatar": "👩", "en": "If Phil emerges from his burrow and sees his shadow on a sunny morning, he gets frightened back inside, meaning six more weeks of winter!", "zh": "如果菲爾爬出地洞，在晴朗早晨看見了自己的影子，牠會嚇得躲回洞裡，代表冬天還要持續六週！", "keywords": ["burrow", "shadow"] },
      { "id": 5, "speaker": "Lucas", "avatar": "👦", "en": "And if it's cloudy and he sees no shadow, spring arrives early! What a charming winter folklore tradition!", "zh": "而如果是陰天沒看到影子，春天就會提早來！這民間傳說傳統真迷人好玩！", "keywords": ["charming", "cloudy"] }
    ],
    "vocabulary": [
      { "word": "groundhog", "phonetic": "/ˈɡraʊnd.hɑːɡ/", "pos": "n.", "zh": "土撥鼠、旱獺", "example": "The groundhog munched quietly on fresh clover." },
      { "word": "burrow", "phonetic": "/ˈbɝː.oʊ/", "pos": "n.", "zh": "（動物掘出的）地洞、洞穴", "example": "Rabbits quickly scampered back into their burrow." },
      { "word": "forecast", "phonetic": "/ˈfɔːr.kæst/", "pos": "v./n.", "zh": "預報、預測", "example": "Meteorologists forecast a sunny weekend." }
    ],
    "dailyPhrase": { "en": "Six more weeks of winter.", "zh": "寒冬還要再持續六週（土撥鼠日的經典名言）" },
    "cultureTip": "每年 2 月 2 日是北美的「Groundhog Day」，最著名的是賓州旁蘇托尼小鎮的土撥鼠「Punxsutawney Phil」，自 1887 年延續至今。"
  },

  # 02-03 [國中挑戰]
  {
    "id": "dialogue-0203",
    "date": "02-03",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "歷史與曆法",
    "topic": {
      "en": "Why Does February Have Only 28 Days?",
      "zh": "為什麼二月份只有短短 28 天？古羅馬曆法解密"
    },
    "situation": "歷史專題研討課上，Mark 和 Kelly 探討羅馬帝國曆法演變，解密二月份天數偏少的歷史趣聞。",
    "speakers": {
      "Mark": { "role": "Mark", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Kelly": { "role": "Kelly", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0203.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mark", "avatar": "🧑", "en": "Kelly, all months have thirty or thirty-one days, except February with just twenty-eight. How did that historical quirk originate?", "zh": "Kelly，所有的月份都有三十或三十一天，唯獨二月只有二十八天。這個歷史奇特怪癖是怎麼來的？", "keywords": ["quirk", "originate"] },
      { "id": 2, "speaker": "Kelly", "avatar": "👧", "en": "It traces back to ancient Rome! Originally, Romulus instituted a ten-month calendar starting in March, completely ignoring the winter dead season.", "zh": "這要追溯到古羅馬！最早羅慕路斯設立了一年十個月的曆法從三月開始，完全不管冬天的農閒無事季節。", "keywords": ["instituted", "calendar"] },
      { "id": 3, "speaker": "Mark", "avatar": "🧑", "en": "Then King Numa added January and February to synchronize with lunar cycles?", "zh": "然後國王努馬才補加上一月和二月，讓曆法與月亮週期同步？", "keywords": ["synchronize", "lunar cycles"] },
      { "id": 4, "speaker": "Kelly", "avatar": "👧", "en": "Yes, but Romans harbored superstitions against even numbers, considering them unlucky! So months had twenty-nine or thirty-one days.", "zh": "對，但羅馬人對偶數有一種迷信恐懼，認為偶數不吉利！所以各月都是二十九或三十一天。", "keywords": ["superstitions", "unlucky"] },
      { "id": 5, "speaker": "Mark", "avatar": "🧑", "en": "And to reach a 355-day year, one month had to bite the bullet with an even number, and February—the purification month—drew the short straw!", "zh": "而為了湊齊 355 天，必須有一個月份認栽承擔偶數，掌管淨化儀式的二月就成了那個倒楣鬼！", "keywords": ["purification", "drew the short straw"] }
    ],
    "vocabulary": [
      { "word": "quirk", "phonetic": "/kwɝːk/", "pos": "n.", "zh": "古怪之處、巧合怪癖", "example": "Every language possesses unique grammatical quirks." },
      { "word": "superstition", "phonetic": "/ˌsuː.pɚˈstɪʃ.ən/", "pos": "n.", "zh": "迷信、迷信觀念", "example": "Spilling salt was once viewed through popular superstition." },
      { "word": "purification", "phonetic": "/ˌpjʊr.ə.fəˈkeɪ.ʃən/", "pos": "n.", "zh": "淨化、洗滌洗禮", "example": "Water filtration ensures chemical purification." }
    ],
    "dailyPhrase": { "en": "Draw the short straw.", "zh": "抽到下下籤、倒楣承擔苦差事。" },
    "cultureTip": "「February」來自拉丁文「Februa（羅馬古老的贖罪淨化節）」，凱撒大帝改革儒略曆時保留了二月的特殊天數，並確立每四年閏一天的閏年機制。"
  },

  # 02-04 [高中進階]
  {
    "id": "dialogue-0204",
    "date": "02-04",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "神經生物學",
    "topic": {
      "en": "The Neurochemistry of Chocolate and Mood",
      "zh": "情人節甜蜜科學：巧克力如何調控大腦快樂神經傳導物質？"
    },
    "situation": "高中化學社課堂上，Ryan 與 Olivia 探討黑巧克力中的可可多酚、苯乙胺與多巴胺受體如何協同創造愉悅幸福感。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0204.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "🧑", "en": "Olivia, as Valentine's displays pop up everywhere, chocolate is universally marketed as the elixir of affection. Is there genuine biochemistry behind that bliss?", "zh": "Olivia，隨著情人節陳列在各處亮相，巧克力普遍被包裝為愛情的魔藥。這份幸福愉悅感背後真的有生物化學依據嗎？", "keywords": ["biochemistry", "elixir"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👩", "en": "Substantial biochemistry, actually! High-percentage dark chocolate contains phenylethylamine, affectionately termed the 'love chemical'.", "zh": "其實有相當紮實的生化基礎！高濃度黑巧克力富含苯乙胺（PEA），被親切稱為『愛情化學分子』。", "keywords": ["phenylethylamine", "affectionately"] },
      { "id": 3, "speaker": "Ryan", "avatar": "🧑", "en": "Which triggers the endogenous release of dopamine in our mesolimbic reward pathways?", "zh": "它能刺激我們中腦邊緣獎賞路徑內生性釋放多巴胺？", "keywords": ["dopamine", "endogenous", "reward"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👩", "en": "Exactly. Furthermore, cacao contains anandamide—an endocannabinoid cannabinoid mimetic literally named after the Sanskrit word for divine bliss.", "zh": "沒錯。此外，可可還含有大麻素衍生物『花生四烯酸乙醇胺（Anandamide）』，字根正是梵文中的『神聖極樂』。", "keywords": ["anandamide", "cannabinoid", "bliss"] },
      { "id": 5, "speaker": "Ryan", "avatar": "🧑", "en": "Paired with rich theobromine improving cerebral blood flow, a single dark truffle is practically a neurochemical symphony of contentment.", "zh": "再搭配能改善大腦血流量的可可鹼，一顆精緻黑松露巧克力簡直就是一場喚醒愉悅神經化學的交響樂。", "keywords": ["theobromine", "symphony", "cerebral"] }
    ],
    "vocabulary": [
      { "word": "elixir", "phonetic": "/iˈlɪk.sɚ/", "pos": "n.", "zh": "靈丹妙藥、萬靈油、長生不老藥", "example": "Laughter is often praised as the finest elixir for grief." },
      { "word": "endogenous", "phonetic": "/enˈdɑː.dʒə.nəs/", "pos": "adj.", "zh": "內生性的、體內自行生成的", "example": "Exercise stimulates endogenous endorphin synthesis." },
      { "word": "symphony", "phonetic": "/ˈsɪm.fə.ni/", "pos": "n.", "zh": "交響樂、諧調一致的組合", "example": "The autumn canopy was a symphony of crimson and amber." }
    ],
    "dailyPhrase": { "en": "A symphony of contentment.", "zh": "一場身心舒暢知足的交響曲。" },
    "cultureTip": "「Anandamide」由以色列科學家 Raphael Mechoulam 於 1992 年命名，源自梵語「Ananda（極致喜悅）」，是大腦調節情緒與疼痛感知的關鍵神經脂質。"
  },

  # 02-05 [國小初階]
  {
    "id": "dialogue-0205",
    "date": "02-05",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "節慶手作",
    "topic": {
      "en": "Assembling an Accordion Paper Lantern",
      "zh": "動手折出圓滾滾的百褶風琴小燈籠"
    },
    "situation": "元宵節快到了，Mia 和哥哥 Leo 拿著大紅色的卡紙，動手折出百褶形狀的提燈小燈籠。",
    "speakers": {
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0205.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mia", "avatar": "👧", "en": "Leo, Lantern Festival is this week! Let's build our own accordion paper lanterns!", "zh": "Leo，元宵節這星期就要到了！我們自己來動手做百褶風琴紙燈籠吧！", "keywords": ["accordion", "lanterns"] },
      { "id": 2, "speaker": "Leo", "avatar": "👦", "en": "Fold the red cardstock back and forth like a fan, then staple the top and bottom circles together.", "zh": "把紅色卡紙像扇子一樣一前一後反覆折，然後把上下兩端的圓圈釘在一起。", "keywords": ["cardstock", "staple"] },
      { "id": 3, "speaker": "Mia", "avatar": "👧", "en": "Pull it open gently... Wow! It expands into a plump red pumpkin lantern!", "zh": "輕輕往外拉開…哇！膨脹成一個圓滾滾的大紅南瓜燈籠了！", "keywords": ["expands", "plump"] },
      { "id": 4, "speaker": "Leo", "avatar": "👦", "en": "Tape a golden silk tassel to the base, and attach a safe little battery LED candle inside.", "zh": "在底座黏上一條金色絲線流蘇，裡面再裝上一顆安全的小電池 LED 蠟燭。", "keywords": ["tassel", "LED candle"] },
      { "id": 5, "speaker": "Mia", "avatar": "👧", "en": "Switch on the light! It glows so warmly! I can't wait to carry it at the neighborhood night walk!", "zh": "打開開關！透出好溫暖的光芒喔！我迫不及待想提著它去社區夜遊提燈籠了！", "keywords": ["glows", "night walk"] }
    ],
    "vocabulary": [
      { "word": "accordion", "phonetic": "/əˈkɔːr.di.ən/", "pos": "n./adj.", "zh": "手風琴、百褶式伸縮的", "example": "Accordion pleated paper expands smoothly." },
      { "word": "tassel", "phonetic": "/ˈtæs.əl/", "pos": "n.", "zh": "流蘇、穗子", "example": "Gold tassels dangled from graduation caps." },
      { "word": "staple", "phonetic": "/ˈsteɪ.pəl/", "pos": "v./n.", "zh": "用訂書機釘住、訂書針", "example": "Staple the report sheets in the top left corner." }
    ],
    "dailyPhrase": { "en": "Glow warmly.", "zh": "散發溫暖柔和的光芒。" },
    "cultureTip": "元宵節提燈籠（Carrying Lanterns）相傳起源於漢代，象徵以光明驅散黑暗、祈求平安，現代多採用環保安全的 LED 提燈。"
  },

  # 02-06 [國小中高]
  {
    "id": "dialogue-0206",
    "date": "02-06",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "節慶文化",
    "topic": {
      "en": "Cracking Riddles on Lanterns",
      "zh": "元宵猜燈謎：動動腦破解趣味謎語"
    },
    "situation": "學校走廊掛滿紅燈籠，每個燈籠下都掛著一張紙條，Sam 和 Emily 抬著頭饒有興味地猜謎解題。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emily": { "role": "Emily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0206.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Emily, look at the riddle slip dangling under this big dragon lantern! Let's solve it!", "zh": "Emily，看掛在這個大龍燈籠下面的謎語紙條！我們來解解看！", "keywords": ["riddle", "dangling"] },
      { "id": 2, "speaker": "Emily", "avatar": "👧", "en": "Read it aloud, Sam! What does the clue say?", "zh": "唸出來聽聽看 Sam！提示寫了什麼？", "keywords": ["clue"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "'I have no legs, but I travel all around the world. I have a spine, but no bones. What am I?'", "zh": "『我沒有腿，卻能走遍全世界；我有書脊（背脊），卻沒有任何骨頭。我是什麼？』", "keywords": ["spine", "bones"] },
      { "id": 4, "speaker": "Emily", "avatar": "👧", "en": "Hmm... A spine... Travel the world... Aha! A book! A library book has a spine and takes you everywhere!", "zh": "嗯…書脊…環遊世界…啊哈！是一本書！圖書館的精裝書有書脊，而且能帶你漫遊全世界！", "keywords": ["library book", "spine"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Flip the card to check the answer on the back... Correct! We won a mini tiger badge! High five!", "zh": "翻開背後的答案卡看看…答對了！我們贏得了一個迷你小老虎徽章！擊掌！", "keywords": ["badge", "correct"] }
    ],
    "vocabulary": [
      { "word": "riddle", "phonetic": "/ˈrɪd.əl/", "pos": "n.", "zh": "謎語、謎題", "example": "Solve this clever word riddle to open the treasure chest." },
      { "word": "dangle", "phonetic": "/ˈdæŋ.ɡəl/", "pos": "v.", "zh": "懸掛、垂下擺動", "example": "Wind chimes dangled beneath the wooden porch." },
      { "word": "spine", "phonetic": "/spaɪn/", "pos": "n.", "zh": "脊椎、脊柱；（書籍的）書脊", "example": "The title was stamped in gold across the book spine." }
    ],
    "dailyPhrase": { "en": "Crack the riddle.", "zh": "解開謎題、猜中燈謎。" },
    "cultureTip": "「猜燈謎（Solving Lantern Riddles）」始於宋代，古人將謎語貼於五彩紗燈之上，兼具文字智慧、文學造詣與幽默趣味。"
  },

  # 02-07 [國中挑戰]
  {
    "id": "dialogue-0207",
    "date": "02-07",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "春節元宵",
    "topic": {
      "en": "Rolling Sweet Tangyuan in Flour",
      "zh": "元宵滾元宵：手搖竹篩滾出白胖香甜芝麻元宵"
    },
    "situation": "元宵節當天下午，Ethan 和同學 Zoe 在傳統老字號糕餅店前，觀看老師傅用大竹篩滾動元宵的絕活。",
    "speakers": {
      "Ethan": { "role": "Ethan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0207.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ethan", "avatar": "👦", "en": "Zoe, watch the pastry master shaking that gigantic round bamboo sieve back and forth with rhythmic power!", "zh": "Zoe，看糕餅大師用有節奏的腕力，前後來回搖晃那個巨大的圓形竹篩！", "keywords": ["bamboo sieve", "pastry master"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Look at the little black sesame filling cubes rolling across mountains of dry glutinous rice flour!", "zh": "看一顆顆黑芝麻內餡小方塊，在堆積如山的乾燥糯米粉海裡滾來滾去！", "keywords": ["sesame", "glutinous"] },
      { "id": 3, "speaker": "Ethan", "avatar": "👦", "en": "Dip in cold water, toss back into the flour, and repeat five times! They grow rounder and plumper like snowballs!", "zh": "沾一下冷水，倒回麵粉裡，反覆五次！它們就像滾雪球一樣越滾越圓、越滾越胖！", "keywords": ["snowballs", "repeat"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "That's the culinary distinction: northern 'Yuanxiao' are rolled in a sieve, whereas southern 'Tangyuan' are wrapped by hand.", "zh": "這就是美食考究：北方『元宵』是用竹篩滾出來的，而南方『湯圓』是用手包出來的。", "keywords": ["culinary", "distinction"] },
      { "id": 5, "speaker": "Ethan", "avatar": "👦", "en": "Boiled in sweet osmanthus syrup, both represent the completion of Lunar New Year celebrations with perfect sweetness!", "zh": "在香甜的桂花糖水裡煮熟，兩者都代表用最圓滿的甜蜜為農曆春節畫下句點！", "keywords": ["osmanthus", "completion"] }
    ],
    "vocabulary": [
      { "word": "sieve", "phonetic": "/sɪv/", "pos": "n.", "zh": "篩子、竹篩、濾網", "example": "Sift powdered sugar through a fine mesh sieve." },
      { "word": "rhythmic", "phonetic": "/ˈrɪð.mɪk/", "pos": "adj.", "zh": "有節奏的、有韻律的", "example": "Dancers swayed to the rhythmic drum beats." },
      { "word": "osmanthus", "phonetic": "/ɑːzˈmæn.θəs/", "pos": "n.", "zh": "桂花", "example": "Fragrant sweet osmanthus blossoms perfumed the garden." }
    ],
    "dailyPhrase": { "en": "Wrap up the celebration.", "zh": "圓滿結束節慶、畫下完美句點。" },
    "cultureTip": "民俗常說「北滾元宵，南包湯圓」：元宵將凝固餡料蘸水在乾粉篩中反覆搖滾而成，口感扎實有咬勁；元宵節標誌著春節假期的正式收尾。"
  },

  # 02-08 [高中進階]
  {
    "id": "dialogue-0208",
    "date": "02-08",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "物理與光學",
    "topic": {
      "en": "The Optics of Lantern Glow and Refraction",
      "zh": "光影之美：傳統燈籠透光與折射的光學原理"
    },
    "situation": "高中物理研討會上，Alex 和 Sophia 探討傳統紙燈籠漫射（Diffused reflection）與現代稜鏡光雕燈節折射的光學原理差異。",
    "speakers": {
      "Alex": { "role": "Alex", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Sophia": { "role": "Sophia", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0208.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Alex", "avatar": "🧑", "en": "Sophia, at the municipal lantern exhibition last night, the contrast between traditional silk lantern glow and laser installations was striking.", "zh": "Sophia，昨晚在市政燈會展覽上，傳統絲綢燈籠柔和的漫射光芒與現代雷射光雕裝置的強烈對比令人震撼。", "keywords": ["exhibition", "installations", "contrast"] },
      { "id": 2, "speaker": "Sophia", "avatar": "👩", "en": "It illustrates wave optics in action! Traditional mulberry paper or translucent silk acts as a diffuse scatterer.", "zh": "這生動詮釋了波動光學！傳統構樹皮紙或半透明絲綢本質上是一個完美的漫反射散射體。", "keywords": ["translucent", "diffuse", "scatterer"] },
      { "id": 3, "speaker": "Alex", "avatar": "🧑", "en": "Right, microscopic fibers scatter high-intensity point-source photons randomly in all directions, softening harsh glare into uniform ambient illumination.", "zh": "對，微觀纖維將高強度的點光源光子隨機散射到各個方向，把刺眼的強光柔化為均勻舒適的環境光。", "keywords": ["microscopic", "photons", "illumination"] },
      { "id": 4, "speaker": "Sophia", "avatar": "👩", "en": "Whereas modern festival sculptures employ acrylic prisms and refractive lenses that exploit Snell's Law to bend and decompose beam wavelengths into iridescent rainbows.", "zh": "而現代燈會藝術裝置則運用壓克力稜鏡與折射透鏡，利用斯乃爾定律折射並將光束波長色散為如彩虹般絢麗的虹彩光澤。", "keywords": ["refractive", "prisms", "iridescent"] },
      { "id": 5, "speaker": "Alex", "avatar": "🧑", "en": "Ancient artisans intuitively mastered diffuse reflection centuries before physicists formulated the underlying optical equations.", "zh": "古代工匠早在物理學家推導出光學方程式前數個世紀，就已憑直覺完美掌握了漫反射的溫潤美學。", "keywords": ["intuitively", "equations"] }
    ],
    "vocabulary": [
      { "word": "translucent", "phonetic": "/trænˈsluː.sənt/", "pos": "adj.", "zh": "半透明的、透光的", "example": "Frosted glass creates pleasant translucent privacy." },
      { "word": "illumination", "phonetic": "/ɪˌluː.məˈneɪ.ʃən/", "pos": "n.", "zh": "照明、照射光彩", "example": "Street illumination enhanced pedestrian nighttime safety." },
      { "word": "iridescent", "phonetic": "/ˌɪr.əˈdes.ənt/", "pos": "adj.", "zh": "彩虹色的、具虹彩變色光澤的", "example": "Soap bubbles shimmer with iridescent colors." }
    ],
    "dailyPhrase": { "en": "Diffuse reflection.", "zh": "漫反射（使光線柔和不刺眼的物理現象）" },
    "cultureTip": "傳統手工花燈運用竹篾骨架與透光棉宣紙，其獨特的透光柔和感（Ambient Warmth）是冷色調電子螢幕永遠無法替代的溫潤質感。"
  },

  # 02-09 [國小初階]
  {
    "id": "dialogue-0209",
    "date": "02-09",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "寒假收心",
    "topic": {
      "en": "Resetting the Alarm Clock for School",
      "zh": "開學倒數收心操：把鬧鐘時間調早一小時"
    },
    "situation": "寒假最後一週，Ruby 和哥哥 Lucas 坐在床頭，開始調整作息時間，準備迎接下週開學。",
    "speakers": {
      "Ruby": { "role": "Ruby", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0209.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ruby", "avatar": "👧", "en": "Lucas, school starts next Monday! No more waking up at nine-thirty in our pajamas!", "zh": "Lucas，下週一就要開學了！我們不能再穿著睡衣睡到九點半了！", "keywords": ["school starts", "pajamas"] },
      { "id": 2, "speaker": "Lucas", "avatar": "👦", "en": "Let's turn the dial on our blue alarm clock from eight-thirty back to seven o'clock.", "zh": "我們把藍色鬧鐘上的旋鈕，從八點半往前調回七點鐘吧。", "keywords": ["dial", "alarm clock"] },
      { "id": 3, "speaker": "Ruby", "avatar": "👧", "en": "If we adjust fifteen minutes earlier each night, our bodies won't feel groggy on the first day!", "zh": "如果我們每天晚上提早十五分鐘上床睡覺，第一天開學身體就不會昏昏欲睡了！", "keywords": ["adjust", "groggy"] },
      { "id": 4, "speaker": "Lucas", "avatar": "👦", "en": "Great plan! Early to bed, early to rise makes you healthy, wealthy, and wise.", "zh": "好計畫！早睡早起讓人健康、富足又有智慧。", "keywords": ["early to bed", "wise"] },
      { "id": 5, "speaker": "Ruby", "avatar": "👧", "en": "Ding-dong! When the alarm rings tomorrow morning, jump right out of bed like a lively bunny!", "zh": "叮咚！明天早晨鬧鐘一響，就要像活潑的小兔子一樣立刻精神抖擻跳起床！", "keywords": ["lively", "bunny"] }
    ],
    "vocabulary": [
      { "word": "groggy", "phonetic": "/ˈɡrɑː.ɡi/", "pos": "adj.", "zh": "昏昏沉沉的、頭腦不清醒的", "example": "He felt groggy after waking from an afternoon nap." },
      { "word": "dial", "phonetic": "/daɪəl/", "pos": "n./v.", "zh": "（時鐘或收音機的）旋鈕、刻度盤", "example": "Rotate the dial clockwise to set the timer." },
      { "word": "lively", "phonetic": "/ˈlaɪv.li/", "pos": "adj.", "zh": "活潑的、精力充沛的", "example": "The school yard was filled with lively chatter." }
    ],
    "dailyPhrase": { "en": "Early to bed, early to rise.", "zh": "早睡早起身體好（西方最著名的作息格言）" },
    "cultureTip": "富蘭克林（Benjamin Franklin）名言：「Early to bed and early to rise makes a man healthy, wealthy, and wise.」，開學前一週微調作息是克服開學症候群的最好方法。"
  },

  # 02-10 [國小中高]
  {
    "id": "dialogue-0210",
    "date": "02-10",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "開學準備",
    "topic": {
      "en": "Shopping for New School Stationery",
      "zh": "逛文具店添購新學期鉛筆與筆記本"
    },
    "situation": "開學前夕在熱鬧的文具店裡，Ben 和 Tina 拿著文具採買清單，挑選新學期要用的彩色原子筆與尺規組。",
    "speakers": {
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Tina": { "role": "Tina", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0210.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ben", "avatar": "👦", "en": "Tina, check our back-to-school list! We need three 2B pencils, a non-dust eraser, and a clear plastic ruler.", "zh": "Tina，確認一下我們的開學清單！我們需要三支 2B 鉛筆、一個無屑橡皮擦，還有一把透明塑膠直尺。", "keywords": ["stationery", "eraser", "ruler"] },
      { "id": 2, "speaker": "Tina", "avatar": "👧", "en": "Look at these pastel highlighters: mint green, lavender, and buttercup yellow! Perfect for key notes!", "zh": "看這些粉嫩馬卡龍色螢光筆：薄荷綠、薰衣草紫和奶黃色！劃重點筆記最完美了！", "keywords": ["highlighters", "pastel"] },
      { "id": 3, "speaker": "Ben", "avatar": "👦", "en": "I'm picking this sturdy double-zipper pencil case to keep all our stationery neatly organized.", "zh": "我選這個結實的雙拉鍊筆袋，能把所有文具收納整理得整整齊齊。", "keywords": ["pencil case", "double-zipper"] },
      { "id": 4, "speaker": "Tina", "avatar": "👧", "en": "And three grid-lined notebooks with thick paper so ink won't bleed through to the other side.", "zh": "還有三本厚紙方格筆記本，這樣墨水才不會透到背面去。", "keywords": ["grid-lined", "bleed through"] },
      { "id": 5, "speaker": "Ben", "avatar": "👦", "en": "Unpacking fresh stationery makes starting a new semester feel exciting and full of possibilities!", "zh": "開箱嶄新的文具，讓展開新學期變得既令人興奮又充滿無限可能！", "keywords": ["semester", "possibilities"] }
    ],
    "vocabulary": [
      { "word": "stationery", "phonetic": "/ˈsteɪ.ʃə.ner.i/", "pos": "n.", "zh": "文具、信紙文具用品", "example": "The stationery store stocked imported calligraphy inks." },
      { "word": "pastel", "phonetic": "/pæsˈtel/", "pos": "adj.", "zh": "粉彩的、柔和淡雅顏色的", "example": "She wore a cozy pastel pink sweater." },
      { "word": "bleed", "phonetic": "/bliːd/", "pos": "v.", "zh": "滲透、洇墨（墨水透光透紙）", "example": "Thick cardstock prevents fountain pen ink from bleeding." }
    ],
    "dailyPhrase": { "en": "Full of possibilities.", "zh": "充滿無限潛力與可能。" },
    "cultureTip": "「Back-to-School Stationery Shopping（開學文具採購）」是全球學生的儀式感時刻，透過親手挑選工具能建立對新學期的正面心理期許。"
  },

  # 02-11 [國中挑戰]
  {
    "id": "dialogue-0211",
    "date": "02-11",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "春節返校日",
    "topic": {
      "en": "First Day Back: Unboxing Fresh Textbooks",
      "zh": "開學第一天：領新課本與聞聞新書的油墨香"
    },
    "situation": "第二學期開學日，Mark 和 Kelly 幫忙學藝股長從教務處搬回整大箱新課本，在教室發給全班同學。",
    "speakers": {
      "Mark": { "role": "Mark", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Kelly": { "role": "Kelly", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0211.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mark", "avatar": "🧑", "en": "Heave-ho! Set the heavy carton down, Kelly. Here are our brand-new semester two textbooks!", "zh": "一、二、三！把這大重紙箱放下來 Kelly。這就是我們下學期嶄新的全套新課本了！", "keywords": ["carton", "textbooks"] },
      { "id": 2, "speaker": "Kelly", "avatar": "👧", "en": "Take a deep breath! That crisp, distinct fragrance of fresh printer ink and glossy paper is unmatched!", "zh": "深吸一口氣！新印刷油墨和光面銅版紙那種清爽獨特的香氣真是太好聞了！", "keywords": ["fragrance", "glossy", "unmatched"] },
      { "id": 3, "speaker": "Mark", "avatar": "🧑", "en": "First order of business: write your full name, class number, and student ID in permanent marker on the inside cover.", "zh": "第一件最重要的事：用不掉色奇異筆在內頁封面寫上全名、班級座號和學號。", "keywords": ["permanent marker", "inside cover"] },
      { "id": 4, "speaker": "Kelly", "avatar": "👧", "en": "And wrap the covers with transparent book jackets to protect the corners from fraying over the semester.", "zh": "再包上透明書套，保護邊邊角角在這一學期裡不會被磨破起毛邊。", "keywords": ["transparent", "fraying"] },
      { "id": 5, "speaker": "Mark", "avatar": "🧑", "en": "A crisp, blank textbook is an unwritten adventure. Let's make this semester our best one yet!", "zh": "一本乾淨空白的新課本就是一場未寫下終點的探險。讓我們把這學期變成有史以來最棒的一學期！", "keywords": ["adventure", "unwritten"] }
    ],
    "vocabulary": [
      { "word": "carton", "phonetic": "/ˈkɑːr.t̬ən/", "pos": "n.", "zh": "厚紙箱、紙板箱", "example": "Unpack the carton of scientific supplies." },
      { "word": "fray", "phonetic": "/freɪ/", "pos": "v.", "zh": "（織物、邊角）磨損、起毛邊", "example": "The cuffs of his favorite denim jacket began to fray." },
      { "word": "unmatched", "phonetic": "/ʌnˈmætʃt/", "pos": "adj.", "zh": "無與倫比的、無可比擬的", "example": "Her dedication to classical violin is completely unmatched." }
    ],
    "dailyPhrase": { "en": "First order of business.", "zh": "第一要務、首要待辦事項。" },
    "cultureTip": "聞新書的油墨香（The smell of fresh books）被心理學家證實能喚起人們對「全新開始與探索求知」的積極期待，是開學日最具儀式感的體驗。"
  },

  # 02-12 [高中進階]
  {
    "id": "dialogue-0212",
    "date": "02-12",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "教育心理學",
    "topic": {
      "en": "The Fresh Start Effect and Behavioral Momentum",
      "zh": "心理學「全新起點效應」：如何利用新學期重塑學習動能？"
    },
    "situation": "高中輔導室研討會上，Ryan 和 Olivia 探討沃頓商學院著名的「全新起點效應（Fresh Start Effect）」，學習如何善用時間地標擺脫過往遺憾。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0212.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "🧑", "en": "Olivia, stepping into the second semester always generates a distinct psychological surge of energy. Is that placebo or science?", "zh": "Olivia，每當踏入下學期，總是能感受到一股獨特的心理充能感。這純粹是心理安慰劑還是有科學依據？", "keywords": ["psychological", "placebo"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👩", "en": "It's robust behavioral science discovered by Professor Katy Milkman, dubbed the 'Fresh Start Effect'.", "zh": "這是華頓商學院 Katy Milkman 教授證實的紮實行為科學，稱為『全新起點效應（Fresh Start Effect）』。", "keywords": ["behavioral", "dubbed"] },
      { "id": 3, "speaker": "Ryan", "avatar": "🧑", "en": "Because temporal landmarks—like a new semester, birthday, or Monday—psychologically segregate our past self from our future self?", "zh": "因為時間地標——比如新學期、生日或是星期一——在心理上將過去的自我與未來的自我劃清了界線？", "keywords": ["temporal landmarks", "segregate"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👩", "en": "Precisely. It relegates past mistakes and procrastination to 'old me', allowing people to approach challenges with unburdened cognitive bandwidth.", "zh": "正是如此。它把過去的失誤與拖延歸類給『過去的我』，讓大腦以沒有負擔的認知頻寬重新迎戰新挑戰。", "keywords": ["bandwidth", "relegates", "unburdened"] },
      { "id": 5, "speaker": "Ryan", "avatar": "🧑", "en": "So the strategic play is anchoring permanent habit architectures right now while this temporal tailwind is blowing at full sail.", "zh": "所以最高明的策略，就是在這股時間地標順風全速吹拂的當下，立刻錨定長期穩固的習慣架構。", "keywords": ["tailwind", "anchoring"] }
    ],
    "vocabulary": [
      { "word": "segregate", "phonetic": "/ˈseɡ.rə.ɡeɪt/", "pos": "v.", "zh": "隔離、區隔開來", "example": "Segregate bio-waste from recyclable plastics." },
      { "word": "bandwidth", "phonetic": "/ˈbænd.wɪtθ/", "pos": "n.", "zh": "頻寬；（借指）心理餘裕、精力容量", "example": "High stress diminishes cognitive bandwidth." },
      { "word": "tailwind", "phonetic": "/ˈteɪl.wɪnd/", "pos": "n.", "zh": "順風、有利推動力", "example": "Supportive mentors provide a powerful tailwind for success." }
    ],
    "dailyPhrase": { "en": "The Fresh Start Effect.", "zh": "全新起點效應（利用時間節點重啟人生動力）" },
    "cultureTip": "賓州大學研究指出，在「時間地標（Temporal Landmarks）」如開學日、新年首日，人們上健身房、訂定學習計畫與改變惡習的執行意願平均暴增 33% 以上。"
  },

  # 02-13 [國小初階]
  {
    "id": "dialogue-0213",
    "date": "02-13",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "校園友誼",
    "topic": {
      "en": "Making Handmade Friendship Valentine Cards",
      "zh": "動手做純真友情愛心卡片送給好朋友"
    },
    "situation": "情人節前一天下午在美勞教室，Toby 和妹妹 Zoe 剪下紅色與粉紅色卡紙，為班上最要好的朋友手寫溫暖的感謝卡片。",
    "speakers": {
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0213.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Toby", "avatar": "👦", "en": "Zoe, fold this pink paper in half, then cut a curved half-heart shape along the fold!", "zh": "Zoe，把這張粉紅色紙對折，然後沿著折疊線剪一個半圓弧的愛心輪廓！", "keywords": ["curved", "half-heart"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Open it up... A perfectly symmetrical heart! Symmetrical on both sides!", "zh": "打開它…一個完全對稱的愛心！兩邊一模一樣對稱！", "keywords": ["symmetrical", "heart"] },
      { "id": 3, "speaker": "Toby", "avatar": "👦", "en": "I'm writing inside for my best buddy David: 'Thanks for sharing your basketball and always cheering me up!'", "zh": "我在裡面寫給我最好的好兄弟 David：『謝謝你常常借我籃球，總是在我難過時逗我開心！』", "keywords": ["cheering", "buddy"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Glue a shiny glitter sticker and a sweet strawberry lollipop onto the card.", "zh": "在卡片上貼一張閃亮亮亮粉貼紙，再用緞帶繫上一支甜甜的草莓棒棒糖。", "keywords": ["glitter", "lollipop"] },
      { "id": 5, "speaker": "Toby", "avatar": "👦", "en": "Valentine's Day at school is all about celebrating kind friendship and saying thank you to our pals!", "zh": "在學校過情人節就是慶祝善良真摯的友誼，向身邊所有的好朋友真誠道謝！", "keywords": ["friendship", "pals"] }
    ],
    "vocabulary": [
      { "word": "symmetrical", "phonetic": "/sɪˈmet.rɪ.kəl/", "pos": "adj.", "zh": "對稱的", "example": "Butterfly wings display beautifully symmetrical patterns." },
      { "word": "pal", "phonetic": "/pæl/", "pos": "n.", "zh": "好朋友、死黨、夥伴", "example": "Childhood pals remained close through adulthood." },
      { "word": "lollipop", "phonetic": "/ˈlɑː.li.pɑːp/", "pos": "n.", "zh": "棒棒糖", "example": "Children enjoyed cherry swirl lollipops." }
    ],
    "dailyPhrase": { "en": "Cheer someone up.", "zh": "讓某人開心振作起來、排解憂愁。" },
    "cultureTip": "在歐美國小，情人節（Valentine's Day）是純粹的「友誼感恩日（Friendship Day）」，班級傳統是每個人準備小卡片或糖果分送給全班每位同學，傳遞友善與包容。"
  },

  # 02-14 [國中挑戰]
  {
    "id": "dialogue-0214",
    "date": "02-14",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "節日關懷",
    "topic": {
      "en": "Valentine's Day: Baking Strawberry Chocolate Bark",
      "zh": "情人節甜蜜烘焙：動手做凍乾草莓黑巧克力脆片"
    },
    "situation": "2月14日午後在家政教室，Sarah 和 Jake 用微波爐融化黑巧克力，鋪上乾燥草莓碎與碎杏仁堅果，冷卻凝固成美味脆片。",
    "speakers": {
      "Sarah": { "role": "Sarah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Jake": { "role": "Jake", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0214.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sarah", "avatar": "👧", "en": "Jake, stir the melted seventy-percent dark chocolate with a rubber spatula until it's silky smooth and glossy.", "zh": "Jake，用橡皮刮刀攪拌融化的百分之七十黑巧克力，直到質地柔滑有光澤。", "keywords": ["spatula", "silky smooth", "melted"] },
      { "id": 2, "speaker": "Jake", "avatar": "👦", "en": "Poured onto the parchment-lined baking sheet! Spread it into an even layer, about a quarter-inch thick.", "zh": "倒在鋪了烘焙紙的烤盤上了！把它抹成大約四分之一英吋厚的均勻薄層。", "keywords": ["parchment", "quarter-inch"] },
      { "id": 3, "speaker": "Sarah", "avatar": "👧", "en": "Now scatter freeze-dried crimson strawberries, chopped roasted almonds, and flaky sea salt over the wet chocolate!", "zh": "現在趁巧克力未乾，撒上凍乾深紅草莓粒、烤香脆杏仁碎和天然片狀海鹽！", "keywords": ["freeze-dried", "almonds", "flaky"] },
      { "id": 4, "speaker": "Jake", "avatar": "👦", "en": "Chill in the fridge for twenty minutes. Snap! Hear that sharp crack? Break it into rustic jagged shards!", "zh": "放進冰箱冷藏二十分鐘。啪嗒！聽見那聲清脆的斷裂聲了嗎？把它掰成一塊塊自然質樸的鋸齒脆片！", "keywords": ["shards", "jagged", "snap"] },
      { "id": 5, "speaker": "Sarah", "avatar": "👧", "en": "Package them in clear cellophane bags tied with red twine for our teachers and club mentors. Happy Valentine's Day!", "zh": "裝進透明玻璃紙袋裡、繫上紅細麻繩送給老師和社團指導老師。情人節快樂！", "keywords": ["cellophane", "Happy Valentine's Day"] }
    ],
    "vocabulary": [
      { "word": "spatula", "phonetic": "/ˈspætʃ.ə.lə/", "pos": "n.", "zh": "刮刀、抹刀（烘焙用）", "example": "Scrape the bowl clean with a flexible silicone spatula." },
      { "word": "shard", "phonetic": "/ʃɑːrd/", "pos": "n.", "zh": "碎片、尖銳碎塊", "example": "Broken chocolate shards made an artistic dessert topping." },
      { "word": "rustic", "phonetic": "/ˈrʌs.tɪk/", "pos": "adj.", "zh": "質樸的、鄉村手作風的", "example": "The bakery featured rustic sourdough loaves." }
    ],
    "dailyPhrase": { "en": "Silky smooth.", "zh": "如絲綢般滑順細膩（烘焙巧克力的頂級質地）" },
    "cultureTip": "「Chocolate Bark（巧克力脆片磚）」是歐美極為流行的自製節慶伴手禮，將融化巧克力撒上果乾堅果自然掰開，外觀質樸美味且心意滿分。"
  },

  # 02-15 [國小中高]
  {
    "id": "dialogue-0215",
    "date": "02-15",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "班級幹部",
    "topic": {
      "en": "Electing New Class Officers for the Semester",
      "zh": "新學期班會：熱烈提名選出班級服務幹部"
    },
    "situation": "週五班會課上，班導師主持新學期幹部選舉，Leo 和 Emma 積極參與提名與無記名投票。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0215.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Emma, today is our semester class officer election! The blackboard is split into four roles.", "zh": "Emma，今天是一學期一次的班級幹部選舉！黑板上分成了四個幹部職位。", "keywords": ["officer", "election", "blackboard"] },
      { "id": 2, "speaker": "Emma", "avatar": "👧", "en": "Class president, vice president, hygiene coordinator, and activities leader! Who are you nominating?", "zh": "班長、副班長、衛生股長和活動康樂股長！你想提名誰？", "keywords": ["nominating", "hygiene"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "I nominate David for hygiene coordinator! He takes tremendous pride in keeping our recycling bins spotless.", "zh": "我提名 David 當衛生股長！他每次把我們的資源回收桶整理得一塵不染，超級負責任。", "keywords": ["hygiene", "recycling"] },
      { "id": 4, "speaker": "Emma", "avatar": "👧", "en": "I second that nomination! And I nominate you, Leo, for activities leader because you plan the most fun games!", "zh": "我附議這項提名！然後我提名你 Leo 當活動股長，因為你總能策劃最好玩的遊戲！", "keywords": ["second", "activities"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Fold your secret ballot slips! Serving our classmates teaches teamwork and leadership responsibility!", "zh": "折好你的無記名選票！為全班同學服務能學會團隊合作與領導責任感！", "keywords": ["ballot", "leadership"] }
    ],
    "vocabulary": [
      { "word": "nominate", "phonetic": "/ˈnɑː.mə.neɪt/", "pos": "v.", "zh": "提名、推薦人選", "example": "Students nominated two candidates for class president." },
      { "word": "ballot", "phonetic": "/ˈbæl.ət/", "pos": "n.", "zh": "無記名選票、投票表決", "example": "Cast your secret ballot into the sealed voting box." },
      { "word": "second", "phonetic": "/ˈsek.ənd/", "pos": "v.", "zh": "（在會議中）附議、贊同提名", "example": "I second the motion to approve the budget." }
    ],
    "dailyPhrase": { "en": "I second that nomination.", "zh": "我附議這項提名（正式會議用語）" },
    "cultureTip": "班級幹部選舉採無記名投票（Secret Ballot），落實「公民民主素養」，讓學生體會服務他人而非單純追求權力的公僕精神。"
  },

  # 02-16 [國中挑戰]
  {
    "id": "dialogue-0216",
    "date": "02-16",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "植物生長",
    "topic": {
      "en": "Watching Early Cherry Blossoms Unfurl",
      "zh": "春意初現：校園粉嫩吉野櫻初綻花苞"
    },
    "situation": "下課走到學校操場旁的花圃，Hannah 和 Max 驚喜發現櫻花樹頂端綻放出了今年春天的第一朵淡粉紅花朵。",
    "speakers": {
      "Hannah": { "role": "Hannah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Max": { "role": "Max", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0216.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Hannah", "avatar": "👧", "en": "Max, look up at the cherry tree beside the running track! The bare branches are bursting with pink dots!", "zh": "Max，抬頭看操場跑道旁的櫻花樹！光禿禿的樹枝上正冒出滿滿的粉紅色小點點！", "keywords": ["cherry tree", "branches"] },
      { "id": 2, "speaker": "Max", "avatar": "👦", "en": "The first wave of Yoshino cherry blossoms is beginning to unfurl! Five delicate pale pink petals!", "zh": "第一波吉野櫻花正開始悄悄展開了！五片嬌嫩的淡粉色小花瓣！", "keywords": ["petals", "unfurl", "Yoshino"] },
      { "id": 3, "speaker": "Hannah", "avatar": "👧", "en": "Cherry blossoms bloom before their leaves even emerge; why does that evolutionary sequence happen?", "zh": "櫻花居然在長出綠葉之前就先開滿花了；為什麼會有這種先花後葉的演化順序呢？", "keywords": ["sequence", "evolutionary"] },
      { "id": 4, "speaker": "Max", "avatar": "👦", "en": "Without dense foliage in the way, pollinators like honeybees can spot the nectar-rich flowers from miles away!", "zh": "因為沒有茂密葉子遮擋，像蜜蜂這樣的傳粉昆蟲老遠就能看見富含花蜜的花朵！", "keywords": ["pollinators", "foliage", "nectar"] },
      { "id": 5, "speaker": "Hannah", "avatar": "👧", "en": "Brilliant natural design. Seeing cherry blossoms means warm spring is truly around the corner!", "zh": "精妙的大自然設計。看見櫻花盛開，代表溫暖的春天真的就在眼前了！", "keywords": ["around the corner", "blossoms"] }
    ],
    "vocabulary": [
      { "word": "unfurl", "phonetic": "/ʌnˈfɝːl/", "pos": "v.", "zh": "（花朵、旗幟）綻放展開、舒展開來", "example": "Morning sunlight encouraged roses to unfurl." },
      { "word": "foliage", "phonetic": "/ˈfoʊ.li.ɪdʒ/", "pos": "n.", "zh": "（植物的）樹葉、枝葉總稱", "example": "Dense autumn foliage painted the hillside scarlet." },
      { "word": "pollinator", "phonetic": "/ˈpɑː.lə.neɪ.t̬ɚ/", "pos": "n.", "zh": "傳粉昆蟲、授粉者", "example": "Bees and butterflies are indispensable pollinators." }
    ],
    "dailyPhrase": { "en": "Right around the corner.", "zh": "就在眼前、即將到來。" },
    "cultureTip": "櫻花「先花後葉」是許多落葉果樹的特有適應機制，二月中下旬台灣山櫻花（Formosan Cherry）與吉野櫻陸續進入盛開季。"
  },

  # 02-17 [國小初階]
  {
    "id": "dialogue-0217",
    "date": "02-17",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "自然觀察",
    "topic": {
      "en": "Planting Sunflower Seeds in Peat Pots",
      "zh": "在泥炭小花盆裡播下向日葵種子"
    },
    "situation": "自然課上，Sam 和 Eric 穿著小圍裙，把黑色帶白條紋的向日葵種子輕輕埋進濕潤的培養土裡。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Eric": { "role": "Eric", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0217.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Eric, fill your small peat pot with rich brown potting soil up to the rim!", "zh": "Eric，用營養豐富的深褐色培養土把你的泥炭小花盆裝到九分滿！", "keywords": ["peat pot", "soil", "rim"] },
      { "id": 2, "speaker": "Eric", "avatar": "👦", "en": "Poke a hole with your pinky finger about one inch deep right in the middle.", "zh": "用小拇指在正中央戳一個大約一英吋深的小洞。", "keywords": ["pinky", "hole"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Drop two striped sunflower seeds pointy-end down, and tuck the soil over them like a blanket.", "zh": "把兩顆帶條紋的向日葵種子尖頭朝下放進去，像蓋被子一樣把泥土輕輕蓋上。", "keywords": ["sunflower seeds", "pointy-end"] },
      { "id": 4, "speaker": "Eric", "avatar": "👦", "en": "Spritz with this water spray bottle so the soil is damp, but not soaked and soggy.", "zh": "用這支噴霧水瓶噴水，讓泥土保持濕潤，但不要積水泡得爛爛的。", "keywords": ["spritz", "damp", "soggy"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Place our pots on the sunny windowsill. In seven days, tiny green sprouts will say hello!", "zh": "把花盆放在陽光充足的窗台上。七天後，微小的綠芽就會探頭打招呼囉！", "keywords": ["windowsill", "sprouts"] }
    ],
    "vocabulary": [
      { "word": "spritz", "phonetic": "/sprɪts/", "pos": "v./n.", "zh": "噴灑、輕微噴水", "example": "Spritz the ferns with cool water daily." },
      { "word": "damp", "phonetic": "/dæmp/", "pos": "adj.", "zh": "潮濕的、微濕潤的", "example": "Seeds germinate best in damp, aerated soil." },
      { "word": "sprout", "phonetic": "/spraʊt/", "pos": "n./v.", "zh": "新芽、幼苗、發芽", "example": "Green bean sprouts poked through the soil overnight." }
    ],
    "dailyPhrase": { "en": "Say hello to the world.", "zh": "探出頭來向世界打招呼（形容種子破土發芽）" },
    "cultureTip": "春季播種（Spring Planting）是小學自然科學啟蒙最經典的實作，讓孩子觀察種子在水分、溫度與氧氣作用下的發芽生命奇蹟。"
  },

  # 02-18 [高中進階]
  {
    "id": "dialogue-0218",
    "date": "02-18",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "哲學與社會學",
    "topic": {
      "en": "Altruism and the Warm Glow Effect",
      "zh": "利他主義的演化之美：為什麼幫助他人能帶來深層幸福感？"
    },
    "situation": "高中社會學研討會上，Grace 與 Leo 探討經濟學與神經科學中的「溫暖光暈效應（Warm Glow Effect）」以及純粹利他與演化互惠的本質。",
    "speakers": {
      "Grace": { "role": "Grace", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" },
      "Leo": { "role": "Leo", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0218.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Grace", "avatar": "👩", "en": "Leo, classical economics assumes humans are strictly rational utility-maximizers driven purely by self-interest. How does modern science explain genuine philanthropy?", "zh": "Leo，古典經濟學假設人類是純粹受自利驅動的理性自私效用最大化者。那現代科學如何解釋純粹的利他慈善行為？", "keywords": ["economics", "philanthropy", "self-interest"] },
      { "id": 2, "speaker": "Leo", "avatar": "🧑", "en": "Economist James Andreoni coined the 'Warm Glow Effect'. Prosocial giving activates neurobiological reward circuits just like eating delicious food.", "zh": "經濟學家 Andreoni 提出了著名的『溫暖光暈效應』。親社會的付出與利他餽贈，能激活與享用美食完全相同的大腦神經回饋獎賞迴路。", "keywords": ["Warm Glow", "circuits", "prosocial"] },
      { "id": 3, "speaker": "Grace", "avatar": "👩", "en": "So evolutionary biology hardwired altruism into our DNA because tribal cooperation ensured collective survival across millennia?", "zh": "所以演化生物學早已把利他本能編寫進了我們的 DNA，因為數萬年來部落的團結互助保障了群體的共同存活？", "keywords": ["altruism", "hardwired", "cooperation"] },
      { "id": 4, "speaker": "Leo", "avatar": "🧑", "en": "Precisely. Oxytocin and endorphins flood the brain during cooperative acts, biologically incentivizing empathy over ruthless exploitation.", "zh": "正是如此。在合作互助時，大腦會分泌催產素與腦內啡，從生理機制上獎勵同理心，抑制殘酷的零和自私剝削。", "keywords": ["oxytocin", "empathy", "incentivizing"] },
      { "id": 5, "speaker": "Grace", "avatar": "👩", "en": "Therefore, compassion is not a naive social construct, but humanity's most sophisticated evolutionary superpower.", "zh": "因此，同理與慈悲絕非天真單純的道德教條，而是人類演化歷程中最精緻強大的終極超能力。", "keywords": ["compassion", "sophisticated"] }
    ],
    "vocabulary": [
      { "word": "altruism", "phonetic": "/ˈæl.tru.ɪ.zəm/", "pos": "n.", "zh": "利他主義、無私奉獻", "example": "True altruism involves sacrifice without expecting reciprocal gain." },
      { "word": "prosocial", "phonetic": "/proʊˈsoʊ.ʃəl/", "pos": "adj.", "zh": "親社會的、有助社會和諧的", "example": "Volunteering cultivates prosocial empathy in teenagers." },
      { "word": "oxytocin", "phonetic": "/ˌɑːk.səˈtoʊ.sɪn/", "pos": "n.", "zh": "催產素（促進信任與愛的腦神經荷爾蒙）", "example": "Hugging loved ones stimulates soothing oxytocin release." }
    ],
    "dailyPhrase": { "en": "Warm glow effect.", "zh": "溫暖光暈效應（助人時內心湧現的純粹溫暖幸福感）" },
    "cultureTip": "經濟學家 James Andreoni 於 1989 年提出「Warm-Glow Giving」理論，證實人類幫助他人時即使不圖回報，內心依然會獲得深刻的「內在自我肯定感」。"
  },

  # 02-19 [國小中高]
  {
    "id": "dialogue-0219",
    "date": "02-19",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "趣味節氣",
    "topic": {
      "en": "Rain Water: The Second Solar Term Arrives",
      "zh": "雨水節氣：草木萌動春雨潤物細無聲"
    },
    "situation": "午後自然課時窗外飄起綿綿細雨，Ken 和 Emma 站在窗邊，聽著輕柔雨聲觀察葉片上的雨珠。",
    "speakers": {
      "Ken": { "role": "Ken", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0219.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ken", "avatar": "👦", "en": "Emma, listen to that gentle pitter-patter sound against the window glass! Spring rain has arrived.", "zh": "Emma，聽那打在窗戶玻璃上溫柔的淅淅瀝瀝聲！春雨悄悄降臨了。", "keywords": ["pitter-patter", "spring rain"] },
      { "id": 2, "speaker": "Emma", "avatar": "👧", "en": "Today on the traditional lunar calendar is 'Rain Water' (Yushui), the second solar term of the year.", "zh": "今天在農曆節氣裡是『雨水』，是整年當中的第二個節氣呢。", "keywords": ["Rain Water", "solar term"] },
      { "id": 3, "speaker": "Ken", "avatar": "👦", "en": "As freezing winter blizzards stop, temperatures rise, and snowfall turns into gentle nourishing drizzle.", "zh": "隨著酷寒暴風雪停止、氣溫回升，天上的降雪就轉化成了溫柔滋潤大地的濛濛細雨。", "keywords": ["nourishing", "drizzle"] },
      { "id": 4, "speaker": "Emma", "avatar": "👧", "en": "Look at the thirsty grass lawn drinking up every raindrop! The poet Du Fu wrote: 'It moistens all things softly and silently.'", "zh": "看乾渴的草皮正咕嚕咕嚕喝著每一滴雨珠！大詩人杜甫寫過：『潤物細無聲』。", "keywords": ["moistens", "silently"] },
      { "id": 5, "speaker": "Ken", "avatar": "👦", "en": "Spring rain is as precious as pure cooking oil for growing crops. Soon the whole world will be vibrant emerald green!", "zh": "春雨貴如油！很快整個世界就要被染成生機盎然的翠綠色了！", "keywords": ["emerald", "crops", "precious"] }
    ],
    "vocabulary": [
      { "word": "pitter-patter", "phonetic": "/ˌpɪt̬.ɚˈpæt̬.ɚ/", "pos": "n.", "zh": "淅淅瀝瀝的輕敲聲（雨聲或小腳步聲）", "example": "The pitter-patter of raindrops soothed her to sleep." },
      { "word": "drizzle", "phonetic": "/ˈdrɪz.əl/", "pos": "n./v.", "zh": "濛濛細雨、下毛毛雨", "example": "A misty drizzle fell across the foggy harbour." },
      { "word": "emerald", "phonetic": "/ˈem.rəld/", "pos": "n./adj.", "zh": "祖母綠、翠綠色的", "example": "The valley sparkled in brilliant emerald hues." }
    ],
    "dailyPhrase": { "en": "Moisten all things silently.", "zh": "潤物細無聲（形容細雨或師恩無聲滋養）" },
    "cultureTip": "「雨水（Rain Water）」是二十四節氣之二，意味著氣溫回暖、冰雪融化為降雨，農諺有「春雨貴如油」之說，大自然草木破土生機盎然。"
  },

  # 02-20 [國中挑戰]
  {
    "id": "dialogue-0220",
    "date": "02-20",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "體育健康",
    "topic": {
      "en": "Fitness Testing: The 800-Meter Endurance Run",
      "zh": "開學體適能測驗：八百公尺耐力跑配速技巧"
    },
    "situation": "體育課操場跑道上，Kevin 和同學 David 正在做拉筋伸展，討論等等體適能 800 公尺跑步的呼吸節奏與過彎配速。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "🧑", "gender": "male", "voice": "en-US-ChristopherNeural" },
      "David": { "role": "David", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0220.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "🧑", "en": "David, our physical fitness assessment is starting! The dreaded 800-meter run is up next.", "zh": "David，我們的體適能測驗開始了！大家最害怕的八百公尺跑馬上就要登場。", "keywords": ["fitness", "assessment"] },
      { "id": 2, "speaker": "David", "avatar": "👦", "en": "Don't sprint out of the gate like a bullet, Kevin! Rookie runners burn out their glycogen in the first two hundred meters.", "zh": "起跑時千萬不要像子彈一樣死命狂衝 Kevin！新手常常在前兩百公尺就把肌醣耗盡累癱了。", "keywords": ["glycogen", "sprint", "burn out"] },
      { "id": 3, "speaker": "Kevin", "avatar": "🧑", "en": "Right. Pacing is key. Maintain a steady cadence: breathe in twice through the nose, exhale twice through the mouth.", "zh": "對，配速才是王道。維持平穩節奏：兩步鼻吸、兩步口吐氣。", "keywords": ["pacing", "cadence", "exhale"] },
      { "id": 4, "speaker": "David", "avatar": "👦", "en": "Draft behind the lead group around the bends to reduce aerodynamic drag, then unleash your final kick in the home stretch!", "zh": "過彎道時跟在領跑集團後面減少風阻，等到最後直線一百公尺再全力衝刺！", "keywords": ["aerodynamic", "home stretch", "unleash"] },
      { "id": 5, "speaker": "Kevin", "avatar": "🧑", "en": "Focus on our own internal tempo, not what other runners are doing. Ready? On your marks, set... Go!", "zh": "專注在我們自己的內在步頻節奏上，不要被別人帶著亂跑。各就各位、預備…跑！", "keywords": ["tempo", "on your marks"] }
    ],
    "vocabulary": [
      { "word": "cadence", "phonetic": "/ˈkeɪ.dəns/", "pos": "n.", "zh": "步頻、節奏韻律", "example": "Distance runners maintain an efficient stride cadence." },
      { "word": "aerodynamic", "phonetic": "/ˌer.oʊ.daɪˈnæm.ɪk/", "pos": "adj.", "zh": "空氣動力的、流線型減阻的", "example": "Cyclists wear sleek aerodynamic helmets." },
      { "word": "home stretch", "phonetic": "/ˌhoʊm ˈstretʃ/", "pos": "n.", "zh": "最後衝刺階段、終點直線跑道", "example": "We are entering the home stretch of the school semester." }
    ],
    "dailyPhrase": { "en": "In the home stretch.", "zh": "進入最後衝刺階段（比賽或專案即將抵達終點）" },
    "cultureTip": "中學體適能「800/1600 公尺跑走」考驗心肺耐力，運動生理學強調掌握「Negative Splits（後段比前段更快的均勻配速）」才能跑出最優成績。"
  },

  # 02-21 [國小初階]
  {
    "id": "dialogue-0221",
    "date": "02-21",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "同儕互動",
    "topic": {
      "en": "Welcoming the New Transfer Student",
      "zh": "熱情歡迎新學期轉學來的新同學"
    },
    "situation": "開學第二週早晨，班上來了一位從外縣市轉來的新同學 Alex，Anna 和弟弟 Tim 在下課時主動上前打招呼帶他熟悉環境。",
    "speakers": {
      "Anna": { "role": "Anna", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Tim": { "role": "Tim", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0221.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Anna", "avatar": "👧", "en": "Hi Alex! Welcome to Class 3A! My name is Anna, and this is my brother Tim.", "zh": "嗨 Alex！歡迎來到三年 A 班！我叫 Anna，這是我弟弟 Tim。", "keywords": ["welcome", "Class 3A"] },
      { "id": 2, "speaker": "Tim", "avatar": "👦", "en": "Starting at a new school can feel a little nervous, but everyone here is super friendly!", "zh": "剛轉來新學校可能會有一點點緊張，但我們班大家都超級友善喔！", "keywords": ["nervous", "friendly"] },
      { "id": 3, "speaker": "Anna", "avatar": "👧", "en": "Do you want us to show you where the water fountain, library, and cafeteria are?", "zh": "你想讓我們帶你看看飲水機、圖書館和學生餐廳在哪裡嗎？", "keywords": ["fountain", "cafeteria"] },
      { "id": 4, "speaker": "Tim", "avatar": "👦", "en": "And you can sit with us at lunch today! We're having delicious sweet and sour pork ribs!", "zh": "今天中午你可以跟我們坐在一起吃午餐！今天營養午餐有超好吃的糖醋排骨喔！", "keywords": ["pork ribs", "lunch"] },
      { "id": 5, "speaker": "Anna", "avatar": "👧", "en": "A warm smile turns a stranger into an instant friend! We're so glad you're here, Alex!", "zh": "一個溫暖的微笑能把陌生人瞬間變成好朋友！我們好高興你轉來我們班喔 Alex！", "keywords": ["stranger", "instant friend"] }
    ],
    "vocabulary": [
      { "word": "fountain", "phonetic": "/ˈfaʊn.tən/", "pos": "n.", "zh": "噴泉、飲水機（Water fountain）", "example": "Refill your reusable bottle at the drinking fountain." },
      { "word": "cafeteria", "phonetic": "/ˌkæf.əˈtɪr.i.ə/", "pos": "n.", "zh": "學校或公司自助餐廳", "example": "Students gathered in the noisy, cheerful cafeteria." },
      { "word": "instant", "phonetic": "/ˈɪn.stənt/", "pos": "adj.", "zh": "立即的、瞬間的", "example": "Their mutual love for books created an instant bond." }
    ],
    "dailyPhrase": { "en": "Feel right at home.", "zh": "感覺像在自己家一樣自在溫暖。" },
    "cultureTip": "西方學校常設立「Buddy System（學長姐小天使制度）」，指派熱情同學陪伴轉學生一至兩週，協助快速融入新班級與校園生活。"
  },

  # 02-22 [高中進階]
  {
    "id": "dialogue-0222",
    "date": "02-22",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "批判性思維",
    "topic": {
      "en": "Confirmation Bias in Social Media Algorithms",
      "zh": "走出資訊同溫層：社群演算法下的確認偏誤思辨"
    },
    "situation": "高中公民與數位素養課上，Jason 和 Chloe 探討社群平台推薦機制如何強化「確認偏誤（Confirmation Bias）」，以及如何建立客觀批判性思考體系。",
    "speakers": {
      "Jason": { "role": "Jason", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0222.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Jason", "avatar": "🧑", "en": "Chloe, whenever I browse my feed, literally every commentator echoes the exact viewpoints I already agree with. It feels validating, yet unsettling.", "zh": "Chloe，每當我滑社群動態，幾乎所有評論員都在重複跟我原本就認同的一模一樣的觀點。這讓人覺得被肯定，卻又隱隱不安。", "keywords": ["validating", "commentator", "echoes"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👩", "en": "That's an algorithmic echo chamber exploiting our evolutionary 'confirmation bias'—our cognitive tendency to embrace flattering data while discarding opposing evidence.", "zh": "那是演算法同溫層在利用我們與生俱來的『確認偏誤』——我們總是傾向擁抱迎合自己立場的數據，而直接忽視反面證據。", "keywords": ["echo chamber", "confirmation bias", "discarding"] },
      { "id": 3, "speaker": "Jason", "avatar": "🧑", "en": "Algorithms don't optimize for objective truth; they optimize for screen engagement, and outrage delivers the highest click-through dopamine.", "zh": "演算法優化的不是客觀真理，而是螢幕停留時長；而激化憤怒恰恰能帶來最高的點閱率與多巴胺刺激。", "keywords": ["outrage", "engagement", "optimize"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👩", "en": "To cultivate intellectual integrity, we must deliberately seek out steel-manned arguments from the other side and interrogate our own assumptions.", "zh": "要培養真正的心智求真素養，我們必須主動去尋找對立陣營最強有力的論點（鋼人論證），並反覆質疑我們自己的既定假設。", "keywords": ["steel-manned", "interrogate", "assumptions"] },
      { "id": 5, "speaker": "Jason", "avatar": "🧑", "en": "True intelligence isn't having answers that confirm what you already believe, but having the courage to change your mind when facts evolve.", "zh": "真正的智慧不是擁有能印證你原有偏見的答案，而是當事實改變時，具備修正自己觀點的勇氣。", "keywords": ["intelligence", "courage"] }
    ],
    "vocabulary": [
      { "word": "confirm", "phonetic": "/kənˈfɝːm/", "pos": "v.", "zh": "證實、確認", "example": "Lab experiments confirmed the chemical hypothesis." },
      { "word": "interrogate", "phonetic": "/ɪnˈter.ə.ɡeɪt/", "pos": "v.", "zh": "審訊、深刻質疑詰問", "example": "Good journalists interrogate surface claims rigorously." },
      { "word": "assumption", "phonetic": "/əˈsʌmp.ʃən/", "pos": "n.", "zh": "假設、預設立場", "example": "Questioning basic assumptions sparks revolutionary innovation." }
    ],
    "dailyPhrase": { "en": "Echo chamber.", "zh": "同溫層、回音室效應（只聽得到相同聲音的閉塞環境）" },
    "cultureTip": "「Steel-manning（鋼人論證）」是批判性思考的核心：不攻擊對手最脆弱的稻草人論點，而是全力幫對手建立最強有力的論證再來檢驗真偽，被視為最高階的理性素養。"
  },

  # 02-23 [國小中高]
  {
    "id": "dialogue-0223",
    "date": "02-23",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "社團活動",
    "topic": {
      "en": "Joining the School Science Olympiad Club",
      "zh": "加入學校科學奧林匹亞實驗探索社"
    },
    "situation": "社團博覽會攤位前，Emma 和 Lucas 拿著社團簡章，看著桌上冒著白煙的乾冰實驗與自製投石機模型。",
    "speakers": {
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0223.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Emma", "avatar": "👧", "en": "Lucas, look at the Science Olympiad booth! They built a miniature wooden catapult launching ping-pong balls into a bucket!", "zh": "Lucas，快看科學奧林匹亞社的攤位！他們做了一座迷你木質投石機，正把乒乓球精準射進水桶裡！", "keywords": ["catapult", "miniature"] },
      { "id": 2, "speaker": "Lucas", "avatar": "👦", "en": "And look at that beaker of purple cabbage indicator liquid turning fiery red when vinegar is added!", "zh": "還有看那個燒杯裡的紫甘藍指示劑，一滴入醋就瞬間變成熱烈的鮮紅色！", "keywords": ["indicator", "vinegar", "beaker"] },
      { "id": 3, "speaker": "Emma", "avatar": "👧", "en": "The club president said members compete in hands-on building challenges, forensics mystery solving, and astronomy quizzes.", "zh": "社長說社員會參加動手工程搭建競賽、鑑識科學解謎推理，還有天文闖關測驗耶。", "keywords": ["forensics", "astronomy", "challenges"] },
      { "id": 4, "speaker": "Lucas", "avatar": "👦", "en": "Sign our names on the registration sheet right now! Science isn't just dry textbook formulas; it's active discovery!", "zh": "立刻在報名表上簽名吧！科學才不只是乾巴巴的課本公式，而是一場場主動的探索發現！", "keywords": ["registration", "formulas"] },
      { "id": 5, "speaker": "Emma", "avatar": "👧", "en": "Put on safety goggles and grab a lab coat! Our junior scientist journey begins this Friday!", "zh": "戴上護目鏡、穿好實驗袍！我們的少年科學家之旅這週五正式啟航！", "keywords": ["goggles", "lab coat"] }
    ],
    "vocabulary": [
      { "word": "catapult", "phonetic": "/ˈkæt̬.ə.pʌlt/", "pos": "n./v.", "zh": "彈射器、投石機、發射", "example": "The wooden catapult launched foam balls across the gym." },
      { "word": "forensics", "phonetic": "/fəˈren.zɪks/", "pos": "n.", "zh": "鑑識科學、法醫破案學", "example": "DNA forensics helped detectives solve the cold case." },
      { "word": "formula", "phonetic": "/ˈfɔːr.mjə.lə/", "pos": "n.", "zh": "配方、公式方程式", "example": "Apply the mathematical formula to calculate velocity." }
    ],
    "dailyPhrase": { "en": "Hands-on discovery.", "zh": "動手做探索、從實踐中發現真知。" },
    "cultureTip": "「Science Olympiad（科學奧林匹亞競賽）」是北美極具代表性的跨學科科技競賽，融合了水火箭、橋樑承重、化學分析等多項動手實作任務。"
  },

  # 02-24 [國中挑戰]
  {
    "id": "dialogue-0224",
    "date": "02-24",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "校園合作",
    "topic": {
      "en": "Forming a Study Group for History and Science",
      "zh": "組建跨科學習讀書會：相互提問加深記憶"
    },
    "situation": "圖書館討論區裡，Tyler 和表姐 Zoe 召集兩位同班好友，制定本學期每週二放學後的定期讀書會公約。",
    "speakers": {
      "Tyler": { "role": "Tyler", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0224.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tyler", "avatar": "👦", "en": "Zoe, studying alone at your bedroom desk often leads to mindless social media scrolling after thirty minutes.", "zh": "Zoe，一個人在房間書桌前悶頭苦讀，常常讀了三十分鐘就忍不住開始無意識滑手機。", "keywords": ["mindless", "studying alone"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "That's why our four-person study group is a game-changer! Mutual peer accountability keeps everyone locked in.", "zh": "這就是為什麼我們四人讀書會是改變局面的關鍵！同儕之間的相互監督能讓大家專心致志。", "keywords": ["accountability", "locked in"] },
      { "id": 3, "speaker": "Tyler", "avatar": "👦", "en": "Let's adopt the Feynman Technique: each of us prepares to explain one complex topic in simple language without jargon.", "zh": "我們來採用費曼學習法：每個人準備用最簡單大白話解釋一個複雜觀念，絕不用艱澀術語。", "keywords": ["Feynman", "jargon"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "I'll teach cellular respiration mechanisms, and you can explain the economic causes of the Industrial Revolution.", "zh": "我來教細胞呼吸作用的機轉，你來解釋工業革命背後的經濟驅動因素。", "keywords": ["respiration", "Industrial Revolution"] },
      { "id": 5, "speaker": "Tyler", "avatar": "👦", "en": "Teaching someone else is the ultimate litmus test of true understanding. When one teaches, two learn!", "zh": "教導別人正是檢驗自己是否真正徹底理解的終極試金石。一人教，兩人學！", "keywords": ["litmus test", "understanding"] }
    ],
    "vocabulary": [
      { "word": "accountability", "phonetic": "/əˌkaʊn.t̬əˈbɪl.ə.t̬i/", "pos": "n.", "zh": "負責義務、監督約束力", "example": "Study partners provide mutual accountability." },
      { "word": "jargon", "phonetic": "/ˈdʒɑːr.ɡən/", "pos": "n.", "zh": "專門術語、行話黑話", "example": "Explain science concepts clearly without confusing jargon." },
      { "word": "litmus test", "phonetic": "/ˈlɪt.məs ˌtest/", "pos": "n.", "zh": "石蕊試驗、終極檢驗試金石", "example": "Patience under stress is the litmus test of leadership." }
    ],
    "dailyPhrase": { "en": "When one teaches, two learn.", "zh": "教學相長、一人教兩人學（拉丁古諺）" },
    "cultureTip": "「The Feynman Technique（費曼學習法）」由諾貝爾物理獎得主理察·費曼提出：如果你無法用小學生都聽得懂的語言解釋一個概念，說明你還沒真正掌握它。"
  },

  # 02-25 [國小初階]
  {
    "id": "dialogue-0225",
    "date": "02-25",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "春季戶外",
    "topic": {
      "en": "Watching Tadpoles Wiggle in the Pond",
      "zh": "蹲在生態池邊看黑黑圓圓的小蝌蚪游動"
    },
    "situation": "午後校園生態池旁，Sam 和 Eric 蹲在木棧道上，看著池塘淺水邊一群搖著尾巴游來游去的小蝌蚪。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Eric": { "role": "Eric", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0225.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Eric, look down into the shallow sunlit water! Hundreds of tiny black dots are wiggling!", "zh": "Eric，看陽光照亮的淺水裡！好幾百顆微小的黑點點正在扭來扭去！", "keywords": ["shallow", "wiggling", "dots"] },
      { "id": 2, "speaker": "Eric", "avatar": "👦", "en": "Tadpoles! Frog eggs from early spring have finally hatched!", "zh": "是小蝌蚪！早春青蛙媽媽產下的卵終於孵化出來了！", "keywords": ["tadpoles", "hatched"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "They have plump oval heads and slender see-through tails that flutter super fast like tiny propellers.", "zh": "牠們有胖嘟嘟的橢圓形小腦袋，和細長透明的小尾巴，像小螺旋槳一樣拍得飛快。", "keywords": ["oval", "propellers", "slender"] },
      { "id": 4, "speaker": "Eric", "avatar": "👦", "en": "Soon their back legs will sprout, their tails will shrink, and ribbit! They will become green tree frogs!", "zh": "不久之後牠們的後腿就會長出來，尾巴慢慢縮排消失，呱呱！就會變成綠色小樹蛙了！", "keywords": ["sprout", "ribbit", "tree frogs"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Metamorphosis is pure biological magic! Keep swimming safely, little tadpoles!", "zh": "完全變態發育真是純粹的生物魔法！小蝌蚪們，平平安安長大游吧！", "keywords": ["metamorphosis", "magic"] }
    ],
    "vocabulary": [
      { "word": "tadpole", "phonetic": "/ˈtæd.poʊl/", "pos": "n.", "zh": "蝌蚪", "example": "Tadpoles swam among the duckweed plants." },
      { "word": "metamorphosis", "phonetic": "/ˌmet̬.əˈmɔːr.fə.sɪs/", "pos": "n.", "zh": "變態發育、蛻變", "example": "The caterpillar underwent metamorphosis into a butterfly." },
      { "word": "propeller", "phonetic": "/prəˈpel.ɚ/", "pos": "n.", "zh": "螺旋槳、推進器", "example": "The small drone buzzed as twin propellers spun." }
    ],
    "dailyPhrase": { "en": "Wiggle around.", "zh": "扭來扭去、搖曳擺動游動。" },
    "cultureTip": "「Metamorphosis（變態）」是兩棲類動物最迷人的生長歷程：從用鰓呼吸的水棲蝌蚪，經歷長出四肢與肺部發育，蛻變成能在陸地跳躍的成年青蛙。"
  },

  # 02-26 [高中進階]
  {
    "id": "dialogue-0226",
    "date": "02-26",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "歷史與人權",
    "topic": {
      "en": "Transitional Justice and Historical Memory",
      "zh": "歷史記憶與療癒：轉型正義如何撫平集體傷痕？"
    },
    "situation": "二二八和平紀念日前夕，高中歷史與公民研習營上，Marcus 與 Bella 探討「轉型正義（Transitional Justice）」的真相調查、賠償與人權共識建立。",
    "speakers": {
      "Marcus": { "role": "Marcus", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Bella": { "role": "Bella", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0226.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Marcus", "avatar": "🧑", "en": "Bella, with February twenty-eighth approaching, society reflects upon historical wounds. Why is confronting painful pasts essential for a healthy democracy?", "zh": "Bella，隨著二二八紀念日臨近，社會再度反思歷史傷痕。為什麼坦然面對痛苦過去對健全的民主制度如此不可或缺？", "keywords": ["wounds", "approaching", "democracy"] },
      { "id": 2, "speaker": "Bella", "avatar": "👩", "en": "Because genuine reconciliation cannot sprout from enforced amnesia. Transitional justice requires unearthing empirical truth, acknowledging culpability, and restoring victim dignity.", "zh": "因為真正的和解絕不可能發芽於強迫遺忘之上。轉型正義需要挖掘客觀歷史真相、承認責任過失，並恢復受害者的名譽與尊嚴。", "keywords": ["reconciliation", "amnesia", "culpability"] },
      { "id": 3, "speaker": "Marcus", "avatar": "🧑", "en": "Like Germany's post-war 'Vergangenheitsbewältigung'—the deliberate struggle to overcome and learn from past atrocities rather than sweeping them under the rug?", "zh": "就像德國戰後的『克服過去（銘記歷史）』——刻意正視並從過往暴行中汲取教訓，而不是將歷史粉飾遮掩掃入地毯下？", "keywords": ["atrocities", "deliberate"] },
      { "id": 4, "speaker": "Bella", "avatar": "👩", "en": "Precisely. Memorialization is an insurance policy against historical relapse. Teaching these chapters in history curricula inoculates future generations against authoritarian impulses.", "zh": "正是如此。建立歷史紀念是防止歷史悲劇重演的保險單。在課綱中教授這些章節，能為下一代接種抵抗威權獨裁衝動的心理疫苗。", "keywords": ["inoculates", "relapse", "authoritarian"] },
      { "id": 5, "speaker": "Marcus", "avatar": "🧑", "en": "Remembering isn't about perpetuating hatred, but anchoring our shared commitment: never again will basic human rights be compromised.", "zh": "銘記歷史絕非為了延續仇恨，而是為了堅定我們共同的誓言：基本人權永遠不再受到踐踏。", "keywords": ["commitment", "compromised"] }
    ],
    "vocabulary": [
      { "word": "reconciliation", "phonetic": "/ˌrek.ənˌsɪl.iˈeɪ.ʃən/", "pos": "n.", "zh": "和解、修復重歸於好", "example": "Truth commissions pave the difficult road toward national reconciliation." },
      { "word": "amnesia", "phonetic": "/æmˈniː.ʒə/", "pos": "n.", "zh": "失憶、遺忘健忘症", "example": "Societal amnesia risks repeating catastrophic historical errors." },
      { "word": "inoculate", "phonetic": "/ɪˈnɑː.kjə.leɪt/", "pos": "v.", "zh": "給…接種疫苗、給予預防免疫保護", "example": "Critical thinking inoculates citizens against propaganda." }
    ],
    "dailyPhrase": { "en": "Never again.", "zh": "永不再犯、絕不讓悲劇重演（人權紀念最高核心宣言）" },
    "cultureTip": "二二八和平紀念日（Peace Memorial Day）是台灣撫平歷史集體創傷、推動轉型正義與人權教育的國定紀念日，強調「和平、理解與人權保障」。"
  },

  # 02-27 [國小中高]
  {
    "id": "dialogue-0227",
    "date": "02-27",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "春季連假",
    "topic": {
      "en": "Planning a Weekend Bicycle Trail Ride",
      "zh": "規畫二二八連假河濱單車微旅行"
    },
    "situation": "週五放學前，Emma 和哥哥 Lucas 在客廳茶几攤開河濱自行車道地圖，檢查輪胎胎壓與水壺裝備。",
    "speakers": {
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-0227.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Emma", "avatar": "👧", "en": "Lucas, we have a three-day holiday weekend coming up! Let's ride our bicycles along the scenic riverbank trail!", "zh": "Lucas，我們即將迎來三天連假耶！我們沿著風景優美的河濱單車道騎腳踏車吧！", "keywords": ["riverbank", "bicycles"] },
      { "id": 2, "speaker": "Lucas", "avatar": "👦", "en": "Awesome idea! First, safety protocol: check the tire pressure with this floor pump until it reads forty PSI.", "zh": "太棒的主意！首先安全第一步：用這支立式打氣筒檢查輪胎胎壓，打到四十 PSI。", "keywords": ["tire pressure", "pump"] },
      { "id": 3, "speaker": "Emma", "avatar": "👧", "en": "Squeeze both hand brakes firmly to make sure the rubber brake pads grip the wheel rims instantly.", "zh": "用力捏一下兩邊的手煞車，確認橡膠煞車皮能立刻咬緊輪框。", "keywords": ["brakes", "pads"] },
      { "id": 4, "speaker": "Lucas", "avatar": "👦", "en": "Buckle your safety helmet snugly under your chin, and pack two insulated water bottles and trail mix.", "zh": "下巴底下把安全帽扣環扣緊，再帶上兩個保溫水壺和綜合堅果果乾包。", "keywords": ["helmet", "trail mix", "insulated"] },
      { "id": 5, "speaker": "Emma", "avatar": "👧", "en": "Pedaling in the gentle February breeze along blooming wildflowers is the ultimate outdoor rejuvenation!", "zh": "伴隨二月微風在盛開野花旁踩著踏板，真是最棒的戶外身心充電！", "keywords": ["pedaling", "rejuvenation"] }
    ],
    "vocabulary": [
      { "word": "protocol", "phonetic": "/ˈproʊ.t̬ə.kɑːl/", "pos": "n.", "zh": "規程、安全程序規範", "example": "Follow laboratory safety protocols strictly." },
      { "word": "rejuvenation", "phonetic": "/rɪˌdʒuː.vənˈeɪ.ʃən/", "pos": "n.", "zh": "恢復活力、重煥生機", "example": "A brisk nature hike provides mental rejuvenation." },
      { "word": "pedal", "phonetic": "/ˈped.əl/", "pos": "v./n.", "zh": "踩踏板、踏板", "example": "Pedal steadily to maintain momentum up the hill." }
    ],
    "dailyPhrase": { "en": "Safety protocol.", "zh": "安全規範程序。" },
    "cultureTip": "台灣擁有全球聞名的環島與河濱自行車專用道（Cycling Trail Network），春季騎乘單車既環保健康又能盡情飽覽沿途綠意水色。"
  },

  # 02-28 [國中挑戰]
  {
    "id": "dialogue-0228",
    "date": "02-28",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "月結與反思",
    "topic": {
      "en": "February Wrap-Up: Spring Has Officially Knocked",
      "zh": "二月月結：春暖花開，向陽而生"
    },
    "situation": "二月的最後一個傍晚，Leo 和 Zoe 坐在操場草皮看著夕陽，回顧過去一個月元宵的喜慶、新學期的啟動與逐漸溫暖的大地。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-0228.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Zoe, today is February twenty-eighth! The shortest month of the year has flown by in the blink of an eye.", "zh": "Zoe，今天是二月二十八日！全年中天數最短的一個月在轉瞬眨眼間飛逝而過。", "keywords": ["blink of an eye", "February"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "It packed so much warmth: Lantern Festival riddles, Valentine cards, and smoothly launching our new semester.", "zh": "這一個月裝滿了好多溫暖：元宵猜燈謎、情人節友情卡片，還有新學期元氣滿滿的啟動。", "keywords": ["warmth", "launching"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Notice how the evening sun sets much later now? Six o'clock and the sky is still bathed in glowing twilight!", "zh": "注意到現在傍晚太陽下山明顯變晚了嗎？六點鐘了天空依然沐浴在燦爛暮光中！", "keywords": ["twilight", "evening sun"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Tomorrow marks March first! The full splendor of vibrant springtime is about to unveil its green tapestry.", "zh": "明天就正式進入三月一日了！萬紫千紅的春天即將鋪展開整片盎然綠毯。", "keywords": ["splendor", "tapestry", "March"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Goodbye chilly winter, hello flourishing spring! Keep learning, keep smiling, and keep growing tall!", "zh": "別了寒冷的冬日，你好生機盎然的春天！持續學習、保持微笑、勇敢向上成長！", "keywords": ["flourishing", "growing"] }
    ],
    "vocabulary": [
      { "word": "twilight", "phonetic": "/ˈtwaɪ.laɪt/", "pos": "n.", "zh": "暮光、黃昏薄暮", "example": "Bats swooped gracefully through the purple twilight." },
      { "word": "splendor", "phonetic": "/ˈsplen.dɚ/", "pos": "n.", "zh": "壯麗輝煌、璀璨光彩", "example": "The alpine sunrise was an unforgettable splendor." },
      { "word": "flourish", "phonetic": "/ˈflɝː.ɪʃ/", "pos": "v.", "zh": "繁榮昌盛、蓬勃生長", "example": "Creative talents flourish in supportive learning environments." }
    ],
    "dailyPhrase": { "en": "In the blink of an eye.", "zh": "轉眼之間、眨眼功夫。" },
    "cultureTip": "過了 2 月 28 日，天文與氣象意義上的春季（Meteorological Spring）在 3 月 1 日全面展開，日照增長、萬物生長，是迎向希望的季節。"
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
    for new_item in FEBRUARY_DIALOGUES:
        if new_item['date'] not in existing_dates:
            existing.append(new_item)
            existing_dates.add(new_item['date'])
            added_count += 1

    # 按照 MM-DD 排序（01-01, 02-01 ~ 02-28, 09-01 ~ 12-31）
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

    print(f"成功新增 2 月份共 {added_count} 篇對話！目前資料庫總計共有 {len(existing)} 篇對話 (涵蓋 1月、2月、9月、10月、11月、12月共 181 天，已跨越全年度一半！)。")

if __name__ == '__main__':
    main()
