__author__ = 'ShaneDiNozzo'

import sys
import subprocess

# noinspection PyUnresolvedReferences
from PyQt5 import QtWidgets, uic, QtGui, QtCore

import dirs_files

form_class = uic.loadUiType("dirsizes.ui")[0]


class MainWindowClass(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.documentslabel.setText(dirs_files.documents_dir)
        self.downloadlabel.setText(dirs_files.downloads_dir)
        self.softdistlabel.setText(dirs_files.software_distribution_dir)
        self.softdistdownlabel.setText(dirs_files.software_distribution_download_dir)

        self.documentssize.setText(dirs_files.get_files_count(dirs_files.documents_dir) + dirs_files.get_folders_count(
            dirs_files.documents_dir) + dirs_files.get_dir_size(dirs_files.documents_dir))
        self.downloadsize.setText(dirs_files.get_files_count(dirs_files.downloads_dir) + dirs_files.get_folders_count(
            dirs_files.downloads_dir) + dirs_files.get_dir_size(dirs_files.downloads_dir))
        self.softdistsize.setText(
            dirs_files.get_files_count(dirs_files.software_distribution_dir) + dirs_files.get_folders_count(
                dirs_files.software_distribution_dir) + dirs_files.get_dir_size(dirs_files.software_distribution_dir))
        self.softdistdownsize.setText(
            dirs_files.get_files_count(dirs_files.software_distribution_download_dir) + dirs_files.get_folders_count(
                dirs_files.software_distribution_download_dir) + dirs_files.get_dir_size(
                dirs_files.software_distribution_download_dir))

        self.documentsbutton.setText('Show "' + dirs_files.documents + '" files')
        self.downloadbutton.setText('Show "' + dirs_files.downloads + '" files')
        self.softdistbutton.setText('Show "' + dirs_files.software_distribution + '" files')
        self.softdistdownbutton.setText('Show "' + dirs_files.software_distribution_download + '" files')

        self.documentsbutton.clicked.connect(lambda: self.open_file_location(dirs_files.documents_dir))
        self.downloadbutton.clicked.connect(lambda: self.open_file_location(dirs_files.downloads_dir))
        self.softdistbutton.clicked.connect(lambda: self.open_file_location(dirs_files.software_distribution_dir))
        self.softdistdownbutton.clicked.connect(
            lambda: self.open_file_location(dirs_files.software_distribution_download_dir))

    @staticmethod
    def open_file_location(start_path):
        subprocess.call("explorer " + start_path, shell=True)


app = QtWidgets.QApplication(sys.argv)
myWindow = MainWindowClass(None)
myWindow.show()
app.exec()