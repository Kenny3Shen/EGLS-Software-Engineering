import requests

Bili_definition = ['10000', '400', '250', '150']


class BiliBili:

    def __init__(self, rid, quality):
        self.rid = rid
        self.quality = quality

    def get_real_url(self):
        # Get the live status and real room number first
        r_url = f'https://api.live.bilibili.com/room/v1/Room/room_init?id={self.rid}'
        with requests.Session() as s:
            res = s.get(r_url).json()
        code = res['code']
        if code == 0:
            live_status = res['data']['live_status']
            if live_status == 1:
                room_id = res['data']['room_id']
                f_url = 'https://api.live.bilibili.com/xlive/web-room/v1/playUrl/playUrl'
                params = {
                    'cid': room_id,
                    'qn': Bili_definition[self.quality],
                    'platform': 'web',
                    'https_url_req': 1,
                    'ptype': 16
                }
                resp = s.get(f_url, params=params).json()
                try:
                    durl = resp['data']['durl']
                    real_url = durl[-1]['url']
                    return real_url
                except KeyError or IndexError:
                    return 'Failed to get link'
            else:
                return 'Live is offline'
        else:
            return 'Room not exist'


if __name__ == '__main__':
    r = input('请输入bilibili直播房间号：\n')
    bilibili = BiliBili(r, 0)
    print(bilibili.get_real_url())
