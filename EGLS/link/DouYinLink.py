import requests
import re
Bili_definition = ['10000', '400', '250', '150']


class DouYin:

    def __init__(self, rid, quality):
        self.rid = rid
        self.quality = quality

    def get_real_url(self):
        try:
            room_id = re.findall(r'(\d{19})', requests.get(f'https://v.douyin.com/{self.rid}').url)[0]
            room_url = f'https://webcast.amemv.com/webcast/reflow/{room_id}'
            response = requests.get(url=room_url).text
            rtmp_pull_url = re.search(r'"rtmp_pull_url":"(.*?flv)"', response).group(1)
            hls_pull_url = re.search(r'"hls_pull_url":"(.*?m3u8)"', response).group(1)
            real_url = [rtmp_pull_url, hls_pull_url]
            return real_url[self.quality]
        except Exception:
            return 'Live streaming not found or room not exist'


if __name__ == '__main__':
    r = input('请输入bilibili直播房间号：\n')
    DouYin = DouYin(r, 1)
    print(DouYin.get_real_url())
