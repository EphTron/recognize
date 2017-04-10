from PyQt5 import QtWidgets, QtCore


class GestureAddWidget(QtWidgets.QWidget):
    add_gesture_signal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(GestureAddWidget, self).__init__(parent)

        self.label = QtWidgets.QLabel("Enter a new gesture name", self)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.label)

        self.line_edit = QtWidgets.QLineEdit(self)
        self.add_button = QtWidgets.QPushButton("Add new gesture symbol", self)
        self.layout.addWidget(self.add_button)

        @QtCore.pyqtSlot()
        def on_click():
            text = self.line_edit.text()
            if text:
                self.add_gesture_signal.emit(text)

        self.add_button.clicked.connect(on_click)
