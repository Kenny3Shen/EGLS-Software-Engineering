from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QFileDialog, QMessageBox
from graph_ui import Ui_Form
import numpy as np
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from EGLS_Backend.backend import MySQL

matplotlib.use("Qt5Agg")  # 声明使用QT5


class MyFigureCanvas(FigureCanvas):
    '''
    通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键
    '''

    def __init__(self, parent=None, width=10, height=5, xlim=(0, 2500), ylim=(-2, 2), dpi=100):
        # 创建一个Figure
        fig = plt.Figure(figsize=(width, height), dpi=dpi, tight_layout=True)  # tight_layout: 用于去除画图时两边的空白

        FigureCanvas.__init__(self, fig)  # 初始化父类
        self.setParent(parent)

        self.axes = fig.add_subplot(111)  # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        self.axes.spines['top'].set_visible(False)  # 去掉上面的横线
        self.axes.spines['right'].set_visible(True)
        self.axes.set_xlim(xlim)
        self.axes.set_ylim(ylim)
        self.axes.set_facecolor('#535353')


class Analysis(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.user = user
        # 初始化 gv_visual_data 的显示
        self.gv_visual_data_content = MyFigureCanvas(width=self.ui.graphicsView.width() / 101,
                                                     height=self.ui.graphicsView.height() / 101,
                                                     xlim=(-1, 5),
                                                     ylim=(0, 40))  # 实例化一个FigureCanvas
        self.analysis()

        # self.ui.btn_sin.clicked.connect(self.plot_sin)

    def analysis(self):
        names = ['DouYu', 'BiliBili', 'AcFun', 'HuYa', 'KuaiShou']
        values = [0] * 5
        sql = f"SELECT platform FROM {self.user}"
        con = MySQL(database='User', sql=sql)
        con.exe()
        data = con.getData()
        for i in range(5):
            values[i] = data.count((i,))

        self.gv_visual_data_content.axes.bar(names, values)
        self.gv_visual_data_content.axes.set_title('Analysis', fontsize=15, color='#00aaff')
        self.gv_visual_data_content.axes.set_xlabel('Platform', fontsize=12, color='#00aaff')
        self.gv_visual_data_content.axes.set_ylabel('Count', fontsize=14, color='#00aaff')
        self.gv_visual_data_content.axes.set_facecolor('#535353')
        for a, b in zip(names, values):
            self.gv_visual_data_content.axes.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
        # 加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        self.graphic_scene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.graphic_scene.addWidget(
            self.gv_visual_data_content)  # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        self.ui.graphicsView.setScene(self.graphic_scene)  # 把QGraphicsScene放入QGraphicsView
        self.ui.graphicsView.show()  # 调用show方法呈现图形

    def plot_sin(self):
        x = np.arange(0, 2 * np.pi, np.pi / 100)
        y = np.sin(x)
        self.gv_visual_data_content.axes.clear()  # 由于图片需要反复绘制，所以每次绘制前清空，然后绘图
        self.gv_visual_data_content.axes.plot(x, y)
        self.gv_visual_data_content.axes.set_title('sin()')
        self.gv_visual_data_content.draw()  # 刷新画布显示图片，否则不刷新显示


if __name__ == "__main__":
    app = QApplication([])
    win = Analysis("shen_ss")
    win.show()
    app.exec_()
