# !/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import logging

def selectESLogs(event, context):
    logger = logging.getLogger()
    try:
        url = 'http://198.23.1.23:9200/sudiyi_java*/_search'
        data = {
            "size": 10,
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "info_content.deviceId": "110000001"
                            }
                        },
                        {
                            "match": {
                                "info_content.packetType": "2"
                            }
                        }
                    ]
                }
            }
        }
        response = requests.post(url, data)
    except Exception:
        logging.debug("获取ES查询失败")
    return "返回状态：%s,返回结果：%s " % (response.status_code,response.text)