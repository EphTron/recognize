#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

from PyQt5 import QtWidgets
from lib.GestureViewWidget import GestureViewWidget
from lib.GestureAddWidget import GestureAddWidget
from lib.ConverterWidget import ConverterWidget


class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        """
        Main widget that holds the different views on our symbols
        Additionally it offers the option to add a new symbol
        :param parent:
        """
        super(MainWidget, self).__init__(parent)

        self.gestures = []
        for file in os.listdir("gestures/"):
            self.gestures.append(file)

        self.gesture_views = []

        self.symbol_adder = GestureAddWidget(self)
        self.symbol_adder.add_gesture_signal.connect(self.add_gesture)

        self.vbox = QtWidgets.QVBoxLayout(self)
        self.vbox.addWidget(self.symbol_adder)

        self.gestures_box = QtWidgets.QGroupBox("Known Gestures:", self)
        _v_layout = QtWidgets.QVBoxLayout(self.gestures_box)
        # list all existing gestures
        for gesture in self.gestures:
            _gesture_view = GestureViewWidget(gesture, self)
            _v_layout.addWidget(_gesture_view)
            self.gesture_views.append(_gesture_view)
        self.gestures_box.setLayout(_v_layout)
        self.vbox.addWidget(self.gestures_box)

        self.capturings_box = QtWidgets.QGroupBox("Captured Point-Lists:", self)
        _v_layout = QtWidgets.QVBoxLayout(self.capturings_box)
        # list all point_lists captured in our vr application
        for file in os.listdir("gesture_point_lists/"):
            if file.endswith(".gpl"):
                _parser_widget = ConverterWidget(file, self)
                _v_layout.addWidget(_parser_widget)
                print(os.path.join("gesture_point_lists/", file))
        self.capturings_box.setLayout(_v_layout)
        self.vbox.addWidget(self.capturings_box)

        self.box = QtWidgets.QGroupBox('Gesture Panel:', self)
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
    mw.resize(600,800)
    mw.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
