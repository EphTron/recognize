#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets
from lib.GestureViewWidget import GestureViewWidget
from lib.GestureAddWidget import GestureAddWidget


class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """
        Main widget that holds the different views on our symbols
        Additionally it offers the option to add a new symbol
        :param parent:
        """
        super(MainWidget, self).__init__(parent)

        # create symbols that can be used
        self.gestures = ['o', "x", "v"]
        self.gesture_views = []

        self.symbol_adder = GestureAddWidget(self)
        self.symbol_adder.add_gesture_signal.connect(self.add_gesture)

        self.vbox = QtWidgets.QVBoxLayout(self)
        self.vbox.addWidget(self.symbol_adder)

        for gesture in self.gestures:
            _gesture_view = GestureViewWidget(gesture, self)
            self.vbox.addWidget(_gesture_view)
            self.gesture_views.append(_gesture_view)

        self.box = QtWidgets.QGroupBox('All gestures:', self)
        self.box.setLayout(self.vbox)

        self.scroll = QtWidgets.QScrollArea(self)
        self.scroll.setWidget(self.box)
        self.scroll.setWidgetResizable(True)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.scroll)

    def add_gesture(self, value):
        if value not in self.symbols:
            self.symbols.append(value)
            _gesture_view = GestureViewWidget(value, self)
            self.vbox.addWidget(_gesture_view)
            self.gesture_views.append(_gesture_view)


def main():
    app = QtWidgets.QApplication([])
    mw = QtWidgets.QMainWindow()
    mw.setWindowTitle("Recog - Nice")
    w = MainWidget(parent=mw)
    mw.setCentralWidget(w)
    mw.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
