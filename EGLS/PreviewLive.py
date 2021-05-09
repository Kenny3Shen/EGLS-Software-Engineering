import time
from PySide2.QtWidgets import QWidget
import threading
import cv2
from PySide2 import QtCore
from PySide2.QtGui import QImage, QPixmap
from preview_ui import Ui_Form


class Preview(QWidget):
    def __init__(self, url):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_Form()
        # 初始化界面
        self.ui.setupUi(self)
        self.url = url
        self.ui.Camera1.setMinimumSize(QtCore.QSize(320, 180))
        self.ui.Camera1.setMaximumSize(QtCore.QSize(320, 180))
        self.ui.Camera1.setAutoFillBackground(True)
        self.ui.Camera1.setScaledContents(True)
        self.ui.gridLayout.addWidget(self.ui.Camera1, 0, 0, 0, 0)
        self.stop = False
        threading.Thread(target=self.showPreview).start()

    def closeEvent(self, event) -> None:
        self.stop = True
        event.accept()

    def showPreview(self):
        cap = cv2.VideoCapture(self.url)
        start = time.time()
        while cap.isOpened() and not self.stop:
            success, frame = cap.read()
            if time.time() - start > 0.05:
                if success:
                    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                    img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                    self.ui.Camera1.setPixmap(QPixmap.fromImage(img))
                start = time.time()
        cap.release()
