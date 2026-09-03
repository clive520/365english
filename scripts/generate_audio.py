#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日對話練習 - 高品質 Neural TTS 語音合成管線
使用微軟 Edge Neural 語音庫，針對國小至高中生特點調校：
1. 咬字清晰度極高、重音標竿、語調親切生動
2. 語速微調平穩，句間保留適度消化與跟讀停頓
3. 自動計算毫秒級時間軸，支援前端單句點選即播
"""

import os
import sys
import json
import asyncio
import tempfile

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import edge_tts
from mutagen.mp3 import MP3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'dialogues.json')
JS_DATA_FILE = os.path.join(BASE_DIR, 'js', 'data.js')
AUDIO_DIR = os.path.join(BASE_DIR, 'audio')

# 角色預設聲音對應表 (微軟頂級美式發音)
VOICE_MAP = {
    'female': 'en-US-JennyNeural',        # 親切自然女聲
    'female_young': 'en-US-AnaNeural',     # 活潑純真童聲/小女孩
    'male': 'en-US-GuyNeural',            # 沉穩標準男聲
    'male_teen': 'en-US-ChristopherNeural' # 陽光青少年男聲
}

async def generate_sentence_audio(text: str, voice: str, rate: str = "-4%") -> tuple[bytes, float]:
    """生成單一語句音訊與取得精確秒數長度"""
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        await communicate.save(tmp_path)
        audio = MP3(tmp_path)
        duration = audio.info.length
        with open(tmp_path, "rb") as f:
            audio_bytes = f.read()
        return audio_bytes, duration
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

async def process_dialogue(item: dict) -> dict:
    """處理單篇對話：合成每句發音、串接為整段 MP3、更新時間標記"""
    dialogue_id = item['id']
    level = item.get('level', 'elementary_basic')
    out_filename = f"{dialogue_id}.mp3"
    out_path = os.path.join(AUDIO_DIR, out_filename)

    # 檢查是否已經存在且已標註時間軸
    has_timestamps = all('startTime' in s for s in item.get('dialogue', []))
    if os.path.exists(out_path) and has_timestamps:
        print(f"⏩ 跳過已存在之音檔：[{item.get('levelName')}] {item['topic']['zh']} ({out_filename})")
        return item

    print(f"\n🎧 正在處理對話：[{item.get('levelName')}] {item['topic']['zh']} ({item['topic']['en']})...")

    # 針對不同年級等級，設定最適合學生的教學語速
    if 'elementary' in level:
        speed_rate = "-6%"  # 國小：速度略為平緩放慢，咬字特別立體
    elif 'junior' in level:
        speed_rate = "-2%"  # 國中：自然日常生活語速
    else:
        speed_rate = "+0%"  # 高中：標準母語自然語速

    combined_mp3_data = bytearray()
    current_time = 0.0

    updated_sentences = []

    for sentence in item['dialogue']:
        speaker_name = sentence['speaker']
        speaker_info = item.get('speakers', {}).get(speaker_name, {})
        gender = speaker_info.get('gender', 'female')
        
        # 決定人聲
        if speaker_info.get('voice'):
            voice = speaker_info['voice']
        elif gender == 'female':
            voice = VOICE_MAP['female']
        else:
            voice = VOICE_MAP['male']

        text = sentence['en']
        print(f"  👉 [{speaker_name}] \"{text}\" (人聲: {voice}, 語速: {speed_rate})")

        audio_bytes, duration = await generate_sentence_audio(text, voice, rate=speed_rate)
        
        start_time = round(current_time, 2)
        end_time = round(start_time + duration, 2)

        sentence_copy = dict(sentence)
        sentence_copy['startTime'] = start_time
        sentence_copy['endTime'] = end_time
        updated_sentences.append(sentence_copy)

        combined_mp3_data.extend(audio_bytes)
        current_time = end_time

    # 輸出最終完整 MP3
    os.makedirs(AUDIO_DIR, exist_ok=True)
    out_filename = f"{dialogue_id}.mp3"
    out_path = os.path.join(AUDIO_DIR, out_filename)
    
    with open(out_path, "wb") as f:
        f.write(combined_mp3_data)

    print(f"  ✅ 音檔已成功生成：{out_path} (總時長約 {round(current_time, 1)} 秒)")

    item_copy = dict(item)
    item_copy['dialogue'] = updated_sentences
    item_copy['audioSrc'] = f"audio/{out_filename}"
    return item_copy

async def main():
    if not os.path.exists(DATA_FILE):
        print(f"❌ 找不到對話資料檔案：{DATA_FILE}")
        sys.exit(1)

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        dialogues = json.load(f)

    print(f"🚀 開始合成英語對話音訊，共計 {len(dialogues)} 篇對話...")

    updated_dialogues = []
    for item in dialogues:
        updated_item = await process_dialogue(item)
        updated_dialogues.append(updated_item)

    # 寫回 dialogues.json
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(updated_dialogues, f, ensure_ascii=False, indent=2)

    # 寫回 js/data.js
    with open(JS_DATA_FILE, 'w', encoding='utf-8') as f:
        f.write("// 預載每日對話資料庫（支援本地離線與 GitHub Pages 靜態環境）\n")
        f.write("window.DAILY_DIALOGUES = ")
        json.dump(updated_dialogues, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    print("\n🎉 全部對話之 MP3 音訊與時間軸標記均已處理完成！")

if __name__ == '__main__':
    asyncio.run(main())
