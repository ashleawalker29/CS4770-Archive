"""
This module is intended to create a Bar Chart from a .csv file.
Author: Ashlea Walker
"""
import altair
from pandas import read_csv
import os

os.chdir('D:\\Documents\\CS4770_datasets\\')

dataset = read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')

nintendo_data = dataset[dataset['Publisher'] == 'Nintendo']
games_per_platform = nintendo_data.groupby('Platform').count().reset_index()

game_chart = altair.Chart(games_per_platform).mark_bar(size = 30).encode(
    altair.X('Platform:N', axis = altair.Axis(title='Platform')),
    altair.Y('Name:Q', axis = altair.Axis(title='Number of Games')),
    altair.Color('Platform:N', scale = altair.Scale(range=['#d20014']), legend = None),
    altair.Tooltip(['Name:Q'], title = 'Games')
).properties(
    width=410,
    title='Unique Games Nintendo Published per Nintendo Platform as of December 2016'
)

game_chart_text = game_chart.mark_text(
    baseline =  'middle',
    color = 'black',
    dy = -7
).encode(
    text = 'Name:Q',
    opacity = altair.value(3.0)
)

(game_chart + game_chart_text)
