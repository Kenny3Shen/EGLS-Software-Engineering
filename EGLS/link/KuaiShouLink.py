# test: https://live.kuaishou.com/u/KPL704668133
# 如获取失败，尝试修改 cookie 中的 did

import json
import re
import requests


# did=web_e9f23e35be2c6eefde872a9296d7a4fa
class KuaiShou:

    def __init__(self, rid, quality, cookie='did=web_e9f23e35be2c6eefde872a9296d7a4fa'):
        self.rid = rid
        self.quality = quality
        self.cookie = cookie

    def get_real_url(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54',
            'cookie': self.cookie}
        with requests.Session() as s:
            res = s.get(f'https://live.kuaishou.com/u/{self.rid}', headers=headers)
            try:
                livestream = re.findall(r'liveStream":(.*),"feedInfo"', res.text)[0]
            except Exception:
                return 'RoomID not exist'
            if livestream:
                try:
                    livestream = json.loads(livestream)
                    playUrls = livestream['json']['playUrls']
                    url = playUrls[self.quality]["url"]
                    return url
                except Exception:
                    return 'RoomID not exist or Current quality type not exist'
            else:
                return 'Live streaming not found or room not exist'


def get_real_url(rid, q):
    try:
        ks = KuaiShou(rid, q)
        return ks.get_real_url()
    except Exception as e:
        print('Exception：', e)
        return False


if __name__ == '__main__':
    # KPL704668133
    r = 'pubg98k416'
    print(get_real_url(r, 0))
