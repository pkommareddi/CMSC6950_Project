from pymagicc import MAGICC6
from pymagicc.scenarios import rcp26, rcp45, rcp60, rcp85
from pymagicc.io import MAGICCData

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from utils import write_delimited_text, read_delimited_text


def main():
    # Read the Magicc data
    magicc_data = read_delimited_text('rcps.tsv', delimiter='\t')

    # Filter the data to Region = 'World' and variable = 'Radiative Forcing'
    filtered_magicc_data = magicc_data[(magicc_data.region == 'World') & (
        magicc_data.variable == 'Radiative Forcing')]
    filtered_magicc_data = filtered_magicc_data.drop(
        ['climate_model', 'model', 'region', 'todo', 'unit', 'variable'], axis=1)

    df = filtered_magicc_data.T.reset_index().drop(0)
    df.columns = ['year', 'rcp26', 'rcp45', 'rcp60', 'rcp85']
    df['year'] = df['year'].astype('datetime64[ns]')

    # Plot the graph and the save the file
    _, ax = plt.subplots(nrows=1, ncols=1, figsize=(16, 9))
    for col in df.columns[1:]:
        ax.plot(df['year'], df[col], label=col.upper())
    ax.legend(title='Scenarios')
    ax.set_xlabel('Year')
    ax.set_ylabel('Radiative Forcing')
    ax.set_title('Radiative Forcing VS Time')
    ax.grid()

    plt.savefig('temp/radiative_forcing.png')


if __name__ == '__main__':
    main()
