#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui

from SymbolWriterWidget import WriterWidget

__author__ = "ephtron"

class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        writer_widget = WriterWidget(self)
        writer_widget.clearImage()

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(writer_widget)

        box = QtWidgets.QGroupBox()
        box.setLayout(vbox)



        scroll = QtWidgets.QScrollArea()
        scroll.setWidget(box)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(600)
        scroll.setFixedWidth(400)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(scroll)


def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = QtWidgets.QMainWindow()
    mw.setWindowTitle("Recognize")
    w = MainWidget(parent=mw)
    mw.setCentralWidget(w)
    mw.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
