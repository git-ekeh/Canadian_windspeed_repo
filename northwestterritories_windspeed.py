#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd 
from matplotlib import pyplot as plt

#Capeparry North West Territories 

 
capeparry_nwt = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/capeparry_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_capeparry_nwt = pd.DataFrame(capeparry_nwt)

df_capeparry_nwt["Jan"] = df_capeparry_nwt["Jan"].replace(-9999.9, df_capeparry_nwt["Jan"].median())
df_capeparry_nwt["Feb"] = df_capeparry_nwt["Feb"].replace(-9999.9, df_capeparry_nwt["Feb"].median())
df_capeparry_nwt["Mar"] = df_capeparry_nwt["Mar"].replace(-9999.9, df_capeparry_nwt["Mar"].median())
df_capeparry_nwt["Apr"] = df_capeparry_nwt["Apr"].replace(-9999.9, df_capeparry_nwt["Apr"].median())
df_capeparry_nwt["May"] = df_capeparry_nwt["May"].replace(-9999.9, df_capeparry_nwt["May"].median())
df_capeparry_nwt["Jun"] = df_capeparry_nwt["Jun"].replace(-9999.9, df_capeparry_nwt["Jun"].median())
df_capeparry_nwt["Jul"] = df_capeparry_nwt["Jul"].replace(-9999.9, df_capeparry_nwt["Jul"].median())
df_capeparry_nwt["Aug"] = df_capeparry_nwt["Aug"].replace(-9999.9, df_capeparry_nwt["Aug"].median())
df_capeparry_nwt["Sep"] = df_capeparry_nwt["Sep"].replace(-9999.9, df_capeparry_nwt["Sep"].median())
df_capeparry_nwt["Oct"] = df_capeparry_nwt["Oct"].replace(-9999.9, df_capeparry_nwt["Oct"].median())
df_capeparry_nwt["Nov"] = df_capeparry_nwt["Nov"].replace(-9999.9, df_capeparry_nwt["Nov"].median())
df_capeparry_nwt["Dec"] = df_capeparry_nwt["Dec"].replace(-9999.9, df_capeparry_nwt["Dec"].median())
df_capeparry_nwt["Annual"] = df_capeparry_nwt["Annual"].replace(-9999.9, df_capeparry_nwt["Annual"].median())
df_capeparry_nwt["Winter"] = df_capeparry_nwt["Winter"].replace(-9999.9, df_capeparry_nwt["Winter"].median())
df_capeparry_nwt["Spring"] = df_capeparry_nwt["Spring"].replace(-9999.9, df_capeparry_nwt["Spring"].median())
df_capeparry_nwt["Summer"] = df_capeparry_nwt["Summer"].replace(-9999.9, df_capeparry_nwt["Summer"].median())
df_capeparry_nwt["Autumn"] = df_capeparry_nwt["Autumn"].replace(-9999.9, df_capeparry_nwt["Autumn"].median())


x1 = df_capeparry_nwt["Year"]
y1 = df_capeparry_nwt["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_capeparry_nwt["Year"]
y2 = df_capeparry_nwt["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_capeparry_nwt["Year"]
y3 = df_capeparry_nwt["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_capeparry_nwt["Year"]
y4 = df_capeparry_nwt["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Capeparry North West Territories")
plt.legend()
plt.show()

#Fort Simpson North West Territories 

fortsimpson_nwt = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/fortsimpson_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_fortsimpson_nwt = pd.DataFrame(fortsimpson_nwt)

df_fortsimpson_nwt["Oct"] = df_fortsimpson_nwt["Oct"].replace(-9999.9, df_fortsimpson_nwt["Oct"].median())
df_fortsimpson_nwt["Nov"] = df_fortsimpson_nwt["Nov"].replace(-9999.9, df_fortsimpson_nwt["Nov"].median())
df_fortsimpson_nwt["Dec"] = df_fortsimpson_nwt["Dec"].replace(-9999.9, df_fortsimpson_nwt["Dec"].median())
df_fortsimpson_nwt["Autumn"] = df_fortsimpson_nwt["Autumn"].replace(-9999.9, df_fortsimpson_nwt["Autumn"].median())

x1 = df_fortsimpson_nwt["Year"]
y1 = df_fortsimpson_nwt["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_fortsimpson_nwt["Year"]
y2 = df_fortsimpson_nwt["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_fortsimpson_nwt["Year"]
y3 = df_fortsimpson_nwt["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_fortsimpson_nwt["Year"]
y4 = df_fortsimpson_nwt["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Fort Simpson North West Territories")
plt.legend()
plt.show()

#Fort Smith North West Territories 
    
fortsmith_nwt = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/fortsmith_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_fortsmith_nwt = pd.DataFrame(fortsmith_nwt)

df_fortsmith_nwt["Oct"] = df_fortsmith_nwt["Oct"].replace(-9999.9, df_fortsmith_nwt["Oct"].median())
df_fortsmith_nwt["Nov"] = df_fortsmith_nwt["Nov"].replace(-9999.9, df_fortsmith_nwt["Nov"].median())
df_fortsmith_nwt["Dec"] = df_fortsmith_nwt["Dec"].replace(-9999.9, df_fortsmith_nwt["Dec"].median())

x1 = df_fortsmith_nwt["Year"]
y1 = df_fortsmith_nwt["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_fortsmith_nwt["Year"]
y2 = df_fortsmith_nwt["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_fortsmith_nwt["Year"]
y3 = df_fortsmith_nwt["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_fortsmith_nwt["Year"]
y4 = df_fortsmith_nwt["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Fort Smith North West Territories")
plt.legend()
plt.show()

#Hayriver North West Territories 

hayriver_nwt = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/hayriver_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_hayriver_nwt = pd.DataFrame(hayriver_nwt)

df_hayriver_nwt["Sep"] = df_hayriver_nwt["Sep"].replace(-9999.9, df_hayriver_nwt["Sep"].median())
df_hayriver_nwt["Oct"] = df_hayriver_nwt["Oct"].replace(-9999.9, df_hayriver_nwt["Oct"].median())
df_hayriver_nwt["Nov"] = df_hayriver_nwt["Nov"].replace(-9999.9, df_hayriver_nwt["Nov"].median())
df_hayriver_nwt["Dec"] = df_hayriver_nwt["Dec"].replace(-9999.9, df_hayriver_nwt["Dec"].median())
df_hayriver_nwt["May"] = df_hayriver_nwt["May"].replace(-9999.9, df_hayriver_nwt["May"].median())
df_hayriver_nwt["Autumn"] = df_hayriver_nwt["Autumn"].replace(-9999.9, df_hayriver_nwt["Autumn"].median())

x1 = df_hayriver_nwt["Year"]
y1 = df_hayriver_nwt["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_hayriver_nwt["Year"]
y2 = df_hayriver_nwt["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_hayriver_nwt["Year"]
y3 = df_hayriver_nwt["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_hayriver_nwt["Year"]
y4 = df_hayriver_nwt["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Hayriver North West Territories")
plt.legend()
plt.show()

#Inuvik North West Territories 

inuvik_nwt = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/inuvik_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_inuvik_nwt = pd.DataFrame(inuvik_nwt)

df_inuvik_nwt["Jan"] = df_inuvik_nwt["Jan"].replace(-9999.9, df_inuvik_nwt["Jan"].median())
df_inuvik_nwt["Feb"] = df_inuvik_nwt["Feb"].replace(-9999.9, df_inuvik_nwt["Feb"].median())
df_inuvik_nwt["Mar"] = df_inuvik_nwt["Mar"].replace(-9999.9, df_inuvik_nwt["Mar"].median())
df_inuvik_nwt["Apr"] = df_inuvik_nwt["Apr"].replace(-9999.9, df_inuvik_nwt["Apr"].median())
df_inuvik_nwt["May"] = df_inuvik_nwt["May"].replace(-9999.9, df_inuvik_nwt["May"].median())
df_inuvik_nwt["Jun"] = df_inuvik_nwt["Jun"].replace(-9999.9, df_inuvik_nwt["Jun"].median())
df_inuvik_nwt["Jul"] = df_inuvik_nwt["Jul"].replace(-9999.9, df_inuvik_nwt["Jul"].median())
df_inuvik_nwt["Aug"] = df_inuvik_nwt["Aug"].replace(-9999.9, df_inuvik_nwt["Aug"].median())
df_inuvik_nwt["Sep"] = df_inuvik_nwt["Sep"].replace(-9999.9, df_inuvik_nwt["Sep"].median())
df_inuvik_nwt["Oct"] = df_inuvik_nwt["Oct"].replace(-9999.9, df_inuvik_nwt["Oct"].median())
df_inuvik_nwt["Nov"] = df_inuvik_nwt["Nov"].replace(-9999.9, df_inuvik_nwt["Nov"].median())
df_inuvik_nwt["Dec"] = df_inuvik_nwt["Dec"].replace(-9999.9, df_inuvik_nwt["Dec"].median())
df_inuvik_nwt["Annual"] = df_inuvik_nwt["Annual"].replace(-9999.9, df_inuvik_nwt["Annual"].median())
df_inuvik_nwt["Winter"] = df_inuvik_nwt["Winter"].replace(-9999.9, df_inuvik_nwt["Winter"].median())
df_inuvik_nwt["Spring"] = df_inuvik_nwt["Spring"].replace(-9999.9, df_inuvik_nwt["Spring"].median())
df_inuvik_nwt["Summer"] = df_inuvik_nwt["Summer"].replace(-9999.9, df_inuvik_nwt["Summer"].median())
df_inuvik_nwt["Autumn"] = df_inuvik_nwt["Autumn"].replace(-9999.9, df_inuvik_nwt["Autumn"].median())

x1 = df_inuvik_nwt["Year"]
y1 = df_inuvik_nwt["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_inuvik_nwt["Year"]
y2 = df_inuvik_nwt["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_inuvik_nwt["Year"]
y3 = df_inuvik_nwt["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_inuvik_nwt["Year"]
y4 = df_inuvik_nwt["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Inuvik North West Territories")
plt.legend()
plt.show()

#Mouldbay North West Territories 

mouldbay_nwt = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/mouldbay_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_mouldbay_nwt = pd.DataFrame(mouldbay_nwt)

df_mouldbay_nwt["Jan"] = df_mouldbay_nwt["Jan"].replace(-9999.9, df_mouldbay_nwt["Jan"].median())
df_mouldbay_nwt["Feb"] = df_mouldbay_nwt["Feb"].replace(-9999.9, df_mouldbay_nwt["Feb"].median())
df_mouldbay_nwt["Mar"] = df_mouldbay_nwt["Mar"].replace(-9999.9, df_mouldbay_nwt["Mar"].median())
df_mouldbay_nwt["Apr"] = df_mouldbay_nwt["Apr"].replace(-9999.9, df_mouldbay_nwt["Apr"].median())
df_mouldbay_nwt["May"] = df_mouldbay_nwt["May"].replace(-9999.9, df_mouldbay_nwt["May"].median())
df_mouldbay_nwt["Jun"] = df_mouldbay_nwt["Jun"].replace(-9999.9, df_mouldbay_nwt["Jun"].median())
df_mouldbay_nwt["Jul"] = df_mouldbay_nwt["Jul"].replace(-9999.9, df_mouldbay_nwt["Jul"].median())
df_mouldbay_nwt["Aug"] = df_mouldbay_nwt["Aug"].replace(-9999.9, df_mouldbay_nwt["Aug"].median())
df_mouldbay_nwt["Sep"] = df_mouldbay_nwt["Sep"].replace(-9999.9, df_mouldbay_nwt["Sep"].median())
df_mouldbay_nwt["Oct"] = df_mouldbay_nwt["Oct"].replace(-9999.9, df_mouldbay_nwt["Oct"].median())
df_mouldbay_nwt["Nov"] = df_mouldbay_nwt["Nov"].replace(-9999.9, df_mouldbay_nwt["Nov"].median())
df_mouldbay_nwt["Dec"] = df_mouldbay_nwt["Dec"].replace(-9999.9, df_mouldbay_nwt["Dec"].median())
df_mouldbay_nwt["Annual"] = df_mouldbay_nwt["Annual"].replace(-9999.9, df_mouldbay_nwt["Annual"].median())
df_mouldbay_nwt["Winter"] = df_mouldbay_nwt["Winter"].replace(-9999.9, df_mouldbay_nwt["Winter"].median())
df_mouldbay_nwt["Spring"] = df_mouldbay_nwt["Spring"].replace(-9999.9, df_mouldbay_nwt["Spring"].median())
df_mouldbay_nwt["Summer"] = df_mouldbay_nwt["Summer"].replace(-9999.9, df_mouldbay_nwt["Summer"].median())
df_mouldbay_nwt["Autumn"] = df_mouldbay_nwt["Autumn"].replace(-9999.9, df_mouldbay_nwt["Autumn"].median())

x1 = df_mouldbay_nwt["Year"]
y1 = df_mouldbay_nwt["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_mouldbay_nwt["Year"]
y2 = df_mouldbay_nwt["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_mouldbay_nwt["Year"]
y3 = df_mouldbay_nwt["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_mouldbay_nwt["Year"]
y4 = df_mouldbay_nwt["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Mouldbay North West Territories")
plt.legend()
plt.show()

#Normalwells North West Territories 

normalwells_nwt = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/normalwells_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_normalwells_nwt = pd.DataFrame(normalwells_nwt)


df_normalwells_nwt["Oct"] = df_normalwells_nwt["Oct"].replace(-9999.9, df_normalwells_nwt["Oct"].median())

x1 = df_normalwells_nwt["Year"]
y1 = df_normalwells_nwt["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_normalwells_nwt["Year"]
y2 = df_normalwells_nwt["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_normalwells_nwt["Year"]
y3 = df_normalwells_nwt["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_normalwells_nwt["Year"]
y4 = df_normalwells_nwt["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Normalwells North West Territories")
plt.legend()
plt.show()

#Sachsharbour North West Territories 

sachsharbour_nwt = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/sachsharbour_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig' )
df_sachsharbour_nwt = pd.DataFrame(sachsharbour_nwt)

df_sachsharbour_nwt["Jan"] = df_sachsharbour_nwt["Jan"].replace(-9999.9, df_sachsharbour_nwt["Jan"].median())
df_sachsharbour_nwt["Feb"] = df_sachsharbour_nwt["Feb"].replace(-9999.9, df_sachsharbour_nwt["Feb"].median())
df_sachsharbour_nwt["Mar"] = df_sachsharbour_nwt["Mar"].replace(-9999.9, df_sachsharbour_nwt["Mar"].median())
df_sachsharbour_nwt["Apr"] = df_sachsharbour_nwt["Apr"].replace(-9999.9, df_sachsharbour_nwt["Apr"].median())
df_sachsharbour_nwt["May"] = df_sachsharbour_nwt["May"].replace(-9999.9, df_sachsharbour_nwt["May"].median())
df_sachsharbour_nwt["Jun"] = df_sachsharbour_nwt["Jun"].replace(-9999.9, df_sachsharbour_nwt["Jun"].median())
df_sachsharbour_nwt["Jul"] = df_sachsharbour_nwt["Jul"].replace(-9999.9, df_sachsharbour_nwt["Jul"].median())
df_sachsharbour_nwt["Aug"] = df_sachsharbour_nwt["Aug"].replace(-9999.9, df_sachsharbour_nwt["Aug"].median())
df_sachsharbour_nwt["Sep"] = df_sachsharbour_nwt["Sep"].replace(-9999.9, df_sachsharbour_nwt["Sep"].median())
df_sachsharbour_nwt["Oct"] = df_sachsharbour_nwt["Oct"].replace(-9999.9, df_sachsharbour_nwt["Oct"].median())
df_sachsharbour_nwt["Nov"] = df_sachsharbour_nwt["Nov"].replace(-9999.9, df_sachsharbour_nwt["Nov"].median())
df_sachsharbour_nwt["Dec"] = df_sachsharbour_nwt["Dec"].replace(-9999.9, df_sachsharbour_nwt["Dec"].median())
df_sachsharbour_nwt["Annual"] = df_sachsharbour_nwt["Annual"].replace(-9999.9, df_sachsharbour_nwt["Annual"].median())
df_sachsharbour_nwt["Winter"] = df_sachsharbour_nwt["Winter"].replace(-9999.9, df_sachsharbour_nwt["Winter"].median())
df_sachsharbour_nwt["Spring"] = df_sachsharbour_nwt["Spring"].replace(-9999.9, df_sachsharbour_nwt["Spring"].median())
df_sachsharbour_nwt["Summer"] = df_sachsharbour_nwt["Summer"].replace(-9999.9, df_sachsharbour_nwt["Summer"].median())
df_sachsharbour_nwt["Autumn"] = df_sachsharbour_nwt["Autumn"].replace(-9999.9, df_sachsharbour_nwt["Autumn"].median())

x1 = df_sachsharbour_nwt["Year"]
y1 = df_sachsharbour_nwt["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_sachsharbour_nwt["Year"]
y2 = df_sachsharbour_nwt["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_sachsharbour_nwt["Year"]
y3 = df_sachsharbour_nwt["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_sachsharbour_nwt["Year"]
y4 = df_sachsharbour_nwt["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Sachs Harbour North West Territories")
plt.legend()
plt.show()

#Tuktoyaktuk North West Territories

tuktoyaktuk_nwt = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/tuktoyaktuk_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding ='utf-8-sig')
df_tuktoyaktuk_nwt = pd.DataFrame(tuktoyaktuk_nwt)

df_tuktoyaktuk_nwt["Jan"] = df_tuktoyaktuk_nwt["Jan"].replace(-9999.9, df_tuktoyaktuk_nwt["Jan"].median())
df_tuktoyaktuk_nwt["Feb"] = df_tuktoyaktuk_nwt["Feb"].replace(-9999.9, df_tuktoyaktuk_nwt["Feb"].median())
df_tuktoyaktuk_nwt["Mar"] = df_tuktoyaktuk_nwt["Mar"].replace(-9999.9, df_tuktoyaktuk_nwt["Mar"].median())
df_tuktoyaktuk_nwt["Apr"] = df_tuktoyaktuk_nwt["Apr"].replace(-9999.9, df_tuktoyaktuk_nwt["Apr"].median())
df_tuktoyaktuk_nwt["May"] = df_tuktoyaktuk_nwt["May"].replace(-9999.9, df_tuktoyaktuk_nwt["May"].median())
df_tuktoyaktuk_nwt["Jun"] = df_tuktoyaktuk_nwt["Jun"].replace(-9999.9, df_tuktoyaktuk_nwt["Jun"].median())
df_tuktoyaktuk_nwt["Jul"] = df_tuktoyaktuk_nwt["Jul"].replace(-9999.9, df_tuktoyaktuk_nwt["Jul"].median())
df_tuktoyaktuk_nwt["Aug"] = df_tuktoyaktuk_nwt["Aug"].replace(-9999.9, df_tuktoyaktuk_nwt["Aug"].median())
df_tuktoyaktuk_nwt["Sep"] = df_tuktoyaktuk_nwt["Sep"].replace(-9999.9, df_tuktoyaktuk_nwt["Sep"].median())
df_tuktoyaktuk_nwt["Oct"] = df_tuktoyaktuk_nwt["Oct"].replace(-9999.9, df_tuktoyaktuk_nwt["Oct"].median())
df_tuktoyaktuk_nwt["Nov"] = df_tuktoyaktuk_nwt["Nov"].replace(-9999.9, df_tuktoyaktuk_nwt["Nov"].median())
df_tuktoyaktuk_nwt["Dec"] = df_tuktoyaktuk_nwt["Dec"].replace(-9999.9, df_tuktoyaktuk_nwt["Dec"].median())
df_tuktoyaktuk_nwt["Annual"] = df_tuktoyaktuk_nwt["Annual"].replace(-9999.9, df_tuktoyaktuk_nwt["Annual"].median())
df_tuktoyaktuk_nwt["Winter"] = df_tuktoyaktuk_nwt["Winter"].replace(-9999.9, df_tuktoyaktuk_nwt["Winter"].median())
df_tuktoyaktuk_nwt["Spring"] = df_tuktoyaktuk_nwt["Spring"].replace(-9999.9, df_tuktoyaktuk_nwt["Spring"].median())
df_tuktoyaktuk_nwt["Summer"] = df_tuktoyaktuk_nwt["Summer"].replace(-9999.9, df_tuktoyaktuk_nwt["Summer"].median())
df_tuktoyaktuk_nwt["Autumn"] = df_tuktoyaktuk_nwt["Autumn"].replace(-9999.9, df_tuktoyaktuk_nwt["Autumn"].median())

x1 = df_tuktoyaktuk_nwt["Year"]
y1 = df_tuktoyaktuk_nwt["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_tuktoyaktuk_nwt["Year"]
y2 = df_tuktoyaktuk_nwt["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_tuktoyaktuk_nwt["Year"]
y3 = df_tuktoyaktuk_nwt["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_tuktoyaktuk_nwt["Year"]
y4 = df_tuktoyaktuk_nwt["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Tuktoyaktuk North West Territories")
plt.legend()
plt.show()

#Yellowknife North West Territories

yellowknife_nwt = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/yellowknife_nwt_cleaned.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_yellowknife_nwt = pd.DataFrame(yellowknife_nwt)

x1 = df_yellowknife_nwt["Year"]
y1 = df_yellowknife_nwt["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_yellowknife_nwt["Year"]
y2 = df_yellowknife_nwt["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_yellowknife_nwt["Year"]
y3 = df_yellowknife_nwt["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_yellowknife_nwt["Year"]
y4 = df_yellowknife_nwt["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Yellowknife North West Territories")
plt.legend()
plt.show()