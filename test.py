import os
import sys

from PIL.ImageQt import ImageQt
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QPushButton
import tempfile

from pdf2image import convert_from_path


class PrintDemo(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(192, 128))
        self.setWindowTitle("Print Demo")

        printButton = QPushButton('Print', self)
        printButton.clicked.connect(self.onPrint)
        printButton.resize(128, 32)
        printButton.move(32, 48)

    def onPrint(self):
        self.printDialog()

    def printDialog(self):
        file_name_merge = '/qrcode_pdf/document-output__16-54-09.pdf'
        unix_path = str(os.path.dirname(__file__))
        unix_path2 = unix_path.replace('\\', '/')
        file_name_merge2 = unix_path2 + file_name_merge
        print(file_name_merge2)

        filePath, filter = QFileDialog.getOpenFileName(
            self, 'Open file', '', 'PDF (*.pdf)')
        print(filePath)
        if not filePath:
            return
        file_extension = os.path.splitext(filePath)[1]

        if file_extension == ".pdf":
            printer = QPrinter(QPrinter.HighResolution)
            dialog = QPrintDialog(printer, self)
            if dialog.exec_() == QPrintDialog.Accepted:
                with tempfile.TemporaryDirectory() as path:
                    images = convert_from_path(
                        filePath, dpi=300, output_folder=path)
                    painter = QPainter()
                    painter.begin(printer)
                    for i, image in enumerate(images):
                        if i > 0:
                            printer.newPage()
                        rect = painter.viewport()
                        qtImage = ImageQt(image)
                        qtImageScaled = qtImage.scaled(
                            rect.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                        painter.drawImage(rect, qtImageScaled)
                    painter.end()
        else:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = PrintDemo()
    mainWin.show()
    sys.exit(app.exec_())
