import os

import altair
from pandas import read_csv

dataset = read_csv(os.path.abspath('../../csv/video_games_sales_as_of_22_Dec_2016.csv'))

nintendo_data = dataset[dataset['Publisher'] == 'Nintendo']
games_per_platform = nintendo_data.groupby('Platform').count().reset_index()

nintendo_platform_chart = altair.Chart(games_per_platform).mark_bar(size = 30).encode(
    altair.X('Platform:N', axis = altair.Axis(title='Platform')),
    altair.Y('Name:Q', axis = altair.Axis(title='Number of Games')),
    altair.Color('Platform:N', scale = altair.Scale(range=['#d20014']), legend = None),
    altair.Tooltip(['Name:Q'], title = 'Games')
).properties(
    width=410,
    title='Unique Games Nintendo Published per Nintendo Platform as of December 2016'
)

nintendo_platform_chart_text = nintendo_platform_chart.mark_text(
    baseline =  'middle',
    color = 'black',
    dy = -7
).encode(
    text = 'Name:Q',
    opacity = altair.value(3.0)
)

full_bar_chart = nintendo_platform_chart + nintendo_platform_chart_text

full_bar_chart.save('bar_chart.html')
