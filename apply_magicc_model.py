from pymagicc import MAGICC6
from pymagicc.scenarios import rcp26, rcp45, rcp60, rcp85

from utils import write_delimited_text

# Run the Magicc binary on RCP26, RCP45, RCP60, and RCP85 scenarios
with MAGICC6() as magicc:
    results = magicc.run(rcp26)
    for rcp in [rcp45, rcp60, rcp85]:
        results.append(magicc.run(rcp), inplace=True)

# Write the MAGICC scenario data to a file
write_delimited_text(results, 'rcps.tsv', delimiter='\t')
