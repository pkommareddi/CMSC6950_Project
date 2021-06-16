import os

import pandas as pd
from pymagicc.io import MAGICCData


def write_delimited_text(data: MAGICCData, filename, delimiter=',', header=True, index=False, append=False):
    '''
    Write a MAGICCData object as a delimited text file to disk
    '''

    if not os.path.exists('temp'):
        os.makedirs('temp')
    filename = os.path.join('temp', filename)

    mode = 'a' if append else 'w'
    data = data.timeseries().reset_index()
    data.to_csv(filename, sep=delimiter, header=header, index=index, mode=mode)


def read_delimited_text(filename, delimiter=',', header='infer'):
    if not os.path.exists('temp'):
        raise RuntimeError('temp folder does not exist')
    filename = os.path.join('temp', filename)
    return pd.read_csv(filename, sep=delimiter, header=header)
