__author__ = 'ShaneDiNozzo'

import sys
import subprocess

# Try to import PyQt5 module ######################################
try:
    # noinspection PyUnresolvedReferences
    import PyQt5
except ImportError:
    print("PyQt5 module not found!")
    exit()

# noinspection PyUnresolvedReferences
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Try to import dirs_files module ################################
try:
    # noinspection PyUnresolvedReferences
    import dirs_files as df
except ImportError:
    print("dirs_files module not found!")
    exit()

from dirs_files import software_distribution_download_dir as softdistdowndir
from dirs_files import software_distribution_dir as softdistdir
from dirs_files import get_folders_count as getfoc
from dirs_files import get_files_count as getfic
from dirs_files import get_dir_size as getds

form_class = uic.loadUiType("dirsizes.ui")[0]


class MainWindowClass(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.iconres = QtGui.QPixmap(':/AppIcon/icon.ico')
        self.icon = QtGui.QIcon(self.iconres)
        self.documentslabel.setText(df.documents_dir)
        self.downloadlabel.setText(df.downloads_dir)
        self.softdistlabel.setText(softdistdir)
        self.softdistdownlabel.setText(softdistdowndir)

        self.documentssize.setText(getfic(df.documents_dir) + getfoc(df.documents_dir) + getds(df.documents_dir))
        self.downloadsize.setText(getfic(df.downloads_dir) + getfoc(df.downloads_dir) + getds(df.downloads_dir))
        self.softdistsize.setText(getfic(softdistdir) + getfoc(softdistdir) + getds(softdistdir))
        self.softdistdownsize.setText(getfic(softdistdowndir) + getfoc(softdistdowndir) + getds(softdistdowndir))

        self.documentsbutton.setText('Show "' + df.documents + '" files')
        self.downloadbutton.setText('Show "' + df.downloads + '" files')
        self.softdistbutton.setText('Show "' + df.software_distribution + '" files')
        self.softdistdownbutton.setText('Show "' + df.software_distribution_download + '" files')

        self.documentsbutton.clicked.connect(lambda: self.open_file_location(df.documents_dir))
        self.downloadbutton.clicked.connect(lambda: self.open_file_location(df.downloads_dir))
        self.softdistbutton.clicked.connect(lambda: self.open_file_location(softdistdir))
        self.softdistdownbutton.clicked.connect(
            lambda: self.open_file_location(softdistdowndir))

    @staticmethod
    def open_file_location(start_path):
        subprocess.call("explorer " + start_path, shell=True)


app = QtWidgets.QApplication(sys.argv)
myWindow = MainWindowClass(None)
myWindow.show()
app.exec()
