from PySide2.QtCore import QObject, Signal


class MySignal(QObject):
    progress_update = Signal(int)
    trueLink_update = Signal(str)
    danmu_update = Signal(str)
    itemsStatus = Signal(int, str, bool)
    trueLinkAppend = Signal(str)
