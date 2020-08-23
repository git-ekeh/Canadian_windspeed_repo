#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd 
from matplotlib import pyplot as plt

#Greenwood Nova Scotia 

greenwood_ns = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/greenwood_ns.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_greenwood_ns = pd.DataFrame(greenwood_ns)

x1 = df_greenwood_ns["Year"]
y1 = df_greenwood_ns["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_greenwood_ns["Year"]
y2 = df_greenwood_ns["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_greenwood_ns["Year"]
y3 = df_greenwood_ns["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_greenwood_ns["Year"]
y4 = df_greenwood_ns["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Greenwood Nova Scotia")
plt.legend()
plt.show()


#Sableisland Nova Scotia

sableisland_ns = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/sableisland_ns.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_sableisland_ns = pd.DataFrame(sableisland_ns)

df_sableisland_ns.dropna(axis = 1, how='all', inplace = True)
df_sableisland_ns.dropna(axis = 0, how='all', inplace = True)

df_sableisland_ns["Jan"] = df_sableisland_ns["Jan"].replace(-9999.9, df_sableisland_ns["Jan"].median())
df_sableisland_ns["Feb"] = df_sableisland_ns["Feb"].replace(-9999.9, df_sableisland_ns["Feb"].median())
df_sableisland_ns["Mar"] = df_sableisland_ns["Mar"].replace(-9999.9, df_sableisland_ns["Mar"].median())
df_sableisland_ns["Apr"] = df_sableisland_ns["Apr"].replace(-9999.9, df_sableisland_ns["Apr"].median())
df_sableisland_ns["May"] = df_sableisland_ns["May"].replace(-9999.9, df_sableisland_ns["May"].median())
df_sableisland_ns["Jun"] = df_sableisland_ns["Jun"].replace(-9999.9, df_sableisland_ns["Jun"].median())
df_sableisland_ns["Jul"] = df_sableisland_ns["Jul"].replace(-9999.9, df_sableisland_ns["Jul"].median())
df_sableisland_ns["Aug"] = df_sableisland_ns["Aug"].replace(-9999.9, df_sableisland_ns["Aug"].median())
df_sableisland_ns["Sep"] = df_sableisland_ns["Sep"].replace(-9999.9, df_sableisland_ns["Sep"].median())
df_sableisland_ns["Oct"] = df_sableisland_ns["Oct"].replace(-9999.9, df_sableisland_ns["Oct"].median())
df_sableisland_ns["Nov"] = df_sableisland_ns["Nov"].replace(-9999.9, df_sableisland_ns["Nov"].median())
df_sableisland_ns["Dec"] = df_sableisland_ns["Dec"].replace(-9999.9, df_sableisland_ns["Dec"].median())
df_sableisland_ns["Annual"] = df_sableisland_ns["Annual"].replace(-9999.9, df_sableisland_ns["Annual"].median())
df_sableisland_ns["Winter"] = df_sableisland_ns["Winter"].replace(-9999.9, df_sableisland_ns["Winter"].median())
df_sableisland_ns["Spring"] = df_sableisland_ns["Spring"].replace(-9999.9, df_sableisland_ns["Spring"].median())
df_sableisland_ns["Summer"] = df_sableisland_ns["Summer"].replace(-9999.9, df_sableisland_ns["Summer"].median())
df_sableisland_ns["Autumn"] = df_sableisland_ns["Autumn"].replace(-9999.9, df_sableisland_ns["Autumn"].median())

x1 = df_sableisland_ns["Year"]
y1 = df_sableisland_ns["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_sableisland_ns["Year"]
y2 = df_sableisland_ns["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_sableisland_ns["Year"]
y3 = df_sableisland_ns["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_sableisland_ns["Year"]
y4 = df_sableisland_ns["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Sable Island Nova Scotia")
plt.legend()
plt.show()

#Shearwater Nova Scotia 

shearwater_ns = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/shearwater_ns.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_shearwater_ns = pd.DataFrame(shearwater_ns)

df_shearwater_ns["Jan"] = df_shearwater_ns["Jan"].replace(-9999.9, df_shearwater_ns["Jan"].median())
df_shearwater_ns["Feb"] = df_shearwater_ns["Feb"].replace(-9999.9, df_shearwater_ns["Feb"].median())
df_shearwater_ns["Mar"] = df_shearwater_ns["Mar"].replace(-9999.9, df_shearwater_ns["Mar"].median())
df_shearwater_ns["Apr"] = df_shearwater_ns["Apr"].replace(-9999.9, df_shearwater_ns["Apr"].median())
df_shearwater_ns["May"] = df_shearwater_ns["May"].replace(-9999.9, df_shearwater_ns["May"].median())
df_shearwater_ns["Jun"] = df_shearwater_ns["Jun"].replace(-9999.9, df_shearwater_ns["Jun"].median())
df_shearwater_ns["Jul"] = df_shearwater_ns["Jul"].replace(-9999.9, df_shearwater_ns["Jul"].median())
df_shearwater_ns["Aug"] = df_shearwater_ns["Aug"].replace(-9999.9, df_shearwater_ns["Aug"].median())
df_shearwater_ns["Sep"] = df_shearwater_ns["Sep"].replace(-9999.9, df_shearwater_ns["Sep"].median())
df_shearwater_ns["Oct"] = df_shearwater_ns["Oct"].replace(-9999.9, df_shearwater_ns["Oct"].median())
df_shearwater_ns["Nov"] = df_shearwater_ns["Nov"].replace(-9999.9, df_shearwater_ns["Nov"].median())
df_shearwater_ns["Dec"] = df_shearwater_ns["Dec"].replace(-9999.9, df_shearwater_ns["Dec"].median())
df_shearwater_ns["Annual"] = df_shearwater_ns["Annual"].replace(-9999.9, df_shearwater_ns["Annual"].median())
df_shearwater_ns["Winter"] = df_shearwater_ns["Winter"].replace(-9999.9, df_shearwater_ns["Winter"].median())
df_shearwater_ns["Spring"] = df_shearwater_ns["Spring"].replace(-9999.9, df_shearwater_ns["Spring"].median())
df_shearwater_ns["Summer"] = df_shearwater_ns["Summer"].replace(-9999.9, df_shearwater_ns["Summer"].median())
df_shearwater_ns["Autumn"] = df_shearwater_ns["Autumn"].replace(-9999.9, df_shearwater_ns["Autumn"].median())

x1 = df_shearwater_ns["Year"]
y1 = df_shearwater_ns["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_shearwater_ns["Year"]
y2 = df_shearwater_ns["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_shearwater_ns["Year"]
y3 = df_shearwater_ns["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_shearwater_ns["Year"]
y4 = df_shearwater_ns["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Shearwater Nova Scotia")
plt.legend()
plt.show()

#Sydney Nova Scotia 

sydney_ns = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/syndney_ns.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_sydney_ns = pd.DataFrame(sydney_ns)

df_sydney_ns["Jan"] = df_sydney_ns["Jan"].replace(-9999.9, df_sydney_ns["Jan"].median())
df_sydney_ns["Feb"] = df_sydney_ns["Feb"].replace(-9999.9, df_sydney_ns["Feb"].median())
df_sydney_ns["Mar"] = df_sydney_ns["Mar"].replace(-9999.9, df_sydney_ns["Mar"].median())
df_sydney_ns["Apr"] = df_sydney_ns["Apr"].replace(-9999.9, df_sydney_ns["Apr"].median())
df_sydney_ns["May"] = df_sydney_ns["May"].replace(-9999.9, df_sydney_ns["May"].median())
df_sydney_ns["Jun"] = df_sydney_ns["Jun"].replace(-9999.9, df_sydney_ns["Jun"].median())
df_sydney_ns["Jul"] = df_sydney_ns["Jul"].replace(-9999.9, df_sydney_ns["Jul"].median())
df_sydney_ns["Aug"] = df_sydney_ns["Aug"].replace(-9999.9, df_sydney_ns["Aug"].median())
df_sydney_ns["Sep"] = df_sydney_ns["Sep"].replace(-9999.9, df_sydney_ns["Sep"].median())
df_sydney_ns["Oct"] = df_sydney_ns["Oct"].replace(-9999.9, df_sydney_ns["Oct"].median())
df_sydney_ns["Nov"] = df_sydney_ns["Nov"].replace(-9999.9, df_sydney_ns["Nov"].median())
df_sydney_ns["Dec"] = df_sydney_ns["Dec"].replace(-9999.9, df_sydney_ns["Dec"].median())
df_sydney_ns["Annual"] = df_sydney_ns["Annual"].replace(-9999.9, df_sydney_ns["Annual"].median())
df_sydney_ns["Winter"] = df_sydney_ns["Winter"].replace(-9999.9, df_sydney_ns["Winter"].median())
df_sydney_ns["Spring"] = df_sydney_ns["Spring"].replace(-9999.9, df_sydney_ns["Spring"].median())
df_sydney_ns["Summer"] = df_sydney_ns["Summer"].replace(-9999.9, df_sydney_ns["Summer"].median())
df_sydney_ns["Autumn"] = df_sydney_ns["Autumn"].replace(-9999.9, df_sydney_ns["Autumn"].median())

x1 = df_sydney_ns["Year"]
y1 = df_sydney_ns["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_sydney_ns["Year"]
y2 = df_sydney_ns["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_sydney_ns["Year"]
y3 = df_sydney_ns["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_sydney_ns["Year"]
y4 = df_sydney_ns["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Sydney Nova Scotia")
plt.legend()
plt.show()

#Westernhead Nova Scotia

westernhead_ns = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/westernhead_ns.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_westernhead_ns = pd.DataFrame(westernhead_ns)

df_westernhead_ns["Jan"] = df_westernhead_ns["Jan"].replace(-9999.9, df_westernhead_ns["Jan"].median())
df_westernhead_ns["Feb"] = df_westernhead_ns["Feb"].replace(-9999.9, df_westernhead_ns["Feb"].median())
df_westernhead_ns["Mar"] = df_westernhead_ns["Mar"].replace(-9999.9, df_westernhead_ns["Mar"].median())
df_westernhead_ns["Apr"] = df_westernhead_ns["Apr"].replace(-9999.9, df_westernhead_ns["Apr"].median())
df_westernhead_ns["May"] = df_westernhead_ns["May"].replace(-9999.9, df_westernhead_ns["May"].median())
df_westernhead_ns["Jun"] = df_westernhead_ns["Jun"].replace(-9999.9, df_westernhead_ns["Jun"].median())
df_westernhead_ns["Jul"] = df_westernhead_ns["Jul"].replace(-9999.9, df_westernhead_ns["Jul"].median())
df_westernhead_ns["Aug"] = df_westernhead_ns["Aug"].replace(-9999.9, df_westernhead_ns["Aug"].median())
df_westernhead_ns["Sep"] = df_westernhead_ns["Sep"].replace(-9999.9, df_westernhead_ns["Sep"].median())
df_westernhead_ns["Oct"] = df_westernhead_ns["Oct"].replace(-9999.9, df_westernhead_ns["Oct"].median())
df_westernhead_ns["Nov"] = df_westernhead_ns["Nov"].replace(-9999.9, df_westernhead_ns["Nov"].median())
df_westernhead_ns["Dec"] = df_westernhead_ns["Dec"].replace(-9999.9, df_westernhead_ns["Dec"].median())
df_westernhead_ns["Annual"] = df_westernhead_ns["Annual"].replace(-9999.9, df_westernhead_ns["Annual"].median())
df_westernhead_ns["Winter"] = df_westernhead_ns["Winter"].replace(-9999.9, df_westernhead_ns["Winter"].median())
df_westernhead_ns["Spring"] = df_westernhead_ns["Spring"].replace(-9999.9, df_westernhead_ns["Spring"].median())
df_westernhead_ns["Summer"] = df_westernhead_ns["Summer"].replace(-9999.9, df_westernhead_ns["Summer"].median())
df_westernhead_ns["Autumn"] = df_westernhead_ns["Autumn"].replace(-9999.9, df_westernhead_ns["Autumn"].median())

x1 = df_westernhead_ns["Year"]
y1 = df_westernhead_ns["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_westernhead_ns["Year"]
y2 = df_westernhead_ns["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_westernhead_ns["Year"]
y3 = df_westernhead_ns["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_westernhead_ns["Year"]
y4 = df_westernhead_ns["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Westernhead Nova Scotia")
plt.legend()
plt.show()

#Yarmouth Novascotia 

yarmouth_ns = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/yarmouth_ns_cleaned.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig' )
df_yarmouth_ns = pd.DataFrame(yarmouth_ns)

df_yarmouth_ns["Jan"] = df_yarmouth_ns["Jan"].replace(-9999.9, df_yarmouth_ns["Jan"].median())
df_yarmouth_ns["Feb"] = df_yarmouth_ns["Feb"].replace(-9999.9, df_yarmouth_ns["Feb"].median())
df_yarmouth_ns["Mar"] = df_yarmouth_ns["Mar"].replace(-9999.9, df_yarmouth_ns["Mar"].median())
df_yarmouth_ns["Apr"] = df_yarmouth_ns["Apr"].replace(-9999.9, df_yarmouth_ns["Apr"].median())
df_yarmouth_ns["May"] = df_yarmouth_ns["May"].replace(-9999.9, df_yarmouth_ns["May"].median())
df_yarmouth_ns["Jun"] = df_yarmouth_ns["Jun"].replace(-9999.9, df_yarmouth_ns["Jun"].median())
df_yarmouth_ns["Jul"] = df_yarmouth_ns["Jul"].replace(-9999.9, df_yarmouth_ns["Jul"].median())
df_yarmouth_ns["Aug"] = df_yarmouth_ns["Aug"].replace(-9999.9, df_yarmouth_ns["Aug"].median())
df_yarmouth_ns["Sep"] = df_yarmouth_ns["Sep"].replace(-9999.9, df_yarmouth_ns["Sep"].median())
df_yarmouth_ns["Oct"] = df_yarmouth_ns["Oct"].replace(-9999.9, df_yarmouth_ns["Oct"].median())
df_yarmouth_ns["Nov"] = df_yarmouth_ns["Nov"].replace(-9999.9, df_yarmouth_ns["Nov"].median())
df_yarmouth_ns["Dec"] = df_yarmouth_ns["Dec"].replace(-9999.9, df_yarmouth_ns["Dec"].median())
df_yarmouth_ns["Annual"] = df_yarmouth_ns["Annual"].replace(-9999.9, df_yarmouth_ns["Annual"].median())
df_yarmouth_ns["Winter"] = df_yarmouth_ns["Winter"].replace(-9999.9, df_yarmouth_ns["Winter"].median())
df_yarmouth_ns["Spring"] = df_yarmouth_ns["Spring"].replace(-9999.9, df_yarmouth_ns["Spring"].median())
df_yarmouth_ns["Summer"] = df_yarmouth_ns["Summer"].replace(-9999.9, df_yarmouth_ns["Summer"].median())
df_yarmouth_ns["Autumn"] = df_yarmouth_ns["Autumn"].replace(-9999.9, df_yarmouth_ns["Autumn"].median())

x1 = df_yarmouth_ns["Year"]
y1 = df_yarmouth_ns["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_yarmouth_ns["Year"]
y2 = df_yarmouth_ns["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_yarmouth_ns["Year"]
y3 = df_yarmouth_ns["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_yarmouth_ns["Year"]
y4 = df_yarmouth_ns["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Yarmouth Nova Scotia")
plt.legend()
plt.show()

