# import pymagicc
from pymagicc import MAGICC6
from pymagicc.scenarios import rcp26, rcp45, rcp60, rcp85
from pymagicc.io import MAGICCData

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from utils import write_delimited_text, read_delimited_text


def main():
    # Run the Magicc binary on RCP26, RCP45, RCP60, and RCP85 scenarios
    with MAGICC6() as magicc:
        results = magicc.run(rcp26)
        for rcp in [rcp45, rcp60, rcp85]:
            results.append(magicc.run(rcp), inplace=True)

    # Write the MAGICC scenario data to a file
    write_delimited_text(results, 'rcps.tsv', delimiter='\t')

    # Read the Magicc data
    magicc_data = read_delimited_text('rcps.tsv', delimiter='\t')
    print(magicc_data.head())

    # Filter the data to Region = 'World' and variable = 'Radiative Forcing'
    filtered_magicc_data = magicc_data[(magicc_data.region == 'World') & (
        magicc_data.variable == 'Radiative Forcing')]
    filtered_magicc_data = filtered_magicc_data.drop(
        ['climate_model', 'model', 'region', 'todo', 'unit', 'variable'], axis=1)

    df = filtered_magicc_data.T.reset_index().drop(0)
    df.columns = ['year', 'rcp26', 'rcp45', 'rcp60', 'rcp85']
    df['year'] = df['year'].astype('datetime64[ns]')

    # Plot the graph and the save the file
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(16, 9))
    ax.plot(df['year'], df['rcp26'], label='RCP26')
    ax.plot(df['year'], df['rcp45'], label='RCP45')
    ax.plot(df['year'], df['rcp60'], label='RCP60')
    ax.plot(df['year'], df['rcp85'], label='RCP85')
    ax.legend(title='Scenarios')
    ax.set_xlabel('Year')
    ax.set_ylabel('Radiative Forcing')
    ax.set_title('Radiative Forcing ')
    ax.grid()

    plt.savefig('temp/radiative_forcing.png')


if __name__ == '__main__':
    main()
