# 阿里ASR-API获取
import os
import time
import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from datetime import datetime

# 时间获取
current_time = datetime.now()
# 格式化时间并打印
formatted_time = current_time.strftime("%Y-%m-%d")

def ASR_token_get():
   # 从环境变量中获取凭证 ***
   # 创建AcsClient实例
   client = AcsClient(
      os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID'),
      os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET'),
       "cn-beijing"
   );

   # 创建request，并设置参数。
   request = CommonRequest()
   request.set_method('GET')
   request.set_domain('nls-gateway.aliyuncs.com')
   request.set_version('2019-02-28')
   request.set_action_name('CreateToken')
   response = client.do_action_with_exception(request)
   jss = json.loads(response)
   request_id = jss.get('request_id')
   return request_i
   d