from PyQt5 import QtWidgets, QtCore

from lib.GestureParser import GestureParser, ScaleMode


class ConverterWidget(QtWidgets.QWidget):
    add_gesture_signal = QtCore.pyqtSignal(str)

    def __init__(self, name, path, parent=None):
        super(ConverterWidget, self).__init__(parent)

        self.path = path
        self.name = name

        self.label = QtWidgets.QLabel(self.name, self)
        self.line_edit = QtWidgets.QLineEdit(self)
        self.line_edit.setPlaceholderText("Gesture Name")
        self.parse_button = QtWidgets.QPushButton("Convert to image", self)

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.parse_button)

        @QtCore.pyqtSlot()
        def on_click():
            gesture_name = self.line_edit.text()
            if gesture_name:
                self.add_gesture_signal.emit(gesture_name)
                self.convert_point_list(gesture_name)

        self.parse_button.clicked.connect(on_click)

    def convert_point_list(self, gesture_name):
        print("clicked")
        _gesture_parser = GestureParser(SCALE_MODE=ScaleMode.NO_SCALE, IMAGE_DIMENSION=32)
        # _gesture_parser.convert_point_list_to_image()
