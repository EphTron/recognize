from PyQt5 import QtWidgets, QtGui, QtCore

from .GestureCreationDialog import GestureCreationDialog


class GestureViewWidget(QtWidgets.QWidget):
    def __init__(self, gesture_name, parent=None):
        super(GestureViewWidget, self).__init__(parent)

        self.gesture_name = gesture_name
        self.writer_dialog = GestureCreationDialog(self.gesture_name, self)

        self.label = QtWidgets.QLabel("Gesture " + self.gesture_name)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.label)

        self.image_label = QtWidgets.QLabel(self)
        self.pixmap = QtGui.QPixmap('gestures/' + self.gesture_name + '/' + self.gesture_name + '0.jpeg')

        self.image_label.setPixmap(self.pixmap)
        self.layout.addWidget(self.image_label)

        self.edit_button = QtWidgets.QPushButton("Edit", self)
        self.layout.addWidget(self.edit_button)

        @QtCore.pyqtSlot()
        def on_click():
            self.writer_dialog.exec_()

        self.edit_button.clicked.connect(on_click)
        self.writer_dialog.new_image_signal.connect(self.update_gesture)
        self.setLayout(self.layout)

    def update_gesture(self):
        self.pixmap = QtGui.QPixmap('gestures/'
                                    + self.gesture_name
                                    + '/'
                                    + self.gesture_name
                                    + '0.jpeg')
        self.image_label.setPixmap(self.pixmap)
