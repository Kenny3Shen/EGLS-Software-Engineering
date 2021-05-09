import requests
import re
import base64
import urllib.parse
import hashlib
import time
# TODO
HuYa_Channel = ['2000p', 'tx', 'bd', 'migu-bd']


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
                    real_url = {
                        'replay': "https:" + liveLineUrl,
                    }
                else:
                    s_url = self.live(liveLineUrl)
                    b_url = self.live(liveLineUrl.replace('_2000', ''))
                    real_url = {
                        '2000p': "https:" + s_url,
                        'tx': "https:" + b_url,
                        'bd': "https:" + b_url.replace('tx.hls.huya.com', 'bd.hls.huya.com'),
                        'migu-bd': "https:" + b_url.replace('tx.hls.huya.com', 'migu-bd.hls.huya.com'),
                    }

                if not isReplay:
                    return real_url[HuYa_Channel[self.quality]]
                else:
                    return real_url['replay']
            else:
                return 'Live streaming not found or room not exist'
        except Exception:
            return 'Live streaming not found or room not exist'

    @staticmethod
    def live(e):
        i, b = e.split('?')
        r = i.split('/')
        s = re.sub(r'.(flv|m3u8)', '', r[-1])
        c = b.split('&', 3)
        c = [i for i in c if i != '']
        n = {i.split('=')[0]: i.split('=')[1] for i in c}
        fm = urllib.parse.unquote(n['fm'])
        u = base64.b64decode(fm).decode('utf-8')
        p = u.split('_')[0]
        f = str(int(time.time() * 1e7))
        ll = n['wsTime']
        t = '0'
        h = '_'.join([p, t, s, f, ll])
        m = hashlib.md5(h.encode('utf-8')).hexdigest()
        y = c[-1]
        url = f"{i}?wsSecret={m}&wsTime={ll}&u={t}&seqid={f}&{y}"
        return url


if __name__ == '__main__':
    room = input('输入虎牙直播房间号：\n')
    hy = HuYa(room, 0)
    print(hy.get_real_url())
