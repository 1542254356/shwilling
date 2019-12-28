import json
import traceback

import requests

url = "http://www.shwilling.com/portal/index/getMpnewsByType"

def getData(start = 0):
    data = {
        'hot_mpnews_num': start,
        "type_id": "hot"
    }
    try:
        ret = requests.post(url, data=data)
    except requests.exceptions.ConnectionError as e:
        traceback.print_stack()
        # 请求频繁导致失败
        return None

    if ret.status_code != 200:
        print("请求错误：", ret.text)
        return None

    try:
        jsonret = json.loads(ret.text)

        if jsonret['errcode'] != 0:
            print(jsonret['errmsg'])
            return None

        return jsonret['data']

    except json.decoder.JSONDecodeError as e:
        print("json解析错误", e)
        return None

def getAllDatas():
    list = []
    start = 0

    while True:
        data = getData(start)
        print(start, len(data))
        if len(data) == 0:
            print("完成")
            break
        list += data
        start += 100

    return list

def main():
    list = []
    start = 0

    while True:
        data = getData(start)
        print(len(data))
        if len(data) == 0 :
            print("完成")
            break
        list += data
        start += 100

    print(list)


if __name__ == '__main__':
    main()