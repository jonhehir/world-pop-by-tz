from collections import Counter
import os
from pathlib import Path

import numpy as np
from timezonefinder import TimezoneFinder

from tzpop.ascii import ASCIIGrid, ASCIIGridJoin


os.chdir(Path(__file__).parent)

# Load ASCII data
grid_nat = ASCIIGrid("data/gpw-v4-national-identifier-grid-rev11_1_deg_asc/gpw_v4_national_identifier_grid_rev11_1_deg.asc")
grid_pop = ASCIIGrid("data/gpw-v4-population-count-adjusted-to-2015-unwpp-country-totals-rev11_2020_1_deg_asc/gpw_v4_population_count_adjusted_to_2015_unwpp_country_totals_rev11_2020_1_deg.asc")
join = ASCIIGridJoin(country=grid_nat, population=grid_pop)


# Iterate over grids to tally population, grouped by country and timezone (e.g., America/New_York)
tzf = TimezoneFinder()
tally = Counter()
for entry in join.entries():
    lat, lng = entry["point"]
    country = int(entry["country"])
    population = entry["population"]

    if np.isnan(population) or population < 0.01:
        continue # nobody lives here

    tz = tzf.timezone_at_land(lat=lat, lng=lng)

    tally[(country, tz)] += population

# Print data as TSV
for key, val in tally.items():
    print("\t".join(map(str, [*key, val])))
