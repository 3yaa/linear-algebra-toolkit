from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(100, 100, 1280, 1080)


def main():
    print("the begin")


if __name__ == "__main__":
    main()