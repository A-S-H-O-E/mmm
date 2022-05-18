import pandas as pd
import plotly.express as px
df = pd.read_csv('W&H.csv')
weight = df['Weight(Pounds)'].tolist()
sum = 0
for w in weight:
    sum = sum + w
mean = sum / len(weight)
print(mean)