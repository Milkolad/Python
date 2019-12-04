import pandas as pd
import numpy as np
import collections
import math

df = pd.read_csv('group.tsv', sep='\t')
a = df.to_numpy()
r=np.zeros(len(a))
r2=np.zeros(len(a))

for i in range(len(a)):
    if((collections.Counter(a[i])['н'])<3):r[i]+=3;
    r[i]+=(collections.Counter(a[i])['+'])*2
    r[i]-=(collections.Counter(a[i])['-'])
    r[i]+=(collections.Counter(a[i])['+-'])+(collections.Counter(a[i])['1/2'])
    print(collections.Counter(a[i]))
    #контрольная
    str=a[i][-1].split(",")
    r[i]+=(collections.Counter(str)["+"])*2.5
    r[i]+=(collections.Counter(str)["+-"])*2
    r[i]+=(collections.Counter(str)["-+"])
    print(collections.Counter(str))
    #округление
    r[i]= math.ceil(r[i])
    if(r[i]>20):r2[i]=20;
    else: r2[i]=r[i];
    print(r[i],"\n")
    print(r2[i],"\n")
    
df["Рейтинг"] = r
df["Рейтинг20"] = r2
df.to_csv('group_res.tsv', decimal=',', sep='\t')