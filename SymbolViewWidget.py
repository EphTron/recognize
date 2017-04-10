from PyQt5 import QtWidgets, QtGui

from SymbolWriterDialog import SymbolWriterDialog

class SymbolViewWidget(QtWidgets.QWidget):
    def __init__(self, symbol, parent=None):
        super(SymbolViewWidget,self).__init__(parent)

        self.symbol = symbol
        self.writer_dialog = SymbolWriterDialog(self.symbol, self)

        self.label = QtWidgets.QLabel("Symbol " + self.symbol)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.label)

        self.image_label = QtWidgets.QLabel()
        if self.symbol == " ":
            self.pixmap = QtGui.QPixmap('symbols/' + "space" + '.png')
        else:
            self.pixmap = QtGui.QPixmap('symbols/' + self.symbol + '.png')
        self.image_label.setPixmap(self.pixmap)
        self.layout.addWidget(self.image_label)

        self.edit_button = QtWidgets.QPushButton("Edit")
        self.layout.addWidget(self.edit_button)

        @pyqtSlot()
        def on_click():
            self.editor_dialog.exec_()

        self.edit_button.clicked.connect(on_click)
        QObject.connect(self.editor_dialog, SIGNAL("new_image"), self.update_symbol)

        self.setLayout(self.layout)

    def update_symbol(self):
        print("new image foo")
        if self.symbol == " ":
            self.pixmap = QPixmap('symbols/' + "space" + '.png')
        else:
            self.pixmap = QPixmap('symbols/' + self.symbol + '.png')
        self.image_label.setPixmap(self.pixmap)
