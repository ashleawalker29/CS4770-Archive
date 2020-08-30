import os

import plotly
from pandas import read_csv

# Offline mode
plotly.offline.init_notebook_mode(connected=True)
dataframe = read_csv(os.path.abspath('../../csv/dnd_character_survey_clarified.csv'))


trace1 = plotly.graph_objs.Scatter3d(
    x=dataframe['Primary_Class'],
    y=dataframe['Race'],
    z=dataframe['Alignment'],
    text=dataframe['Race'].value_counts(),
    mode='markers',
    marker=dict(
        sizemode='diameter',
        size=dataframe['Race'].value_counts(),
    )
)

data = [trace1]

layout = plotly.graph_objs.Layout(
    title='Favorite D&D Character Combinations',
    scene = dict(
        xaxis=dict(
            title='<b>Primary Class</b>'),
        yaxis=dict(
            title='<b>Race</b>'),
        zaxis=dict(
            title='<b>Alignment</b>'),
    )
)

figure = plotly.graph_objs.Figure(data=data, layout=layout)

plotly.offline.plot(figure, filename='3d_chart.html')
