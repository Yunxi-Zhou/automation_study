import requests
import unittest
import re

class TestCookieToken(unittest.TestCase):

    csrf_token = ""
    session = requests.session()

    def test_1_index(self):
        url = "http://47.107.116.139/phpwind/"
        res = TestCookieToken.session.get(url=url)

        value = re.search('name="csrf_token" value="(.+?)"',res.text)
        print(value)
        TestCookieToken.csrf_token = value.group(1)

    def test_2_login(self):
        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login"
        data = {
            "username": "admin",
            "password": "msxy",
            "csrf_token": TestCookieToken.csrf_token,
            "back_url": "http://47.107.116.139/phpwind/",
            "invite": ""

        }
        headers = {
            "Accept": "application/json text/javascript, /; q=0.01",
            "X-Requested-With": "XMLHttpRequest"
        }
        res = TestCookieToken.session.post(url=url,data=data,headers=headers)
        print(res.text)