-- Throw everything into a SQLite DB with this script.
-- You'll need to have your files located at:
-- - tally.tsv
-- - timezones.tsv
-- - countries.tsv

-- Note that countries.tsv should be taken directly from the GPW
-- data download (but renamed/relocated approporiately).

CREATE TABLE population (
    country_code NUMBER,
    iana_code TEXT,
    population NUMBER,
    PRIMARY KEY (country_code, iana_code)
);

CREATE TABLE countries (
    country_code NUMBER PRIMARY KEY,
    iso_code TEXT,
    unsd_code NUMBER,
    country_name TEXT,
    ciesin_code NUMBER,
    data_type TEXT,
    data_code NUMBER,
    data_year NUMBER,
    data_level NUMBER,
    sex_level NUMBER,
    age_level NUMBER,
    gr_start NUMBER,
    gr_end NUMBER,
    gr_level NUMBER,
    last_census NUMBER,
    mean_unit_km NUMBER
);

CREATE TABLE timezones (
    iana_code TEXT PRIMARY KEY,
    winter_offset NUMBER,
    summer_offset NUMBER
);

.mode tabs
.import tally.tsv population
.import --skip 1 countries.tsv countries
.import timezones.tsv timezones
