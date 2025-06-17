import requests

class RequestUtil:
    sess = requests.Session()

    # common send requests
    def all_send_request(self, **kwargs):
        res = RequestUtil.sess.request(**kwargs)
        return res