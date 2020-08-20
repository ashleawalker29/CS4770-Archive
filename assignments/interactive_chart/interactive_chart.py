import os

import plotly
from pandas import read_csv

# Plotly offline mode
plotly.offline.init_notebook_mode(connected=True)
dataset = read_csv(os.path.abspath('../../csv/dnd_character_survey_clarified.csv'))

male_data = dataset[dataset['Gender'] == 'Male']
female_data = dataset[dataset['Gender'] == 'Female']

male_chart = plotly.graph_objs.Bar(
    y = male_data["Age"],
    x = male_data["Age"].value_counts(),
    text = male_data["Age"].value_counts(),
    orientation = 'h',
    name = 'Men',
    marker = dict(
        color='#63D1F4'
    )
)

female_chart = plotly.graph_objs.Bar(
    y = female_data["Age"],
    x = female_data["Age"].value_counts() * -1,
    text = female_data["Age"].value_counts(),
    orientation = 'h',
    name = 'Women',
    marker = dict(
        color='#FFC0CB'
    )
)

layout = plotly.graph_objs.Layout(
    title='D&D Survey Result Male/Female Age Distribution',
    scene = dict(
        xaxis=dict(
            title='<b>Count</b>'),
        yaxis=dict(
            title='<b>Age</b>'),
    ),
    barmode = 'overlay',
    bargap = 0.1
)

interactive_chart_data = [male_chart, female_chart]

figure = plotly.graph_objs.Figure(data=interactive_chart_data, layout=layout)

plotly.offline.plot(figure, filename='interactive_chart.html')
