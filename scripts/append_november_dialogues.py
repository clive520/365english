#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次建立 11 月份生活對話 (11-01 至 11-30，共 30 篇)
涵蓋深秋轉冬、熱可可、英語話劇、感恩節大餐與志工服務！
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'dialogues.json')

NOVEMBER_DIALOGUES = [
  # 11-01 [國小初階]
  {
    "id": "dialogue-1101",
    "date": "11-01",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "季節變換",
    "topic": {
      "en": "Welcome November and Steaming Hot Cocoa",
      "zh": "迎接十一月與熱騰騰的棉花糖可可"
    },
    "situation": "十一月的第一天早晨，外面吹起冷風，Toby 和妹妹 Zoe 捧著熱可可暖手。",
    "speakers": {
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1101.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Toby", "avatar": "👦", "en": "November is officially here! The morning grass is covered in white frost.", "zh": "十一月正式到來了！早晨的草地上覆蓋著一層白霜呢。", "keywords": ["November", "frost"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "My fingertips are freezing! Can Mom make us hot cocoa?", "zh": "我的手指頭快凍僵了！媽媽可以幫我們煮熱可可嗎？", "keywords": ["freezing", "cocoa"] },
      { "id": 3, "speaker": "Toby", "avatar": "👦", "en": "She already did! Smell that sweet, rich chocolate steam?", "zh": "她已經煮好囉！聞到那個香甜濃郁的巧克力熱氣了嗎？", "keywords": ["steam", "rich"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Look! Three mini marshmallows are bobbing up and down on top!", "zh": "看！三顆小棉花糖在上面一浮一沉的耶！", "keywords": ["marshmallows", "bobbing"] },
      { "id": 5, "speaker": "Toby", "avatar": "👦", "en": "Hold the warm mug with both hands. It warms you up instantly from head to toe!", "zh": "用雙手捧著溫熱的馬克杯，從頭到腳瞬間就暖和起來了！", "keywords": ["mug", "instantly"] }
    ],
    "vocabulary": [
      { "word": "frost", "phonetic": "/frɑːst/", "pos": "n.", "zh": "霜、白霜", "example": "Delicate frost coated the window pane." },
      { "word": "freezing", "phonetic": "/ˈfriː.zɪŋ/", "pos": "adj.", "zh": "極冷的、冰凍的", "example": "Put on your gloves; it's freezing outside." },
      { "word": "mug", "phonetic": "/mʌɡ/", "pos": "n.", "zh": "馬克杯、大茶杯", "example": "He drank hot soup from a ceramic mug." }
    ],
    "dailyPhrase": { "en": "From head to toe.", "zh": "從頭到腳、全身上下。" },
    "cultureTip": "進入十一月霜降後，歐美家庭常在熱可可上放幾顆棉花糖或擠上鮮奶油，這是冬季最具代表性的暖心飲品。"
  },

  # 11-02 [國小中高]
  {
    "id": "dialogue-1102",
    "date": "11-02",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "趣味科學",
    "topic": {
      "en": "Why Do We See Our Breath?",
      "zh": "為什麼冬天呼氣會冒白煙？"
    },
    "situation": "早自習前排隊進校門，Lucas 和 Tina 發現說話時嘴巴一直吐出像小雲朵般的白煙。",
    "speakers": {
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Tina": { "role": "Tina", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1102.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lucas", "avatar": "👦", "en": "Tina, watch this! Every time I exhale, a puff of white smoke comes out like a dragon!", "zh": "Tina，看這個！我每次呼氣時，都會像小恐龍一樣噴出一團白煙！", "keywords": ["exhale", "puff"] },
      { "id": 2, "speaker": "Tina", "avatar": "👧", "en": "Haha, me too! Is that real smoke, or is it water vapor?", "zh": "哈哈，我也是！那是真的煙嗎？還是水蒸氣呢？", "keywords": ["vapor", "smoke"] },
      { "id": 3, "speaker": "Lucas", "avatar": "👦", "en": "Our science teacher told us: our warm breath contains invisible water vapor.", "zh": "我們自然老師說過：我們溫熱的呼氣裡含有看不見的水蒸氣。", "keywords": ["invisible", "breath"] },
      { "id": 4, "speaker": "Tina", "avatar": "👧", "en": "And when warm vapor meets chilly outside air, it instantly condenses into tiny water droplets!", "zh": "而當溫暖的水蒸氣遇上外面冰冷的冷空氣，就會瞬間凝結成微小的水滴！", "keywords": ["condenses", "droplets"] },
      { "id": 5, "speaker": "Lucas", "avatar": "👦", "en": "So we are literally creating miniature clouds right in front of our noses!", "zh": "所以我們等於是在自己的鼻尖前製造迷你小雲朵呢！", "keywords": ["miniature", "clouds"] }
    ],
    "vocabulary": [
      { "word": "exhale", "phonetic": "/eksˈheɪl/", "pos": "v.", "zh": "呼氣、吐氣", "example": "Inhale deeply and then exhale slowly." },
      { "word": "condense", "phonetic": "/kənˈdens/", "pos": "v.", "zh": "（氣體）凝結、濃縮", "example": "Steam condenses into water on cold glass." },
      { "word": "droplet", "phonetic": "/ˈdrɑː.plət/", "pos": "n.", "zh": "微小水滴、飛沫", "example": "Tiny droplets of morning dew sparkled on the grass." }
    ],
    "dailyPhrase": { "en": "See your breath.", "zh": "呼氣成霧（形容天氣真正轉冷）" },
    "cultureTip": "英文常說「It's cold enough to see your breath」，意思是冷到一哈氣就能看見白霧，是寒冬即將到來的生動指標。"
  },

  # 11-03 [國中挑戰]
  {
    "id": "dialogue-1103",
    "date": "11-03",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "社團活動",
    "topic": {
      "en": "Auditioning for the School Drama Club",
      "zh": "參加學校英語話劇社試鏡"
    },
    "situation": "放學後的禮堂舞台旁，Mark 和 Kelly 拿著台詞劇本互相對詞，準備參加年度冬季舞台劇選角。",
    "speakers": {
      "Mark": { "role": "Mark", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Kelly": { "role": "Kelly", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1103.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mark", "avatar": "🧑", "en": "Kelly, my palms are sweating! The drama club director has called five candidates already.", "zh": "Kelly，我手心直冒汗！話劇社指導老師已經叫進去五位候選人了。", "keywords": ["sweating", "director", "candidates"] },
      { "id": 2, "speaker": "Kelly", "avatar": "👧", "en": "Take a slow deep breath, Mark. You have rehearsed this monologue dozens of times.", "zh": "慢慢深呼吸，Mark。這段獨白你已經排練過幾十遍了。", "keywords": ["rehearsed", "monologue"] },
      { "id": 3, "speaker": "Mark", "avatar": "🧑", "en": "What if I get stage fright and completely forget my opening line?", "zh": "要是我突然怯場、完全忘記開場第一句台詞該怎麼辦？", "keywords": ["stage fright", "opening line"] },
      { "id": 4, "speaker": "Kelly", "avatar": "👧", "en": "Just focus on projecting your voice to the back row and connecting with the character's emotion.", "zh": "只要專注把聲音投射到最後一排觀眾席，融入角色的真實情感就行了。", "keywords": ["projecting", "emotion"] },
      { "id": 5, "speaker": "Mark", "avatar": "🧑", "en": "You're right. Next up is my number! Break a leg, Kelly, we've got this!", "zh": "妳說得對。下一個號碼就是我了！祝我們演出順利，我們一定可以的！", "keywords": ["break a leg"] }
    ],
    "vocabulary": [
      { "word": "audition", "phonetic": "/ɑːˈdɪʃ.ən/", "pos": "n./v.", "zh": "試鏡、試音選拔", "example": "Hundreds of students auditioned for the musical lead." },
      { "word": "monologue", "phonetic": "/ˈmɑː.nə.lɑːɡ/", "pos": "n.", "zh": "獨白、長篇演說", "example": "He delivered a dramatic Shakespearean monologue." },
      { "word": "rehearse", "phonetic": "/rəˈhɝːs/", "pos": "v.", "zh": "排練、演練", "example": "The cast rehearsed late into the evening." }
    ],
    "dailyPhrase": { "en": "Break a leg!", "zh": "祝演出順利！（西方表演藝術界的傳統反語祝福，絕不可說 Good luck）" },
    "cultureTip": "在西方劇場界，直接說「Good luck」被視為不吉利的禁忌（Taboo），大家會互道「Break a leg!」來祈求登台演出圓滿順利。"
  },

  # 11-04 [高中進階]
  {
    "id": "dialogue-1104",
    "date": "11-04",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "心理學與成長",
    "topic": {
      "en": "The Neurobiology of Gratitude",
      "zh": "感恩習慣背後的腦神經科學"
    },
    "situation": "高三自習課休息時，Ryan 和 Olivia 討論每天睡前寫下三件感恩小事如何重塑大腦神經迴路。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1104.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "🧑", "en": "Olivia, our counselor suggested keeping a nightly gratitude journal throughout November. Is it actually scientifically backed?", "zh": "Olivia，輔導老師建議我們整個十一月維持寫睡前感恩日記的習慣。這在科學上真的有根據嗎？", "keywords": ["gratitude journal", "scientifically"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👩", "en": "Absolutely. Brain scans reveal that expressing gratitude activates the medial prefrontal cortex, stimulating serotonin and dopamine release.", "zh": "千真萬確。腦部斷層掃描顯示，表達感謝能激活內側前額葉皮質，刺激血清素與多巴胺的分泌。", "keywords": ["prefrontal cortex", "serotonin"] },
      { "id": 3, "speaker": "Ryan", "avatar": "🧑", "en": "So it's not merely wishful positive thinking, but a biological mechanism that rewires neuroplastic pathways?", "zh": "所以這不只是廂情願的正向思考，而是一種真正重塑大腦神經可塑性的生理機制？", "keywords": ["rewires", "neuroplastic"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👩", "en": "Exactly. Human evolution predisposes us to a negativity bias for survival, whereas intentional gratitude trains the brain to spot abundance.", "zh": "正是。人類演化為了生存本能讓我們有負面偏誤，而刻意的感恩能訓練大腦發現身邊的富足與善意。", "keywords": ["negativity bias", "abundance"] },
      { "id": 5, "speaker": "Ryan", "avatar": "🧑", "en": "Starting tonight, I'll jot down three authentic things I appreciate before closing my eyes.", "zh": "從今晚開始，我閉上眼睛前一定要手寫下三件我真心感謝的人事物。", "keywords": ["authentic", "appreciate"] }
    ],
    "vocabulary": [
      { "word": "serotonin", "phonetic": "/ˌser.əˈtoʊ.nɪn/", "pos": "n.", "zh": "血清素（調節情緒與安定心靈的神經遞質）", "example": "Sunlight exposure boosts natural serotonin levels." },
      { "word": "predispose", "phonetic": "/ˌpriː.dɪˈspoʊz/", "pos": "v.", "zh": "使…傾向於、預先影響", "example": "Chronic fatigue predisposes students to irritability." },
      { "word": "abundance", "phonetic": "/əˈbʌn.dəns/", "pos": "n.", "zh": "充裕、豐富、繁榮", "example": "Nature provides an abundance of autumn fruits." }
    ],
    "dailyPhrase": { "en": "Negativity bias.", "zh": "負面偏誤（人類大腦傾向放大壞消息的心理傾向）" },
    "cultureTip": "加州大學戴維斯分校（UC Davis）的 Robert Emmons 教授長期研究證實：持續實踐感恩記錄的人，睡眠品質更佳、免疫力更高且幸福感顯著提升。"
  },

  # 11-05 [國小初階]
  {
    "id": "dialogue-1105",
    "date": "11-05",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "戶外探險",
    "topic": {
      "en": "Jumping into the Pile of Autumn Leaves",
      "zh": "跳進滿滿的金黃落葉堆裡"
    },
    "situation": "週六下午在庭院打掃落葉，Mia 和哥哥 Leo 把金黃色楓葉掃成一座像小山一樣的大堆。",
    "speakers": {
      "Mia": { "role": "Mia", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1105.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mia", "avatar": "👧", "en": "Leo, we raked all the red and yellow leaves into a gigantic mound!", "zh": "Leo，我們把所有紅黃落葉耙成一座超級大的小山丘了！", "keywords": ["raked", "mound"] },
      { "id": 2, "speaker": "Leo", "avatar": "👦", "en": "Are you thinking what I'm thinking? Ready, set, jump!", "zh": "妳是不是也在想跟我一樣的事？各就各位、預備、跳！", "keywords": ["jump"] },
      { "id": 3, "speaker": "Mia", "avatar": "👧", "en": "Wheee! Crash! The leaves are soft like a feather pillow!", "zh": "哇！咚！落葉摸起來好柔軟，就像羽毛枕頭一樣！", "keywords": ["feather", "pillow"] },
      { "id": 4, "speaker": "Leo", "avatar": "👦", "en": "Leaves are scattered in your hair! You look like a leafy woodland fairy!", "zh": "妳頭髮上全黏滿了落葉！看起來超像森林裡的樹葉小仙子！", "keywords": ["woodland", "fairy"] },
      { "id": 5, "speaker": "Mia", "avatar": "👧", "en": "Let's rake them together one more time and leap again!", "zh": "我們再把落葉堆成一堆，然後再跳一次吧！", "keywords": ["leap", "rake"] }
    ],
    "vocabulary": [
      { "word": "rake", "phonetic": "/reɪk/", "pos": "v./n.", "zh": "（用耙子）耙平、落葉耙", "example": "Dad raked the dry leaves off the driveway." },
      { "word": "mound", "phonetic": "/maʊnd/", "pos": "n.", "zh": "土丘、堆、小山峰", "example": "Ants built a mound near the garden fence." },
      { "word": "scatter", "phonetic": "/ˈskæt̬.ɚ/", "pos": "v.", "zh": "散落、撒落", "example": "Wind scattered the papers across the room." }
    ],
    "dailyPhrase": { "en": "Ready, set, jump!", "zh": "各就各位，跳！（充滿童趣的歡樂口號）" },
    "cultureTip": "把落葉堆成大堆然後飛撲跳進去（Jumping in leaf piles），是所有在溫帶氣候長大孩子童年不可或缺的美好回憶！"
  },

  # 11-06 [國小中高]
  {
    "id": "dialogue-1106",
    "date": "11-06",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "校園公益",
    "topic": {
      "en": "The School Charity Book Drive",
      "zh": "校園二手圖書愛心捐贈義賣"
    },
    "situation": "下課時間，Sam 和 Emily 抱著整理好的童話故事書與科普雜誌，送到圖書館門口的愛心捐書箱。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emily": { "role": "Emily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1106.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Emily, I packed eight illustrated adventure books that I outgrew for the book drive.", "zh": "Emily，我把我小時候看過的八本冒險插畫繪本整理好，拿來參加圖書募集活動。", "keywords": ["outgrew", "book drive"] },
      { "id": 2, "speaker": "Emily", "avatar": "👧", "en": "Wonderful! I brought five animal encyclopedia volumes. Where will these books be sent?", "zh": "太棒了！我帶了五冊動物百科全書。這些書會送到哪裡去呢？", "keywords": ["encyclopedia", "volumes"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "The librarian said they will be donated to remote rural elementary schools to build classroom reading corners.", "zh": "圖書館阿姨說會捐贈給偏遠地區的鄉村小學，幫他們搭建班級圖書閱讀角。", "keywords": ["donated", "rural"] },
      { "id": 4, "speaker": "Emily", "avatar": "👧", "en": "Giving gently used books a second life brings stories to children who need them most.", "zh": "讓保存完好的二手書重獲新生，能把好故事帶給最需要它們的孩子們。", "keywords": ["second life", "gently used"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Sharing knowledge is the most powerful gift of all!", "zh": "分享知識真的是世界上最棒、最充滿力量的禮物！", "keywords": ["sharing", "powerful"] }
    ],
    "vocabulary": [
      { "word": "donate", "phonetic": "/doʊˈneɪt/", "pos": "v.", "zh": "捐贈、捐獻", "example": "We donate warm coats to the local shelter." },
      { "word": "encyclopedia", "phonetic": "/ɪnˌsaɪ.kləˈpiː.di.ə/", "pos": "n.", "zh": "百科全書", "example": "He looked up dinosaurs in the encyclopedia." },
      { "word": "rural", "phonetic": "/ˈrʊr.əl/", "pos": "adj.", "zh": "鄉村的、偏遠農村的", "example": "Fresh mountain air characterizes rural life." }
    ],
    "dailyPhrase": { "en": "Give it a second life.", "zh": "賦予它第二生命（二手循環再利用）" },
    "cultureTip": "「Book Drive（募書活動）」常由學校或公益團體在感恩季發起，旨在弭平偏鄉孩童的閱讀資源差距（Reading Equity）。"
  },

  # 11-07 [國中挑戰]
  {
    "id": "dialogue-1107",
    "date": "11-07",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "科技與生活",
    "topic": {
      "en": "Smartphone Battery Life in Chilly Weather",
      "zh": "冬天低溫下手機電池掉電變快了？"
    },
    "situation": "在公車候車亭等車時，Ethan 驚呼自己剛充飽的手機電量竟然莫名驟降，Zoe 從電化學原理向他解釋原因。",
    "speakers": {
      "Ethan": { "role": "Ethan", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1107.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ethan", "avatar": "👦", "en": "Wait, my phone battery percentage just plummeted from seventy to twenty percent in five minutes! Is it broken?", "zh": "等等，我手機電量剛剛五分鐘內突然從百分之七十暴跌到二十！是壞掉了嗎？", "keywords": ["plummeted", "percentage"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Don't panic, it's the cold weather effect! Lithium-ion batteries rely on liquid chemical reactions.", "zh": "別慌，那是天冷效應！鋰離子電池是依靠液態電解液的化學反應運作的。", "keywords": ["lithium-ion", "chemical"] },
      { "id": 3, "speaker": "Ethan", "avatar": "👦", "en": "So when the ambient temperature approaches freezing, the internal electrolyte thickens?", "zh": "所以當環境溫度接近冰點時，內部的電解液流動就會變遲鈍？", "keywords": ["ambient", "electrolyte"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Precisely. Internal resistance spikes, tricking the sensor into registering a low charge.", "zh": "正是如此。內部電阻瞬間飆升，騙過感應晶片以為電量不足。", "keywords": ["resistance", "sensor"] },
      { "id": 5, "speaker": "Ethan", "avatar": "👦", "en": "Aha! If I keep my phone in my inside coat pocket close to body heat, it should recover.", "zh": "原來如此！如果我把手機放進貼近體溫的外套內袋保溫，電量就會恢復了。", "keywords": ["pocket", "recover"] }
    ],
    "vocabulary": [
      { "word": "plummet", "phonetic": "/ˈplʌm.ɪt/", "pos": "v.", "zh": "暴跌、驟降", "example": "Temperatures plummeted below zero overnight." },
      { "word": "ambient", "phonetic": "/ˈæm.bi.ənt/", "pos": "adj.", "zh": "周遭環境的", "example": "The ambient noise made studying difficult." },
      { "word": "electrolyte", "phonetic": "/iˈlek.trə.laɪt/", "pos": "n.", "zh": "電解液、電解質", "example": "Sports drinks replenish lost electrolytes." }
    ],
    "dailyPhrase": { "en": "Body heat.", "zh": "人體體溫（戶外禦寒時最天然的熱源）" },
    "cultureTip": "現代智慧型手機的最佳運作溫度為 0°C 至 35°C。低溫時電池活性減慢，只要回溫後容量就會恢復正常，不會永久損壞。"
  },

  # 11-08 [高中進階]
  {
    "id": "dialogue-1108",
    "date": "11-08",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "哲學思辨",
    "topic": {
      "en": "The Power of Constructive Disagreement",
      "zh": "建設性歧見與思想激盪的力量"
    },
    "situation": "高中辯論社模擬賽結束後，Alex 和 Sophia 探討為何健康的爭論與傾聽反對觀點是追求真理不可或缺的基石。",
    "speakers": {
      "Alex": { "role": "Alex", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Sophia": { "role": "Sophia", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1108.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Alex", "avatar": "🧑", "en": "Sophia, today's debate on universal basic income got pretty heated, yet nobody took it personally.", "zh": "Sophia，今天關於全民基本收入的辯論非常激烈，但大家完全沒有訴諸人身攻擊。", "keywords": ["heated", "personally"] },
      { "id": 2, "speaker": "Sophia", "avatar": "👩", "en": "That's the hallmark of intellectual maturity: attacking the merit of the argument rather than the person behind it.", "zh": "這正是心智成熟的標誌：攻擊論點本身的嚴謹度，而不是針對提出論點的人。", "keywords": ["hallmark", "intellectual", "merit"] },
      { "id": 3, "speaker": "Alex", "avatar": "🧑", "en": "Too often, modern online culture treats disagreement as enmity, creating suffocating echo chambers.", "zh": "現代網路文化往往把意見不同視為敵對，進而形成令人窒息的同溫層回音室。", "keywords": ["enmity", "echo chambers"] },
      { "id": 4, "speaker": "Sophia", "avatar": "👩", "en": "Echo chambers breed fragility. Iron sharpens iron; our beliefs only become robust when tested against rigorous opposition.", "zh": "同溫層只會助長脆弱。玉不琢不成器；我們的信念唯有經過嚴謹反對觀點的淬鍊，才會變得堅韌扎實。", "keywords": ["fragility", "robust", "opposition"] },
      { "id": 5, "speaker": "Alex", "avatar": "🧑", "en": "Cheers to that. Genuine progress requires embracing ideological friction with intellectual humility.", "zh": "完全同意。真正的文明進步，需要以思想上的謙遜來擁抱觀點的良性摩擦。", "keywords": ["friction", "humility"] }
    ],
    "vocabulary": [
      { "word": "hallmark", "phonetic": "/ˈhɑːl.mɑːrk/", "pos": "n.", "zh": "標誌、特徵、品質保證印記", "example": "Attention to detail is the hallmark of great craftsmanship." },
      { "word": "fragility", "phonetic": "/frəˈdʒɪl.ə.t̬i/", "pos": "n.", "zh": "脆弱性、易碎特質", "example": "Overprotection often increases emotional fragility." },
      { "word": "humility", "phonetic": "/hjuːˈmɪl.ə.t̬i/", "pos": "n.", "zh": "謙遜、虛心", "example": "Wisdom begins with intellectual humility." }
    ],
    "dailyPhrase": { "en": "Iron sharpens iron.", "zh": "鐵磨鐵磨出刃；砥礪切磋使彼此更精進（源自箴言經典格言）" },
    "cultureTip": "「Constructive Disagreement（建設性歧見）」是西方高等學術研討的核心價值，旨在透過理性思辨（Socratic Dialogue）讓雙方看見自身思考盲點。"
  },

  # 11-09 [國小初階]
  {
    "id": "dialogue-1109",
    "date": "11-09",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "動物日常",
    "topic": {
      "en": "Bears Getting Ready to Hibernate",
      "zh": "大黑熊吃飽飽準備冬眠"
    },
    "situation": "繪本閱讀課上，Ruby 和 Lucas 正在看一本關於野生動物如何度過寒冷冬天的立體書。",
    "speakers": {
      "Ruby": { "role": "Ruby", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1109.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ruby", "avatar": "👧", "en": "Lucas, look at this picture of a grizzly bear! Why is it eating so much salmon and berries?", "zh": "Lucas，看這張大灰熊的照片！為什麼牠要吃這麼多鮭魚和野生莓果呀？", "keywords": ["grizzly", "salmon"] },
      { "id": 2, "speaker": "Lucas", "avatar": "👦", "en": "It needs to build a thick layer of fat before it enters hibernation for the entire winter.", "zh": "牠必須在進入整整一個冬天的冬眠之前，長出厚厚的一層脂肪。", "keywords": ["hibernation", "layer"] },
      { "id": 3, "speaker": "Ruby", "avatar": "👧", "en": "Does the bear sleep through the winter without waking up to eat?", "zh": "那大熊真的能整個冬天一直睡覺，都不用醒來吃東西嗎？", "keywords": ["waking up"] },
      { "id": 4, "speaker": "Lucas", "avatar": "👦", "en": "Yes! Its heart rate slows down tremendously to conserve energy inside its cozy den.", "zh": "沒錯！牠的心跳會減慢非常多，在溫暖舒適的樹洞巢穴裡節省能量。", "keywords": ["heart rate", "den"] },
      { "id": 5, "speaker": "Ruby", "avatar": "👧", "en": "Sleeping all winter long sounds like the ultimate cozy nap!", "zh": "睡一整個冬天聽起來真的是世界上最棒的溫暖大午睡耶！", "keywords": ["cozy nap"] }
    ],
    "vocabulary": [
      { "word": "hibernate", "phonetic": "/ˈhaɪ.bɚ.neɪt/", "pos": "v.", "zh": "（動物）冬眠", "example": "Bears hibernate in hollow trees or rock caves." },
      { "word": "salmon", "phonetic": "/ˈsæm.ən/", "pos": "n.", "zh": "鮭魚、三文魚（字母 l 不發音）", "example": "Grizzly bears catch fresh salmon in the rushing river." },
      { "word": "den", "phonetic": "/den/", "pos": "n.", "zh": "獸穴、巢穴", "example": "The mother fox protected her cubs inside the den." }
    ],
    "dailyPhrase": { "en": "Conserve energy.", "zh": "節省體力、儲存能量。" },
    "cultureTip": "在英文中「salmon（鮭魚）」的「l」是不發音的（默音），發音為 /ˈsæm.ən/，這是初學英語最容易被糾正的經典單字之一！"
  },

  # 11-10 [國小中高]
  {
    "id": "dialogue-1110",
    "date": "11-10",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "體育健康",
    "topic": {
      "en": "Warming Up Before PE Class",
      "zh": "體育課前做好暖身伸展運動"
    },
    "situation": "初冬上午的操場上，體育股長 Ben 帶著全班同學在做體育課前的動態伸展操。",
    "speakers": {
      "Ben": { "role": "Ben", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Tina": { "role": "Tina", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1110.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ben", "avatar": "👦", "en": "All right team, circle up! Because it's chilly, we must spend a full ten minutes on warm-up drills.", "zh": "好的全班集合成大圈圈！因為今天天氣冷，我們必須做滿整整十分鐘的暖身動作。", "keywords": ["circle up", "warm-up"] },
      { "id": 2, "speaker": "Tina", "avatar": "👧", "en": "Start with arm rotations and ankle rolls to loosen up our joints!", "zh": "先從手臂大風車旋轉和轉腳踝開始，把我們的關節活動開來！", "keywords": ["rotations", "joints"] },
      { "id": 3, "speaker": "Ben", "avatar": "👦", "en": "Now twenty jumping jacks! Get the heart pumping and increase blood flow to cold muscles.", "zh": "現在開合跳二十下！讓心跳加速，把溫暖血液送到冰涼的肌肉裡。", "keywords": ["jumping jacks", "muscles"] },
      { "id": 4, "speaker": "Tina", "avatar": "👧", "en": "Skipping warm-ups in cold weather easily causes painful muscle cramps or pulled tendons.", "zh": "在冷天省略熱身很容易造成疼痛的肌肉抽筋或肌腱拉傷。", "keywords": ["cramps", "tendons"] },
      { "id": 5, "speaker": "Ben", "avatar": "👦", "en": "I feel warm and energized already! Let the dodgeball game begin!", "zh": "我已經覺得全身暖烘烘、充滿活力了！躲避球大賽開始囉！", "keywords": ["energized", "dodgeball"] }
    ],
    "vocabulary": [
      { "word": "rotation", "phonetic": "/roʊˈteɪ.ʃən/", "pos": "n.", "zh": "旋轉、轉動", "example": "Gentle neck rotations relieve stiffness." },
      { "word": "cramp", "phonetic": "/kræmp/", "pos": "n.", "zh": "抽筋、痙攣", "example": "Cold pool water brought on a leg cramp." },
      { "word": "energize", "phonetic": "/ˈen.ɚ.dʒaɪz/", "pos": "v.", "zh": "使精力充沛、注入活力", "example": "A brisk morning jog energizes the whole body." }
    ],
    "dailyPhrase": { "en": "Get the heart pumping.", "zh": "讓心跳加速、熱血沸騰。" },
    "cultureTip": "運動醫學強調「Dynamic Stretching（動態伸展）」遠優於靜態拉筋，透過活動關節與開合跳（Jumping Jacks）能有效提升肌肉核心溫度並預防受傷。"
  },

  # 11-11 [國中挑戰]
  {
    "id": "dialogue-1111",
    "date": "11-11",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "生活反思",
    "topic": {
      "en": "Singles' Day Shopping Fever",
      "zh": "雙十一購物節：真的有需要買嗎？"
    },
    "situation": "午休時間，Mark 和 Kelly 看到手機滿屏的雙十一打折促銷廣告，討論理性消費與避免衝動購物。",
    "speakers": {
      "Mark": { "role": "Mark", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Kelly": { "role": "Kelly", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1111.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mark", "avatar": "🧑", "en": "Kelly, today is November eleventh! Every shopping app is bombarding me with countdown banners and coupons.", "zh": "Kelly，今天是雙十一！每個購物 app 都用倒數橫幅和大額折價券瘋狂轟炸我。", "keywords": ["coupons", "bombarding"] },
      { "id": 2, "speaker": "Kelly", "avatar": "👧", "en": "It creates artificial urgency. They want us to believe we're missing out if we don't purchase right now.", "zh": "這營造了一種人造的急迫感，想讓我們覺得現在不買就虧大了。", "keywords": ["urgency", "missing out"] },
      { "id": 3, "speaker": "Mark", "avatar": "🧑", "en": "I was tempted to buy a fancy wireless keyboard just because it was fifty percent off.", "zh": "我剛剛差點因為打五折就衝動想買一把酷炫的無線鍵盤。", "keywords": ["tempted", "wireless"] },
      { "id": 4, "speaker": "Kelly", "avatar": "👧", "en": "Ask yourself the golden question: would you buy it at full retail price? If not, you're not saving fifty percent; you're wasting fifty percent.", "zh": "問自己這個黃金問題：如果是原價你會買嗎？如果不會，那你不是省了五成，而是浪費了五成。", "keywords": ["retail", "wasting"] },
      { "id": 5, "speaker": "Mark", "avatar": "🧑", "en": "Spot on logic! I'll put my phone away and stick to the 48-hour cooling-off rule.", "zh": "太精闢的邏輯了！我還是把手機收起來，堅持 48 小時冷靜期法則吧。", "keywords": ["cooling-off", "logic"] }
    ],
    "vocabulary": [
      { "word": "coupon", "phonetic": "/ˈkuː.pɑːn/", "pos": "n.", "zh": "優惠券、折價券", "example": "Clip coupons to save money on groceries." },
      { "word": "urgency", "phonetic": "/ˈɝː.dʒən.si/", "pos": "n.", "zh": "急迫性、緊迫感", "example": "Marketers create a sense of urgency to boost sales." },
      { "word": "retail", "phonetic": "/ˈriː.teɪl/", "pos": "n./adj.", "zh": "零售的、原價零售", "example": "The suggested retail price is twenty dollars." }
    ],
    "dailyPhrase": { "en": "Cooling-off rule.", "zh": "冷靜期法則（消費前先暫停 48 小時考慮）" },
    "cultureTip": "行為經濟學指出，商家利用「FOMO（Fear of Missing Out，錯失恐懼症）」製造限量與限時搶購，冷靜期（Cooling-off Period）是打破衝動消費的最佳利器。"
  },

  # 11-12 [高中進階]
  {
    "id": "dialogue-1112",
    "date": "11-12",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "科技與社會",
    "topic": {
      "en": "Algorithmic Bias in Daily Applications",
      "zh": "演算法偏見如何悄悄影響日常生活？"
    },
    "situation": "高中資訊科技研習課上，Ryan 與 Olivia 探討訓練資料偏差如何導致 AI 在徵才面試與信用審查中產生隱性歧視。",
    "speakers": {
      "Ryan": { "role": "Ryan", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Olivia": { "role": "Olivia", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1112.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ryan", "avatar": "🧑", "en": "Olivia, we often assume computer algorithms are purely objective, but recent studies prove they inherit human prejudices.", "zh": "Olivia，我們常以為電腦演算法絕對客觀，但近期研究證實它們全盤繼承了人類的偏見。", "keywords": ["objective", "prejudices"] },
      { "id": 2, "speaker": "Olivia", "avatar": "👩", "en": "Precisely. If an AI resume screening model is trained on historical corporate hiring data dominated by one demographic, it penalizes minority applicants.", "zh": "正是如此。如果 AI 履歷篩選模型是用過去由單一族群主導的歷史招募資料訓練的，它就會自動對少數群體應徵者扣分。", "keywords": ["demographic", "penalizes"] },
      { "id": 3, "speaker": "Ryan", "avatar": "🧑", "en": "Garbage in, garbage out; biased training data inadvertently institutionalizes historical inequality at algorithmic speed.", "zh": "垃圾進，垃圾出；帶有偏見的訓練資料會在不知不覺中以演算法的高速，將歷史上的不平等制度化。", "keywords": ["institutionalizes", "inequality"] },
      { "id": 4, "speaker": "Olivia", "avatar": "👩", "en": "This is why algorithmic auditing and ethical AI regulation are becoming vital fields in modern data science.", "zh": "這就是為什麼演算法審計與倫理 AI 監管，正成為現代資料科學中最不可或缺的核心領域。", "keywords": ["auditing", "regulation"] },
      { "id": 5, "speaker": "Ryan", "avatar": "🧑", "en": "Transparency is non-negotiable. Code that governs human opportunities must be accountable to human dignity.", "zh": "透明度是不容妥協的底線。掌管人類機會與命運的程式碼，必須對人的尊嚴負起責任。", "keywords": ["transparency", "dignity"] }
    ],
    "vocabulary": [
      { "word": "prejudice", "phonetic": "/ˈpredʒ.ə.dɪs/", "pos": "n.", "zh": "偏見、歧視成見", "example": "Education helps dismantle cultural prejudice." },
      { "word": "demographic", "phonetic": "/ˌdem.əˈɡræf.ɪk/", "pos": "n./adj.", "zh": "人口統計的、特定族群特徵", "example": "The survey analyzed diverse demographic groups." },
      { "word": "transparency", "phonetic": "/trænˈspær.ən.si/", "pos": "n.", "zh": "透明度、公開透明", "example": "Public institutions must maintain total transparency." }
    ],
    "dailyPhrase": { "en": "Garbage in, garbage out.", "zh": "輸入錯誤，輸出必然錯誤（電腦科學最著名定律 GIGO）" },
    "cultureTip": "「Algorithmic Bias（演算法偏見）」已成為全球聯合國教科文組織（UNESCO）與歐盟 AI 法案（EU AI Act）監管審查的最核心議題。"
  },

  # 11-13 [國小初階]
  {
    "id": "dialogue-1113",
    "date": "11-13",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "生活自理",
    "topic": {
      "en": "Wearing Gloves and Fuzzy Earmuffs",
      "zh": "戴上手套與毛茸茸的保暖耳罩"
    },
    "situation": "冬日早晨出門前，媽媽拿出一對粉紅色的毛茸茸耳罩和針織手套給 Zoe 戴上。",
    "speakers": {
      "Mom": { "role": "媽媽", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1113.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Mom", "avatar": "👩", "en": "Zoe, come here! It is windy today, so put on these fuzzy earmuffs.", "zh": "Zoe，過來這邊！今天風很大，把這個毛茸茸的耳罩戴上。", "keywords": ["fuzzy", "earmuffs"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "They look like two little white bunnies resting on my ears!", "zh": "它們看起來就像兩隻小白兔趴在我的耳朵上休息一樣！", "keywords": ["bunnies", "ears"] },
      { "id": 3, "speaker": "Mom", "avatar": "👩", "en": "And here are your matching knitted mittens. Slip your thumbs into the side pockets.", "zh": "還有妳同套的針織連指手套，把大拇指滑進旁邊的小孔裡。", "keywords": ["mittens", "thumbs"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "Look Mom, my hands look like gentle bear paws! No freezing wind can touch me now!", "zh": "媽媽看，我的手看起來像溫柔的小熊掌！現在再冷的風也吹不到我了！", "keywords": ["paws", "freezing"] },
      { "id": 5, "speaker": "Mom", "avatar": "👩", "en": "Snug as a bug in a rug! Now you are fully ready for the school bus.", "zh": "溫暖舒服得不得了！現在妳完全準備好去搭校車囉。", "keywords": ["snug", "school bus"] }
    ],
    "vocabulary": [
      { "word": "earmuffs", "phonetic": "/ˈɪr.mʌfs/", "pos": "n.", "zh": "防寒耳罩", "example": "Wear earmuffs to keep your ears warm in winter." },
      { "word": "mittens", "phonetic": "/ˈmɪt.ənz/", "pos": "n.", "zh": "連指手套（拇指分開、其餘四指合在一起）", "example": "Toddlers usually wear mittens rather than gloves." },
      { "word": "snug", "phonetic": "/snʌɡ/", "pos": "adj.", "zh": "溫暖舒適的、緊密貼合的", "example": "The baby fell asleep, snug under the quilt." }
    ],
    "dailyPhrase": { "en": "Snug as a bug in a rug.", "zh": "溫暖舒服極了、無比愜意（英語最著名的可愛童謠成語）" },
    "cultureTip": "「Mittens（連指手套）」與「Gloves（五指分開的手套）」不同。連指手套讓四指聚集在一起互相傳遞體溫，在極寒環境下的保暖效果遠比五指手套更出色！"
  },

  # 11-14 [國中挑戰]
  {
    "id": "dialogue-1114",
    "date": "11-14",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "自然科學",
    "topic": {
      "en": "Why Do Evergreen Trees Stay Green?",
      "zh": "為什麼松樹常青不會掉光葉子？"
    },
    "situation": "生物園區參觀時，Sarah 和 Jake 停在幾棵高聳的松樹前，好奇楓樹葉子掉光了，而松樹卻依然翠綠挺拔。",
    "speakers": {
      "Sarah": { "role": "Sarah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Jake": { "role": "Jake", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1114.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Jake", "avatar": "👦", "en": "Sarah, all the oak and maple trees have shed their leaves, but these pine trees are completely green!", "zh": "Sarah，橡樹和楓樹的葉子都掉光了，但這些松樹居然還是整棵鬱鬱蔥蔥！", "keywords": ["pine trees", "shed"] },
      { "id": 2, "speaker": "Sarah", "avatar": "👧", "en": "That's why they are called evergreens! Touch their needle-shaped leaves; what do you feel?", "zh": "這就是為什麼它們被稱為常青樹！摸摸它們針狀的葉子，你有什麼感覺？", "keywords": ["evergreens", "needle"] },
      { "id": 3, "speaker": "Jake", "avatar": "👦", "en": "They feel waxy and stiff, not soft like broad maple leaves.", "zh": "摸起來硬挺挺的，而且表面有一層滑滑的蠟質，不像寬大的楓樹葉那麼軟。", "keywords": ["waxy", "stiff"] },
      { "id": 4, "speaker": "Sarah", "avatar": "👧", "en": "That waxy coating and narrow surface area prevent precious moisture from evaporating in dry winter winds.", "zh": "那層蠟質保護膜與狹窄的表面積，能防止珍貴的水分在乾燥的寒冬風中蒸發掉。", "keywords": ["evaporating", "coating"] },
      { "id": 5, "speaker": "Jake", "avatar": "👦", "en": "Nature's evolutionary engineering is sheer genius!", "zh": "大自然在生物演化上的工程設計真的太絕妙了！", "keywords": ["evolutionary", "genius"] }
    ],
    "vocabulary": [
      { "word": "evergreen", "phonetic": "/ˈev.ɚ.ɡriːn/", "pos": "n./adj.", "zh": "常青樹、萬年青", "example": "Pine and spruce are common evergreen conifers." },
      { "word": "waxy", "phonetic": "/ˈwæk.si/", "pos": "adj.", "zh": "如蠟般的、蠟質的", "example": "The waxy layer prevents water loss from the plant." },
      { "word": "evaporate", "phonetic": "/ɪˈvæp.ə.reɪt/", "pos": "v.", "zh": "蒸發、化為氣體", "example": "Puddles evaporate quickly under bright sunshine." }
    ],
    "dailyPhrase": { "en": "Sheer genius.", "zh": "純粹的天才設計、絕妙無比。" },
    "cultureTip": "落葉樹（Deciduous trees）冬天落葉是為了休眠省水；而常青針葉樹（Evergreen Conifers）透過針狀葉與抗凍樹脂（Antifreeze Sap），在冰雪覆蓋下依然能進行光合作用。"
  },

  # 11-15 [國小中高]
  {
    "id": "dialogue-1115",
    "date": "11-15",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "校園生活",
    "topic": {
      "en": "The Golden Rule of Friendship",
      "zh": "與同學相處的黃金友誼法則"
    },
    "situation": "午休時間，看到兩位同組同學因為搶同一顆籃球鬧彆扭，Leo 和 Emma 過去溫和開導調解。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1115.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Emma, arguing over who shoots the basketball first is silly. Why don't they take turns?", "zh": "Emma，為了爭誰先投籃球而吵架太傻了。他們為什麼不輪流投呢？", "keywords": ["arguing", "take turns"] },
      { "id": 2, "speaker": "Emma", "avatar": "👧", "en": "People sometimes forget the Golden Rule: treat others the way you want to be treated.", "zh": "大家有時候會忘了黃金法則：己所不欲，勿施於人，你想別人怎麼對待你，你就怎麼對待別人。", "keywords": ["Golden Rule", "treated"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "Exactly. Nobody likes being yelled at or pushed around during recess.", "zh": "沒錯。下課時間沒有人喜歡被大聲吼叫或被推擠。", "keywords": ["recess", "yelled"] },
      { "id": 4, "speaker": "Emma", "avatar": "👧", "en": "Let's invite them to play a friendly three-point shooting contest together.", "zh": "我們邀請他們一起來玩一場友誼三分球定點投籃賽吧。", "keywords": ["contest", "friendly"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Turn conflict into cooperation! That's what real champions do.", "zh": "把衝突化為合作！這才是真正球場冠軍該有的風範。", "keywords": ["conflict", "cooperation"] }
    ],
    "vocabulary": [
      { "word": "conflict", "phonetic": "/ˈkɑːn.flɪkt/", "pos": "n.", "zh": "衝突、爭端", "example": "Calm communication helps resolve daily conflict." },
      { "word": "cooperation", "phonetic": "/koʊˌɑː.pəˈreɪ.ʃən/", "pos": "n.", "zh": "合作、協力", "example": "Successful missions require close team cooperation." },
      { "word": "recess", "phonetic": "/ˈriː.ses/", "pos": "n.", "zh": "（學校）下課休息時間", "example": "Children ran happily to the playground at recess." }
    ],
    "dailyPhrase": { "en": "The Golden Rule.", "zh": "黃金法則（待人如己的崇高道德準則）" },
    "cultureTip": "「The Golden Rule」在西方文明跨越宗教與哲學，核心名言是「Do unto others as you would have them do unto you」，是校園品格教育的核心理念。"
  },

  # 11-16 [國中挑戰]
  {
    "id": "dialogue-1116",
    "date": "11-16",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "飲食健康",
    "topic": {
      "en": "Craving Warm Comfort Food in Winter",
      "zh": "冬日療癒美食：暖胃又暖心的熱湯"
    },
    "situation": "週日降溫的傍晚，Hannah 和媽媽在廚房燉煮一鍋濃郁的玉米濃湯與現烤香蒜麵包片。",
    "speakers": {
      "Hannah": { "role": "Hannah", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Mom": { "role": "媽媽", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1116.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Hannah", "avatar": "👧", "en": "Mom, hearing the chilly wind howl outside makes me crave comfort food so intensely!", "zh": "媽媽，聽著外面寒風呼呼作響，讓我特別渴望吃暖呼呼的療癒美食！", "keywords": ["comfort food", "howl"] },
      { "id": 2, "speaker": "Mom", "avatar": "👩", "en": "That's why I'm simmering a big pot of creamy sweet corn chowder with diced potatoes.", "zh": "所以我正在文火慢燉一大鍋加了馬鈴薯丁的香濃甜玉米濃湯呀。", "keywords": ["simmering", "chowder"] },
      { "id": 3, "speaker": "Hannah", "avatar": "👧", "en": "Can I toast thick sourdough bread slices and rub fresh garlic butter over them?", "zh": "我可以把厚切酸種麵包烤得脆脆的，然後抹上新鮮大蒜奶油嗎？", "keywords": ["sourdough", "garlic butter"] },
      { "id": 4, "speaker": "Mom", "avatar": "👩", "en": "Dipping warm crunchy garlic bread into velvety soup is the ultimate winter solace.", "zh": "把溫熱酥脆的大蒜麵包沾進絲滑濃湯裡，真的是冬天最至高無上的心靈撫慰。", "keywords": ["velvety", "solace"] },
      { "id": 5, "speaker": "Hannah", "avatar": "👧", "en": "Family dinners on cold November evenings are the coziest moments in the world.", "zh": "在十一月寒涼的夜晚一家人圍坐吃晚餐，真的是全世界最溫暖的時刻了。", "keywords": ["coziest", "evenings"] }
    ],
    "vocabulary": [
      { "word": "simmer", "phonetic": "/ˈsɪm.ɚ/", "pos": "v.", "zh": "文火慢燉、小火慢熬", "example": "Simmer the beef stew for two hours." },
      { "word": "chowder", "phonetic": "/ˈtʃaʊ.dɚ/", "pos": "n.", "zh": "（加有蔬菜海鮮的）稠濃湯", "example": "New England clam chowder is creamy and savory." },
      { "word": "solace", "phonetic": "/ˈsɑː.lɪs/", "pos": "n.", "zh": "撫慰、慰藉", "example": "Listening to classical music brings peaceful solace." }
    ],
    "dailyPhrase": { "en": "Comfort food.", "zh": "撫慰心靈的療癒美食（通常是暖胃有家常溫度的料理）" },
    "cultureTip": "「Comfort food」是指那些能喚起童年美好回憶、帶來強烈安全感與幸福感的高碳水或暖胃料理，如肉醬起司通心粉（Mac & Cheese）或香濃雞湯。"
  },

  # 11-17 [國小初階]
  {
    "id": "dialogue-1117",
    "date": "11-17",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "生活美德",
    "topic": {
      "en": "Three Magic Words: Please, Thank You, Sorry",
      "zh": "三句有禮貌的神奇魔力小咒語"
    },
    "situation": "在校園走廊轉角，Sam 不小心撞到了 Eric，兩位小朋友互相禮貌道歉與道謝。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Eric": { "role": "Eric", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1117.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Oops! I'm so sorry, Eric! I didn't see you around the corner.", "zh": "哎呀！真對不起 Eric！我剛才轉彎沒看到你。", "keywords": ["sorry", "corner"] },
      { "id": 2, "speaker": "Eric", "avatar": "👦", "en": "That's okay, Sam! Nobody got hurt. Here, let me help you pick up your books.", "zh": "沒關係 Sam！沒有人受傷。來，我幫你把掉在地上的書撿起來。", "keywords": ["pick up", "hurt"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Thank you so much! You are very kind.", "zh": "太謝謝你了！你真貼心。", "keywords": ["thank you", "kind"] },
      { "id": 4, "speaker": "Eric", "avatar": "👦", "en": "You're welcome! Polite words are like magic keys that open happy hearts.", "zh": "不客氣！有禮貌的話就像神奇鑰匙，能打開快樂的心門。", "keywords": ["keys", "polite"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "'Please', 'Thank you', and 'I'm sorry' make every day brighter!", "zh": "『請』、『謝謝』和『對不起』，讓每一天都變得更美好！", "keywords": ["brighter", "magic words"] }
    ],
    "vocabulary": [
      { "word": "polite", "phonetic": "/pəˈlaɪt/", "pos": "adj.", "zh": "有禮貌的、彬彬有禮的", "example": "Polite manners make a lasting positive impression." },
      { "word": "corner", "phonetic": "/ˈkɔːr.nɚ/", "pos": "n.", "zh": "轉角、角落", "example": "Slow down when turning the hallway corner." },
      { "word": "brighter", "phonetic": "/ˈbraɪ.t̬ɚ/", "pos": "adj.", "zh": "更光明的、更燦爛的", "example": "Her cheerful laughter made the room brighter." }
    ],
    "dailyPhrase": { "en": "The three magic words.", "zh": "三句有禮貌的神奇魔語（Please, Thank You, Sorry）" },
    "cultureTip": "在美語幼兒園與小學教室，老師一定會教「The Magic Words」（魔法咒語）：Please（請）、Thank you（謝謝）、I'm sorry（對不起），是人際潤滑的黃金法寶。"
  },

  # 11-18 [高中進階]
  {
    "id": "dialogue-1118",
    "date": "11-18",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "社會公益",
    "topic": {
      "en": "Combating Food Waste Through Food Banks",
      "zh": "惜食共享：食物銀行如何對抗糧食浪費？"
    },
    "situation": "高三扶輪少年服務團課後，Grace 和 Leo 討論即將在感恩節週籌辦的社區食物銀行食物募捐箱活動。",
    "speakers": {
      "Grace": { "role": "Grace", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" },
      "Leo": { "role": "Leo", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1118.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Grace", "avatar": "👩", "en": "Leo, it's paradoxical that roughly one-third of all food produced globally is wasted, while millions experience food insecurity.", "zh": "Leo，全球生產的糧食約有三分之一被白白浪費，同時卻有數百萬人面臨糧食匱乏，這現象真令人感到諷刺矛盾。", "keywords": ["paradoxical", "insecurity"] },
      { "id": 2, "speaker": "Leo", "avatar": "🧑", "en": "It's largely a logistics and distribution failure. Supermarkets discard cosmetic 'ugly' produce that is entirely nutritious and safe.", "zh": "這很大程度上是物流與分配機制的失敗。超市經常丟棄僅僅外觀不完美、但營養完全無損且安全的『醜蔬果』。", "keywords": ["cosmetic", "distribution"] },
      { "id": 3, "speaker": "Grace", "avatar": "👩", "en": "Our Interact club can partner with local food banks to collect non-perishable canned goods, rice, and oats before Thanksgiving.", "zh": "我們的少年扶輪社可以在感恩節前與在地食物銀行合作，募集不易腐壞的罐頭食品、白米和燕麥片。", "keywords": ["non-perishable", "food banks"] },
      { "id": 4, "speaker": "Leo", "avatar": "🧑", "en": "We should also promote apps that connect neighborhood bakeries with consumers to sell surplus bread at heavy discounts before closing.", "zh": "我們還可以推廣惜食 app，把社區麵包店打烊前多餘未售出的麵包以超低折價提供給需要的民眾。", "keywords": ["surplus", "discounts"] },
      { "id": 5, "speaker": "Grace", "avatar": "👩", "en": "Dignified food rescue transforms surplus into solidarity. Let's draft our volunteer shift schedule.", "zh": "維護尊嚴的食物救援，能把過剩資源化為社會團結互助的暖流。我們現在就來排志工值班表吧。", "keywords": ["solidarity", "rescue"] }
    ],
    "vocabulary": [
      { "word": "paradoxical", "phonetic": "/ˌper.əˈdɑːk.sɪ.kəl/", "pos": "adj.", "zh": "矛盾的、似是而非的", "example": "It is paradoxical that modern technology can isolate people." },
      { "word": "surplus", "phonetic": "/ˈsɝː.pləs/", "pos": "n./adj.", "zh": "過剩的、剩餘物資", "example": "The farm donated its surplus crop to charity." },
      { "word": "solidarity", "phonetic": "/ˌsɑː.lɪˈder.ə.t̬i/", "pos": "n.", "zh": "團結一致、互助同心", "example": "Neighbors demonstrated inspiring solidarity during the crisis." }
    ],
    "dailyPhrase": { "en": "Non-perishable goods.", "zh": "不易腐壞的耐久乾貨食品（食物銀行最歡迎的捐贈品）" },
    "cultureTip": "「Food Bank（食物銀行）」是現代社會安全網的重要基石。捐贈非易腐罐頭（Canned Goods）與全穀燕麥，是歐美感恩季最普遍有意義的社區參與方式。"
  },

  # 11-19 [國小中高]
  {
    "id": "dialogue-1119",
    "date": "11-19",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "趣味歷史",
    "topic": {
      "en": "The Story of the First Thanksgiving",
      "zh": "第一屆感恩節的歷史小故事"
    },
    "situation": "社會課分組討論時，Ken 和 Emma 正在看 1621 年五月花號移民與原住民 Wampanoag 共享秋收盛宴的插畫。",
    "speakers": {
      "Ken": { "role": "Ken", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1119.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Ken", "avatar": "👦", "en": "Emma, did you know the first Thanksgiving in 1621 lasted three whole days?", "zh": "Emma，妳知道 1621 年的第一屆感恩節居然連續慶祝了整整三天嗎？", "keywords": ["Thanksgiving", "1621"] },
      { "id": 2, "speaker": "Emma", "avatar": "👧", "en": "Yes! The Pilgrims and the Wampanoag Native Americans gathered to celebrate their successful autumn harvest.", "zh": "知道！清教徒移民和美洲原住民萬帕諾亞格人聚在一起，慶祝他們豐碩的秋收成果。", "keywords": ["Pilgrims", "harvest"] },
      { "id": 3, "speaker": "Ken", "avatar": "👦", "en": "Did they eat roast turkey with cranberry sauce like we do today?", "zh": "那他們當時也是像我們現在一樣吃烤火雞配蔓越莓醬嗎？", "keywords": ["turkey", "cranberry"] },
      { "id": 4, "speaker": "Emma", "avatar": "👧", "en": "Historians say their feast featured wild fowl, venison, cornmeal bread, and freshly caught lobsters!", "zh": "歷史學家說他們的盛宴菜單包含了野禽、鹿肉、玉米麵包，還有剛捕撈的新鮮大龍蝦呢！", "keywords": ["venison", "lobsters"] },
      { "id": 5, "speaker": "Ken", "avatar": "👦", "en": "Lobster at Thanksgiving? That sounds deliciously unexpected!", "zh": "感恩節吃龍蝦？聽起來真是出乎意料地美味呀！", "keywords": ["unexpected", "deliciously"] }
    ],
    "vocabulary": [
      { "word": "harvest", "phonetic": "/ˈhɑːr.vəst/", "pos": "n./v.", "zh": "收成、收割、秋收", "example": "Farmers celebrated a bountiful grain harvest." },
      { "word": "feast", "phonetic": "/fiːst/", "pos": "n.", "zh": "盛宴、宴席", "example": "The royal banquet was a magnificent feast." },
      { "word": "venison", "phonetic": "/ˈven.ə.sən/", "pos": "n.", "zh": "鹿肉", "example": "Venison was a traditional staple for early settlers." }
    ],
    "dailyPhrase": { "en": "Celebrate the harvest.", "zh": "慶祝豐收、歡慶秋收盛宴。" },
    "cultureTip": "1621 年 Plymouth 的第一屆感恩盛宴上，由於當時糖非常昂貴匱乏，所以根本沒有現在常見的蔓越莓醬（Cranberry sauce）或甜南瓜派喔！"
  },

  # 11-20 [國中挑戰]
  {
    "id": "dialogue-1120",
    "date": "11-20",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "節慶盛事",
    "topic": {
      "en": "Watching the Giant Balloons at Macy's Parade",
      "zh": "欣賞梅西感恩節大遊行的巨型氣球"
    },
    "situation": "感恩節前夕，Kevin 和 David 在看電視預告紐約曼哈頓即將登場的梅西百貨感恩節大遊行巨型卡通氣球。",
    "speakers": {
      "Kevin": { "role": "Kevin", "avatar": "🧑", "gender": "male", "voice": "en-US-ChristopherNeural" },
      "David": { "role": "David", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1120.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Kevin", "avatar": "🧑", "en": "David, the Macy's Thanksgiving Day Parade will be broadcast live next Thursday morning!", "zh": "David，梅西百貨感恩節大遊行下週四上午就要全球實況轉播了！", "keywords": ["parade", "broadcast"] },
      { "id": 2, "speaker": "David", "avatar": "👦", "en": "I love the colossal helium character balloons floating between the Manhattan skyscrapers!", "zh": "我超愛看那些在曼哈頓摩天大樓之間飄揚穿梭的超巨大氦氣卡通角色氣球！", "keywords": ["helium", "colossal", "skyscrapers"] },
      { "id": 3, "speaker": "Kevin", "avatar": "🧑", "en": "Each giant balloon requires up to ninety handlers holding long tether ropes on the ground.", "zh": "每一個巨型氣球地面上都需要多達九十位工作人員緊緊拉著長長的安全繩索呢。", "keywords": ["handlers", "tether"] },
      { "id": 4, "speaker": "David", "avatar": "👦", "en": "If gusts of wind hit, keeping those four-story-tall balloons stable is serious teamwork.", "zh": "要是碰上陣風吹拂，要維持四層樓高的巨大氣球平穩真的考驗超級團隊默契。", "keywords": ["stable", "gusts"] },
      { "id": 5, "speaker": "Kevin", "avatar": "🧑", "en": "Watching the parade in our pajamas while eating breakfast is my absolute favorite holiday tradition.", "zh": "穿著睡衣一邊吃早餐一邊看大遊行，絕對是我最愛的感恩節傳統。", "keywords": ["pajamas", "tradition"] }
    ],
    "vocabulary": [
      { "word": "colossal", "phonetic": "/kəˈlɑː.səl/", "pos": "adj.", "zh": "龐大無比的、極巨大的", "example": "The museum displays a colossal dinosaur skeleton." },
      { "word": "tether", "phonetic": "/ˈteð.ɚ/", "pos": "n./v.", "zh": "拴繩、繫繩、拴住", "example": "Keep the boat tethered securely to the dock." },
      { "word": "tradition", "phonetic": "/trəˈdɪʃ.ən/", "pos": "n.", "zh": "傳統、習俗", "example": "Lighting lanterns is a cherished holiday tradition." }
    ],
    "dailyPhrase": { "en": "A holiday tradition.", "zh": "節日不可或缺的溫馨傳統習俗。" },
    "cultureTip": "「Macy's Thanksgiving Day Parade」自 1924 年開辦，每年吸引超過 350 萬現場觀眾與 5000 萬電視觀眾收看，象徵美國聖誕冬季假期季正式鳴槍起跑！"
  },

  # 11-21 [國小初階]
  {
    "id": "dialogue-1121",
    "date": "11-21",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "感恩手作",
    "topic": {
      "en": "Tracing My Hand Turkey",
      "zh": "用小手掌畫出可愛火雞"
    },
    "situation": "美術課上，Anna 示範如何把自己的手掌平貼在圖畫紙上，用鉛筆描邊畫出經典的手掌小火雞。",
    "speakers": {
      "Anna": { "role": "Anna", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Tim": { "role": "Tim", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1121.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Anna", "avatar": "👧", "en": "Tim, let's make a cute Hand Turkey craft for Thanksgiving!", "zh": "Tim，我們來做一個可愛的手掌火雞感恩節勞作吧！", "keywords": ["hand turkey", "craft"] },
      { "id": 2, "speaker": "Tim", "avatar": "👦", "en": "How do you turn a hand into a turkey bird?", "zh": "要把手掌怎麼變成一隻火雞呢？", "keywords": ["turn into"] },
      { "id": 3, "speaker": "Anna", "avatar": "👧", "en": "Place your hand flat on the paper and spread your fingers wide like feathers!", "zh": "把手平平放在紙上，把手指張開得像漂亮的羽毛一樣！", "keywords": ["spread", "feathers"] },
      { "id": 4, "speaker": "Tim", "avatar": "👦", "en": "The thumb is the turkey's head and neck! Now I trace with my brown crayon.", "zh": "大拇指是火雞的頭和脖子！現在我用咖啡色蠟筆描出輪廓。", "keywords": ["thumb", "trace"] },
      { "id": 5, "speaker": "Anna", "avatar": "👧", "en": "Color each finger feather red, orange, and yellow. It looks adorably charming!", "zh": "把每一根手指羽毛塗上紅色、橘色和黃色。看起來真是可愛極了！", "keywords": ["adorably", "charming"] }
    ],
    "vocabulary": [
      { "word": "trace", "phonetic": "/treɪs/", "pos": "v.", "zh": "沿輪廓描繪、描摹", "example": "Trace the outline of your hand with a pencil." },
      { "word": "feather", "phonetic": "/ˈfeð.ɚ/", "pos": "n.", "zh": "羽毛", "example": "Peacocks display dazzling iridescent feathers." },
      { "word": "adorably", "phonetic": "/əˈdɔːr.ə.bli/", "pos": "adv.", "zh": "可愛地、討人喜愛地", "example": "The puppy tilted its head adorably." }
    ],
    "dailyPhrase": { "en": "Spread your fingers.", "zh": "張開你的手指頭。" },
    "cultureTip": "「Hand Turkey」是北美小學幼稚園每年十一月家喻戶曉的傳統美術勞作，小手掌描成火雞、寫上感恩感謝的話，送給父母珍藏。"
  },

  # 11-22 [高中進階]
  {
    "id": "dialogue-1122",
    "date": "11-22",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "哲學反思",
    "topic": {
      "en": "Gratitude vs. Toxic Positivity",
      "zh": "真正的感恩與「有毒正能量」的界線"
    },
    "situation": "高三班會課後，Jason 和 Chloe 探討強迫自己隨時樂觀的「有毒正向」危害，以及如何真誠接納負面情緒。",
    "speakers": {
      "Jason": { "role": "Jason", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Chloe": { "role": "Chloe", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1122.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Jason", "avatar": "🧑", "en": "Chloe, whenever someone is feeling overwhelmed, telling them to 'just look on the bright side' often feels dismissive.", "zh": "Chloe，每當有人感到快被生活壓垮時，叫他們『看開點、想好的那一面』往往讓人感覺被敷衍否定。", "keywords": ["dismissive", "bright side"] },
      { "id": 2, "speaker": "Chloe", "avatar": "👩", "en": "That's textbook toxic positivity. It invalidates genuine human pain, grief, and justified anger.", "zh": "那是教科書級的『有毒正能量』。它否定並抹煞了真實的人性痛苦、悲傷與正當憤怒。", "keywords": ["toxic positivity", "invalidates"] },
      { "id": 3, "speaker": "Jason", "avatar": "🧑", "en": "So how does authentic gratitude differ from suppressing negative emotions?", "zh": "那麼，真誠的感恩與壓抑負面情緒之間到底有什麼本質區別？", "keywords": ["authentic", "suppressing"] },
      { "id": 4, "speaker": "Chloe", "avatar": "👩", "en": "Authentic gratitude coexists with sorrow. You can acknowledge hardship while simultaneously appreciating small anchors of kindness.", "zh": "真正的感恩能與悲傷共存。你可以坦然承認困境與艱難，同時由衷感謝那些支撐你的微小善意。", "keywords": ["hardship", "simultaneously"] },
      { "id": 5, "speaker": "Jason", "avatar": "🧑", "en": "I love that nuance. We don't have to put on a phony smile to cultivate sincere thankfulness.", "zh": "我喜歡這個細膩的分界。我們不必戴著虛假強顏歡笑的假面具，也能培養真摯的感謝之心。", "keywords": ["nuance", "phony"] }
    ],
    "vocabulary": [
      { "word": "dismissive", "phonetic": "/dɪˈsmɪs.ɪv/", "pos": "adj.", "zh": "輕蔑的、不屑一顧的、敷衍的", "example": "A dismissive wave of the hand offended the guest." },
      { "word": "invalidate", "phonetic": "/ɪnˈvæl.ə.deɪt/", "pos": "v.", "zh": "使無效、否定（他人感受）", "example": "Never invalidate a friend's honest emotional distress." },
      { "word": "nuance", "phonetic": "/ˈnuː.ɑːns/", "pos": "n.", "zh": "細微差異、微妙之處", "example": "Understanding linguistic nuances requires deep cultural empathy." }
    ],
    "dailyPhrase": { "en": "Look on the bright side.", "zh": "看開點、往好的方面看（若在對方悲傷時過度使用易淪為有毒正能量）" },
    "cultureTip": "心理學名詞「Toxic Positivity（有毒正能量）」指過度要求維持正向表象，強行壓抑憤怒或悲傷等健康情緒，反而導致更嚴重的心理內耗。"
  },

  # 11-23 [國小中高]
  {
    "id": "dialogue-1123",
    "date": "11-23",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "感恩廚房",
    "topic": {
      "en": "Making Tangy Cranberry Sauce",
      "zh": "在廚房煮酸甜濃郁的蔓越莓醬"
    },
    "situation": "感恩節前一天下午，Lucas 在廚房幫媽媽把一顆顆紅艷的生鮮蔓越莓倒入鍋中熬煮果醬。",
    "speakers": {
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Mom": { "role": "媽媽", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1123.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lucas", "avatar": "👦", "en": "Mom, listen to that! The fresh cranberries are making popping sounds inside the pot!", "zh": "媽媽快聽！鍋子裡新鮮的蔓越莓一顆顆發出嗶嗶啵啵破掉的聲音耶！", "keywords": ["cranberries", "popping"] },
      { "id": 2, "speaker": "Mom", "avatar": "👩", "en": "That's their skins bursting open as natural pectin is released to thicken our sauce.", "zh": "那是果皮受熱爆開，釋放天然果膠讓醬汁變得濃稠濃郁。", "keywords": ["pectin", "thicken"] },
      { "id": 3, "speaker": "Lucas", "avatar": "👦", "en": "Can I stir in this cup of freshly squeezed orange juice and grated orange zest?", "zh": "我能把這一杯現榨柳橙汁和刨好的橘子皮屑倒進去攪拌嗎？", "keywords": ["zest", "stir"] },
      { "id": 4, "speaker": "Mom", "avatar": "👩", "en": "Yes! Citrus zest gives our ruby red sauce an irresistible bright holiday aroma.", "zh": "可以！柑橘皮屑會賦予我們這鍋寶石紅果醬一股讓人無法抗拒的節慶明亮香氣。", "keywords": ["citrus", "aroma"] },
      { "id": 5, "speaker": "Lucas", "avatar": "👦", "en": "Homemade cranberry sauce beats canned jelly by a thousand miles!", "zh": "自己現煮的蔓越莓果醬，比市售鐵罐頭果凍好吃上一千倍！", "keywords": ["homemade", "beats"] }
    ],
    "vocabulary": [
      { "word": "cranberry", "phonetic": "/ˈkræn.ber.i/", "pos": "n.", "zh": "蔓越莓、小紅莓", "example": "Cranberry juice is delightfully tart and sweet." },
      { "word": "zest", "phonetic": "/zest/", "pos": "n.", "zh": "柑橘類果皮碎屑、熱情熱忱", "example": "Add grated lemon zest to enhance the cake flavor." },
      { "word": "pectin", "phonetic": "/ˈpek.tɪn/", "pos": "n.", "zh": "果膠", "example": "Apples and cranberries naturally contain high pectin." }
    ],
    "dailyPhrase": { "en": "Beat it by a thousand miles.", "zh": "勝過千百倍、遠遠超越。" },
    "cultureTip": "蔓越莓（Cranberry）是少數原生於北美大陸的水果之一，酸甜的蔓越莓醬能中和烤火雞肉的油脂，是感恩節大餐不可或缺的靈魂配醬。"
  },

  # 11-24 [國中挑戰]
  {
    "id": "dialogue-1124",
    "date": "11-24",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "感恩節慶",
    "topic": {
      "en": "Happy Thanksgiving! The Family Feast",
      "zh": "感恩節快樂！溫馨全家團圓盛宴"
    },
    "situation": "感恩節當晚，全家人圍坐在溫暖的餐桌旁，Tyler 和表姐 Zoe 在切烤火雞前輪流分享今年最感謝的事情。",
    "speakers": {
      "Tyler": { "role": "Tyler", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1124.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Tyler", "avatar": "👦", "en": "Happy Thanksgiving, Zoe! Look at that golden-brown roast turkey in the center of the table!", "zh": "感恩節快樂 Zoe！看餐桌正中央那隻烤得金黃焦香的大火雞！", "keywords": ["Happy Thanksgiving", "roast turkey"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "And grandma's legendary herb stuffing, creamy mashed potatoes, and warm gravy boat!", "zh": "還有外婆傳奇的香草烤麵包填料、綿密馬鈴薯泥，以及熱騰騰的肉汁船壺！", "keywords": ["stuffing", "gravy"] },
      { "id": 3, "speaker": "Tyler", "avatar": "👦", "en": "Before we carve the drumsticks, let's go around the table and each share one thing we are grateful for.", "zh": "在切大火雞腿之前，我們先輪流繞著桌子，每個人分享一件今年最感恩的事吧。", "keywords": ["carve", "grateful"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "I am deeply grateful for our family's good health and all the loving support during tough exam weeks.", "zh": "我由衷感謝我們全家人身體健康，以及在段考壓力大的那幾週大家給我的滿滿溫暖支持。", "keywords": ["health", "support"] },
      { "id": 5, "speaker": "Tyler", "avatar": "👦", "en": "Hear, hear! Pass the cranberry sauce, and let's dig into this magnificent feast!", "zh": "贊成！把蔓越莓醬遞過來，讓我們好好享用這頓豐盛大餐吧！", "keywords": ["magnificent", "dig into"] }
    ],
    "vocabulary": [
      { "word": "stuffing", "phonetic": "/ˈstʌf.ɪŋ/", "pos": "n.", "zh": "（火雞或禽類內部的）填料、餡料", "example": "The herb stuffing seasoned with sage smelled heavenly." },
      { "word": "gravy", "phonetic": "/ˈɡreɪ.vi/", "pos": "n.", "zh": "肉汁醬、調味肉汁", "example": "Pour warm gravy over the mashed potatoes." },
      { "word": "grateful", "phonetic": "/ˈɡreɪt.fəl/", "pos": "adj.", "zh": "感恩的、心存感激的", "example": "We are grateful for peaceful days and good friends." }
    ],
    "dailyPhrase": { "en": "Happy Thanksgiving!", "zh": "感恩節快樂！（每年十一月第四個星期四最溫馨的祝福語）" },
    "cultureTip": "感恩節傳統中，在開動切火雞（Carving the turkey）前，家人會手牽手圍坐輪流說出「What I'm grateful for」，凝聚家族深厚情感。"
  },

  # 11-25 [國小初階]
  {
    "id": "dialogue-1125",
    "date": "11-25",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "趣味遊戲",
    "topic": {
      "en": "Pulling the Thanksgiving Wishbone",
      "zh": "扳開感恩節火雞許願骨"
    },
    "situation": "感恩節大餐隔天午餐，Sam 和弟弟 Eric 拿著風乾的 Y 字形火雞胸骨，準備用力拔骨頭許願。",
    "speakers": {
      "Sam": { "role": "Sam", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Eric": { "role": "Eric", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1125.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Sam", "avatar": "👦", "en": "Eric, the turkey wishbone is completely dry! Grab one of the two ends.", "zh": "Eric，火雞許願骨已經完全風乾了！各抓住兩邊的一端吧。", "keywords": ["wishbone", "ends"] },
      { "id": 2, "speaker": "Eric", "avatar": "👦", "en": "I'm holding the left side with my pinky finger! What is the rule?", "zh": "我用小拇指勾住左邊！遊戲規則是什麼呀？", "keywords": ["pinky", "rule"] },
      { "id": 3, "speaker": "Sam", "avatar": "👦", "en": "Make a secret wish in your heart, then we both pull until it snaps!", "zh": "在心裡許一個秘密願望，然後我們兩個一起用力拉直到骨頭斷開！", "keywords": ["snaps", "wish"] },
      { "id": 4, "speaker": "Eric", "avatar": "👦", "en": "One, two, three, pull! Crack! Look, I got the bigger piece!", "zh": "一、二、三、拉！啪！看，我拿到比較大截的這一半了！", "keywords": ["crack", "bigger"] },
      { "id": 5, "speaker": "Sam", "avatar": "👦", "en": "Congratulations! That means your secret wish is bound to come true!", "zh": "恭喜你！那代表你的秘密願望一定會美夢成真喔！", "keywords": ["come true", "bound"] }
    ],
    "vocabulary": [
      { "word": "wishbone", "phonetic": "/ˈwɪʃ.boʊn/", "pos": "n.", "zh": "（禽類的）許願骨、叉骨", "example": "Children snapped the wishbone after Thanksgiving dinner." },
      { "word": "snap", "phonetic": "/snæp/", "pos": "v.", "zh": "啪的一聲折斷、斷裂", "example": "The brittle twig snapped in two." },
      { "word": "pinky", "phonetic": "/ˈpɪŋ.ki/", "pos": "n.", "zh": "小手指、小拇指", "example": "They made a pinky promise to keep the secret." }
    ],
    "dailyPhrase": { "en": "Make a secret wish.", "zh": "在心底許下一個秘密願望。" },
    "cultureTip": "「Wishbone」是鳥類的叉骨（Furcula）。相傳拿到斷裂後較大那一塊（The larger half）的人，所許下的願望就能實現，英文成語「Get a lucky break」由此而來。"
  },

  # 11-26 [高中進階]
  {
    "id": "dialogue-1126",
    "date": "11-26",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "經濟與消費",
    "topic": {
      "en": "Black Friday Madness and Mindful Consumption",
      "zh": "黑色星期五狂潮與正念消費思辨"
    },
    "situation": "感恩節隔天「黑色星期五」，高中好友 Marcus 與 Bella 在商場美食街看著瘋狂搶購的人潮，反思消費主義對心理與地球的影響。",
    "speakers": {
      "Marcus": { "role": "Marcus", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Bella": { "role": "Bella", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1126.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Marcus", "avatar": "🧑", "en": "Bella, the contrast is staggering: yesterday we celebrated gratitude for what we have, and today people are trampling each other for flat-screen TVs.", "zh": "Bella，這對比真強烈：昨天我們才慶祝感恩所擁有的一切，今天大家就為了搶打折平面電視互相推擠踩踏。", "keywords": ["contrast", "trampling"] },
      { "id": 2, "speaker": "Bella", "avatar": "👩", "en": "That irony captures hyper-consumerism. Marketing convinces us that purchasing discounts equates to acquiring happiness.", "zh": "這種諷刺精準體現了極端消費主義。商業行銷成功說服大眾以為搶到打折就等同於獲得幸福。", "keywords": ["hyper-consumerism", "irony"] },
      { "id": 3, "speaker": "Marcus", "avatar": "🧑", "en": "Yet the hedonic treadmill kicks in within days, leaving people just as unsatisfied and burdened with clutter.", "zh": "然而『享樂跑步機效應』幾天內就會生效，讓人們依然不滿足，家裡還多了一堆用不上的雜物負擔。", "keywords": ["hedonic treadmill", "clutter"] },
      { "id": 4, "speaker": "Bella", "avatar": "👩", "en": "Mindful consumption urges us to invest in experiential memories and human connections rather than accumulating disposable material possessions.", "zh": "正念消費主張我們把資源投資在體驗性回憶與人際情感連結上，而不是堆積一次性的物質商品。", "keywords": ["experiential", "possessions"] },
      { "id": 5, "speaker": "Marcus", "avatar": "🧑", "en": "Wealth isn't defined by what you accumulate, but by what you are content to live without.", "zh": "真正的富足不在於你囤積了多少東西，而在於你內心充實到不需要靠什麼來證明自己。", "keywords": ["wealth", "accumulate"] }
    ],
    "vocabulary": [
      { "word": "consumerism", "phonetic": "/kənˈsuː.mɚ.ɪ.zəm/", "pos": "n.", "zh": "消費主義", "example": "Unchecked consumerism accelerates resource depletion." },
      { "word": "clutter", "phonetic": "/ˈklʌt̬.ɚ/", "pos": "n.", "zh": "雜亂堆積物、雜物", "example": "Clear the desktop clutter to improve your study focus." },
      { "word": "experiential", "phonetic": "/ɪkˌspɪr.iˈen.ʃəl/", "pos": "adj.", "zh": "體驗性的、經驗導向的", "example": "Experiential learning creates profound lasting impressions." }
    ],
    "dailyPhrase": { "en": "The hedonic treadmill.", "zh": "享樂跑步機（物質慾望滿足後快樂感迅速回落到基線的心理現象）" },
    "cultureTip": "心理學著名的「Hedonic Treadmill」指出，購買物質帶來的多巴胺興奮通常只能維持數天；反而是旅行、志工與深度人際體驗，能帶來長遠的幸福感。"
  },

  # 11-27 [國小中高]
  {
    "id": "dialogue-1127",
    "date": "11-27",
    "level": "elementary_adv",
    "levelName": "國小中高 (A1+)",
    "levelBadgeColor": "#0284c7",
    "category": "節慶美食",
    "topic": {
      "en": "Leftover Turkey Sandwiches",
      "zh": "感恩節吃不完的烤火雞肉三明治"
    },
    "situation": "感恩節後的週六中午，Emma 和哥哥 Lucas 一起用大餐剩餘的火雞肉和配菜自製豪華夾心三明治。",
    "speakers": {
      "Emma": { "role": "Emma", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Lucas": { "role": "Lucas", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1127.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Emma", "avatar": "👧", "en": "Lucas, the fridge is overflowing with leftover turkey from Thursday night! What should we do?", "zh": "Lucas，冰箱裡塞滿了週四晚上剩的大火雞肉！我們該怎麼解決？", "keywords": ["leftover", "overflowing"] },
      { "id": 2, "speaker": "Lucas", "avatar": "👦", "en": "Time to build the world-famous day-after Thanksgiving turkey sandwich!", "zh": "該來做聞名遐邇的『感恩節隔日豪華火雞三明治』囉！", "keywords": ["sandwich", "famous"] },
      { "id": 3, "speaker": "Emma", "avatar": "👧", "en": "How do we layer it so every bite is packed with holiday flavor?", "zh": "我們要怎麼疊夾層，才能讓每一口都吃得到滿滿的節慶風味？", "keywords": ["layer", "bite"] },
      { "id": 4, "speaker": "Lucas", "avatar": "👦", "en": "Toasted bread, roasted turkey breast, a spoonful of cranberry sauce, and savory stuffing in the middle!", "zh": "烤吐司、烤火雞胸肉片、一大匙蔓越莓果醬，中間還要夾鹹香的烤填料麵包丁！", "keywords": ["turkey breast", "stuffing"] },
      { "id": 5, "speaker": "Emma", "avatar": "👧", "en": "Sweet, savory, and crunchy all in one mouthful! Leftovers never tasted this glorious!", "zh": "一口咬下又有甜、又有鹹、又有酥脆！剩菜從來沒這麼驚豔好吃過！", "keywords": ["glorious", "mouthful"] }
    ],
    "vocabulary": [
      { "word": "leftover", "phonetic": "/ˈleftˌoʊ.vɚ/", "pos": "n./adj.", "zh": "剩菜、吃剩的食物", "example": "Store the leftover soup in an airtight container." },
      { "word": "layer", "phonetic": "/ˈleɪ.ɚ/", "pos": "v./n.", "zh": "層層堆疊、分層", "example": "Layer the lasagna pasta with ricotta cheese." },
      { "word": "glorious", "phonetic": "/ˈɡlɔːr.i.əs/", "pos": "adj.", "zh": "極好的、光彩奪目的、美味絕頂的", "example": "The kitchen was filled with glorious aromas." }
    ],
    "dailyPhrase": { "en": "All in one mouthful.", "zh": "一口咬下全包含（形容層次豐富的多重美味）" },
    "cultureTip": "「The Day-After Turkey Sandwich」在美語日常中幾乎自成一種飲食文化，將感恩節剩下的火雞、蔓越莓醬與肉汁夾入吐司，被許多人認為比正餐還好吃！"
  },

  # 11-28 [國中挑戰]
  {
    "id": "dialogue-1128",
    "date": "11-28",
    "level": "junior",
    "levelName": "國中挑戰 (A2~B1)",
    "levelBadgeColor": "#d97706",
    "category": "生活反思",
    "topic": {
      "en": "Buy Nothing Day: A Fresh Perspective",
      "zh": "「無消費日」：放下購物欲的清爽體驗"
    },
    "situation": "在學校自習室裡，Leo 和 Zoe 聊到國際發起的「無消費日（Buy Nothing Day）」，嘗試 24 小時不花一毛錢的生活實驗。",
    "speakers": {
      "Leo": { "role": "Leo", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" },
      "Zoe": { "role": "Zoe", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1128.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Leo", "avatar": "👦", "en": "Zoe, did you know that worldwide environmental groups celebrate 'Buy Nothing Day' alongside Black Friday?", "zh": "Zoe，妳知道全球環保團體在黑五購物狂潮的同時，提倡慶祝『無消費日』嗎？", "keywords": ["Buy Nothing Day", "environmental"] },
      { "id": 2, "speaker": "Zoe", "avatar": "👧", "en": "Yes! The challenge is simple: commit to not spending a single dime for twenty-four hours.", "zh": "知道！挑戰非常簡單：承諾在整整二十四小時內，不花任何一毛錢。", "keywords": ["dime", "commit"] },
      { "id": 3, "speaker": "Leo", "avatar": "👦", "en": "I tried it today! Instead of buying boba tea or gaming skins, I borrowed a book from the library and went jogging in the park.", "zh": "我今天就嘗試了！我不買珍奶也不買遊戲造型，而是去圖書館借了一本書，然後到公園慢跑。", "keywords": ["jogging", "skins"] },
      { "id": 4, "speaker": "Zoe", "avatar": "👧", "en": "It makes you realize that the most refreshing pleasures in life—sunshine, fresh air, exercise, reading—are completely free.", "zh": "這真讓人體會到，生活中最令人身心舒暢的樂趣——陽光、新鮮空氣、運動、閱讀——完全是免費的。", "keywords": ["refreshing", "pleasures"] },
      { "id": 5, "speaker": "Leo", "avatar": "👦", "en": "Stepping out of the consumer treadmill feels liberating and serene.", "zh": "跳脫出消費主義的無底洞，感覺身心無比自由又平靜。", "keywords": ["liberating", "serene"] }
    ],
    "vocabulary": [
      { "word": "commit", "phonetic": "/kəˈmɪt/", "pos": "v.", "zh": "下定決心、承諾致力於", "example": "Commit yourself to daily reading habits." },
      { "word": "liberating", "phonetic": "/ˈlɪb.ə.reɪ.t̬ɪŋ/", "pos": "adj.", "zh": "讓人感到解脫自由的", "example": "Decluttering your bedroom feels truly liberating." },
      { "word": "serene", "phonetic": "/səˈriːn/", "pos": "adj.", "zh": "安詳平靜的、寧靜致遠的", "example": "The calm lake was serene in the morning mist." }
    ],
    "dailyPhrase": { "en": "Not a single dime.", "zh": "一毛錢也不花（形容極其節儉或實踐無消費）" },
    "cultureTip": "「Buy Nothing Day（國際無消費日）」由加拿大藝術家 Ted Dave 於 1992 年發起，旨在抗議過度消費主義與資源浪費，現已推廣至全球 65 個國家。"
  },

  # 11-29 [國小初階]
  {
    "id": "dialogue-1129",
    "date": "11-29",
    "level": "elementary_basic",
    "levelName": "國小初階 (A1)",
    "levelBadgeColor": "#22c55e",
    "category": "生活美學",
    "topic": {
      "en": "Drawing on the Foggy Window Pane",
      "zh": "在霧濛濛的冰冷玻璃窗上畫畫"
    },
    "situation": "深秋降溫的早晨，車窗和房間窗戶起了一層厚厚白霧，Lily 和 Toby 用小手指在玻璃上畫笑臉。",
    "speakers": {
      "Lily": { "role": "Lily", "avatar": "👧", "gender": "female", "voice": "en-US-JennyNeural" },
      "Toby": { "role": "Toby", "avatar": "👦", "gender": "male", "voice": "en-US-GuyNeural" }
    },
    "audioSrc": "audio/dialogue-1129.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Lily", "avatar": "👧", "en": "Toby, breathe on the window pane! It fogs up instantly like magic glass!", "zh": "Toby，對著窗玻璃吹口氣！它瞬間就像魔法玻璃一樣起了一層厚霧！", "keywords": ["breathe", "pane", "fogs up"] },
      { "id": 2, "speaker": "Toby", "avatar": "👦", "en": "Watch! I use my index finger to draw a smiling sun and a little sailboat.", "zh": "看！我用食指在上面畫了一個笑瞇瞇的太陽和一艘小帆船。", "keywords": ["index finger", "sailboat"] },
      { "id": 3, "speaker": "Lily", "avatar": "👧", "en": "I'm drawing a snowman wearing a pointed top hat beside your sun!", "zh": "我在你的太陽旁邊畫一個戴著尖尖大禮帽的雪人！", "keywords": ["snowman", "top hat"] },
      { "id": 4, "speaker": "Toby", "avatar": "👦", "en": "Tiny drops of water are trickling down like little tears!", "zh": "微小的水珠正順著線條像小眼淚一樣滴落下來呢！", "keywords": ["trickling", "tears"] },
      { "id": 5, "speaker": "Lily", "avatar": "👧", "en": "Wipe it clean with a sleeve and we have a blank glass canvas all over again!", "zh": "用袖子輕輕擦乾淨，我們就又有一張全新的透明玻璃畫布了！", "keywords": ["canvas", "sleeve"] }
    ],
    "vocabulary": [
      { "word": "pane", "phonetic": "/peɪn/", "pos": "n.", "zh": "（一塊）窗玻璃", "example": "Frost formed geometric patterns on the window pane." },
      { "word": "trickle", "phonetic": "/ˈtrɪk.əl/", "pos": "v.", "zh": "緩緩滴落、細細流動", "example": "Rain trickled down the windshield." },
      { "word": "canvas", "phonetic": "/ˈkæn.vəs/", "pos": "n.", "zh": "畫布、帆布", "example": "The artist splashed vibrant oils on the blank canvas." }
    ],
    "dailyPhrase": { "en": "Fog up.", "zh": "起霧、表面凝結出霧氣。" },
    "cultureTip": "冬天室內外溫差大時，室內潮濕空氣接觸冰冷玻璃產生凝結現象（Condensation），在起霧玻璃上作畫是全世界孩童共通的生活童趣！"
  },

  # 11-30 [高中進階]
  {
    "id": "dialogue-1130",
    "date": "11-30",
    "level": "senior",
    "levelName": "高中進階 (B1~B2)",
    "levelBadgeColor": "#e11d48",
    "category": "歲末展望",
    "topic": {
      "en": "November Reflection and Preparing for the Final Month",
      "zh": "十一月總結：為即將到來的年終歲末做好準備"
    },
    "situation": "十一月的最後一天傍晚，高中生 Henry 和 Claire 在校園步道漫步，回顧秋天這三個月的收穫，並準備迎接即將到來的十二月年終考評。",
    "speakers": {
      "Henry": { "role": "Henry", "avatar": "🧑", "gender": "male", "voice": "en-US-GuyNeural" },
      "Claire": { "role": "Claire", "avatar": "👩", "gender": "female", "voice": "en-US-JennyNeural" }
    },
    "audioSrc": "audio/dialogue-1130.mp3",
    "dialogue": [
      { "id": 1, "speaker": "Henry", "avatar": "🧑", "en": "Claire, today is November thirtieth. Autumn has officially yielded to winter, with just thirty-one days left in this year.", "zh": "Claire，今天是十一月三十日。秋天已正式交棒給冬天，今年只剩下最後三十一天了。", "keywords": ["yielded", "November"] },
      { "id": 2, "speaker": "Claire", "avatar": "👩", "en": "Looking back at September, October, and November, our consistent daily English dialogues really compounded into noticeable fluency.", "zh": "回顧九月、十月和十一月這三個月，我們堅持每天練習的生活英語對話，真的複利累積成了肉眼可見的流利度。", "keywords": ["compounded", "fluency"] },
      { "id": 3, "speaker": "Henry", "avatar": "🧑", "en": "I speak with so much more spontaneous confidence now without constantly translating word-for-word in my head.", "zh": "我現在開口說英語自信自然多了，再也不必在腦袋裡字對字逐字翻譯。", "keywords": ["spontaneous", "translating"] },
      { "id": 4, "speaker": "Claire", "avatar": "👩", "en": "December will bring final semester projects, winter holiday celebrations, and annual reflections.", "zh": "十二月將迎來期末大專案、溫暖冬日節慶，以及歲末年終的年度省思。", "keywords": ["reflections", "semester"] },
      { "id": 5, "speaker": "Henry", "avatar": "🧑", "en": "Let's finish this year strong! Consistency is the bridge between goals and accomplishment.", "zh": "讓我們把今年完美收官！持之以恆，正是連接目標與成就最堅固的橋樑。", "keywords": ["finish strong", "consistency"] }
    ],
    "vocabulary": [
      { "word": "yield", "phonetic": "/jiːld/", "pos": "v.", "zh": "讓位、讓步、產出", "example": "Autumn yields to the chilly winds of winter." },
      { "word": "spontaneous", "phonetic": "/spɑːnˈteɪ.ni.əs/", "pos": "adj.", "zh": "自發的、自然而然脫口而出的", "example": "Her spontaneous speech won standing applause." },
      { "word": "consistency", "phonetic": "/kənˈsɪs.tən.si/", "pos": "n.", "zh": "始終如一、持之以恆", "example": "Consistency beats intensity every single time." }
    ],
    "dailyPhrase": { "en": "Finish strong!", "zh": "堅持到底、完美收官！（年末或賽末最有力的精神號角）" },
    "cultureTip": "「Finish strong!」是歐美學校與體育界在年末或學期末最激勵人心的口號，提醒大家在最後衝刺階段不鬆懈，讓一整年的努力圓滿開花結果。"
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
    for new_item in NOVEMBER_DIALOGUES:
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

    print(f"成功新增 11 月份共 {added_count} 篇對話！目前資料庫總計共有 {len(existing)} 篇對話 (涵蓋 9 月、10 月與 11 月共 91 天)。")

if __name__ == '__main__':
    main()
