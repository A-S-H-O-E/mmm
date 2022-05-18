import statistics as st
import pandas as pd
df = pd.read_csv('W&H.csv')
height = df['Height(Inches)'].tolist()
n = len(height)
print(st.median(height))
if(n % 2 == 0):
    median = height[n//2]
else:
    median = (height[(n-1)//2] + height[(n+1)//2])/2
# median = height[n//2]
print(median)