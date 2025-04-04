# Electronic prescription generator 电子药方生成器
import re
from datetime import datetime

# 获取当前时间
current_time = datetime.now()
# 格式化时间并打印
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# 分割文本以找到</think> 之后的内容
def EPG(ask , choice):
    if choice == "1":
        match = re.search(r'</think>(.*?)$', ask, re.DOTALL)
        result = match.group(1)
        result = re.sub(r'^\s', '', result)
        result = re.sub(r'^\s', '', result)
        print()
        print("===" * 30)
        print(" " * 34 + "电子药方 - 按摩方案" + " " * 34)
        print("=^=" * 30)
        print(result)
        print("===" * 30)
        print("按摩方案生成时间为：", formatted_time)
        print("===" * 30)
        print()
        # 将结果写入文件
        file_path = "Electronic_scheme/电子药方-按摩方案.txt"
        file = open(file_path, "a", encoding="utf-8")  # "w" 表示写入模式，encoding指定编码
        # 写入内容
        file.writelines(result)
        # 关闭文件
        file.close()

    if choice == "2":
        index = ask.find("</think>")
        result = ask[index + len("</think>"):]
        index_2 = result.find("###")
        result = result[index_2:]
        print()
        print("===" * 30)
        print(" " * 34 + "电子药方 - 按摩方案" + " " * 34)
        print("=^=" * 30)
        print(result)
        print("===" * 30)
        print("按摩方案生成时间为：", formatted_time)
        print("===" * 30)
        print()
        # 将结果写入文件
        file_path = "Electronic_scheme/电子药方-按摩方案.txt"
        file = open(file_path, "a", encoding="utf-8")  # "w" 表示写入模式，encoding指定编码
        # 写入内容
        file.writelines(result)
        # 关闭文件
        file.close()

    if choice == "3":
        index = ask.find("</think>")
        result = ask[index + len("</think>"):]
        index_2 = result.find("###")
        result = result[index_2:]
        print()
        print("===" * 30)
        print(" " * 34 + "电子药方 - 按摩方案" + " " * 34)
        print("=^=" * 30)
        print(result)
        print("===" * 30)
        print("按摩方案生成时间为：", formatted_time)
        print("===" * 30)
        print()
        # 将结果写入文件
        file_path = "Electronic_scheme/电子药方-按摩方案.txt"
        file = open(file_path, "a", encoding="utf-8")  # "w" 表示写入模式，encoding指定编码
        # 写入内容
        file.writelines(result)
        # 关闭文件
        file.close()







