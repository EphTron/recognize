from PyQt5 import QtWidgets, QtGui, QtCore

from GestureCreationDialog import GestureCreationDialog


class GestureViewWidget(QtWidgets.QWidget):
    def __init__(self, gesture, parent=None):
        super(GestureViewWidget, self).__init__(parent)

        self.gesture = gesture
        self.writer_dialog = GestureCreationDialog(self.gesture, self)

        self.label = QtWidgets.QLabel("Gesture " + self.gesture)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.label)

        self.image_label = QtWidgets.QLabel(self)

        if self.gesture == " ":
            self.pixmap = QtGui.QPixmap('gesture/symbols/' + "space" + '.png')
        else:
            self.pixmap = QtGui.QPixmap('gesture/symbols/' + self.gesture + '.png')

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
        print("new image foo")
        if self.gesture == " ":
            self.pixmap = QtGui.QPixmap('gesture/symbols/' + "space" + '.png')
        else:
            self.pixmap = QtGui.QPixmap('gesture/symbols/' + self.gesture + '.png')
        self.image_label.setPixmap(self.pixmap)
