import jsonpath
import pytest
from publicdemo.commons.request_util import RequestUtil
from publicdemo.commons.yaml_util import write_yaml, read_yaml, read_testcase

class TestApi:
    # 1. get the access token Interface
    @pytest.mark.parametrize("casedata",read_testcase("./testcases/dk_manage/test_get_token.yaml"))
    def test_get_token(self,casedata):
        method = casedata["request"]['method']
        url = casedata["request"]["url"]
        datas = casedata["request"]["params"]
        res = RequestUtil().all_send_request(method=method,url=url,params=datas)
        result = res.json()
        if "access_token" in res.text:
            # get access token (method 1: use global value to store and get the value)
            # method 2: save API response in yaml
            value = jsonpath.jsonpath(result, "$.access_token")
            data = {"access_token": value[0]}
            write_yaml(data)

    # 2. get tag API Interface
    @pytest.mark.parametrize("casedata",read_testcase("./testcases/dk_manage/test_select_flag.yaml"))
    def test_select_flag(self,casedata):
        method = casedata["request"]['method']
        url = casedata["request"]["url"]
        datas = casedata["request"]["params"]
        for key,value in datas.items():
            datas[key] = read_yaml(key)
        RequestUtil().all_send_request(method=method,url=url,params=datas)

    # 3. upload file
    @pytest.mark.parametrize("casedata",read_testcase("./testcases/dk_manage/test_file_upload.yaml"))
    def test_file_upload(self,casedata):
        method = casedata["request"]['method']
        url = casedata["request"]["url"]
        datas = casedata["request"]["params"]
        files = casedata["request"]["files"]
        for key,value in datas.items():
            datas[key] = read_yaml(key)
        for key,value in files.items():
            files[key] = open(value,"rb")
        # mac: /Users/ethan/Downloads/IMG_2049.jpg
        # windows: C:\\Users\zhouy\Downloads\IMG_2049.jpg
        RequestUtil().all_send_request(method=method,url=url,params=datas,files=files)