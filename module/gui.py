from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

from mainWin import Ui_MainWindow
import module.logic as logic

class MainWin(QMainWindow,Ui_MainWindow):
    def __init__(self,interval=10):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.interval=interval
        self.initWindow()

    def initWindow(self):
        #TODO 설정에서 지정된 기능만 실행하도록 추가예정
        #일단은 전부 실행하도록함

        self.isActivate=[False,False,False]

        for i in range(3):
            self.deactivate(i)

        func=lambda: self.BTNClicked(0)
        self.csBTN.clicked.connect(func)

        func=lambda: self.BTNClicked(1)
        self.gnuBTN.clicked.connect(func)

        func=lambda: self.BTNClicked(2)
        self.agencyBTN.clicked.connect(func)

    def run(self,interval=10):
        self.activate(0)
        logic.run('cs')

    def BTNClicked(self, whichOne=None):
        if whichOne==None:
            print("ClickError: No Target")
            return

        if self.isActivate[whichOne]==True:
            self.deactivate(whichOne)

        else:
            self.activate(whichOne)


    def activate(self,whichOne=None):
        if whichOne==None:
            #TODO 테스트코드
            print("ActivateError: No Target")
            return

        elif whichOne==0:
            ##CS
            self.csBTN.setText("중지")
            self.csStatus.setText("활성화됨")
        elif whichOne==1:
            #GNU
            self.gnuBTN.setText("중지")
            self.gnuStatus.setText("활성화됨")
        else:
            #Agency
            self.agencyBTN.setText("중지")
            self.agencyStatus.setText('활성화됨')

        self.isActivate[whichOne] = True

    def deactivate(self,whichOne=None):
        if whichOne==None:
            #TODO 테스트코드
            print("DeactivateError: No Target")
            return

        elif whichOne == 0:
            ##CS
            self.csBTN.setText("실행")
            self.csStatus.setText("대기")

        elif whichOne == 1:
            # GNU
            self.gnuBTN.setText("실행")
            self.gnuStatus.setText("대기")

        else:
            # Agency
            self.agencyBTN.setText("실행")
            self.agencyStatus.setText('대기')

        self.isActivate[whichOne] = False

if __name__=='__main__':
    app=QApplication(sys.argv)
    MainWindow=MainWin()
    MainWindow.show()
    sys.exit(app.exec_())