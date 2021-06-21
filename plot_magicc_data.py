import os
import glob

import pandas as pd
import matplotlib.pyplot as plt

from utils import read_delimited_text


def main(variable):
    path = os.getcwd()
    csv_files = glob.glob(os.path.join(path, 'temp', "*_magicc_data.tsv"))
    l = []
    for f in csv_files:
        l.append(read_delimited_text(f.split("/")[-1], delimiter='\t'))

    # Read the Magicc data
    magicc_data = pd.concat(l).reset_index(drop=True)

    # Filter the data to Region = 'World' and variable = 'Radiative Forcing'
    filtered_magicc_data = magicc_data[(magicc_data.region == 'World') & (
        magicc_data.variable == variable)]
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
    ax.set_ylabel(variable)
    ax.set_title(f'{variable} VS Time')
    ax.grid()

    filename = variable.replace(' ', '_')
    plt.savefig(f'temp/{filename}.png')


if __name__ == '__main__':
    import sys
    main(sys.argv[1])
