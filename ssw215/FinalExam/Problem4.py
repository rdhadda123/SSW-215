import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Exam file_2-2.csv")
df.columns = ['customer_ID', 'gender', 'age', 'annual_income', 'spending_score']

print(df)

df_sorted = df.sort_values(by='spending_score')
print(df_sorted)

subset = df.loc[:, ['gender', 'annual_income']]
print(subset)

grouped = df.groupby('gender')['annual_income']
print(grouped.describe())

df.plot.scatter(x = 'age', y = 'annual_income')
plt.show()