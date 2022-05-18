import pandas as pd
import plotly.express as px
df = pd.read_csv('W&H.csv')
height = df['Height(Inches)'].tolist()
sum = 0
for h in height:
    sum = sum + h
mean = sum / len(height)
print(mean)