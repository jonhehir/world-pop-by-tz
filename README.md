# World Population by Timezone

Have you ever wondered...

- what are the world's most/least populous timezones?
- what percentage of the world population lives in timezones with irregular offsets like UTC+5:30?
- how many people live within *X* hours of a given timezone?
- what percentage of the world observes DST?
- what other countries share my timezone?
- what is the distribution of population by timezone for a given country?

So have I! Good data on this is hard to find.

## The Database

- `tally.py` produces a table of world population grouped by IANA timezone code (e.g., `America/New_York`) and country code.
- `timezones.py` produces a table of timezone data by IANA code.
- The GPWv4 National Identifier dataset (see "Data Sources" below) includes a table of country data.
- These can be compiled into one nice SQLite DB via `sql/import.sql`.

## Data Sources

Population data comes from [Gridded Population of the World (GPW) v4](https://sedac.ciesin.columbia.edu/data/collection/gpw-v4) from [Socioeconomic Data and Applications Center (SEDAC)](https://sedac.ciesin.columbia.edu/). This is a raster dataset of world population available at various resolutions. Each country's population data is sourced differently, so the effective resolution of the data varies from one nation to another. For the United States, for example, the raster data is produced by rasterization of small areal units from the U.S. Census. Each country's data in GPWv4 is adjusted to match the 2015 Revision of the United Nation's World Population Prospects country totals.

Geographic timezone lookup is powered by [`timezonefinder`](https://github.com/jannikmi/timezonefinder). Additional timezone information is pulled from the IANA `tz` database via [`pytz`](https://github.com/stub42/pytzata/).

## Similar Work

This is not the first time someone has tried to get to address the question of world population by timezone. The two methods I'm familiar with from the past are:

- Manual data aggregation [(example)](https://www.reddit.com/r/dataisbeautiful/comments/7v743h/population_of_the_world_by_time_zone_oc/): This is painstaking work.
- Heuristics based on country-level data [(example)](https://blog.cyberclip.com/world-population-by-time-zone): The linked example takes a list of country populations and divides it evenly across timezones that intersect that country. Thus, for example, Canada is assumed to be evenly divided across six timezones, when in reality, the majority of the population resides in one timezone.

## Limitations

Since we're working with rasterized data here, it will be the case that some small portion of the population is misattributed to the wrong country and/or timezone. This would be mitigated by using a higher resolution dataset. Currently, I've only run this on the lowest resolution data for testing. At some point, I will get around to running this on higher resolution data.

If very high resolution data is desired, it would probably be wise to rewrite the tally to rasterize the GeoJSON from [`timezone-boundary-builder`](https://github.com/evansiroky/timezone-boundary-builder) and do a fully GeoTIFF/numpy approach to reading and aggregating.
