from PySide2.QtWidgets import QWidget, QMessageBox
from about_ui import Ui_Form


class About(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.label_3.setOpenExternalLinks(True)
