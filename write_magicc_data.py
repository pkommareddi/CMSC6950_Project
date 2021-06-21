from pymagicc import MAGICC6
from pymagicc.scenarios import rcp26, rcp45, rcp60, rcp85

from utils import write_delimited_text

def write_magicc_data(scenario, filename):
    with MAGICC6() as magicc:
        result = magicc.run(scenario)

    # Write the MAGICC scenario data to a file
    write_delimited_text(result, filename, delimiter='\t')


if __name__ == '__main__':
    import sys

    scenario_name = sys.argv[1]
    scenario_map = {
        'rcp26': rcp26,
        'rcp45': rcp45,
        'rcp60': rcp60,
        'rcp85': rcp85
    }
    write_magicc_data(scenario_map[scenario_name], scenario_name + '_magicc_data.tsv')
