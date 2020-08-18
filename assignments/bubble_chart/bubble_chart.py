from plotly import tools, graph_objs
import plotly
import numpy
from pandas import read_csv

# Offline mode
plotly.offline.init_notebook_mode(connected=True)
dataframe = read_csv('D:\\Documents\\CS4770_datasets\\dnd_character_survey_clarified.csv')

trace1 = graph_objs.Scatter(
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

layout = graph_objs.Layout(
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

fig=graph_objs.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='AWalker_bubble_chart.html')
