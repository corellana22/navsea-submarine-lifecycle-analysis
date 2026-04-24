# Program to get unique hull numbers in data 

import pandas as pd

df = pd.read_csv("submarine_lifecycle_cleaned.csv")
#print("test:\n",df.head())

df_hull = df[["Hull Number"]]
#print("test2:\n", df_hull.head())

df_hull = df_hull.drop_duplicates()
print("test3:\n", df_hull.head())

out_path = "submarine_hull_numbers.csv"
df_hull.to_csv(out_path, index=False)
print(f"\nSaved to: {out_path}")

#EOF