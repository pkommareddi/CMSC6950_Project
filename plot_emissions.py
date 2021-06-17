import utils
import matplotlib.pyplot as plt


def plot_emmisions(rcps, scenario, variable, file_name):
    rcp26 = rcps[(rcps.scenario == scenario) & (rcps.variable == variable)]
    unit = rcp26['unit'].drop_duplicates().tolist()[0]
    rcp26 = rcp26.drop(['climate_model', 'model', 'scenario', 'todo', 'unit', 'variable'], axis=1)
    rcp26 = rcp26.T.reset_index().drop(0)
    rcp26.columns = ['year', 'Bunkers', 'R5LAM', 'R5MAF', 'R5ASIA', 'R5REF', 'R5OECD', 'World']
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

plot_emmisions(rcps, 'RCP26', 'Emissions|CH4', 'temp/RCP26_Emissions|CH4.png')
plot_emmisions(rcps, 'RCP45', 'Emissions|CH4', 'temp/RCP45_Emissions|CH4.png')
plot_emmisions(rcps, 'RCP26', 'Emissions|CO2|MAGICC Fossil and Industrial', 'temp/RCP26_Emissions|CO2.png')
plot_emmisions(rcps, 'RCP45', 'Emissions|CO2|MAGICC Fossil and Industrial', 'temp/RCP45_Emissions|CO2.png')
