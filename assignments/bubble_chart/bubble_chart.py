import os

import plotly
from pandas import read_csv

# Plotly offline mode
plotly.offline.init_notebook_mode(connected=True)
dataframe = read_csv(os.path.abspath('../../csv/dnd_character_survey_clarified.csv'))

trace1 = plotly.graph_objs.Scatter(
    x = dataframe['Age'],
    y = dataframe['Characters_Played'],
    text = dataframe['Characters_Played'],
    mode = 'markers',
    marker = dict(
        size = 10,
        color = dataframe['Characters_Played'],
        colorscale = 'Blues',
        showscale = True
    )
)

layout = plotly.graph_objs.Layout(
    title = 'Player Age and the Number of Characters They\'ve Played',
    hovermode = 'closest',
    xaxis = dict(
        title = 'Age (years)',
    ),
    yaxis = dict(
        title = 'Number of Characters Played',
    )
)

data = [trace1]

figure = plotly.graph_objs.Figure(data=data, layout=layout)

plotly.offline.plot(figure, filename='bubble_chart.html')
