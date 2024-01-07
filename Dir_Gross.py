import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Bala Eesan\Downloads\HVA\Mini Hackathon 2.0\imdb_top_1000.csv")
data = data.rename(columns={"Series_Title": "Movies_Title"})
data['Gross'] = data['Gross'].str.replace(',', '')
data['Gross'] = data['Gross'].astype('float64')
data['Gross'] = data['Gross'].replace(np.nan, 0)

s=data.groupby(['Director']).sum().reset_index()
d=s.sort_values(['Gross'],ascending=False)[:10]

fig,axs=plt.subplots(figsize=(20,5))
g=sns.barplot(x=d['Director'],y=d['Gross'], palette = 'hls')
g.set_title("Top 10 Directors vs Gross Earnings", weight = "bold")

plt.show()
