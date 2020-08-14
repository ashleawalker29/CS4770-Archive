from plotly import tools, graph_objs
import plotly
import numpy
from pandas import read_csv

# Offline mode
plotly.offline.init_notebook_mode(connected=True)
dataset = read_csv('D:\\Documents\\CS4770_datasets\\dnd_character_survey_clarified.csv')

male_df = dataset[dataset['Gender'] == 'Male']
female_df = dataset[dataset['Gender'] == 'Female']

male_chart = graph_objs.Bar(
    y = male_df["Age"],
    x = male_df["Age"].value_counts(),
    text = male_df["Age"].value_counts(),
    orientation = 'h',
    name = 'Men',
    marker = dict(
        color='#63D1F4'
    )
)
female_chart = graph_objs.Bar(
    y = female_df["Age"],
    x = female_df["Age"].value_counts() * -1,
    text = female_df["Age"].value_counts(),
    orientation = 'h',
    name = 'Women',
    marker = dict(
        color='#FFC0CB'
    )
)

data = [male_chart, female_chart]

layout=graph_objs.Layout(
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

fig=graph_objs.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='AWalker_interactive_chart.html')
