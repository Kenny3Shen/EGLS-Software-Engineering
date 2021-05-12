import hashlib
import re
import time
import execjs
import requests


# 获取斗鱼和爱奇艺的直播源，需 JavaScript 环境，可使用 node.js。


class DouYu:

    def __init__(self, rid, quality):
        # 房间号通常为1~7位纯数字，浏览器地址栏中看到的房间号不一定是真实rid.
        self.DY_definition = ['', '4000p', '2000p', '1200p']
        self.did = '10000000000000000000000000001501'
        self.t10 = str(int(time.time()))
        self.t13 = str(int((time.time() * 1000)))
        self.quality = quality
        self.s = requests.Session()
        self.res = self.s.get('https://m.douyu.com/' + str(rid)).text
        self.rid = self.getRID()

    def getRID(self):
        result = re.search(r'rid":(\d{1,7}),"vipId', self.res)
        if result:
            return result.group(1)
        else:
            return 'Illegal Room ID or not found'

    @staticmethod
    def md5(data):
        return hashlib.md5(data.encode('utf-8')).hexdigest()

    def get_pre(self):
        url = 'https://playweb.douyucdn.cn/lapi/live/hlsH5Preview/' + self.rid
        data = {
            'rid': self.rid,
            'did': self.did
        }
        auth = DouYu.md5(self.rid + self.t13)
        headers = {
            'rid': self.rid,
            'time': self.t13,
            'auth': auth
        }
        res = self.s.post(url, headers=headers, data=data).json()
        error = res['error']
        data = res['data']
        key = ''
        if data:
            rtmp_live = data['rtmp_live']
            key = re.search(r'(\d{1,7}[0-9a-zA-Z]+)_?\d{0,4}(/playlist|.m3u8)', rtmp_live).group(1)
        return error, key

    def get_js(self):
        result = re.search(r'(function ub98484234.*)\s(var.*)', self.res).group()
        func_ub9 = re.sub(r'eval.*;}', 'strc;}', result)
        js = execjs.compile(func_ub9)
        res = js.call('ub98484234')

        v = re.search(r'v=(\d+)', res).group(1)
        rb = DouYu.md5(self.rid + self.did + self.t10 + v)

        func_sign = re.sub(r'return rt;}\);?', 'return rt;}', res)
        func_sign = func_sign.replace('(function (', 'function sign(')
        func_sign = func_sign.replace('CryptoJS.MD5(cb).toString()', '"' + rb + '"')

        js = execjs.compile(func_sign)
        params = js.call('sign', self.rid, self.did, self.t10)
        params += '&ver=219032101&rid={}&rate=-1'.format(self.rid)

        url = 'https://m.douyu.com/api/room/ratestream'
        res = self.s.post(url, params=params).text
        key = re.search(r'(\d{1,7}[0-9a-zA-Z]+)_?\d{0,4}(.m3u8|/playlist)', res).group(1)

        return key

    def get_pc_js(self, cdn='ws-h5', rate=0):
        """
        通过PC网页端的接口获取完整直播源。
        :param cdn: 主线路ws-h5、备用线路tct-h5
        :param rate: 1流畅；2高清；3超清；4蓝光4M；0蓝光8M或10M
        :return: JSON格式
        """
        res = self.s.get('https://www.douyu.com/' + str(self.rid)).text
        result = re.search(r'(vdwdae325w_64we[\s\S]*function ub98484234[\s\S]*?)function', res).group(1)
        func_ub9 = re.sub(r'eval.*?;}', 'strc;}', result)
        js = execjs.compile(func_ub9)
        res = js.call('ub98484234')

        v = re.search(r'v=(\d+)', res).group(1)
        rb = DouYu.md5(self.rid + self.did + self.t10 + v)

        func_sign = re.sub(r'return rt;}\);?', 'return rt;}', res)
        func_sign = func_sign.replace('(function (', 'function sign(')
        func_sign = func_sign.replace('CryptoJS.MD5(cb).toString()', '"' + rb + '"')

        js = execjs.compile(func_sign)
        params = js.call('sign', self.rid, self.did, self.t10)

        params += '&cdn={}&rate={}'.format(cdn, rate)
        url = 'https://www.douyu.com/lapi/live/getH5Play/{}'.format(self.rid)
        res = self.s.post(url, params=params).json()

        return res

    def get_Third_API(self):
        url = f'https://web.sinsyth.com/lxapi/douyujx.x?roomid={self.rid}'
        js = requests.get(url).json()
        if js['state'] == 'SUCCESS':
            stream = js['Rendata']['link']
            patten = r'\/([0-9].*?)[_.]'
            ID = re.search(patten, stream).group(0)
            if ID[-1] == '.':  # replay
                trueLink = f'http://tx2play1.douyucdn.cn/live{ID}flv?uuid='
            elif self.quality == 0:
                trueLink = f'http://tx2play1.douyucdn.cn/live{ID[:-1]}.flv?uuid='
            else:
                trueLink = f'http://tx2play1.douyucdn.cn/live{ID}{self.DY_definition[self.quality]}.flv?uuid='
            return trueLink
        elif js['state'] == 'NO':
            return 'Live is offline'
        else:
            return 'Live Stream Not Found'

    def get_real_url(self):
        if self.rid == 'Illegal Room ID or not found':
            return self.rid
        error, key = self.get_pre()
        if error == 0:
            pass
        elif error == 102:
            return 'Room not exist'
        elif error == 104:
            return 'Live is offline'
        else:
            key = self.get_js()
        if self.quality == 0:
            trueLink = f"http://tx2play1.douyucdn.cn/live/{key}.flv?uuid="
        else:
            trueLink = f"http://tx2play1.douyucdn.cn/live/{key}_{self.DY_definition[self.quality]}.flv?uuid="
        return trueLink


if __name__ == '__main__':
    r = input('输入斗鱼直播间号：\n')
    s = DouYu(r, 1)
    print(s.get_real_url())
