import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250224.csv")

fur_colors = data["Primary Fur Color"].dropna()
color_counts = data["Primary Fur Color"].value_counts()


df = pd.DataFrame({
    "Fur Color": color_counts.index,
    "Count": color_counts.values
})

print(df)

