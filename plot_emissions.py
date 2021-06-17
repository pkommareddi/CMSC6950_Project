import utils
import matplotlib.pyplot as plt


def plot_emmisions(rcps, scenario, variable, file_name):
    rcp26 = rcps[(rcps.scenario == scenario) & (rcps.variable == variable)]
    unit = rcp26['unit'].drop_duplicates().tolist()[0]
    rcp26 = rcp26.drop(['climate_model', 'model', 'scenario',
                       'todo', 'unit', 'variable'], axis=1)
    rcp26 = rcp26.T.reset_index().drop(0)
    rcp26.columns = ['year', 'Bunkers', 'R5LAM',
                     'R5MAF', 'R5ASIA', 'R5REF', 'R5OECD', 'World']
    rcp26 = rcp26[rcp26.year < '2101']
    rcp26['year'] = rcp26['year'].astype('datetime64[ns]')

    # Plot the graph and the save the file
    _, ax = plt.subplots(nrows=1, ncols=1, figsize=(16, 9))
    for col in rcp26.columns[1:]:
        ax.plot(rcp26['year'], rcp26[col], label=col)
    ax.legend(title='Regions')
    ax.set_xlabel('Year')
    ax.set_ylabel(unit)
    ax.set_title(f'{scenario} {variable}')
    ax.grid()
    plt.savefig(file_name)


# read RCP data
rcps = utils.read_delimited_text('rcps.tsv', delimiter='\t')


if __name__ == '__main__':
    import sys

    utils.create_temp_dir_if_not_exists()
    plot_emmisions(rcps, sys.argv[1], sys.argv[2], sys.argv[3])
