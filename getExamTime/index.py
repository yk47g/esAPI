# -*- coding: utf8 -*-
import json
from esAPI import esAPI
def main_handler(event, context):
    # print("Received event: " + json.dumps(event, indent = 2))
    # print("Received context: " + str(context))
    account = event["queryString"]["account"]
    password = event["queryString"]["password"]
    esapi = esAPI(url='http://jwxt.gcu.edu.cn',code='huananligongdaxueguangzhouxueyuan', account=account, password=password)
    login_result = esapi.user_login()
    if login_result is True:
        return esapi.get_exam_time()
    else:
        return login_result
