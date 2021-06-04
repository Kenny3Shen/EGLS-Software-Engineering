import requests
import re
import base64
import urllib.parse
import hashlib
import time

HuYa_Quality = ['', '_4000', '_2000', '_1200']


class HuYa:

    def __init__(self, rid, quality):
        self.rid = rid
        self.quality = quality

    def get_real_url(self):
        # noinspection PyBroadException
        try:
            room_url = f'https://m.huya.com/{self.rid}'
            header = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36 '
            }
            response = requests.get(url=room_url, headers=header).text
            liveLineUrl = re.findall(r'liveLineUrl = "([\s\S]*?)";', response)[0]
            liveLineUrl = str(base64.b64decode(liveLineUrl), "utf-8")
            isReplay = False
            if liveLineUrl:
                if 'replay' in liveLineUrl:
                    isReplay = True
                    real_url = f"https:{self.live(liveLineUrl)}"
                else:
                    real_url = f"https:{self.live(liveLineUrl)}"
                if not isReplay:
                    r = re.sub('.m3u8', f'{HuYa_Quality[self.quality]}.m3u8', real_url)
                    return r
                else:
                    return real_url
            else:
                return 'Live streaming not found or room not exist'
        except Exception:
            return 'Live streaming not found or room not exist'

    @staticmethod
    def live(e):
        i, b = e.split('?')
        r = i.split('/')
        s = re.sub(r'.(flv|m3u8)', '', r[-1])
        c = b.split('&')
        c = [i for i in c if i != '']
        n = {i.split('=')[0]: i.split('=')[1] for i in c}
        fm = urllib.parse.unquote(n['fm'])
        u = base64.b64decode(fm).decode('utf-8')
        p = u.split('_')[0]
        f = str(int(time.time() * 1e7))
        ctype = n['ctype']
        t = n['t']
        mf = hashlib.md5((f + '|' + ctype + '|' + t).encode('utf-8')).hexdigest()
        ll = n['wsTime']
        uid = '0'
        h = '_'.join([p, uid, s, mf, ll])
        m = hashlib.md5(h.encode('utf-8')).hexdigest()
        url = "{}?wsSecret={}&wsTime={}&uid={}&seqid={}&ctype={}&ver=1&t={}".format(i, m, ll, uid, f, ctype, t)
        return url


if __name__ == '__main__':
    room = input('输入虎牙直播房间号：\n')
    hy = HuYa(room, 1)
    print(hy.get_real_url())
