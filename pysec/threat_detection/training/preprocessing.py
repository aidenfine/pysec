
import tqdm
import random
import pathlib
import itertools
import collections

import os
import cv2
import numpy as np
import remotezip as rz

import tensorflow as tf

# Some modules to display an animation using imageio.
import imageio
from IPython import display
from urllib import request


URL = 'https://storage.googleapis.com/thumos14_files/UCF101_videos.zip'



def list_files_from_zip_url(zip_url):
  """ List the files in each class of the dataset given a URL with the zip file.

    Args:
      zip_url: A URL from which the files can be extracted from.

    Returns:
      List of files in each of the classes.
  """
  files = []
  with rz.RemoteZip(zip_url) as zip:
    for zip_info in zip.infolist():
      files.append(zip_info.filename)
  return files

files = list_files_from_zip_url(URL)
files = [f for f in files if f.endswith('.avi')]
files [:10]

def get_class(fname):
  return fname.split('_')[-3]


def get_files_per_class(files):
  """ Retrieve the files that belong to each class.

    Args:
      files: List of files in the dataset.

    Returns:
      Dictionary of class names (key) and files (values). 
  """
  files_for_class = collections.defaultdict(list)
  for fname in files:
    class_name = get_class(fname)
    files_for_class[class_name].append(fname)
  return files_for_class


"""
DEFINE num of classes and files per class
"""
NUM_CLASSES = 10
FILES_PER_CLASS = 50


files_for_class = get_files_per_class(files)
classes = list(files_for_class.keys())
     
print('Num classes:', len(classes))
print('Num videos for class[0]:', len(files_for_class[classes[0]]))