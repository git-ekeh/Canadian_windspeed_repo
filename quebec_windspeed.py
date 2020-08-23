#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd 
from matplotlib import pyplot as plt

#Bagotville Quebec 
bagotville_queb = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/bagotville_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_bagotville_queb = pd.DataFrame(bagotville_queb)

df_bagotville_queb["Jan"] = df_bagotville_queb["Jan"].replace(-9999.9, df_bagotville_queb["Jan"].median())
df_bagotville_queb["Feb"] = df_bagotville_queb["Feb"].replace(-9999.9, df_bagotville_queb["Feb"].median())
df_bagotville_queb["Mar"] = df_bagotville_queb["Mar"].replace(-9999.9, df_bagotville_queb["Mar"].median())
df_bagotville_queb["Apr"] = df_bagotville_queb["Apr"].replace(-9999.9, df_bagotville_queb["Apr"].median())
df_bagotville_queb["May"] = df_bagotville_queb["May"].replace(-9999.9, df_bagotville_queb["May"].median())
df_bagotville_queb["Jun"] = df_bagotville_queb["Jun"].replace(-9999.9, df_bagotville_queb["Jun"].median())
df_bagotville_queb["Jul"] = df_bagotville_queb["Jul"].replace(-9999.9, df_bagotville_queb["Jul"].median())
df_bagotville_queb["Aug"] = df_bagotville_queb["Aug"].replace(-9999.9, df_bagotville_queb["Aug"].median())
df_bagotville_queb["Sep"] = df_bagotville_queb["Sep"].replace(-9999.9, df_bagotville_queb["Sep"].median())
df_bagotville_queb["Oct"] = df_bagotville_queb["Oct"].replace(-9999.9, df_bagotville_queb["Oct"].median())
df_bagotville_queb["Nov"] = df_bagotville_queb["Nov"].replace(-9999.9, df_bagotville_queb["Nov"].median())
df_bagotville_queb["Dec"] = df_bagotville_queb["Dec"].replace(-9999.9, df_bagotville_queb["Dec"].median())
df_bagotville_queb["Annual"] = df_bagotville_queb["Annual"].replace(-9999.9, df_bagotville_queb["Annual"].median())
df_bagotville_queb["Winter"] = df_bagotville_queb["Winter"].replace(-9999.9, df_bagotville_queb["Winter"].median())
df_bagotville_queb["Spring"] = df_bagotville_queb["Spring"].replace(-9999.9, df_bagotville_queb["Spring"].median())
df_bagotville_queb["Summer"] = df_bagotville_queb["Summer"].replace(-9999.9, df_bagotville_queb["Summer"].median())
df_bagotville_queb["Autumn"] = df_bagotville_queb["Autumn"].replace(-9999.9, df_bagotville_queb["Autumn"].median())

x1 = df_bagotville_queb["Year"]
y1 = df_bagotville_queb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_bagotville_queb["Year"]
y2 = df_bagotville_queb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_bagotville_queb["Year"]
y3 = df_bagotville_queb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_bagotville_queb["Year"]
y4 = df_bagotville_queb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Bagotville Quebec")
plt.legend()
plt.show()

#Baiecomeau Quebec
baiecomeau_queb = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/baiecomeau_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_baiecomeau_queb = pd.DataFrame(baiecomeau_queb)

df_baiecomeau_queb["Jan"] = df_baiecomeau_queb["Jan"].replace(-9999.9, df_baiecomeau_queb["Jan"].median())
df_baiecomeau_queb["Feb"] = df_baiecomeau_queb["Feb"].replace(-9999.9, df_baiecomeau_queb["Feb"].median())
df_baiecomeau_queb["Mar"] = df_baiecomeau_queb["Mar"].replace(-9999.9, df_baiecomeau_queb["Mar"].median())
df_baiecomeau_queb["Apr"] = df_baiecomeau_queb["Apr"].replace(-9999.9, df_baiecomeau_queb["Apr"].median())
df_baiecomeau_queb["May"] = df_baiecomeau_queb["May"].replace(-9999.9, df_baiecomeau_queb["May"].median())
df_baiecomeau_queb["Jun"] = df_baiecomeau_queb["Jun"].replace(-9999.9, df_baiecomeau_queb["Jun"].median())
df_baiecomeau_queb["Jul"] = df_baiecomeau_queb["Jul"].replace(-9999.9, df_baiecomeau_queb["Jul"].median())
df_baiecomeau_queb["Aug"] = df_baiecomeau_queb["Aug"].replace(-9999.9, df_baiecomeau_queb["Aug"].median())
df_baiecomeau_queb["Sep"] = df_baiecomeau_queb["Sep"].replace(-9999.9, df_baiecomeau_queb["Sep"].median())
df_baiecomeau_queb["Oct"] = df_baiecomeau_queb["Oct"].replace(-9999.9, df_baiecomeau_queb["Oct"].median())
df_baiecomeau_queb["Nov"] = df_baiecomeau_queb["Nov"].replace(-9999.9, df_baiecomeau_queb["Nov"].median())
df_baiecomeau_queb["Dec"] = df_baiecomeau_queb["Dec"].replace(-9999.9, df_baiecomeau_queb["Dec"].median())
df_baiecomeau_queb["Annual"] = df_baiecomeau_queb["Annual"].replace(-9999.9, df_baiecomeau_queb["Annual"].median())
df_baiecomeau_queb["Winter"] = df_baiecomeau_queb["Winter"].replace(-9999.9, df_baiecomeau_queb["Winter"].median())
df_baiecomeau_queb["Spring"] = df_baiecomeau_queb["Spring"].replace(-9999.9, df_baiecomeau_queb["Spring"].median())
df_baiecomeau_queb["Summer"] = df_baiecomeau_queb["Summer"].replace(-9999.9, df_baiecomeau_queb["Summer"].median())
df_baiecomeau_queb["Autumn"] = df_baiecomeau_queb["Autumn"].replace(-9999.9, df_baiecomeau_queb["Autumn"].median())

x1 = df_baiecomeau_queb["Year"]
y1 = df_baiecomeau_queb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_baiecomeau_queb["Year"]
y2 = df_baiecomeau_queb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_baiecomeau_queb["Year"]
y3 = df_baiecomeau_queb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_baiecomeau_queb["Year"]
y4 = df_baiecomeau_queb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Baiecomeau Quebec")
plt.legend()
plt.show()

#Inukjuak Quebec 

inukjuak_queb = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/inukjuak_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_inukjuak_queb = pd.DataFrame(inukjuak_queb)

df_inukjuak_queb["Jan"] = df_inukjuak_queb["Jan"].replace(-9999.9, df_inukjuak_queb["Jan"].median())
df_inukjuak_queb["Feb"] = df_inukjuak_queb["Feb"].replace(-9999.9, df_inukjuak_queb["Feb"].median())
df_inukjuak_queb["Mar"] = df_inukjuak_queb["Mar"].replace(-9999.9, df_inukjuak_queb["Mar"].median())
df_inukjuak_queb["Apr"] = df_inukjuak_queb["Apr"].replace(-9999.9, df_inukjuak_queb["Apr"].median())
df_inukjuak_queb["May"] = df_inukjuak_queb["May"].replace(-9999.9, df_inukjuak_queb["May"].median())
df_inukjuak_queb["Jun"] = df_inukjuak_queb["Jun"].replace(-9999.9, df_inukjuak_queb["Jun"].median())
df_inukjuak_queb["Jul"] = df_inukjuak_queb["Jul"].replace(-9999.9, df_inukjuak_queb["Jul"].median())
df_inukjuak_queb["Aug"] = df_inukjuak_queb["Aug"].replace(-9999.9, df_inukjuak_queb["Aug"].median())
df_inukjuak_queb["Sep"] = df_inukjuak_queb["Sep"].replace(-9999.9, df_inukjuak_queb["Sep"].median())
df_inukjuak_queb["Oct"] = df_inukjuak_queb["Oct"].replace(-9999.9, df_inukjuak_queb["Oct"].median())
df_inukjuak_queb["Nov"] = df_inukjuak_queb["Nov"].replace(-9999.9, df_inukjuak_queb["Nov"].median())
df_inukjuak_queb["Dec"] = df_inukjuak_queb["Dec"].replace(-9999.9, df_inukjuak_queb["Dec"].median())
df_inukjuak_queb["Annual"] = df_inukjuak_queb["Annual"].replace(-9999.9, df_inukjuak_queb["Annual"].median())
df_inukjuak_queb["Winter"] = df_inukjuak_queb["Winter"].replace(-9999.9, df_inukjuak_queb["Winter"].median())
df_inukjuak_queb["Spring"] = df_inukjuak_queb["Spring"].replace(-9999.9, df_inukjuak_queb["Spring"].median())
df_inukjuak_queb["Summer"] = df_inukjuak_queb["Summer"].replace(-9999.9, df_inukjuak_queb["Summer"].median())
df_inukjuak_queb["Autumn"] = df_inukjuak_queb["Autumn"].replace(-9999.9, df_inukjuak_queb["Autumn"].median())

x1 = df_inukjuak_queb["Year"]
y1 = df_inukjuak_queb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_inukjuak_queb["Year"]
y2 = df_inukjuak_queb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_inukjuak_queb["Year"]
y3 = df_inukjuak_queb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_inukjuak_queb["Year"]
y4 = df_inukjuak_queb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Inukjuak Quebec")
plt.legend()
plt.show()

#Jean Lesage Airport Quebec 

jeanlesageairport_queb = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/jeanlesageairpot_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_jeanlesageairport_queb = pd.DataFrame(jeanlesageairport_queb)

x1 = df_jeanlesageairport_queb["Year"]
y1 = df_jeanlesageairport_queb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_jeanlesageairport_queb["Year"]
y2 = df_jeanlesageairport_queb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_jeanlesageairport_queb["Year"]
y3 = df_jeanlesageairport_queb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_jeanlesageairport_queb["Year"]
y4 = df_jeanlesageairport_queb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Jean Lesage Airport Quebec")
plt.legend()
plt.show()

#Kujjuuarapik Quebec

kujjuuarapik_queb = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/kujjuuarapik_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_kujjuuarapik_queb = pd.DataFrame(kujjuuarapik_queb)

df_kujjuuarapik_queb["Jan"] = df_kujjuuarapik_queb["Jan"].replace(-9999.9, df_kujjuuarapik_queb["Jan"].median())
df_kujjuuarapik_queb["Feb"] = df_kujjuuarapik_queb["Feb"].replace(-9999.9, df_kujjuuarapik_queb["Feb"].median())
df_kujjuuarapik_queb["Mar"] = df_kujjuuarapik_queb["Mar"].replace(-9999.9, df_kujjuuarapik_queb["Mar"].median())
df_kujjuuarapik_queb["Apr"] = df_kujjuuarapik_queb["Apr"].replace(-9999.9, df_kujjuuarapik_queb["Apr"].median())
df_kujjuuarapik_queb["May"] = df_kujjuuarapik_queb["May"].replace(-9999.9, df_kujjuuarapik_queb["May"].median())
df_kujjuuarapik_queb["Jun"] = df_kujjuuarapik_queb["Jun"].replace(-9999.9, df_kujjuuarapik_queb["Jun"].median())
df_kujjuuarapik_queb["Jul"] = df_kujjuuarapik_queb["Jul"].replace(-9999.9, df_kujjuuarapik_queb["Jul"].median())
df_kujjuuarapik_queb["Aug"] = df_kujjuuarapik_queb["Aug"].replace(-9999.9, df_kujjuuarapik_queb["Aug"].median())
df_kujjuuarapik_queb["Sep"] = df_kujjuuarapik_queb["Sep"].replace(-9999.9, df_kujjuuarapik_queb["Sep"].median())
df_kujjuuarapik_queb["Oct"] = df_kujjuuarapik_queb["Oct"].replace(-9999.9, df_kujjuuarapik_queb["Oct"].median())
df_kujjuuarapik_queb["Nov"] = df_kujjuuarapik_queb["Nov"].replace(-9999.9, df_kujjuuarapik_queb["Nov"].median())
df_kujjuuarapik_queb["Dec"] = df_kujjuuarapik_queb["Dec"].replace(-9999.9, df_kujjuuarapik_queb["Dec"].median())
df_kujjuuarapik_queb["Annual"] = df_kujjuuarapik_queb["Annual"].replace(-9999.9, df_kujjuuarapik_queb["Annual"].median())
df_kujjuuarapik_queb["Winter"] = df_kujjuuarapik_queb["Winter"].replace(-9999.9, df_kujjuuarapik_queb["Winter"].median())
df_kujjuuarapik_queb["Spring"] = df_kujjuuarapik_queb["Spring"].replace(-9999.9, df_kujjuuarapik_queb["Spring"].median())
df_kujjuuarapik_queb["Summer"] = df_kujjuuarapik_queb["Summer"].replace(-9999.9, df_kujjuuarapik_queb["Summer"].median())
df_kujjuuarapik_queb["Autumn"] = df_kujjuuarapik_queb["Autumn"].replace(-9999.9, df_kujjuuarapik_queb["Autumn"].median())

x1 = df_kujjuuarapik_queb["Year"]
y1 = df_kujjuuarapik_queb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_kujjuuarapik_queb["Year"]
y2 = df_kujjuuarapik_queb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_kujjuuarapik_queb["Year"]
y3 = df_kujjuuarapik_queb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_kujjuuarapik_queb["Year"]
y4 = df_kujjuuarapik_queb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Kujjuuarapik Quebec")
plt.legend()
plt.show()

#Montjoli Quebec 

montjoli_queb = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/montjoli_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding ='utf-8-sig')
df_montjoli_queb = pd.DataFrame(montjoli_queb)

df_montjoli_queb["Oct"] = df_montjoli_queb["Oct"].replace(-9999.9, df_montjoli_queb["Oct"].median())

x1 = df_montjoli_queb["Year"]
y1 = df_montjoli_queb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_montjoli_queb["Year"]
y2 = df_montjoli_queb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_montjoli_queb["Year"]
y3 = df_montjoli_queb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_montjoli_queb["Year"]
y4 = df_montjoli_queb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Montjoli Quebec")
plt.legend()
plt.show()

#Montreal Quebec 

montrealpet_queb = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/montrealpet_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_montrealpet_queb = pd.DataFrame(montrealpet_queb)

x1 = df_montrealpet_queb["Year"]
y1 = df_montrealpet_queb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_montrealpet_queb["Year"]
y2 = df_montrealpet_queb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_montrealpet_queb["Year"]
y3 = df_montrealpet_queb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_montrealpet_queb["Year"]
y4 = df_montrealpet_queb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Montrealpet Quebec")
plt.legend()
plt.show()

#Natashquan Quebec 

natashquan_queb = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/natashquan_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_natashquan_queb = pd.DataFrame(natashquan_queb)

df_natashquan_queb["Jan"] = df_natashquan_queb["Jan"].replace(-9999.9, df_natashquan_queb["Jan"].median())
df_natashquan_queb["Feb"] = df_natashquan_queb["Feb"].replace(-9999.9, df_natashquan_queb["Feb"].median())
df_natashquan_queb["Mar"] = df_natashquan_queb["Mar"].replace(-9999.9, df_natashquan_queb["Mar"].median())
df_natashquan_queb["Apr"] = df_natashquan_queb["Apr"].replace(-9999.9, df_natashquan_queb["Apr"].median())
df_natashquan_queb["May"] = df_natashquan_queb["May"].replace(-9999.9, df_natashquan_queb["May"].median())
df_natashquan_queb["Jun"] = df_natashquan_queb["Jun"].replace(-9999.9, df_natashquan_queb["Jun"].median())
df_natashquan_queb["Jul"] = df_natashquan_queb["Jul"].replace(-9999.9, df_natashquan_queb["Jul"].median())
df_natashquan_queb["Aug"] = df_natashquan_queb["Aug"].replace(-9999.9, df_natashquan_queb["Aug"].median())
df_natashquan_queb["Sep"] = df_natashquan_queb["Sep"].replace(-9999.9, df_natashquan_queb["Sep"].median())
df_natashquan_queb["Oct"] = df_natashquan_queb["Oct"].replace(-9999.9, df_natashquan_queb["Oct"].median())
df_natashquan_queb["Nov"] = df_natashquan_queb["Nov"].replace(-9999.9, df_natashquan_queb["Nov"].median())
df_natashquan_queb["Dec"] = df_natashquan_queb["Dec"].replace(-9999.9, df_natashquan_queb["Dec"].median())
df_natashquan_queb["Annual"] = df_natashquan_queb["Annual"].replace(-9999.9, df_natashquan_queb["Annual"].median())
df_natashquan_queb["Winter"] = df_natashquan_queb["Winter"].replace(-9999.9, df_natashquan_queb["Winter"].median())
df_natashquan_queb["Spring"] = df_natashquan_queb["Spring"].replace(-9999.9, df_natashquan_queb["Spring"].median())
df_natashquan_queb["Summer"] = df_natashquan_queb["Summer"].replace(-9999.9, df_natashquan_queb["Summer"].median())
df_natashquan_queb["Autumn"] = df_natashquan_queb["Autumn"].replace(-9999.9, df_natashquan_queb["Autumn"].median())

x1 = df_natashquan_queb["Year"]
y1 = df_natashquan_queb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_natashquan_queb["Year"]
y2 = df_natashquan_queb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_natashquan_queb["Year"]
y3 = df_natashquan_queb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_natashquan_queb["Year"]
y4 = df_natashquan_queb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Natashquan Quebec")
plt.legend()
plt.show()


#Rouyn Quebec 

rouyn_queb = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/rouyn_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_rouyn_queb = pd.DataFrame(rouyn_queb)

df_rouyn_queb["Jan"] = df_rouyn_queb["Jan"].replace(-9999.9, df_rouyn_queb["Jan"].median())
df_rouyn_queb["Feb"] = df_rouyn_queb["Feb"].replace(-9999.9, df_rouyn_queb["Feb"].median())
df_rouyn_queb["Mar"] = df_rouyn_queb["Mar"].replace(-9999.9, df_rouyn_queb["Mar"].median())
df_rouyn_queb["Apr"] = df_rouyn_queb["Apr"].replace(-9999.9, df_rouyn_queb["Apr"].median())
df_rouyn_queb["May"] = df_rouyn_queb["May"].replace(-9999.9, df_rouyn_queb["May"].median())
df_rouyn_queb["Jun"] = df_rouyn_queb["Jun"].replace(-9999.9, df_rouyn_queb["Jun"].median())
df_rouyn_queb["Jul"] = df_rouyn_queb["Jul"].replace(-9999.9, df_rouyn_queb["Jul"].median())
df_rouyn_queb["Aug"] = df_rouyn_queb["Aug"].replace(-9999.9, df_rouyn_queb["Aug"].median())
df_rouyn_queb["Sep"] = df_rouyn_queb["Sep"].replace(-9999.9, df_rouyn_queb["Sep"].median())
df_rouyn_queb["Oct"] = df_rouyn_queb["Oct"].replace(-9999.9, df_rouyn_queb["Oct"].median())
df_rouyn_queb["Nov"] = df_rouyn_queb["Nov"].replace(-9999.9, df_rouyn_queb["Nov"].median())
df_rouyn_queb["Dec"] = df_rouyn_queb["Dec"].replace(-9999.9, df_rouyn_queb["Dec"].median())
df_rouyn_queb["Annual"] = df_rouyn_queb["Annual"].replace(-9999.9, df_rouyn_queb["Annual"].median())
df_rouyn_queb["Winter"] = df_rouyn_queb["Winter"].replace(-9999.9, df_rouyn_queb["Winter"].median())
df_rouyn_queb["Spring"] = df_rouyn_queb["Spring"].replace(-9999.9, df_rouyn_queb["Spring"].median())
df_rouyn_queb["Summer"] = df_rouyn_queb["Summer"].replace(-9999.9, df_rouyn_queb["Summer"].median())
df_rouyn_queb["Autumn"] = df_rouyn_queb["Autumn"].replace(-9999.9, df_rouyn_queb["Autumn"].median())

x1 = df_rouyn_queb["Year"]
y1 = df_rouyn_queb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_rouyn_queb["Year"]
y2 = df_rouyn_queb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_rouyn_queb["Year"]
y3 = df_rouyn_queb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_rouyn_queb["Year"]
y4 = df_rouyn_queb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Rouyn Quebec")
plt.legend()
plt.show()

#Roverbal Quebec

roverbal_queb = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/roverbal_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_roverbal_queb = pd.DataFrame(roverbal_queb)

df_roverbal_queb["Jan"] = df_roverbal_queb["Jan"].replace(-9999.9, df_roverbal_queb["Jan"].median())
df_roverbal_queb["Feb"] = df_roverbal_queb["Feb"].replace(-9999.9, df_roverbal_queb["Feb"].median())
df_roverbal_queb["Mar"] = df_roverbal_queb["Mar"].replace(-9999.9, df_roverbal_queb["Mar"].median())
df_roverbal_queb["Apr"] = df_roverbal_queb["Apr"].replace(-9999.9, df_roverbal_queb["Apr"].median())
df_roverbal_queb["May"] = df_roverbal_queb["May"].replace(-9999.9, df_roverbal_queb["May"].median())
df_roverbal_queb["Jun"] = df_roverbal_queb["Jun"].replace(-9999.9, df_roverbal_queb["Jun"].median())
df_roverbal_queb["Jul"] = df_roverbal_queb["Jul"].replace(-9999.9, df_roverbal_queb["Jul"].median())
df_roverbal_queb["Aug"] = df_roverbal_queb["Aug"].replace(-9999.9, df_roverbal_queb["Aug"].median())
df_roverbal_queb["Sep"] = df_roverbal_queb["Sep"].replace(-9999.9, df_roverbal_queb["Sep"].median())
df_roverbal_queb["Oct"] = df_roverbal_queb["Oct"].replace(-9999.9, df_roverbal_queb["Oct"].median())
df_roverbal_queb["Nov"] = df_roverbal_queb["Nov"].replace(-9999.9, df_roverbal_queb["Nov"].median())
df_roverbal_queb["Dec"] = df_roverbal_queb["Dec"].replace(-9999.9, df_roverbal_queb["Dec"].median())
df_roverbal_queb["Annual"] = df_roverbal_queb["Annual"].replace(-9999.9, df_roverbal_queb["Annual"].median())
df_roverbal_queb["Winter"] = df_roverbal_queb["Winter"].replace(-9999.9, df_roverbal_queb["Winter"].median())
df_roverbal_queb["Spring"] = df_roverbal_queb["Spring"].replace(-9999.9, df_roverbal_queb["Spring"].median())
df_roverbal_queb["Summer"] = df_roverbal_queb["Summer"].replace(-9999.9, df_roverbal_queb["Summer"].median())
df_roverbal_queb["Autumn"] = df_roverbal_queb["Autumn"].replace(-9999.9, df_roverbal_queb["Autumn"].median())

x1 = df_roverbal_queb["Year"]
y1 = df_roverbal_queb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_roverbal_queb["Year"]
y2 = df_roverbal_queb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_roverbal_queb["Year"]
y3 = df_roverbal_queb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_roverbal_queb["Year"]
y4 = df_roverbal_queb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Roverbal Quebec")
plt.legend()
plt.show()

#Schefferville Quebec 

schefferville_queb = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/schefferville_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_schefferville_queb = pd.DataFrame(schefferville_queb)

df_schefferville_queb["Nov"] = df_schefferville_queb["Nov"].replace(-9999.9, df_schefferville_queb["Nov"].median())
df_schefferville_queb["Sep"] = df_schefferville_queb["Sep"].replace(-9999.9, df_schefferville_queb["Sep"].median())
df_schefferville_queb["Oct"] = df_schefferville_queb["Oct"].replace(-9999.9, df_schefferville_queb["Oct"].median())
df_schefferville_queb["Autumn"] = df_schefferville_queb["Autumn"].replace(-9999.9, df_schefferville_queb["Autumn"].median())

x1 = df_schefferville_queb["Year"]
y1 = df_schefferville_queb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_schefferville_queb["Year"]
y2 = df_schefferville_queb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_schefferville_queb["Year"]
y3 = df_schefferville_queb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_schefferville_queb["Year"]
y4 = df_schefferville_queb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Schefferville Quebec")
plt.legend()
plt.show()

#Septiles Quebec 

septiles_queb = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/septiles_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_septiles_queb = pd.DataFrame(septiles_queb)

df_septiles_queb["Apr"] = df_septiles_queb["Apr"].replace(-9999.9, df_septiles_queb["Apr"].median())
df_septiles_queb["May"] = df_septiles_queb["May"].replace(-9999.9, df_septiles_queb["May"].median())
df_septiles_queb["Jun"] = df_septiles_queb["Jun"].replace(-9999.9, df_septiles_queb["Jun"].median())
df_septiles_queb["Jul"] = df_septiles_queb["Jul"].replace(-9999.9, df_septiles_queb["Jul"].median())
df_septiles_queb["Aug"] = df_septiles_queb["Aug"].replace(-9999.9, df_septiles_queb["Aug"].median())
df_septiles_queb["Sep"] = df_septiles_queb["Sep"].replace(-9999.9, df_septiles_queb["Sep"].median())
df_septiles_queb["Oct"] = df_septiles_queb["Oct"].replace(-9999.9, df_septiles_queb["Oct"].median())
df_septiles_queb["Nov"] = df_septiles_queb["Nov"].replace(-9999.9, df_septiles_queb["Nov"].median())
df_septiles_queb["Dec"] = df_septiles_queb["Dec"].replace(-9999.9, df_septiles_queb["Dec"].median())
df_septiles_queb["Annual"] = df_septiles_queb["Annual"].replace(-9999.9, df_septiles_queb["Annual"].median())
df_septiles_queb["Winter"] = df_septiles_queb["Winter"].replace(-9999.9, df_septiles_queb["Winter"].median())
df_septiles_queb["Spring"] = df_septiles_queb["Spring"].replace(-9999.9, df_septiles_queb["Spring"].median())
df_septiles_queb["Summer"] = df_septiles_queb["Summer"].replace(-9999.9, df_septiles_queb["Summer"].median())
df_septiles_queb["Autumn"] = df_septiles_queb["Autumn"].replace(-9999.9, df_septiles_queb["Autumn"].median())

x1 = df_septiles_queb["Year"]
y1 = df_septiles_queb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_septiles_queb["Year"]
y2 = df_septiles_queb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_septiles_queb["Year"]
y3 = df_septiles_queb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_septiles_queb["Year"]
y4 = df_septiles_queb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Septiles Quebec")
plt.legend()
plt.show()

#Sherbrooke Quebec 

sherbrooke_queb = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/sherbrooke_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_sherbrooke_queb = pd.DataFrame(sherbrooke_queb)


df_sherbrooke_queb["Jan"] = df_sherbrooke_queb["Jan"].replace(-9999.9, df_sherbrooke_queb["Jan"].median())
df_sherbrooke_queb["Feb"] = df_sherbrooke_queb["Feb"].replace(-9999.9, df_sherbrooke_queb["Feb"].median())
df_sherbrooke_queb["Mar"] = df_sherbrooke_queb["Mar"].replace(-9999.9, df_sherbrooke_queb["Mar"].median())
df_sherbrooke_queb["Apr"] = df_sherbrooke_queb["Apr"].replace(-9999.9, df_sherbrooke_queb["Apr"].median())
df_sherbrooke_queb["May"] = df_sherbrooke_queb["May"].replace(-9999.9, df_sherbrooke_queb["May"].median())
df_sherbrooke_queb["Jun"] = df_sherbrooke_queb["Jun"].replace(-9999.9, df_sherbrooke_queb["Jun"].median())
df_sherbrooke_queb["Jul"] = df_sherbrooke_queb["Jul"].replace(-9999.9, df_sherbrooke_queb["Jul"].median())
df_sherbrooke_queb["Aug"] = df_sherbrooke_queb["Aug"].replace(-9999.9, df_sherbrooke_queb["Aug"].median())
df_sherbrooke_queb["Sep"] = df_sherbrooke_queb["Sep"].replace(-9999.9, df_sherbrooke_queb["Sep"].median())
df_sherbrooke_queb["Oct"] = df_sherbrooke_queb["Oct"].replace(-9999.9, df_sherbrooke_queb["Oct"].median())
df_sherbrooke_queb["Nov"] = df_sherbrooke_queb["Nov"].replace(-9999.9, df_sherbrooke_queb["Nov"].median())
df_sherbrooke_queb["Dec"] = df_sherbrooke_queb["Dec"].replace(-9999.9, df_sherbrooke_queb["Dec"].median())
df_sherbrooke_queb["Annual"] = df_sherbrooke_queb["Annual"].replace(-9999.9, df_sherbrooke_queb["Annual"].median())
df_sherbrooke_queb["Winter"] = df_sherbrooke_queb["Winter"].replace(-9999.9, df_sherbrooke_queb["Winter"].median())
df_sherbrooke_queb["Spring"] = df_sherbrooke_queb["Spring"].replace(-9999.9, df_sherbrooke_queb["Spring"].median())
df_sherbrooke_queb["Summer"] = df_sherbrooke_queb["Summer"].replace(-9999.9, df_sherbrooke_queb["Summer"].median())
df_sherbrooke_queb["Autumn"] = df_sherbrooke_queb["Autumn"].replace(-9999.9, df_sherbrooke_queb["Autumn"].median())


x1 = df_sherbrooke_queb["Year"]
y1 = df_sherbrooke_queb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_sherbrooke_queb["Year"]
y2 = df_sherbrooke_queb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_sherbrooke_queb["Year"]
y3 = df_sherbrooke_queb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_sherbrooke_queb["Year"]
y4 = df_sherbrooke_queb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Sherbrooke Quebec")
plt.legend()
plt.show()

#Valdor Quebec 

valdor_queb = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/valdor_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding ='utf-8-sig')
df_valdor_queb = pd.DataFrame(valdor_queb)

df_valdor_queb["Jan"] = df_valdor_queb["Jan"].replace(-9999.9, df_valdor_queb["Jan"].median())
df_valdor_queb["Feb"] = df_valdor_queb["Feb"].replace(-9999.9, df_valdor_queb["Feb"].median())
df_valdor_queb["Mar"] = df_valdor_queb["Mar"].replace(-9999.9, df_valdor_queb["Mar"].median())
df_valdor_queb["Apr"] = df_valdor_queb["Apr"].replace(-9999.9, df_valdor_queb["Apr"].median())
df_valdor_queb["May"] = df_valdor_queb["May"].replace(-9999.9, df_valdor_queb["May"].median())
df_valdor_queb["Jun"] = df_valdor_queb["Jun"].replace(-9999.9, df_valdor_queb["Jun"].median())
df_valdor_queb["Jul"] = df_valdor_queb["Jul"].replace(-9999.9, df_valdor_queb["Jul"].median())
df_valdor_queb["Aug"] = df_valdor_queb["Aug"].replace(-9999.9, df_valdor_queb["Aug"].median())
df_valdor_queb["Sep"] = df_valdor_queb["Sep"].replace(-9999.9, df_valdor_queb["Sep"].median())
df_valdor_queb["Oct"] = df_valdor_queb["Oct"].replace(-9999.9, df_valdor_queb["Oct"].median())
df_valdor_queb["Nov"] = df_valdor_queb["Nov"].replace(-9999.9, df_valdor_queb["Nov"].median())
df_valdor_queb["Dec"] = df_valdor_queb["Dec"].replace(-9999.9, df_valdor_queb["Dec"].median())
df_valdor_queb["Annual"] = df_valdor_queb["Annual"].replace(-9999.9, df_valdor_queb["Annual"].median())
df_valdor_queb["Winter"] = df_valdor_queb["Winter"].replace(-9999.9, df_valdor_queb["Winter"].median())
df_valdor_queb["Spring"] = df_valdor_queb["Spring"].replace(-9999.9, df_valdor_queb["Spring"].median())
df_valdor_queb["Summer"] = df_valdor_queb["Summer"].replace(-9999.9, df_valdor_queb["Summer"].median())
df_valdor_queb["Autumn"] = df_valdor_queb["Autumn"].replace(-9999.9, df_valdor_queb["Autumn"].median())


x1 = df_valdor_queb["Year"]
y1 = df_valdor_queb["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_valdor_queb["Year"]
y2 = df_valdor_queb["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_valdor_queb["Year"]
y3 = df_valdor_queb["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_valdor_queb["Year"]
y4 = df_valdor_queb["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Valdor Quebec")
plt.legend()
plt.show()