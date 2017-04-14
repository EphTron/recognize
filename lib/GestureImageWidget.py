import os
from PyQt5 import QtWidgets, QtGui, QtCore

from lib.GestureCreationDialog import GestureCreationDialog


class GestureImageWidget(QtWidgets.QWidget):
    def __init__(self, gesture_name, image_id, parent=None):
        super(GestureImageWidget, self).__init__(parent)
        self.gesture_name = gesture_name
        self.image_id = image_id

        self.layout = QtWidgets.QVBoxLayout(self)

        self.label = QtWidgets.QLabel(self.gesture_name, self)
        self.layout.addWidget(self.label)

        self.image_label = QtWidgets.QLabel(self)
        self.path = 'gestures/' + self.gesture_name + '/' \
                    + self.gesture_name + '_' + str(self.image_id) + '.jpeg'
        if os.path.exists(self.path):
            self.pixmap = QtGui.QPixmap(self.path)
            self.pixmap = self.pixmap.scaled(100, 100)
            self.image_label.setPixmap(self.pixmap)
        self.layout.addWidget(self.image_label)

        self.button_layout = QtWidgets.QHBoxLayout()

        self.edit_button = QtWidgets.QPushButton("Edit", self)
        self.button_layout.addWidget(self.edit_button)

        @QtCore.pyqtSlot()
        def on_click_edit():
            print("edit")
            creation_dialog = GestureCreationDialog(self.gesture_name, self.image_id, self)
            creation_dialog.exec_()
        self.edit_button.clicked.connect(on_click_edit)

        self.remove_button = QtWidgets.QPushButton("Delete", self)
        self.button_layout.addWidget(self.remove_button)
        self.remove_button.clicked.connect(self.remove_gesture)

        self.layout.addLayout(self.button_layout)
        self.box = QtWidgets.QGroupBox(self.gesture_name + "_" + str(self.image_id), self)
        self.box.setLayout(self.layout)
        self.setMinimumSize(140, 140)

    def remove_gesture(self):
        print("remove", self.path)