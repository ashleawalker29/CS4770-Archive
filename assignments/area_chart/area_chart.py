import os

import altair
from pandas import read_csv

dataset = read_csv(os.path.abspath('video_games_sales_as_of_22_Dec_2016.csv'))

# Obtain all publisher's datasets seperately.
nintendo_dataset = dataset[dataset['Publisher'] == 'Nintendo']
sony_dataset = dataset[dataset['Publisher'] == 'Sony Computer Entertainment']
microsoft_dataset = dataset[dataset['Publisher'] == 'Microsoft Game Studios']

# Obtain all game titles that have a registered 'Year of Release'.
nintendo_data = nintendo_dataset.dropna(subset=['Year_of_Release'])
sony_data = sony_dataset.dropna(subset=['Year_of_Release'])
microsoft_data = microsoft_dataset.dropna(subset=['Year_of_Release'])

# Generate a chart for each game company (Nintendo, Sony, and Microsoft).
nintendo_chart = altair.Chart(nintendo_data).mark_area(color='#d20014', opacity=0.3).encode(
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

microsoft_chart = altair.Chart(microsoft_data).mark_area(opacity=0.3).encode(
    altair.X('Year_of_Release:O', axis=altair.Axis(title='Year of Release')),
    altair.Y('count()', axis=altair.Axis(title='Number of Games'), stack=None),
    altair.Color('Publisher:N')
)

# Layer all generated charts together to form one cohesive chart.
game_companies_chart = altair.layer(nintendo_chart, sony_chart)
game_companies_chart = altair.layer(game_companies_chart, microsoft_chart)

# Generate final chart.
game_companies_chart
