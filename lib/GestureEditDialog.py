import os

from PyQt5 import QtCore, QtWidgets
from .GestureCreationWidget import GestureCreationWidget
from .GestureImageWidget import GestureImageWidget


class GestureEditDialog(QtWidgets.QDialog):
    new_image_signal = QtCore.pyqtSignal()

    def __init__(self, gesture_name, image_count, parent=None):
        super(GestureEditDialog, self).__init__(parent)

        self.gesture_name = gesture_name
        self.image_count = image_count
        _image_positions = [(i, j) for i in range(6) for j in range(self.image_count//(6-1))]
        print(_image_positions)
        self.image_widgets = []
        self.layout = QtWidgets.QVBoxLayout(self)

        self.grid_layout = QtWidgets.QGridLayout()
        _count = 0
        for idx, image in enumerate(os.listdir("gestures/"+self.gesture_name)):
            if image.endswith(".jpeg"):
                _image_widget = GestureImageWidget(self.gesture_name, _count)
                self.image_widgets.append(_image_widget)
                self.grid_layout.addWidget(_image_widget,
                                        *_image_positions[idx])
                _count += 1

        hbox = QtWidgets.QHBoxLayout()
        self.exit_button = QtWidgets.QPushButton("Exit")
        hbox.addWidget(self.exit_button)

        self.grid_box = QtWidgets.QGroupBox("All Gestures Images", self)
        self.grid_box.setLayout(self.grid_layout)

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidget(self.grid_box)
        self.scroll.setWidgetResizable(True)

        self.layout.addWidget(self.scroll)
        self.layout.addLayout(hbox)
        self.setLayout(self.layout)
        self.resize(1000,900)


        @QtCore.pyqtSlot()
        def close():
            self.close()

        self.exit_button.clicked.connect(close)


