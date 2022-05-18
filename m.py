import pandas as pd
import plotly.express as px
import statistics as st
df = pd.read_csv('W&H.csv')
height = df['Height(Inches)'].tolist()
mode = st.mode(height)

median = st.median(height)
print(median)