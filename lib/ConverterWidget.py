from PyQt5 import QtWidgets

from lib.GestureParser import GestureParser, ScaleMode


class ConverterWidget(QtWidgets.QWidget):
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

        self.parse_button.clicked.connect(self.parse2image)

    def parse2image(self):
        print("clicked")
        _gesture_parser = GestureParser(SCALE_MODE=ScaleMode.NO_SCALE, IMAGE_DIMENSION=32)
        # _gesture_parser.convert_point_list_to_image()
