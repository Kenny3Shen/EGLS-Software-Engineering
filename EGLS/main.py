import os
import re
import webbrowser
from threading import Thread

from PySide2.QtCore import QFile, QSettings
from PySide2.QtGui import QIcon, QCursor
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMessageBox, QInputDialog, QLineEdit, QMenu

from DanMu import DanMu
import Login
import MySignal
# import PreviewLive
from EGLS_Backend.backend import MySQL
from link import DouYuLink, AcFunLink, BiliBiliLink, HuYaLink, DouYinLink, KuaiShouLink
from shared_ptr import SP


class MainWindow:
    def __init__(self):
        ui_file = QFile('ui/main.ui')
        ui_file.open(QFile.ReadOnly)
        ui_file.close()
        self.ui = QUiLoader().load(ui_file)

        # super().__init__()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)

        self.definition = ['Blue-Ray', 'Super', 'High', 'Standard']
        self.HuYa_Channel = ['2000p', 'tx', 'bd', 'migu-bd']
        self.DouYin_Channel = ['rtmp', 'hls']
        self.platform = ['DouYu', 'BiliBili', 'AcFun', 'HuYa', 'DouYin', 'KuaiShou']
        self.LinkList = [self.DouYu, self.BiliBili, self.AcFun, self.HuYa, self.DouYin, self.KuaiShou]
        self.originalURL = ['https://www.douyu.com/', 'https://live.bilibili.com/', 'https://live.acfun.cn/live/',
                            'https://www.huya.com/', 'https://v.douyin.com/', 'https://live.kuaishou.com/u/']
        self.pattern = r'^(.*?)\([a-z]{2,3}line\)$'
        self.URL_List = []
        self.__initIniSettting()

        self.rid, self.quality, self.pf_index = '', 0, 0
        self.openingFavorites = False  # 不能同时多次打开收藏夹
        self.MySignal = MySignal.MySignal()
        self.user = 'None'
        self.__isKeepLogin()
        self.__setSlot()
        self.__createContextMenu()

    def __initIniSettting(self):
        if not os.path.exists('.setting.ini'):
            ini = QSettings(".setting.ini", QSettings.IniFormat)
            ini.setIniCodec('uft-8')
            ini.setValue('Account/Username', 'None')
            ini.setValue('Account/Password', '')
            ini.setValue('Kuaishou_cookies/KS_Cookies', 'did=web_e9f23e35be2c6eefde872a9296d7a4fa')
            ini.setValue('DouyuLinkMethod/Method', '0')
            self.ui.actionThird_party_API.toggle()
        else:
            ini = QSettings(".setting.ini", QSettings.IniFormat)
            ini.setIniCodec('uft-8')
            getMethod = ini.value('DouyuLinkMethod/Method')
            if getMethod == '0':
                self.ui.actionThird_party_API.toggle()
            else:
                self.ui.actionOriginal_API.toggle()

    def __isKeepLogin(self):
        ini = QSettings(".setting.ini", QSettings.IniFormat)
        user = ini.value('Account/Username')
        if user != 'None' and user is not None:
            con = MySQL(database='User', sql=f"SELECT Title FROM {user}")
            con.exe()
            data = con.getData()
            # con = pymysql.connect(host="localhost", user="root", password="kr20000118", database="UserLink")
            self.user = user
            self.ui.actionSign_in.setText('Sign out')
            self.ui.trueLink.setPlainText(f'Hello, {self.user}!')
            for i in data:
                self.ui.favorites.addItem(i[0])
            Thread(target=self.detect).start()

    def __setSlot(self):
        self.ui.actionSign_in.triggered.connect(self.signHandler)
        self.ui.actionReadMe.triggered.connect(lambda: self.ui.trueLink.setPlainText(readMe))
        self.ui.actionSet_KuaiShou_Cookie.triggered.connect(self.setKuaiShouCookies)
        self.ui.definite.addItems(self.definition)
        self.ui.platform.addItems(self.platform)
        # self.ui.preview.clicked.connect(self.previewLink)
        self.ui.button.clicked.connect(self.getLink)
        self.ui.roomID.textChanged.connect(self.setRoomID)
        self.ui.roomID.returnPressed.connect(self.getLink)
        self.ui.addAsx.clicked.connect(self.addToFavorites)
        self.ui.potplayer.clicked.connect(self.openWithPotplayer)
        self.ui.myLive.clicked.connect(self.openFavorites)
        self.ui.favorites.itemDoubleClicked.connect(self.doubleClickedFavorites)
        # self.ui.favorites.itemEntered.connect(lambda: self.ui.favorites.currentItem().setToolTip('123'))
        self.ui.platform.currentIndexChanged.connect(self.alterDefinition)
        # self.ui.detect.clicked.connect(self.detectStatus)
        self.MySignal.itemsStatus.connect(self.setItemsText)
        self.MySignal.progress_update.connect(self.setProgressBar)
        self.MySignal.trueLink_update.connect(self.setTrueLink)
        # self.ui.deleteFav.clicked.connect(self.delItem)
        # self.ui.sign.clicked.connect(self.signIn)
        self.ui.actionThird_party_API.triggered.connect(self.__setDouyuMethodByThirdAPI)
        self.ui.actionOriginal_API.triggered.connect(self.__setDouyuMethodByOriginalAPI)

    def __setDouyuMethodByThirdAPI(self):
        self.ui.actionOriginal_API.toggle()
        ini = QSettings(".setting.ini", QSettings.IniFormat)
        ini.setIniCodec('uft-8')
        ini.setValue('DouyuLinkMethod/Method', '0')

    def __setDouyuMethodByOriginalAPI(self):
        self.ui.actionThird_party_API.toggle()
        ini = QSettings(".setting.ini", QSettings.IniFormat)
        ini.setIniCodec('uft-8')
        ini.setValue('DouyuLinkMethod/Method', '1')

    def setItemsText(self, row, status):
        self.ui.favorites.item(row).setText(status)

    def detectStatus(self):
        itemCount = self.ui.favorites.count()
        if itemCount == 0:
            QMessageBox.information(self.ui, 'Notice', 'Empty favorties')
            return
        else:
            if self.openingFavorites:
                QMessageBox.warning(self.ui, 'Warning', 'Task in progress, please wait for completion')
                return
            self.openingFavorites = True
            Thread(target=self.detect).start()
            self.openingFavorites = False

    def detect(self):
        # con = pymysql.connect(host="localhost", user="root", password="kr20000118", database="UserLink")
        con = MySQL(database='User', sql=f"SELECT * FROM {self.user}")
        con.exe()
        data = con.getData()
        row = 0
        for i in data:
            thread = Thread(target=self.detechItemStatus, args=(row, i))
            row += 1
            thread.setDaemon(True)
            thread.start()

    def detechItemStatus(self, row, info, append_list=False):
        title, self.pf_index, self.rid, self.quality, ID = info
        url = self.getURL(emit=False)
        if 'http://' not in url and 'https://' not in url:
            self.MySignal.itemsStatus.emit(row, f"{title}(offline)")
        else:
            self.MySignal.itemsStatus.emit(row, f"{title}(online)")
        if append_list:
            self.URL_List.append((title, url, ID))

    def __createContextMenu(self):
        # 创建右键菜单
        # 必须将ContextMenuPolicy设置为Qt.CustomContextMenu
        # 否则无法使用customContextMenuRequested信号
        self.ui.favorites.customContextMenuRequested.connect(self.__showFavoritesMenu)
        self.ui.trueLink.customContextMenuRequested.connect(self.__showTextBrowserMenu)

        # Create FavoritesMenu
        self.FavoritesMenu = QMenu(self.ui.favorites)
        self.action_openItem = self.FavoritesMenu.addAction('Open')
        self.action_getDanmu = self.FavoritesMenu.addAction('Get DanMu')
        self.action_getOriginURL = self.FavoritesMenu.addAction('Open Original Room')
        self.action_delItem = self.FavoritesMenu.addAction('Delete')
        self.action_refresh = self.FavoritesMenu.addAction('Refresh')
        self.action_rename = self.FavoritesMenu.addAction('Rename')
        # Associate actions with processing functions by trigger
        self.action_openItem.triggered.connect(self.doubleClickedFavorites)
        self.action_getDanmu.triggered.connect(self.showDanmuWindow)
        self.action_getOriginURL.triggered.connect(self.getOriginURL)
        self.action_delItem.triggered.connect(self.delItem)
        self.action_refresh.triggered.connect(self.detectStatus)
        self.action_rename.triggered.connect(self.renameItem)
        # 创建TextBrowserMenu
        self.TextMenu = QMenu(self.ui.trueLink)
        self.action_copyLink = self.TextMenu.addAction('Copy')
        # self.action_previewLink = self.TextMenu.addAction('Preview')
        self.action_openLink = self.TextMenu.addAction('Open')
        # 将动作与处理函数相关联
        self.action_copyLink.triggered.connect(self.copyLink)
        # self.action_previewLink.triggered.connect(self.previewLink)
        self.action_openLink.triggered.connect(self.openWithPotplayer)

    def __showTextBrowserMenu(self):
        self.TextMenu.move(QCursor().pos())
        self.TextMenu.show()

    def __showFavoritesMenu(self):
        # 右键点击时调用的函数
        # 菜单显示前，将它移动到鼠标点击的位置
        self.FavoritesMenu.move(QCursor().pos())
        self.FavoritesMenu.show()

    def renameItem(self):
        def renmae(new, old):
            c = MySQL(database='User',
                      sql=f"UPDATE {self.user} SET Title = '{new}' WHERE title = '{old}'")
            c.exe()
            url = self.getURL(emit=False)
            if 'http://' in url or 'https://' in url:
                new = f"{new}(online)"
            else:
                new = f"{new}(offline)"
            self.MySignal.itemsStatus.emit(self.ui.favorites.currentRow(), new)

        # 一个可用于提取直播连接并将其收藏的软件
        oldTitle = re.findall(self.pattern, self.ui.favorites.currentItem().text())[0]
        while True:
            newTitle, submit = QInputDialog.getText(self.ui, "Input new title", "title:", QLineEdit.Normal, "")
            newTitle.strip()
            if not submit:
                break
            else:
                if newTitle == oldTitle:
                    break
                if newTitle == '':
                    QMessageBox.critical(self.ui, 'ERROR', 'Input must be not empty!')
                    continue
                if len(newTitle) > 32:
                    QMessageBox.critical(self.ui, 'ERROR', 'Title too long')
                    continue
                # con = pymysql.connect(host="localhost", user="root", password="kr20000118", database='UserLink')
                existedTitle = f"SELECT Title FROM {self.user} WHERE Title = '{newTitle}'"
                con = MySQL(database='User', sql=existedTitle)
                con.exe()
                if len(con.getData()) > 0:  # 重复标题名
                    QMessageBox.critical(self.ui, 'ERROR', 'Title existed!')
                else:
                    Thread(target=renmae, args=(newTitle, oldTitle)).start()
                    break

    def getOriginURL(self):
        try:
            OringinalUrl = self.getItemInformation()[0]
        except TypeError:
            QMessageBox.critical(self.ui, 'Warning', 'Invalid operation')
            return
        # self.ui.trueLink.setOpenExternalLinks(True)
        # self.ui.trueLink.append(f"<a href='{OringinalUrl}'>{OringinalUrl}</a>")
        self.MySignal.trueLink_update.emit(OringinalUrl)
        webbrowser.open(OringinalUrl)

    def getItemInformation(self):
        try:
            title = self.ui.favorites.currentItem().text()
            title = re.findall(self.pattern, title)[0]
        except AttributeError:
            return
        # con = pymysql.connect(host="localhost", user="root", password="kr20000118", database='UserLink')
        titleData = f"SELECT {self.user}.Platform,{self.user}.RoomId FROM {self.user} " \
                    f"WHERE {self.user}.Title = '{title}'"
        con = MySQL(database='User', sql=titleData)
        con.exe()
        data = con.getData()
        pf_Index, rid = data[0]
        url = f'{self.originalURL[pf_Index]}{rid}'
        return url, pf_Index, rid

    def showDanmuWindow(self):
        roomInformation = self.getItemInformation()
        if not roomInformation:
            QMessageBox.critical(self.ui, 'Warning', 'Invalid Operation')
            return
        if roomInformation[1] == 4 or roomInformation[1] == 5:
            QMessageBox.warning(self.ui, 'Warning', 'Not support this platform')
            return
        SP.danmuWindow = DanMu(roomInformation[0], self.platform[roomInformation[1]], roomInformation[2])
        SP.danmuWindow.show()

    # def previewLink(self):
    #     url = self.ui.trueLink.toPlainText()
    #     if 'http://' not in url and 'https://' not in url:
    #         QMessageBox.warning(self.ui, 'ERROR', 'Illegal URL!')
    #         return
    #
    #     SP.previewWindow = PreviewLive.Preview(url)
    #     SP.previewWindow.show()

    def setTrueLink(self, link):
        self.ui.trueLink.setPlainText(link)

    def setRoomID(self):
        self.rid = self.ui.roomID.text()

    def setPlatform(self):
        self.pf_index = self.ui.platform.currentIndex()

    def setProgressBar(self, value):
        self.ui.progressBar.setValue(value)

    def setKuaiShouCookies(self):
        cookie, okPressed = QInputDialog.getText(self.ui, "Input your cookie", "Cookie:", QLineEdit.Normal, "")
        if not okPressed:
            pass
        else:
            ini = QSettings(".setting.ini", QSettings.IniFormat)
            ini.setIniCodec('uft-8')
            ini.setValue('Kuaishou_cookies/KS_Cookies', cookie)

    def setQuality(self):
        self.quality = self.ui.definite.currentIndex()

    def alterDefinition(self):
        self.ui.definite.clear()
        cur_pf_index = self.ui.platform.currentIndex()
        if cur_pf_index in [0, 1, 2, 5]:
            self.ui.definite.addItems(self.definition)
        elif cur_pf_index == 3:
            self.ui.definite.addItems(self.HuYa_Channel)
        elif cur_pf_index == 4:
            self.ui.definite.addItems(self.DouYin_Channel)

    def getURL(self, emit=True):
        res = self.LinkList[self.pf_index]()
        # if self.pf_index == 0:
        #     res = self.DouYu()
        #     # self.ui.trueLink.setPlainText(self.DouYu())
        # elif self.pf_index == 1:
        #     res = self.BiliBili()
        #     # thread = MyThread(target=self.BiliBili)
        # elif self.pf_index == 2:
        #     res = self.AcFun()
        #     # thread = MyThread(target=self.AcFun)
        # elif self.pf_index == 3:
        #     res = self.HuYa()
        #     # thread = MyThread(target=self.HuYa)
        # elif self.pf_index == 4:
        #     res = self.DouYin()
        #     # thread = MyThread(target=self.DouYin)
        # elif self.pf_index == 5:
        #     res = self.KuaiShou()
        #     # = MyThread(target=self.KuaiShou)
        # thread.start()
        # thread.join()
        # res = thread.get_result()
        if emit:
            self.MySignal.trueLink_update.emit(res)
        return res

    def signHandler(self):
        def clearFavorites():
            for _ in range(self.ui.favorites.count()):
                self.ui.favorites.takeItem(0)

        if self.user == 'None':
            SP.loginWindow = Login.Login()
            SP.loginWindow.ui.show()
        else:
            if QMessageBox.question(self.ui, 'Confirm', f'Are you sure you want to sign out?') == QMessageBox.Yes:
                self.user = 'None'
                self.ui.actionSign_in.setText('Sign in')
                self.ui.trueLink.setPlainText("")
                self.ui.progressBar.setValue(0)
                thread = Thread(target=clearFavorites)
                thread.start()
                # url = 'http://127.0.0.1/api/sign'
                # requests.Session().post(url, json={
                #     'action': 'signout',
                # })

    def doubleClickedFavorites(self):
        Thread(target=self.openItem).start()

    def openItem(self):
        title = self.ui.favorites.currentItem().text()
        try:
            title = re.findall(self.pattern, title)[0]
        except IndexError:
            self.MySignal.trueLink_update.emit(f"{title}:Remote end closed connection without response")
        # con = pymysql.connect(host="localhost", user="root", password="kr20000118", database='UserLink')
        # cursor = con.cursor()
        # cursor.execute(f"SELECT * FROM {self.user} WHERE {self.user}.Title = '{title}'")
        # data = cursor.fetchone()
        # cursor.close()
        # con.close()
        con = MySQL(database='User', sql=f"SELECT * FROM {self.user} WHERE {self.user}.Title = '{title}'")
        con.exe()
        data = con.getData()
        _, self.pf_index, self.rid, self.quality, __ = data[0]
        url = self.getURL()
        if 'http://' in url or 'https://' in url:
            self.MySignal.itemsStatus.emit(self.ui.favorites.currentRow(), f"{title}(online)")
            with open('TemporaryFile.asx', 'w') as f:
                f.write('<asx version = "3.0" >')
                f.write(f'<entry><title>{title}</title><ref href = "{url}"/></entry>')
            os.startfile('TemporaryFile.asx')
            #  self.progressSignal.trueLink_update.emit(f"Opening \"{title}\"")
        else:
            self.MySignal.itemsStatus.emit(self.ui.favorites.currentRow(), f"{title}(offline)")
            self.MySignal.trueLink_update.emit(f"\"{title}\" is offline({url})")

    def delItem(self):
        try:
            title = self.ui.favorites.currentItem().text()
            title = re.findall(self.pattern, title)[0]
        except AttributeError:
            QMessageBox.critical(self.ui, 'Warning', 'Invalid operation')
            return
        else:
            if QMessageBox.question(self.ui, 'Confirm',
                                    f'Are you sure you want to delete "{title}"?') == QMessageBox.Yes:
                self.ui.favorites.takeItem(self.ui.favorites.currentRow())
                thread = Thread(target=self.takeItemFromDB, args=(title,))
                thread.start()

    def takeItemFromDB(self, t):
        con = MySQL(database='User', sql=f"DELETE FROM {self.user} WHERE Title = '{t}'")
        con.exe()

    def addToFavorites(self):
        self.setRoomID()
        self.setPlatform()
        self.setQuality()
        if self.user == 'None':
            choice = QMessageBox.question(self.ui, 'Access deny',
                                          'This function is only available to logged in users.\n '
                                          'Would you want to sign in?')
            if choice == QMessageBox.Yes:
                self.signHandler()
            return
        if self.rid == '':
            QMessageBox.critical(self.ui, 'ERROR', 'Room ID must be not empty!')
            return
        self.ui.addAsx.setEnabled(False)
        while True:
            title, OK = QInputDialog.getText(self.ui, "Entitle", "Title", QLineEdit.Normal,
                                             f"{self.platform[self.pf_index]}"
                                             f"_{self.rid}_{self.ui.definite.currentText()}")
            title = title.strip()
            if OK:
                if title == '':
                    QMessageBox.critical(self.ui, 'ERROR', 'Input must be not empty!')
                    continue
                if len(title) > 32:
                    QMessageBox.critical(self.ui, 'ERROR', 'Title too long')
                    continue
                # con = pymysql.connect(host="localhost", user="root", password="kr20000118", database='UserLink')
                existedTitle = f"SELECT Title FROM {self.user} WHERE Title = '{title}'"
                con = MySQL(database='User', sql=existedTitle)
                con.exe()
                if len(con.getData()) > 0:  # 重复标题名
                    QMessageBox.critical(self.ui, 'ERROR', 'Title existed!')
                else:
                    sql = f"INSERT INTO {self.user}(Title, Platform, RoomId, Definition) " \
                          f"VALUES ('{title}',{self.pf_index}, '{self.rid}', {self.quality})"
                    MySQL(database='User', sql=sql).exe()
                    self.ui.favorites.insertItem(self.ui.favorites.count(), f'{title}')  # 尾插
                    url = self.getURL()
                    if 'http://' in url or 'https://' in url:
                        self.MySignal.itemsStatus.emit(self.ui.favorites.count() - 1, f"{title}(online)")
                    else:
                        self.MySignal.itemsStatus.emit(self.ui.favorites.count() - 1, f"{title}(offline)")
                    # self.ui.favorites.addItem(f'{title}') # 头插
                    break
            else:
                break
        self.ui.addAsx.setEnabled(True)

    # def newFavorites(self, t):
    #     sql = f"INSERT INTO {self.user}(Title, Platform, RoomId, Definition) " \
    #           f"VALUES ('{t}',{self.pf_index}, '{self.rid}', {self.quality})"
    #     self.ui.favorites.insertItem(self.ui.favorites.count(), f'{t}')  # 尾插
    #     # self.ui.favorites.addItem(f'{title}') # 头插

    def openFavorites(self):
        if self.user == 'None':
            QMessageBox.critical(self.ui, 'ERROR', 'Please login first!')
        else:
            itemCount = self.ui.favorites.count()
            if itemCount == 0:
                QMessageBox.warning(self.ui, 'Warning', 'You favorites is empty.')
            else:
                if self.openingFavorites:
                    QMessageBox.warning(self.ui, 'Warning', 'The task is in progress, '
                                                            'please wait for the task to complete.')
                    return
                self.ui.trueLink.setPlainText("Loading your favorites")
                self.ui.progressBar.setRange(0, itemCount * 3)
                Thread(target=self.writeFavorites).start()

    def writeFavorites(self):
        self.openingFavorites = True
        # con = pymysql.connect(host="localhost", user="root", password="kr20000118", database="UserLink")
        con = MySQL(database='User', sql=f"SELECT * FROM {self.user}")
        con.exe()
        data = con.getData()
        self.URL_List.clear()
        threadList = []
        row, count = 0, 0
        for i in data:
            thread = Thread(target=self.detechItemStatus, args=(row, i, True))
            threadList.append(thread)
            row += 1
        for thread in threadList:
            thread.setDaemon(True)
            thread.start()
            self.MySignal.progress_update.emit(count)
            count += 1
        for thread in threadList:
            thread.join()
            self.MySignal.progress_update.emit(count)
            count += 1
        self.URL_List.sort(key=lambda x: x[2])
        if not os.path.exists("MyFavorites"):
            os.mkdir("MyFavorites")
        with open('MyFavorites/MyFavorites.asx', 'w') as f:
            f.write('<asx version = "3.0" >\n')
            for title, url, _ in self.URL_List:
                try:
                    if 'http://' in url or 'https://' in url:
                        self.MySignal.itemsStatus.emit(count % self.ui.favorites.count(), f"{title}(online)")
                        f.write(f'<entry><title>{title}</title><ref href = "{url}"/></entry>\n')
                    else:
                        self.MySignal.itemsStatus.emit(count % self.ui.favorites.count(), f"{title}(offline)")
                except IOError:
                    pass
                count += 1
                self.MySignal.progress_update.emit(count)
        os.startfile(os.path.normpath('MyFavorites/MyFavorites.asx'))
        self.MySignal.trueLink_update.emit('Task completed')
        self.openingFavorites = False

    def getLink(self):
        if self.openingFavorites:
            QMessageBox.warning(self.ui, 'Warning', 'Opening your favorites, please wait for completion.')
            return
        self.setRoomID()
        if self.rid == '':
            QMessageBox.critical(self.ui, 'ERROR', 'Room ID cannot be empty.')
            return
        # self.ui.button.setEnabled(False)
        self.setPlatform()
        self.setQuality()
        Thread(target=self.getURL).start()
        #  self.ui.trueLink.setPlainText(res)
        # self.ui.button.setEnabled(True)

    def copyLink(self):
        self.ui.trueLink.selectAll()
        self.ui.trueLink.copy()

    def openWithPotplayer(self):
        url = self.ui.trueLink.toPlainText()
        if url == '':
            QMessageBox.warning(self.ui, 'ERROR', 'URL cannot be empty!')
            return
        elif 'http://' not in url and 'https://' not in url:
            QMessageBox.warning(self.ui, 'ERROR', 'Illegal URL!')
            return
        else:
            choice = QMessageBox.question(self.ui, 'Confirm', 'Do you want to open thr current URL with PotPlayer?')
            if choice == QMessageBox.Yes:
                with open('TemporaryFile.asx', 'w') as f:
                    f.write('<asx version = "3.0" >')
                    f.write('<entry>'
                            f'<title>{self.platform[self.pf_index]}_{self.rid}_{self.ui.definite.currentText()}</title>'
                            f'<ref href = "{url}"/>'
                            '</entry>')
                os.startfile('TemporaryFile.asx')

    def DouYu(self):
        s = DouYuLink.DouYu(self.rid, self.quality)
        ini = QSettings(".setting.ini", QSettings.IniFormat)
        ini.setIniCodec('uft-8')
        getMethod = ini.value('DouyuLinkMethod/Method')
        if getMethod == '0':
            return s.get_Third_API()
        else:
            return s.get_real_url()

    def BiliBili(self):
        b = BiliBiliLink.BiliBili(self.rid, self.quality)
        return b.get_real_url()

    def AcFun(self):
        a = AcFunLink.AcFun(self.rid, self.quality)
        return a.get_real_url()

    def HuYa(self):
        h = HuYaLink.HuYa(self.rid, self.quality)
        return h.get_real_url()

    def DouYin(self):
        d = DouYinLink.DouYin(self.rid, self.quality)
        return d.get_real_url()

    def KuaiShou(self):
        ini = QSettings(".setting.ini", QSettings.IniFormat)
        ini.setIniCodec('uft-8')
        KS_Cookies = ini.value('Kuaishou_cookies/KS_Cookies')
        k = KuaiShouLink.KuaiShou(self.rid, self.quality, KS_Cookies)
        return k.get_real_url()


if __name__ == '__main__':
    readMe = "0.请先下载PotPlayer（或任意可打开直播链接的播放器）\n" \
             "1.选择直播平台，输入房间号，选择清晰度(线路)，点击Get\n" \
             "2.点击PotPlayer打开直播链接（选择PotPlayer为默认打开方式）\n" \
             "3.虎牙平台无法选择清晰度，可选择4种直播线路\n" \
             "4.抖音平台只有一种清晰度,可选择2种直播线路\n" \
             "5.使用手机上打开抖音直播间后，选择“分享--复制链接”，输入分享链接中最后7个字符串\n" \
             "例如：v.douyin.com/{room_id}/"

    app = QApplication([])
    app.setStyle('Fusion')
    app.setWindowIcon(QIcon('main.ico'))
    SP.mainWindow = MainWindow()
    SP.mainWindow.ui.show()
    app.exec_()
    if os.path.exists('TemporaryFile.asx'):
        os.remove('TemporaryFile.asx')
