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

def ask_condition():
    random_word_call = random.choice(ask_call)
    random_word_text = random.choice(ask_text)
    random_word = random.choice(ask_for)
    if 6<= hour <=10:
        input(f"亲爱的{random_word_call}，早上好，我是您的私人按摩师，{random_word_text}{random_word}:")
    elif 11<= hour <=14:
        input(f"亲爱的{random_word_call}，中午好，我是您的私人按摩师，{random_word_text}{random_word}:")
    elif 15<= hour <=18:
        input(f"亲爱的{random_word_call}，下午好，我是您的私人按摩师，{random_word_text}{random_word}:")
    elif 19<= hour <=23:
        input(f"亲爱的{random_word_call}，晚上好，我是您的私人按摩师，{random_word_text}{random_word}:")
    else:
        input(f"亲爱的{random_word_call}，我是您的私人按摩师，夜深了，还点休息吗^^？{random_word_text}{random_word}:")


