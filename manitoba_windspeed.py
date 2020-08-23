#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd 
from matplotlib import pyplot as plt

#Brandon Manitoba
brandon_man = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/brandon_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_brandon_man = pd.DataFrame(brandon_man)

df_brandon_man["Jan"] = df_brandon_man["Jan"].replace(-9999.9, df_brandon_man["Jan"].median())
df_brandon_man["Feb"] = df_brandon_man["Feb"].replace(-9999.9, df_brandon_man["Feb"].median())
df_brandon_man["Mar"] = df_brandon_man["Mar"].replace(-9999.9, df_brandon_man["Mar"].median())
df_brandon_man["Apr"] = df_brandon_man["Apr"].replace(-9999.9, df_brandon_man["Apr"].median())
df_brandon_man["May"] = df_brandon_man["May"].replace(-9999.9, df_brandon_man["May"].median())
df_brandon_man["Jun"] = df_brandon_man["Jun"].replace(-9999.9, df_brandon_man["Jun"].median())
df_brandon_man["Jul"] = df_brandon_man["Jul"].replace(-9999.9, df_brandon_man["Jul"].median())
df_brandon_man["Aug"] = df_brandon_man["Aug"].replace(-9999.9, df_brandon_man["Aug"].median())
df_brandon_man["Sep"] = df_brandon_man["Sep"].replace(-9999.9, df_brandon_man["Sep"].median())
df_brandon_man["Oct"] = df_brandon_man["Oct"].replace(-9999.9, df_brandon_man["Oct"].median())
df_brandon_man["Nov"] = df_brandon_man["Nov"].replace(-9999.9, df_brandon_man["Nov"].median())
df_brandon_man["Dec"] = df_brandon_man["Dec"].replace(-9999.9, df_brandon_man["Dec"].median())
df_brandon_man["Annual"] = df_brandon_man["Annual"].replace(-9999.9, df_brandon_man["Annual"].median())
df_brandon_man["Winter"] = df_brandon_man["Winter"].replace(-9999.9, df_brandon_man["Winter"].median())
df_brandon_man["Spring"] = df_brandon_man["Spring"].replace(-9999.9, df_brandon_man["Spring"].median())
df_brandon_man["Summer"] = df_brandon_man["Summer"].replace(-9999.9, df_brandon_man["Summer"].median())
df_brandon_man["Autumn"] = df_brandon_man["Autumn"].replace(-9999.9, df_brandon_man["Autumn"].median())

x1 = df_brandon_man["Year"]
y1 = df_brandon_man["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_brandon_man["Year"]
y2 = df_brandon_man["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_brandon_man["Year"]
y3 = df_brandon_man["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_brandon_man["Year"]
y4 = df_brandon_man["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Brandon Manitoba")
plt.legend()
plt.show()

#Churchill Manitoba 
churchill_man = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/churchill_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_churchill_man = pd.DataFrame(churchill_man)

x1 = df_churchill_man["Year"]
y1 = df_churchill_man["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_churchill_man["Year"]
y2 = df_churchill_man["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_churchill_man["Year"]
y3 = df_churchill_man["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_churchill_man["Year"]
y4 = df_churchill_man["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Churchill Manitoba")
plt.legend()
plt.show()

#Dauphin Manitoba 

dauphin_man = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/dauphin_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_dauphin_man = pd.DataFrame(dauphin_man)

x1 = df_dauphin_man["Year"]
y1 = df_dauphin_man["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_dauphin_man["Year"]
y2 = df_dauphin_man["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_dauphin_man["Year"]
y3 = df_dauphin_man["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_dauphin_man["Year"]
y4 = df_dauphin_man["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Dauphin Manitoba")
plt.legend()
plt.show()

#Flinflon Manitoba 

flinflon_man = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/flinflon_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_flinflon_man = pd.DataFrame(flinflon_man)

df_flinflon_man["Jan"] = df_flinflon_man["Jan"].replace(-9999.9, df_flinflon_man["Jan"].median())
df_flinflon_man["Feb"] = df_flinflon_man["Feb"].replace(-9999.9, df_flinflon_man["Feb"].median())
df_flinflon_man["Mar"] = df_flinflon_man["Mar"].replace(-9999.9, df_flinflon_man["Mar"].median())
df_flinflon_man["Apr"] = df_flinflon_man["Apr"].replace(-9999.9, df_flinflon_man["Apr"].median())
df_flinflon_man["May"] = df_flinflon_man["May"].replace(-9999.9, df_flinflon_man["May"].median())
df_flinflon_man["Jun"] = df_flinflon_man["Jun"].replace(-9999.9, df_flinflon_man["Jun"].median())
df_flinflon_man["Jul"] = df_flinflon_man["Jul"].replace(-9999.9, df_flinflon_man["Jul"].median())
df_flinflon_man["Aug"] = df_flinflon_man["Aug"].replace(-9999.9, df_flinflon_man["Aug"].median())
df_flinflon_man["Sep"] = df_flinflon_man["Sep"].replace(-9999.9, df_flinflon_man["Sep"].median())
df_flinflon_man["Oct"] = df_flinflon_man["Oct"].replace(-9999.9, df_flinflon_man["Oct"].median())
df_flinflon_man["Nov"] = df_flinflon_man["Nov"].replace(-9999.9, df_flinflon_man["Nov"].median())
df_flinflon_man["Dec"] = df_flinflon_man["Dec"].replace(-9999.9, df_flinflon_man["Dec"].median())
df_flinflon_man["Annual"] = df_flinflon_man["Annual"].replace(-9999.9, df_flinflon_man["Annual"].median())
df_flinflon_man["Winter"] = df_flinflon_man["Winter"].replace(-9999.9, df_flinflon_man["Winter"].median())
df_flinflon_man["Spring"] = df_flinflon_man["Spring"].replace(-9999.9, df_flinflon_man["Spring"].median())
df_flinflon_man["Summer"] = df_flinflon_man["Summer"].replace(-9999.9, df_flinflon_man["Summer"].median())
df_flinflon_man["Autumn"] = df_flinflon_man["Autumn"].replace(-9999.9, df_flinflon_man["Autumn"].median())

x1 = df_flinflon_man["Year"]
y1 = df_flinflon_man["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_flinflon_man["Year"]
y2 = df_flinflon_man["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_flinflon_man["Year"]
y3 = df_flinflon_man["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_flinflon_man["Year"]
y4 = df_flinflon_man["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Flinflon Manitoba")
plt.legend()
plt.show()

#Gillam Manitoba 
    
gillam_man = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/gillam_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_gillam_man = pd.DataFrame(gillam_man)

df_gillam_man["Jan"] = df_gillam_man["Jan"].replace(-9999.9, df_gillam_man["Jan"].median())
df_gillam_man["Feb"] = df_gillam_man["Feb"].replace(-9999.9, df_gillam_man["Feb"].median())
df_gillam_man["Mar"] = df_gillam_man["Mar"].replace(-9999.9, df_gillam_man["Mar"].median())
df_gillam_man["Apr"] = df_gillam_man["Apr"].replace(-9999.9, df_gillam_man["Apr"].median())
df_gillam_man["May"] = df_gillam_man["May"].replace(-9999.9, df_gillam_man["May"].median())
df_gillam_man["Jun"] = df_gillam_man["Jun"].replace(-9999.9, df_gillam_man["Jun"].median())
df_gillam_man["Jul"] = df_gillam_man["Jul"].replace(-9999.9, df_gillam_man["Jul"].median())
df_gillam_man["Aug"] = df_gillam_man["Aug"].replace(-9999.9, df_gillam_man["Aug"].median())
df_gillam_man["Sep"] = df_gillam_man["Sep"].replace(-9999.9, df_gillam_man["Sep"].median())
df_gillam_man["Oct"] = df_gillam_man["Oct"].replace(-9999.9, df_gillam_man["Oct"].median())
df_gillam_man["Nov"] = df_gillam_man["Nov"].replace(-9999.9, df_gillam_man["Nov"].median())
df_gillam_man["Dec"] = df_gillam_man["Dec"].replace(-9999.9, df_gillam_man["Dec"].median())
df_gillam_man["Annual"] = df_gillam_man["Annual"].replace(-9999.9, df_gillam_man["Annual"].median())
df_gillam_man["Winter"] = df_gillam_man["Winter"].replace(-9999.9, df_gillam_man["Winter"].median())
df_gillam_man["Spring"] = df_gillam_man["Spring"].replace(-9999.9, df_gillam_man["Spring"].median())
df_gillam_man["Summer"] = df_gillam_man["Summer"].replace(-9999.9, df_gillam_man["Summer"].median())
df_gillam_man["Autumn"] = df_gillam_man["Autumn"].replace(-9999.9, df_gillam_man["Autumn"].median())

x1 = df_gillam_man["Year"]
y1 = df_gillam_man["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_gillam_man["Year"]
y2 = df_gillam_man["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_gillam_man["Year"]
y3 = df_gillam_man["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_gillam_man["Year"]
y4 = df_gillam_man["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Gillam Manitoba")
plt.legend()
plt.show()

#Island Lake Manitoba 

islandlake_man = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/islandlake_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_islandlake_man = pd.DataFrame(islandlake_man)

df_islandlake_man["Jan"] = df_islandlake_man["Jan"].replace(-9999.9, df_islandlake_man["Jan"].median())
df_islandlake_man["Feb"] = df_islandlake_man["Feb"].replace(-9999.9, df_islandlake_man["Feb"].median())
df_islandlake_man["Mar"] = df_islandlake_man["Mar"].replace(-9999.9, df_islandlake_man["Mar"].median())
df_islandlake_man["Apr"] = df_islandlake_man["Apr"].replace(-9999.9, df_islandlake_man["Apr"].median())
df_islandlake_man["May"] = df_islandlake_man["May"].replace(-9999.9, df_islandlake_man["May"].median())
df_islandlake_man["Jun"] = df_islandlake_man["Jun"].replace(-9999.9, df_islandlake_man["Jun"].median())
df_islandlake_man["Jul"] = df_islandlake_man["Jul"].replace(-9999.9, df_islandlake_man["Jul"].median())
df_islandlake_man["Aug"] = df_islandlake_man["Aug"].replace(-9999.9, df_islandlake_man["Aug"].median())
df_islandlake_man["Sep"] = df_islandlake_man["Sep"].replace(-9999.9, df_islandlake_man["Sep"].median())
df_islandlake_man["Oct"] = df_islandlake_man["Oct"].replace(-9999.9, df_islandlake_man["Oct"].median())
df_islandlake_man["Nov"] = df_islandlake_man["Nov"].replace(-9999.9, df_islandlake_man["Nov"].median())
df_islandlake_man["Dec"] = df_islandlake_man["Dec"].replace(-9999.9, df_islandlake_man["Dec"].median())
df_islandlake_man["Annual"] = df_islandlake_man["Annual"].replace(-9999.9, df_islandlake_man["Annual"].median())
df_islandlake_man["Spring"] = df_islandlake_man["Spring"].replace(-9999.9, df_islandlake_man["Spring"].median())
df_islandlake_man["Summer"] = df_islandlake_man["Summer"].replace(-9999.9, df_islandlake_man["Summer"].median())
df_islandlake_man["Autumn"] = df_islandlake_man["Autumn"].replace(-9999.9, df_islandlake_man["Autumn"].median())
df_islandlake_man["Winter"] = df_islandlake_man["Winter"].replace(-9999.9, df_islandlake_man["Winter"].median())

x1 = df_islandlake_man["Year"]
y1 = df_islandlake_man["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_islandlake_man["Year"]
y2 = df_islandlake_man["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_islandlake_man["Year"]
y3 = df_islandlake_man["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_islandlake_man["Year"]
y4 = df_islandlake_man["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Islandlake Manitoba")
plt.legend()
plt.show()

#Pilot Mound Manitoba 

pilotmound_man = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/pilotmound_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_pilotmound_man = pd.DataFrame(pilotmound_man)

df_pilotmound_man["Jan"] = df_pilotmound_man["Jan"].replace(-9999.9, df_pilotmound_man["Jan"].median())
df_pilotmound_man["Feb"] = df_pilotmound_man["Feb"].replace(-9999.9, df_pilotmound_man["Feb"].median())
df_pilotmound_man["Mar"] = df_pilotmound_man["Mar"].replace(-9999.9, df_pilotmound_man["Mar"].median())
df_pilotmound_man["Apr"] = df_pilotmound_man["Apr"].replace(-9999.9, df_pilotmound_man["Apr"].median())
df_pilotmound_man["May"] = df_pilotmound_man["May"].replace(-9999.9, df_pilotmound_man["May"].median())
df_pilotmound_man["Jun"] = df_pilotmound_man["Jun"].replace(-9999.9, df_pilotmound_man["Jun"].median())
df_pilotmound_man["Jul"] = df_pilotmound_man["Jul"].replace(-9999.9, df_pilotmound_man["Jul"].median())
df_pilotmound_man["Aug"] = df_pilotmound_man["Aug"].replace(-9999.9, df_pilotmound_man["Aug"].median())
df_pilotmound_man["Sep"] = df_pilotmound_man["Sep"].replace(-9999.9, df_pilotmound_man["Sep"].median())
df_pilotmound_man["Oct"] = df_pilotmound_man["Oct"].replace(-9999.9, df_pilotmound_man["Oct"].median())
df_pilotmound_man["Nov"] = df_pilotmound_man["Nov"].replace(-9999.9, df_pilotmound_man["Nov"].median())
df_pilotmound_man["Dec"] = df_pilotmound_man["Dec"].replace(-9999.9, df_pilotmound_man["Dec"].median())
df_pilotmound_man["Annual"] = df_pilotmound_man["Annual"].replace(-9999.9, df_pilotmound_man["Annual"].median())
df_pilotmound_man["Winter"] = df_pilotmound_man["Winter"].replace(-9999.9, df_pilotmound_man["Winter"].median())
df_pilotmound_man["Spring"] = df_pilotmound_man["Spring"].replace(-9999.9, df_pilotmound_man["Spring"].median())
df_pilotmound_man["Summer"] = df_pilotmound_man["Summer"].replace(-9999.9, df_pilotmound_man["Summer"].median())
df_pilotmound_man["Autumn"] = df_pilotmound_man["Autumn"].replace(-9999.9, df_pilotmound_man["Autumn"].median())

x1 = df_pilotmound_man["Year"]
y1 = df_pilotmound_man["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_pilotmound_man["Year"]
y2 = df_pilotmound_man["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_pilotmound_man["Year"]
y3 = df_pilotmound_man["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_pilotmound_man["Year"]
y4 = df_pilotmound_man["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Pilotmound Manitoba")
plt.legend()
plt.show()

#Thepas Manitoba

thepas_man = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/thepas_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_thepas_man = pd.DataFrame(thepas_man)

df_thepas_man["Oct"] = df_thepas_man["Oct"].replace(-9999.9, df_thepas_man["Oct"].median())
df_thepas_man["Nov"] = df_thepas_man["Nov"].replace(-9999.9, df_thepas_man["Nov"].median())
df_thepas_man["Autumn"] = df_thepas_man["Autumn"].replace(-9999.9, df_thepas_man["Autumn"].median())
df_thepas_man["Dec"] = df_thepas_man["Dec"].replace(-9999.9, df_thepas_man["Dec"].median())

x1 = df_thepas_man["Year"]
y1 = df_thepas_man["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_thepas_man["Year"]
y2 = df_thepas_man["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_thepas_man["Year"]
y3 = df_thepas_man["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_thepas_man["Year"]
y4 = df_thepas_man["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Thespas Manitoba")
plt.legend()
plt.show()

#Thompson Manitoba 

thompson_man = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/thompson_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_thompson_man = pd.DataFrame(thompson_man)

df_thompson_man["Jan"] = df_thompson_man["Jan"].replace(-9999.9, df_thompson_man["Jan"].median())
df_thompson_man["Feb"] = df_thompson_man["Feb"].replace(-9999.9, df_thompson_man["Feb"].median())
df_thompson_man["Mar"] = df_thompson_man["Mar"].replace(-9999.9, df_thompson_man["Mar"].median())
df_thompson_man["Apr"] = df_thompson_man["Apr"].replace(-9999.9, df_thompson_man["Apr"].median())
df_thompson_man["May"] = df_thompson_man["May"].replace(-9999.9, df_thompson_man["May"].median())
df_thompson_man["Jun"] = df_thompson_man["Jun"].replace(-9999.9, df_thompson_man["Jun"].median())
df_thompson_man["Jul"] = df_thompson_man["Jul"].replace(-9999.9, df_thompson_man["Jul"].median())
df_thompson_man["Aug"] = df_thompson_man["Aug"].replace(-9999.9, df_thompson_man["Aug"].median())
df_thompson_man["Sep"] = df_thompson_man["Sep"].replace(-9999.9, df_thompson_man["Sep"].median())
df_thompson_man["Oct"] = df_thompson_man["Oct"].replace(-9999.9, df_thompson_man["Oct"].median())
df_thompson_man["Nov"] = df_thompson_man["Nov"].replace(-9999.9, df_thompson_man["Nov"].median())
df_thompson_man["Dec"] = df_thompson_man["Dec"].replace(-9999.9, df_thompson_man["Dec"].median())
df_thompson_man["Annual"] = df_thompson_man["Annual"].replace(-9999.9, df_thompson_man["Annual"].median())
df_thompson_man["Winter"] = df_thompson_man["Winter"].replace(-9999.9, df_thompson_man["Winter"].median())
df_thompson_man["Spring"] = df_thompson_man["Spring"].replace(-9999.9, df_thompson_man["Spring"].median())
df_thompson_man["Summer"] = df_thompson_man["Summer"].replace(-9999.9, df_thompson_man["Summer"].median())
df_thompson_man["Autumn"] = df_thompson_man["Autumn"].replace(-9999.9, df_thompson_man["Autumn"].median())

x1 = df_thompson_man["Year"]
y1 = df_thompson_man["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_thompson_man["Year"]
y2 = df_thompson_man["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_thompson_man["Year"]
y3 = df_thompson_man["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_thompson_man["Year"]
y4 = df_thompson_man["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Thompson Manitoba")
plt.legend()
plt.show()

#Winnipeg Manitoba

winnipeg_man = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/winnipeg_man_cleaned.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_winnipeg_man = pd.DataFrame(winnipeg_man)

df_winnipeg_man["Jan"] = df_winnipeg_man["Jan"].replace(-9999.9, df_winnipeg_man["Jan"].median())
df_winnipeg_man["Feb"] = df_winnipeg_man["Feb"].replace(-9999.9, df_winnipeg_man["Feb"].median())
df_winnipeg_man["Mar"] = df_winnipeg_man["Mar"].replace(-9999.9, df_winnipeg_man["Mar"].median())
df_winnipeg_man["Apr"] = df_winnipeg_man["Apr"].replace(-9999.9, df_winnipeg_man["Apr"].median())
df_winnipeg_man["May"] = df_winnipeg_man["May"].replace(-9999.9, df_winnipeg_man["May"].median())
df_winnipeg_man["Jun"] = df_winnipeg_man["Jun"].replace(-9999.9, df_winnipeg_man["Jun"].median())
df_winnipeg_man["Jul"] = df_winnipeg_man["Jul"].replace(-9999.9, df_winnipeg_man["Jul"].median())
df_winnipeg_man["Aug"] = df_winnipeg_man["Aug"].replace(-9999.9, df_winnipeg_man["Aug"].median())
df_winnipeg_man["Sep"] = df_winnipeg_man["Sep"].replace(-9999.9, df_winnipeg_man["Sep"].median())
df_winnipeg_man["Oct"] = df_winnipeg_man["Oct"].replace(-9999.9, df_winnipeg_man["Oct"].median())
df_winnipeg_man["Nov"] = df_winnipeg_man["Nov"].replace(-9999.9, df_winnipeg_man["Nov"].median())
df_winnipeg_man["Dec"] = df_winnipeg_man["Dec"].replace(-9999.9, df_winnipeg_man["Dec"].median())
df_winnipeg_man["Annual"] = df_winnipeg_man["Annual"].replace(-9999.9, df_winnipeg_man["Annual"].median())
df_winnipeg_man["Winter"] = df_winnipeg_man["Winter"].replace(-9999.9, df_winnipeg_man["Winter"].median())
df_winnipeg_man["Spring"] = df_winnipeg_man["Spring"].replace(-9999.9, df_winnipeg_man["Spring"].median())
df_winnipeg_man["Summer"] = df_winnipeg_man["Summer"].replace(-9999.9, df_winnipeg_man["Summer"].median())
df_winnipeg_man["Autumn"] = df_winnipeg_man["Autumn"].replace(-9999.9, df_winnipeg_man["Autumn"].median())


x1 = df_winnipeg_man["Year"]
y1 = df_winnipeg_man["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_winnipeg_man["Year"]
y2 = df_winnipeg_man["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_winnipeg_man["Year"]
y3 = df_winnipeg_man["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_winnipeg_man["Year"]
y4 = df_winnipeg_man["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Winnipeg Manitoba")
plt.legend()
plt.show()