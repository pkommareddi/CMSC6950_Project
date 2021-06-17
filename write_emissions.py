import utils
from pymagicc.scenarios import rcp26, rcp45, rcp60, rcp85

scenarios_list = [rcp26, rcp45, rcp60, rcp85]

# Save scenarios data to disk
utils.create_temp_dir_if_not_exists()
utils.save_scenarios_as_delimited_text(scenarios_list, 'rcps.tsv')