from publicdemo.commons.request_util import RequestUtil
import re
import pytest

class TestPhpwind:
    csrf_token = ""

    # cookie related interface
    @pytest.mark.smoke
    def test_start(self):
        url = "http://47.107.116.139/phpwind/"
        res = RequestUtil().all_send_request(method="get",url=url)
        result = res.text
        TestPhpwind.csrf_token = re.search('name="csrf_token" value="(.*?)"', result).group(1)
        print(TestPhpwind.csrf_token)

    @pytest.mark.smoke
    def test_login(self):
        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        datas = {
            "username": "zhouy218",
            "password": "136671",
            "csrf_token": TestPhpwind.csrf_token,
            "back_url": "http://47.107.116.139/phpwind/",
            "invite": ""
        }
        headers = {
            "Accept": "application/json, text/javascript, /; q=0.01",
            "X-Requested-With": "XMLHttpRequest"
        }
        res = RequestUtil().all_send_request(method="post",url=url, data=datas, headers=headers)
        print(res.json())