"""
This module is intended to create an Area Chart from a .csv file.
Author: Ashlea Walker
"""
import altair
from pandas import read_csv

dataset = read_csv('D:\\Documents\\CS4770_datasets\\Video_Games_Sales_as_at_22_Dec_2016.csv')

nin_data = dataset[dataset['Publisher'] == 'Nintendo']
nin_data = nin_data.dropna(subset=['Year_of_Release'])
sony_data = dataset[dataset['Publisher'] == 'Sony Computer Entertainment']
sony_data = sony_data.dropna(subset=['Year_of_Release'])
ms_data = dataset[dataset['Publisher'] == 'Microsoft Game Studios']
ms_data = ms_data.dropna(subset=['Year_of_Release'])

nin_chart = altair.Chart(nin_data).mark_area(color='#d20014', opacity=0.3).encode(
    altair.X('Year_of_Release:O', axis=altair.Axis(title='Year of Release')),
    altair.Y('count()', axis=altair.Axis(title='Number of Games'), stack=None),
    altair.Color('Publisher:N', scale=altair.Scale(range=['#0e7a0d', '#d20014', '#003791']))
).properties(
    title='Games Published by Leading Companies Over Time'
)

sony_chart = altair.Chart(sony_data).mark_area(opacity=0.3).encode(
    altair.X('Year_of_Release:O', axis=altair.Axis(title='Year of Release')),
    altair.Y('count()', axis=altair.Axis(title='Number of Games'), stack=None),
    altair.Color('Publisher:N')
)

ms_chart = altair.Chart(ms_data).mark_area(opacity=0.3).encode(
    altair.X('Year_of_Release:O', axis=altair.Axis(title='Year of Release')),
    altair.Y('count()', axis=altair.Axis(title='Number of Games'), stack=None),
    altair.Color('Publisher:N')
)

full_chart = altair.layer(nin_chart, sony_chart)
full_chart = altair.layer(full_chart, ms_chart)

full_chart
