# World Population by Timezone

Have you ever wondered...

- what's the world's most/least populous timezone?
- what percentage of the world population lives in timezones with irregular offsets like UTC+5:30?
- how many people live within three hours of a given timezone?
- how many other countries share my timezone?

So have I! Good data on this is hard to find.

## The Database

This produces a table of population grouped by IANA timezone code (e.g., `America/New_York`) and country code.

Auxilliary tables for UTC offsets, DST information, country names, etc.

## Data Sources

Population data comes from [Gridded Population of the World (GPW) v4](https://sedac.ciesin.columbia.edu/data/collection/gpw-v4) from [Socioeconomic Data and Applications Center (SEDAC)](https://sedac.ciesin.columbia.edu/). This is a raster dataset of world population available at various resolutions. Each country's population data is sourced differently, so the effective resolution of the data varies from one nation to another. For the United States, for example, the raster data is produced by rasterization of small areal units from the U.S. Census. Each country's data in GPWv4 is adjusted to match the 2015 Revision of the United Nation's World Population Prospects country totals.

Geographic timezone lookup is powered by [`timezonefinder`](https://github.com/jannikmi/timezonefinder), which in turn sources data from [`timezone-boundary-builder`](https://github.com/evansiroky/timezone-boundary-builder). Additional timezone information is pulled from the IANA `tz` database via [`tzdata`](https://pypi.org/project/tzdata/).

