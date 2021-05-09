import requests
import json

AC_definition = [3, 2, 1, 0]


class AcFun:

    def __init__(self, rid, quality):
        self.rid = rid
        self.quality = quality

    def get_real_url(self):
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': '_did=H5_',
            'referer': 'https://m.acfun.cn/'
        }
        url = 'https://id.app.acfun.cn/rest/app/visitor/login'
        data = 'sid=acfun.api.visitor'
        res = requests.post(url, data=data, headers=headers).json()
        userid = res['userId']
        visitor_st = res['acfun.api.visitor_st']

        url = 'https://api.kuaishouzt.com/rest/zt/live/web/startPlay'
        params = {
            'subBiz': 'mainApp',
            'kpn': 'ACFUN_APP',
            'kpf': 'PC_WEB',
            'userId': userid,
            'did': 'H5_',
            'acfun.api.visitor_st': visitor_st
        }
        data = f'authorId={self.rid}&pullStreamType=FLV'
        res = requests.post(url, params=params, data=data,
                            headers=headers).json()
        if res['result'] == 1:
            data = res['data']
            videoplayres = json.loads(data['videoPlayRes'])
            liveadaptivemanifest, = videoplayres['liveAdaptiveManifest']
            adaptationset = liveadaptivemanifest['adaptationSet']
            # noinspection PyBroadException
            try:
                representation = adaptationset['representation'][3 - self.quality]
                real_url = representation['url']
                return real_url
            except Exception:
                return 'Current quality type not exist.'
        else:
            return 'Live streaming not found'


if __name__ == '__main__':
    r = input('请输入AcFun直播房间号：\n')
    acfun = AcFun(r, 3)
    r = acfun.get_real_url()
    print(r)
