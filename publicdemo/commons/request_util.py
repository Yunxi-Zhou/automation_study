import requests

class RequestUtil:
    sess = requests.Session()

    # common send requests
    # Connection: keep-alive
    def all_send_request(self, **kwargs):
        res = RequestUtil.sess.request(**kwargs)
        print("返回内容：",res.text)
        return res