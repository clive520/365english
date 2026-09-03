#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次建立 12 月份生活對話 (12-01 至 12-31，共 31 篇)
涵蓋降雪冬日、佈置聖誕樹、秘密交換禮物、冬至、聖誕大餐與跨年倒數！
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'dialogues.json')

DECEMBER_DIALOGUES = [
  # 12-01 [國小初階]
  {
    "id": "dialogue-1201",
    "date": "12-01",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "節慶倒數",
    "topic": {
      "en": "Opening the Advent Calendar Door",
      "zh": "打開聖誕倒數月曆的第一扇小門"
    },
    "situation": "十二月的第一天早晨，Toby 和妹妹 Zoe 迫不及待地跑到客廳，打開木質倒數月曆上一號的小木門。",
    "speakers": {
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1201.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Toby", "avatar": "👦", "en": "December is finally here! Zoe, it's time to open door number one on our advent calendar!", "zh": "十二月終於到了！Zoe，該來打開我們倒數月曆上的一號小門了！", "keywords": ["December", "advent calendar"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Can I open it? I see a shiny golden knob on the wooden box!", "zh": "可以讓我開嗎？我看見木盒子上有一個閃閃發亮的小金把手！", "keywords": ["knob", "shiny"] },
      { "id": 3, "speaker": "Toby", "avatar": "👦", "en": "Go ahead! Turn the latch gently... What surprise is hiding inside?", "zh": "開吧！輕輕轉動門閂…裡面藏著什麼驚喜呢？", "keywords": ["latch", "surprise"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "A milk chocolate snowman wrapped in silver foil! Yum!", "zh": "是一個包著銀色鋁箔紙的牛奶巧克力小雪人！太棒了！", "keywords": ["chocolate", "snowman"] },
      { "id": 5, "speaker": "Toby", "avatar": "👦", "en": "Twenty-four days until Christmas! The magical holiday countdown officially begins!", "zh": "離聖誕節還有二十四天！神奇的節日倒數正式開始囉！", "keywords": ["countdown", "magical"] }
    ],
    "vocabulary": [
      { "word": "latch", "phonetic": "/lætʃ/", "pos": "n./v.", "zh": "門閂、插銷", "example": "Lift the brass latch to open the garden gate." },
      { "word": "foil", "phonetic": "/fɔɪl/", "pos": "n.", "zh": "金屬箔、鋁箔紙", "example": "Wrap the leftover sandwich in aluminum foil." },
      { "word": "knob", "phonetic": "/nɑːb/", "pos": "n.", "zh": "球形把手、旋鈕", "example": "Turn the doorknob clockwise." }
    ],
    "dailyPhrase": { "en": "The countdown begins!", "zh": "倒數計時正式開始！" },
    "cultureTip": "「Advent Calendar（聖誕倒數月曆）」源自 19 世紀德國，從 12 月 1 日到 24 日每天打開一扇小格子，裡面裝著糖果、巧克力或聖經經文。"
  },

  # 12-02 [國小中高]
  {
    "id": "dialogue-1202",
    "date": "12-02",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "家庭溫馨",
    "topic": {
      "en": "Unpacking Christmas Ornaments",
      "zh": "開箱整理聖誕樹吊飾與彩球"
    },
    "situation": "週六下午在客廳，Lucas 和媽媽從儲藏室搬出大收納箱，整理準備掛上聖誕樹的各色吊飾。",
    "speakers": {
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mom": { "role": "媽媽", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1202.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lucas", "avatar": "👦", "en": "Mom, this cardboard storage box is packed with treasures from last year!", "zh": "媽媽，這個紙收納箱裡裝滿了去年的寶藏耶！", "keywords": ["treasures", "cardboard"] },
      { "id": 2, "speaker": "Mom", "avatar": "👩", "en": "Handle those glass baubles with extreme care, Lucas. They are fragile and shatter easily.", "zh": "拿那些玻璃彩球時要格外小心喔 Lucas，它們很脆弱、一摔就碎。", "keywords": ["baubles", "fragile"] },
      { "id": 3, "speaker": "Lucas", "avatar": "👦", "en": "Look at this handmade clay angel I sculpted back in first grade! Its wing is slightly crooked.", "zh": "看這個我小學一年級捏的手工黏土小天使！它的翅膀有一點點歪歪的。", "keywords": ["sculpted", "crooked"] },
      { "id": 4, "speaker": "Mom", "avatar": "👩", "en": "That makes it even more precious! Every single ornament carries a cherished family memory.", "zh": "那樣反而更珍貴！每一個吊飾都承載著一段值得珍藏的家庭回憶。", "keywords": ["precious", "cherished"] },
      { "id": 5, "speaker": "Lucas", "avatar": "👦", "en": "Let's test the string of warm fairy lights before wrapping them around the tree branches.", "zh": "我們先來測看看這串暖黃小串燈會不會亮，再把它繞在樹枝上吧。", "keywords": ["fairy lights", "branches"] }
    ],
    "vocabulary": [
      { "word": "bauble", "phonetic": "/ˈbɑː.bəl/", "pos": "n.", "zh": "（聖誕樹上的）彩球吊飾", "example": "Glittering red baubles adorned the fir tree." },
      { "word": "fragile", "phonetic": "/ˈfrædʒ.əl/", "pos": "adj.", "zh": "易碎的、脆弱的", "example": "Fragile porcelain teacups require gentle washing." },
      { "word": "cherish", "phonetic": "/ˈtʃer.ɪʃ/", "pos": "v.", "zh": "珍惜、珍愛、銘記在心", "example": "We cherish the moments spent with grandparents." }
    ],
    "dailyPhrase": { "en": "Handle with care.", "zh": "小心輕放、謹慎處理。" },
    "cultureTip": "西方家庭常有收集「Commemorative Ornaments（紀念吊飾）」的傳統，每年添購一個記錄孩子成長、旅行或重要里程碑的吊飾掛在樹上。"
  },

  # 12-03 [國中挑戰]
  {
    "id": "dialogue-1203",
    "date": "12-03",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "班級活動",
    "topic": {
      "en": "Drawing Names for Secret Santa",
      "zh": "班上抽籤準備聖誕交換禮物"
    },
    "situation": "班會課上，班長 Mark 拿著裝滿同學名字紙條的小紅帽，讓 Kelly 和全班同學依序抽籤。",
    "speakers": {
      "Mark": { "role": "Mark", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Kelly": { "role": "Kelly", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1203.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mark", "avatar": "🧑", "en": "Attention class! Shake the Santa hat well before picking a folded slip of paper.", "zh": "全班注意！抽折好的紙條之前先把聖誕帽搖一搖喔。", "keywords": ["Santa hat", "folded"] },
      { "id": 2, "speaker": "Kelly", "avatar": "👧", "en": "Remember the cardinal rule: if you draw your own name, put it right back and redraw immediately!", "zh": "記住最重要的鐵律：如果你抽到自己的名字，要立刻放回去重抽！", "keywords": ["cardinal rule", "redraw"] },
      { "id": 3, "speaker": "Mark", "avatar": "🧑", "en": "And keep your recipient an absolute top-secret mystery until our exchange party on the 23rd.", "zh": "還有在 23 號的交換派對之前，你送禮的對象絕對要保密到家！", "keywords": ["recipient", "mystery"] },
      { "id": 4, "speaker": "Kelly", "avatar": "👧", "en": "What is our agreed price ceiling so nobody feels financial pressure?", "zh": "我們約定的禮物預算上限是多少？這樣大家才不會有金錢壓力。", "keywords": ["price ceiling", "financial"] },
      { "id": 5, "speaker": "Mark", "avatar": "🧑", "en": "Strictly under ten dollars, with bonus points for thoughtful, personalized or handcrafted gifts!", "zh": "嚴格限制在十美元以內，如果是用心、具個人特色或親手製作的禮物會有加分！", "keywords": ["handcrafted", "personalized"] }
    ],
    "vocabulary": [
      { "word": "recipient", "phonetic": "/rɪˈsɪp.i.ənt/", "pos": "n.", "zh": "收件人、接受禮物者", "example": "Write the recipient's full address on the parcel." },
      { "word": "cardinal", "phonetic": "/ˈkɑːr.dɪ.nəl/", "pos": "adj.", "zh": "基本的、首要的、極重要的", "example": "Honesty is a cardinal virtue in any friendship." },
      { "word": "handcrafted", "phonetic": "/ˌhændˈkræf.tɪd/", "pos": "adj.", "zh": "純手工打造的", "example": "She sells beautiful handcrafted leather journals." }
    ],
    "dailyPhrase": { "en": "Price ceiling.", "zh": "價格上限、預算封頂。" },
    "cultureTip": "「Secret Santa（神秘聖誕老人交換禮物）」是全球學校與辦公室最受歡迎的歲末社交遊戲，設定價格上限能避免禮物攀比的尷尬。"
  },

  # 12-04 [高中進階]
  {
    "id": "dialogue-1204",
    "date": "12-04",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "社會經濟學",
    "topic": {
      "en": "The Deadweight Loss of Holiday Gift-Giving",
      "zh": "送禮的經濟學：節慶禮物的無謂損失？"
    },
    "situation": "高中經濟學社團研討會上，Ryan 和 Olivia 討論著名經濟學論文《聖誕節的無謂損失》（The Deadweight Loss of Christmas）。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1204.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "🧑", "en": "Olivia, I read Joel Waldfogel's paper arguing that holiday gift-giving causes severe economic inefficiency, or 'deadweight loss'.", "zh": "Olivia，我讀了經濟學家 Waldfogel 的論文，他主張節日送禮會造成嚴重的經濟無效率，也就是所謂的『無謂損失』。", "keywords": ["deadweight loss", "inefficiency"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👩", "en": "Right, because buyers rarely possess perfect knowledge of the recipient's preferences, leading them to overpay for unwanted items.", "zh": "對，因為送禮者很少完全掌握收禮者的真實偏好，導致花了高價卻買了對方用不上的東西。", "keywords": ["preferences", "unwanted"] },
      { "id": 3, "speaker": "Ryan", "avatar": "🧑", "en": "Economists suggest cash or gift cards are mathematically superior because they allow maximum utility optimization.", "zh": "經濟學家認為給現金或禮品卡在數理上最有效率，因為能讓消費者達到效用最大化。", "keywords": ["optimization", "utility"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👩", "en": "Yet pure financial rationality misses the sociopsychological signal: a tailored physical gift communicates effort, care, and emotional investment.", "zh": "然而純粹的財務理性忽略了社會心理學的訊號：一件精心挑選的實體禮物傳遞的是心力、關懷與情感投入。", "keywords": ["rationality", "investment"] },
      { "id": 5, "speaker": "Ryan", "avatar": "🧑", "en": "True. The value of a gift isn't merely transactional utility, but the enduring relational bond it strengthens.", "zh": "確實如此。禮物的價值絕非僅僅是交易效用，而是它所加固鞏固的深厚人際紐帶。", "keywords": ["transactional", "relational"] }
    ],
    "vocabulary": [
      { "word": "inefficiency", "phonetic": "/ˌɪn.ɪˈfɪʃ.ən.si/", "pos": "n.", "zh": "無效率、浪費", "example": "Outdated software creates workplace inefficiency." },
      { "word": "utility", "phonetic": "/juːˈtɪl.ə.t̬i/", "pos": "n.", "zh": "效用、實用性（經濟學名詞）", "example": "Consumers seek maximum utility within their budget." },
      { "word": "transactional", "phonetic": "/trænˈzæk.ʃən.əl/", "pos": "adj.", "zh": "交易性的、單純事務性的", "example": "True friendship goes far beyond transactional favors." }
    ],
    "dailyPhrase": { "en": "Deadweight loss.", "zh": "無謂損失（經濟學指市場資源配置未能達到帕雷托最優造成的淨損失）" },
    "cultureTip": "耶魯大學經濟學家 Joel Waldfogel 1993 年發表的論文估算，送禮人花費的金額通常高於收禮者對該物品的主觀估值約 10%~30%，引發學界對禮物文化的熱烈思辨。"
  },

  # 12-05 [國小初階]
  {
    "id": "dialogue-1205",
    "date": "12-05",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "冬季大自然",
    "topic": {
      "en": "The First Snowflake of Winter",
      "zh": "飄落手心的第一片小雪花"
    },
    "situation": "下課走到戶外，Mia 突然感覺有涼涼的東西落在臉頰上，抬頭發現天空下起了白雪花。",
    "speakers": {
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1205.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mia", "avatar": "👧", "en": "Leo, look at my black wool coat sleeve! Tiny white stars are dancing down from the gray sky!", "zh": "Leo，快看我的黑呢大衣衣袖！微小的白色小星星正從灰濛濛的天空翩翩跳舞降落！", "keywords": ["snowflake", "sleeve"] },
      { "id": 2, "speaker": "Leo", "avatar": "👦", "en": "Snow! It is the very first snowfall of the winter season!", "zh": "下雪了！這是今年冬天的第一場初雪耶！", "keywords": ["snowfall", "season"] },
      { "id": 3, "speaker": "Mia", "avatar": "👧", "en": "Look closely with this magnifying glass: every snowflake has six delicate crystal arms!", "zh": "用放大鏡仔細看：每一片雪花都有六支精緻的六角水晶冰臂！", "keywords": ["magnifying glass", "crystal"] },
      { "id": 4, "speaker": "Leo", "avatar": "👦", "en": "Did you know that no two snowflakes in the whole world are completely identical?", "zh": "妳知道全世界沒有任何兩片雪花的圖案是一模一樣的嗎？", "keywords": ["identical", "world"] },
      { "id": 5, "speaker": "Mia", "avatar": "👧", "en": "Nature is the greatest ice artist ever! I hope it snows enough to build a giant snowman tomorrow!", "zh": "大自然真是最偉大的冰雪藝術家！真希望下大一點，明天就能堆大雪人了！", "keywords": ["snowman", "artist"] }
    ],
    "vocabulary": [
      { "word": "snowflake", "phonetic": "/ˈsnoʊ.fleɪk/", "pos": "n.", "zh": "雪花、雪片", "example": "A delicate snowflake landed on her woolen scarf." },
      { "word": "identical", "phonetic": "/aɪˈden.t̬ə.kəl/", "pos": "adj.", "zh": "完全相同的、一模一樣的", "example": "The twins wore identical blue jackets." },
      { "word": "crystal", "phonetic": "/ˈkrɪs.təl/", "pos": "n./adj.", "zh": "水晶、晶體", "example": "Ice crystals formed on the frosted window." }
    ],
    "dailyPhrase": { "en": "Dance down from the sky.", "zh": "從空中翩翩降落。" },
    "cultureTip": "水分子因六角形晶格（Hexagonal lattice）排列，所有雪花都嚴格遵循六重對稱性（Six-fold symmetry），在大氣溫度與濕度變化下形成千變萬化的獨特結晶。"
  },

  # 12-06 [國小中高]
  {
    "id": "dialogue-1206",
    "date": "12-06",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "節慶烘焙",
    "topic": {
      "en": "Building a Gingerbread House",
      "zh": "動手搭建糖霜薑餅屋"
    },
    "situation": "週日午後，Sam 和 Emily 正在用烘烤好的薑餅片、黏稠糖霜與七彩軟糖建造夢幻糖果屋。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emily": { "role": "Emily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1206.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Emily, pipe thick royal icing along the edges of the gingerbread walls. Icing acts like edible cement!", "zh": "Emily，沿著薑餅牆壁的邊緣擠上濃厚的皇家糖霜。糖霜就像可以吃的黏著水泥一樣！", "keywords": ["icing", "cement", "gingerbread"] },
      { "id": 2, "speaker": "Emily", "avatar": "👧", "en": "Hold the roof panels steady for thirty seconds until the sugary mortar hardens firmly.", "zh": "把屋頂斜板扶住三十秒不要動，等糖霜灰漿完全凝固變硬。", "keywords": ["mortar", "hardens"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Now for the fun part: decorating! Let's line the roof eaves with white icing icicles.", "zh": "現在來到最好玩的部分：裝飾！我們在屋簷邊緣擠出一排像白雪冰柱一樣的糖霜吧。", "keywords": ["icicles", "eaves"] },
      { "id": 4, "speaker": "Emily", "avatar": "👧", "en": "I'll pave the cobblestone front walkway with rainbow M&M candies and peppermint swirl stepping stones.", "zh": "我用彩虹 M&M 巧克力豆鋪門口小石子路，再用紅白薄荷旋轉糖當踏步石。", "keywords": ["peppermint", "walkway"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "It looks like a fairytale cottage straight out of Hansel and Gretel!", "zh": "看起來簡直就像直接從《糖果屋》童話故事裡走出來的夢幻小屋！", "keywords": ["cottage", "fairytale"] }
    ],
    "vocabulary": [
      { "word": "icing", "phonetic": "/ˈaɪ.sɪŋ/", "pos": "n.", "zh": "糖霜、糖衣", "example": "Spread lemon icing over the warm biscuits." },
      { "word": "icicle", "phonetic": "/ˈaɪ.sɪ.kəl/", "pos": "n.", "zh": "冰柱、垂冰", "example": "Long glistening icicles hung from the wooden roof." },
      { "word": "edible", "phonetic": "/ˈed.ə.bəl/", "pos": "adj.", "zh": "可食用的", "example": "These garden flowers are completely edible." }
    ],
    "dailyPhrase": { "en": "Straight out of a fairytale.", "zh": "如同從童話故事裡走出來一般夢幻。" },
    "cultureTip": "「Gingerbread House（薑餅屋）」源自 16 世紀德國，受格林童話《糖果屋（Hansel and Gretel）》熱潮推動，成為歐美聖誕節最受歡迎的親子手作體驗。"
  },

  # 12-07 [國中挑戰]
  {
    "id": "dialogue-1207",
    "date": "12-07",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "冬日運動",
    "topic": {
      "en": "Gliding on the Outdoor Ice Rink",
      "zh": "在戶外溜冰場感受冰上滑行"
    },
    "situation": "週六下午，Ethan 和同學 Zoe 繫緊冰刀鞋帶，踏上市政廣場中央熱鬧的戶外滑冰場。",
    "speakers": {
      "Ethan": { "role": "Ethan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1207.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ethan", "avatar": "👦", "en": "Zoe, grip my arm! My ankles feel wobbly, and the smooth ice surface is slick as glass!", "zh": "Zoe，快抓緊我的手！我的腳踝搖搖晃晃的，光滑的冰面滑得跟玻璃一樣！", "keywords": ["wobbly", "slick"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Bend your knees slightly and lean your center of gravity forward, Ethan. Don't lean backward!", "zh": "把膝蓋稍微彎曲，重心往前傾，Ethan。千萬不要往後倒！", "keywords": ["gravity", "knees"] },
      { "id": 3, "speaker": "Ethan", "avatar": "👦", "en": "Push off with the inside edge of one blade, then glide on the other... Hey, I'm actually moving smoothly!", "zh": "用一隻冰刀內刃往後蹬，然後另一隻腳往前滑…嘿，我真的開始流暢滑動了！", "keywords": ["blade", "glide"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Look at you go! Feel the crisp winter wind against your cheeks as classic holiday music plays!", "zh": "看你滑得多棒！伴隨著歡樂的聖誕音樂，感受涼爽的冬風拂過臉頰！", "keywords": ["holiday music", "cheeks"] },
      { "id": 5, "speaker": "Ethan", "avatar": "👦", "en": "Ice skating feels just like flying without wings! Let's do another three laps!", "zh": "滑冰的感覺就像沒長翅膀在飛翔一樣！我們再來滑個三圈吧！", "keywords": ["laps", "flying"] }
    ],
    "vocabulary": [
      { "word": "glide", "phonetic": "/ɡlaɪd/", "pos": "v.", "zh": "滑行、滑動", "example": "Swans glide gracefully across the still pond." },
      { "word": "wobbly", "phonetic": "/ˈwɑː.bli/", "pos": "adj.", "zh": "搖晃不穩的、顫巍巍的", "example": "The wooden chair had a wobbly leg." },
      { "word": "slick", "phonetic": "/slɪk/", "pos": "adj.", "zh": "光滑濕滑的", "example": "Rain made the highway dangerously slick." }
    ],
    "dailyPhrase": { "en": "Center of gravity.", "zh": "重心（運動與滑冰時保持平衡的核心）" },
    "cultureTip": "戶外溜冰場（Outdoor Ice Rink）是歐美大城市（如紐約洛克斐勒中心、倫敦索美塞特宮）冬天的著名地標，在巨型聖誕樹下溜冰充滿浪漫節慶氛圍。"
  },

  # 12-08 [高中進階]
  {
    "id": "dialogue-1208",
    "date": "12-08",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "環境與氣候",
    "topic": {
      "en": "The Science of Polar Vortex Disruptions",
      "zh": "極地渦旋崩潰與極端嚴寒的氣候科學"
    },
    "situation": "高中地球科學專題課後，Alex 與 Sophia 探討北極暖化如何導致噴射氣流波動，進而將極地渦旋寒潮送至中低緯度地區。",
    "speakers": {
      "Alex": { "role": "Alex", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Sophia": { "role": "Sophia", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1208.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Alex", "avatar": "🧑", "en": "Sophia, climate deniers often point to severe sub-zero winter blizzards as supposed evidence that global warming is a hoax.", "zh": "Sophia，氣候懷疑論者常把零下幾十度的極端嚴寒暴風雪，拿來當作全球暖化是一場騙局的所謂證據。", "keywords": ["blizzards", "deniers", "hoax"] },
      { "id": 2, "speaker": "Sophia", "avatar": "👩", "en": "Which demonstrates profound scientific illiteracy. The culprit behind sudden deep freezes is polar vortex instability.", "zh": "這正顯示了對大氣科學常識的極度匱乏。導致低緯度劇烈急凍的真正罪魁禍首，是極地渦旋的不穩定失衡。", "keywords": ["culprit", "instability", "illiteracy"] },
      { "id": 3, "speaker": "Alex", "avatar": "🧑", "en": "Because the Arctic is warming three to four times faster than the global average, the temperature gradient weakens?", "zh": "因為北極的暖化速度是全球平均的三到四倍，導致南北溫差梯度大幅減弱？", "keywords": ["gradient", "Arctic"] },
      { "id": 4, "speaker": "Sophia", "avatar": "👩", "en": "Exactly. A weaker temperature contrast destabilizes the high-altitude jet stream, causing it to meander into giant wave lobes that spill freezing Arctic air southward.", "zh": "沒錯。溫差縮小會讓高空噴射氣流減弱蛇行，形成巨大的波浪狀擺動，把北極極寒空氣一口氣向南傾瀉。", "keywords": ["jet stream", "meander"] },
      { "id": 5, "speaker": "Alex", "avatar": "🧑", "en": "So paradoxical winter extremes are direct manifestations of climate disruption, not contradictions to it.", "zh": "因此看似矛盾的極端低溫嚴寒，正是全球氣候失調的直接體現，而非對暖化趨勢的否定。", "keywords": ["manifestations", "paradoxical"] }
    ],
    "vocabulary": [
      { "word": "blizzard", "phonetic": "/ˈblɪz.ɚd/", "pos": "n.", "zh": "暴風雪、大風雪", "example": "The blizzard grounded all commercial flights." },
      { "word": "meander", "phonetic": "/miˈæn.dɚ/", "pos": "v.", "zh": "蜿蜒、曲折蛇行", "example": "The lazy stream meandered across the green valley." },
      { "word": "manifestation", "phonetic": "/ˌmæn.ə.fesˈteɪ.ʃən/", "pos": "n.", "zh": "顯現、具體表現", "example": "Art is a profound manifestation of human creativity." }
    ],
    "dailyPhrase": { "en": "Polar vortex.", "zh": "極地渦旋（盤踞在極地高空旋轉的冷空氣氣旋）" },
    "cultureTip": "「Arctic Amplification（北極放大效應）」指出北極冰層融化減少了反照率（Albedo），吸收更多太陽熱能，反常地加劇了中緯度歐美與東亞冬天的極端氣候。"
  },

  # 12-09 [國小初階]
  {
    "id": "dialogue-1209",
    "date": "12-09",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "動物趣事",
    "topic": {
      "en": "Penguins Waddling on the Ice",
      "zh": "小企鵝在冰面上搖搖擺擺走路"
    },
    "situation": "動物紀錄片課堂上，Ruby 和 Lucas 看到畫面上一群穿著黑燕尾服、挺著大肚子搖晃走路的南極企鵝。",
    "speakers": {
      "Ruby": { "role": "Ruby", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1209.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ruby", "avatar": "👧", "en": "Lucas, look at those emperor penguins on TV! They walk like adorable little gentlemen in tuxedos!", "zh": "Lucas，看電視上那些皇帝企鵝！牠們走起路來像穿著燕尾服的可愛小紳士！", "keywords": ["penguins", "tuxedos"] },
      { "id": 2, "speaker": "Lucas", "avatar": "👦", "en": "They waddle left and right with their flippers spread out for balance!", "zh": "牠們張開短短的小鰭翅維持平衡，左搖一下、右擺一下！", "keywords": ["waddle", "flippers"] },
      { "id": 3, "speaker": "Ruby", "avatar": "👧", "en": "Look! That funny one just flopped onto its belly and is sliding across the slick ice like a sled!", "zh": "快看！那隻搞笑的企鵝直接趴下肚子貼著冰面，像雪橇一樣在光滑的冰上滑行耶！", "keywords": ["sliding", "belly", "sled"] },
      { "id": 4, "speaker": "Lucas", "avatar": "👦", "en": "That sliding move is called 'tobogganing'! It saves them energy when traveling across frozen land.", "zh": "那種滑行動作叫做『雪橇式滑行（Tobogganing）』！在結冰陸地上移動能幫牠們省很多體力。", "keywords": ["tobogganing", "energy"] },
      { "id": 5, "speaker": "Ruby", "avatar": "👧", "en": "I wish I could belly-slide on the ice just like a happy penguin!", "zh": "真希望我也能像快樂的小企鵝一樣趴著肚子溜冰！", "keywords": ["happy", "belly-slide"] }
    ],
    "vocabulary": [
      { "word": "waddle", "phonetic": "/ˈwɑː.dəl/", "pos": "v.", "zh": "（鴨子、企鵝等）搖搖擺擺地走", "example": "Ducks waddled slowly down to the pond." },
      { "word": "flipper", "phonetic": "/ˈflɪp.ɚ/", "pos": "n.", "zh": "（海豹、企鵝等的）鰭肢、鰭翅", "example": "Sea turtles propel themselves with strong flippers." },
      { "word": "toboggan", "phonetic": "/təˈbɑː.ɡən/", "pos": "n./v.", "zh": "平底長雪橇、乘雪橇滑行", "example": "Children loved to toboggan down the snowy hill." }
    ],
    "dailyPhrase": { "en": "Waddle around.", "zh": "搖搖晃晃晃來晃去（形容幼童或企鵝可愛步態）" },
    "cultureTip": "生物學中企鵝用腹部在冰雪表面滑行的行為正式名稱即為「Tobogganing」（來自北美原住民米克馬克語的平底雪橇）。"
  },

  # 12-10 [國小中高]
  {
    "id": "dialogue-1210",
    "date": "12-10",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "校園生活",
    "topic": {
      "en": "Decorating the Classroom Christmas Tree",
      "zh": "全班合力佈置教室聖誕樹"
    },
    "situation": "放學打掃完後，Ben 和 Tina 帶領班上同學一起在教室講台旁組裝人造聖誕樹並掛上發光星星。",
    "speakers": {
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Tina": { "role": "Tina", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1210.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ben", "avatar": "👦", "en": "Tina, fluff out all the green pine branches so the tree looks full and bushy!", "zh": "Tina，把所有綠色松枝撥蓬鬆開來，這樣整棵樹看起來才會又豐滿又茂密！", "keywords": ["fluff", "bushy"] },
      { "id": 2, "speaker": "Tina", "avatar": "👧", "en": "Look at these origami paper cranes our classmates folded! We can hang them with red ribbons.", "zh": "看同學們折的這些紙折千羽鶴！我們可以用紅色緞帶把牠們掛上去。", "keywords": ["origami", "cranes", "ribbons"] },
      { "id": 3, "speaker": "Ben", "avatar": "👦", "en": "Combining Western pine trees with multicultural origami makes our classroom tree one of a kind!", "zh": "把西方聖誕松樹與多元文化的摺紙結合，讓我們的教室聖誕樹獨一無二！", "keywords": ["multicultural", "one of a kind"] },
      { "id": 4, "speaker": "Tina", "avatar": "👧", "en": "Who gets the honor of crowning the very top of the tree with the golden star topper?", "zh": "誰能享有殊榮把閃亮的金色大星星樹頂裝飾戴在最頂端呢？", "keywords": ["crowning", "star topper"] },
      { "id": 5, "speaker": "Ben", "avatar": "👦", "en": "Let's ask Teacher Lin! Plug in the lights... Wow, our classroom feels instantly enchanted!", "zh": "我們請林老師來戴！插上電源小燈泡…哇，我們的教室瞬間充滿了魔法仙境的氛圍！", "keywords": ["plug in", "enchanted"] }
    ],
    "vocabulary": [
      { "word": "origami", "phonetic": "/ˌɔːr.əˈɡɑː.mi/", "pos": "n.", "zh": "摺紙藝術", "example": "Origami develops spatial awareness and hand dexterity." },
      { "word": "topper", "phonetic": "/ˈtɑː.pɚ/", "pos": "n.", "zh": "（樹頂或蛋糕頂部的）頂飾", "example": "A radiant golden angel served as the tree topper." },
      { "word": "enchanted", "phonetic": "/ɪnˈtʃæn.t̬ɪd/", "pos": "adj.", "zh": "如施了魔法般的、著迷陶醉的", "example": "The winter forest looked enchanted under the full moon." }
    ],
    "dailyPhrase": { "en": "One of a kind.", "zh": "獨一無二、絕無僅有。" },
    "cultureTip": "聖誕樹頂端的裝飾（Tree Topper）傳統上為「伯利恆之星（Star of Bethlehem）」或「報喜天使（Herald Angel）」，象徵希望與指引的明燈。"
  },

  # 12-11 [國中挑戰]
  {
    "id": "dialogue-1211",
    "date": "12-11",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "社團學習",
    "topic": {
      "en": "Singing Christmas Carols in the Choir",
      "zh": "合唱團排練經典聖誕頌歌"
    },
    "situation": "音樂教室裡，合唱團員 Mark 和 Kelly 正在跟隨鋼琴伴奏，分部排練四部和聲的經典名曲《平安夜》。",
    "speakers": {
      "Mark": { "role": "Mark", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Kelly": { "role": "Kelly", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1211.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kelly", "avatar": "👧", "en": "Mark, soprano and alto parts are blending nicely, but let's check measure twelve for the baritones.", "zh": "Mark，女高音和女低音聲部融合得很棒，但我們來確認一下第十二小節男中音的音準。", "keywords": ["soprano", "baritone", "measure"] },
      { "id": 2, "speaker": "Mark", "avatar": "🧑", "en": "Right. We were singing slightly flat on the transition to the minor chord. Let me hum the pitch.", "zh": "沒錯。我們在轉折進小和弦時音準有點偏低偏平了。我來哼唱一下那個音高。", "keywords": ["flat", "pitch", "minor chord"] },
      { "id": 3, "speaker": "Kelly", "avatar": "👧", "en": "Much better! 'Silent Night' sounds simple, yet four-part harmony demands impeccable dynamic control.", "zh": "好多了！《平安夜》旋律聽起來簡單，但四部合唱需要無可挑剔的強弱力度控制。", "keywords": ["Silent Night", "harmony", "impeccable"] },
      { "id": 4, "speaker": "Mark", "avatar": "🧑", "en": "Next week our choir will go caroling at the local nursing home and children's hospital ward.", "zh": "下週我們合唱團就要到當地的養老照護中心和兒童醫院病房報佳音了。", "keywords": ["caroling", "nursing home"] },
      { "id": 5, "speaker": "Kelly", "avatar": "👧", "en": "Music has that extraordinary power to bring solace, warmth, and hope during the cold winter.", "zh": "音樂真的具備那種在寒冷冬日裡帶來撫慰、溫暖與希望的非凡力量。", "keywords": ["extraordinary", "warmth"] }
    ],
    "vocabulary": [
      { "word": "harmony", "phonetic": "/ˈhɑːr.mə.ni/", "pos": "n.", "zh": "和聲、和諧融洽", "example": "Vocal harmonies resonated throughout the cathedral." },
      { "word": "impeccable", "phonetic": "/ɪmˈpek.ə.bəl/", "pos": "adj.", "zh": "無可挑剔的、完美的", "example": "Her musical timing and posture were impeccable." },
      { "word": "carol", "phonetic": "/ˈker.əl/", "pos": "n./v.", "zh": "聖誕頌歌、歡唱聖誕歌", "example": "Carolers sang traditional holiday carols door-to-door." }
    ],
    "dailyPhrase": { "en": "Sing slightly flat.", "zh": "唱得偏低了一點（音準略低於標準音高）" },
    "cultureTip": "《Silent Night（平安夜）》於 1818 年由奧地利神父 Joseph Mohr 作詞、Franz Gruber 作曲，已被聯合國教科文組織（UNESCO）列為非物質文化遺產。"
  },

  # 12-12 [高中進階]
  {
    "id": "dialogue-1212",
    "date": "12-12",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "心理學與人文",
    "topic": {
      "en": "Seasonal Affective Disorder and Light Therapy",
      "zh": "冬季憂鬱症（SAD）與光照療法的科學探索"
    },
    "situation": "高中醫學研習社課堂上，Ryan 與 Olivia 就高緯度地區冬季日照銳減引發的「季節性情緒失調（SAD）」進行生理機轉探討。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1212.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "🧑", "en": "Olivia, with the sun setting before five in the afternoon, many of my peers report persistent lethargy and sugar cravings.", "zh": "Olivia，隨著下午不到五點太陽就落山，身邊好多同學都反映持續感到無精打采、而且特別想吃甜食。", "keywords": ["lethargy", "cravings", "persistent"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👩", "en": "That's symptomatic of Seasonal Affective Disorder, appropriately abbreviated as SAD. Diminished sunlight disrupts circadian rhythms.", "zh": "那是季節性情緒失調的典型症狀，縮寫恰好就是 SAD（悲傷）。日照銳減會擾亂我們體內的晝夜生理節律。", "keywords": ["symptomatic", "circadian"] },
      { "id": 3, "speaker": "Ryan", "avatar": "🧑", "en": "Because darkness triggers premature melatonin production while depleting daytime serotonin synthesis?", "zh": "因為天黑提早刺激褪黑激素分泌，同時耗竭了白天維持好心情的血清素合成？", "keywords": ["melatonin", "serotonin"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👩", "en": "Precisely. The first-line clinical intervention is phototherapy: sitting near a 10,000-lux full-spectrum light box for thirty minutes every morning.", "zh": "正是如此。臨床首選介入手段是光照療法：每天早晨坐在發出 10,000 勒克斯的全光譜燈箱旁照光三十分鐘。", "keywords": ["phototherapy", "intervention"] },
      { "id": 5, "speaker": "Ryan", "avatar": "🧑", "en": "Fascinating how directly photons govern human neurochemistry. Taking brisk outdoor lunchtime walks is a simple, cost-free countermeasure.", "zh": "光子居然能如此直接調控人類的大腦神經化學，真不可思議。利用午休時間到戶外快步走曬曬太陽，就是最簡單免費的對策。", "keywords": ["neurochemistry", "countermeasure"] }
    ],
    "vocabulary": [
      { "word": "lethargy", "phonetic": "/ˈleθ.ɚ.dʒi/", "pos": "n.", "zh": "倦怠、無精打采、嗜睡", "example": "Dehydration often manifests as chronic lethargy." },
      { "word": "circadian", "phonetic": "/sɝːˈkeɪ.di.ən/", "pos": "adj.", "zh": "晝夜節律的、二十四小時生理週期的", "example": "Jet lag severely disrupts internal circadian rhythms." },
      { "word": "countermeasure", "phonetic": "/ˈkaʊn.t̬ɚˌmeʒ.ɚ/", "pos": "n.", "zh": "對策、反制措施", "example": "Regular exercise is an effective countermeasure against stress." }
    ],
    "dailyPhrase": { "en": "Circadian rhythm.", "zh": "晝夜生理節律（人體生物鐘）" },
    "cultureTip": "北歐國家（如芬蘭、挪威）冬季日照僅數小時，家戶和學校普遍配置「Light Therapy Box（光療箱）」，被證實對改善冬季憂鬱有顯著療效。"
  },

  # 12-13 [國小初階]
  {
    "id": "dialogue-1213",
    "date": "12-13",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "冬日手作",
    "topic": {
      "en": "Cutting Paper Snowflakes with Scissors",
      "zh": "用安全剪刀剪出精美窗花雪花"
    },
    "situation": "美勞課上，Toby 和妹妹 Zoe 拿著正方形白紙折成小三角形，準備剪出美麗的六角雪花剪紙。",
    "speakers": {
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1213.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Toby", "avatar": "👦", "en": "Zoe, fold this white paper square into a triangle, then fold it twice more!", "zh": "Zoe，把這張白色正方形紙折成三角形，然後再連續對折兩次！", "keywords": ["fold", "triangle"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Like this? Now it looks like a slice of pizza! Where do we snip with the scissors?", "zh": "像這樣嗎？現在看起來像一片披薩！我們要用剪刀剪哪裡呢？", "keywords": ["snip", "scissors"] },
      { "id": 3, "speaker": "Toby", "avatar": "👦", "en": "Snip tiny triangles, diamonds, and curves along the folded edges.", "zh": "沿著折好的側邊剪出微小的三角形、菱形和弧線條。", "keywords": ["diamonds", "curves"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Carefully unfold it... Wow! Look at the lace pattern! It looks like real frozen frost!", "zh": "小心翼翼把它攤開…哇！看這蕾絲花紋！看起來就像真正結在玻璃上的冰霜一樣！", "keywords": ["unfold", "lace pattern"] },
      { "id": 5, "speaker": "Toby", "avatar": "👦", "en": "Let's tape twenty paper snowflakes onto our classroom windows to create an indoor blizzard!", "zh": "我們把二十張剪紙雪花貼在教室窗戶上，打造一個室內冬日雪景吧！", "keywords": ["blizzard", "tape"] }
    ],
    "vocabulary": [
      { "word": "snip", "phonetic": "/snɪp/", "pos": "v./n.", "zh": "（用剪刀）剪下、剪小口", "example": "Snip off the loose thread with small scissors." },
      { "word": "unfold", "phonetic": "/ʌnˈfoʊld/", "pos": "v.", "zh": "攤開、展開", "example": "Unfold the road map across the desk." },
      { "word": "lace", "phonetic": "/leɪs/", "pos": "n.", "zh": "蕾絲、透光花邊", "example": "The curtains had delicate lace trim." }
    ],
    "dailyPhrase": { "en": "Unfold with care.", "zh": "小心翼翼地攤開展開。" },
    "cultureTip": "剪紙雪花（Paper Snowflakes）是西方學校最經典的冬季教室裝飾活動，透過紙張折疊幾何對稱，讓孩子在動手中理解對稱美學。"
  },

  # 12-14 [國中挑戰]
  {
    "id": "dialogue-1214",
    "date": "12-14",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "烘焙美食",
    "topic": {
      "en": "Rolling Out Cinnamon Roll Dough",
      "zh": "廚房飄香：烘烤熱肉桂捲與淋上奶油乳酪霜"
    },
    "situation": "週六早晨，Sarah 和 Jake 在廚房把發酵好的麵團擀平，塗滿奶油黑糖肉桂餡，捲成胖胖的肉桂捲。",
    "speakers": {
      "Sarah": { "role": "Sarah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Jake": { "role": "Jake", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1214.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sarah", "avatar": "👧", "en": "Jake, dust the silicone baking mat with flour so the yeast dough doesn't stick to the rolling pin.", "zh": "Jake，在矽膠烘焙墊上撒點麵粉，這樣發酵麵團才不會黏在擀麵棍上。", "keywords": ["flour", "rolling pin"] },
      { "id": 2, "speaker": "Jake", "avatar": "👦", "en": "Rolled into a broad rectangle! Now spread softened butter generously across the surface.", "zh": "擀成一大張長方形了！現在把軟化奶油大方均勻地塗滿整片表面。", "keywords": ["generously", "rectangle"] },
      { "id": 3, "speaker": "Sarah", "avatar": "👧", "en": "Sprinkle the dark brown sugar and cinnamon mixture evenly, leaving a half-inch border.", "zh": "把黑糖和肉桂粉均勻撒上去，邊緣要留半英吋的封口邊喔。", "keywords": ["border", "cinnamon"] },
      { "id": 4, "speaker": "Jake", "avatar": "👦", "en": "Roll it tightly into a log, slice into twelve rounds with dental floss, and place them in the baking dish!", "zh": "緊緊捲成一根圓柱長條，用乾淨牙線切成十二顆圓捲，排進烤盤裡！", "keywords": ["dental floss", "baking dish"] },
      { "id": 5, "speaker": "Sarah", "avatar": "👧", "en": "While they bake, I'll whip cream cheese glaze. Warm cinnamon rolls on a chilly morning are pure heaven!", "zh": "在烤的時候我來打奶油乳酪淋醬。冷涼的早晨吃上一顆熱騰騰的肉桂捲簡直在天堂！", "keywords": ["glaze", "cream cheese"] }
    ],
    "vocabulary": [
      { "word": "rectangle", "phonetic": "/ˈrek.tæŋ.ɡəl/", "pos": "n.", "zh": "長方形、矩形", "example": "Cut the dough into an even rectangle." },
      { "word": "glaze", "phonetic": "/ɡleɪz/", "pos": "n./v.", "zh": "淋醬、糖漿糖霜、上光", "example": "Drizzle warm vanilla glaze over the pastries." },
      { "word": "generously", "phonetic": "/ˈdʒen.ər.əs.li/", "pos": "adv.", "zh": "大方慷慨地、厚厚一層地", "example": "Spread jam generously over buttered toast." }
    ],
    "dailyPhrase": { "en": "Pure heaven.", "zh": "極致享受、如置身天堂般的幸福美味。" },
    "cultureTip": "烘焙高手切軟生麵團常用無味牙線（Unflavored Dental Floss）交叉收緊切割，比用菜刀更能保持切面圓潤平整不被壓扁！"
  },

  # 12-15 [國小中高]
  {
    "id": "dialogue-1215",
    "date": "12-15",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "動物關懷",
    "topic": {
      "en": "Making Pinecone Bird Feeders",
      "zh": "製作松果鳥食器幫助小鳥過冬"
    },
    "situation": "自然社課上，Leo 和 Emma 拿著撿來的乾燥大松果，塗上花生醬並滾上滿滿鳥飼料穀粒，掛在校園樹枝上。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1215.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Emma, when the ground freezes hard, wild winter birds struggle to dig up seeds or insects.", "zh": "Emma，當土地結凍變硬時，野生冬鳥很難挖到種子或小蟲子吃。", "keywords": ["struggle", "seeds"] },
      { "id": 2, "speaker": "Emma", "avatar": "👧", "en": "That's why we are creating pinecone bird feeders! Tie a sturdy piece of twine around the pinecone top first.", "zh": "這就是為什麼我們要親手做松果鳥食器！先用一條結實的麻繩綁在松果頂部。", "keywords": ["twine", "feeders"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Now smear natural peanut butter into every nook and cranny between the scales with a butter knife.", "zh": "現在用抹刀把天然花生醬抹進松果鱗片之間的每一個縫隙與角落裡。", "keywords": ["smear", "cranny", "scales"] },
      { "id": 4, "speaker": "Emma", "avatar": "👧", "en": "Roll the sticky pinecone in this tray of black sunflower seeds, cracked corn, and millet!", "zh": "把黏答答的松果放進這個裝滿黑葵花子、碎玉米與小米的托盤裡滾一滾！", "keywords": ["sunflower", "millet"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Let's hang them outside our classroom window. Look! A tiny chickadee is already swooping in for lunch!", "zh": "我們把牠們掛在教室窗外吧。快看！一隻小山雀已經拍拍翅膀飛過來吃午餐了！", "keywords": ["chickadee", "swooping"] }
    ],
    "vocabulary": [
      { "word": "twine", "phonetic": "/twaɪn/", "pos": "n.", "zh": "麻線、麻繩", "example": "Tie the bundle of newspapers securely with twine." },
      { "word": "smear", "phonetic": "/smɪr/", "pos": "v.", "zh": "塗抹、厚厚塗上", "example": "Smear cream cheese on the toasted bagel." },
      { "word": "swoop", "phonetic": "/swuːp/", "pos": "v.", "zh": "俯衝、凌空飛撲而下", "example": "The falcon swooped down to catch its prey." }
    ],
    "dailyPhrase": { "en": "Every nook and cranny.", "zh": "每一個角落與縫隙、到處每個細微處。" },
    "cultureTip": "「Pinecone Bird Feeder」是北美經典的冬日環境保育手作，花生醬富含脂肪與蛋白質，為高新陳代謝的越冬小鳥提供救命熱量。"
  },

  # 12-16 [國中挑戰]
  {
    "id": "dialogue-1216",
    "date": "12-16",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "校園生活",
    "topic": {
      "en": "Wearing Ugly Christmas Sweaters",
      "zh": "穿上趣味搞怪聖誕醜毛衣"
    },
    "situation": "週五學校舉辦「Ugly Sweater Day（聖誕醜毛衣日）」，Hannah 和 Max 在走廊看著彼此身上浮誇搞笑的毛衣哈哈大笑。",
    "speakers": {
      "Hannah": { "role": "Hannah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Max": { "role": "Max", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1216.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Hannah", "avatar": "👧", "en": "Max, your sweater is gloriously tacky! Is that a plush 3D reindeer head poking out of your chest?", "zh": "Max，你的毛衣真是俗氣得太精彩了！胸前那是有一隻立體填充馴鹿頭探出來嗎？", "keywords": ["tacky", "plush", "reindeer"] },
      { "id": 2, "speaker": "Max", "avatar": "👦", "en": "Press the reindeer's nose, Hannah! Go ahead, give it a squeeze!", "zh": "按一下馴鹿的紅鼻子，Hannah！快點，用力捏一下試試看！", "keywords": ["squeeze", "press"] },
      { "id": 3, "speaker": "Hannah", "avatar": "👧", "en": "Honk honk! It squeaks like a bicycle horn, and red LEDs are blinking on the antlers!", "zh": "叭叭！它居然像腳踏車喇叭一樣發出叫聲，鹿角上還有紅色 LED 燈在閃爍！", "keywords": ["squeaks", "antlers"] },
      { "id": 4, "speaker": "Max", "avatar": "👦", "en": "And look at yours! Shiny metallic tinsel garlands sewn around green elf shoes with jingle bells!", "zh": "看妳的也不遑多讓！用亮晶晶金蔥彩條圍繞著綠色小精靈鞋，走起路來鈴鐺叮噹響！", "keywords": ["tinsel", "jingle bells"] },
      { "id": 5, "speaker": "Hannah", "avatar": "👧", "en": "Embracing silliness brings so much pure laughter to the end of the semester!", "zh": "大家一起放下包袱搞怪搞笑，為學期末帶來了好多最純粹的歡笑！", "keywords": ["silliness", "laughter"] }
    ],
    "vocabulary": [
      { "word": "tacky", "phonetic": "/ˈtæk.i/", "pos": "adj.", "zh": "俗氣的、廉價誇張的（帶幽默褒義）", "example": "The tourist shop sold delightfully tacky souvenirs." },
      { "word": "antler", "phonetic": "/ˈænt.lɚ/", "pos": "n.", "zh": "（鹿的）鹿角", "example": "The majestic stag grew branching antlers." },
      { "word": "tinsel", "phonetic": "/ˈtɪn.səl/", "pos": "n.", "zh": "（裝飾用的）金蔥彩條、金屬箔條", "example": "Silver tinsel shimmered under the twinkling tree lights." }
    ],
    "dailyPhrase": { "en": "Embrace the silliness.", "zh": "坦然擁抱無厘頭搞笑（享受純粹的快樂）" },
    "cultureTip": "每年 12 月第三個星期五是全美「National Ugly Christmas Sweater Day」，大家爭相穿上毛球、鈴鐺與閃燈誇張毛衣，比比誰最搞怪！"
  },

  # 12-17 [國小初階]
  {
    "id": "dialogue-1217",
    "date": "12-17",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "冬日手作",
    "topic": {
      "en": "Making a Fluffy Cotton Ball Snowman",
      "zh": "動手做蓬鬆棉花球小雪人"
    },
    "situation": "美勞角裡，Sam 和 Eric 正在藍色卡紙上用白膠黏貼棉花球，組裝戴橘色胡蘿蔔鼻子的雪人。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Eric": { "role": "Eric", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1217.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Eric, dip cotton balls into white craft glue! We need one big circle and one small circle.", "zh": "Eric，把棉花球沾上白色手作用白膠！我們需要黏出一個大圓圈和一個小圓圈。", "keywords": ["cotton balls", "glue"] },
      { "id": 2, "speaker": "Eric", "avatar": "👦", "en": "The big cotton circle is the snowman's tummy, and the top is the head!", "zh": "大棉花圈是雪人的胖肚肚，上面的小圈是圓圓的頭！", "keywords": ["tummy", "circle"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Glue two tiny black buttons for eyes, and a triangle piece of orange felt for the carrot nose.", "zh": "黏上兩顆小黑扣子當眼睛，再黏一片三角形橘色不織布當胡蘿蔔鼻子。", "keywords": ["felt", "carrot nose"] },
      { "id": 4, "speaker": "Eric", "avatar": "👦", "en": "I'm tying a mini red yarn ribbon around his neck as a warm winter scarf.", "zh": "我在他的脖子上圍一圈紅色毛線小緞帶，當作防寒小圍巾。", "keywords": ["yarn", "scarf"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "He feels so soft and squishy! No melting indoors for our friendly cotton snowman!", "zh": "摸起來好軟好有彈性喔！我們友善的棉花小雪人在室內永遠不會融化！", "keywords": ["squishy", "melting"] }
    ],
    "vocabulary": [
      { "word": "tummy", "phonetic": "/ˈtʌm.i/", "pos": "n.", "zh": "肚子、肚皮（兒語）", "example": "The puppy rolled over to have its tummy rubbed." },
      { "word": "squishy", "phonetic": "/ˈskwɪʃ.i/", "pos": "adj.", "zh": "軟綿綿的、易捏有彈性的", "example": "Fresh marshmallows are delightfully squishy." },
      { "word": "yarn", "phonetic": "/jɑːrn/", "pos": "n.", "zh": "毛線、紗線", "example": "Grandmother knitted mittens from thick wool yarn." }
    ],
    "dailyPhrase": { "en": "Soft and squishy.", "zh": "又軟又好捏（形容棉花、麵團舒適手感）" },
    "cultureTip": "室內棉花手工雪人（Cotton Ball Snowman）是氣候不常降雪地區的幼童最愛的冬季勞作，既能體驗雪人樂趣又不用受凍！"
  },

  # 12-18 [高中進階]
  {
    "id": "dialogue-1218",
    "date": "12-18",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "哲學與生活",
    "topic": {
      "en": "Hygge: The Nordic Art of Winter Coziness",
      "zh": "Hygge：北歐冬日溫馨愜意的慢活美學"
    },
    "situation": "高中外語社文化沙龍上，Grace 與 Leo 探討丹麥著名的幸福哲學「Hygge」，學習在嚴寒冬日中創造溫暖治癒的心理空間。",
    "speakers": {
      "Grace": { "role": "Grace", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" },
      "Leo": { "role": "Leo", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1218.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Grace", "avatar": "👩", "en": "Leo, Denmark consistently ranks among the happiest nations globally despite harsh, dark Scandinavian winters. What is their secret?", "zh": "Leo，儘管面臨嚴酷黑暗的斯堪地那維亞寒冬，丹麥卻始終高居全球幸福指數前列。他們的秘訣到底是什麼？", "keywords": ["Denmark", "Scandinavian"] },
      { "id": 2, "speaker": "Leo", "avatar": "🧑", "en": "It revolves largely around 'Hygge'—a cultural concept defined as intentional coziness, presence, and simple everyday contentment.", "zh": "這很大程度上圍繞著『Hygge』——一種以刻意營造的溫馨、活在當下與品味日常微小知足為核心的文化哲學。", "keywords": ["Hygge", "contentment", "coziness"] },
      { "id": 3, "speaker": "Grace", "avatar": "👩", "en": "So rather than fighting the cold, they lean into it with flickering candles, wool blankets, hot tea, and intimate conversation with loved ones.", "zh": "所以他們不是對抗嚴冬，而是順應它：點燃微光搖曳的蠟燭、蓋著羊毛毯、手捧熱茶，與親愛的人共享親密的交談。", "keywords": ["intimate", "flickering"] },
      { "id": 4, "speaker": "Leo", "avatar": "🧑", "en": "Precisely. Hygge strips away social pretense, status anxiety, and digital screens, fostering an atmosphere where you feel emotionally safe.", "zh": "正是如此。Hygge 剝離了虛假的社交偽裝、身份焦慮與 3C 螢幕干擾，營造一個讓人在情感上感到無比安全的庇護所。", "keywords": ["pretense", "anxiety", "sanctuary"] },
      { "id": 5, "speaker": "Grace", "avatar": "👩", "en": "In our fast-paced society, cultivating a Hygge corner at home is the premier antidote to chronic modern burnout.", "zh": "在步調飛快的現代社會中，在家打造一個專屬的 Hygge 溫馨角落，正是療癒長期慢性內耗的最佳良方。", "keywords": ["burnout", "antidote"] }
    ],
    "vocabulary": [
      { "word": "contentment", "phonetic": "/kənˈtent.mənt/", "pos": "n.", "zh": "知足、心滿意足", "example": "True wealth is mental peace and contentment." },
      { "word": "pretense", "phonetic": "/prɪˈtens/", "pos": "n.", "zh": "虛假偽裝、矯揉造作", "example": "Abandon all pretense and speak from the heart." },
      { "word": "burnout", "phonetic": "/ˈbɝːn.aʊt/", "pos": "n.", "zh": "職業倦怠、身心耗竭", "example": "Restful sleep prevents mental and physical burnout." }
    ],
    "dailyPhrase": { "en": "Intentional coziness.", "zh": "刻意營造的溫馨與舒適感（Hygge 生活的核心）" },
    "cultureTip": "丹麥語「Hygge（發音約為 hoo-guh）」於 2016 年被《牛津字典》列為年度代表詞彙，象徵在一杯熱飲、溫暖燭光與真誠相伴中找尋生命安頓。"
  },

  # 12-19 [國小中高]
  {
    "id": "dialogue-1219",
    "date": "12-19",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "節慶祝福",
    "topic": {
      "en": "Writing Holiday Greeting Cards",
      "zh": "手寫溫馨節慶賀卡寄給親友"
    },
    "situation": "下課時間，Ken 和 Emma 拿出彩色卡紙、印章與水彩筆，為遠方的祖父母與老師手寫新年賀卡。",
    "speakers": {
      "Ken": { "role": "Ken", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1219.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ken", "avatar": "👦", "en": "Emma, what heartfelt greeting should I write inside my card for Grandma and Grandpa?", "zh": "Emma，在寫給我外公外婆的卡片裡面，我該寫什麼溫暖真誠的祝福語呢？", "keywords": ["heartfelt", "greeting"] },
      { "id": 2, "speaker": "Emma", "avatar": "👧", "en": "How about: 'Wishing you a holiday season brimming with warmth, love, and joyful laughter'?", "zh": "這句如何：『祝您擁有一個洋溢著溫暖、關愛與歡聲笑語的溫馨節日』？", "keywords": ["brimming", "warmth"] },
      { "id": 3, "speaker": "Ken", "avatar": "👦", "en": "That sounds lovely! I will use this metallic gold calligraphy pen for their names.", "zh": "聽起來好棒！我要用這支金屬金色西洋書法筆寫他們的名字。", "keywords": ["calligraphy", "metallic"] },
      { "id": 4, "speaker": "Emma", "avatar": "👧", "en": "Press this wooden rubber stamp of a holly berry wreath in green and red ink at the bottom.", "zh": "在底端用紅綠雙色印泥蓋上這個冬青果花圈木質印章。", "keywords": ["stamp", "wreath", "holly"] },
      { "id": 5, "speaker": "Ken", "avatar": "👦", "en": "Lick the envelope, attach the festive holiday stamp, and drop it into the red postbox!", "zh": "封上信封、貼上節慶紀念郵票，投入紅色郵筒寄出囉！", "keywords": ["envelope", "postbox"] }
    ],
    "vocabulary": [
      { "word": "heartfelt", "phonetic": "/ˈhɑːrt.felt/", "pos": "adj.", "zh": "由衷的、打從心底真誠的", "example": "She expressed heartfelt thanks to her mentors." },
      { "word": "brim", "phonetic": "/brɪm/", "pos": "v.", "zh": "充滿、洋溢、溢出", "example": "Her eyes brimmed with tears of joy." },
      { "word": "wreath", "phonetic": "/riːθ/", "pos": "n.", "zh": "花環、花圈（如聖誕花圈）", "example": "A pine wreath hung on the oak front door." }
    ],
    "dailyPhrase": { "en": "Brimming with joy.", "zh": "洋溢著滿滿的喜悅。" },
    "cultureTip": "在電子郵件與通訊軟體普及的今天，歐美依舊保留聖誕手寫實體卡片（Christmas Card）的溫馨傳統，被視為最珍貴有溫度的人際心意。"
  },

  # 12-20 [國中挑戰]
  {
    "id": "dialogue-1220",
    "date": "12-20",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "文化與習俗",
    "topic": {
      "en": "Winter Solstice and Sweet Rice Dumplings",
      "zh": "冬至大如年：全家搓湯圓慶團圓"
    },
    "situation": "冬至前夕，Kevin 和同學 David 在家政教室跟隨食譜學習搓紅白雙色熱糯米湯圓。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "🧑", "gender": "male", "voice": "en-US-ChristopherNeural" },
      "David": { "role": "David", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1220.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "🧑", "en": "David, the Winter Solstice is almost here! It's astronomical: the shortest daylight and longest night of the entire year.", "zh": "David，冬至快到了！在天文上這是一年中白晝最短、黑夜最長的一天。", "keywords": ["Winter Solstice", "astronomical"] },
      { "id": 2, "speaker": "David", "avatar": "👦", "en": "In our cultural tradition, eating sweet glutinous rice dumplings—tangyuan—symbolizes family wholeness and togetherness.", "zh": "在我們的文化傳統中，吃甜糯米湯圓象徵著全家人圓滿與團聚和樂。", "keywords": ["togetherness", "glutinous"] },
      { "id": 3, "speaker": "Kevin", "avatar": "🧑", "en": "Knead the glutinous dough, pinch off a small piece, and roll it between your palms into a marble-sized sphere.", "zh": "揉勻糯米團，捏下一小塊，在兩手手掌之間搓成彈珠大小的圓球。", "keywords": ["palms", "sphere"] },
      { "id": 4, "speaker": "David", "avatar": "👦", "en": "Drop them into simmering hot brown sugar and fresh ginger soup until they float to the surface.", "zh": "放進慢火微滾的黑糖生薑甜湯裡，煮到一顆顆浮出水面就熟了。", "keywords": ["ginger soup", "surface"] },
      { "id": 5, "speaker": "Kevin", "avatar": "🧑", "en": "Chewy, warm, and comforting. With the solstice passed, daylight hours gradually grow longer each day!", "zh": "Q 彈、溫暖又療癒。過完冬至，每一天的日照時間就要開始慢慢變長囉！", "keywords": ["daylight", "comforting"] }
    ],
    "vocabulary": [
      { "word": "solstice", "phonetic": "/ˈsɑːl.stɪs/", "pos": "n.", "zh": "至日（夏至或冬至）", "example": "The winter solstice occurs around December 21st." },
      { "word": "glutinous", "phonetic": "/ˈɡluː.t̬ən.əs/", "pos": "adj.", "zh": "黏的、糯米的", "example": "Glutinous rice is essential for making mochi." },
      { "word": "togetherness", "phonetic": "/təˈɡeð.ɚ.nəs/", "pos": "n.", "zh": "團聚、親密無間的情感", "example": "Holidays foster a warm sense of family togetherness." }
    ],
    "dailyPhrase": { "en": "The shortest day, the longest night.", "zh": "白晝最短、黑夜最長的一天（冬至的天文特徵）" },
    "cultureTip": "冬至（Winter Solstice）在古代有「冬至大如年」之說，過了這天陽氣漸長（The return of the light），在東西方文化中都象徵著新生的希望。"
  },

  # 12-21 [國小初階]
  {
    "id": "dialogue-1221",
    "date": "12-21",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "節慶裝飾",
    "topic": {
      "en": "Hanging Stockings by the Fireplace",
      "zh": "把紅色長統襪掛在壁爐旁"
    },
    "situation": "聖誕節即將到來，Anna 和弟弟 Tim 拿著繡著自己英文名字的紅色絨毛長統襪，掛在客廳壁爐架上。",
    "speakers": {
      "Anna": { "role": "Anna", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Tim": { "role": "Tim", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1221.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Anna", "avatar": "👧", "en": "Tim, look at our cozy stockings! Mine is red with white fur trim, and yours is dark green!", "zh": "Tim，看我們溫暖的長統襪！我的是白毛邊紅襪子，你的是深綠色的！", "keywords": ["stockings", "fur trim"] },
      { "id": 2, "speaker": "Tim", "avatar": "👦", "en": "Let's hang them on these brass hooks along the fireplace mantelpiece.", "zh": "我們把它們掛在壁爐架邊緣的黃銅掛鉤上吧。", "keywords": ["mantelpiece", "hooks"] },
      { "id": 3, "speaker": "Anna", "avatar": "👧", "en": "Legend says Santa slides down the chimney on Christmas Eve and fills stockings with treats!", "zh": "傳說聖誕老人在平安夜會從煙囪滑下來，把各種小禮物塞滿襪子！", "keywords": ["chimney", "Santa"] },
      { "id": 4, "speaker": "Tim", "avatar": "👦", "en": "What goodies are you hoping for?", "zh": "妳最希望襪子裡裝什麼好東西？", "keywords": ["goodies"] },
      { "id": 5, "speaker": "Anna", "avatar": "👧", "en": "A striped peppermint candy cane, sticker sheets, and shiny chocolate coins!", "zh": "紅白條紋薄荷拐杖糖、精美貼紙包，還有閃閃發亮的巧克力金幣！", "keywords": ["candy cane", "coins"] }
    ],
    "vocabulary": [
      { "word": "mantelpiece", "phonetic": "/ˈmæn.təl.piːs/", "pos": "n.", "zh": "壁爐架、壁爐台", "example": "Family portraits sat atop the marble mantelpiece." },
      { "word": "chimney", "phonetic": "/ˈtʃɪm.ni/", "pos": "n.", "zh": "煙囪", "example": "Smoke curled gently out of the brick chimney." },
      { "word": "candy cane", "phonetic": "/ˈkæn.di keɪn/", "pos": "n.", "zh": "拐杖糖（紅白條紋薄荷糖）", "example": "Hang a candy cane on the Christmas tree." }
    ],
    "dailyPhrase": { "en": "Fill with treats.", "zh": "裝滿美味可口的小點心。" },
    "cultureTip": "「Stocking Stuffers」專指那些體積小巧、適合塞入聖誕襪裡的小禮物，如護唇膏、小文具、精巧拼圖或巧克力糖果。"
  },

  # 12-22 [高中進階]
  {
    "id": "dialogue-1222",
    "date": "12-22",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "哲學思辨",
    "topic": {
      "en": "Solitude vs. Loneliness in Modern Times",
      "zh": "獨處的平靜與孤獨的煎熬：現代人的心靈邊界"
    },
    "situation": "自習室閉館後，Jason 和 Chloe 沿著冬夜靜謐的街道漫步，深入辨析主動選擇的「有益獨處（Solitude）」與被動寂寞的本質差異。",
    "speakers": {
      "Jason": { "role": "Jason", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1222.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Jason", "avatar": "🧑", "en": "Chloe, in our hyper-connected world where notifications ping around the clock, silence can sometimes feel deafening.", "zh": "Chloe，在當今這個訊息隨時叮咚響的高度連結世界裡，安靜有時候反而讓人感到震耳欲聾。", "keywords": ["hyper-connected", "deafening"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👩", "en": "People conflate loneliness with solitude, but philosophically, they are worlds apart. Loneliness is the pain of being alone; solitude is the glory of being alone.", "zh": "大家常把寂寞與獨處混為一談，但哲學上兩者天差地別。寂寞是孤身一人的痛苦；而獨處則是享受與自己相伴的榮耀。", "keywords": ["conflate", "solitude", "loneliness"] },
      { "id": 3, "speaker": "Jason", "avatar": "🧑", "en": "Paul Tillich's famous distinction! Loneliness feels like a deficiency, whereas intentional solitude provides mental sanctuary for deep reflection.", "zh": "神學家田立克名言！寂寞讓人覺得匱乏空虛，而有意識的獨處則為深度反思提供了心靈聖所。", "keywords": ["deficiency", "sanctuary"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👩", "en": "If you cannot bear being alone with your own thoughts without compulsively reaching for your phone, you are essentially a stranger to yourself.", "zh": "如果你無法靜下心與自己的思緒獨處，而必須強迫性地抓起手機，本質上你對自己來說就是個陌生人。", "keywords": ["compulsively", "stranger"] },
      { "id": 5, "speaker": "Jason", "avatar": "🧑", "en": "Winter's stillness invites that homecoming. Befriending yourself in quiet solitude is the ultimate self-mastery.", "zh": "冬天的寂靜正召喚著這場心靈的回歸。在安靜的獨處中與自己成為好友，就是最高境界的自我掌控。", "keywords": ["homecoming", "self-mastery"] }
    ],
    "vocabulary": [
      { "word": "conflate", "phonetic": "/kənˈfleɪt/", "pos": "v.", "zh": "混淆、合併（兩個不同概念）", "example": "Do not conflate confidence with arrogance." },
      { "word": "solitude", "phonetic": "/ˈsɑː.lə.tuːd/", "pos": "n.", "zh": "獨處（正面平靜的孤獨享受）", "example": "He cherished the peaceful solitude of the mountains." },
      { "word": "compulsive", "phonetic": "/kəmˈpʌl.sɪv/", "pos": "adj.", "zh": "強迫性的、難以克制的", "example": "Compulsive phone checking disrupts productive work." }
    ],
    "dailyPhrase": { "en": "Befriend yourself.", "zh": "與自己和解、成為自己最好的朋友。" },
    "cultureTip": "哲學家保羅·田立克（Paul Tillich）名言：「Language has created the word 'loneliness' to express the pain of being alone. And it has created the word 'solitude' to express the glory of being alone.」"
  },

  # 12-23 [國小中高]
  {
    "id": "dialogue-1223",
    "date": "12-23",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "同儕分享",
    "topic": {
      "en": "The Classroom Gift Exchange Party",
      "zh": "放學前的全班聖誕拆禮物派對"
    },
    "situation": "學期最後一天放學前，Emma 和 Lucas 坐在圍成一圈的教室中央，拆開各自抽到的神秘聖誕禮物。",
    "speakers": {
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1223.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Emma", "avatar": "👧", "en": "Lucas, untie the satin ribbon on your package! Who was your Secret Santa?", "zh": "Lucas，解開你禮物盒上的緞面蝴蝶結！誰是你的神秘聖誕老人呀？", "keywords": ["satin", "Secret Santa"] },
      { "id": 2, "speaker": "Lucas", "avatar": "👦", "en": "Tear open the glossy wrapping paper... Whoa! A solar-powered mini rover kit!", "zh": "撕開亮面包裝紙…哇！是一組太陽能動力迷你火星探測車模型套件！", "keywords": ["wrapping paper", "rover"] },
      { "id": 3, "speaker": "Emma", "avatar": "👧", "en": "Look at the signed card: 'To my best science lab partner, from David!' That is so thoughtful!", "zh": "看上面的簽名卡片：『送給我最棒的自然實驗搭檔，David 贈！』這真的太貼心了！", "keywords": ["thoughtful", "partner"] },
      { "id": 4, "speaker": "Lucas", "avatar": "👦", "en": "Now open yours, Emma! What is inside that square parcel?", "zh": "現在換妳開禮物了 Emma！那個方方正正的包裹裡是什麼？", "keywords": ["parcel"] },
      { "id": 5, "speaker": "Emma", "avatar": "👧", "en": "A hardcover sketch journal with vibrant watercolor pans! It's the most wonderful holiday surprise ever!", "zh": "是一本精裝繪圖筆記本，還附有一整盒鮮豔的水彩餅！這真是有史以來最棒的假期驚喜！", "keywords": ["journal", "watercolor"] }
    ],
    "vocabulary": [
      { "word": "parcel", "phonetic": "/ˈpɑːr.səl/", "pos": "n.", "zh": "包裹、郵包", "example": "The courier delivered a heavy parcel to our doorstep." },
      { "word": "hardcover", "phonetic": "/ˈhɑːrdˌkʌv.ɚ/", "pos": "adj./n.", "zh": "精裝本的、硬皮書", "example": "I purchased the collector's hardcover edition." },
      { "word": "satin", "phonetic": "/ˈsæt.ən/", "pos": "n./adj.", "zh": "緞子、絲緞般的", "example": "She wore a lovely ivory satin ribbon." }
    ],
    "dailyPhrase": { "en": "Tear open the wrapping paper.", "zh": "興奮地撕開禮物包裝紙。" },
    "cultureTip": "學校放冬假（Winter Break）前最後一天通常被稱為「Holiday Party Day」，師生共享餅乾點心、交換禮物，在溫馨祝福聲中互道假期快樂。"
  },

  # 12-24 [國中挑戰]
  {
    "id": "dialogue-1224",
    "date": "12-24",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "溫馨平安夜",
    "topic": {
      "en": "Christmas Eve: Cookies for Santa and Reindeer Carrots",
      "zh": "平安夜：為聖誕老人準備餅乾與馴鹿胡蘿蔔"
    },
    "situation": "12月24日平安夜睡覺前，Tyler 和表姐 Zoe 在廚房壁爐邊的托盤上擺放熱牛奶、餅乾與洗乾淨的胡蘿蔔。",
    "speakers": {
      "Tyler": { "role": "Tyler", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1224.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tyler", "avatar": "👦", "en": "Zoe, it's Christmas Eve! Set the red ceramic plate on the hearth before we head upstairs to bed.", "zh": "Zoe，今天是平安夜！在我們上樓睡覺前，先把紅色陶瓷盤擺在壁爐邊。", "keywords": ["Christmas Eve", "hearth"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "I'll arrange three fresh chocolate chip cookies and pour a tall glass of whole milk for Santa.", "zh": "我放三片現烤巧克力脆片餅乾，再為聖誕老人倒一大杯全脂鮮奶。", "keywords": ["chocolate chip", "arrange"] },
      { "id": 3, "speaker": "Tyler", "avatar": "👦", "en": "Don't forget the nine hardworking reindeer, especially Rudolph! Here are four crunchy carrots with the green tops on.", "zh": "別忘了那九隻辛苦拉雪橇的馴鹿，尤其是魯道夫！這裡有四根帶綠葉的新鮮脆胡蘿蔔。", "keywords": ["reindeer", "Rudolph"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "I'll leave a little note: 'Dear Santa and reindeer, thank you for spreading joy across the globe!'", "zh": "我再留一張小紙條：『親愛的聖誕老人與馴鹿，謝謝你們將歡樂播撒到全世界！』", "keywords": ["spreading joy", "note"] },
      { "id": 5, "speaker": "Tyler", "avatar": "👦", "en": "Now off to bed! Santa only visits when everyone is fast asleep. Merry Christmas Eve!", "zh": "現在快上床睡覺囉！聖誕老人只有在大家都熟睡時才會悄悄來訪。平安夜快樂！", "keywords": ["fast asleep", "Merry Christmas"] }
    ],
    "vocabulary": [
      { "word": "hearth", "phonetic": "/hɑːrθ/", "pos": "n.", "zh": "壁爐地面、壁爐邊", "example": "The family gathered around the warm hearth." },
      { "word": "arrange", "phonetic": "/əˈreɪndʒ/", "pos": "v.", "zh": "排列、佈置整齊", "example": "She arranged fresh flowers in the glass vase." },
      { "word": "fast asleep", "phonetic": "/fæst əˈsliːp/", "pos": "adj.", "zh": "熟睡的、酣睡的", "example": "The exhausted hikers were fast asleep within minutes." }
    ],
    "dailyPhrase": { "en": "Merry Christmas Eve!", "zh": "平安夜快樂！（12月24日最常說的節慶祝福）" },
    "cultureTip": "平安夜在壁爐旁留下「Cookies and Milk for Santa」與「Carrots for the Reindeer」，是西方家庭代代相傳、守護孩童純真想像力的美好習俗。"
  },

  # 12-25 [國小初階]
  {
    "id": "dialogue-1225",
    "date": "12-25",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "聖誕清晨",
    "topic": {
      "en": "Merry Christmas! Santa Came Last Night!",
      "zh": "聖誕節快樂！聖誕老人昨晚真的來過了！"
    },
    "situation": "12月25日清晨天剛亮，Sam 和 Eric 穿著恐龍睡衣光著腳丫跑到客廳聖誕樹下，驚喜發現滿地禮物盒。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Eric": { "role": "Eric", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1225.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Eric, wake up! Merry Christmas! Look under the glowing tree!", "zh": "Eric，快醒醒！聖誕節快樂！看發光聖誕樹底下！", "keywords": ["Merry Christmas", "glowing"] },
      { "id": 2, "speaker": "Eric", "avatar": "👦", "en": "He came! The plate of cookies is empty except for a few crumbs, and the milk glass is gone!", "zh": "他真的來過了！餅乾盤全空了只剩幾顆碎屑，牛奶也喝得一乾二淨！", "keywords": ["crumbs", "empty"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "And the carrots have tiny bite marks on them! The reindeer enjoyed their midnight snack!", "zh": "而且胡蘿蔔上還有小小的咬痕！馴鹿昨晚好好享受了牠們的宵夜點心！", "keywords": ["bite marks", "midnight snack"] },
      { "id": 4, "speaker": "Eric", "avatar": "👦", "en": "Our stockings are bulging with toys, and look at this huge green box with my name tag!", "zh": "我們的長統襪塞滿了禮物鼓鼓的，還有這個貼著我名字的大綠盒子！", "keywords": ["bulging", "name tag"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Merry Christmas, Eric! This is the most joyful and magical morning of the whole year!", "zh": "聖誕快樂 Eric！這真的是全年中充滿最多歡笑與奇蹟的早晨！", "keywords": ["joyful", "magical"] }
    ],
    "vocabulary": [
      { "word": "crumb", "phonetic": "/krʌm/", "pos": "n.", "zh": "麵包屑、餅乾碎屑", "example": "Sweep the cookie crumbs off the dining table." },
      { "word": "bulge", "phonetic": "/bʌldʒ/", "pos": "v./n.", "zh": "膨脹、塞得鼓鼓的", "example": "His pockets bulged with colorful marbles." },
      { "word": "joyful", "phonetic": "/ˈdʒɔɪ.fəl/", "pos": "adj.", "zh": "充滿喜悅的、令人歡欣的", "example": "The wedding was a joyful celebration." }
    ],
    "dailyPhrase": { "en": "Merry Christmas!", "zh": "聖誕節快樂！（全球最通用的聖誕節祝福語）" },
    "cultureTip": "聖誕清晨（Christmas Morning）全家穿著節慶睡衣一起拆禮物（Unwrapping presents），是西方家庭一年中最幸福凝聚的經典畫面。"
  },

  # 12-26 [高中進階]
  {
    "id": "dialogue-1226",
    "date": "12-26",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "歷史與人文",
    "topic": {
      "en": "Boxing Day Traditions and Goodwill",
      "zh": "節禮日（Boxing Day）的博愛互助歷史淵源"
    },
    "situation": "聖誕節隔天 12 月 26 日，高中歷史研討小組 Marcus 與 Bella 討論英國及大英國協傳統節日「Boxing Day」的起源與社會博愛精神。",
    "speakers": {
      "Marcus": { "role": "Marcus", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Bella": { "role": "Bella", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1226.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Marcus", "avatar": "🧑", "en": "Bella, many people today mistake Boxing Day as a day for retail sales or prize fighting sports.", "zh": "Bella，很多人今天都誤以為節禮日（Boxing Day）是去百貨公司搶打折或是看拳擊比賽的日子。", "keywords": ["Boxing Day", "mistake"] },
      { "id": 2, "speaker": "Bella", "avatar": "👩", "en": "Its true historical origin in Britain was profoundly philanthropic. Churches opened donation 'alms boxes' to distribute charity to the impoverished.", "zh": "它在英國真正的歷史起源其實充滿了博愛慈善精神。教堂會在聖誕隔天打開奉獻箱（Alms boxes），將善款物資分發給貧困家庭。", "keywords": ["philanthropic", "alms", "impoverished"] },
      { "id": 3, "speaker": "Marcus", "avatar": "🧑", "en": "Employers would also present domestic staff and tradespeople with 'Christmas boxes' containing bonuses and leftover feast food as tokens of gratitude.", "zh": "雇主也會在當天致贈家僕與勞工裝有年終獎金與豐盛佳餚的聖誕禮物盒，感謝他們一整年的辛勞付出。", "keywords": ["tradespeople", "tokens"] },
      { "id": 4, "speaker": "Bella", "avatar": "👩", "en": "It served as a societal equalizer, reminding the affluent that true holiday spirit resides in sharing bounty with frontline laborers.", "zh": "它發揮了社會天平的作用，提醒富裕階層：真正的節日精神在於將豐收與第一線基層勞工共同分享。", "keywords": ["equalizer", "frontline", "bounty"] },
      { "id": 5, "speaker": "Marcus", "avatar": "🧑", "en": "Reviving that philanthropic consciousness makes December twenty-sixth meaningful far beyond commercial sales flyers.", "zh": "重拾那份博愛助人的初衷，能讓十二月二十六日的意義遠遠超越商業傳單上的打折促銷。", "keywords": ["philanthropic", "consciousness"] }
    ],
    "vocabulary": [
      { "word": "philanthropic", "phonetic": "/ˌfɪl.ænˈθrɑː.pɪk/", "pos": "adj.", "zh": "慈善的、博愛的", "example": "The foundation funded philanthropic education initiatives." },
      { "word": "impoverished", "phonetic": "/ɪmˈpɑː.vɚ.ɪʃt/", "pos": "adj.", "zh": "赤貧的、匱乏的", "example": "Charity organizations distribute food to impoverished neighborhoods." },
      { "word": "bounty", "phonetic": "/ˈbaʊn.t̬i/", "pos": "n.", "zh": "慷慨餽贈、豐沛物產", "example": "We gave thanks for nature's abundant autumn bounty." }
    ],
    "dailyPhrase": { "en": "A token of gratitude.", "zh": "聊表寸心、表達感謝的微薄心意禮品。" },
    "cultureTip": "「Boxing Day（12月26日）」為英國、加拿大、澳洲等大英國協國家的法定假日，除了慈善淵源，也是全家觀看英超足球「節禮日大戰」的傳統節日。"
  },

  # 12-27 [國小中高]
  {
    "id": "dialogue-1227",
    "date": "12-27",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "冬日休閒",
    "topic": {
      "en": "A Cozy Afternoon of Family Jigsaw Puzzles",
      "zh": "冬日午後圍坐拼千片拼圖"
    },
    "situation": "聖誕假期的午後，外頭下著微雪，Emma 和哥哥 Lucas 在客廳咖啡桌上合力挑戰一幅一千片雪景拼圖。",
    "speakers": {
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1227.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Emma", "avatar": "👧", "en": "Lucas, one thousand puzzle pieces look like an overwhelming sea of colorful cardboard!", "zh": "Lucas，這一千片拼圖片看起來好像一片汪洋大海，讓人眼花撩亂！", "keywords": ["jigsaw", "overwhelming"] },
      { "id": 2, "speaker": "Lucas", "avatar": "👦", "en": "Rule number one of jigsaw puzzles: separate all the straight flat border pieces first!", "zh": "玩拼圖的黃金第一步：先把所有有平直邊緣的邊框片挑出來！", "keywords": ["border", "separate"] },
      { "id": 3, "speaker": "Emma", "avatar": "👧", "en": "Great strategy! Constructing the outside frame gives our puzzle a clear boundary.", "zh": "好策略！把外圍的邊框先搭起來，能給我們的拼圖一個清晰的輪廓邊界。", "keywords": ["boundary", "frame"] },
      { "id": 4, "speaker": "Lucas", "avatar": "👦", "en": "Now sort the interior pieces by distinctive color: deep blue sky, red village cottage, and snowy pine trees.", "zh": "現在按特殊顏色分類內部的碎片：深藍色夜空、紅色鄉村小屋，還有落雪的松樹林。", "keywords": ["interior", "distinctive"] },
      { "id": 5, "speaker": "Emma", "avatar": "👧", "en": "Click! Look, this piece with the chimney chimney fits like a glove! Teamwork makes piecing it together effortless!", "zh": "卡嗒！看，這片有小煙囪的碎片完美卡進去了！團隊合作讓拼拼圖變得好輕鬆！", "keywords": ["fits like a glove", "effortless"] }
    ],
    "vocabulary": [
      { "word": "jigsaw", "phonetic": "/ˈdʒɪɡ.sɑː/", "pos": "n.", "zh": "拼圖遊戲、拼圖玩具", "example": "Working on a jigsaw puzzle sharpens spatial reasoning." },
      { "word": "distinctive", "phonetic": "/dɪˈstɪŋk.tɪv/", "pos": "adj.", "zh": "與眾不同的、獨特的", "example": "The bird had distinctive sapphire plumage." },
      { "word": "effortless", "phonetic": "/ˈef.ɚt.ləs/", "pos": "adj.", "zh": "毫不費力的、輕鬆自如的", "example": "Her graceful piano playing seemed completely effortless." }
    ],
    "dailyPhrase": { "en": "Fit like a glove.", "zh": "天衣無縫、完全吻合匹配。" },
    "cultureTip": "拼千片拼圖（Jigsaw Puzzle）是歐美家庭在冬季長假（Winter Break）最熱門的「Slow Living（慢活）」室內靜態活動，能訓練專注力與耐性。"
  },

  # 12-28 [國中挑戰]
  {
    "id": "dialogue-1228",
    "date": "12-28",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "寒假閱讀",
    "topic": {
      "en": "Setting Up a Winter Break Reading List",
      "zh": "列出寒假專屬充電閱讀書單"
    },
    "situation": "在市圖書館青少年閱覽室，Leo 和 Zoe 拿著筆記本，為即將到來的兩週冬季寒假挑選小說與科普書籍。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1228.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Zoe, winter break is the golden opportunity to dive into books we didn't have time to read during busy exam weeks.", "zh": "Zoe，寒假正是沉浸在大考忙碌期間沒空讀的那些好書的黃金機會！", "keywords": ["winter break", "opportunity"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "I agree! I'm planning to read a classic adventure novel, one popular science book about quantum physics, and a biography.", "zh": "我同意！我打算讀一本經典冒險小說、一本關於量子物理的科普書，還有一本傳記。", "keywords": ["biography", "quantum physics"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Curating a diversified reading menu keeps reading exciting rather than feeling like homework.", "zh": "打造多元化的閱讀菜單，能讓讀書維持充滿期待的趣味，而不是像在寫作業一樣累。", "keywords": ["diversified", "curating"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Let's set a realistic goal: twenty-five pages a day before bed with hot peppermint tea.", "zh": "我們來訂個切實可行的目標：每天睡前配一杯熱薄荷茶讀二十五頁。", "keywords": ["realistic", "peppermint tea"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "A book is a magic passport to another world. Let our winter literary journey begin!", "zh": "一本書就是通往另一個世界的魔法護照。讓我們展開這趟冬日文學之旅吧！", "keywords": ["passport", "literary"] }
    ],
    "vocabulary": [
      { "word": "curate", "phonetic": "/kjʊˈreɪt/", "pos": "v.", "zh": "精心挑選、策畫整理（清單或展覽）", "example": "She curated an inspiring playlist for studying." },
      { "word": "diversified", "phonetic": "/daɪˈvɝː.sə.faɪd/", "pos": "adj.", "zh": "多元化的、多樣性的", "example": "A diversified diet promotes overall health." },
      { "word": "literary", "phonetic": "/ˈlɪt̬.ə.rer.i/", "pos": "adj.", "zh": "文學的、文字素養的", "example": "The classic novel won prestigious literary awards." }
    ],
    "dailyPhrase": { "en": "A passport to another world.", "zh": "通往另一個世界的護照（形容閱讀打開無限眼界）" },
    "cultureTip": "研究顯示，寒假如果完全中斷閱讀，會產生「Winter Slide（假期學力滑坡）」；每天只要保持 20 分鐘課外閱讀，開學後的語彙理解力將顯著拔尖。"
  },

  # 12-29 [國小初階]
  {
    "id": "dialogue-1229",
    "date": "12-29",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "生活自律",
    "topic": {
      "en": "Winter Room Cleaning and Donating Toys",
      "zh": "年終歲末整理房間與玩具捐贈"
    },
    "situation": "年終倒數前夕，Lily 和 Toby 在臥室整理自己的玩具箱與書架，把保存良好的益智積木放進捐贈箱。",
    "speakers": {
      "Lily": { "role": "Lily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1229.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lily", "avatar": "👧", "en": "Toby, the year is ending in just two days! Let's give our bedrooms a thorough year-end decluttering.", "zh": "Toby，今年再過兩天就要結束了！我們把臥室來個徹底的年終大整理吧。", "keywords": ["year-end", "decluttering"] },
      { "id": 2, "speaker": "Toby", "avatar": "👦", "en": "I'll sort through my toy bins: one pile to keep, and one pile of gently loved toys to donate.", "zh": "我來分類我的玩具箱：一堆留著，另一堆保存完好、小時候很愛的玩具拿去捐贈。", "keywords": ["donate", "gently loved"] },
      { "id": 3, "speaker": "Lily", "avatar": "👧", "en": "Here are my complete wooden building blocks and stuffed teddy bear. They are clean and ready for a new home.", "zh": "這裡是我的完整木質積木組和填充泰迪熊，都洗得很乾淨，準備好去新家了。", "keywords": ["building blocks", "stuffed"] },
      { "id": 4, "speaker": "Toby", "avatar": "👦", "en": "Wiping the bookshelf dust makes room for fresh new books and notebooks in the coming year!", "zh": "把書架灰塵擦乾淨，就能為新的一年騰出空間放新書和筆記本囉！", "keywords": ["dust", "bookshelf"] },
      { "id": 5, "speaker": "Lily", "avatar": "👧", "en": "A tidy room brings a clear, calm mind. Out with the old, in with the new!", "zh": "乾淨整齊的房間帶來清爽平靜的心情。舊的不去，新的不來！", "keywords": ["tidy", "calm mind"] }
    ],
    "vocabulary": [
      { "word": "declutter", "phonetic": "/diːˈklʌt̬.ɚ/", "pos": "v.", "zh": "斷捨離、清理雜物", "example": "Declutter your wardrobe to start the new year fresh." },
      { "word": "tidy", "phonetic": "/ˈtaɪ.di/", "pos": "adj./v.", "zh": "整潔的、整齊的、整理", "example": "Keep your study desk tidy and organized." },
      { "word": "thorough", "phonetic": "/ˈθɝː.oʊ/", "pos": "adj.", "zh": "徹底的、完全詳盡的", "example": "She conducted a thorough inspection of the equipment." }
    ],
    "dailyPhrase": { "en": "Out with the old, in with the new!", "zh": "除舊布新！舊的不去，新的不來！（歲末大掃除最經典諺語）" },
    "cultureTip": "「Out with the old, in with the new」源自英國 19 世紀新年傳統，透過清理空間與整理心靈，揮別過去一年的包袱、以嶄新面貌迎接新年。"
  },

  # 12-30 [高中進階]
  {
    "id": "dialogue-1230",
    "date": "12-30",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "年度復盤",
    "topic": {
      "en": "Conducting an Honest Annual Life Audit",
      "zh": "年終深度復盤：為自己的年度生活做一場真誠審計"
    },
    "situation": "12月30日午後在安靜的咖啡館角，高三好友 Henry 與 Claire 拿著年度手帳，針對過去一年的身心健康、學業技能與人際關係進行客觀復盤。",
    "speakers": {
      "Henry": { "role": "Henry", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Claire": { "role": "Claire", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1230.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Henry", "avatar": "🧑", "en": "Claire, before rushing into writing ambitious resolutions for next year, let's conduct a rigorous annual audit of the past twelve months.", "zh": "Claire，在急著為明年寫下雄心勃勃的願望清單之前，我們先來對過去十二個月做一次嚴謹客觀的年度審計復盤吧。", "keywords": ["audit", "resolutions", "rigorous"] },
      { "id": 2, "speaker": "Claire", "avatar": "👩", "en": "I use the 'Stop, Start, Continue' framework. What habits drained your energy that you must ruthlessly eliminate?", "zh": "我習慣用『停止、啟動、保持』的三維架構。過去一年有哪些嚴重內耗你精力的習慣是你必須果斷戒除的？", "keywords": ["eliminate", "habits", "drained"] },
      { "id": 3, "speaker": "Henry", "avatar": "🧑", "en": "Late-night revenge bedtime procrastination was my primary pitfall; it degraded my morning focus and emotional regulation.", "zh": "報復性熬夜睡眠拖延是我最大的痛點坑洞，它嚴重損害了我隔天早晨的專注力與情緒調節能力。", "keywords": ["pitfall", "procrastination"] },
      { "id": 4, "speaker": "Claire", "avatar": "👩", "en": "And on the positive side, committing to our daily English listening and conversational habit was definitely our crown achievement.", "zh": "而正面收穫方面，堅持每天進行英語聽力與對話練習，絕對是我們今年最閃亮的一項里程碑成就。", "keywords": ["achievement", "committing"] },
      { "id": 5, "speaker": "Henry", "avatar": "🧑", "en": "Self-awareness is the prerequisite for transformation. Examining reality without judgment equips us to step into the future with intentionality.", "zh": "深刻的自省覺察是蛻變成長的前提。不帶苛責地如實審視過往，能賦予我們目標篤定地邁向未來的勇氣。", "keywords": ["transformation", "intentionality", "prerequisite"] }
    ],
    "vocabulary": [
      { "word": "audit", "phonetic": "/ˈɑː.dɪt/", "pos": "n./v.", "zh": "審計、全面審查復盤", "example": "Conduct an honest audit of your time expenditure." },
      { "word": "prerequisite", "phonetic": "/ˌpriːˈrek.wə.zɪt/", "pos": "n./adj.", "zh": "先決條件、必備前提", "example": "Trust is an indispensable prerequisite for teamwork." },
      { "word": "intentionality", "phonetic": "/ɪnˌten.ʃənˈæl.ə.t̬i/", "pos": "n.", "zh": "意圖明確、有目標意識的行動力", "example": "Live each day with deliberate intentionality." }
    ],
    "dailyPhrase": { "en": "Stop, Start, Continue.", "zh": "停止、啟動、保持（全球頂尖經理人與個人成長最實用的三步復盤法）" },
    "cultureTip": "「Annual Life Audit（年度生活審計）」是現代歐美青年流行的高階自我管理法，強調回顧真實數據、經驗教訓，而非只憑感性空想新年目標。"
  },

  # 12-31 [國中挑戰]
  {
    "id": "dialogue-1231",
    "date": "12-31",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "跨年倒數",
    "topic": {
      "en": "New Year's Eve: Ten, Nine, Eight... Happy New Year!",
      "zh": "跨年夜：十、九、八…新年快樂！"
    },
    "situation": "12月31日跨年夜最後一分鐘，全家人與朋友守在電視直播與窗前，大聲倒數計時迎接璀璨新年零點鐘聲。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "🧑", "gender": "male", "voice": "en-US-ChristopherNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1231.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "🧑", "en": "Look at the giant illuminated clock! Sixty seconds remaining in this remarkable year!", "zh": "看巨大的發光倒數大時鐘！這個精彩難忘的一年只剩最後六十秒了！", "keywords": ["illuminated", "remaining"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Grab your noise-makers, party poppers, and sparkling apple cider glasses!", "zh": "拿好你們的手搖發聲器、派對拉炮，還有氣泡蘋果西打玻璃杯！", "keywords": ["poppers", "cider", "glasses"] },
      { "id": 3, "speaker": "Kevin", "avatar": "🧑", "en": "Everyone join in the countdown! Ten! Nine! Eight! Seven! Six!", "zh": "大家一起加入大聲倒數！十！九！八！七！六！", "keywords": ["countdown", "join in"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Five! Four! Three! Two! One... Midnight! HAPPY NEW YEAR!", "zh": "五！四！三！二！一…午夜零點！新年快樂！", "keywords": ["midnight", "Happy New Year"] },
      { "id": 5, "speaker": "Kevin", "avatar": "🧑", "en": "Bells are chiming, fireworks are bursting in the sky, and confetti is showering down! Here's to a fantastic, healthy, and brilliant new year ahead!", "zh": "鐘聲悠揚敲響，煙火在夜空中綻放，彩紙繽紛灑落！敬我們即將迎來的精彩、健康、無比燦爛的嶄新一年！", "keywords": ["confetti", "chiming", "fireworks"] }
    ],
    "vocabulary": [
      { "word": "confetti", "phonetic": "/kənˈfet.i/", "pos": "n.", "zh": "（派對慶祝用的）五彩碎紙屑", "example": "Colorful confetti showered over the cheering crowd." },
      { "word": "chime", "phonetic": "/tʃaɪm/", "pos": "v./n.", "zh": "（鐘聲）鳴響、悠揚敲鐘聲", "example": "The cathedral clock chimed twelve strokes at midnight." },
      { "word": "illuminated", "phonetic": "/ɪˈluː.mə.neɪ.t̬ɪd/", "pos": "adj.", "zh": "照亮的、燈火輝煌的", "example": "The illuminated skyline looked breathtaking." }
    ],
    "dailyPhrase": { "en": "Happy New Year!", "zh": "新年快樂！（午夜零點全體狂歡歡呼的最經典名句）" },
    "cultureTip": "紐約時代廣場的「Times Square Ball Drop（水晶球跨年倒數降落）」自 1907 年延續至今，零點時伴隨著合唱《Auld Lang Syne（友誼天長地久）》，象徵歲月流轉、友誼永存。"
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
    for new_item in DECEMBER_DIALOGUES:
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

    print(f"成功新增 12 月份共 {added_count} 篇對話！目前資料庫總計共有 {len(existing)} 篇對話 (涵蓋 9 月至 12 月共 122 天，完整一整個學期)。")

if __name__ == '__main__':
    main()
