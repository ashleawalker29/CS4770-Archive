"""
This module is intended to create a Histogram from a .csv file.
Author: Ashlea Walker
"""
import altair
from pandas import read_csv

dataset = read_csv('D:\\Documents\\CS4770_datasets\\Video_Games_Sales_as_at_22_Dec_2016.csv')

nintendo_data = dataset[dataset['Publisher'] == 'Nintendo'] # Limiit to just Nintendo Game Title
nintendo_data = nintendo_data.dropna(subset=['Critic_Score']) # Remove all Values that aren't available

bar_chart = altair.Chart(nintendo_data).mark_bar(color='grey', size=15).encode(
    altair.X("Critic_Score:O", axis=altair.Axis(title='Critic Score')),
    altair.Y('count()', axis=altair.Axis(title='Number of Games')),
    altair.Tooltip(['Critic_Score:O'], title='Critic Score'),
).properties(
    width=950,
    title='Distribution of Nintendo Games per Critic Score'
)

bar_chart_text = bar_chart.mark_text(
    color='black',
    dy=-3
).encode(
    text='count()',
)

(bar_chart + bar_chart_text)
