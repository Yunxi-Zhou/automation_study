import jsonpath
import random
import json
from publicdemo.commons.request_util import RequestUtil


class TestApi:
    access_token = ""

    # 1. get the access token Interface
    def test_get_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        datas = {
            "grant_type": "client_credential",
            "appid": "wx74a8627810cfa308",
            "secret": "e40a02f9d79a8097df497e6aaf93ab80"
        }
        res = RequestUtil().all_send_request(method="get",url=url,params=datas)
        result = res.json()
        print(result)
        # get access token (method 1: use global value to store and get the value)
        value = jsonpath.jsonpath(result, "$.access_token")
        TestApi.access_token = value[0]

    # 2. get tag API Interface
    def test_select_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/get"
        datas = {
            "access_token": TestApi.access_token
        }
        res = RequestUtil().all_send_request(method="get",url=url,params=datas)

    # 3. create tag API InterFace (post)
    def test_create_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/create?access_token=" + TestApi.access_token
        datas = {
            "tag":{"name":"广东"+str(random.randint(10000,99999))}
        }
        res = RequestUtil().all_send_request(method="post",url=url, json=datas)
        result_str = json.loads(json.dumps(res.json()).replace("\\\\","\\"))

    # 4. delete file
    def test_file_upload(self):
        url = "https://api.weixin.qq.com/cgi-bin/media/upload?acpi.access_token" + TestApi.access_token
        datas = {"media": open("/Users/ethan/Downloads/IMG_2049.jpg", "rb")}
        # mac: /Users/ethan/Downloads/IMG_2049.jpg
        # windows: C:\\Users\zhouy\Downloads\IMG_2049.jpg
        res = RequestUtil().all_send_request(method="post",url=url, files=datas)
        print(res.json())