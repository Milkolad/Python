import numpy as np
import pandas as pd

df = pd.read_csv('./aircraft.csv', sep=';', parse_dates=['дата действующего свидетельства о регистрации'])
print(df.loc[df['дата действующего свидетельства о регистрации'].index.min(), ['Тип (наименование) воздушного судна']])
