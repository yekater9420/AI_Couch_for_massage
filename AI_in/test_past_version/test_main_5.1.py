# deepseek_api 5.1 测试版本
'''
1.优化了ASR语音识别程序
2.优化显示设置
3.新增判断器：1>超过10秒未说话结束录音 2>噪声容忍度
4.新增自动检测关机关键词的语音关机系统
5.修复了语音输入为None时程序依然会执行的问题
6.新增若3次为检测到语音输入，程序自动关机
7.新增语音合成功能，程序可以文字转语音
'''
# 官方库
import sys
import yaml
import time
# 自定义库
from utils.EPG import EPG
from invoking_API.ASR_API import *
from invoking_API.Large_Model_API import Deepseek_API
from invoking_API.ASR_token_get import ASR_token_get

# 加载配置文件
f = open("../config/config_large_model.yaml", "r", encoding="utf-8")
conf_str = f.read()
f.close() # 及时释放资源，防止数据损坏和锁定
config = yaml.load(conf_str, Loader=yaml.FullLoader)

# 大模型选择--->可外接询问切换
def choice_Large_Model():
    # 大模型选择器
    #Large_model = input("1. DeepSeek-R1 \n2. DeepSeek-V3 \n3. DeepSeek-R1-Distill-Liama-70B \n 请配置您需要的大模型： ")
    Large_model = "3"
    if Large_model == "1":
        base_url = config["DeepSeek"]["DeepSeek-R1"]["base_url"]
        api_key = config["DeepSeek"]["DeepSeek-R1"]["api_key"]
        model = config["DeepSeek"]["DeepSeek-R1"]["model"]
        return base_url, api_key, model
    if Large_model == "2":
        base_url = config["DeepSeek"]["DeepSeek-V3"]["base_url"]
        api_key = config["DeepSeek"]["DeepSeek-V3"]["api_key"]
        model = config["DeepSeek"]["DeepSeek-V3"]["model"]
        return base_url, api_key, model
    if Large_model == "3":
        base_url = config["DeepSeek"]["DeepSeek-R1-Distill-Liama-70B"]["base_url"]
        api_key = config["DeepSeek"]["DeepSeek-R1-Distill-Liama-70B"]["api_key"]
        model = config["DeepSeek"]["DeepSeek-R1-Distill-Liama-70B"]["model"]
        return base_url, api_key, model

# API发问设置
def API_Setting(question ,stream=False):
    stream = False
    role = "user"
    content = f"你是一位专业的，从业40年的中医按摩医师，对人体穴位了解十分精通，现在有一位病人：{question}，帮他按摩一下,并给出详细步骤和按摩方案"
    return stream, role, content

# 阿里语音合成API
import http.client
import json
import io
import numpy as np
import sounddevice as sd
from pydub import AudioSegment
from invoking_API.ASR_token_get import ASR_token_get

# 设置 FFmpeg 路径
AudioSegment.converter = r"ffmpeg/bin/ffmpeg.exe"
AudioSegment.ffprobe = r"ffmpeg/bin/ffprobe.exe"

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
        'format': format,       # 阿里云 TTS 支持的格式
        'sample_rate': sampleRate,
        'voice': 'zhimiao_emo',  # 语音类型
        'volume': 49,           # 音量
        'speech_rate': -10,     # 语速
        'pitch_rate': -3        # 音调
    }

    # 使用 ensure_ascii=False 避免中文字符转义
    body_json = json.dumps(body, ensure_ascii=False).encode('utf-8')
    #print('The POST request body content:', body_json.decode('utf-8'))

    try:
        conn = http.client.HTTPSConnection(host)
        conn.request(method='POST', url=url, body=body_json, headers=httpHeaders)
        response = conn.getresponse()

        # 打印响应状态和内容类型
        #print('Response status and reason:', response.status, response.reason)
        content_type = response.getheader('Content-Type')
        #print('Content-Type:', content_type)

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
            #print('Audio played successfully!')
        else:
            print(f"Unsupported content type: {content_type}")
            print("Response data:", audio_data[:100])  # 打印前 100 字节调试
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

def Speech_synthesis_API(text , format = 'mp3' , sampleRate=16000):
    appKey = 'xC6t9KpVsYnz7eHT'
    token = ASR_token_get()  # 确保正确获取 token
    processPOSTRequest(appKey, token, text, format, sampleRate)

# DeepSeek 启动！
def Deepseek_work(choice):
    Speech_detection_feedback().Large_model_response_start()
    setting = API_Setting(question, stream=False)
    result = Deepseek_API(choice[0], choice[1], choice[2], setting[0], setting[1], setting[2])
    Speech_detection_feedback().Large_model_response_end()
    EPG(result)

# 语音输入检测
def voice_input_detection():
    '''
    检测语音输入是否为空--->0，
    若为0，继续发问3次，直到不为0为止
    若发问3次后，仍为0，则自动关机
    '''
    count = 0
    while 1:
        question = Ali_ASR_API_main()
        print("抱歉亲，我没有听清您的讲话，可以再讲一次吗？")
        Speech_synthesis_API("抱歉亲，我没有听清您的讲话，可以再讲一次吗？")
        count = count + 1
        if len(question) >= 5:
            Deepseek_work(choice)
        if count == 3:
            print_show_beatuiful("抱歉亲，3次未检测到语音输入，我已自动关机，欢迎下次使用")
            Speech_synthesis_API("抱歉亲，3次未检测到语音输入，我已自动关机，欢迎下次使用")
            sys.exit(0)

# 测试
if __name__ == '__main__':
    # 结束关键词检测
    end_message = {"关机" , "退出程序" , "再见"}

    # 大模型选择
    choice = choice_Large_Model()

    # 第一次问候
    ask = ask_condition_first()
    print(ask)
    Speech_synthesis_API(ask)
    # 语音识别输入
    question = Ali_ASR_API_main()
    print_show_beatuiful(question)
    if any(i in question for i in end_message):
        bye = ask_condition_bye()
        print(bye)
        Speech_synthesis_API(bye)
        sys.exit(0)
    elif len(question) == 0 :
        print("抱歉亲，我没有听清您的讲话，可以再讲一次吗？")
        Speech_synthesis_API("抱歉亲，我没有听清您的讲话，可以再讲一次吗？")
        voice_input_detection()
    else:
        Deepseek_work(choice)

        # 第二次询问
        ask = ask_condition_sec()
        print(ask)
        Speech_synthesis_API(ask)
        # 语音识别输入
        question = Ali_ASR_API_main()
        print_show_beatuiful(question)
        if any(i in question for i in end_message):
            bye = ask_condition_bye()
            print(bye)
            Speech_synthesis_API(bye)
            sys.exit(0)
        elif len(question) == 0 :
            print("抱歉亲，我没有听清您的讲话，可以再讲一次吗？")
            Speech_synthesis_API("抱歉亲，我没有听清您的讲话，可以再讲一次吗？")
            voice_input_detection()
        else:
            Deepseek_work(choice)
            # 多次询问
            while True:
                ask = ask_condition_other()
                print(ask)
                Speech_synthesis_API(ask)
                # 语音识别输入
                question = Ali_ASR_API_main()
                print_show_beatuiful(question)
                if any(i in question for i in end_message):
                    bye = ask_condition_bye()
                    print(bye)
                    Speech_synthesis_API(bye)
                    sys.exit(0)
                elif len(question) == 0 :
                    print("抱歉亲，我没有听清您的讲话，可以再讲一次吗？")
                    Speech_synthesis_API("抱歉亲，我没有听清您的讲话，可以再讲一次吗？")
                    count = 0
                    while 1:
                        question = Ali_ASR_API_main()
                        print("抱歉亲，我没有听清您的讲话，可以再讲一次吗？")
                        Speech_synthesis_API("抱歉亲，我没有听清您的讲话，可以再讲一次吗？")
                        voice_input_detection()
                else:
                    Deepseek_work(choice)


