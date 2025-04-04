# DeepSeekAPI接口
# 官方库
from openai import OpenAI

# 自定义库
#

# 定义DeepseekAPI接口
def Deepseek_API(base_url , api_key , model , stream, role , content):
    '''
    封装Deepseek-API接口
    :param base_url:API链接地址
    :param api_key:API秘钥
    :param model:模型选择
    :param stream:是否为流式输出
    :param role:角色
    :param content:语句
    :return:
    '''
    # 构造 client
    client = OpenAI(
        base_url=base_url,
        api_key=api_key,
    )
    # 流式
    stream = stream
    # 发送请求
    chat_completion = client.chat.completions.create(
        model= model,
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
                if chunk.choices[0].delta.reasoning_content != None and len(
                        chunk.choices[0].delta.reasoning_content) != 0:
                    print(f"{chunk.choices[0].delta.reasoning_content}", end="")

            # 模型最终返回的content
            if hasattr(chunk.choices[0].delta, 'content'):
                if chunk.choices[0].delta.content != None and len(chunk.choices[0].delta.content) != 0:
                    print(chunk.choices[0].delta.content, end="")

    else:
        result = chat_completion.choices[0].message.content
        return result
























