# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dirsizes.ui'
#
# Created: Tue Jan 20 14:00:24 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(243, 280)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.softdistlabel = QtWidgets.QLabel(self.centralwidget)
        self.softdistlabel.setText("")
        self.softdistlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.softdistlabel.setObjectName("softdistlabel")
        self.verticalLayout.addWidget(self.softdistlabel)
        self.softdistsize = QtWidgets.QLabel(self.centralwidget)
        self.softdistsize.setText("")
        self.softdistsize.setAlignment(QtCore.Qt.AlignCenter)
        self.softdistsize.setObjectName("softdistsize")
        self.verticalLayout.addWidget(self.softdistsize)
        self.softdistbutton = QtWidgets.QPushButton(self.centralwidget)
        self.softdistbutton.setText("")
        self.softdistbutton.setObjectName("softdistbutton")
        self.verticalLayout.addWidget(self.softdistbutton)
        self.softdistdownlabel = QtWidgets.QLabel(self.centralwidget)
        self.softdistdownlabel.setText("")
        self.softdistdownlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.softdistdownlabel.setObjectName("softdistdownlabel")
        self.verticalLayout.addWidget(self.softdistdownlabel)
        self.softdistdownsize = QtWidgets.QLabel(self.centralwidget)
        self.softdistdownsize.setText("")
        self.softdistdownsize.setAlignment(QtCore.Qt.AlignCenter)
        self.softdistdownsize.setObjectName("softdistdownsize")
        self.verticalLayout.addWidget(self.softdistdownsize)
        self.softdistdownbutton = QtWidgets.QPushButton(self.centralwidget)
        self.softdistdownbutton.setText("")
        self.softdistdownbutton.setObjectName("softdistdownbutton")
        self.verticalLayout.addWidget(self.softdistdownbutton)
        self.downloadlabel = QtWidgets.QLabel(self.centralwidget)
        self.downloadlabel.setText("")
        self.downloadlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.downloadlabel.setObjectName("downloadlabel")
        self.verticalLayout.addWidget(self.downloadlabel)
        self.downloadsize = QtWidgets.QLabel(self.centralwidget)
        self.downloadsize.setText("")
        self.downloadsize.setAlignment(QtCore.Qt.AlignCenter)
        self.downloadsize.setObjectName("downloadsize")
        self.verticalLayout.addWidget(self.downloadsize)
        self.downloadbutton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadbutton.setText("")
        self.downloadbutton.setObjectName("downloadbutton")
        self.verticalLayout.addWidget(self.downloadbutton)
        self.documentslabel = QtWidgets.QLabel(self.centralwidget)
        self.documentslabel.setText("")
        self.documentslabel.setObjectName("documentslabel")
        self.verticalLayout.addWidget(self.documentslabel)
        self.documentssize = QtWidgets.QLabel(self.centralwidget)
        self.documentssize.setText("")
        self.documentssize.setObjectName("documentssize")
        self.verticalLayout.addWidget(self.documentssize)
        self.documentsbutton = QtWidgets.QPushButton(self.centralwidget)
        self.documentsbutton.setText("")
        self.documentsbutton.setObjectName("documentsbutton")
        self.verticalLayout.addWidget(self.documentsbutton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dir Sizes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

