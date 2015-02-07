__author__ = 'ShaneDiNozzo'

import os

# noinspection PyUnresolvedReferences
import dirsizes_logic

# Set location variables
documents = '\Documents'
documents_dir = os.getenv('USERPROFILE') + documents
software_distribution_download = '\SoftwareDistribution\Download'
software_distribution_download_dir = os.getenv('windir') + software_distribution_download
downloads = '\Downloads'
downloads_dir = os.getenv('USERPROFILE') + downloads
software_distribution = '\SoftwareDistribution'
software_distribution_dir = os.getenv('windir') + software_distribution


def get_dir_size(start_path):
    total_size = 0
    total_size_twodecimal = ''

    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            filepath = os.path.join(dirpath, f)
            total_size += os.path.getsize(filepath)

    if 1 <= len(str(total_size)) <= 3:
        total_size_twodecimal = '%.2f' % total_size + ' B'
    elif 4 <= len(str(total_size)) <= 6:
        total_size_in_kb = total_size / 1024
        total_size_twodecimal = '%.2f' % total_size_in_kb + ' KB'
    elif 7 <= len(str(total_size)) <= 9:
        mb = 1024 * 1024
        total_size_in_mb = total_size / mb
        total_size_twodecimal = '%.2f' % total_size_in_mb + ' MB'
    elif 10 <= len(str(total_size)) <= 12:
        gb = 1024 * 1024 * 1024
        total_size_in_gb = total_size / gb
        total_size_twodecimal = '%.2f' % total_size_in_gb + ' GB'
    elif 13 <= len(str(total_size)) <= 15:
        tb = 1024 * 1024 * 1024 * 1024
        total_size_in_tb = total_size / tb
        total_size_twodecimal = '%.2f' % total_size_in_tb + ' TB'
    else:
        print('The size of the folder is greater than TB!')  # Maximum value is TB!

    return total_size_twodecimal


def get_files_count(start_path):
    count = 0
    for f in os.listdir(start_path):
        if os.path.isfile(os.path.join(start_path, f)):
            count += 1

    return str(count) + ' file(s) - '


def get_folders_count(start_path):
    foldercountarray = [os.path.join(start_path, o) for o in os.listdir(start_path) if
                        os.path.isdir(os.path.join(start_path, o))]
    return str(len(foldercountarray)) + ' folder(s) / '
