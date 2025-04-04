# -*- coding: UTF-8 -*-

import http.client
import json
import io
import numpy as np
import sounddevice as sd
from pydub import AudioSegment
from invoking_API.ASR_token_get import ASR_token_get  # 确保正确导入您的 token 获取函数

# 设置 FFmpeg 路径（根据您的实际路径修改）
AudioSegment.converter = r"ffmpeg/bin/ffmpeg.exe"  # 替换为您的实际路径
AudioSegment.ffprobe = r"ffmpeg/bin/ffprobe.exe"   # 替换为您的实际路径

def processPOSTRequest(appKey, token, text, format, sampleRate):
    host = 'nls-gateway-cn-beijing.aliyuncs.com'
    url = f'https://{host}/stream/v1/tts'
    httpHeaders = {
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg'  # 显式接受 MP3 格式
    }

    body = {
        'appkey': appKey,
        'token': token,
        'text': text,
        'format': format,       # 阿里云 TTS 支持的格式（如 mp3）
        'sample_rate': sampleRate,
        'voice': 'zhimiao_emo',  # 语音类型
        'volume': 49,           # 音量
        'speech_rate': -10,     # 语速
        'pitch_rate': -3        # 音调
    }

    # 使用 ensure_ascii=False 避免中文字符转义
    body_json = json.dumps(body, ensure_ascii=False).encode('utf-8')
    print('The POST request body content:', body_json.decode('utf-8'))

    try:
        conn = http.client.HTTPSConnection(host)
        conn.request(method='POST', url=url, body=body_json, headers=httpHeaders)
        response = conn.getresponse()

        # 打印响应状态和内容类型
        print('Response status and reason:', response.status, response.reason)
        content_type = response.getheader('Content-Type')
        print('Content-Type:', content_type)

        # 读取音频数据
        audio_data = response.read()

        if 'audio/mpeg' in content_type:
            # 使用 pydub 加载 MP3 数据
            audio = AudioSegment.from_mp3(io.BytesIO(audio_data))

            # 确保音频格式符合要求（16 位、单声道）
            audio = audio.set_channels(1).set_sample_width(2)

            # 将音频数据转换为 NumPy 数组
            audio_array = np.array(audio.get_array_of_samples()).astype(np.int16)

            # 使用 sounddevice 播放音频
            sd.play(audio_array, samplerate=audio.frame_rate)
            sd.wait()  # 等待播放完成
            print('Audio played successfully!')
        else:
            print(f"Unsupported content type: {content_type}")
            print("Response data:", audio_data[:100])  # 打印前 100 字节调试

        conn.close()
    except Exception as e:
        print(f"Error: {e}")

# 调用示例
appKey = 'xC6t9KpVsYnz7eHT'  # 替换为您的阿里云 AppKey
token = ASR_token_get()      # 确保正确获取 token
text = '亲爱的总裁大人，下午好，我是您的私人AI按摩师，最近有什么情况？'  # 原始中文文本
format = 'mp3'               # 阿里云 TTS 支持的格式
sampleRate = 16000           # 采样率（确保与服务端一致）

processPOSTRequest(appKey, token, text, format, sampleRate)