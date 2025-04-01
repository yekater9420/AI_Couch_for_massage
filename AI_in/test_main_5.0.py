# deepseek_api 5.0版本
'''
1.优化了4.0版本中API封装调用，使大模型可以自由切换
2.新增'config.yaml'配置文件,增强数据保密性
3.新增环境一键配置文件'requirements.txt'
4.优化了4.0版本中提问流程，使提问更加符合具体场景
5.修复了4.0版本中输入为None的情况
6.新增语音输入（ASR）
6.新增ASR动态token获取接口
7.补充阿里云语音识别大模型SDK文件 “alibabacloud-nls-python-sdk-dev-20241203.zip”
'''
# 官方库
from openai import OpenAI
from invoking_API.Large_Model_API import Deepseek_API
import yaml
# 自定义库
from utils.EPG import EPG
from Individuation.Ind_for_ask import *

# 加载配置文件
f = open("config/config_large_model.yaml", "r", encoding="utf-8")
conf_str = f.read()
f.close() # 及时释放资源，防止数据损坏和锁定
config = yaml.load(conf_str, Loader=yaml.FullLoader)

# 大模型选择--->可外接询问切换
def choice_Large_Model():
    Large_model = input("1. DeepSeek-R1 \n2. DeepSeek-V3 \n3. DeepSeek-R1-Distill-Liama-70B \n 请配置您需要的大模型： ")
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

# API设置
def API_Setting(question ,stream):
    stream = False
    role = "user"
    content = f"你是一位专业的，从业40年的中医按摩医师，对人体穴位了解十分精通，现在有一位病人：{question}，帮他按摩一下,并给出详细步骤和按摩方案"
    return stream, role, content

if __name__ == '__main__':
    # 大模型选择
    choice = choice_Large_Model()

    # 语音模块接入
    question = ask_condition_first()
    if question == "exit":
        ask_condition_bye()
    else:
        setting = API_Setting(question , stream = False)
        result = Deepseek_API(choice[0], choice[1], choice[2], setting[0], setting[1], setting[2])
        EPG(result)
        # 第二次询问
        question = ask_condition_sec()
        if question == "exit":
            ask_condition_bye()
        else:
            setting = API_Setting(question, stream=False)
            result = Deepseek_API(choice[0], choice[1], choice[2], setting[0], setting[1], setting[2])
            EPG(result)
            while True:
                question = ask_condition_other()
                if question == "exit":
                    ask_condition_bye()
                    break
                else:
                    setting = API_Setting(question, stream=False)
                    result = Deepseek_API(choice[0], choice[1], choice[2], setting[0], setting[1], setting[2])
                    EPG(result)


