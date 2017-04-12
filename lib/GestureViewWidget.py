import os
from PyQt5 import QtWidgets, QtGui, QtCore

from .GestureEditDialog import GestureEditDialog
from .GestureCreationDialog import GestureCreationDialog


class GestureViewWidget(QtWidgets.QWidget):
    def __init__(self, gesture_name, parent=None):
        super(GestureViewWidget, self).__init__(parent)

        self.gesture_name = gesture_name
        self.image_count = len([name for name in os.listdir('gestures/'+self.gesture_name) if name.endswith(".jpeg")])
        print(self.gesture_name + " with " + str(self.image_count) + " images")

        self.gesture_creation_dialog = GestureCreationDialog(self.gesture_name, self.image_count, self)
        self.gesture_creation_dialog.new_image_signal.connect(self.update_gesture)

        self.label = QtWidgets.QLabel("Gesture " + self.gesture_name)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.label)

        self.image_label = QtWidgets.QLabel(self)
        self.path = 'gestures/' + self.gesture_name + '/' \
                    + self.gesture_name + '_0.jpeg'

        if os.path.exists(self.path):
            self.pixmap = QtGui.QPixmap(self.path)
            self.pixmap = self.pixmap.scaled(64, 64)
            self.image_label.setPixmap(self.pixmap)
        self.layout.addWidget(self.image_label)

        self.button_layout = QtWidgets.QVBoxLayout()

        self.edit_button = QtWidgets.QPushButton("Edit Gesture Images", self)
        self.button_layout.addWidget(self.edit_button)

        self.add_button = QtWidgets.QPushButton("Add Gesture Image", self)
        self.button_layout.addWidget(self.add_button)

        self.layout.addLayout(self.button_layout)

        @QtCore.pyqtSlot()
        def on_click_edit():
            gesture_edit_dialog = GestureEditDialog(self.gesture_name, self.image_count, self)
            gesture_edit_dialog.exec_()

        self.edit_button.clicked.connect(on_click_edit)

        @QtCore.pyqtSlot()
        def on_click_creation():
            self.gesture_creation_dialog.exec_()

        self.add_button.clicked.connect(on_click_creation)

        self.setLayout(self.layout)

    def update_gesture(self):
        self.image_count = len([name for name in os.listdir('gestures/'+self.gesture_name) if name.endswith(".jpeg")])
        self.gesture_creation_dialog.set_gesture_image_id(self.image_count)
        print(self.gesture_name + " updated. Now has " + str(self.image_count) + " images")

        if os.path.exists(self.path):
            self.pixmap = QtGui.QPixmap(self.path)
            self.pixmap = self.pixmap.scaled(64, 64)
            self.image_label.setPixmap(self.pixmap)
