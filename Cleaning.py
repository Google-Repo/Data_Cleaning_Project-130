import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]

df.to_csv('Cleared Data.csv')
print(df.head())