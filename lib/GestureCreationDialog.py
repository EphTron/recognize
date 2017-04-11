from PyQt5 import QtCore, QtWidgets
from .GestureCreationWidget import GestureCreationWidget


class GestureCreationDialog(QtWidgets.QDialog):
    new_image_signal = QtCore.pyqtSignal()

    def __init__(self, gesture, parent=None):
        super(GestureCreationDialog, self).__init__(parent)

        self.gesture = gesture
        self.initUI()

    def initUI(self):

        hbox = QtWidgets.QHBoxLayout()

        self.save_button = QtWidgets.QPushButton("Save")
        hbox.addWidget(self.save_button)

        self.exit_button = QtWidgets.QPushButton("Exit")
        hbox.addWidget(self.exit_button)

        self.gesture_creator = GestureCreationWidget(self)
        self.gesture_creator.clearImage()

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.gesture_creator)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        @QtCore.pyqtSlot()
        def save():
            file_format = "png"
            self.saveFile(file_format)
        self.save_button.clicked.connect(save)

        @QtCore.pyqtSlot()
        def close():
            self.close()
        self.exit_button.clicked.connect(close)

    def closeEvent(self, event):
        if self.maybeSave():
            event.accept()
        else:
            event.ignore()
        self.emit(QtCore.SIGNAL("new_image"))

    def maybeSave(self):
        if self.gesture_creator.isModified():
            ret = QtWidgets.QMessageBox.warning(self, "Symbol Editor",
                                                "The image has been modified.\n"
                                                "Do you want to save your changes?",
                                                QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard |
                                                QtWidgets.QMessageBox.Cancel)
            if ret == QtWidgets.QMessageBox.Save:
                return self.saveFile('png')
            elif ret == QtWidgets.QMessageBox.Cancel:
                return False

        return True

    def saveFile(self, fileFormat):
        initialPath = QtCore.QDir.currentPath() + '/symbols/' + self.gesture + '.' + fileFormat

        fileName = QtWidgets.QFileDialog.getSaveFileName(self, "Save As",
                                                         initialPath,
                                                         "%s Files (*.%s);;All Files (*)" % (
                                                             fileFormat.upper(), fileFormat))
        if fileName:
            print("saving")
            if self.gesture_creator.saveImage(fileName, fileFormat):
                self.close()
            else:
                return False
        return False
