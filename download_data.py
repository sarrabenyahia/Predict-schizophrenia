#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 15:08:21 2022

@author: edouard.duchesnay@cea.fr
"""
import os
import os.path
# import numpy as np
# import pandas as pd
import urllib.request
# import click

# from sklearn.model_selection import train_test_split
from shutil import unpack_archive  # , copyfile, make_archive, move

try:
    PATH_DATA = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "data"
    )
except NameError:
    PATH_DATA = "data"

os.makedirs(PATH_DATA, exist_ok=True)

URL_DATA = 'ftp://ftp.cea.fr/pub/unati/people/educhesnay/data/\
brain_anatomy_schizophrenia_data/sz_public_202211.zip'  # PUBLIC DATASET


def fetch_data(urls, dst, verbose=1):
    """Fetch dataset.

    Args:
        urls (str, ): list/tuple of urls.
        dst (str): destination directory.

    Returns:
        downloaded ([str, ]): paths to downloaded files.

    """
    downloaded = []
    for url in urls:
        dst_filename = os.path.join(dst, os.path.basename(url))
        if not os.path.exists(dst_filename):
            if verbose:
                print("Download: %s" % url)
            urllib.request.urlretrieve(url, dst_filename)
        downloaded.append(dst_filename)
    return downloaded


if __name__ == "__main__":

    # Download and unzip dataset
    zip_filename = \
        fetch_data(urls=[URL_DATA], dst=PATH_DATA,
                   verbose=1)[0]

    unpack_archive(zip_filename, extract_dir=PATH_DATA)
