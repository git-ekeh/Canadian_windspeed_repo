#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd 
from matplotlib import pyplot as plt


#Fredericton New Brunswick 

fredericton_nb = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/fredericton_nb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_fredericton_nb = pd.DataFrame(fredericton_nb)

x1 = df_fredericton_nb["Year"]
y1 = df_fredericton_nb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_fredericton_nb["Year"]
y2 = df_fredericton_nb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_fredericton_nb["Year"]
y3 = df_fredericton_nb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_fredericton_nb["Year"]
y4 = df_fredericton_nb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Fredericton New Brunswick")
plt.legend()
plt.show()

#Miramichi New Brunswick 

miramichi_nb = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/miramichi_nb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_miramichi_nb = pd.DataFrame(miramichi_nb)

df_miramichi_nb["Jan"] = df_miramichi_nb["Jan"].replace(-9999.9, df_miramichi_nb["Jan"].median())
df_miramichi_nb["Feb"] = df_miramichi_nb["Feb"].replace(-9999.9, df_miramichi_nb["Feb"].median())
df_miramichi_nb["Mar"] = df_miramichi_nb["Mar"].replace(-9999.9, df_miramichi_nb["Mar"].median())
df_miramichi_nb["Apr"] = df_miramichi_nb["Apr"].replace(-9999.9, df_miramichi_nb["Apr"].median())
df_miramichi_nb["May"] = df_miramichi_nb["May"].replace(-9999.9, df_miramichi_nb["May"].median())
df_miramichi_nb["Jun"] = df_miramichi_nb["Jun"].replace(-9999.9, df_miramichi_nb["Jun"].median())
df_miramichi_nb["Jul"] = df_miramichi_nb["Jul"].replace(-9999.9, df_miramichi_nb["Jul"].median())
df_miramichi_nb["Aug"] = df_miramichi_nb["Aug"].replace(-9999.9, df_miramichi_nb["Aug"].median())
df_miramichi_nb["Sep"] = df_miramichi_nb["Sep"].replace(-9999.9, df_miramichi_nb["Sep"].median())
df_miramichi_nb["Oct"] = df_miramichi_nb["Oct"].replace(-9999.9, df_miramichi_nb["Oct"].median())
df_miramichi_nb["Nov"] = df_miramichi_nb["Nov"].replace(-9999.9, df_miramichi_nb["Nov"].median())
df_miramichi_nb["Dec"] = df_miramichi_nb["Dec"].replace(-9999.9, df_miramichi_nb["Dec"].median())
df_miramichi_nb["Annual"] = df_miramichi_nb["Annual"].replace(-9999.9, df_miramichi_nb["Annual"].median())
df_miramichi_nb["Winter"] = df_miramichi_nb["Winter"].replace(-9999.9, df_miramichi_nb["Winter"].median())
df_miramichi_nb["Spring"] = df_miramichi_nb["Spring"].replace(-9999.9, df_miramichi_nb["Spring"].median())
df_miramichi_nb["Summer"] = df_miramichi_nb["Summer"].replace(-9999.9, df_miramichi_nb["Summer"].median())
df_miramichi_nb["Autumn"] = df_miramichi_nb["Autumn"].replace(-9999.9, df_miramichi_nb["Autumn"].median())

x1 = df_miramichi_nb["Year"]
y1 = df_miramichi_nb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_miramichi_nb["Year"]
y2 = df_miramichi_nb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_miramichi_nb["Year"]
y3 = df_miramichi_nb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_miramichi_nb["Year"]
y4 = df_miramichi_nb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Miramichi New Brunswick")
plt.legend()
plt.show()

#Miscousisland New Brunswick 

miscouisland_nb= pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/miscouisland_nb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_miscouisland_nb = pd.DataFrame(miscouisland_nb)

df_miscouisland_nb["Jan"] = df_miscouisland_nb["Jan"].replace(-9999.9, df_miscouisland_nb["Jan"].median())
df_miscouisland_nb["Feb"] = df_miscouisland_nb["Feb"].replace(-9999.9, df_miscouisland_nb["Feb"].median())
df_miscouisland_nb["Mar"] = df_miscouisland_nb["Mar"].replace(-9999.9, df_miscouisland_nb["Mar"].median())
df_miscouisland_nb["Apr"] = df_miscouisland_nb["Apr"].replace(-9999.9, df_miscouisland_nb["Apr"].median())
df_miscouisland_nb["May"] = df_miscouisland_nb["May"].replace(-9999.9, df_miscouisland_nb["May"].median())
df_miscouisland_nb["Jun"] = df_miscouisland_nb["Jun"].replace(-9999.9, df_miscouisland_nb["Jun"].median())
df_miscouisland_nb["Jul"] = df_miscouisland_nb["Jul"].replace(-9999.9, df_miscouisland_nb["Jul"].median())
df_miscouisland_nb["Aug"] = df_miscouisland_nb["Aug"].replace(-9999.9, df_miscouisland_nb["Aug"].median())
df_miscouisland_nb["Sep"] = df_miscouisland_nb["Sep"].replace(-9999.9, df_miscouisland_nb["Sep"].median())
df_miscouisland_nb["Oct"] = df_miscouisland_nb["Oct"].replace(-9999.9, df_miscouisland_nb["Oct"].median())
df_miscouisland_nb["Nov"] = df_miscouisland_nb["Nov"].replace(-9999.9, df_miscouisland_nb["Nov"].median())
df_miscouisland_nb["Dec"] = df_miscouisland_nb["Dec"].replace(-9999.9, df_miscouisland_nb["Dec"].median())
df_miscouisland_nb["Annual"] = df_miscouisland_nb["Annual"].replace(-9999.9, df_miscouisland_nb["Annual"].median())
df_miscouisland_nb["Winter"] = df_miscouisland_nb["Winter"].replace(-9999.9, df_miscouisland_nb["Winter"].median())
df_miscouisland_nb["Spring"] = df_miscouisland_nb["Spring"].replace(-9999.9, df_miscouisland_nb["Spring"].median())
df_miscouisland_nb["Summer"] = df_miscouisland_nb["Summer"].replace(-9999.9, df_miscouisland_nb["Summer"].median())
df_miscouisland_nb["Autumn"] = df_miscouisland_nb["Autumn"].replace(-9999.9, df_miscouisland_nb["Autumn"].median())

x1 = df_miscouisland_nb["Year"]
y1 = df_miscouisland_nb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_miscouisland_nb["Year"]
y2 = df_miscouisland_nb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_miscouisland_nb["Year"]
y3 = df_miscouisland_nb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_miscouisland_nb["Year"]
y4 = df_miscouisland_nb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Miscou Island New Brunswick")
plt.legend()
plt.show()

#Saint John New Brunswick 

saintjohn_nb = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/saintjohn_nb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_saintjohn_nb = pd.DataFrame(saintjohn_nb)

x1 = df_saintjohn_nb["Year"]
y1 = df_saintjohn_nb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_saintjohn_nb["Year"]
y2 = df_saintjohn_nb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_saintjohn_nb["Year"]
y3 = df_saintjohn_nb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_saintjohn_nb["Year"]
y4 = df_saintjohn_nb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Saint John New Brunswick")
plt.legend()
plt.show()
