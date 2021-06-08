from threading import Thread
from PySide2.QtWidgets import QWidget
import asyncio
from danmu import danmaku
from danmu_ui import Ui_Form
import MySignal


class DanMu(QWidget):
    def __init__(self, url, platform, room):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle(f'{platform}_{room}')
        self.ui.danmuText.ensureCursorVisible()
        self.url = url
        self.MySignal = MySignal.MySignal()
        self.stop = False
        self.MySignal.danmu_update.connect(self.setDanMu)

        Thread(target=lambda: asyncio.run(self.main()), daemon=True).start()

    def setDanMu(self, msg):
        self.ui.danmuText.append(msg)

    def closeEvent(self, event) -> None:
        self.stop = True
        event.accept()

    async def printer(self, q):
        while not self.stop:
            m = await q.get()
            if m['msg_type'] == 'danmaku':
                # print(f'{m["name"]}：{m["content"]}')
                self.MySignal.danmu_update.emit(f'{m["name"]}：<font color="white">{m["content"]}</font>')

    async def main(self):
        q = asyncio.Queue()
        dmc = danmaku.DanmakuClient(self.url, q)
        asyncio.create_task(self.printer(q))
        try:
            await dmc.start()
        except Exception as e:
            self.MySignal.danmu_update.emit(f'{str(e)}，请稍后再试或尝试更换cookie（快手平台）。')
            await dmc.stop()
