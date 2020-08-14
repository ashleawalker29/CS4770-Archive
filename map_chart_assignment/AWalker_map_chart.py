"""
This module is intended to create an Scatter Plot from a .csv file.
Author: Ashlea Walker
"""
import altair
from pandas import read_csv
from vega_datasets import data

dataset = read_csv('D:\\Documents\\CS4770_datasets\\geo_texture.csv', low_memory=False)
dataset_1 = dataset.iloc[:5000]
dataset_2 = dataset.iloc[5001:10000]
dataset_3 = dataset.iloc[10001:15000]
dataset_4 = dataset.iloc[15001:20000]
dataset_5 = dataset.iloc[20001:25000]
dataset_6 = dataset.iloc[25001:30000]

data_map_1 = altair.Chart(dataset_1).mark_circle(size=3).encode(
    longitude='LONGITUDE:Q',
    latitude='LATITUDE:Q'
).project(type='albersUsa').properties(
    width=1000,
    height=600
)

data_map_2 = altair.Chart(dataset_2).mark_circle(size=3).encode(
    longitude='LONGITUDE:Q',
    latitude='LATITUDE:Q'
).project(type='albersUsa').properties(
    width=1000,
    height=600
)

data_map_3 = altair.Chart(dataset_3).mark_circle(size=3).encode(
    longitude='LONGITUDE:Q',
    latitude='LATITUDE:Q'
).project(type='albersUsa').properties(
    width=1000,
    height=600
)

data_map_4 = altair.Chart(dataset_4).mark_circle(size=3).encode(
    longitude='LONGITUDE:Q',
    latitude='LATITUDE:Q'
).project(type='albersUsa').properties(
    width=1000,
    height=600
)

data_map_5 = altair.Chart(dataset_5).mark_circle(size=3).encode(
    longitude='LONGITUDE:Q',
    latitude='LATITUDE:Q'
).project(type='albersUsa').properties(
    width=1000,
    height=600
)

data_map_6 = altair.Chart(dataset_6).mark_circle(size=3).encode(
    longitude='LONGITUDE:Q',
    latitude='LATITUDE:Q'
).project(type='albersUsa').properties(
    width=1000,
    height=600
)

states = altair.topo_feature(data.us_10m.url, feature='states')

# US states background
background = altair.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).properties(
    width=1000,
    height=600,
    title='Sediment Geological Survey Locations Taken by the Atlantic Continental Margin Program'
).project('albersUsa')

full_chart = altair.layer(
    data_map_1,
    data_map_2,
    data_map_3,
    data_map_4,
    data_map_5,
    data_map_6,
    background
)

full_chart
