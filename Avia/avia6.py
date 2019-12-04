import numpy as np
import pandas as pd

adf = pd.read_csv('./airports.csv', encoding='utf-8')
ptdf = pd.read_csv('./passenger transportation.csv', encoding='utf-8', sep=';')

month_adf = ptdf.drop(['Год периода данных'], axis=1)
month_adf = month_adf.replace('***', None)
month_adf = month_adf.fillna('0')
month_adf.loc[:,'Январь':'Январь - Декабрь'] = month_adf.loc[:,'Январь':'Январь - Декабрь'].apply(lambda x: x.str.replace(' ', '').astype(int))
pd.DataFrame(month_adf).to_csv(r"result.csv")
