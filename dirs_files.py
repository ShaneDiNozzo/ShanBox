__author__ = "ShaneDiNozzo"

import os
# noinspection PyUnresolvedReferences
import dirsizes_logic

documents = "\Documents"
software_distribution_download = '\SoftwareDistribution\Download'
downloads = '\Downloads'
software_distribution = '\SoftwareDistribution'
software_distribution_dir = os.getenv("windir") + software_distribution
downloads_dir = os.getenv('USERPROFILE') + downloads
software_distribution_download_dir = os.getenv('windir') + software_distribution_download
documents_dir = os.getenv("USERPROFILE") + documents


def get_dir_size(start_path):
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            filepath = os.path.join(dirpath, f)
            total_size += os.path.getsize(filepath)

    mb = 1024 * 1024
    total_size_in_mb = total_size / mb
    total_size_twodec = "%.2f" % total_size_in_mb + " MB"
    if len(total_size_twodec) >= 11:
        total_size_in_gb = total_size_in_mb / 1024
        total_size_twodec = "%.2f" % total_size_in_gb + " GB"

    return total_size_twodec


def get_files_count(start_path):
    count = 0
    for f in os.listdir(start_path):
        if os.path.isfile(os.path.join(start_path, f)):
            count += 1

    return str(count) + " file(s) / "