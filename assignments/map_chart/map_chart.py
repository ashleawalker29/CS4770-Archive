import os

import altair
from pandas import read_csv
from vega_datasets import data

dataset = read_csv(os.path.abspath('../../csv/geo_texture.csv'), low_memory=False)

# Altair can only process 5000 rows at a time, so the datasets are broken up into manageable sets.
dataset_1 = dataset.iloc[:5000]
dataset_2 = dataset.iloc[5001:10000]
dataset_3 = dataset.iloc[10001:15000]
dataset_4 = dataset.iloc[15001:20000]
dataset_5 = dataset.iloc[20001:25000]
dataset_6 = dataset.iloc[25001:30000]

# Create a map chart for each subset of the data.
map_chart_1 = altair.Chart(dataset_1).mark_circle(size=3).encode(
    longitude='LONGITUDE:Q',
    latitude='LATITUDE:Q'
).project(type='albersUsa').properties(
    width=1000,
    height=600
)

map_chart_2 = altair.Chart(dataset_2).mark_circle(size=3).encode(
    longitude='LONGITUDE:Q',
    latitude='LATITUDE:Q'
).project(type='albersUsa').properties(
    width=1000,
    height=600
)

map_chart_3 = altair.Chart(dataset_3).mark_circle(size=3).encode(
    longitude='LONGITUDE:Q',
    latitude='LATITUDE:Q'
).project(type='albersUsa').properties(
    width=1000,
    height=600
)

map_chart_4 = altair.Chart(dataset_4).mark_circle(size=3).encode(
    longitude='LONGITUDE:Q',
    latitude='LATITUDE:Q'
).project(type='albersUsa').properties(
    width=1000,
    height=600
)

map_chart_5 = altair.Chart(dataset_5).mark_circle(size=3).encode(
    longitude='LONGITUDE:Q',
    latitude='LATITUDE:Q'
).project(type='albersUsa').properties(
    width=1000,
    height=600
)

map_chart_6 = altair.Chart(dataset_6).mark_circle(size=3).encode(
    longitude='LONGITUDE:Q',
    latitude='LATITUDE:Q'
).project(type='albersUsa').properties(
    width=1000,
    height=600
)

# Grab the geological data for the USA. It will be used as the background of chart, giving context.
states = altair.topo_feature(data.us_10m.url, feature='states')

# Add labels and background.
background = altair.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).properties(
    width=1000,
    height=600,
    title='Sediment Geological Survey Locations Taken by the Atlantic Continental Margin Program'
).project('albersUsa')

# Merge all subsets of data from the CSV and the background layet
full_map_chart = altair.layer(
    map_chart_1,
    map_chart_2,
    map_chart_3,
    map_chart_4,
    map_chart_5,
    map_chart_6,
    background
)

full_map_chart.save('map_chart.html')
