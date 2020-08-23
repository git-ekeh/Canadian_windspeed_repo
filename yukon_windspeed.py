#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd 
from matplotlib import pyplot as plt

#Burwash Yukon Territories 

burwash_yt = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/burwash_yt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_burwash_yt = pd.DataFrame(burwash_yt)

df_burwash_yt["Jan"] = df_burwash_yt["Jan"].replace(-9999.9, df_burwash_yt["Jan"].median())
df_burwash_yt["Feb"] = df_burwash_yt["Feb"].replace(-9999.9, df_burwash_yt["Feb"].median())
df_burwash_yt["Mar"] = df_burwash_yt["Mar"].replace(-9999.9, df_burwash_yt["Mar"].median())
df_burwash_yt["Apr"] = df_burwash_yt["Apr"].replace(-9999.9, df_burwash_yt["Apr"].median())
df_burwash_yt["May"] = df_burwash_yt["May"].replace(-9999.9, df_burwash_yt["May"].median())
df_burwash_yt["Jun"] = df_burwash_yt["Jun"].replace(-9999.9, df_burwash_yt["Jun"].median())
df_burwash_yt["Jul"] = df_burwash_yt["Jul"].replace(-9999.9, df_burwash_yt["Jul"].median())
df_burwash_yt["Aug"] = df_burwash_yt["Aug"].replace(-9999.9, df_burwash_yt["Aug"].median())
df_burwash_yt["Sep"] = df_burwash_yt["Sep"].replace(-9999.9, df_burwash_yt["Sep"].median())
df_burwash_yt["Oct"] = df_burwash_yt["Oct"].replace(-9999.9, df_burwash_yt["Oct"].median())
df_burwash_yt["Nov"] = df_burwash_yt["Nov"].replace(-9999.9, df_burwash_yt["Nov"].median())
df_burwash_yt["Dec"] = df_burwash_yt["Dec"].replace(-9999.9, df_burwash_yt["Dec"].median())
df_burwash_yt["Annual"] = df_burwash_yt["Annual"].replace(-9999.9, df_burwash_yt["Annual"].median())
df_burwash_yt["Winter"] = df_burwash_yt["Winter"].replace(-9999.9, df_burwash_yt["Winter"].median())
df_burwash_yt["Spring"] = df_burwash_yt["Spring"].replace(-9999.9, df_burwash_yt["Spring"].median())
df_burwash_yt["Summer"] = df_burwash_yt["Summer"].replace(-9999.9, df_burwash_yt["Summer"].median())
df_burwash_yt["Autumn"] = df_burwash_yt["Autumn"].replace(-9999.9, df_burwash_yt["Autumn"].median())

x1 = df_burwash_yt["Year"]
y1 = df_burwash_yt["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_burwash_yt["Year"]
y2 = df_burwash_yt["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_burwash_yt["Year"]
y3 = df_burwash_yt["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_burwash_yt["Year"]
y4 = df_burwash_yt["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Burwash Yukon Territories")
plt.legend()
plt.show()

#Mayo Yukon Territories 

mayo_yt = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/mayo_yt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_mayo_yt = pd.DataFrame(mayo_yt)

df_mayo_yt["Apr"] = df_mayo_yt["Apr"].replace(-9999.9, df_mayo_yt["Apr"].median())
df_mayo_yt["May"] = df_mayo_yt["May"].replace(-9999.9, df_mayo_yt["Apr"].median())
df_mayo_yt["Oct"] = df_mayo_yt["Oct"].replace(-9999.9, df_mayo_yt["Oct"].median())
df_mayo_yt["Spring"] = df_mayo_yt["Spring"].replace(-9999.9, df_mayo_yt["Spring"].median())

x1 = df_mayo_yt["Year"]
y1 = df_mayo_yt["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_mayo_yt["Year"]
y2 = df_mayo_yt["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_mayo_yt["Year"]
y3 = df_mayo_yt["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_mayo_yt["Year"]
y4 = df_mayo_yt["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Mayo Yukon Terrirtories")
plt.legend()
plt.show()

#Teslin Yukon Territories 

teslin_yt = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/teslin_yt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_teslin_yt = pd.DataFrame(teslin_yt)

df_teslin_yt["Jan"] = df_teslin_yt["Jan"].replace(-9999.9, df_teslin_yt["Jan"].median())
df_teslin_yt["Feb"] = df_teslin_yt["Feb"].replace(-9999.9, df_teslin_yt["Feb"].median())
df_teslin_yt["Mar"] = df_teslin_yt["Mar"].replace(-9999.9, df_teslin_yt["Mar"].median())
df_teslin_yt["Apr"] = df_teslin_yt["Apr"].replace(-9999.9, df_teslin_yt["Apr"].median())
df_teslin_yt["May"] = df_teslin_yt["May"].replace(-9999.9, df_teslin_yt["May"].median())
df_teslin_yt["Jun"] = df_teslin_yt["Jun"].replace(-9999.9, df_teslin_yt["Jun"].median())
df_teslin_yt["Jul"] = df_teslin_yt["Jul"].replace(-9999.9, df_teslin_yt["Jul"].median())
df_teslin_yt["Aug"] = df_teslin_yt["Aug"].replace(-9999.9, df_teslin_yt["Aug"].median())
df_teslin_yt["Sep"] = df_teslin_yt["Sep"].replace(-9999.9, df_teslin_yt["Sep"].median())
df_teslin_yt["Oct"] = df_teslin_yt["Oct"].replace(-9999.9, df_teslin_yt["Oct"].median())
df_teslin_yt["Nov"] = df_teslin_yt["Nov"].replace(-9999.9, df_teslin_yt["Nov"].median())
df_teslin_yt["Dec"] = df_teslin_yt["Dec"].replace(-9999.9, df_teslin_yt["Dec"].median())
df_teslin_yt["Annual"] = df_teslin_yt["Annual"].replace(-9999.9, df_teslin_yt["Annual"].median())
df_teslin_yt["Winter"] = df_teslin_yt["Winter"].replace(-9999.9, df_teslin_yt["Winter"].median())
df_teslin_yt["Spring"] = df_teslin_yt["Spring"].replace(-9999.9, df_teslin_yt["Spring"].median())
df_teslin_yt["Summer"] = df_teslin_yt["Summer"].replace(-9999.9, df_teslin_yt["Summer"].median())
df_teslin_yt["Autumn"] = df_teslin_yt["Autumn"].replace(-9999.9, df_teslin_yt["Autumn"].median())

x1 = df_teslin_yt["Year"]
y1 = df_teslin_yt["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_teslin_yt["Year"]
y2 = df_teslin_yt["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_teslin_yt["Year"]
y3 = df_teslin_yt["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_teslin_yt["Year"]
y4 = df_teslin_yt["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Teslin Yukon Territories")
plt.legend()
plt.show()

#Watsonlake Yukon Territories 

watsonlake_yt = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/watsonlake_yt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_watsonlake_yt = pd.DataFrame(watsonlake_yt)

df_watsonlake_yt["Jan"] = df_watsonlake_yt["Jan"].replace(-9999.9, df_watsonlake_yt["Jan"].median())
df_watsonlake_yt["Feb"] = df_watsonlake_yt["Feb"].replace(-9999.9, df_watsonlake_yt["Feb"].median())
df_watsonlake_yt["Oct"] = df_watsonlake_yt["Oct"].replace(-9999.9, df_watsonlake_yt["Oct"].median())
df_watsonlake_yt["Nov"] = df_watsonlake_yt["Nov"].replace(-9999.9, df_watsonlake_yt["Nov"].median())
df_watsonlake_yt["Dec"] = df_watsonlake_yt["Dec"].replace(-9999.9, df_watsonlake_yt["Dec"].median())
df_watsonlake_yt["Winter"] = df_watsonlake_yt["Winter"].replace(-9999.9, df_watsonlake_yt["Winter"].median())

x1 = df_watsonlake_yt["Year"]
y1 = df_watsonlake_yt["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_watsonlake_yt["Year"]
y2 = df_watsonlake_yt["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_watsonlake_yt["Year"]
y3 = df_watsonlake_yt["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_watsonlake_yt["Year"]
y4 = df_watsonlake_yt["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Watson Yukon Territories")
plt.legend()
plt.show()

#Whitehourse Yukon Territories 

whitehorse_yt = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/whitehorse_yt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_whitehorse_yt = pd.DataFrame(whitehorse_yt)

x1 = df_whitehorse_yt["Year"]
y1 = df_whitehorse_yt["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_whitehorse_yt["Year"]
y2 = df_whitehorse_yt["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_whitehorse_yt["Year"]
y3 = df_whitehorse_yt["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_whitehorse_yt["Year"]
y4 = df_whitehorse_yt["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Whitehorse Yukon Territories")
plt.legend()
plt.show()
