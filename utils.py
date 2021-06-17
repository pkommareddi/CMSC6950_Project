import os

import pandas as pd
from pandas import DataFrame
from pymagicc.io import MAGICCData

from copy import deepcopy


def convert_MAGICCData_to_df(data: MAGICCData) -> DataFrame:
    return data.timeseries().reset_index()


def convert_df_to_MAGICCData(data: DataFrame) -> MAGICCData:
    return MAGICCData(data)


def save_scenarios_as_delimited_text(scenarios, filename):
    '''
    Format the RCP scenario data as a DataFrame
    '''

    rcps = deepcopy(scenarios[0])
    for scenario in scenarios[1:]:
        rcps.append(scenario, inplace=True)
    write_delimited_text(rcps, filename, delimiter='\t')


def create_temp_dir_if_not_exists():
    '''
    Create a temp dir for saving intermediate data and visualizations
    '''

    if not os.path.exists('temp'):
        os.makedirs('temp')


def write_delimited_text(data: MAGICCData, filename, delimiter=',', header=True, index=False, append=False):
    '''
    Write a MAGICCData object as a delimited text file to disk
    '''

    create_temp_dir_if_not_exists()
    filename = os.path.join('temp', filename)
    mode = 'a' if append else 'w'
    data = convert_MAGICCData_to_df(data)
    data.to_csv(filename, sep=delimiter, header=header, index=index, mode=mode)


def read_delimited_text(filename, delimiter=',', header='infer'):
    '''
    Read a delimited text file as DataFrame
    '''

    if not os.path.exists('temp'):
        raise RuntimeError('temp folder does not exist')
    filename = os.path.join('temp', filename)
    return pd.read_csv(filename, sep=delimiter, header=header)
