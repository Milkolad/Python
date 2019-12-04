import numpy as np
import pandas as pd
import csv

df = pd.read_csv("aircraft.csv",sep=';')
un=(df.groupby(['Вид воздушного судна',])['Тип (наименование) воздушного судна'].unique()).loc['самолет']
pd.DataFrame(un).to_csv(r"result.csv")