from esAPI import esAPI
import json

esapi = esAPI(url='http://jwxt.gcu.edu.cn',code='huananligongdaxueguangzhouxueyuan', account='201810098161', password='wwd123456')
login_result = esapi.user_login()
if login_result is True:
    print(json.dumps(esapi.get_schedule()))
else:
    print(login_result)

