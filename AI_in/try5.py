import http.client
import json
import pyaudio
import keyboard
import time
from invoking_API.ASR_token_get import ASR_token_get

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
NO_VOICE_TIMEOUT = 5  # 无语音输入超时时间

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
            print("录音时间达到最大限制，结束录音。")
            break

        if current_time - last_voice_time > NO_VOICE_TIMEOUT:
            print("超过5秒未检测到语音输入，结束录音。")
            break

        # 超时前警告
        if not timeout_warning_given and current_time - last_voice_time > NO_VOICE_TIMEOUT - 5:
            print("警告：请继续说话，否则录音将在5秒后结束。")
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
    body = response.read()
    conn.close()

    body = json.loads(body)
    status = body.get('status', None)

    if status == 20000000:
        return body['result']
    else:
        print('Recognizer failed!')
        print('Status code:', status)
        return str(status)



def main():
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
    a = process(request, token, stream)

    # 关闭PyAudio终止进程
    p.terminate()
    return a

if __name__ == "__main__":
    print("请讲话：")
    a = main()
    print("#"*50)
    print(a)
    print("#" * 50)