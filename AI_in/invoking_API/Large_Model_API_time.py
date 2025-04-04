#

import time
from openai import OpenAI
from Individuation.Ind_for_ask import print_show_beatuiful

def Deepseek_API(base_url, api_key, model, stream, role, content):
    '''
    封装Deepseek-API接口
    :param base_url: API链接地址
    :param api_key: API秘钥
    :param model: 模型选择
    :param stream: 是否为流式输出
    :param role: 角色
    :param content: 语句
    :return:
    '''
    # 记录开始时间
    start_time = time.perf_counter()

    try:
        # 构造 client
        client = OpenAI(
            base_url=base_url,
            api_key=api_key,
        )

        # 发送请求
        chat_completion = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": role,
                    "content": content,
                }
            ],
            stream=stream,
        )

        if stream:
            for chunk in chat_completion:
                # 思维链内容
                if hasattr(chunk.choices[0].delta, 'reasoning_content'):
                    if chunk.choices[0].delta.reasoning_content is not None and len(
                            chunk.choices[0].delta.reasoning_content) != 0:
                        print(f"{chunk.choices[0].delta.reasoning_content}", end="")

                # 模型最终返回的content
                if hasattr(chunk.choices[0].delta, 'content'):
                    if chunk.choices[0].delta.content is not None and len(chunk.choices[0].delta.content) != 0:
                        print(chunk.choices[0].delta.content, end="")
        else:
            result = chat_completion.choices[0].message.content
            return result

    finally:
        # 记录结束时间
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print_show_beatuiful(f"函数运行时间：{elapsed_time:.6f} 秒")
        #print(f"函数运行时间：{elapsed_time:.6f} 秒")

# 示例调用
if __name__ == "__main__":
    # 替换为你的参数
    base_url = "https://api.deepseek.com/v1"
    api_key = "your_api_key"
    model = "your_model"
    stream = False
    role = "user"
    content = "Hello, how are you?"

    # 调用函数
    result = Deepseek_API(base_url, api_key, model, stream, role, content)
    print("\n最终结果：", result)