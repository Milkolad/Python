import numpy as np
import pandas as pd
import re

df = pd.read_csv('./airlines.csv', encoding='utf-8')
df = df.dropna()
df['Самолеты'] = df['Самолеты'].str.split(',').apply(lambda x: list(map(lambda y: re.sub(r"\(.*\)", "", y).replace(" ", ""), x)))
pd.DataFrame(df).to_csv(r"result.csv")