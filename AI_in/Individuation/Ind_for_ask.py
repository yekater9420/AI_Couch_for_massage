# 个性化询问病情包
import random
from datetime import datetime

# 获取当前时间
current_time = datetime.now()
# 格式化时间并打印
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
hour = current_time.hour
ask_call = ["主人" , "总裁大人"]
ask_text = ["最近有什么不适吗？","最近有什么情况？","今天有什么不舒服的吗？"]
ask_for = ["我可以帮您做点什么？" ,"有什么我可以帮您的吗？","需要我帮您按摩吗？","需要一些按摩吗？"]
ask_time = {"早上好" , "中午好", "下午好" , "晚上好" , "夜深了，早点休息吧"}

def ask_condition_first():
    random_word_call = random.choice(ask_call)
    random_word_text = random.choice(ask_text)
    random_word = random.choice(ask_for)

    if 6<= hour <=10:
        return input(f"亲爱的{random_word_call}，早上好，我是您的私人AI按摩师，{random_word_text}{random_word}:")
    elif 11<= hour <=14:
        return input(f"亲爱的{random_word_call}，中午好，我是您的私人AI按摩师，{random_word_text}{random_word}:")
    elif 15<= hour <=18:
        return input(f"亲爱的{random_word_call}，下午好，我是您的私人AI按摩师，{random_word_text}{random_word}:")
    elif 19<= hour <=23:
        return input(f"亲爱的{random_word_call}，晚上好，我是您的私人AI按摩师，{random_word_text}{random_word}:")
    else:
        return input(f"亲爱的{random_word_call}，我是您的私人AI按摩师，夜深了，还不休息吗^^？{random_word_text}{random_word}:")


ask_text_sec = ["还有其他不舒服的吗？","可以进一步形容一下吗，是怎么样的疼痛？","可以再具体一下吗？"]
def  ask_condition_sec():
    random_word_call_sec = random.choice(ask_text_sec)
    return input(f"{random_word_call_sec}：")

ask_text_other = ["这个力度怎么样？","我的手法还行吗？","需要加大或者减小力道吗?","现在感觉怎么样？"]
def ask_condition_other():
    random_word_call_other = random.choice(ask_text_other)
    return input(f"{random_word_call_other}：")

ask_text_bye = ["如果您还有需要，请随时叫我~" , "按摩结束，您要注意休息，身体最重要，不要过度劳累~"]
def ask_condition_bye():
    random_word_call = random.choice(ask_call)
    random_word_call_bye = random.choice(ask_text_bye)
    if 19 <= hour <= 23:
        return print(f"亲爱的{random_word_call}，{random_word_call_bye}晚安~")
    if 0<= hour <= 6:
        return print(f"亲爱的{random_word_call}，夜深了，早点休息，{random_word_call_bye}晚安~")


