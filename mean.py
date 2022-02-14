import plotly.express as px
import pandas as pd 
import numpy as np

df = pd.read_csv("data.csv")

marks = df["Marks In Percentage"].tolist()
daysPresent = df["Days Present"]

fig = px.scatter(df,x=daysPresent, y=marks)

fig.show()

c = np.corrcoef(daysPresent, marks)
    
print("Correlation between Marks in percentage and Days present --->",c[0,1])
