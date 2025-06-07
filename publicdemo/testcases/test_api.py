import jsonpath
import requests
import random
import json
import re

class TestApi:
    access_token = ""
    csrf_token = ""

    # 1. get the access token Interface
    def test_get_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        datas = {
            "grant_type": "client_credential",
            "appid": "wx74a8627810cfa308",
            "secret": "e40a02f9d79a8097df497e6aaf93ab80"
        }
        res = requests.get(url, params=datas)
        result = res.json()
        # get access token (method 1: use global value to store and get the value)
        value = jsonpath.jsonpath(result, "$.access_token")
        TestApi.access_token = value[0]

    # 2. get tag API Interface
    def test_select_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/get"
        datas = {
            "access_token": TestApi.access_token
        }
        res = requests.get(url, params=datas)

    # 3. create tag API InterFace (post)
    def test_create_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/create?access_token=" + TestApi.access_token
        datas = {
            "tag":{"name":"广东"+str(random.randint(10000,99999))}
        }
        res = requests.post(url, json=datas)
        result_str = json.loads(json.dumps(res.json()).replace("\\\\","\\"))

    # 4. delete file
    def test_file_upload(self):
        url = "https://api.weixin.qq.com/cgi-bin/media/upload?acpi.access_token" + TestApi.access_token
        datas = {"media": open("/Users/ethan/Downloads/IMG_2049.jpg", "rb")}
        res = requests.post(url, json=datas)
        print(res.json())

    # cookie related interface
    def test_start(self):
        url = "http://47.107.116.139/phpwind/"
        res = requests.get(url)
        result = res.text
        print(result)
        TestApi.csrf_token = re.search('name="csrf_token" value="(.*?)"', result).group(1)

    def test_login(self):
        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        datas = {
            "username": "zhouy218",
            "password": "136671",
            "csrf_token": read_yaml("csrf_token"),
            "back_url": "http://47.107.116.139/phpwind/",
            "invite": ""
        }
        headers = {
            "Accept": "application/json, text/javascript, /; q=0.01",
            "X-Requested-With": "XMLHttpRequest"
        }
        res = requests.post(url, json=datas, headers=headers)
        print(res.json())

if __name__ == '__main__':
    test = TestApi()
    test.test_get_token()
    test.test_select_flag()
    test.test_file_upload()
    test.test_start()