from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import qrcode
from datetime import datetime
import sqlite3
from PyQt5.QtWidgets import *
import os
import sys
from PIL import Image
from PyQt5.QtCore import QRegExp, QRect
from PyQt5.QtGui import QRegExpValidator
import hashlib
from reportlab.lib import utils
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from pdf2image import convert_from_path
import time
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame
import csv
import os.path
from PyPDF2 import PdfFileMerger
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QRegion
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
import tempfile
from PIL.ImageQt import ImageQt
import psutil
from PyQt5.QtGui import QMovie
# Do not use Global Variables unless absolutely necessary which 99.9% of the time
# is not the case -- so the basic rule is never use them

# You are not using the added functionality of a QMainWindow as such you ought not
# use it as that is a lot of unnecessary overhead that you are including without
# using and its best to just go with a simple QWidget


class popup_window(QWidget):                           # <===
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Are you sure?")
        self.setWindowIcon(QtGui.QIcon('qr-code-generator.ico'))
        Top = 200
        Left = 200
        Width = 240
        Hight = 320

        self.setGeometry(Left, Top, Width, Hight)
        self.center()
        self.setWindowFlags(Qt.Widget | Qt.FramelessWindowHint)
        radius = 10
        base = self.rect()
        ellipse = QRect(0, 0, 2 * radius, 2 * radius)

        base_region = QRegion(base.adjusted(radius, 0, -radius, 0))
        base_region |= QRegion(base.adjusted(0, radius, 0, -radius))

        base_region |= QRegion(ellipse, QRegion.Ellipse)
        ellipse.moveTopRight(base.topRight())
        base_region |= QRegion(ellipse, QRegion.Ellipse)
        ellipse.moveBottomRight(base.bottomRight())
        base_region |= QRegion(ellipse, QRegion.Ellipse)
        ellipse.moveBottomLeft(base.bottomLeft())
        base_region |= QRegion(ellipse, QRegion.Ellipse)

        self.setMask(base_region)

        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(10, 270, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)

        self.buttonBox.accepted.connect(self.accepted)
        self.buttonBox.rejected.connect(self.reject)

        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 10, 101, 256))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.label1_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(8)
        self.label1_2.setFont(font)
        self.label1_2.setText(textEdit_EmpNo_text)
        self.label1_2.setObjectName("label1_2")
        self.gridLayout.addWidget(self.label1_2, 0, 0, 1, 1)

        self.label2_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(8)
        self.label2_2.setFont(font)
        self.label2_2.setText(textEdit_Line_text)
        self.label2_2.setObjectName("label2_2")
        self.gridLayout.addWidget(self.label2_2, 1, 0, 1, 1)

        self.label3_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(8)
        self.label3_2.setFont(font)
        self.label3_2.setText(textEdit_comboBox)
        self.label3_2.setObjectName("label3_2")
        self.gridLayout.addWidget(self.label3_2, 2, 0, 1, 1)

        self.label4_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(8)
        self.label4_2.setFont(font)
        self.label4_2.setText(textEdit_KanbanId_text)
        self.label4_2.setObjectName("label4_2")
        self.gridLayout.addWidget(self.label4_2, 3, 0, 1, 1)

        self.label5_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(8)
        self.label5_2.setFont(font)
        self.label5_2.setText(textEdit_PartNo_text)
        self.label5_2.setObjectName("label5_2")
        self.gridLayout.addWidget(self.label5_2, 4, 0, 1, 1)

        self.label6_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(8)
        self.label6_2.setFont(font)
        self.label6_2.setText(textEdit_PartId_text)
        self.label6_2.setObjectName("label6_2")
        self.gridLayout.addWidget(self.label6_2, 5, 0, 1, 1)

        self.label7_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(8)
        self.label7_2.setFont(font)
        self.label7_2.setText(textEdit_calendarEdit)
        self.label7_2.setObjectName("label7_2")
        self.gridLayout.addWidget(self.label7_2, 6, 0, 1, 1)

        self.label8_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(8)
        self.label8_2.setFont(font)
        self.label8_2.setText(textEdit_timeEdit)
        self.label8_2.setObjectName("label8_2")
        self.gridLayout.addWidget(self.label8_2, 7, 0, 1, 1)

        self.label9_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(8)
        self.label9_2.setFont(font)
        self.label9_2.setText(textEdit_Amount_text)
        self.label9_2.setObjectName("label9_2")
        self.gridLayout.addWidget(self.label9_2, 8, 0, 1, 1)

        self.label10_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(8)
        self.label10_2.setFont(font)
        self.label10_2.setText(textEdit_AmountStart_text)
        self.label10_2.setObjectName("label10_2")
        self.gridLayout.addWidget(self.label10_2, 9, 0, 1, 1)

        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(20, 10, 92, 256))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.verticalLayout.addWidget(self.label1)

        self.label2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.verticalLayout.addWidget(self.label2)

        self.label3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.verticalLayout.addWidget(self.label3)

        self.label4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.verticalLayout.addWidget(self.label4)

        self.label5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label5.setFont(font)
        self.label5.setObjectName("label5")
        self.verticalLayout.addWidget(self.label5)

        self.label6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label6.setFont(font)
        self.label6.setObjectName("label6")
        self.verticalLayout.addWidget(self.label6)

        self.label7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label7.setFont(font)
        self.label7.setObjectName("label7")
        self.verticalLayout.addWidget(self.label7)

        self.label8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label8.setFont(font)
        self.label8.setObjectName("label8")
        self.verticalLayout.addWidget(self.label8)

        self.label9 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label9.setFont(font)
        self.label9.setObjectName("label9")
        self.verticalLayout.addWidget(self.label9)

        self.label10 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.label10.setFont(font)
        self.label10.setObjectName("label10")
        self.verticalLayout.addWidget(self.label10)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("confirm", "Are you sure?"))
        self.label1.setText(_translate("confirm", "รหัสพนักงาน"))
        self.label2.setText(_translate("confirm", "Line"))
        self.label3.setText(_translate("confirm", "Shift"))
        self.label4.setText(_translate("confirm", "KANBAN ID"))
        self.label5.setText(_translate("confirm", "Part No."))
        self.label6.setText(_translate("confirm", "Part ID"))
        self.label7.setText(_translate("confirm", "Select Date :"))
        self.label8.setText(_translate("confirm", "Select Time : "))
        self.label9.setText(_translate("confirm", "จำนวนที่ต้องการ"))
        self.label10.setText(_translate("confirm", "เริ่มที่"))

        self.clicked = False

        # Label Create
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(25, 25, 250, 250))
        self.label.setMinimumSize(QtCore.QSize(250, 250))
        self.label.setMaximumSize(QtCore.QSize(250, 250))
        self.label.setObjectName("lb1")

        self.movie = QMovie("Rolling-1s.gif")
        self.label.setMovie(self.movie)

        # Start Animation

    def startAnimation(self):
        self.movie.start()

    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()

    def paintEvent(self, event):
        p = QPainter(self)
        p.fillRect(self.rect(), QColor('gainsboro'))

    def mousePressEvent(self, event):
        self.old_pos = event.screenPos()

    def mouseMoveEvent(self, event):
        if self.clicked:
            dx = self.old_pos.x() - event.screenPos().x()
            dy = self.old_pos.y() - event.screenPos().y()
            self.move(self.pos().x() - dx, self.pos().y() - dy)
        self.old_pos = event.screenPos()
        self.clicked = True

        return QWidget.mouseMoveEvent(self, event)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def reject(self):
        self.close()

    def accepted(self):
        global textEdit_EmpNo_text
        global textEdit_Amount_text
        global textEdit_AmountStart_text
        global textEdit_KanbanId_text
        global textEdit_Line_text
        global textEdit_PartId_text
        global textEdit_PartNo_text
        global textEdit_timeEdit
        global textEdit_comboBox
        global textEdit_calendarEdit

        # Data to be encoded

        self.startAnimation()

        date_time_stamp_now = datetime.now()
        timestampStr_now = date_time_stamp_now.strftime("%d%m%Y-%H%M%S")

        conn = sqlite3.connect('qr_code.db')
        conn.execute("INSERT INTO QRCODE (Employee_ID,\
        Amount,\
        Amount_start,\
        Kanban_ID,\
        Line,\
        Part_ID,\
        Part_NO,\
        Time_select,\
        Shift,\
        Date_select,\
        Date_time_stamp)\
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (textEdit_EmpNo_text, textEdit_Amount_text, textEdit_AmountStart_text, textEdit_KanbanId_text, textEdit_Line_text, textEdit_PartId_text, textEdit_PartNo_text, textEdit_timeEdit, textEdit_comboBox, textEdit_calendarEdit, timestampStr_now))
        conn.commit()
        conn.close()

        dateTimeObj = datetime.now()
        list_path = []
        for i in range(int(textEdit_Amount_text)):
            print(i)
            if i == 0:

                str_textEdit_AmountStart_text = str(
                    textEdit_AmountStart_text)
                zero_filled_number = str_textEdit_AmountStart_text.zfill(4)
                dateFormattedYear = dateTimeObj.strftime("%y")
                dateFormattedMonth = dateTimeObj.strftime("%m")
                dateFormattedDay = dateTimeObj.strftime("%d")
                CodeGen = dateFormattedYear + dateFormattedMonth + \
                    dateFormattedDay + textEdit_comboBox + zero_filled_number
                data = {"Part_ID": textEdit_PartId_text,
                        "CodeGen": CodeGen,
                        }
                # Encoding data using make() function
                img = qrcode.make(data)

                # Saving as an image file
                timestampStr = date_time_stamp_now.strftime("_%H-%M-%S")
                path_qrcode = 'qrcode_bin/QRCode_' + CodeGen + timestampStr

                list_path.append(path_qrcode)

                img.save(path_qrcode + '.jpg')

                pagesize = (127.92, 85.28)

                pdf = canvas.Canvas(
                    path_qrcode + '.pdf', pagesize=pagesize)
                pdf.drawImage(path_qrcode + '.jpg',
                              50, 20, 57.09, 57.09)
                pdf.setFont("Times-Roman", 14)
                pdf.drawString(10, 40, textEdit_PartId_text)
                pdf.drawString(25, 12, CodeGen)
                flow_obj = []
                styles = getSampleStyleSheet()
                text = ''''''
                styleN = styles['Normal']
                p_text = Paragraph(text, styleN)
                flow_obj.append(p_text)
                f = Frame(0, 0, 127.8, 85.1, showBoundary=1)
                f.addFromList(flow_obj, pdf)

                pdf.save()

            else:
                textEdit_AmountStart_text = int(
                    textEdit_AmountStart_text) + 1
                str_textEdit_AmountStart_text = str(
                    textEdit_AmountStart_text)
                zero_filled_number = str_textEdit_AmountStart_text.zfill(4)
                dateFormattedYear = dateTimeObj.strftime("%y")
                dateFormattedMonth = dateTimeObj.strftime("%m")
                dateFormattedDay = dateTimeObj.strftime("%d")
                CodeGen = dateFormattedYear + dateFormattedMonth + \
                    dateFormattedDay + textEdit_comboBox + zero_filled_number
                data = {"Part_ID": textEdit_PartId_text,
                        "CodeGen": CodeGen,
                        }
                # Encoding data using make() function
                img = qrcode.make(data)
                # Saving as an image file
                timestampStr = date_time_stamp_now.strftime("_%H-%M-%S")
                path_qrcode = 'qrcode_bin/QRCode_' + CodeGen + timestampStr

                list_path.append(path_qrcode)

                img.save(path_qrcode + '.jpg')

                pagesize = (127.92, 85.28)

                pdf = canvas.Canvas(
                    path_qrcode + '.pdf', pagesize=pagesize)
                pdf.drawImage(path_qrcode + '.jpg',
                              50, 20, 57.09, 57.09)
                pdf.setFont("Times-Roman", 14)
                pdf.drawString(10, 40, textEdit_PartId_text)
                pdf.drawString(25, 12, CodeGen)
                flow_obj = []
                styles = getSampleStyleSheet()
                text = ''''''
                styleN = styles['Normal']
                p_text = Paragraph(text, styleN)
                flow_obj.append(p_text)
                f = Frame(0, 0, 127.8, 85.1, showBoundary=1)
                f.addFromList(flow_obj, pdf)

                pdf.save()

        message = ",\n".join(list_path)
        message1 = "Generate QR code have successfully. \n" + message

        merger = PdfFileMerger()
        for filename in list_path:

            merger.append(filename + ".pdf")

        timestampStr = date_time_stamp_now.strftime("_%H-%M-%S")

        file_name_merge = "qrcode_pdf/document-output_" + timestampStr + ".pdf"
        merger.write(file_name_merge)

        merger.close()

        # QMessageBox.about(self, "แจ้งเตือน",
        #                   message1)

        unix_path = str(os.path.dirname(__file__))

        unix_path2 = unix_path.replace('\\', '/')

        filePath = unix_path2 + '/' + file_name_merge

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
#####################################################
        self.stopAnimation()
        QMessageBox.about(self, "แจ้งเตือน",
                          "Send data for print Successfully! ")

        directory1 = "qrcode_pdf/"
        test1 = os.listdir(directory1)

        for item1 in test1:
            # if item.endswith(".jpg"):
            #     os.remove(os.path.join(directory, item))
            if item1.endswith(".pdf"):
                os.remove(os.path.join(directory1, item1))

        directory = "qrcode_bin/"
        test = os.listdir(directory)
        for item in test:
            if item.endswith(".jpg"):
                os.remove(os.path.join(directory, item))
            if item.endswith(".pdf"):
                os.remove(os.path.join(directory, item))

#         try:
#             directory = "qrcode_bin/"
#             test = os.listdir(directory)

#             for item in test:
#                 if item.endswith(".jpg"):
#                     os.remove(os.path.join(directory, item))
#                 if item.endswith(".pdf"):
#                     os.remove(os.path.join(directory, item))
#         except:  # PermissionError: [WinError 32] The process cannot access the file because it is being used by another process
#             for proc in psutil.process_iter():
#                 if proc.name() == 'python.exe':
#                     proc.kill()

#             directory = "qrcode_bin/"
#             test = os.listdir(directory)

#             for item in test:
#                 if item.endswith(".jpg"):
#                     os.remove(os.path.join(directory, item))
#                 if item.endswith(".pdf"):
#                     os.remove(os.path.join(directory, item))

        self.close()

    def reject(self):
        self.close()


class admin_page(QWidget):                           # <===
    def __init__(self):

        global textUsername

        QWidget.__init__(self)
        self.setWindowTitle("Program Qrcode Generator")
        self.setWindowIcon(QtGui.QIcon('qr-code-generator.ico'))
        Top = 200
        Left = 200
        Width = 700
        Hight = 520
        self.setGeometry(Left, Top, Width, Hight)
        self.center()
        self.setWindowFlags(Qt.Widget | Qt.FramelessWindowHint)
        radius = 10
        base = self.rect()
        ellipse = QRect(0, 0, 2 * radius, 2 * radius)

        base_region = QRegion(base.adjusted(radius, 0, -radius, 0))
        base_region |= QRegion(base.adjusted(0, radius, 0, -radius))

        base_region |= QRegion(ellipse, QRegion.Ellipse)
        ellipse.moveTopRight(base.topRight())
        base_region |= QRegion(ellipse, QRegion.Ellipse)
        ellipse.moveBottomRight(base.bottomRight())
        base_region |= QRegion(ellipse, QRegion.Ellipse)
        ellipse.moveBottomLeft(base.bottomLeft())
        base_region |= QRegion(ellipse, QRegion.Ellipse)

        self.setMask(base_region)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(20, 50, 661, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        # self.tab.setIcon(
        #     self.style().standardIcon(QStyle.SP_FileDialogStart))

        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_16.setGeometry(QtCore.QRect(50, 770, 121, 31))
        self.lineEdit_16.setAutoFillBackground(False)
        self.lineEdit_16.setStyleSheet("")
        self.lineEdit_16.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_16.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_16.setObjectName("lineEdit_16")

        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_17.setGeometry(QtCore.QRect(250, 770, 121, 31))
        self.lineEdit_17.setAutoFillBackground(False)
        self.lineEdit_17.setStyleSheet("")
        self.lineEdit_17.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_17.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_17.setObjectName("lineEdit_17")

        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_18.setGeometry(QtCore.QRect(470, 770, 121, 31))
        self.lineEdit_18.setAutoFillBackground(False)
        self.lineEdit_18.setStyleSheet("")
        self.lineEdit_18.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_18.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_18.setObjectName("lineEdit_18")

        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 70, 421, 281))
        self.layoutWidget.setObjectName("layoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.table_part_kanban = QtWidgets.QTableWidget(self.layoutWidget)
        self.table_part_kanban.setObjectName("table_part_kanban")
        self.horizontalLayout.addWidget(self.table_part_kanban)
        self.table_part_kanban.setRowCount(10)
        self.table_part_kanban.setColumnCount(3)
        columns1 = ['KANBAN_ID', 'PART_NO', 'PART_ID']
        self.table_part_kanban.setHorizontalHeaderLabels(columns1)

        self.table_part_kanban.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)
        self.table_part_kanban.horizontalHeader().setSectionResizeMode(
            1, QtWidgets.QHeaderView.Stretch)
        self.table_part_kanban.horizontalHeader().setSectionResizeMode(
            2, QtWidgets.QHeaderView.Stretch)

        conn5 = sqlite3.connect('qr_code.db')

        result1 = conn5.execute("SELECT * FROM PART_KANBAN")
        self.table_part_kanban.setRowCount(0)
        for row_number1, row_data1 in enumerate(result1):
            self.table_part_kanban.insertRow(row_number1)
            for column_number1, data1 in enumerate(row_data1):

                self.table_part_kanban.setItem(
                    row_number1, column_number1, QtWidgets.QTableWidgetItem(str(data1)))

        conn5.commit()

        conn5.close()

        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 360, 421, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)

        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.lineEdit_Kanban_ID = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_Kanban_ID.setAutoFillBackground(False)
        self.lineEdit_Kanban_ID.setStyleSheet("")
        self.lineEdit_Kanban_ID.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_Kanban_ID.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_Kanban_ID.setObjectName("lineEdit_Kanban_ID")
        self.horizontalLayout_3.addWidget(self.lineEdit_Kanban_ID)

        self.lineEdit_Part_NO = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_Part_NO.setAutoFillBackground(False)
        self.lineEdit_Part_NO.setStyleSheet("")
        self.lineEdit_Part_NO.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_Part_NO.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_Part_NO.setObjectName("lineEdit_Part_NO")
        self.horizontalLayout_3.addWidget(self.lineEdit_Part_NO)

        self.lineEdit_Part_ID = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_Part_ID.setAutoFillBackground(False)
        self.lineEdit_Part_ID.setStyleSheet("")
        self.lineEdit_Part_ID.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_Part_ID.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_Part_ID.setObjectName("lineEdit_Part_ID")
        self.horizontalLayout_3.addWidget(self.lineEdit_Part_ID)

        self.layoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(260, 390, 171, 25))
        self.layoutWidget_2.setObjectName("layoutWidget_2")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_part_kanban_Add = QtWidgets.QPushButton(
            self.layoutWidget_2)
        self.pushButton_part_kanban_Add.setObjectName(
            "pushButton_part_kanban_Add")
        self.horizontalLayout_4.addWidget(self.pushButton_part_kanban_Add)
        self.pushButton_part_kanban_Add.clicked.connect(self.add_part_kanban)
        self.pushButton_part_kanban_Add.setIcon(
            self.style().standardIcon(QStyle.SP_DialogApplyButton))

        self.pushButton_part_kanban_Del = QtWidgets.QPushButton(
            self.layoutWidget_2)
        self.pushButton_part_kanban_Del.setObjectName(
            "pushButton_part_kanban_Del")
        self.horizontalLayout_4.addWidget(self.pushButton_part_kanban_Del)
        self.pushButton_part_kanban_Del.clicked.connect(
            self.delete_part_kanban)
        self.pushButton_part_kanban_Del.setIcon(
            self.style().standardIcon(QStyle.SP_TrashIcon))

        self.search_part_kanban = QtWidgets.QLineEdit(self.tab)
        self.search_part_kanban.setGeometry(QtCore.QRect(10, 40, 421, 20))
        self.search_part_kanban.setObjectName("search_part_kanban")
        self.search_part_kanban.textChanged.connect(self.findName_part_kanban)
        self.search_part_kanban.setStyleSheet("\n"
                                              "border-style: outset;\n"
                                              "border-width: 1px;\n"
                                              "border-radius: 7px;\n"
                                              "border-color: black;\n"
                                              "padding: 4px;")

        self.lineEdit_Line = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Line.setGeometry(QtCore.QRect(440, 361, 201, 20))
        self.lineEdit_Line.setAutoFillBackground(False)
        self.lineEdit_Line.setStyleSheet("")
        self.lineEdit_Line.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_Line.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_Line.setObjectName("lineEdit_Line")

        self.table_line = QtWidgets.QTableWidget(self.tab)
        self.table_line.setGeometry(QtCore.QRect(440, 70, 201, 281))
        self.table_line.setObjectName("table_line")
        self.table_line.setRowCount(1)
        self.table_line.setColumnCount(1)
        columns1 = ['LINE']
        self.table_line.setHorizontalHeaderLabels(columns1)

        self.table_line.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)

        conn5 = sqlite3.connect('qr_code.db')

        result1 = conn5.execute("SELECT * FROM LINE")
        self.table_line.setRowCount(0)
        for row_number1, row_data1 in enumerate(result1):
            self.table_line.insertRow(row_number1)
            for column_number1, data1 in enumerate(row_data1):

                self.table_line.setItem(
                    row_number1, column_number1, QtWidgets.QTableWidgetItem(str(data1)))

        conn5.commit()

        conn5.close()

        self.search_line = QtWidgets.QLineEdit(self.tab)
        self.search_line.setGeometry(QtCore.QRect(440, 40, 201, 20))
        self.search_line.setObjectName("search_line")
        self.search_line.textChanged.connect(self.findName_line)
        self.search_line.setStyleSheet("\n"
                                       "border-style: outset;\n"
                                       "border-width: 1px;\n"
                                       "border-radius: 7px;\n"
                                       "border-color: black;\n"
                                       "padding: 4px;")

        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(470, 390, 171, 25))
        self.widget.setObjectName("widget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.pushButton_Line_Add = QtWidgets.QPushButton(self.widget)
        self.pushButton_Line_Add.setObjectName("pushButton_Line_Add")
        self.horizontalLayout_2.addWidget(self.pushButton_Line_Add)
        self.pushButton_Line_Add.clicked.connect(self.add_line)
        self.pushButton_Line_Add.setIcon(
            self.style().standardIcon(QStyle.SP_DialogApplyButton))

        self.pushButton_Line_Del = QtWidgets.QPushButton(self.widget)
        self.pushButton_Line_Del.setObjectName("pushButton_Line_Del")
        self.horizontalLayout_2.addWidget(self.pushButton_Line_Del)
        self.pushButton_Line_Del.clicked.connect(self.delete_line)
        self.pushButton_Line_Del.setIcon(
            self.style().standardIcon(QStyle.SP_TrashIcon))

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 10, 341, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 10, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.add_admin_user)
        self.pushButton_2.setIcon(
            self.style().standardIcon(QStyle.SP_DialogApplyButton))

        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 631, 291))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(3)
        columns1 = ['Employee_ID', 'Password', 'Create_date']
        self.tableWidget.setHorizontalHeaderLabels(columns1)

        self.tableWidget.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            2, QtWidgets.QHeaderView.Stretch)

        conn5 = sqlite3.connect('qr_code.db')

        result1 = conn5.execute("SELECT * FROM ADMIN_USER")
        self.tableWidget.setRowCount(0)
        for row_number1, row_data1 in enumerate(result1):
            self.tableWidget.insertRow(row_number1)
            for column_number1, data1 in enumerate(row_data1):

                self.tableWidget.setItem(
                    row_number1, column_number1, QtWidgets.QTableWidgetItem(str(data1)))

        conn5.commit()

        conn5.close()

        self.delete_admin_user_button = QtWidgets.QPushButton(self.tab_2)
        self.delete_admin_user_button.setGeometry(
            QtCore.QRect(520, 390, 121, 31))
        self.delete_admin_user_button.setObjectName("delete_admin_user_button")
        self.delete_admin_user_button.clicked.connect(self.delete_admin_user)
        self.delete_admin_user_button.setIcon(
            self.style().standardIcon(QStyle.SP_TrashIcon))

        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(10, 50, 631, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.tabWidget.addTab(self.tab_2, "")

        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 20, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.MainWindow)
        self.pushButton_3.setIcon(
            self.style().standardIcon(QStyle.SP_ArrowBack))

        self.tabWidget.raise_()
        self.label_2.raise_()
        self.pushButton_3.raise_()

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Program Qrcode Generator"))
        self.label_2.setText(_translate("Dialog", "ADMIN PAGE"))
        self.label.setText(_translate("Dialog", "Edit Data"))
        # self.label.setIcon(
        #     self.style().standardIcon(QStyle.SP_FileDialogStart))

        self.lineEdit_16.setPlaceholderText(_translate("Dialog", "PART ID"))
        self.lineEdit_17.setPlaceholderText(_translate("Dialog", "PART ID"))
        self.lineEdit_18.setPlaceholderText(_translate("Dialog", "PART ID"))
        self.lineEdit_Part_ID.setPlaceholderText(
            _translate("Dialog", "PART ID"))
        self.lineEdit_Part_NO.setPlaceholderText(
            _translate("Dialog", "PART NO"))
        self.lineEdit_Kanban_ID.setPlaceholderText(
            _translate("Dialog", "KABAN ID"))
        self.pushButton_part_kanban_Add.setText(_translate("Dialog", "Add"))
        self.pushButton_part_kanban_Del.setText(_translate("Dialog", "Delete"))
        self.search_part_kanban.setPlaceholderText(
            _translate("Dialog", "Search . . ."))
        self.lineEdit_Line.setPlaceholderText(_translate("Dialog", "LINE"))
        self.search_line.setPlaceholderText(
            _translate("Dialog", "Search . . ."))
        self.pushButton_Line_Add.setText(_translate("Dialog", "Add"))
        self.pushButton_Line_Del.setText(_translate("Dialog", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("Dialog", "Edit Data"))
        self.lineEdit_3.setPlaceholderText(
            _translate("Dialog", "Add Employee ID"))
        self.pushButton_2.setText(_translate("Dialog", "Add"))
        self.label_3.setText(_translate("Dialog", "ADD Employee ID"))
        self.delete_admin_user_button.setText(_translate("Dialog", "Delete"))
        self.lineEdit_9.setPlaceholderText(
            _translate("Dialog", "Search . . ."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("Dialog", "Add admin"))
        self.pushButton_3.setText(_translate("Dialog", "back"))
        self.clicked = False

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def MainWindow(self):                                             # <===
        self.w = MainWindow()
        self.w.show()
        self.hide()

    def paintEvent(self, event):
        p = QPainter(self)
        p.fillRect(self.rect(), QColor(128, 128, 128, 128))

    def mousePressEvent(self, event):
        self.old_pos = event.screenPos()

    def mouseMoveEvent(self, event):
        if self.clicked:
            dx = self.old_pos.x() - event.screenPos().x()
            dy = self.old_pos.y() - event.screenPos().y()
            self.move(self.pos().x() - dx, self.pos().y() - dy)
        self.old_pos = event.screenPos()
        self.clicked = True

        return QWidget.mouseMoveEvent(self, event)

    def findName_line(self):
        name3 = self.search_line.text().lower()
        for row3 in range(self.table_line.rowCount()):
            item3 = self.table_line.item(row3, 0)

            self.table_line.setRowHidden(
                row3, name3 not in item3.text().lower())

    def findName_part_kanban(self):
        name1 = self.search_part_kanban.text().lower()
        for row1 in range(self.table_part_kanban.rowCount()):
            item1 = self.table_part_kanban.item(row1, 0)

            self.table_part_kanban.setRowHidden(
                row1, name1 not in item1.text().lower())

    def add_part_kanban(self):
        connect = sqlite3.connect('qr_code.db')

        part_id = self.lineEdit_Part_ID.text()
        part_no = self.lineEdit_Part_NO.text()
        kanban_id = self.lineEdit_Kanban_ID.text()

        date_now = datetime.now()
        date_now_convert = date_now.strftime('%d/%m/%Y %H:%M')

        if part_id == "" or part_no == "" or kanban_id == "":
            self.lineEdit_Part_ID.setFocus()
            self.lineEdit_Part_ID.setStyleSheet(
                "border: 1px solid red;")
            self.lineEdit_Part_NO.setFocus()
            self.lineEdit_Part_NO.setStyleSheet(
                "border: 1px solid red;")
            self.lineEdit_Kanban_ID.setFocus()
            self.lineEdit_Kanban_ID.setStyleSheet(
                "border: 1px solid red;")
            popup3 = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                                           "แจ้งเตือน",
                                           "กรุณากรอกข้อมูลให้ครบถ้วน",
                                           QtWidgets.QMessageBox.Ok,
                                           self)
            popup3.show()

        else:

            # result_check_duplicate_part_id = connect.execute(
            #     "SELECT PART_ID FROM PART_KANBAN where PART_ID = ? ", (part_id,))
            # result_check_duplicate_part_no = connect.execute(
            #     "SELECT PART_NO FROM PART_KANBAN where PART_NO = ? ", (part_no,))
            result_check_duplicate_kanban = connect.execute(
                "SELECT KANBAN_ID FROM PART_KANBAN where KANBAN_ID = ? ", (kanban_id,))

            # check_count_part_id = 0
            # check_count_part_no = 0
            check_count_kanban = 0
            # for row1 in result_check_duplicate_part_id:
            #     check_count_part_id = check_count_part_id + 1
            # for row2 in result_check_duplicate_part_id:
            #     check_count_part_no = check_count_part_no + 1
            for row3 in result_check_duplicate_kanban:
                check_count_kanban = check_count_kanban + 1

            if check_count_kanban == 0:

                textEmployee_on = Employee_on

                connect.execute("INSERT INTO PART_KANBAN (PART_ID,PART_NO,KANBAN_ID,Create_date,EMPLOYEE_ID) VALUES (? , ? , ?, ?, ?)",
                                (part_id, part_no, kanban_id, date_now_convert, textEmployee_on))

                connect.commit()

                QMessageBox.information(
                    self,
                    "Program QR code Generator",
                    "Data added successfully .",
                    QMessageBox.Ok)

                self.lineEdit_Part_ID.setStyleSheet("")

                self.lineEdit_Part_NO.setStyleSheet(
                    "")

                self.lineEdit_Kanban_ID.setStyleSheet(
                    "")

                self.load_database_part_kanban()

            else:
                self.lineEdit_Part_ID.setFocus()
                self.lineEdit_Part_ID.setStyleSheet(
                    "border: 1px solid red;")
                self.lineEdit_Part_NO.setFocus()
                self.lineEdit_Part_NO.setStyleSheet(
                    "border: 1px solid red;")
                self.lineEdit_Kanban_ID.setFocus()
                self.lineEdit_Kanban_ID.setStyleSheet(
                    "border: 1px solid red;")

                QMessageBox.critical(
                    self,
                    "Data is Duplicated.",
                    "Data is Duplicated. (Part_id or Part_no or kanban_id)",
                    QMessageBox.Ok)

            connect.close()

    def load_database_part_kanban(self):
        while self.table_part_kanban.rowCount() > 0:
            self.table_part_kanban.removeRow(0)
        conn4 = sqlite3.connect('qr_code.db')
        result = conn4.execute("SELECT * FROM PART_KANBAN")
        self.table_part_kanban.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table_part_kanban.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table_part_kanban.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        conn4.commit()

    def add_line(self):
        connect = sqlite3.connect('qr_code.db')

        line = self.lineEdit_Line.text()

        date_now = datetime.now()
        date_now_convert = date_now.strftime('%d/%m/%Y %H:%M')

        if line == "":
            popup3 = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                                           "แจ้งเตือน",
                                           "กรุณากรอกข้อมูลให้ครบถ้วน",
                                           QtWidgets.QMessageBox.Ok,
                                           self)
            popup3.show()

        else:

            result_check_duplicate_line = connect.execute(
                "SELECT LINE FROM LINE where LINE = ? ", (line,))

            check_count_line = 0

            for row3 in result_check_duplicate_line:
                check_count_line = check_count_line + 1

            if check_count_line == 0:
                textEmployee_on = Employee_on

                connect.execute("INSERT INTO LINE (LINE,Create_date,EMPLOYEE_ID) VALUES (?, ? , ?)",
                                (line, date_now_convert,textEmployee_on))

                connect.commit()

                QMessageBox.information(
                    self,
                    "Program QR code Generator",
                    "Data added successfully .",
                    QMessageBox.Ok)

                self.load_database_line()

            else:

                QMessageBox.critical(
                    self,
                    "Data is Duplicated.",
                    "Data is Duplicated.",
                    QMessageBox.Ok)

            connect.close()

    def load_database_line(self):
        while self.table_line.rowCount() > 0:
            self.table_line.removeRow(0)
        conn4 = sqlite3.connect('qr_code.db')
        result = conn4.execute("SELECT LINE FROM LINE")
        self.table_line.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table_line.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table_line.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        conn4.commit()

    def delete_part_kanban(self):
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("Are you sure to delete ?")
        msgBox.setWindowTitle("Delete Data Warning")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:

            conne = sqlite3.connect('qr_code.db')

            result1 = conne.execute("SELECT * FROM PART_KANBAN")

            for row_data in enumerate(result1):
                if row_data[0] == self.table_part_kanban.currentRow():
                    data = row_data[1]
                    kanban_id = data[0]
                    part_no = data[1]
                    part_id = data[2]
                    create_date = data[3]

                    conne.execute("DELETE FROM PART_KANBAN WHERE  KANBAN_ID=? AND PART_NO=? AND PART_ID=? AND Create_date=?",
                                  (kanban_id, part_no, part_id, create_date,))
                    conne.commit()

                    self.load_database_part_kanban()

            QMessageBox.information(
                self,
                "Program QR code Generator",
                "The data was successfully deleted.",
                QMessageBox.Ok)

            conne.close()

    def delete_line(self):
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("Are you sure to delete ?")
        msgBox.setWindowTitle("Delete Data Warning")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:

            conne = sqlite3.connect('qr_code.db')

            result1 = conne.execute("SELECT * FROM LINE")

            for row_data in enumerate(result1):
                if row_data[0] == self.table_line.currentRow():
                    data = row_data[1]
                    line = data[0]
                    create_date = data[1]

                    conne.execute("DELETE FROM LINE WHERE LINE=? AND Create_date=?",
                                  (line, create_date,))
                    conne.commit()

                    self.load_database_line()

            QMessageBox.information(
                self,
                "Program QR code Generator",
                "The data was successfully deleted.",
                QMessageBox.Ok)

            conne.close()

    def delete_admin_user(self):

        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("Are you sure to delete ?")
        msgBox.setWindowTitle("Delete Data Warning")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            conn4 = sqlite3.connect('qr_code.db')

            result = conn4.execute("SELECT * FROM ADMIN_USER")

            for row_data in enumerate(result):
                if row_data[0] == self.tableWidget.currentRow():
                    data = row_data[1]
                    employee_id = data[0]
                    pass_word = data[1]
                    time_create = data[2]
                    conn4.execute("DELETE FROM ADMIN_USER WHERE Employee_ID=? AND Password=? AND Time_to_update=?",
                                  (employee_id, pass_word, time_create,))
                    conn4.commit()

                    self.load_database_admin()

            QMessageBox.information(
                self,
                "Program QR code Generator",
                "The admin was successfully deleted.",
                QMessageBox.Ok)

            conn4.close()

    def load_database_admin(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        conn5 = sqlite3.connect('qr_code.db')
        result1 = conn5.execute("SELECT * FROM ADMIN_USER")
        self.tableWidget.setRowCount(0)
        for row_number1, row_data1 in enumerate(result1):
            self.tableWidget.insertRow(row_number1)
            for column_number1, data1 in enumerate(row_data1):

                self.tableWidget.setItem(
                    row_number1, column_number1, QtWidgets.QTableWidgetItem(str(data1)))

        conn5.commit()

        conn5.close()

    def add_admin_user(self):
        conn6 = sqlite3.connect('qr_code.db')
        admin_new = self.lineEdit_3.text()

        # password_salt = os.urandom(32).hex()
        password = admin_new

        result_check_duplicate = conn6.execute(
            "SELECT Employee_ID FROM ADMIN_USER where Employee_ID = ?", (admin_new,))

        check_count = 0
        for row1 in result_check_duplicate:
            check_count = check_count + 1

        if check_count == 0:

            hash = hashlib.sha512()
            # hash.update(('%s%s' % (password_salt, password)).encode('utf-8'))
            hash.update(('%s' % (password)).encode('utf-8'))
            password_hash = hash.hexdigest()

            conn6.execute("INSERT INTO ADMIN_USER (Employee_ID,Password,Time_to_update) \
                VALUES (? , ? , ?)", (admin_new, password_hash, datetime.now()))

            conn6.commit()

            self.load_database_admin()

            QMessageBox.information(
                self,
                "Program QR code Generator",
                "The new admin was successfully added.",
                QMessageBox.Ok)
        else:

            QMessageBox.critical(
                self,
                "Employee ID is Duplicated.",
                "Employee ID is already.",
                QMessageBox.Ok)

        conn6.close()

#         self.label_2 = QtWidgets.QLabel(self)
#         self.label_2.setGeometry(QtCore.QRect(20, 10, 141, 31))
#         font = QtGui.QFont()
#         font.setFamily("Mitr")
#         font.setPointSize(16)
#         self.label_2.setFont(font)
#         self.label_2.setObjectName("label_2")

#         self.tabWidget = QtWidgets.QTabWidget(self)
#         self.tabWidget.setGeometry(QtCore.QRect(20, 50, 661, 461))
#         self.tabWidget.setObjectName("tabWidget")

#         # self.tab = QtWidgets.QWidget()
#         # self.tab.setObjectName("tab")

#         # self.pushButton = QtWidgets.QPushButton(self.tab)
#         # self.pushButton.setGeometry(QtCore.QRect(520, 10, 121, 31))
#         # self.pushButton.setObjectName("pushButton")
#         # self.pushButton.clicked.connect(self.add_part)

#         # self.delete_part_button = QtWidgets.QPushButton(self.tab)
#         # self.delete_part_button.setGeometry(
#         #     QtCore.QRect(520, 390, 121, 31))
#         # self.delete_part_button.setObjectName("delete_part_button")
#         # self.delete_part_button.clicked.connect(self.delete_part)

#         # self.lineEdit = QtWidgets.QLineEdit(self.tab)
#         # self.lineEdit.setGeometry(QtCore.QRect(110, 10, 191, 31))
#         # self.lineEdit.setObjectName("lineEdit")

#         # self.tableWidget = QtWidgets.QTableWidget(self.tab)
#         # self.tableWidget.setGeometry(QtCore.QRect(10, 90, 631, 291))
#         # self.tableWidget.setRowCount(10)
#         # self.tableWidget.setColumnCount(4)
#         # self.tableWidget.setObjectName("tableWidget")
#         # columns = ['Part_ID', 'Part_NO', 'Create_date', 'Employee_ID_added']
#         # self.tableWidget.setHorizontalHeaderLabels(columns)

#         # self.tableWidget.horizontalHeader().setSectionResizeMode(
#         #     0, QtWidgets.QHeaderView.Stretch)
#         # self.tableWidget.horizontalHeader().setSectionResizeMode(
#         #     1, QtWidgets.QHeaderView.Stretch)
#         # self.tableWidget.horizontalHeader().setSectionResizeMode(
#         #     2, QtWidgets.QHeaderView.Stretch)
#         # self.tableWidget.horizontalHeader().setSectionResizeMode(
#         #     3, QtWidgets.QHeaderView.Stretch)

#         # conn4 = sqlite3.connect('qr_code.db')

#         # result = conn4.execute("SELECT * FROM PART_DETAIL")
#         # self.tableWidget.setRowCount(0)
#         # for row_number, row_data in enumerate(result):
#         #     self.tableWidget.insertRow(row_number)
#         #     for column_number, data in enumerate(row_data):

#         #         self.tableWidget.setItem(
#         #             row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

#         # conn4.commit()

#         # conn4.close()
#         # self.search = QLineEdit(self.tab)
#         # self.search.setGeometry(QtCore.QRect(10, 50, 631, 31))
#         # self.search.setObjectName("search")
#         # self.search.textChanged.connect(self.findName)
#         # self.search.setStyleSheet("\n"
#         #                           "border-style: outset;\n"
#         #                           "border-width: 1px;\n"
#         #                           "border-radius: 7px;\n"
#         #                           "border-color: black;\n"
#         #                           "padding: 4px;")
#         # self.label = QtWidgets.QLabel(self.tab)
#         # self.label.setGeometry(QtCore.QRect(10, 10, 91, 31))
#         # font = QtGui.QFont()
#         # font.setFamily("Mitr")
#         # font.setPointSize(12)
#         # self.label.setFont(font)
#         # self.label.setObjectName("label")

#         # self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
#         # self.lineEdit_2.setGeometry(QtCore.QRect(320, 10, 181, 31))
#         # self.lineEdit_2.setObjectName("lineEdit_2")

# ###################################################################

#         self.tab = QtWidgets.QWidget()
#         self.tab.setObjectName("tab")
#         self.label = QtWidgets.QLabel(self.tab)
#         self.label.setGeometry(QtCore.QRect(10, 10, 91, 31))
#         font = QtGui.QFont()
#         font.setFamily("Mitr")
#         font.setPointSize(12)
#         self.label.setFont(font)
#         self.label.setObjectName("label")
#         self.layoutWidget = QtWidgets.QWidget(self.tab)
#         self.layoutWidget.setGeometry(QtCore.QRect(10, 70, 631, 281))
#         self.layoutWidget.setObjectName("layoutWidget")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
#         self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout.setObjectName("horizontalLayout")

#         self.tableWidget_Part_ID = QtWidgets.QTableWidget(self.layoutWidget)
#         self.tableWidget_Part_ID.setObjectName("tableWidget_Part_ID")
#         self.tableWidget_Part_ID.setColumnCount(1)
#         self.tableWidget_Part_ID.setRowCount(1)
#         self.horizontalLayout.addWidget(self.tableWidget_Part_ID)
#         columns = ['PART_ID']
#         self.tableWidget_Part_ID.setHorizontalHeaderLabels(columns)

#         self.tableWidget_Part_ID.horizontalHeader().setSectionResizeMode(
#             0, QtWidgets.QHeaderView.Stretch)

#         conn_part_id = sqlite3.connect('qr_code.db')

#         result = conn_part_id.execute("SELECT * FROM PART_ID")
#         self.tableWidget_Part_ID.setRowCount(0)
#         for row_number, row_data in enumerate(result):
#             self.tableWidget_Part_ID.insertRow(row_number)
#             for column_number, data in enumerate(row_data):

#                 self.tableWidget_Part_ID.setItem(
#                     row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

#         conn_part_id.commit()

#         conn_part_id.close()

#         self.tableWidget_Part_NO = QtWidgets.QTableWidget(self.layoutWidget)
#         self.tableWidget_Part_NO.setObjectName("tableWidget_Part_NO")
#         self.tableWidget_Part_NO.setColumnCount(1)
#         self.tableWidget_Part_NO.setRowCount(1)
#         self.horizontalLayout.addWidget(self.tableWidget_Part_NO)
#         columns1 = ['PART_NO']
#         self.tableWidget_Part_NO.setHorizontalHeaderLabels(columns1)

#         self.tableWidget_Part_NO.horizontalHeader().setSectionResizeMode(
#             0, QtWidgets.QHeaderView.Stretch)

#         conn_part_no = sqlite3.connect('qr_code.db')

#         result = conn_part_no.execute("SELECT * FROM PART_NO")
#         self.tableWidget_Part_NO.setRowCount(0)
#         for row_number, row_data in enumerate(result):
#             self.tableWidget_Part_NO.insertRow(row_number)
#             for column_number, data in enumerate(row_data):

#                 self.tableWidget_Part_NO.setItem(
#                     row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

#         conn_part_no.commit()

#         conn_part_no.close()

#         self.tableWidget_Line = QtWidgets.QTableWidget(self.layoutWidget)
#         self.tableWidget_Line.setObjectName("tableWidget_Line")
#         self.tableWidget_Line.setColumnCount(1)
#         self.tableWidget_Line.setRowCount(1)
#         self.horizontalLayout.addWidget(self.tableWidget_Line)
#         columns2 = ['LINE']
#         self.tableWidget_Line.setHorizontalHeaderLabels(columns2)

#         self.tableWidget_Line.horizontalHeader().setSectionResizeMode(
#             0, QtWidgets.QHeaderView.Stretch)

#         conn_line = sqlite3.connect('qr_code.db')

#         result = conn_line.execute("SELECT * FROM LINE")
#         self.tableWidget_Line.setRowCount(0)
#         for row_number, row_data in enumerate(result):
#             self.tableWidget_Line.insertRow(row_number)
#             for column_number, data in enumerate(row_data):

#                 self.tableWidget_Line.setItem(
#                     row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

#         conn_line.commit()

#         conn_line.close()

#         self.tableWidget_Kanban_ID = QtWidgets.QTableWidget(self.layoutWidget)
#         self.tableWidget_Kanban_ID.setObjectName("tableWidget_Kanban_ID")
#         self.tableWidget_Kanban_ID.setColumnCount(1)
#         self.tableWidget_Kanban_ID.setRowCount(1)
#         self.horizontalLayout.addWidget(self.tableWidget_Kanban_ID)
#         columns3 = ['KANBAN_ID']
#         self.tableWidget_Kanban_ID.setHorizontalHeaderLabels(columns3)

#         self.tableWidget_Kanban_ID.horizontalHeader().setSectionResizeMode(
#             0, QtWidgets.QHeaderView.Stretch)

#         conn_kanban = sqlite3.connect('qr_code.db')

#         result = conn_kanban.execute("SELECT * FROM KANBAN_ID")
#         self.tableWidget_Kanban_ID.setRowCount(0)
#         for row_number, row_data in enumerate(result):
#             self.tableWidget_Kanban_ID.insertRow(row_number)
#             for column_number, data in enumerate(row_data):

#                 self.tableWidget_Kanban_ID.setItem(
#                     row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

#         conn_kanban.commit()

#         conn_kanban.close()

#         self.layoutWidget1 = QtWidgets.QWidget(self.tab)
#         self.layoutWidget1.setGeometry(QtCore.QRect(10, 40, 631, 20))
#         self.layoutWidget1.setObjectName("layoutWidget1")
#         self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
#         self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_2.setObjectName("horizontalLayout_2")
#         self.lineEdit_search_Part_ID = QtWidgets.QLineEdit(self.layoutWidget1)
#         self.lineEdit_search_Part_ID.setMinimumSize(QtCore.QSize(0, 0))
#         self.lineEdit_search_Part_ID.setObjectName("lineEdit_search_Part_ID")
#         self.horizontalLayout_2.addWidget(self.lineEdit_search_Part_ID)
#         self.lineEdit_search_Part_ID.textChanged.connect(self.findName_part_id)
#         self.lineEdit_search_Part_ID.setStyleSheet("\n"
#                                                    "border-style: outset;\n"
#                                                    "border-width: 1px;\n"
#                                                    "border-radius: 7px;\n"
#                                                    "border-color: black;\n"
#                                                    "padding: 4px;")

#         self.lineEdit_search_Part_NO = QtWidgets.QLineEdit(self.layoutWidget1)
#         self.lineEdit_search_Part_NO.setObjectName("lineEdit_search_Part_NO")
#         self.horizontalLayout_2.addWidget(self.lineEdit_search_Part_NO)
#         self.lineEdit_search_Part_NO.textChanged.connect(self.findName_part_no)
#         self.lineEdit_search_Part_NO.setStyleSheet("\n"
#                                                    "border-style: outset;\n"
#                                                    "border-width: 1px;\n"
#                                                    "border-radius: 7px;\n"
#                                                    "border-color: black;\n"
#                                                    "padding: 4px;")

#         self.lineEdit_search_Line = QtWidgets.QLineEdit(self.layoutWidget1)
#         self.lineEdit_search_Line.setObjectName("lineEdit_search_Line")
#         self.horizontalLayout_2.addWidget(self.lineEdit_search_Line)
#         self.lineEdit_search_Line.textChanged.connect(self.findName_line)
#         self.lineEdit_search_Line.setStyleSheet("\n"
#                                                 "border-style: outset;\n"
#                                                 "border-width: 1px;\n"
#                                                 "border-radius: 7px;\n"
#                                                 "border-color: black;\n"
#                                                 "padding: 4px;")

#         self.lineEdit_search_Kanban_ID = QtWidgets.QLineEdit(
#             self.layoutWidget1)
#         self.lineEdit_search_Kanban_ID.setObjectName(
#             "lineEdit_search_Kanban_ID")
#         self.horizontalLayout_2.addWidget(self.lineEdit_search_Kanban_ID)
#         self.lineEdit_search_Kanban_ID.textChanged.connect(
#             self.findName_kanban)
#         self.lineEdit_search_Kanban_ID.setStyleSheet("\n"
#                                                      "border-style: outset;\n"
#                                                      "border-width: 1px;\n"
#                                                      "border-radius: 7px;\n"
#                                                      "border-color: black;\n"
#                                                      "padding: 4px;")

#         self.layoutWidget2 = QtWidgets.QWidget(self.tab)
#         self.layoutWidget2.setGeometry(QtCore.QRect(10, 360, 631, 25))
#         self.layoutWidget2.setObjectName("layoutWidget2")
#         self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
#         self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_3.setObjectName("horizontalLayout_3")

#         self.lineEdit_Part_ID = QtWidgets.QLineEdit(self.layoutWidget2)
#         self.lineEdit_Part_ID.setAutoFillBackground(False)
#         self.lineEdit_Part_ID.setStyleSheet("")
#         self.lineEdit_Part_ID.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
#         self.lineEdit_Part_ID.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
#         self.lineEdit_Part_ID.setObjectName("lineEdit_Part_ID")
#         self.horizontalLayout_3.addWidget(self.lineEdit_Part_ID)

#         self.lineEdit_Part_NO = QtWidgets.QLineEdit(self.layoutWidget2)
#         self.lineEdit_Part_NO.setAutoFillBackground(False)
#         self.lineEdit_Part_NO.setStyleSheet("")
#         self.lineEdit_Part_NO.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
#         self.lineEdit_Part_NO.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
#         self.lineEdit_Part_NO.setObjectName("lineEdit_Part_NO")
#         self.horizontalLayout_3.addWidget(self.lineEdit_Part_NO)

#         self.lineEdit_Line = QtWidgets.QLineEdit(self.layoutWidget2)
#         self.lineEdit_Line.setAutoFillBackground(False)
#         self.lineEdit_Line.setStyleSheet("")
#         self.lineEdit_Line.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
#         self.lineEdit_Line.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
#         self.lineEdit_Line.setObjectName("lineEdit_Line")
#         self.horizontalLayout_3.addWidget(self.lineEdit_Line)

#         self.lineEdit_Kanban_ID = QtWidgets.QLineEdit(self.layoutWidget2)
#         self.lineEdit_Kanban_ID.setAutoFillBackground(False)
#         self.lineEdit_Kanban_ID.setStyleSheet("")
#         self.lineEdit_Kanban_ID.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
#         self.lineEdit_Kanban_ID.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
#         self.lineEdit_Kanban_ID.setObjectName("lineEdit_Kanban_ID")
#         self.horizontalLayout_3.addWidget(self.lineEdit_Kanban_ID)

#         self.layoutWidget_2 = QtWidgets.QWidget(self.tab)
#         self.layoutWidget_2.setGeometry(QtCore.QRect(10, 390, 631, 25))
#         self.layoutWidget_2.setObjectName("layoutWidget_2")
#         self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
#         self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_4.setObjectName("horizontalLayout_4")

#         self.pushButton_Part_ID_Add = QtWidgets.QPushButton(
#             self.layoutWidget_2)
#         self.pushButton_Part_ID_Add.setObjectName("pushButton_Part_ID_Add")
#         self.horizontalLayout_4.addWidget(self.pushButton_Part_ID_Add)
#         self.pushButton_Part_ID_Add.clicked.connect(self.add_part_id)

#         self.pushButton_Part_ID_Del = QtWidgets.QPushButton(
#             self.layoutWidget_2)
#         self.pushButton_Part_ID_Del.setAutoFillBackground(False)
#         self.pushButton_Part_ID_Del.setObjectName("pushButton_Part_ID_Del")
#         self.horizontalLayout_4.addWidget(self.pushButton_Part_ID_Del)
#         self.pushButton_Part_ID_Del.clicked.connect(self.delete_part_id)

#         self.pushButton_Part_NO_Add = QtWidgets.QPushButton(
#             self.layoutWidget_2)
#         self.pushButton_Part_NO_Add.setObjectName("pushButton_Part_NO_Add")
#         self.horizontalLayout_4.addWidget(self.pushButton_Part_NO_Add)
#         self.pushButton_Part_NO_Add.clicked.connect(self.add_part_no)

#         self.pushButton_Part_NO_Del = QtWidgets.QPushButton(
#             self.layoutWidget_2)
#         self.pushButton_Part_NO_Del.setObjectName("pushButton_Part_NO_Del")
#         self.horizontalLayout_4.addWidget(self.pushButton_Part_NO_Del)
#         self.pushButton_Part_NO_Del.clicked.connect(self.delete_part_no)

#         self.pushButton_Line_Add = QtWidgets.QPushButton(self.layoutWidget_2)
#         self.pushButton_Line_Add.setObjectName("pushButton_Line_Add")
#         self.horizontalLayout_4.addWidget(self.pushButton_Line_Add)
#         self.pushButton_Line_Add.clicked.connect(self.add_line)

#         self.pushButton_Line_Del = QtWidgets.QPushButton(self.layoutWidget_2)
#         self.pushButton_Line_Del.setObjectName("pushButton_Line_Del")
#         self.horizontalLayout_4.addWidget(self.pushButton_Line_Del)
#         self.pushButton_Line_Del.clicked.connect(self.delete_line)

#         self.pushButton_Kanban_ID_Add = QtWidgets.QPushButton(
#             self.layoutWidget_2)
#         self.pushButton_Kanban_ID_Add.setObjectName("pushButton_Kanban_ID_Add")
#         self.horizontalLayout_4.addWidget(self.pushButton_Kanban_ID_Add)
#         self.pushButton_Kanban_ID_Add.clicked.connect(self.add_kanban)

#         self.pushButton_Kanban_ID_Del = QtWidgets.QPushButton(
#             self.layoutWidget_2)
#         self.pushButton_Kanban_ID_Del.setObjectName("pushButton_Kanban_ID_Del")
#         self.horizontalLayout_4.addWidget(self.pushButton_Kanban_ID_Del)
#         self.pushButton_Kanban_ID_Del.clicked.connect(self.delete_kanban)

# ##################################################################

#         self.tabWidget.addTab(self.tab, "")
#         self.tab_2 = QtWidgets.QWidget()
#         self.tab_2.setObjectName("tab_2")

#         self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
#         self.lineEdit_3.setGeometry(QtCore.QRect(150, 10, 341, 31))
#         self.lineEdit_3.setObjectName("lineEdit_3")
#         reg_ex = QRegExp("[0-9]+.?[0-9]{,2}")
#         input_validator = QRegExpValidator(reg_ex, self.lineEdit_3)
#         self.lineEdit_3.setValidator(input_validator)

#         self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
#         self.tableWidget_2.setGeometry(QtCore.QRect(10, 90, 631, 291))
#         self.tableWidget_2.setObjectName("tableWidget_2")
#         self.tableWidget_2.setRowCount(10)
#         self.tableWidget_2.setColumnCount(3)
#         columns1 = ['Employee_ID', 'Password', 'Create_date']
#         self.tableWidget_2.setHorizontalHeaderLabels(columns1)

#         self.tableWidget_2.horizontalHeader().setSectionResizeMode(
#             0, QtWidgets.QHeaderView.Stretch)
#         self.tableWidget_2.horizontalHeader().setSectionResizeMode(
#             1, QtWidgets.QHeaderView.Stretch)
#         self.tableWidget_2.horizontalHeader().setSectionResizeMode(
#             2, QtWidgets.QHeaderView.Stretch)

#         conn5 = sqlite3.connect('qr_code.db')

#         result1 = conn5.execute("SELECT * FROM ADMIN_USER")
#         self.tableWidget_2.setRowCount(0)
#         for row_number1, row_data1 in enumerate(result1):
#             self.tableWidget_2.insertRow(row_number1)
#             for column_number1, data1 in enumerate(row_data1):

#                 self.tableWidget_2.setItem(
#                     row_number1, column_number1, QtWidgets.QTableWidgetItem(str(data1)))

#         conn5.commit()

#         conn5.close()

#         self.search2 = QLineEdit(self.tab_2)
#         self.search2.setGeometry(QtCore.QRect(10, 50, 631, 31))
#         self.search2.setObjectName("search2")
#         self.search2.textChanged.connect(self.find_admin_user)
#         self.search2.setStyleSheet("\n"
#                                    "border-style: outset;\n"
#                                    "border-width: 1px;\n"
#                                    "border-radius: 7px;\n"
#                                    "border-color: black;\n"
#                                    "padding: 4px;")

#         self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
#         self.pushButton_2.setGeometry(QtCore.QRect(520, 10, 121, 31))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.pushButton_2.clicked.connect(self.add_admin_user)

#         self.delete_admin_user_button = QtWidgets.QPushButton(self.tab_2)
#         self.delete_admin_user_button.setGeometry(
#             QtCore.QRect(520, 390, 121, 31))
#         self.delete_admin_user_button.setObjectName("delete_admin_user_button")
#         self.delete_admin_user_button.clicked.connect(self.delete_admin_user)

#         self.pushButton_3 = QtWidgets.QPushButton(self)
#         self.pushButton_3.setGeometry(QtCore.QRect(590, 20, 91, 31))
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.pushButton_3.clicked.connect(self.MainWindow)
#         self.pushButton_3.setIcon(
#             self.style().standardIcon(QStyle.SP_ArrowBack))

#         self.label_3 = QtWidgets.QLabel(self.tab_2)
#         self.label_3.setGeometry(QtCore.QRect(10, 10, 121, 31))
#         font = QtGui.QFont()
#         font.setFamily("Mitr")
#         font.setPointSize(12)
#         self.label_3.setFont(font)
#         self.label_3.setObjectName("label_3")

#         self.tabWidget.addTab(self.tab_2, "")
#         self.tabWidget.raise_()
#         self.label_2.raise_()

#         # _translate = QtCore.QCoreApplication.translate
#         # self.setWindowTitle(_translate("Dialog", "Program Qrcode Generator"))
#         # self.label_2.setText(_translate("Dialog", "ADMIN PAGE"))
#         # self.pushButton.setText(_translate("Dialog", "Add"))
#         # self.delete_part_button.setText(_translate("Dialog", "Delete"))
#         # self.lineEdit.setPlaceholderText(_translate("Dialog", "PART ID"))
#         # self.label.setText(_translate("Dialog", "ADD PART"))
#         # self.lineEdit_2.setPlaceholderText(_translate("Dialog", "PART NO"))
#         # self.tabWidget.setTabText(self.tabWidget.indexOf(
#         #     self.tab), _translate("Dialog", "Add Part"))
#         # self.lineEdit_3.setPlaceholderText(
#         #     _translate("Dialog", "Add Employee ID"))
#         # self.pushButton_2.setText(_translate("Dialog", "Add"))
#         # self.delete_admin_user_button.setText(_translate("Dialog", "Delete"))
#         # self.label_3.setText(_translate("Dialog", "ADD Employee ID"))
#         # self.tabWidget.setTabText(self.tabWidget.indexOf(
#         #     self.tab_2), _translate("Dialog", "Add admin"))
#         # self.pushButton_3.setText(_translate("Dialog", "BACK"))
#         # self.search.setPlaceholderText(
#         #     _translate("Dialog", "Type of search..."))
#         # self.search2.setPlaceholderText(
#         #     _translate("Dialog", "Type of search..."))

#         _translate = QtCore.QCoreApplication.translate
#         self.setWindowTitle(_translate("Dialog", "Program Qrcode Generator"))
#         self.label_2.setText(_translate("Dialog", "ADMIN PAGE"))
#         self.label.setText(_translate("Dialog", "Edit Data"))

#         self.lineEdit_search_Part_ID.setPlaceholderText(
#             _translate("Dialog", "Search . . ."))
#         self.lineEdit_search_Part_NO.setPlaceholderText(
#             _translate("Dialog", "Search . . ."))
#         self.lineEdit_search_Line.setPlaceholderText(
#             _translate("Dialog", "Search . . ."))
#         self.lineEdit_search_Kanban_ID.setPlaceholderText(
#             _translate("Dialog", "Search . . ."))
#         self.lineEdit_Part_ID.setPlaceholderText(
#             _translate("Dialog", "Add PART ID"))
#         self.lineEdit_Part_NO.setPlaceholderText(
#             _translate("Dialog", "Add PART NO"))
#         self.lineEdit_Line.setPlaceholderText(_translate("Dialog", "Add LINE"))
#         self.lineEdit_Kanban_ID.setPlaceholderText(
#             _translate("Dialog", "Add KABAN ID"))
#         self.pushButton_Part_ID_Add.setText(_translate("Dialog", "Add"))
#         self.pushButton_Part_ID_Del.setText(_translate("Dialog", "Delete"))
#         self.pushButton_Part_NO_Add.setText(_translate("Dialog", "Add"))
#         self.pushButton_Part_NO_Del.setText(_translate("Dialog", "Delete"))
#         self.pushButton_Line_Add.setText(_translate("Dialog", "Add"))
#         self.pushButton_Line_Del.setText(_translate("Dialog", "Delete"))
#         self.pushButton_Kanban_ID_Add.setText(_translate("Dialog", "Add"))
#         self.pushButton_Kanban_ID_Del.setText(_translate("Dialog", "Delete"))
#         self.tabWidget.setTabText(self.tabWidget.indexOf(
#             self.tab), _translate("Dialog", "Edit Data"))
#         self.lineEdit_3.setPlaceholderText(
#             _translate("Dialog", "Add Employee ID"))
#         self.pushButton_2.setText(_translate("Dialog", "Add"))
#         self.label_3.setText(_translate("Dialog", "ADD Employee ID"))
#         self.delete_admin_user_button.setText(_translate("Dialog", "Delete"))
#         self.search2.setPlaceholderText(
#             _translate("Dialog", "Search . . ."))
#         self.tabWidget.setTabText(self.tabWidget.indexOf(
#             self.tab_2), _translate("Dialog", "Add admin"))
#         self.pushButton_3.setText(_translate("Dialog", "back"))

#         self.clicked = False

#     def paintEvent(self, event):
#         p = QPainter(self)
#         p.fillRect(self.rect(), QColor(128, 128, 128, 128))

#     def mousePressEvent(self, event):
#         self.old_pos = event.screenPos()

#     def mouseMoveEvent(self, event):
#         if self.clicked:
#             dx = self.old_pos.x() - event.screenPos().x()
#             dy = self.old_pos.y() - event.screenPos().y()
#             self.move(self.pos().x() - dx, self.pos().y() - dy)
#         self.old_pos = event.screenPos()
#         self.clicked = True

#         return QWidget.mouseMoveEvent(self, event)

#     def center(self):
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())

#     def MainWindow(self):                                             # <===
#         self.w = MainWindow()
#         self.w.show()
#         self.hide()

#     def findName_part_id(self):
#         name = self.lineEdit_search_Part_ID.text().lower()
#         for row in range(self.tableWidget_Part_ID.rowCount()):
#             item = self.tableWidget_Part_ID.item(row, 0)

#             self.tableWidget_Part_ID.setRowHidden(
#                 row, name not in item.text().lower())

#     def findName_part_no(self):
#         name1 = self.lineEdit_search_Part_NO.text().lower()
#         for row1 in range(self.tableWidget_Part_NO.rowCount()):
#             item1 = self.tableWidget_Part_NO.item(row1, 0)

#             self.tableWidget_Part_NO.setRowHidden(
#                 row1, name1 not in item1.text().lower())

#     def findName_kanban(self):
#         name2 = self.lineEdit_search_Kanban_ID.text().lower()
#         for row2 in range(self.tableWidget_Kanban_ID.rowCount()):
#             item2 = self.tableWidget_Kanban_ID.item(row2, 0)

#             self.tableWidget_Kanban_ID.setRowHidden(
#                 row2, name2 not in item2.text().lower())

#     def findName_line(self):
#         name3 = self.lineEdit_search_Line.text().lower()
#         for row3 in range(self.tableWidget_Line.rowCount()):
#             item3 = self.tableWidget_Line.item(row3, 0)

#             self.tableWidget_Line.setRowHidden(
#                 row3, name3 not in item3.text().lower())

#     def find_admin_user(self):

#         name4 = self.search2.text().lower()
#         for row4 in range(self.tableWidget_2.rowCount()):
#             item4 = self.tableWidget_2.item(row4, 0)
#             # if the search is *not* in the item's text *do not hide* the row
#             self.tableWidget_2.setRowHidden(
#                 row4, name4 not in item4.text().lower())

#     def add_part_id(self):
#         connect = sqlite3.connect('qr_code.db')

#         part_id = self.lineEdit_Part_ID.text()

#         date_now = datetime.now()
#         date_now_convert = date_now.strftime('%d/%m/%Y %H:%M')

#         if part_id == "":
#             popup3 = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
#                                            "แจ้งเตือน",
#                                            "กรุณากรอกข้อมูลให้ครบถ้วน",
#                                            QtWidgets.QMessageBox.Ok,
#                                            self)
#             popup3.show()

#         else:

#             result_check_duplicate = connect.execute(
#                 "SELECT PART_ID FROM PART_ID where PART_ID = ?", (part_id,))

#             check_count = 0
#             for row1 in result_check_duplicate:
#                 check_count = check_count + 1

#             if check_count == 0:

#                 connect.execute("INSERT INTO PART_ID (PART_ID,Create_date) VALUES (? , ?)",
#                                 (part_id, date_now_convert))

#                 connect.commit()

#                 QMessageBox.information(
#                     self,
#                     "Program QR code Generator",
#                     "The part id was successfully added.",
#                     QMessageBox.Ok)

#                 self.load_database_part_id()

#             else:

#                 QMessageBox.critical(
#                     self,
#                     "Part ID is Duplicated.",
#                     "Part ID is already.",
#                     QMessageBox.Ok)

#             connect.close()

#     def add_part_no(self):
#         connect = sqlite3.connect('qr_code.db')

#         part_no = self.lineEdit_Part_NO.text()

#         date_now = datetime.now()
#         date_now_convert = date_now.strftime('%d/%m/%Y %H:%M')

#         if part_no == "":
#             popup3 = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
#                                            "แจ้งเตือน",
#                                            "กรุณากรอกข้อมูลให้ครบถ้วน",
#                                            QtWidgets.QMessageBox.Ok,
#                                            self)
#             popup3.show()

#         else:

#             result_check_duplicate = connect.execute(
#                 "SELECT PART_NO FROM PART_NO where PART_NO = ?", (part_no,))

#             check_count = 0
#             for row1 in result_check_duplicate:
#                 check_count = check_count + 1

#             if check_count == 0:

#                 connect.execute("INSERT INTO PART_NO (PART_NO,Create_date) VALUES (? , ?)",
#                                 (part_no, date_now_convert))

#                 connect.commit()

#                 QMessageBox.information(
#                     self,
#                     "Program QR code Generator",
#                     "The part id was successfully added.",
#                     QMessageBox.Ok)

#                 self.load_database_part_no()

#             else:

#                 QMessageBox.critical(
#                     self,
#                     "Part NO is Duplicated.",
#                     "Part NO is already.",
#                     QMessageBox.Ok)

#             connect.close()

#     def add_line(self):
#         connect = sqlite3.connect('qr_code.db')

#         line = self.lineEdit_Line.text()

#         date_now = datetime.now()
#         date_now_convert = date_now.strftime('%d/%m/%Y %H:%M')

#         if line == "":
#             popup3 = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
#                                            "แจ้งเตือน",
#                                            "กรุณากรอกข้อมูลให้ครบถ้วน",
#                                            QtWidgets.QMessageBox.Ok,
#                                            self)
#             popup3.show()

#         else:

#             result_check_duplicate = connect.execute(
#                 "SELECT LINE FROM LINE where LINE = ?", (line,))

#             check_count = 0
#             for row1 in result_check_duplicate:
#                 check_count = check_count + 1

#             if check_count == 0:

#                 connect.execute("INSERT INTO LINE (LINE,Create_date) VALUES (? , ?)",
#                                 (line, date_now_convert))

#                 connect.commit()

#                 QMessageBox.information(
#                     self,
#                     "Program QR code Generator",
#                     "The LINE was successfully added.",
#                     QMessageBox.Ok)

#                 self.load_database_line()

#             else:

#                 QMessageBox.critical(
#                     self,
#                     "LINE is Duplicated.",
#                     "LINE is already.",
#                     QMessageBox.Ok)

#             connect.close()

#     def add_kanban(self):
#         connect = sqlite3.connect('qr_code.db')

#         kanban = self.lineEdit_Kanban_ID.text()

#         date_now = datetime.now()
#         date_now_convert = date_now.strftime('%d/%m/%Y %H:%M')

#         if kanban == "":
#             popup3 = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
#                                            "แจ้งเตือน",
#                                            "กรุณากรอกข้อมูลให้ครบถ้วน",
#                                            QtWidgets.QMessageBox.Ok,
#                                            self)
#             popup3.show()

#         else:

#             result_check_duplicate = connect.execute(
#                 "SELECT KANBAN_ID FROM KANBAN_ID where KANBAN_ID = ?", (kanban,))

#             check_count = 0
#             for row1 in result_check_duplicate:
#                 check_count = check_count + 1

#             if check_count == 0:

#                 connect.execute("INSERT INTO KANBAN_ID (KANBAN_ID,Create_date) VALUES (? , ?)",
#                                 (kanban, date_now_convert))

#                 connect.commit()

#                 QMessageBox.information(
#                     self,
#                     "Program QR code Generator",
#                     "The KANBAN_ID was successfully added.",
#                     QMessageBox.Ok)

#                 self.load_database_kanban()

#             else:

#                 QMessageBox.critical(
#                     self,
#                     "KANBAN_ID is Duplicated.",
#                     "KANBAN_ID is already.",
#                     QMessageBox.Ok)

#             connect.close()

#     def add_admin_user(self):
#         conn6 = sqlite3.connect('qr_code.db')
#         admin_new = self.lineEdit_3.text()

#         # password_salt = os.urandom(32).hex()
#         password = admin_new

#         result_check_duplicate = conn6.execute(
#             "SELECT Employee_ID FROM ADMIN_USER where Employee_ID = ?", (admin_new,))

#         check_count = 0
#         for row1 in result_check_duplicate:
#             check_count = check_count + 1

#         if check_count == 0:

#             hash = hashlib.sha512()
#             # hash.update(('%s%s' % (password_salt, password)).encode('utf-8'))
#             hash.update(('%s' % (password)).encode('utf-8'))
#             password_hash = hash.hexdigest()

#             conn6.execute("INSERT INTO ADMIN_USER (Employee_ID,Password,Time_to_update) \
#                 VALUES (? , ? , ?)", (admin_new, password_hash, datetime.now()))

#             result1 = conn6.execute("SELECT * FROM ADMIN_USER")
#             self.tableWidget_2.setRowCount(0)
#             for row_number1, row_data1 in enumerate(result1):
#                 self.tableWidget_2.insertRow(row_number1)
#                 for column_number1, data1 in enumerate(row_data1):

#                     self.tableWidget_2.setItem(
#                         row_number1, column_number1, QtWidgets.QTableWidgetItem(str(data1)))

#             conn6.commit()

#             QMessageBox.information(
#                 self,
#                 "Program QR code Generator",
#                 "The new admin was successfully added.",
#                 QMessageBox.Ok)
#         else:

#             QMessageBox.critical(
#                 self,
#                 "Employee ID is Duplicated.",
#                 "Employee ID is already.",
#                 QMessageBox.Ok)

#         conn6.close()

#     def delete_admin_user(self):

#         msgBox = QMessageBox(self)
#         msgBox.setIcon(QMessageBox.Warning)
#         msgBox.setText("Are you sure to delete ?")
#         msgBox.setWindowTitle("Delete Data Warning")
#         msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

#         returnValue = msgBox.exec()
#         if returnValue == QMessageBox.Ok:
#             conn4 = sqlite3.connect('qr_code.db')

#             result = conn4.execute("SELECT * FROM ADMIN_USER")

#             for row_data in enumerate(result):
#                 if row_data[0] == self.tableWidget_2.currentRow():
#                     data = row_data[1]
#                     employee_id = data[0]
#                     pass_word = data[1]
#                     time_create = data[2]
#                     conn4.execute("DELETE FROM ADMIN_USER WHERE Employee_ID=? AND Password=? AND Time_to_update=?",
#                                   (employee_id, pass_word, time_create,))
#                     conn4.commit()

#                     self.load_database_admin()

#             QMessageBox.information(
#                 self,
#                 "Program QR code Generator",
#                 "The admin was successfully deleted.",
#                 QMessageBox.Ok)

#             conn4.close()

#     def delete_part_id(self):
#         msgBox = QMessageBox(self)
#         msgBox.setIcon(QMessageBox.Warning)
#         msgBox.setText("Are you sure to delete ?")
#         msgBox.setWindowTitle("Delete Data Warning")
#         msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#         # msgBox.buttonClicked.connect(msgButtonClick)

#         returnValue = msgBox.exec()
#         if returnValue == QMessageBox.Ok:

#             conne = sqlite3.connect('qr_code.db')

#             result1 = conne.execute("SELECT * FROM PART_ID")

#             for row_data in enumerate(result1):
#                 if row_data[0] == self.tableWidget_Part_ID.currentRow():
#                     data = row_data[1]
#                     part_id = data[0]
#                     create_date = data[1]

#                     conne.execute("DELETE FROM PART_ID WHERE Part_ID=? AND Create_date=?",
#                                   (part_id, create_date,))
#                     conne.commit()

#                     self.load_database_part_id()

#             QMessageBox.information(
#                 self,
#                 "Program QR code Generator",
#                 "The part id was successfully deleted.",
#                 QMessageBox.Ok)

#             conne.close()

#     def delete_part_no(self):
#         msgBox = QMessageBox(self)
#         msgBox.setIcon(QMessageBox.Warning)
#         msgBox.setText("Are you sure to delete ?")
#         msgBox.setWindowTitle("Delete Data Warning")
#         msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#         # msgBox.buttonClicked.connect(msgButtonClick)

#         returnValue = msgBox.exec()
#         if returnValue == QMessageBox.Ok:

#             conne = sqlite3.connect('qr_code.db')

#             result1 = conne.execute("SELECT * FROM PART_NO")

#             for row_data in enumerate(result1):
#                 if row_data[0] == self.tableWidget_Part_NO.currentRow():
#                     data = row_data[1]
#                     part_no = data[0]
#                     create_date = data[1]

#                     conne.execute("DELETE FROM PART_NO WHERE PART_NO=? AND Create_date=?",
#                                   (part_no, create_date,))
#                     conne.commit()

#                     self.load_database_part_no()

#             QMessageBox.information(
#                 self,
#                 "Program QR code Generator",
#                 "The part_no was successfully deleted.",
#                 QMessageBox.Ok)

#             conne.close()

#     def delete_line(self):
#         msgBox = QMessageBox(self)
#         msgBox.setIcon(QMessageBox.Warning)
#         msgBox.setText("Are you sure to delete ?")
#         msgBox.setWindowTitle("Delete Data Warning")
#         msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#         # msgBox.buttonClicked.connect(msgButtonClick)

#         returnValue = msgBox.exec()
#         if returnValue == QMessageBox.Ok:

#             conne = sqlite3.connect('qr_code.db')

#             result1 = conne.execute("SELECT * FROM LINE")

#             for row_data in enumerate(result1):
#                 if row_data[0] == self.tableWidget_Line.currentRow():
#                     data = row_data[1]
#                     line = data[0]
#                     create_date = data[1]

#                     conne.execute("DELETE FROM LINE WHERE LINE=? AND Create_date=?",
#                                   (line, create_date,))
#                     conne.commit()

#                     self.load_database_line()

#             QMessageBox.information(
#                 self,
#                 "Program QR code Generator",
#                 "The line was successfully deleted.",
#                 QMessageBox.Ok)

#             conne.close()

#     def delete_kanban(self):
#         msgBox = QMessageBox(self)
#         msgBox.setIcon(QMessageBox.Warning)
#         msgBox.setText("Are you sure to delete ?")
#         msgBox.setWindowTitle("Delete Data Warning")
#         msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#         # msgBox.buttonClicked.connect(msgButtonClick)

#         returnValue = msgBox.exec()
#         if returnValue == QMessageBox.Ok:

#             conne = sqlite3.connect('qr_code.db')

#             result1 = conne.execute("SELECT * FROM KANBAN_ID")

#             for row_data in enumerate(result1):
#                 if row_data[0] == self.tableWidget_Kanban_ID.currentRow():
#                     data = row_data[1]
#                     kanban_id = data[0]
#                     create_date = data[1]

#                     conne.execute("DELETE FROM KANBAN_ID WHERE KANBAN_ID=? AND Create_date=?",
#                                   (kanban_id, create_date,))
#                     conne.commit()

#                     self.load_database_kanban()

#             QMessageBox.information(
#                 self,
#                 "Program QR code Generator",
#                 "The kanban_id was successfully deleted.",
#                 QMessageBox.Ok)

#             conne.close()

#     def load_database_part_id(self):
#         while self.tableWidget_Part_ID.rowCount() > 0:
#             self.tableWidget_Part_ID.removeRow(0)
#         conn4 = sqlite3.connect('qr_code.db')
#         result = conn4.execute("SELECT * FROM PART_ID")
#         self.tableWidget_Part_ID.setRowCount(0)
#         for row_number, row_data in enumerate(result):
#             self.tableWidget_Part_ID.insertRow(row_number)
#             for column_number, data in enumerate(row_data):
#                 self.tableWidget_Part_ID.setItem(
#                     row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

#         conn4.commit()

#     def load_database_part_no(self):
#         while self.tableWidget_Part_NO.rowCount() > 0:
#             self.tableWidget_Part_NO.removeRow(0)
#         conn4 = sqlite3.connect('qr_code.db')
#         result = conn4.execute("SELECT * FROM PART_NO")
#         self.tableWidget_Part_NO.setRowCount(0)
#         for row_number, row_data in enumerate(result):
#             self.tableWidget_Part_NO.insertRow(row_number)
#             for column_number, data in enumerate(row_data):
#                 self.tableWidget_Part_NO.setItem(
#                     row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

#         conn4.commit()

#     def load_database_line(self):
#         while self.tableWidget_Line.rowCount() > 0:
#             self.tableWidget_Line.removeRow(0)
#         conn4 = sqlite3.connect('qr_code.db')
#         result = conn4.execute("SELECT * FROM LINE")
#         self.tableWidget_Line.setRowCount(0)
#         for row_number, row_data in enumerate(result):
#             self.tableWidget_Line.insertRow(row_number)
#             for column_number, data in enumerate(row_data):
#                 self.tableWidget_Line.setItem(
#                     row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

#         conn4.commit()

#     def load_database_kanban(self):
#         while self.tableWidget_Kanban_ID.rowCount() > 0:
#             self.tableWidget_Kanban_ID.removeRow(0)
#         conn4 = sqlite3.connect('qr_code.db')
#         result = conn4.execute("SELECT * FROM KANBAN_ID")
#         self.tableWidget_Kanban_ID.setRowCount(0)
#         for row_number, row_data in enumerate(result):
#             self.tableWidget_Kanban_ID.insertRow(row_number)
#             for column_number, data in enumerate(row_data):
#                 self.tableWidget_Kanban_ID.setItem(
#                     row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

#         conn4.commit()

#     def load_database_admin(self):
#         while self.tableWidget_2.rowCount() > 0:
#             self.tableWidget_2.removeRow(0)
#         conn5 = sqlite3.connect('qr_code.db')
#         result1 = conn5.execute("SELECT * FROM ADMIN_USER")
#         self.tableWidget_2.setRowCount(0)
#         for row_number1, row_data1 in enumerate(result1):
#             self.tableWidget_2.insertRow(row_number1)
#             for column_number1, data1 in enumerate(row_data1):

#                 self.tableWidget_2.setItem(
#                     row_number1, column_number1, QtWidgets.QTableWidgetItem(str(data1)))

#         conn5.commit()

#         conn5.close()


class Window2(QWidget):
    def __init__(self):

        QWidget.__init__(self)
        self.setWindowTitle("Program Qrcode Generator")
        self.setWindowIcon(QtGui.QIcon('qr-code-generator.ico'))
        Top = 200
        Left = 200
        Width = 700
        Hight = 520
        self.setGeometry(Left, Top, Width, Hight)
        self.center()
        self.setWindowFlags(Qt.Widget | Qt.FramelessWindowHint)
        radius = 10
        base = self.rect()
        ellipse = QRect(0, 0, 2 * radius, 2 * radius)

        base_region = QRegion(base.adjusted(radius, 0, -radius, 0))
        base_region |= QRegion(base.adjusted(0, radius, 0, -radius))

        base_region |= QRegion(ellipse, QRegion.Ellipse)
        ellipse.moveTopRight(base.topRight())
        base_region |= QRegion(ellipse, QRegion.Ellipse)
        ellipse.moveBottomRight(base.bottomRight())
        base_region |= QRegion(ellipse, QRegion.Ellipse)
        ellipse.moveBottomLeft(base.bottomLeft())
        base_region |= QRegion(ellipse, QRegion.Ellipse)

        self.setMask(base_region)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(60, 50, 581, 431))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(5)
        self.frame.setMidLineWidth(6)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(190, 110, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(150, 270, 261, 31))
        # self.pushButton.setStyleSheet("background-color:black;\n"
        #                               "border-style: outset;\n"
        #                               "color:white;\n"
        #                               "border-radius: 7px;\n"
        #                               "border-color: black;\n"
        #                               "padding: 4px;"
        #                               )
        self.pushButton.setStyleSheet("background-color:black;\n"
                                      "border-style: outset;\n"
                                      "color:white;\n"
                                      "border-radius: 7px;\n"
                                      "border-color: black;\n"
                                      "padding: 4px;")
        # self.pushButton.setStyleSheet("QPushButton::pressed"
        #                               "{"
        #                               "background-color : red;"
        #                               "}"
        #                               "QPushButton::hover"
        #                               "{"
        #                               "background-color : lightgreen;"
        #                               "}")

        self.pushButton.setStyleSheet("QPushButton#pushButton {"
                                      "background-color:black;\n"
                                      "border-style: outset;\n"
                                      "color:white;\n"
                                      "border-radius: 7px;\n"
                                      "border-color: black;\n"
                                      "padding: 4px;"
                                      "}"

                                      "QPushButton#pushButton:hover {"
                                      "background-color:grey;\n"
                                      "border-style: outset;\n"
                                      "color:white;\n"
                                      "border-radius: 7px;\n"
                                      "border-color: black;\n"
                                      "padding: 4px;"
                                      "}"

                                      "QPushButton#pushButton:pressed {"
                                      "background-color:white;\n"
                                      "border-style: outset;\n"
                                      "color:black;\n"
                                      "border-radius: 7px;\n"
                                      "border-color: black;\n"
                                      "padding: 4px;"
                                      "}")

        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Login_check)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 370, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.MainWindow)
        self.pushButton_2.setIcon(
            self.style().standardIcon(QStyle.SP_ArrowBack))

        self.textUsername = QtWidgets.QLineEdit(self.frame)
        self.textUsername.setGeometry(QtCore.QRect(150, 170, 261, 31))
        self.textUsername.setStyleSheet("\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 7px;\n"
                                        "border-color: black;\n"
                                        "padding: 4px;")
        self.textUsername.setObjectName("textUsername")

        self.textPassword = QtWidgets.QLineEdit(self.frame)
        self.textPassword.setGeometry(QtCore.QRect(150, 220, 261, 31))
        self.textPassword.setStyleSheet("\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 7px;\n"
                                        "border-color: black;\n"
                                        "padding: 4px;")
        self.textPassword.setObjectName("textPassword")
        self.textPassword.setEchoMode(QtWidgets.QLineEdit.Password)

        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "ADMIN LOGIN"))
        self.pushButton.setText(_translate("Dialog", "LOG IN"))

        self.pushButton_2.setText(_translate("Dialog", "BACK"))
        self.textUsername.setPlaceholderText(_translate("Dialog", "Username"))
        self.textPassword.setPlaceholderText(_translate("Dialog", "Password"))

        self.clicked = False

    def paintEvent(self, event):
        p = QPainter(self)
        p.fillRect(self.rect(), QColor(128, 128, 128, 128))

    def mousePressEvent(self, event):
        self.old_pos = event.screenPos()

    def mouseMoveEvent(self, event):
        if self.clicked:
            dx = self.old_pos.x() - event.screenPos().x()
            dy = self.old_pos.y() - event.screenPos().y()
            self.move(self.pos().x() - dx, self.pos().y() - dy)
        self.old_pos = event.screenPos()
        self.clicked = True

        return QWidget.mouseMoveEvent(self, event)

    def MainWindow(self):                                             # <===
        self.w = MainWindow()
        self.w.show()
        self.hide()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def Login_check(self):

        global textUsername

        textUsername = self.textUsername.text()
        textPassword = self.textPassword.text()

        if textUsername == "" and textPassword == "":
            popup3 = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                                           "แจ้งเตือน",
                                           "กรุณากรอก Username Password",
                                           QtWidgets.QMessageBox.Ok,
                                           self)

            popup3.show()

        else:

            hash = hashlib.sha512()
            # hash.update(('%s%s' % (password_salt, password)).encode('utf-8'))
            hash.update(('%s' % (textPassword)).encode('utf-8'))
            password_hash = hash.hexdigest()

            conn2 = sqlite3.connect('qr_code.db')
            username_db = conn2.execute(
                "SELECT Employee_ID,Password from ADMIN_USER Where Employee_ID = ?", (textUsername,))

            check_count = 0
            for row1 in username_db:
                check_count = check_count + 1

            conn2.commit()

            conn2.close()

            if check_count > 0:
                conn3 = sqlite3.connect('qr_code.db')
                username_db1 = conn3.execute(
                    "SELECT Employee_ID,Password from ADMIN_USER Where Employee_ID = ?", (textUsername,))
                user_for_check = []
                pass_for_check = []

                for row3 in username_db1:
                    print("hello")
                    user_for_check.append(row3[0])
                    pass_for_check.append(row3[1])

                if textUsername == user_for_check[0] and password_hash == pass_for_check[0]:
                    # if textUsername == user_for_check[0]:

                    QMessageBox.information(
                        self,
                        "Program QR code Generator",
                        "Welcome to ADMIN PAGE",
                        QMessageBox.Ok)

                    global Employee_on
                    Employee_on = textUsername

                    self.w = admin_page()
                    self.w.show()
                    self.hide()

                else:
                    popup1 = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                                                   "แจ้งเตือน",
                                                   "Username and Password is wrong! please try again.",
                                                   QtWidgets.QMessageBox.Ok,
                                                   self)
                    popup1.show()
                conn3.commit()

                conn3.close()
            else:
                popup2 = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                                               "แจ้งเตือน",
                                               "Username and Password is wrong! please try again.",
                                               QtWidgets.QMessageBox.Ok,
                                               self)
                popup2.show()


class MainWindow(QWidget):

    def __init__(self):

        global textEdit_calendarEdit
        global textEdit_timeEdit
        textEdit_calendarEdit = datetime.today().strftime('%Y-%m-%d')
        textEdit_timeEdit = datetime.today().strftime('%H:%M')
        QWidget.__init__(self)
        self.setWindowTitle("Program Qrcode Generator")
        self.setWindowIcon(QtGui.QIcon('qr-code-generator.ico'))
        Top = 0
        Left = 0
        Width = 700
        Hight = 520
        self.setGeometry(Left, Top, Width, Hight)
        self.center()
        self.setWindowFlags(Qt.FramelessWindowHint)
        radius = 10
        base = self.rect()
        ellipse = QRect(0, 0, 2 * radius, 2 * radius)

        base_region = QRegion(base.adjusted(radius, 0, -radius, 0))
        base_region |= QRegion(base.adjusted(0, radius, 0, -radius))

        base_region |= QRegion(ellipse, QRegion.Ellipse)
        ellipse.moveTopRight(base.topRight())
        base_region |= QRegion(ellipse, QRegion.Ellipse)
        ellipse.moveBottomRight(base.bottomRight())
        base_region |= QRegion(ellipse, QRegion.Ellipse)
        ellipse.moveBottomLeft(base.bottomLeft())
        base_region |= QRegion(ellipse, QRegion.Ellipse)

        self.setMask(base_region)
        # shadow = QGraphicsDropShadowEffect(blurRadius=1, xOffset=3, yOffset=3)
        # self.setGraphicsEffect(shadow)

        # # adding shadow to the label
        # self.QWidget.setGraphicsEffect(shadow)

        self.score = 0
        self.counter = 0
        self.test = 0
        self.question_prompts = []

        self.textEdit_EmpNo = QtWidgets.QLineEdit(self)
        self.textEdit_EmpNo.setGeometry(QtCore.QRect(160, 110, 151, 31))
        self.textEdit_EmpNo.setObjectName("textEdit_EmpNo")
        reg_ex = QRegExp("[0-9]+.?[0-9]{,2}")
        input_validator = QRegExpValidator(reg_ex, self.textEdit_EmpNo)
        self.textEdit_EmpNo.setValidator(input_validator)

        conz = sqlite3.connect('qr_code.db')
        cursor = conz.execute("SELECT * from LINE")
        line_autocomplete = []

        for row in cursor:

            line_autocomplete.append(row[0])

        completer_line = QCompleter(line_autocomplete)
        completer_line.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.textEdit_Line = QtWidgets.QLineEdit(self)
        self.textEdit_Line.setGeometry(QtCore.QRect(160, 160, 151, 31))
        self.textEdit_Line.setObjectName("textEdit_Line")
        self.textEdit_Line.setCompleter(completer_line)

        conz.close()

        conn1 = sqlite3.connect('qr_code.db')
        cursor1 = conn1.execute("SELECT DISTINCT PART_NO from PART_KANBAN ")
        part_no_autocomplete = []

        for row1 in cursor1:
            part_no_autocomplete.append(row1[0])

        completer_part_no = QCompleter(part_no_autocomplete)
        completer_part_no.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.textEdit_PartNo = QtWidgets.QLineEdit(self)
        self.textEdit_PartNo.setGeometry(QtCore.QRect(160, 310, 151, 31))
        self.textEdit_PartNo.setObjectName("textEdit_PartNo")
        self.textEdit_PartNo.setCompleter(completer_part_no)
        # self.textEdit_PartNo.textChanged.connect(self.change_state2)

        conn1.close()

        conn = sqlite3.connect('qr_code.db')

        cursor = conn.execute("SELECT DISTINCT PART_ID from PART_KANBAN")

        part_id_autocomplete = []

        for row in cursor:

            part_id_autocomplete.append(row[0])

        completer_part_id = QCompleter(part_id_autocomplete)
        completer_part_id.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.textEdit_PartId = QtWidgets.QLineEdit(self)
        self.textEdit_PartId.setGeometry(QtCore.QRect(160, 360, 151, 31))
        self.textEdit_PartId.setObjectName("textEdit_PartId")
        self.textEdit_PartId.setCompleter(completer_part_id)
        # self.textEdit_PartId.textChanged.connect(self.change_state1)

        conn.close()

        conn2 = sqlite3.connect('qr_code.db')
        cursor = conn2.execute("SELECT KANBAN_ID from PART_KANBAN ")
        kanban_id_autocomplete = []

        for row in cursor:

            kanban_id_autocomplete.append(row[0])

        completer_kanban_id = QCompleter(kanban_id_autocomplete)
        completer_kanban_id.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.textEdit_KanbanId = QtWidgets.QLineEdit(self)
        self.textEdit_KanbanId.setGeometry(QtCore.QRect(160, 260, 151, 31))
        self.textEdit_KanbanId.setObjectName("textEdit_KanbanId")
        self.textEdit_KanbanId.setCompleter(completer_kanban_id)
        self.textEdit_KanbanId.textChanged.connect(self.change_state)
        self.textEdit_KanbanId.setStyleSheet(
            "border: 2px solid black;")

        conn2.close()

        self.textEdit_AmountStart = QtWidgets.QLineEdit(self)
        self.textEdit_AmountStart.setGeometry(QtCore.QRect(320, 460, 51, 31))
        self.textEdit_AmountStart.setObjectName("textEdit_AmountStart")
        reg_ex = QRegExp("[0-9]+.?[0-9]{,2}")
        input_validator = QRegExpValidator(reg_ex, self.textEdit_AmountStart)
        self.textEdit_AmountStart.setValidator(input_validator)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 110, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(350, 120, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(350, 360, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(20, 260, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(20, 310, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(20, 360, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(20, 460, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_setup = QtWidgets.QLabel(self)
        self.label_setup.setGeometry(QtCore.QRect(20, 420, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_setup.setFont(font)
        self.label_setup.setObjectName("label_setup")

        self.label_10 = QtWidgets.QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(260, 460, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.timeEdit = QtWidgets.QTimeEdit(self)
        self.timeEdit.setGeometry(QtCore.QRect(520, 360, 141, 31))
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setObjectName("timeEdit")

        self.textEdit_Amount = QtWidgets.QLineEdit(self)
        self.textEdit_Amount.setGeometry(QtCore.QRect(180, 460, 51, 31))
        self.textEdit_Amount.setObjectName("textEdit_Amount")
        reg_ex = QRegExp("[0-9]+.?[0-9]{,2}")
        input_validator = QRegExpValidator(reg_ex, self.textEdit_Amount)
        self.textEdit_Amount.setValidator(input_validator)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(500, 50, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.window2)
        self.pushButton.setIcon(
            self.style().standardIcon(QStyle.SP_VistaShield))

        self.calendarWidget = QtWidgets.QCalendarWidget(self)
        self.calendarWidget.setGeometry(QtCore.QRect(350, 160, 312, 183))
        self.calendarWidget.setMinimumSize(QtCore.QSize(312, 0))
        self.calendarWidget.setMaximumSize(QtCore.QSize(800, 600))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.selectionChanged.connect(self.calendar_date)

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(160, 211, 151, 31))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.comboBox.setObjectName("comboBox")
        shift = ["A", "B"]
        # adding list of items to combo box
        self.comboBox.addItems(shift)

        self.printButton = QtWidgets.QPushButton(self)
        self.printButton.setGeometry(QtCore.QRect(390, 460, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.printButton.setFont(font)
        self.printButton.setObjectName("printButton")
        self.printButton.clicked.connect(self.print_function)
        self.printButton.setIcon(
            self.style().standardIcon(QStyle.SP_DialogApplyButton))

        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.exit_app)
        self.pushButton_3.setStyleSheet("background: red; color:white;")

        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(570, 460, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.export_csv)
        self.pushButton_4.setIcon(
            self.style().standardIcon(QStyle.SP_DialogSaveButton))

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(20, 80, 651, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(20, 400, 651, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(20, 40, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(20)
        # font.setUnderline(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(500, 115, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Mitr")
        font.setPointSize(15)
        font.setUnderline(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 701, 101))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color:cornflowerblue")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Program Qrcode Generator"))
        self.label.setText(_translate("Dialog", "รหัสพนักงาน"))
        self.label_2.setText(_translate("Dialog", "Line"))
        self.label_3.setText(_translate("Dialog", "Shift"))
        self.label_4.setText(_translate("Dialog", "Select Date :"))
        self.label_5.setText(_translate("Dialog", "Select Time : "))
        self.label_6.setText(_translate("Dialog", "Kanban ID"))
        self.label_7.setText(_translate("Dialog", "Part No."))
        self.label_8.setText(_translate("Dialog", "Part ID"))
        self.label_9.setText(_translate("Dialog", "จำนวนที่ต้องการ"))
        self.label_setup.setText(_translate("Dialog", "Setup Printer"))
        self.label_10.setText(_translate("Dialog", "เริ่มที่"))
        self.timeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.timeEdit.setDisplayFormat(_translate("Dialog", "HH:mm"))
        self.pushButton.setText(_translate("Dialog", "Admin Login"))
        self.printButton.setText(_translate("Dialog", "Print"))
        self.pushButton_3.setText(_translate("Dialog", "X"))
        self.pushButton_4.setText(_translate("Dialog", "Export log"))
        self.label_11.setText(_translate("Dialog", "Qrcode Generator"))
        self.label_12.setText(_translate(
            "Dialog", datetime.today().strftime('%Y-%m-%d')))
        self.clicked = False
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.label_11.raise_()
        self.label_12.raise_()

    def change_state(self):
        textEdit_KanbanId_text = self.textEdit_KanbanId.text()
        conn10 = sqlite3.connect('qr_code.db')

        cursor = conn10.execute(
            "SELECT * from PART_KANBAN WHERE KANBAN_ID =? ", (textEdit_KanbanId_text,))

        for row in cursor:

            self.textEdit_PartId.setText(row[2])
            self.textEdit_PartNo.setText(row[1])

        conn10.close()

    def paintEvent(self, event):
        p = QPainter(self)
        p.fillRect(self.rect(), QColor(128, 128, 128, 128))

    def mousePressEvent(self, event):
        self.old_pos = event.screenPos()

    def mouseMoveEvent(self, event):
        if self.clicked:
            dx = self.old_pos.x() - event.screenPos().x()
            dy = self.old_pos.y() - event.screenPos().y()
            self.move(self.pos().x() - dx, self.pos().y() - dy)
        self.old_pos = event.screenPos()
        self.clicked = True

        return QWidget.mouseMoveEvent(self, event)

    def window2(self):                                             # <===
        self.w = Window2()
        self.w.show()
        self.hide()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def calendar_date(self):
        global textEdit_calendarEdit

        dateselected = self.calendarWidget.selectedDate()
        textEdit_calendarEdit = str(dateselected.toPyDate())
        self.label_12.setText(textEdit_calendarEdit)
        # print('{0}/{1}/{2}'.format(qDate.month(), qDate.day(), qDate.year()))
        # print(f'Day Number of the year: {qDate.dayOfYear()}')
        # print(f'Day Number of the week: {qDate.dayOfWeek()}')

    def export_csv(self):
        # conn = sqlite3.connect('qr_code.db')
        # conn.text_factory = str ## my current (failed) attempt to resolve this
        # cur = conn.cursor()
        # data = cur.execute("SELECT * FROM QRCODE")

        # with open('qr_code_log.csv', 'wb') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(['Employee_ID', 'Kanban_ID', 'Line','Part_ID','Part_NO','Time_select','Shift','Date_select','Date_time_stamp','Amount','Amount_start'])
        #     writer.writerows(data)

        inpsql3 = sqlite3.connect('qr_code.db')
        sql3_cursor = inpsql3.cursor()
        sql3_cursor.execute('SELECT * FROM QRCODE')

        file_name = "qr_code_log"

        # foo_dir = QFileDialog.getSaveFileName(
        #     # self, 'Select directory for save file csv', ".csv")
        #     self, "Save csv file", "", "Csv Files (*.csv)", options=QFileDialog.setLabelText(file_name))
        fileName = QFileDialog.getSaveFileName(self, "Save",
                                                     "qr_code_log.csv",
                                                     "Excel (*.csv)")
        print(fileName)
        fileName_use = fileName[0]
        print('>>>>>>>', fileName_use)
        if fileName_use:
            # for fileName in fileName:
            with open(fileName_use, 'w') as out_csv_file:
                csv_out = csv.writer(out_csv_file)
                # write header
                csv_out.writerow([d[0] for d in sql3_cursor.description])
                # write data
                for result in sql3_cursor:
                    csv_out.writerow(result)
            message = "Export file CSV on directory  \n" + \
                fileName_use + "\n" + "have successfully."
            QMessageBox.information(
                self,
                "CSV exported successfully.",
                message,
                QMessageBox.Ok)

        inpsql3.close()

    def print_function(self):
        global textEdit_EmpNo_text
        global textEdit_Amount_text
        global textEdit_AmountStart_text
        global textEdit_KanbanId_text
        global textEdit_Line_text
        global textEdit_PartId_text
        global textEdit_PartNo_text
        global textEdit_timeEdit
        global textEdit_comboBox
        global textEdit_calendarEdit

        textEdit_comboBox = self.comboBox.currentText()
        textEdit_EmpNo_text = self.textEdit_EmpNo.text()
        textEdit_Amount_text = self.textEdit_Amount.text()
        textEdit_AmountStart_text = self.textEdit_AmountStart.text()
        textEdit_KanbanId_text = self.textEdit_KanbanId.text()
        textEdit_Line_text = self.textEdit_Line.text()
        textEdit_PartId_text = self.textEdit_PartId.text()
        textEdit_PartNo_text = self.textEdit_PartNo.text()
        textEdit_timeEdit = self.timeEdit.time().toString()

        if textEdit_EmpNo_text == "" or textEdit_Amount_text == "" or textEdit_AmountStart_text == "" or textEdit_KanbanId_text == "" or textEdit_PartId_text == "" or textEdit_PartNo_text == "":
            print("Empty Value Not Allowed")

            popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                                          "แจ้งเตือน",
                                          "กรุณากรอกข้อมูลให้ครบถ้วน",
                                          QtWidgets.QMessageBox.Ok,
                                          self)
            popup.show()

        else:

            conn_forcheck = sqlite3.connect('qr_code.db')
            result_check_part_kanban = conn_forcheck.execute(
                "SELECT * FROM PART_KANBAN where KANBAN_ID=? AND PART_NO=? AND PART_ID = ?", (textEdit_KanbanId_text, textEdit_PartNo_text, textEdit_PartId_text,))
            result_check_part_id = conn_forcheck.execute(
                "SELECT PART_ID FROM PART_KANBAN where PART_ID = ?", (textEdit_PartId_text,))
            result_check_part_no = conn_forcheck.execute(
                "SELECT PART_NO FROM PART_KANBAN where PART_NO = ?", (textEdit_PartNo_text,))
            result_check_line = conn_forcheck.execute(
                "SELECT LINE FROM LINE where LINE = ?", (textEdit_Line_text,))
            result_check_kanban = conn_forcheck.execute(
                "SELECT KANBAN_ID FROM PART_KANBAN where KANBAN_ID = ?", (textEdit_KanbanId_text,))

            check_count_part_id = 0
            check_count_part_no = 0
            check_count_line = 0
            check_count_kanban = 0
            check_count_part_kanban = 0
            for row1 in result_check_part_id:
                check_count_part_id = check_count_part_id + 1
            for row2 in result_check_part_no:
                check_count_part_no = check_count_part_no + 1
            for row3 in result_check_line:
                check_count_line = check_count_line + 1
            for row4 in result_check_part_kanban:
                check_count_part_kanban = check_count_part_kanban + 1
            for row5 in result_check_kanban:
                check_count_kanban = check_count_kanban + 1

            if check_count_part_kanban == 0:

                # if check_count_kanban == 0:

                #     if check_count_kanban == 0 and check_count_part_no == 0:
                #         self.textEdit_KanbanId.setFocus()
                #         self.textEdit_KanbanId.setStyleSheet(
                #             "border: 1px solid red;")
                #         self.textEdit_PartNo.setFocus()
                #         self.textEdit_PartNo.setStyleSheet(
                #             "border: 1px solid red;")
                #     elif check_count_kanban == 0 and check_count_part_id == 0:
                #         self.textEdit_KanbanId.setFocus()
                #         self.textEdit_KanbanId.setStyleSheet(
                #             "border: 1px solid red;")
                #         self.textEdit_PartId.setFocus()
                #         self.textEdit_PartId.setStyleSheet(
                #             "border: 1px solid red;")
                #     else:
                #         self.textEdit_KanbanId.setFocus()
                #         self.textEdit_KanbanId.setStyleSheet(
                #             "border: 1px solid red;")

                # elif check_count_part_no == 0:
                #     if check_count_part_id == 0 and check_count_part_no == 0:
                #         self.textEdit_PartId.setFocus()
                #         self.textEdit_PartId.setStyleSheet(
                #             "border: 1px solid red;")
                #         self.textEdit_PartNo.setFocus()
                #         self.textEdit_PartNo.setStyleSheet(
                #             "border: 1px solid red;")
                #     else:
                #         self.textEdit_PartNo.setFocus()
                #         self.textEdit_PartNo.setStyleSheet(
                #             "border: 1px solid red;")
                # elif check_count_part_id == 0:
                #     self.textEdit_PartId.setFocus()
                #     self.textEdit_PartId.setStyleSheet(
                #         "border: 1px solid red;")

                # else:
                #     self.textEdit_PartNo.setFocus()
                #     self.textEdit_PartNo.setStyleSheet(
                #         "border: 1px solid red;")
                #     self.textEdit_PartId.setFocus()
                #     self.textEdit_PartId.setStyleSheet(
                #         "border: 1px solid red;")
                #     self.textEdit_KanbanId.setFocus()
                #     self.textEdit_KanbanId.setStyleSheet(
                #         "border: 1px solid red;")
                self.textEdit_PartNo.setFocus()
                self.textEdit_PartNo.setStyleSheet(
                    "border: 1px solid red;")
                self.textEdit_PartId.setFocus()
                self.textEdit_PartId.setStyleSheet(
                    "border: 1px solid red;")
                self.textEdit_KanbanId.setFocus()
                self.textEdit_KanbanId.setStyleSheet(
                    "border: 1px solid red;")
                popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                                              "แจ้งเตือน",
                                              "part id , part no , Kanban id ไม่ถูกต้อง / ไม่มีข้อมูลในระบบ กรุณาให้ admin เพิ่มข้อมูล",
                                              QtWidgets.QMessageBox.Ok,
                                              self)
                popup.show()
            else:

                self.textEdit_PartNo.setStyleSheet(
                    "border: 0px solid red;")

                self.textEdit_PartId.setStyleSheet(
                    "border: 0px solid red;")

                self.textEdit_KanbanId.setStyleSheet(
                    "border: 0px solid red;")

                if check_count_line == 0:
                    self.textEdit_Line.setFocus()
                    self.textEdit_Line.setStyleSheet(
                        "QLineEdit:focus { border: 1px solid red; }")
                    popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                                                  "แจ้งเตือน",
                                                  "Line ไม่ถูกต้อง / ไม่มี Line นี้อยู่ กรุณาให้ admin เพิ่มข้อมูล",
                                                  QtWidgets.QMessageBox.Ok,
                                                  self)
                    popup.show()
                else:
                    # if check_count_line == 0:
                    #     self.textEdit_Line.setFocus()
                    #     self.textEdit_Line.setStyleSheet(
                    #         "QLineEdit:focus { border: 1px solid red; }")
                    #     popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                    #                                   "แจ้งเตือน",
                    #                                   "line ไม่ถูกต้อง / ไม่มี line นี้อยู่ กรุณาให้ admin เพิ่มข้อมูล",
                    #                                   QtWidgets.QMessageBox.Ok,
                    #                                   self)
                    #     popup.show()
                    # else:
                    #     if check_count_kanban == 0:
                    #         self.textEdit_KanbanId.setFocus()
                    #         self.textEdit_KanbanId.setStyleSheet(
                    #             "QLineEdit:focus { border: 1px solid red; }")
                    #         popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                    #                                       "แจ้งเตือน",
                    #                                       "kanban id ไม่ถูกต้อง / ไม่มี kanban id นี้อยู่ กรุณาให้ admin เพิ่มข้อมูล",
                    #                                       QtWidgets.QMessageBox.Ok,
                    #                                       self)
                    #         popup.show()
                    #     else:
                    #         self.w = popup_window()
                    #         self.w.show()
                    self.w = popup_window()
                    self.w.show()

    def exit_app(self):
        self.close()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
  # To help with clarity I always call this the Main Event
  # Thread because that is what it is and this helps one
  # remember that when the go talking about the Main Event
  # Thread
    MainEventThread = QApplication([])
    MainEventThread.setStyle('Fusion')

    application = MainWindow()
    application.show()

  # This is the Qt5 way of doing this line if you are using
  # PySide2 you still have to use the old Qt4 style which is
  # sys.exit(MainEventHandler.exec_())
    MainEventThread.exec()
