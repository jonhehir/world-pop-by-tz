from argparse import ArgumentParser
from collections import Counter

import numpy as np
from timezonefinder import TimezoneFinder

from tzpop.ascii import ASCIIGrid, ASCIIGridJoin


# Get file paths from commmand line args
parser = ArgumentParser()
parser.add_argument("nat", type=str, help="Path to national identifier grid (ASCII)")
parser.add_argument("pop", type=str, help="Path to population grid (ASCII)")
args = parser.parse_args()

# Load ASCII data
join = ASCIIGridJoin(
    country=ASCIIGrid(args.nat),
    population=ASCIIGrid(args.pop)
)


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
