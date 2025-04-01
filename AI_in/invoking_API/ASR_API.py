# 阿里语音识别（Ali-ASR）API
# App_key:WqwOrQpgdALOI4L3

import json
import threading
import sys
import keyboard  # 键盘监听
import time
import nls
import pyaudio


#==================
# 配置参数
#==================
# 定义音频流参数
FORMAT = pyaudio.paInt16  # 音频格式
CHANNELS = 1  # 声道数
RATE = 16000  # 采样率
CHUNK = 640  # 数据块大小


class SpeechTranscriberThread(threading.Thread):
    # 构造函数，初始化线程
    def __init__(self, thread_id , URL, TOKEN, APPKEY):
        # 调用父类的构造函数
        threading.Thread.__init__(self)
        # 存储线程的标识符
        self.thread_id = thread_id
        # 初始化NlsSpeechTranscriber对象，配置NLS服务的参数和回调函数
        self.sr = nls.NlsSpeechTranscriber(
            url=URL,
            token=TOKEN,
            appkey=APPKEY,
            # on_sentence_begin=self.on_sentence_begin,
            on_sentence_end=self.on_sentence_end,
            # on_start=self.on_start,
            # on_result_changed=self.on_result_changed,
            # on_completed=self.on_completed,
            # on_error=self.on_error,
            # on_close=self.on_close
        )
        # 初始化PyAudio对象
        self.p = pyaudio.PyAudio()
        # 打开一个音频流，用于从麦克风读取数据
        self.stream = self.p.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  input=True,
                                  frames_per_buffer=CHUNK)

    # 清理资源的方法
    def cleanup(self):
        # 如果音频流存在，则停止和关闭它
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        # 如果PyAudio实例存在，则终止它
        if self.p:
            self.p.terminate()

    def run(self):
        # 输出消息，表示线程开始语音转录
        # print(f"Thread {self.thread_id}: Starting speech transcription.")
        # 启动语音识别
        self.sr.start(aformat="pcm",
                      enable_intermediate_result=True,
                      enable_punctuation_prediction=True,
                      enable_inverse_text_normalization=True)
        try:
            # 假设我们使用一个标志来控制循环
            self.running = True
            # 循环读取音频数据并发送到NLS服务
            while self.running:
                data = self.stream.read(CHUNK)
                self.sr.send_audio(data)
                # 稍作延迟
                time.sleep(0.01)
        except Exception as e:
            print(f"Thread {self.thread_id}: Error during transcription: {e}")
        finally:
            # 清理资源
            self.cleanup()

    def on_sentence_end(self, message):
        # 输出句子结束的消息
        # print(f"Thread {self.thread_id}: Sentence end: {message}")
        message_dict = json.loads(message)
        # 提取payload部分
        payload = message_dict.get('payload', {})
        # 提取并输出result内容
        result = payload.get('result', '')
        print(result, end='')

    def stop_transcription(self):
        """停止转录并清理资源"""
        self.running = False
        self.sr.stop()
        self.cleanup()


def on_press(event):
    """当按键被按下时调用的函数"""
    if event.name == 'esc':  # 如果按下的是ESC键
        print('ESC key pressed. Exiting...')
        # 停止监听所有键盘事件
        keyboard.unhook_all()
        # 停止转录线程
        transcriber_thread.stop_transcription()
        # 等待转录线程退出
        transcriber_thread.join()
        # 退出程序
        sys.exit()


def ASR_API_main():
    global transcriber_thread
    # 禁用NLS SDK的跟踪日志
    nls.enableTrace(False)
    # 创建SpeechTranscriberThread实例，并传入线程标识符
    transcriber_thread = SpeechTranscriberThread("z")
    # 钩子键盘事件
    keyboard.hook(callback=on_press)
    # 启动线程
    transcriber_thread.start()
    # 等待线程完成
    transcriber_thread.join()

