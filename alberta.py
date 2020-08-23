#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd 
from matplotlib import pyplot as plt

#Calgary Alberta

calgary_alber = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/calgary_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_calgary_alber = pd.DataFrame(calgary_alber)
 
x1 = df_calgary_alber["Year"]
y1 = df_calgary_alber["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_calgary_alber["Year"]
y2 = df_calgary_alber["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_calgary_alber["Year"]
y3 = df_calgary_alber["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_calgary_alber["Year"]
y4 = df_calgary_alber["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Calgary Alberta")
plt.legend()
plt.show()

#Coldlake Alberta    
coldlake_alber = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/coldlake_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_coldlake_alber = pd.DataFrame(coldlake_alber)

df_coldlake_alber["Jan"] = df_coldlake_alber["Jan"].replace(-9999.9, df_coldlake_alber["Jan"].median())
df_coldlake_alber["Feb"] = df_coldlake_alber["Feb"].replace(-9999.9, df_coldlake_alber["Feb"].median())
df_coldlake_alber["Mar"] = df_coldlake_alber["Mar"].replace(-9999.9, df_coldlake_alber["Mar"].median())
df_coldlake_alber["Apr"] = df_coldlake_alber["Apr"].replace(-9999.9, df_coldlake_alber["Apr"].median())
df_coldlake_alber["May"] = df_coldlake_alber["May"].replace(-9999.9, df_coldlake_alber["May"].median())
df_coldlake_alber["Jun"] = df_coldlake_alber["Jun"].replace(-9999.9, df_coldlake_alber["Jun"].median())
df_coldlake_alber["Jul"] = df_coldlake_alber["Jul"].replace(-9999.9, df_coldlake_alber["Jul"].median())
df_coldlake_alber["Aug"] = df_coldlake_alber["Aug"].replace(-9999.9, df_coldlake_alber["Aug"].median())
df_coldlake_alber["Sep"] = df_coldlake_alber["Sep"].replace(-9999.9, df_coldlake_alber["Sep"].median())
df_coldlake_alber["Oct"] = df_coldlake_alber["Oct"].replace(-9999.9, df_coldlake_alber["Oct"].median())
df_coldlake_alber["Nov"] = df_coldlake_alber["Nov"].replace(-9999.9, df_coldlake_alber["Nov"].median())
df_coldlake_alber["Dec"] = df_coldlake_alber["Dec"].replace(-9999.9, df_coldlake_alber["Dec"].median())
df_coldlake_alber["Annual"] = df_coldlake_alber["Annual"].replace(-9999.9, df_coldlake_alber["Annual"].median())
df_coldlake_alber["Winter"] = df_coldlake_alber["Winter"].replace(-9999.9, df_coldlake_alber["Winter"].median())
df_coldlake_alber["Spring"] = df_coldlake_alber["Spring"].replace(-9999.9, df_coldlake_alber["Spring"].median())
df_coldlake_alber["Summer"] = df_coldlake_alber["Summer"].replace(-9999.9, df_coldlake_alber["Summer"].median())
df_coldlake_alber["Autumn"] = df_coldlake_alber["Autumn"].replace(-9999.9, df_coldlake_alber["Autumn"].median())

x1 = df_coldlake_alber["Year"]
y1 = df_coldlake_alber["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_coldlake_alber["Year"]
y2 = df_coldlake_alber["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_coldlake_alber["Year"]
y3 = df_coldlake_alber["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_coldlake_alber["Year"]
y4 = df_coldlake_alber["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')


plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Coldlake Alberta")
plt.legend()
plt.show()


#Coronation Alberta 
    
coronation_alber = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/coronation_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding= 'utf-8-sig')
df_coronation_alber = pd.DataFrame(coronation_alber)

df_coronation_alber["Dec"] = df_coronation_alber["Dec"].replace(-9999.9, df_coronation_alber["Dec"].median())

x1 = df_coronation_alber["Year"]
y1 = df_coronation_alber["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_coronation_alber["Year"]
y2 = df_coronation_alber["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_coronation_alber["Year"]
y3 = df_coronation_alber["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_coronation_alber["Year"]
y4 = df_coronation_alber["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Coranation Alberta")
plt.legend()
plt.show()

#Edmonton Alberta

edmonton_alber = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/edmonton_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_edmonton_alber = pd.DataFrame(edmonton_alber)

df_edmonton_alber["Jan"] = df_edmonton_alber["Jan"].replace(-9999.9, df_edmonton_alber["Jan"].median())
df_edmonton_alber["Feb"] = df_edmonton_alber["Feb"].replace(-9999.9, df_edmonton_alber["Feb"].median())
df_edmonton_alber["Mar"] = df_edmonton_alber["Mar"].replace(-9999.9, df_edmonton_alber["Mar"].median())
df_edmonton_alber["Apr"] = df_edmonton_alber["Apr"].replace(-9999.9, df_edmonton_alber["Apr"].median())
df_edmonton_alber["May"] = df_edmonton_alber["May"].replace(-9999.9, df_edmonton_alber["May"].median())
df_edmonton_alber["Jun"] = df_edmonton_alber["Jun"].replace(-9999.9, df_edmonton_alber["Jun"].median())
df_edmonton_alber["Jul"] = df_edmonton_alber["Jul"].replace(-9999.9, df_edmonton_alber["Jul"].median())
df_edmonton_alber["Aug"] = df_edmonton_alber["Aug"].replace(-9999.9, df_edmonton_alber["Aug"].median())
df_edmonton_alber["Sep"] = df_edmonton_alber["Sep"].replace(-9999.9, df_edmonton_alber["Sep"].median())
df_edmonton_alber["Oct"] = df_edmonton_alber["Oct"].replace(-9999.9, df_edmonton_alber["Oct"].median())
df_edmonton_alber["Nov"] = df_edmonton_alber["Nov"].replace(-9999.9, df_edmonton_alber["Nov"].median())
df_edmonton_alber["Dec"] = df_edmonton_alber["Dec"].replace(-9999.9, df_edmonton_alber["Dec"].median())
df_edmonton_alber["Annual"] = df_edmonton_alber["Annual"].replace(-9999.9, df_edmonton_alber["Annual"].median())
df_edmonton_alber["Winter"] = df_edmonton_alber["Winter"].replace(-9999.9, df_edmonton_alber["Winter"].median())
df_edmonton_alber["Spring"] = df_edmonton_alber["Spring"].replace(-9999.9, df_edmonton_alber["Spring"].median())
df_edmonton_alber["Summer"] = df_edmonton_alber["Summer"].replace(-9999.9, df_edmonton_alber["Summer"].median())
df_edmonton_alber["Autumn"] = df_edmonton_alber["Autumn"].replace(-9999.9, df_edmonton_alber["Autumn"].median())
 
x1 = df_edmonton_alber["Year"]
y1 = df_edmonton_alber["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_edmonton_alber["Year"]
y2 = df_edmonton_alber["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_edmonton_alber["Year"]
y3 = df_edmonton_alber["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_edmonton_alber["Year"]
y4 = df_edmonton_alber["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')



plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Edmonton Alberta")
plt.legend()
plt.show()

#Edmonton City Centre Alberta 

edmontoncitycentre_alber = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/edmontoncitycentre_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_edmontoncitycentre_alber = pd.DataFrame(edmontoncitycentre_alber)
   
x1 = df_edmontoncitycentre_alber["Year"]
y1 = df_edmontoncitycentre_alber["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_edmontoncitycentre_alber["Year"]
y2 = df_edmontoncitycentre_alber["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_edmontoncitycentre_alber["Year"]
y3 = df_edmontoncitycentre_alber["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_edmontoncitycentre_alber["Year"]
y4 = df_edmontoncitycentre_alber["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')



plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Edmonton City Centre Alberta")
plt.legend()
plt.show()

#Edmontonnamao Alberta 

edmontonnamao_alber = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/edmontonnamao_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_edmontonnamao_alber = pd.DataFrame(edmontonnamao_alber)

df_edmontonnamao_alber["Jan"] = df_edmontonnamao_alber["Jan"].replace(-9999.9, df_edmontonnamao_alber["Jan"].median())
df_edmontonnamao_alber["Feb"] = df_edmontonnamao_alber["Feb"].replace(-9999.9, df_edmontonnamao_alber["Feb"].median())
df_edmontonnamao_alber["Mar"] = df_edmontonnamao_alber["Mar"].replace(-9999.9, df_edmontonnamao_alber["Mar"].median())
df_edmontonnamao_alber["Apr"] = df_edmontonnamao_alber["Apr"].replace(-9999.9, df_edmontonnamao_alber["Apr"].median())
df_edmontonnamao_alber["May"] = df_edmontonnamao_alber["May"].replace(-9999.9, df_edmontonnamao_alber["May"].median())
df_edmontonnamao_alber["Jun"] = df_edmontonnamao_alber["Jun"].replace(-9999.9, df_edmontonnamao_alber["Jun"].median())
df_edmontonnamao_alber["Jul"] = df_edmontonnamao_alber["Jul"].replace(-9999.9, df_edmontonnamao_alber["Jul"].median())
df_edmontonnamao_alber["Aug"] = df_edmontonnamao_alber["Aug"].replace(-9999.9, df_edmontonnamao_alber["Aug"].median())
df_edmontonnamao_alber["Sep"] = df_edmontonnamao_alber["Sep"].replace(-9999.9, df_edmontonnamao_alber["Sep"].median())
df_edmontonnamao_alber["Oct"] = df_edmontonnamao_alber["Oct"].replace(-9999.9, df_edmontonnamao_alber["Oct"].median())
df_edmontonnamao_alber["Nov"] = df_edmontonnamao_alber["Nov"].replace(-9999.9, df_edmontonnamao_alber["Nov"].median())
df_edmontonnamao_alber["Dec"] = df_edmontonnamao_alber["Dec"].replace(-9999.9, df_edmontonnamao_alber["Dec"].median())
df_edmontonnamao_alber["Annual"] = df_edmontonnamao_alber["Annual"].replace(-9999.9, df_edmontonnamao_alber["Annual"].median())
df_edmontonnamao_alber["Winter"] = df_edmontonnamao_alber["Winter"].replace(-9999.9, df_edmontonnamao_alber["Winter"].median())
df_edmontonnamao_alber["Spring"] = df_edmontonnamao_alber["Spring"].replace(-9999.9, df_edmontonnamao_alber["Spring"].median())
df_edmontonnamao_alber["Summer"] = df_edmontonnamao_alber["Summer"].replace(-9999.9, df_edmontonnamao_alber["Summer"].median())
df_edmontonnamao_alber["Autumn"] = df_edmontonnamao_alber["Autumn"].replace(-9999.9, df_edmontonnamao_alber["Autumn"].median())

x1 = df_edmontonnamao_alber["Year"]
y1 = df_edmontonnamao_alber["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_edmontonnamao_alber["Year"]
y2 = df_edmontonnamao_alber["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_edmontonnamao_alber["Year"]
y3 = df_edmontonnamao_alber["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_edmontonnamao_alber["Year"]
y4 = df_edmontonnamao_alber["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')



plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Edmontonnamao Alberta")
plt.legend()
plt.show()

#Fortmcmurray Alberta 

fortmcmurray_alber = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/fortmcmurray_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_fortmcmurray_alber = pd.DataFrame(fortmcmurray_alber)

x1 = df_fortmcmurray_alber["Year"]
y1 = df_fortmcmurray_alber["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_fortmcmurray_alber["Year"]
y2 = df_fortmcmurray_alber["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_fortmcmurray_alber["Year"]
y3 = df_fortmcmurray_alber["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_fortmcmurray_alber["Year"]
y4 = df_fortmcmurray_alber["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')



plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Fort McMurray Alberta")
plt.legend()
plt.show()

#Grand Prarie Alberta

grandprairie_alber = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/grandprairie_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_grandprairie_alber = pd.DataFrame(grandprairie_alber)

x1 = df_grandprairie_alber["Year"]
y1 = df_grandprairie_alber["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_grandprairie_alber["Year"]
y2 = df_grandprairie_alber["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_grandprairie_alber["Year"]
y3 = df_grandprairie_alber["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_grandprairie_alber["Year"]
y4 = df_grandprairie_alber["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')



plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Grandprairie Alberta")
plt.legend()
plt.show()

#Highlevel Alberta 

highlevel_alber = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds//highlevel_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_highlevel_alber = pd.DataFrame(highlevel_alber)

df_highlevel_alber["Jan"] = df_highlevel_alber["Jan"].replace(-9999.9, df_highlevel_alber["Jan"].median())
df_highlevel_alber["Feb"] = df_highlevel_alber["Feb"].replace(-9999.9, df_highlevel_alber["Feb"].median())
df_highlevel_alber["Mar"] = df_highlevel_alber["Mar"].replace(-9999.9, df_highlevel_alber["Mar"].median())
df_highlevel_alber["Apr"] = df_highlevel_alber["Apr"].replace(-9999.9, df_highlevel_alber["Apr"].median())
df_highlevel_alber["May"] = df_highlevel_alber["May"].replace(-9999.9, df_highlevel_alber["May"].median())
df_highlevel_alber["Jun"] = df_highlevel_alber["Jun"].replace(-9999.9, df_highlevel_alber["Jun"].median())
df_highlevel_alber["Jul"] = df_highlevel_alber["Jul"].replace(-9999.9, df_highlevel_alber["Jul"].median())
df_highlevel_alber["Aug"] = df_highlevel_alber["Aug"].replace(-9999.9, df_highlevel_alber["Aug"].median())
df_highlevel_alber["Sep"] = df_highlevel_alber["Sep"].replace(-9999.9, df_highlevel_alber["Sep"].median())
df_highlevel_alber["Oct"] = df_highlevel_alber["Oct"].replace(-9999.9, df_highlevel_alber["Oct"].median())
df_highlevel_alber["Nov"] = df_highlevel_alber["Nov"].replace(-9999.9, df_highlevel_alber["Nov"].median())
df_highlevel_alber["Dec"] = df_highlevel_alber["Dec"].replace(-9999.9, df_highlevel_alber["Dec"].median())
df_highlevel_alber["Annual"] = df_highlevel_alber["Annual"].replace(-9999.9, df_highlevel_alber["Annual"].median())
df_highlevel_alber["Winter"] = df_highlevel_alber["Winter"].replace(-9999.9, df_highlevel_alber["Winter"].median())
df_highlevel_alber["Spring"] = df_highlevel_alber["Spring"].replace(-9999.9, df_highlevel_alber["Spring"].median())
df_highlevel_alber["Summer"] = df_highlevel_alber["Summer"].replace(-9999.9, df_highlevel_alber["Summer"].median())
df_highlevel_alber["Autumn"] = df_highlevel_alber["Autumn"].replace(-9999.9, df_highlevel_alber["Autumn"].median())

x1 = df_highlevel_alber["Year"]
y1 = df_highlevel_alber["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_highlevel_alber["Year"]
y2 = df_highlevel_alber["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_highlevel_alber["Year"]
y3 = df_highlevel_alber["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_highlevel_alber["Year"]
y4 = df_highlevel_alber["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')



plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Highlevel Alberta")
plt.legend()
plt.show()


#Jaspar Alberta 

jaspar_alber = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/jaspar_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_jaspar_alber = pd.DataFrame(jaspar_alber)

df_jaspar_alber["Feb"] = df_jaspar_alber["Feb"].replace(-9999.9, df_jaspar_alber["Feb"].median())
df_jaspar_alber["Jul"] = df_jaspar_alber["Jul"].replace(-9999.9, df_jaspar_alber["Jul"].median())
df_jaspar_alber["Aug"] = df_jaspar_alber["Aug"].replace(-9999.9, df_jaspar_alber["Aug"].median())
df_jaspar_alber["Sep"] = df_jaspar_alber["Sep"].replace(-9999.9, df_jaspar_alber["Sep"].median())
df_jaspar_alber["Summer"] = df_jaspar_alber["Summer"].replace(-9999.9, df_jaspar_alber["Summer"].median())

x1 = df_jaspar_alber["Year"]
y1 = df_jaspar_alber["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_jaspar_alber["Year"]
y2 = df_jaspar_alber["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_jaspar_alber["Year"]
y3 = df_jaspar_alber["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_jaspar_alber["Year"]
y4 = df_jaspar_alber["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')



plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Jaspar Alberta")
plt.legend()
plt.show()

#Lethbridge Alberta 

lethbridge_alber = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/lethbridge_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_lethbridge_alber = pd.DataFrame(lethbridge_alber)

x1 = df_lethbridge_alber["Year"]
y1 = df_lethbridge_alber["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_lethbridge_alber["Year"]
y2 = df_lethbridge_alber["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_lethbridge_alber["Year"]
y3 = df_lethbridge_alber["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_lethbridge_alber["Year"]
y4 = df_lethbridge_alber["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')



plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Lethbridge Alberta")
plt.legend()
plt.show()

#Medicinehat Alberta 

medicinehat_alber = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/medicinehat_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_medicinehat_alber = pd.DataFrame(medicinehat_alber)

df_medicinehat_alber.dropna(axis = 1, how='all', inplace = True)
df_medicinehat_alber.dropna(axis = 0, how='all', inplace = True)
df_medicinehat_alber.dropna(axis = 0, how='any', inplace = True)

df_medicinehat_alber["Jan"] = df_medicinehat_alber["Jan"].replace(-9999.9, df_medicinehat_alber["Jan"].median())
df_medicinehat_alber["Feb"] = df_medicinehat_alber["Feb"].replace(-9999.9, df_medicinehat_alber["Feb"].median())
df_medicinehat_alber["Mar"] = df_medicinehat_alber["Mar"].replace(-9999.9, df_medicinehat_alber["Mar"].median())
df_medicinehat_alber["Apr"] = df_medicinehat_alber["Apr"].replace(-9999.9, df_medicinehat_alber["Apr"].median())
df_medicinehat_alber["May"] = df_medicinehat_alber["May"].replace(-9999.9, df_medicinehat_alber["May"].median())
df_medicinehat_alber["Jun"] = df_medicinehat_alber["Jun"].replace(-9999.9, df_medicinehat_alber["Jun"].median())
df_medicinehat_alber["Jul"] = df_medicinehat_alber["Jul"].replace(-9999.9, df_medicinehat_alber["Jul"].median())
df_medicinehat_alber["Aug"] = df_medicinehat_alber["Aug"].replace(-9999.9, df_medicinehat_alber["Aug"].median())
df_medicinehat_alber["Sep"] = df_medicinehat_alber["Sep"].replace(-9999.9, df_medicinehat_alber["Sep"].median())
df_medicinehat_alber["Oct"] = df_medicinehat_alber["Oct"].replace(-9999.9, df_medicinehat_alber["Oct"].median())
df_medicinehat_alber["Nov"] = df_medicinehat_alber["Nov"].replace(-9999.9, df_medicinehat_alber["Nov"].median())
df_medicinehat_alber["Dec"] = df_medicinehat_alber["Dec"].replace(-9999.9, df_medicinehat_alber["Dec"].median())
df_medicinehat_alber["Annual"] = df_medicinehat_alber["Annual"].replace(-9999.9, df_medicinehat_alber["Annual"].median())
df_medicinehat_alber["Winter"] = df_medicinehat_alber["Winter"].replace(-9999.9, df_medicinehat_alber["Winter"].median())
df_medicinehat_alber["Spring"] = df_medicinehat_alber["Spring"].replace(-9999.9, df_medicinehat_alber["Spring"].median())
df_medicinehat_alber["Summer"] = df_medicinehat_alber["Summer"].replace(-9999.9, df_medicinehat_alber["Summer"].median())
df_medicinehat_alber["Autumn"] = df_medicinehat_alber["Autumn"].replace(-9999.9, df_medicinehat_alber["Autumn"].median())

x1 = df_medicinehat_alber["Year"]
y1 = df_medicinehat_alber["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_medicinehat_alber["Year"]
y2 = df_medicinehat_alber["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_medicinehat_alber["Year"]
y3 = df_medicinehat_alber["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_medicinehat_alber["Year"]
y4 = df_medicinehat_alber["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')



plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Medicinehat Alberta")
plt.legend()
plt.show()

#Peace River Alberta 
peaceriver_alber = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/peaceriver_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_peaceriver_alber = pd.DataFrame(peaceriver_alber)

df_peaceriver_alber["Jan"] = df_peaceriver_alber["Jan"].replace(-9999.9, df_peaceriver_alber["Jan"].median())
df_peaceriver_alber["Feb"] = df_peaceriver_alber["Feb"].replace(-9999.9, df_peaceriver_alber["Feb"].median())
df_peaceriver_alber["Mar"] = df_peaceriver_alber["Mar"].replace(-9999.9, df_peaceriver_alber["Mar"].median())
df_peaceriver_alber["Apr"] = df_peaceriver_alber["Apr"].replace(-9999.9, df_peaceriver_alber["Apr"].median())
df_peaceriver_alber["May"] = df_peaceriver_alber["May"].replace(-9999.9, df_peaceriver_alber["May"].median())
df_peaceriver_alber["Jun"] = df_peaceriver_alber["Jun"].replace(-9999.9, df_peaceriver_alber["Jun"].median())
df_peaceriver_alber["Jul"] = df_peaceriver_alber["Jul"].replace(-9999.9, df_peaceriver_alber["Jul"].median())
df_peaceriver_alber["Aug"] = df_peaceriver_alber["Aug"].replace(-9999.9, df_peaceriver_alber["Aug"].median())
df_peaceriver_alber["Sep"] = df_peaceriver_alber["Sep"].replace(-9999.9, df_peaceriver_alber["Sep"].median())
df_peaceriver_alber["Oct"] = df_peaceriver_alber["Oct"].replace(-9999.9, df_peaceriver_alber["Oct"].median())
df_peaceriver_alber["Nov"] = df_peaceriver_alber["Nov"].replace(-9999.9, df_peaceriver_alber["Nov"].median())
df_peaceriver_alber["Dec"] = df_peaceriver_alber["Dec"].replace(-9999.9, df_peaceriver_alber["Dec"].median())
df_peaceriver_alber["Annual"] = df_peaceriver_alber["Annual"].replace(-9999.9, df_peaceriver_alber["Annual"].median())
df_peaceriver_alber["Winter"] = df_peaceriver_alber["Winter"].replace(-9999.9, df_peaceriver_alber["Winter"].median())
df_peaceriver_alber["Spring"] = df_peaceriver_alber["Spring"].replace(-9999.9, df_peaceriver_alber["Spring"].median())
df_peaceriver_alber["Summer"] = df_peaceriver_alber["Summer"].replace(-9999.9, df_peaceriver_alber["Summer"].median())
df_peaceriver_alber["Autumn"] = df_peaceriver_alber["Autumn"].replace(-9999.9, df_peaceriver_alber["Autumn"].median())

x1 = df_peaceriver_alber["Year"]
y1 = df_peaceriver_alber["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_peaceriver_alber["Year"]
y2 = df_peaceriver_alber["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_peaceriver_alber["Year"]
y3 = df_peaceriver_alber["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_peaceriver_alber["Year"]
y4 = df_peaceriver_alber["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')



plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Peaceriver Alberta")
plt.legend()
plt.show()

#Reddeer Alberta 

reddeer_alber = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/reddeer_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_reddeer_alber = pd.DataFrame(reddeer_alber)

df_reddeer_alber["May"] = df_reddeer_alber["May"].replace(-9999.9, df_reddeer_alber["May"].median())
df_reddeer_alber["Jun"] = df_reddeer_alber["Jun"].replace(-9999.9, df_reddeer_alber["Jun"].median())
df_reddeer_alber["Jul"] = df_reddeer_alber["Jul"].replace(-9999.9, df_reddeer_alber["Jul"].median())
df_reddeer_alber["Aug"] = df_reddeer_alber["Aug"].replace(-9999.9, df_reddeer_alber["Aug"].median())
df_reddeer_alber["Sep"] = df_reddeer_alber["Sep"].replace(-9999.9, df_reddeer_alber["Sep"].median())
df_reddeer_alber["Oct"] = df_reddeer_alber["Oct"].replace(-9999.9, df_reddeer_alber["Oct"].median())
df_reddeer_alber["Nov"] = df_reddeer_alber["Nov"].replace(-9999.9, df_reddeer_alber["Nov"].median())
df_reddeer_alber["Dec"] = df_reddeer_alber["Dec"].replace(-9999.9, df_reddeer_alber["Dec"].median())
df_reddeer_alber["Summer"] = df_reddeer_alber["Summer"].replace(-9999.9, df_reddeer_alber["Summer"].median())
df_reddeer_alber["Autumn"] = df_reddeer_alber["Autumn"].replace(-9999.9, df_reddeer_alber["Autumn"].median())
df_reddeer_alber["Annual"] = df_reddeer_alber["Annual"].replace(-9999.9, df_reddeer_alber["Annual"].median())

x1 = df_reddeer_alber["Year"]
y1 = df_reddeer_alber["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_reddeer_alber["Year"]
y2 = df_reddeer_alber["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_reddeer_alber["Year"]
y3 = df_reddeer_alber["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_reddeer_alber["Year"]
y4 = df_reddeer_alber["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')



plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Red Deer Alberta")
plt.legend()
plt.show()

