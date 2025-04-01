f = open("config/config_ASR.yaml", "r", encoding="utf-8")
conf_str = f.read()
f.close() # 及时释放资源，防止数据损坏和锁定
config = yaml.load(conf_str, Loader=yaml.FullLoader)
ARS_url = config["ALI"]["BeiJing"]["ASR_URL"]
AppKEY = config["ALI"]["BeiJing"]["APPKEY"]
print(ARS_url)
print(AppKEY)

