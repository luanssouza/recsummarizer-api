import pandas as pd

import numpy as np
from s3fs.core import S3FileSystem

from os import environ

def read_csv(object_name, header = 'infer', names = None, sep = ',', index_col = None):
    object_name = f"{environ['S3_BUCKET']}/{object_name}"
    return pd.read_csv(object_name, header = header, names = names, sep = sep, index_col = index_col)

def read_numpy(object_name):
    if ("s3://" in environ['S3_BUCKET']):
        s3fs = S3FileSystem()
        object_name = f"{environ['S3_BUCKET']}/{object_name}"
        return np.load(s3fs.open(object_name))
    else:
        return np.load(object_name)