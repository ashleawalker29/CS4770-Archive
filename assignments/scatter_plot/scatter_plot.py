import os

import altair
from pandas import read_csv

dataset = read_csv(os.path.abspath('../../csv/video_games_sales_as_of_22_Dec_2016.csv'))

nintendo_data = dataset[dataset['Publisher'] == 'Nintendo']
# Drop the game Wii Sports since it is a huge outlier (NA Sales = 41.36, Global Sales = 82.53)
# within the scale of the other games.
nintendo_data = nintendo_data[nintendo_data['Name'] != 'Wii Sports']

nintendo_chart = altair.Chart(nintendo_data).mark_point(color='#d20014', opacity=0.5).encode(
    altair.X(
        'Global_Sales:Q',
        axis=altair.Axis(title='Number of Global Sales (millions of units)'),
        scale=altair.Scale(domain=[0,45])),
    altair.Y(
        'NA_Sales:Q',
        axis=altair.Axis(title='Number of North America Sales (millions of units)'),
        scale=altair.Scale(domain=[0,45])),
    altair.Color(
        'Name:N',
        scale=altair.Scale(range=['#d20014']),
        legend=None),
    tooltip=['Name:N', 'NA_Sales:Q', 'Global_Sales:Q']
).properties(
    title='Effect of North America\'s Sales to Global Sales of Nintendo Games'
).interactive()

nintendo_chart.save('scatter_plot.html')
