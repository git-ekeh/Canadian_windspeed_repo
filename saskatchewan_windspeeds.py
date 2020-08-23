#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd 
from matplotlib import pyplot as plt


#Broadview Saskatchewan 
broadview_sask = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/broadview_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_broadview_sask = pd.DataFrame(broadview_sask)

df_broadview_sask["Oct"] = df_broadview_sask["Oct"].replace(-9999.9, df_broadview_sask["Oct"].median())

x1 = df_broadview_sask["Year"]
y1 = df_broadview_sask["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_broadview_sask["Year"]
y2 = df_broadview_sask["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_broadview_sask["Year"]
y3 = df_broadview_sask["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_broadview_sask["Year"]
y4 = df_broadview_sask["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Broadview Saskatchewan")
plt.legend()
plt.show()

#Estevan Saskatchewan 

estevan_sask = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/estevan_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_estevan_sask = pd.DataFrame(estevan_sask)

x1 = df_estevan_sask["Year"]
y1 = df_estevan_sask["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_estevan_sask["Year"]
y2 = df_estevan_sask["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_estevan_sask["Year"]
y3 = df_estevan_sask["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_estevan_sask["Year"]
y4 = df_estevan_sask["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Estevan Saskatchewan")
plt.legend()
plt.show()

#Laronge Saskatchewan 

laronge_sask = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/laronge_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_laronge_sask = pd.DataFrame(laronge_sask)

df_laronge_sask["Jan"] = df_laronge_sask["Jan"].replace(-9999.9, df_laronge_sask["Jan"].median())
df_laronge_sask["Feb"] = df_laronge_sask["Feb"].replace(-9999.9, df_laronge_sask["Feb"].median())
df_laronge_sask["Mar"] = df_laronge_sask["Mar"].replace(-9999.9, df_laronge_sask["Mar"].median())
df_laronge_sask["Apr"] = df_laronge_sask["Apr"].replace(-9999.9, df_laronge_sask["Apr"].median())
df_laronge_sask["May"] = df_laronge_sask["May"].replace(-9999.9, df_laronge_sask["May"].median())
df_laronge_sask["Jun"] = df_laronge_sask["Jun"].replace(-9999.9, df_laronge_sask["Jun"].median())
df_laronge_sask["Jul"] = df_laronge_sask["Jul"].replace(-9999.9, df_laronge_sask["Jul"].median())
df_laronge_sask["Aug"] = df_laronge_sask["Aug"].replace(-9999.9, df_laronge_sask["Aug"].median())
df_laronge_sask["Sep"] = df_laronge_sask["Sep"].replace(-9999.9, df_laronge_sask["Sep"].median())
df_laronge_sask["Oct"] = df_laronge_sask["Oct"].replace(-9999.9, df_laronge_sask["Oct"].median())
df_laronge_sask["Nov"] = df_laronge_sask["Nov"].replace(-9999.9, df_laronge_sask["Nov"].median())
df_laronge_sask["Dec"] = df_laronge_sask["Dec"].replace(-9999.9, df_laronge_sask["Dec"].median())
df_laronge_sask["Annual"] = df_laronge_sask["Annual"].replace(-9999.9, df_laronge_sask["Annual"].median())
df_laronge_sask["Winter"] = df_laronge_sask["Winter"].replace(-9999.9, df_laronge_sask["Winter"].median())
df_laronge_sask["Spring"] = df_laronge_sask["Spring"].replace(-9999.9, df_laronge_sask["Spring"].median())
df_laronge_sask["Summer"] = df_laronge_sask["Summer"].replace(-9999.9, df_laronge_sask["Summer"].median())
df_laronge_sask["Autumn"] = df_laronge_sask["Autumn"].replace(-9999.9, df_laronge_sask["Autumn"].median())


x1 = df_laronge_sask["Year"]
y1 = df_laronge_sask["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_laronge_sask["Year"]
y2 = df_laronge_sask["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_laronge_sask["Year"]
y3 = df_laronge_sask["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_laronge_sask["Year"]
y4 = df_laronge_sask["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Laronge Saskatchewan")
plt.legend()
plt.show()

#Moosejaw Saskatchewan

moosejaw_sask = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/moosejaw_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_moosejaw_sask = pd.DataFrame(moosejaw_sask)

df_moosejaw_sask["Jan"] = df_moosejaw_sask["Jan"].replace(-9999.9, df_moosejaw_sask["Jan"].median())
df_moosejaw_sask["Feb"] = df_moosejaw_sask["Feb"].replace(-9999.9, df_moosejaw_sask["Feb"].median())
df_moosejaw_sask["Mar"] = df_moosejaw_sask["Mar"].replace(-9999.9, df_moosejaw_sask["Mar"].median())
df_moosejaw_sask["Apr"] = df_moosejaw_sask["Apr"].replace(-9999.9, df_moosejaw_sask["Apr"].median())
df_moosejaw_sask["May"] = df_moosejaw_sask["May"].replace(-9999.9, df_moosejaw_sask["May"].median())
df_moosejaw_sask["Jun"] = df_moosejaw_sask["Jun"].replace(-9999.9, df_moosejaw_sask["Jun"].median())
df_moosejaw_sask["Jul"] = df_moosejaw_sask["Jul"].replace(-9999.9, df_moosejaw_sask["Jul"].median())
df_moosejaw_sask["Aug"] = df_moosejaw_sask["Aug"].replace(-9999.9, df_moosejaw_sask["Aug"].median())
df_moosejaw_sask["Sep"] = df_moosejaw_sask["Sep"].replace(-9999.9, df_moosejaw_sask["Sep"].median())
df_moosejaw_sask["Oct"] = df_moosejaw_sask["Oct"].replace(-9999.9, df_moosejaw_sask["Oct"].median())
df_moosejaw_sask["Nov"] = df_moosejaw_sask["Nov"].replace(-9999.9, df_moosejaw_sask["Nov"].median())
df_moosejaw_sask["Dec"] = df_moosejaw_sask["Dec"].replace(-9999.9, df_moosejaw_sask["Dec"].median())
df_moosejaw_sask["Annual"] = df_moosejaw_sask["Annual"].replace(-9999.9, df_moosejaw_sask["Annual"].median())
df_moosejaw_sask["Winter"] = df_moosejaw_sask["Winter"].replace(-9999.9, df_moosejaw_sask["Winter"].median())
df_moosejaw_sask["Spring"] = df_moosejaw_sask["Spring"].replace(-9999.9, df_moosejaw_sask["Spring"].median())
df_moosejaw_sask["Summer"] = df_moosejaw_sask["Summer"].replace(-9999.9, df_moosejaw_sask["Summer"].median())
df_moosejaw_sask["Autumn"] = df_moosejaw_sask["Autumn"].replace(-9999.9, df_moosejaw_sask["Autumn"].median())

x1 = df_moosejaw_sask["Year"]
y1 = df_moosejaw_sask["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_moosejaw_sask["Year"]
y2 = df_moosejaw_sask["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_moosejaw_sask["Year"]
y3 = df_moosejaw_sask["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_moosejaw_sask["Year"]
y4 = df_moosejaw_sask["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Moosejaw Saskatchewan")
plt.legend()
plt.show()

#Northbattleford Saskatchewan 

northbattleford_sask = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/northbattleford_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_northbattleford_sask = pd.DataFrame(northbattleford_sask)

df_northbattleford_sask["Sep"] = df_northbattleford_sask["Sep"].replace(-9999.9, df_northbattleford_sask["Sep"].median())
df_northbattleford_sask["Oct"] = df_northbattleford_sask["Oct"].replace(-9999.9, df_northbattleford_sask["Oct"].median())
df_northbattleford_sask["Autumn"] = df_northbattleford_sask["Autumn"].replace(-9999.9, df_northbattleford_sask["Autumn"].median())

x1 = df_northbattleford_sask["Year"]
y1 = df_northbattleford_sask["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_northbattleford_sask["Year"]
y2 = df_northbattleford_sask["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_northbattleford_sask["Year"]
y3 = df_northbattleford_sask["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_northbattleford_sask["Year"]
y4 = df_northbattleford_sask["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("North Battleford Saskatchewan")
plt.legend()
plt.show()

#Prince Albert Saskatchewan 

princealbert_sask = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/princealbert_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_princealbert_sask = pd.DataFrame(princealbert_sask)

df_princealbert_sask["Oct"] = df_princealbert_sask["Oct"].replace(-9999.9, df_princealbert_sask["Oct"].median())

x1 = df_princealbert_sask["Year"]
y1 = df_princealbert_sask["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_princealbert_sask["Year"]
y2 = df_princealbert_sask["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_princealbert_sask["Year"]
y3 = df_princealbert_sask["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_princealbert_sask["Year"]
y4 = df_princealbert_sask["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Prince Albert Saskatchewan")
plt.legend()
plt.show()

#Regina Saskatchewan 

regina_sask = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/regina_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_regina_sask = pd.DataFrame(regina_sask)

x1 = df_regina_sask["Year"]
y1 = df_regina_sask["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_regina_sask["Year"]
y2 = df_regina_sask["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_regina_sask["Year"]
y3 = df_regina_sask["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_regina_sask["Year"]
y4 = df_regina_sask["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Regina Saskatchewan")
plt.legend()
plt.show()

#Saskatoon Diefenbaker Saskatchewan 

saskatoondiefenbaker_sask = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/saskatoondiefenbaker_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_saskatoondiefenbaker_sask  = pd.DataFrame(saskatoondiefenbaker_sask)

x1 = df_saskatoondiefenbaker_sask["Year"]
y1 = df_saskatoondiefenbaker_sask["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_saskatoondiefenbaker_sask["Year"]
y2 = df_saskatoondiefenbaker_sask["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_saskatoondiefenbaker_sask["Year"]
y3 = df_saskatoondiefenbaker_sask["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_saskatoondiefenbaker_sask["Year"]
y4 = df_saskatoondiefenbaker_sask["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Saskatoon Diefenbaker Saskatchewan")
plt.legend()
plt.show()

#Swiftcurrent Saskatchewan 

swiftcurrent_sask = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/swiftcurrent_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_swiftcurrent_sask = pd.DataFrame(swiftcurrent_sask)

df_swiftcurrent_sask["Oct"] = df_swiftcurrent_sask["Oct"].replace(-9999.9, df_swiftcurrent_sask["Oct"].median())

x1 = df_swiftcurrent_sask["Year"]
y1 = df_swiftcurrent_sask["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_swiftcurrent_sask["Year"]
y2 = df_swiftcurrent_sask["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_swiftcurrent_sask["Year"]
y3 = df_swiftcurrent_sask["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_swiftcurrent_sask["Year"]
y4 = df_swiftcurrent_sask["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Swiftcurrent Saskatchewan")
plt.legend()
plt.show()

#Yorkton Saskatchewan 

yorkton_sask = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/yorkton_sask_cleaned.csv",engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_yorkton_sask = pd.DataFrame(yorkton_sask)

df_yorkton_sask["Jan"] = df_yorkton_sask["Jan"].replace(-9999.9, df_yorkton_sask["Jan"].median())
df_yorkton_sask["Feb"] = df_yorkton_sask["Feb"].replace(-9999.9, df_yorkton_sask["Feb"].median())
df_yorkton_sask["Mar"] = df_yorkton_sask["Mar"].replace(-9999.9, df_yorkton_sask["Mar"].median())
df_yorkton_sask["Apr"] = df_yorkton_sask["Apr"].replace(-9999.9, df_yorkton_sask["Apr"].median())
df_yorkton_sask["May"] = df_yorkton_sask["May"].replace(-9999.9, df_yorkton_sask["May"].median())
df_yorkton_sask["Jun"] = df_yorkton_sask["Jun"].replace(-9999.9, df_yorkton_sask["Jun"].median())
df_yorkton_sask["Jul"] = df_yorkton_sask["Jul"].replace(-9999.9, df_yorkton_sask["Jul"].median())
df_yorkton_sask["Aug"] = df_yorkton_sask["Aug"].replace(-9999.9, df_yorkton_sask["Aug"].median())
df_yorkton_sask["Sep"] = df_yorkton_sask["Sep"].replace(-9999.9, df_yorkton_sask["Sep"].median())
df_yorkton_sask["Oct"] = df_yorkton_sask["Oct"].replace(-9999.9, df_yorkton_sask["Oct"].median())
df_yorkton_sask["Nov"] = df_yorkton_sask["Nov"].replace(-9999.9, df_yorkton_sask["Nov"].median())
df_yorkton_sask["Dec"] = df_yorkton_sask["Dec"].replace(-9999.9, df_yorkton_sask["Dec"].median())
df_yorkton_sask["Annual"] = df_yorkton_sask["Annual"].replace(-9999.9, df_yorkton_sask["Annual"].median())
df_yorkton_sask["Winter"] = df_yorkton_sask["Winter"].replace(-9999.9, df_yorkton_sask["Winter"].median())
df_yorkton_sask["Spring"] = df_yorkton_sask["Spring"].replace(-9999.9, df_yorkton_sask["Spring"].median())
df_yorkton_sask["Summer"] = df_yorkton_sask["Summer"].replace(-9999.9, df_yorkton_sask["Summer"].median())
df_yorkton_sask["Autumn"] = df_yorkton_sask["Autumn"].replace(-9999.9, df_yorkton_sask["Autumn"].median())

x1 = df_yorkton_sask["Year"]
y1 = df_yorkton_sask["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_yorkton_sask["Year"]
y2 = df_yorkton_sask["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_yorkton_sask["Year"]
y3 = df_yorkton_sask["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_yorkton_sask["Year"]
y4 = df_yorkton_sask["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Yorkton Saskatchewan")
plt.legend()
plt.show()

