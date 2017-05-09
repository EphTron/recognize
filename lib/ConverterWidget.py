import os
from PyQt5 import QtWidgets, QtCore, QtGui
import PIL.Image

from lib.GestureParser import GestureParser, ScaleMode
from lib.GestureCreationDialog import  GestureCreationDialog

import matplotlib.pyplot as plt
import numpy as np


class ConverterWidget(QtWidgets.QWidget):
    add_gesture_signal = QtCore.pyqtSignal(str)

    def __init__(self, name, path, parent=None):
        super(ConverterWidget, self).__init__(parent)

        self.name = name
        self.path = path

        self.label = QtWidgets.QLabel(self.name, self)
        self.image_label = QtWidgets.QLabel(self)
        self.pixmap = QtGui.QPixmap()
        self.line_edit = QtWidgets.QLineEdit(self)
        self.line_edit.setPlaceholderText("Gesture Name")
        self.parse_button = QtWidgets.QPushButton("Convert to image", self)

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.parse_button)
        self.layout.addWidget(self.image_label)

        @QtCore.pyqtSlot()
        def on_click():
            gesture_name = self.line_edit.text()
            if gesture_name:
                self.add_gesture_signal.emit(gesture_name)
                _img = self.convert_point_list_to_qimage(gesture_name)
                gesture_creation_dialog = GestureCreationDialog(gesture_name, 100, self)

                self.pixmap = QtGui.QPixmap(_img)
                self.pixmap = self.pixmap.scaled(124, 124)
                self.image_label.setPixmap(self.pixmap)
                # gesture_creation_dialog.load_image(_img)
                # gesture_creation_dialog.exec_()
                print("jauuuu")

        self.parse_button.clicked.connect(on_click)

    def convert_point_list_to_qimage(self, gesture_name):

        self.add_gesture_signal.emit(gesture_name)

        print("clicked")
        _gp = GestureParser(SCALE_MODE=ScaleMode.NO_SCALE, IMAGE_DIMENSION=32)
        _point_list = _gp.convert_gpl_to_pointlist(self.path, self.name)
        _image_array = _gp.convert_point_list_to_scaled_image_array(_point_list)
        # _path = QtCore.QDir.currentPath() \
        #            + '/gestures/' \
        #            + gesture_name \
        #            + '/'
        #_gp.save_array_as_image(_image_array, _path, gesture_name)

        print("dtype: ",_image_array.dtype)
        print("strides", _image_array.strides[0])
        im = _image_array
        gray_color_table = [QtGui.qRgb(i, i, i) for i in range(256)]

        qim = QtGui.QImage(im.data, im.shape[0], im.shape[1], im.strides[0], QtGui.QImage.Format_Indexed8)
        qim.setColorTable(gray_color_table)

        return qim

        # plt.figure(1)
        # plt.imshow(_image_array)
        # plt.show()

        #height, width = _image_array.shape
        #bgra = np.zeros([height, width, 4], dtype=np.uint8)
        #bgra[:, :, 0:3] = _image_array
        #return QtGui.QImage(bgra.data, width, height, QtGui.QImage.Format_RGB32)
        # _image = QtGui.QImage(_image_array, _image_array.shape[0], _image_array.shape[1], QtGui.QImage.Format_RGB888)
        # QtGui.QImage.Format_Grayscale8
        # print(_image, _image_array.shape)
        # return _image



