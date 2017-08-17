import sys
from PyQt5.QtWidgets import QApplication


from module.gui import MainWin

def main():
    app=QApplication(sys.argv)
    MainWindow=MainWin()
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
