from plotly import tools, graph_objs
import plotly
import numpy
from pandas import read_csv

# Offline mode
plotly.offline.init_notebook_mode(connected=True)
dataframe = read_csv('D:\\Documents\\CS4770_datasets\\dnd_character_survey_clarified.csv')


trace1 = graph_objs.Scatter3d(
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
layout=graph_objs.Layout(
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

fig=graph_objs.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='AWalker_3d_chart.html')
