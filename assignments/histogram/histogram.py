import os

import altair
from pandas import read_csv

dataset = read_csv(os.path.abspath('../../csv/video_games_sales_as_of_22_Dec_2016.csv'))

nintendo_data = dataset[dataset['Publisher'] == 'Nintendo']
nintendo_data = nintendo_data.dropna(subset=['Critic_Score'])

histogram = altair.Chart(nintendo_data).mark_bar(color='grey', size=15).encode(
    altair.X("Critic_Score:O", axis=altair.Axis(title='Critic Score')),
    altair.Y('count()', axis=altair.Axis(title='Number of Games')),
    altair.Tooltip(['Critic_Score:O'], title='Critic Score'),
).properties(
    width=950,
    title='Distribution of Nintendo Games per Critic Score'
)

histogram_text = histogram.mark_text(
    color='black',
    dy=-3
).encode(
    text='count()',
)

full_histogram = histogram + histogram_text

full_histogram.save('histogram.html')
