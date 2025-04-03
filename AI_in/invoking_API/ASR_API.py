# Ali-ASR_API 一句话语音识别接口
import http.client
import json
import pyaudio
import keyboard
import time
from invoking_API.ASR_token_get import ASR_token_get
from Individuation.Ind_for_ask import *

host = 'nls-gateway-cn-shanghai.aliyuncs.com'
conn = http.client.HTTPSConnection(host)

# 服务请求地址
url = 'https://nls-gateway-cn-shanghai.aliyuncs.com/stream/v1/asr'
appKey = "CEAKfkvNUZmQhQlI"
token = ASR_token_get()

# 音频参数
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
MAX_RECORD_TIME = 59  # 最大录音时间
NO_VOICE_TIMEOUT = 10  # 无语音输入超时时间

# 噪声容忍度

def process(request, token, audioStream):
    # 读取音频流
    audioContent = bytearray()
    start_time = time.time()
    last_voice_time = start_time
    timeout_warning_given = False  # 添加超时警告标志

    while True:
        data = audioStream.read(CHUNK)
        audioContent.extend(data)
        current_time = time.time()

        # 检测语音活动（优化后的逻辑）
        has_voice = False
        for sample in data:
            if abs(sample) > 300:  # 调整阈值以适应环境噪声
                has_voice = True
                break

        if has_voice:
            last_voice_time = current_time
            timeout_warning_given = False  # 重置超时警告标志

        # 超时逻辑
        if current_time - start_time > MAX_RECORD_TIME:
            print("录音时间达到最大限制，录音结束。")
            break

        if current_time - last_voice_time > NO_VOICE_TIMEOUT:
            print("超过10秒未检测到语音输入，录音结束。")
            break

        # 超时前警告
        if not timeout_warning_given and current_time - last_voice_time > NO_VOICE_TIMEOUT - 5:
            # 是否启用超时警告
            #print("警告：请继续说话，否则录音将在5秒后结束。")
            timeout_warning_given = True

        if keyboard.is_pressed('esc'):
            print("按下Esc键，结束录音。")
            break

    audioStream.stop_stream()
    audioStream.close()

    # 设置HTTPS请求头部
    httpHeaders = {
        'X-NLS-Token': token,
        'Content-type': 'application/octet-stream',
        'Content-Length': len(audioContent)
    }

    conn = http.client.HTTPSConnection(host)
    conn.request(method='POST', url=request, body=audioContent, headers=httpHeaders)

    response = conn.getresponse()
    '''
    print('Response status and response reason:')
    print(response.status, response.reason)
    '''
    # 读取响应内容
    body = response.read()

    # 关闭底层的 TCP 连接，释放与服务器通信所占用的系统资源
    conn.close()

    # 打印获取结果
    # print('Recognize response is:')
    body = json.loads(body)
    # print(body)

    # 获取状态请求码
    status = body['status']
    # 判断返回状态请求码
    if status == 20000000:  # 20000000是阿里云语音识别服务的返回结果中提取状态码，表示成功
        result = body['result']
        #print('Recognize result: ' + result)
        return result
    else:
        print('Recognizer failed!')
        print('Status code: ' + str(status))
        return str(status)


def Ali_ASR_API_main():
    # 初始化PyAudio
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    # 设置RESTful请求参数
    request = url + '?appkey=' + appKey
    request = request + '&format=pcm'
    request = request + '&sample_rate=' + str(RATE)
    request = request + '&enable_punctuation_prediction=true'
    request = request + '&enable_inverse_text_normalization=true'
    request = request + '&enable_voice_detection=false'
    # 打印请求
    #print('Request: ' + request)

    # 语音识别检测
    Speech_detection_feedback().Ali_ASR_response()

    # 调用process函数处理请求
    result = process(request, token, stream)
    # 关闭PyAudio终止进程
    p.terminate()
    return result


# 测试
if __name__ == "__main__":
    print("请讲话：")
    a = Ali_ASR_API_main()
    print("#"*50)
    print(a)
    print(type(a))
    print(len(a))
    print("#" * 50)
