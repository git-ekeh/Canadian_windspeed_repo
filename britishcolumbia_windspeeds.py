#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd 
from matplotlib import pyplot as plt

#Blueriver British Columbia 
blueriver_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/blueriver_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_blueriver_bc = pd.DataFrame(blueriver_bc)

df_blueriver_bc["Jan"] = df_blueriver_bc["Jan"].replace(-9999.9, df_blueriver_bc["Jan"].median())
df_blueriver_bc["Feb"] = df_blueriver_bc["Feb"].replace(-9999.9, df_blueriver_bc["Feb"].median())
df_blueriver_bc["Mar"] = df_blueriver_bc["Mar"].replace(-9999.9, df_blueriver_bc["Mar"].median())
df_blueriver_bc["Apr"] = df_blueriver_bc["Apr"].replace(-9999.9, df_blueriver_bc["Apr"].median())
df_blueriver_bc["May"] = df_blueriver_bc["May"].replace(-9999.9, df_blueriver_bc["May"].median())
df_blueriver_bc["Jun"] = df_blueriver_bc["Jun"].replace(-9999.9, df_blueriver_bc["Jun"].median())
df_blueriver_bc["Jul"] = df_blueriver_bc["Jul"].replace(-9999.9, df_blueriver_bc["Jul"].median())
df_blueriver_bc["Aug"] = df_blueriver_bc["Aug"].replace(-9999.9, df_blueriver_bc["Aug"].median())
df_blueriver_bc["Sep"] = df_blueriver_bc["Sep"].replace(-9999.9, df_blueriver_bc["Sep"].median())
df_blueriver_bc["Oct"] = df_blueriver_bc["Oct"].replace(-9999.9, df_blueriver_bc["Oct"].median())
df_blueriver_bc["Nov"] = df_blueriver_bc["Nov"].replace(-9999.9, df_blueriver_bc["Nov"].median())
df_blueriver_bc["Dec"] = df_blueriver_bc["Dec"].replace(-9999.9, df_blueriver_bc["Dec"].median())
df_blueriver_bc["Annual"] = df_blueriver_bc["Annual"].replace(-9999.9, df_blueriver_bc["Annual"].median())
df_blueriver_bc["Winter"] = df_blueriver_bc["Winter"].replace(-9999.9, df_blueriver_bc["Winter"].median())
df_blueriver_bc["Spring"] = df_blueriver_bc["Spring"].replace(-9999.9, df_blueriver_bc["Spring"].median())
df_blueriver_bc["Summer"] = df_blueriver_bc["Summer"].replace(-9999.9, df_blueriver_bc["Summer"].median())
df_blueriver_bc["Autumn"] = df_blueriver_bc["Autumn"].replace(-9999.9, df_blueriver_bc["Autumn"].median())

x1 = df_blueriver_bc["Year"]
y1 = df_blueriver_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_blueriver_bc["Year"]
y2 = df_blueriver_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_blueriver_bc["Year"]
y3 = df_blueriver_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_blueriver_bc["Year"]
y4 = df_blueriver_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Blueriver British Columbia")
plt.legend()
plt.show()


#Castlegar British Columbia 
    
castlegar_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/castlegar_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_castlegar_bc = pd.DataFrame(castlegar_bc)

df_castlegar_bc["Jan"] = df_castlegar_bc["Jan"].replace(-9999.9, df_castlegar_bc["Jan"].median())
df_castlegar_bc["Feb"] = df_castlegar_bc["Feb"].replace(-9999.9, df_castlegar_bc["Feb"].median())
df_castlegar_bc["Mar"] = df_castlegar_bc["Mar"].replace(-9999.9, df_castlegar_bc["Mar"].median())
df_castlegar_bc["Apr"] = df_castlegar_bc["Apr"].replace(-9999.9, df_castlegar_bc["Apr"].median())
df_castlegar_bc["May"] = df_castlegar_bc["May"].replace(-9999.9, df_castlegar_bc["May"].median())
df_castlegar_bc["Jun"] = df_castlegar_bc["Jun"].replace(-9999.9, df_castlegar_bc["Jun"].median())
df_castlegar_bc["Jul"] = df_castlegar_bc["Jul"].replace(-9999.9, df_castlegar_bc["Jul"].median())
df_castlegar_bc["Aug"] = df_castlegar_bc["Aug"].replace(-9999.9, df_castlegar_bc["Aug"].median())
df_castlegar_bc["Sep"] = df_castlegar_bc["Sep"].replace(-9999.9, df_castlegar_bc["Sep"].median())
df_castlegar_bc["Oct"] = df_castlegar_bc["Oct"].replace(-9999.9, df_castlegar_bc["Oct"].median())
df_castlegar_bc["Nov"] = df_castlegar_bc["Nov"].replace(-9999.9, df_castlegar_bc["Nov"].median())
df_castlegar_bc["Dec"] = df_castlegar_bc["Dec"].replace(-9999.9, df_castlegar_bc["Dec"].median())
df_castlegar_bc["Annual"] = df_castlegar_bc["Annual"].replace(-9999.9, df_castlegar_bc["Annual"].median())
df_castlegar_bc["Winter"] = df_castlegar_bc["Winter"].replace(-9999.9, df_castlegar_bc["Winter"].median())
df_castlegar_bc["Spring"] = df_castlegar_bc["Spring"].replace(-9999.9, df_castlegar_bc["Spring"].median())
df_castlegar_bc["Summer"] = df_castlegar_bc["Summer"].replace(-9999.9, df_castlegar_bc["Summer"].median())
df_castlegar_bc["Autumn"] = df_castlegar_bc["Autumn"].replace(-9999.9, df_castlegar_bc["Autumn"].median())

x1 = df_castlegar_bc["Year"]
y1 = df_castlegar_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_castlegar_bc["Year"]
y2 = df_castlegar_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_castlegar_bc["Year"]
y3 = df_castlegar_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_castlegar_bc["Year"]
y4 = df_castlegar_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Castlegar British Columbia")
plt.legend()
plt.show()

#Comox British Columbia

comox_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/comox_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding= 'utf-8-sig')
df_comox_bc = pd.DataFrame(comox_bc)

x1 = df_comox_bc["Year"]
y1 = df_comox_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_comox_bc["Year"]
y2 = df_comox_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_comox_bc["Year"]
y3 = df_comox_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_comox_bc["Year"]
y4 = df_comox_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Comox British Columbia")
plt.legend()
plt.show()

#Cranbrook British Columbia 
        
cranbrook_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/cranbrook_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding= 'utf-8-sig')
df_cranbrook_bc = pd.DataFrame(cranbrook_bc)

df_cranbrook_bc["Jan"] = df_cranbrook_bc["Jan"].replace(-9999.9, df_cranbrook_bc["Jan"].median())
df_cranbrook_bc["Feb"] = df_cranbrook_bc["Feb"].replace(-9999.9, df_cranbrook_bc["Feb"].median())
df_cranbrook_bc["Mar"] = df_cranbrook_bc["Mar"].replace(-9999.9, df_cranbrook_bc["Mar"].median())
df_cranbrook_bc["Apr"] = df_cranbrook_bc["Apr"].replace(-9999.9, df_cranbrook_bc["Apr"].median())
df_cranbrook_bc["May"] = df_cranbrook_bc["May"].replace(-9999.9, df_cranbrook_bc["May"].median())
df_cranbrook_bc["Jun"] = df_cranbrook_bc["Jun"].replace(-9999.9, df_cranbrook_bc["Jun"].median())
df_cranbrook_bc["Jul"] = df_cranbrook_bc["Jul"].replace(-9999.9, df_cranbrook_bc["Jul"].median())
df_cranbrook_bc["Aug"] = df_cranbrook_bc["Aug"].replace(-9999.9, df_cranbrook_bc["Aug"].median())
df_cranbrook_bc["Sep"] = df_cranbrook_bc["Sep"].replace(-9999.9, df_cranbrook_bc["Sep"].median())
df_cranbrook_bc["Oct"] = df_cranbrook_bc["Oct"].replace(-9999.9, df_cranbrook_bc["Oct"].median())
df_cranbrook_bc["Nov"] = df_cranbrook_bc["Nov"].replace(-9999.9, df_cranbrook_bc["Nov"].median())
df_cranbrook_bc["Dec"] = df_cranbrook_bc["Dec"].replace(-9999.9, df_cranbrook_bc["Dec"].median())
df_cranbrook_bc["Annual"] = df_cranbrook_bc["Annual"].replace(-9999.9, df_cranbrook_bc["Annual"].median())
df_cranbrook_bc["Winter"] = df_cranbrook_bc["Winter"].replace(-9999.9, df_cranbrook_bc["Winter"].median())
df_cranbrook_bc["Spring"] = df_cranbrook_bc["Spring"].replace(-9999.9, df_cranbrook_bc["Spring"].median())
df_cranbrook_bc["Summer"] = df_cranbrook_bc["Summer"].replace(-9999.9, df_cranbrook_bc["Summer"].median())
df_cranbrook_bc["Autumn"] = df_cranbrook_bc["Autumn"].replace(-9999.9, df_cranbrook_bc["Autumn"].median())
 
x1 = df_cranbrook_bc["Year"]
y1 = df_cranbrook_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_cranbrook_bc["Year"]
y2 = df_cranbrook_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_cranbrook_bc["Year"]
y3 = df_cranbrook_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_cranbrook_bc["Year"]
y4 = df_cranbrook_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Cranbrook British Columbia")
plt.legend()
plt.show()

#Dawsoncreek British Columbia 

dawsoncreek_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/dawsoncreek_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_dawsoncreek_bc = pd.DataFrame(dawsoncreek_bc)


df_dawsoncreek_bc["Jan"] = df_dawsoncreek_bc["Jan"].replace(-9999.9, df_dawsoncreek_bc["Jan"].median())
df_dawsoncreek_bc["Feb"] = df_dawsoncreek_bc["Feb"].replace(-9999.9, df_dawsoncreek_bc["Feb"].median())
df_dawsoncreek_bc["Mar"] = df_dawsoncreek_bc["Mar"].replace(-9999.9, df_dawsoncreek_bc["Mar"].median())
df_dawsoncreek_bc["Apr"] = df_dawsoncreek_bc["Apr"].replace(-9999.9, df_dawsoncreek_bc["Apr"].median())
df_dawsoncreek_bc["May"] = df_dawsoncreek_bc["May"].replace(-9999.9, df_dawsoncreek_bc["May"].median())
df_dawsoncreek_bc["Jun"] = df_dawsoncreek_bc["Jun"].replace(-9999.9, df_dawsoncreek_bc["Jun"].median())
df_dawsoncreek_bc["Jul"] = df_dawsoncreek_bc["Jul"].replace(-9999.9, df_dawsoncreek_bc["Jul"].median())
df_dawsoncreek_bc["Aug"] = df_dawsoncreek_bc["Aug"].replace(-9999.9, df_dawsoncreek_bc["Aug"].median())
df_dawsoncreek_bc["Sep"] = df_dawsoncreek_bc["Sep"].replace(-9999.9, df_dawsoncreek_bc["Sep"].median())
df_dawsoncreek_bc["Oct"] = df_dawsoncreek_bc["Oct"].replace(-9999.9, df_dawsoncreek_bc["Oct"].median())
df_dawsoncreek_bc["Nov"] = df_dawsoncreek_bc["Nov"].replace(-9999.9, df_dawsoncreek_bc["Nov"].median())
df_dawsoncreek_bc["Dec"] = df_dawsoncreek_bc["Dec"].replace(-9999.9, df_dawsoncreek_bc["Dec"].median())
df_dawsoncreek_bc["Annual"] = df_dawsoncreek_bc["Annual"].replace(-9999.9, df_dawsoncreek_bc["Annual"].median())
df_dawsoncreek_bc["Winter"] = df_dawsoncreek_bc["Winter"].replace(-9999.9, df_dawsoncreek_bc["Winter"].median())
df_dawsoncreek_bc["Spring"] = df_dawsoncreek_bc["Spring"].replace(-9999.9, df_dawsoncreek_bc["Spring"].median())
df_dawsoncreek_bc["Summer"] = df_dawsoncreek_bc["Summer"].replace(-9999.9, df_dawsoncreek_bc["Summer"].median())
df_dawsoncreek_bc["Autumn"] = df_dawsoncreek_bc["Autumn"].replace(-9999.9, df_dawsoncreek_bc["Autumn"].median())

x1 = df_dawsoncreek_bc["Year"]
y1 = df_dawsoncreek_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_dawsoncreek_bc["Year"]
y2 = df_dawsoncreek_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_dawsoncreek_bc["Year"]
y3 = df_dawsoncreek_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_dawsoncreek_bc["Year"]
y4 = df_dawsoncreek_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Dawsoncreek British Columbia")
plt.legend()
plt.show()

#Deaselake British Columbia 
    
deaselake_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/deaselake_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_deaselake_bc = pd.DataFrame(deaselake_bc)

df_deaselake_bc["Jan"] = df_deaselake_bc["Jan"].replace(-9999.9, df_deaselake_bc["Jan"].median())
df_deaselake_bc["Feb"] = df_deaselake_bc["Feb"].replace(-9999.9, df_deaselake_bc["Feb"].median())
df_deaselake_bc["Mar"] = df_deaselake_bc["Mar"].replace(-9999.9, df_deaselake_bc["Mar"].median())
df_deaselake_bc["Apr"] = df_deaselake_bc["Apr"].replace(-9999.9, df_deaselake_bc["Apr"].median())
df_deaselake_bc["May"] = df_deaselake_bc["May"].replace(-9999.9, df_deaselake_bc["May"].median())
df_deaselake_bc["Jun"] = df_deaselake_bc["Jun"].replace(-9999.9, df_deaselake_bc["Jun"].median())
df_deaselake_bc["Jul"] = df_deaselake_bc["Jul"].replace(-9999.9, df_deaselake_bc["Jul"].median())
df_deaselake_bc["Aug"] = df_deaselake_bc["Aug"].replace(-9999.9, df_deaselake_bc["Aug"].median())
df_deaselake_bc["Sep"] = df_deaselake_bc["Sep"].replace(-9999.9, df_deaselake_bc["Sep"].median())
df_deaselake_bc["Oct"] = df_deaselake_bc["Oct"].replace(-9999.9, df_deaselake_bc["Oct"].median())
df_deaselake_bc["Nov"] = df_deaselake_bc["Nov"].replace(-9999.9, df_deaselake_bc["Nov"].median())
df_deaselake_bc["Dec"] = df_deaselake_bc["Dec"].replace(-9999.9, df_deaselake_bc["Dec"].median())
df_deaselake_bc["Annual"] = df_deaselake_bc["Annual"].replace(-9999.9, df_deaselake_bc["Annual"].median())
df_deaselake_bc["Winter"] = df_deaselake_bc["Winter"].replace(-9999.9, df_deaselake_bc["Winter"].median())
df_deaselake_bc["Spring"] = df_deaselake_bc["Spring"].replace(-9999.9, df_deaselake_bc["Spring"].median())
df_deaselake_bc["Summer"] = df_deaselake_bc["Summer"].replace(-9999.9, df_deaselake_bc["Summer"].median())
df_deaselake_bc["Autumn"] = df_deaselake_bc["Autumn"].replace(-9999.9, df_deaselake_bc["Autumn"].median())

x1 = df_deaselake_bc["Year"]
y1 = df_deaselake_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_deaselake_bc["Year"]
y2 = df_deaselake_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_deaselake_bc["Year"]
y3 = df_deaselake_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_deaselake_bc["Year"]
y4 = df_deaselake_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Deaselake British Columbia")
plt.legend()
plt.show()

#Fort Nelson British Columbia 

fortnelson_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/fortnelson_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_fortnelson_bc = pd.DataFrame(fortnelson_bc)

x1 = df_fortnelson_bc["Year"]
y1 = df_fortnelson_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_fortnelson_bc["Year"]
y2 = df_fortnelson_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_fortnelson_bc["Year"]
y3 = df_fortnelson_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_fortnelson_bc["Year"]
y4 = df_fortnelson_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Fort Nelson British Columbia")
plt.legend()
plt.show()

#Fort st. John British Columbia 

fortstjohn_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/fortstjohn_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_fortstjohn_bc = pd.DataFrame(fortstjohn_bc)

x1 = df_fortstjohn_bc["Year"]
y1 = df_fortstjohn_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_fortstjohn_bc["Year"]
y2 = df_fortstjohn_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_fortstjohn_bc["Year"]
y3 = df_fortstjohn_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_fortstjohn_bc["Year"]
y4 = df_fortstjohn_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Fort st.John British Columbia")
plt.legend()
plt.show()


#Hopea British Columbia 

hopea_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/hopea_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_hopea_bc = pd.DataFrame(hopea_bc)


x1 = df_hopea_bc["Year"]
y1 = df_hopea_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_hopea_bc["Year"]
y2 = df_hopea_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_hopea_bc["Year"]
y3 = df_hopea_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_hopea_bc["Year"]
y4 = df_hopea_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Hopea British Columbia")
plt.legend()
plt.show()

#Kamloops British Columbia 

kamloops_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/kamloops_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_kamloops_bc = pd.DataFrame(kamloops_bc)


x1 = df_kamloops_bc["Year"]
y1 = df_kamloops_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_kamloops_bc["Year"]
y2 = df_kamloops_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_kamloops_bc["Year"]
y3 = df_kamloops_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_kamloops_bc["Year"]
y4 = df_kamloops_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Kamloops British Columbia")
plt.legend()
plt.show()

#Kelowna British Columbia 

kelowna_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/kelowna_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_kelowna_bc = pd.DataFrame(kelowna_bc)

df_kelowna_bc["Jan"] = df_kelowna_bc["Jan"].replace(-9999.9, df_kelowna_bc["Jan"].median())
df_kelowna_bc["Feb"] = df_kelowna_bc["Feb"].replace(-9999.9, df_kelowna_bc["Feb"].median())
df_kelowna_bc["Mar"] = df_kelowna_bc["Mar"].replace(-9999.9, df_kelowna_bc["Mar"].median())
df_kelowna_bc["Apr"] = df_kelowna_bc["Apr"].replace(-9999.9, df_kelowna_bc["Apr"].median())
df_kelowna_bc["May"] = df_kelowna_bc["May"].replace(-9999.9, df_kelowna_bc["May"].median())
df_kelowna_bc["Jun"] = df_kelowna_bc["Jun"].replace(-9999.9, df_kelowna_bc["Jun"].median())
df_kelowna_bc["Jul"] = df_kelowna_bc["Jul"].replace(-9999.9, df_kelowna_bc["Jul"].median())
df_kelowna_bc["Aug"] = df_kelowna_bc["Aug"].replace(-9999.9, df_kelowna_bc["Aug"].median())
df_kelowna_bc["Sep"] = df_kelowna_bc["Sep"].replace(-9999.9, df_kelowna_bc["Sep"].median())
df_kelowna_bc["Oct"] = df_kelowna_bc["Oct"].replace(-9999.9, df_kelowna_bc["Oct"].median())
df_kelowna_bc["Nov"] = df_kelowna_bc["Nov"].replace(-9999.9, df_kelowna_bc["Nov"].median())
df_kelowna_bc["Dec"] = df_kelowna_bc["Dec"].replace(-9999.9, df_kelowna_bc["Dec"].median())
df_kelowna_bc["Annual"] = df_kelowna_bc["Annual"].replace(-9999.9, df_kelowna_bc["Annual"].median())
df_kelowna_bc["Winter"] = df_kelowna_bc["Winter"].replace(-9999.9, df_kelowna_bc["Winter"].median())
df_kelowna_bc["Spring"] = df_kelowna_bc["Spring"].replace(-9999.9, df_kelowna_bc["Spring"].median())
df_kelowna_bc["Summer"] = df_kelowna_bc["Summer"].replace(-9999.9, df_kelowna_bc["Summer"].median())
df_kelowna_bc["Autumn"] = df_kelowna_bc["Autumn"].replace(-9999.9, df_kelowna_bc["Autumn"].median())

x1 = df_kelowna_bc["Year"]
y1 = df_kelowna_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_kelowna_bc["Year"]
y2 = df_kelowna_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_kelowna_bc["Year"]
y3 = df_kelowna_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_kelowna_bc["Year"]
y4 = df_kelowna_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Kelowna British Columbia")
plt.legend()
plt.show()

#Langara British Columbia 

langara_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/langara_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_langara_bc = pd.DataFrame(langara_bc)

df_langara_bc["Jan"] = df_langara_bc["Jan"].replace(-9999.9, df_langara_bc["Jan"].median())
df_langara_bc["Feb"] = df_langara_bc["Feb"].replace(-9999.9, df_langara_bc["Feb"].median())
df_langara_bc["Mar"] = df_langara_bc["Mar"].replace(-9999.9, df_langara_bc["Mar"].median())
df_langara_bc["Apr"] = df_langara_bc["Apr"].replace(-9999.9, df_langara_bc["Apr"].median())
df_langara_bc["May"] = df_langara_bc["May"].replace(-9999.9, df_langara_bc["May"].median())
df_langara_bc["Jun"] = df_langara_bc["Jun"].replace(-9999.9, df_langara_bc["Jun"].median())
df_langara_bc["Jul"] = df_langara_bc["Jul"].replace(-9999.9, df_langara_bc["Jul"].median())
df_langara_bc["Aug"] = df_langara_bc["Aug"].replace(-9999.9, df_langara_bc["Aug"].median())
df_langara_bc["Sep"] = df_langara_bc["Sep"].replace(-9999.9, df_langara_bc["Sep"].median())
df_langara_bc["Oct"] = df_langara_bc["Oct"].replace(-9999.9, df_langara_bc["Oct"].median())
df_langara_bc["Nov"] = df_langara_bc["Nov"].replace(-9999.9, df_langara_bc["Nov"].median())
df_langara_bc["Dec"] = df_langara_bc["Dec"].replace(-9999.9, df_langara_bc["Dec"].median())
df_langara_bc["Annual"] = df_langara_bc["Annual"].replace(-9999.9, df_langara_bc["Annual"].median())
df_langara_bc["Winter"] = df_langara_bc["Winter"].replace(-9999.9, df_langara_bc["Winter"].median())
df_langara_bc["Spring"] = df_langara_bc["Spring"].replace(-9999.9, df_langara_bc["Spring"].median())
df_langara_bc["Summer"] = df_langara_bc["Summer"].replace(-9999.9, df_langara_bc["Summer"].median())
df_langara_bc["Autumn"] = df_langara_bc["Autumn"].replace(-9999.9, df_langara_bc["Autumn"].median())

x1 = df_langara_bc["Year"]
y1 = df_langara_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_langara_bc["Year"]
y2 = df_langara_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_langara_bc["Year"]
y3 = df_langara_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_langara_bc["Year"]
y4 = df_langara_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Langara British Columbia")
plt.legend()
plt.show()

#McInessisland British Columbia 

mcinessisland_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/mcinessisland_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_mcinessisland_bc = pd.DataFrame(mcinessisland_bc)

df_mcinessisland_bc["Jan"] = df_mcinessisland_bc["Jan"].replace(-9999.9, df_mcinessisland_bc["Jan"].median())
df_mcinessisland_bc["Feb"] = df_mcinessisland_bc["Feb"].replace(-9999.9, df_mcinessisland_bc["Feb"].median())
df_mcinessisland_bc["Mar"] = df_mcinessisland_bc["Mar"].replace(-9999.9, df_mcinessisland_bc["Mar"].median())
df_mcinessisland_bc["Apr"] = df_mcinessisland_bc["Apr"].replace(-9999.9, df_mcinessisland_bc["Apr"].median())
df_mcinessisland_bc["May"] = df_mcinessisland_bc["May"].replace(-9999.9, df_mcinessisland_bc["May"].median())
df_mcinessisland_bc["Jun"] = df_mcinessisland_bc["Jun"].replace(-9999.9, df_mcinessisland_bc["Jun"].median())
df_mcinessisland_bc["Jul"] = df_mcinessisland_bc["Jul"].replace(-9999.9, df_mcinessisland_bc["Jul"].median())
df_mcinessisland_bc["Aug"] = df_mcinessisland_bc["Aug"].replace(-9999.9, df_mcinessisland_bc["Aug"].median())
df_mcinessisland_bc["Sep"] = df_mcinessisland_bc["Sep"].replace(-9999.9, df_mcinessisland_bc["Sep"].median())
df_mcinessisland_bc["Oct"] = df_mcinessisland_bc["Oct"].replace(-9999.9, df_mcinessisland_bc["Oct"].median())
df_mcinessisland_bc["Nov"] = df_mcinessisland_bc["Nov"].replace(-9999.9, df_mcinessisland_bc["Nov"].median())
df_mcinessisland_bc["Dec"] = df_mcinessisland_bc["Dec"].replace(-9999.9, df_mcinessisland_bc["Dec"].median())
df_mcinessisland_bc["Annual"] = df_mcinessisland_bc["Annual"].replace(-9999.9, df_mcinessisland_bc["Annual"].median())
df_mcinessisland_bc["Winter"] = df_mcinessisland_bc["Winter"].replace(-9999.9, df_mcinessisland_bc["Winter"].median())
df_mcinessisland_bc["Spring"] = df_mcinessisland_bc["Spring"].replace(-9999.9, df_mcinessisland_bc["Spring"].median())
df_mcinessisland_bc["Summer"] = df_mcinessisland_bc["Summer"].replace(-9999.9, df_mcinessisland_bc["Summer"].median())
df_mcinessisland_bc["Autumn"] = df_mcinessisland_bc["Autumn"].replace(-9999.9, df_mcinessisland_bc["Autumn"].median())

x1 = df_mcinessisland_bc["Year"]
y1 = df_mcinessisland_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_mcinessisland_bc["Year"]
y2 = df_mcinessisland_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_mcinessisland_bc["Year"]
y3 = df_mcinessisland_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_mcinessisland_bc["Year"]
y4 = df_mcinessisland_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("McIness Island British Columbia")
plt.legend()
plt.show()

#Nanaimo British Columbia 

nanaimo_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/nanaimo_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_nanaimo_bc = pd.DataFrame(nanaimo_bc)

df_nanaimo_bc["Jan"] = df_nanaimo_bc["Jan"].replace(-9999.9, df_nanaimo_bc["Jan"].median())
df_nanaimo_bc["Feb"] = df_nanaimo_bc["Feb"].replace(-9999.9, df_nanaimo_bc["Feb"].median())
df_nanaimo_bc["Mar"] = df_nanaimo_bc["Mar"].replace(-9999.9, df_nanaimo_bc["Mar"].median())
df_nanaimo_bc["Apr"] = df_nanaimo_bc["Apr"].replace(-9999.9, df_nanaimo_bc["Apr"].median())
df_nanaimo_bc["May"] = df_nanaimo_bc["May"].replace(-9999.9, df_nanaimo_bc["May"].median())
df_nanaimo_bc["Jun"] = df_nanaimo_bc["Jun"].replace(-9999.9, df_nanaimo_bc["Jun"].median())
df_nanaimo_bc["Jul"] = df_nanaimo_bc["Jul"].replace(-9999.9, df_nanaimo_bc["Jul"].median())
df_nanaimo_bc["Aug"] = df_nanaimo_bc["Aug"].replace(-9999.9, df_nanaimo_bc["Aug"].median())
df_nanaimo_bc["Sep"] = df_nanaimo_bc["Sep"].replace(-9999.9, df_nanaimo_bc["Sep"].median())
df_nanaimo_bc["Oct"] = df_nanaimo_bc["Oct"].replace(-9999.9, df_nanaimo_bc["Oct"].median())
df_nanaimo_bc["Nov"] = df_nanaimo_bc["Nov"].replace(-9999.9, df_nanaimo_bc["Nov"].median())
df_nanaimo_bc["Dec"] = df_nanaimo_bc["Dec"].replace(-9999.9, df_nanaimo_bc["Dec"].median())
df_nanaimo_bc["Annual"] = df_nanaimo_bc["Annual"].replace(-9999.9, df_nanaimo_bc["Annual"].median())
df_nanaimo_bc["Winter"] = df_nanaimo_bc["Winter"].replace(-9999.9, df_nanaimo_bc["Winter"].median())
df_nanaimo_bc["Spring"] = df_nanaimo_bc["Spring"].replace(-9999.9, df_nanaimo_bc["Spring"].median())
df_nanaimo_bc["Summer"] = df_nanaimo_bc["Summer"].replace(-9999.9, df_nanaimo_bc["Summer"].median())
df_nanaimo_bc["Autumn"] = df_nanaimo_bc["Autumn"].replace(-9999.9, df_nanaimo_bc["Autumn"].median())

x1 = df_nanaimo_bc["Year"]
y1 = df_nanaimo_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_nanaimo_bc["Year"]
y2 = df_nanaimo_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_nanaimo_bc["Year"]
y3 = df_nanaimo_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_nanaimo_bc["Year"]
y4 = df_nanaimo_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Nanaimo British Columbia")
plt.legend()
plt.show()

#Penticton British Columbia 

penticton_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/penticton_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_penticton_bc = pd.DataFrame(penticton_bc)

x1 = df_penticton_bc["Year"]
y1 = df_penticton_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_penticton_bc["Year"]
y2 = df_penticton_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_penticton_bc["Year"]
y3 = df_penticton_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_penticton_bc["Year"]
y4 = df_penticton_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Penticton British Columbia")
plt.legend()
plt.show()

#Port Hardy

porthardy_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/porthardy_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_porthardy_bc = pd.DataFrame(porthardy_bc)


df_porthardy_bc.dropna(axis = 1, how='all', inplace = True)
df_porthardy_bc.dropna(axis = 0, how='all', inplace = True)

df_porthardy_bc["Jan"] = df_porthardy_bc["Jan"].replace(-9999.9, df_porthardy_bc["Jan"].median())
df_porthardy_bc["Feb"] = df_porthardy_bc["Feb"].replace(-9999.9, df_porthardy_bc["Feb"].median())
df_porthardy_bc["Mar"] = df_porthardy_bc["Mar"].replace(-9999.9, df_porthardy_bc["Mar"].median())
df_porthardy_bc["Apr"] = df_porthardy_bc["Apr"].replace(-9999.9, df_porthardy_bc["Apr"].median())
df_porthardy_bc["May"] = df_porthardy_bc["May"].replace(-9999.9, df_porthardy_bc["May"].median())
df_porthardy_bc["Jun"] = df_porthardy_bc["Jun"].replace(-9999.9, df_porthardy_bc["Jun"].median())
df_porthardy_bc["Jul"] = df_porthardy_bc["Jul"].replace(-9999.9, df_porthardy_bc["Jul"].median())
df_porthardy_bc["Aug"] = df_porthardy_bc["Aug"].replace(-9999.9, df_porthardy_bc["Aug"].median())
df_porthardy_bc["Sep"] = df_porthardy_bc["Sep"].replace(-9999.9, df_porthardy_bc["Sep"].median())
df_porthardy_bc["Oct"] = df_porthardy_bc["Oct"].replace(-9999.9, df_porthardy_bc["Oct"].median())
df_porthardy_bc["Nov"] = df_porthardy_bc["Nov"].replace(-9999.9, df_porthardy_bc["Nov"].median())
df_porthardy_bc["Dec"] = df_porthardy_bc["Dec"].replace(-9999.9, df_porthardy_bc["Dec"].median())
df_porthardy_bc["Annual"] = df_porthardy_bc["Annual"].replace(-9999.9, df_porthardy_bc["Annual"].median())
df_porthardy_bc["Winter"] = df_porthardy_bc["Winter"].replace(-9999.9, df_porthardy_bc["Winter"].median())
df_porthardy_bc["Spring"] = df_porthardy_bc["Spring"].replace(-9999.9, df_porthardy_bc["Spring"].median())
df_porthardy_bc["Summer"] = df_porthardy_bc["Summer"].replace(-9999.9, df_porthardy_bc["Summer"].median())
df_porthardy_bc["Autumn"] = df_porthardy_bc["Autumn"].replace(-9999.9, df_porthardy_bc["Autumn"].median())

x1 = df_porthardy_bc["Year"]
y1 = df_porthardy_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_porthardy_bc["Year"]
y2 = df_porthardy_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_porthardy_bc["Year"]
y3 = df_porthardy_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_porthardy_bc["Year"]
y4 = df_porthardy_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Port Hardy British Columbia")
plt.legend()
plt.show()

#Prince George British Columbia 

princegeorge_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/princegeorge_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_princegeorge_bc = pd.DataFrame(princegeorge_bc)

df_princegeorge_bc["Feb"] = df_princegeorge_bc["Feb"].replace(-9999.9, df_princegeorge_bc["Feb"].median())

x1 = df_princegeorge_bc["Year"]
y1 = df_princegeorge_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_princegeorge_bc["Year"]
y2 = df_princegeorge_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_princegeorge_bc["Year"]
y3 = df_princegeorge_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_princegeorge_bc["Year"]
y4 = df_princegeorge_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Prince George British Columbia")
plt.legend()
plt.show()

#Prince Rupert British Columbia 

princerupert_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/princerupert_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_princerupert_bc = pd.DataFrame(princerupert_bc)

df_princerupert_bc["Jan"] = df_princerupert_bc["Jan"].replace(-9999.9, df_princerupert_bc["Jan"].median())
df_princerupert_bc["Feb"] = df_princerupert_bc["Feb"].replace(-9999.9, df_princerupert_bc["Feb"].median())
df_princerupert_bc["Mar"] = df_princerupert_bc["Mar"].replace(-9999.9, df_princerupert_bc["Mar"].median())
df_princerupert_bc["Apr"] = df_princerupert_bc["Apr"].replace(-9999.9, df_princerupert_bc["Apr"].median())
df_princerupert_bc["May"] = df_princerupert_bc["May"].replace(-9999.9, df_princerupert_bc["May"].median())
df_princerupert_bc["Jun"] = df_princerupert_bc["Jun"].replace(-9999.9, df_princerupert_bc["Jun"].median())
df_princerupert_bc["Jul"] = df_princerupert_bc["Jul"].replace(-9999.9, df_princerupert_bc["Jul"].median())
df_princerupert_bc["Aug"] = df_princerupert_bc["Aug"].replace(-9999.9, df_princerupert_bc["Aug"].median())
df_princerupert_bc["Sep"] = df_princerupert_bc["Sep"].replace(-9999.9, df_princerupert_bc["Sep"].median())
df_princerupert_bc["Oct"] = df_princerupert_bc["Oct"].replace(-9999.9, df_princerupert_bc["Oct"].median())
df_princerupert_bc["Nov"] = df_princerupert_bc["Nov"].replace(-9999.9, df_princerupert_bc["Nov"].median())
df_princerupert_bc["Dec"] = df_princerupert_bc["Dec"].replace(-9999.9, df_princerupert_bc["Dec"].median())
df_princerupert_bc["Annual"] = df_princerupert_bc["Annual"].replace(-9999.9, df_princerupert_bc["Annual"].median())
df_princerupert_bc["Winter"] = df_princerupert_bc["Winter"].replace(-9999.9, df_princerupert_bc["Winter"].median())
df_princerupert_bc["Spring"] = df_princerupert_bc["Spring"].replace(-9999.9, df_princerupert_bc["Spring"].median())
df_princerupert_bc["Summer"] = df_princerupert_bc["Summer"].replace(-9999.9, df_princerupert_bc["Summer"].median())
df_princerupert_bc["Autumn"] = df_princerupert_bc["Autumn"].replace(-9999.9, df_princerupert_bc["Autumn"].median())

x1 = df_princerupert_bc["Year"]
y1 = df_princerupert_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_princerupert_bc["Year"]
y2 = df_princerupert_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_princerupert_bc["Year"]
y3 = df_princerupert_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_princerupert_bc["Year"]
y4 = df_princerupert_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Prince Rupert British Columbia")
plt.legend()
plt.show()

#Princeton British Columbia 

princeton_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/princeton_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_princeton_bc = pd.DataFrame(princeton_bc)

x1 = df_princeton_bc["Year"]
y1 = df_princeton_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_princeton_bc["Year"]
y2 = df_princeton_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_princeton_bc["Year"]
y3 = df_princeton_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_princeton_bc["Year"]
y4 = df_princeton_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Princeton British Columbia")
plt.legend()
plt.show()

#Quesnel British Columbia 

quesnel_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/quesnel_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_quesnel_bc = pd.DataFrame(quesnel_bc)

df_quesnel_bc["Jan"] = df_quesnel_bc["Jan"].replace(-9999.9, df_quesnel_bc["Jan"].median())
df_quesnel_bc["Feb"] = df_quesnel_bc["Feb"].replace(-9999.9, df_quesnel_bc["Feb"].median())
df_quesnel_bc["Mar"] = df_quesnel_bc["Mar"].replace(-9999.9, df_quesnel_bc["Mar"].median())
df_quesnel_bc["Apr"] = df_quesnel_bc["Apr"].replace(-9999.9, df_quesnel_bc["Apr"].median())
df_quesnel_bc["May"] = df_quesnel_bc["May"].replace(-9999.9, df_quesnel_bc["May"].median())
df_quesnel_bc["Jun"] = df_quesnel_bc["Jun"].replace(-9999.9, df_quesnel_bc["Jun"].median())
df_quesnel_bc["Jul"] = df_quesnel_bc["Jul"].replace(-9999.9, df_quesnel_bc["Jul"].median())
df_quesnel_bc["Aug"] = df_quesnel_bc["Aug"].replace(-9999.9, df_quesnel_bc["Aug"].median())
df_quesnel_bc["Sep"] = df_quesnel_bc["Sep"].replace(-9999.9, df_quesnel_bc["Sep"].median())
df_quesnel_bc["Oct"] = df_quesnel_bc["Oct"].replace(-9999.9, df_quesnel_bc["Oct"].median())
df_quesnel_bc["Nov"] = df_quesnel_bc["Nov"].replace(-9999.9, df_quesnel_bc["Nov"].median())
df_quesnel_bc["Dec"] = df_quesnel_bc["Dec"].replace(-9999.9, df_quesnel_bc["Dec"].median())
df_quesnel_bc["Annual"] = df_quesnel_bc["Annual"].replace(-9999.9, df_quesnel_bc["Annual"].median())
df_quesnel_bc["Winter"] = df_quesnel_bc["Winter"].replace(-9999.9, df_quesnel_bc["Winter"].median())
df_quesnel_bc["Spring"] = df_quesnel_bc["Spring"].replace(-9999.9, df_quesnel_bc["Spring"].median())
df_quesnel_bc["Summer"] = df_quesnel_bc["Summer"].replace(-9999.9, df_quesnel_bc["Summer"].median())
df_quesnel_bc["Autumn"] = df_quesnel_bc["Autumn"].replace(-9999.9, df_quesnel_bc["Autumn"].median())

x1 = df_quesnel_bc["Year"]
y1 = df_quesnel_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_quesnel_bc["Year"]
y2 = df_quesnel_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_quesnel_bc["Year"]
y3 = df_quesnel_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_quesnel_bc["Year"]
y4 = df_quesnel_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Quesnel British Columbia")
plt.legend()
plt.show()

#Sandspit British Columbia 

sandspit_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/sandspit_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_sandspit_bc  = pd.DataFrame(sandspit_bc)

df_sandspit_bc["Jun"] = df_sandspit_bc["Jun"].replace(-9999.9, df_sandspit_bc["Jun"].median())
df_sandspit_bc["Sep"] = df_sandspit_bc["Sep"].replace(-9999.9, df_sandspit_bc["Sep"].median())
df_sandspit_bc["Oct"] = df_sandspit_bc["Oct"].replace(-9999.9, df_sandspit_bc["Oct"].median())
df_sandspit_bc["Autumn"] = df_sandspit_bc["Autumn"].replace(-9999.9, df_sandspit_bc["Autumn"].median())


x1 = df_sandspit_bc["Year"]
y1 = df_sandspit_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_sandspit_bc["Year"]
y2 = df_sandspit_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_sandspit_bc["Year"]
y3 = df_sandspit_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_sandspit_bc["Year"]
y4 = df_sandspit_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Sandspit British Columbia")
plt.legend()
plt.show()

#Smithers British Columbia 

smithers_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/smithers_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_smithers_bc = pd.DataFrame(smithers_bc)

x1 = df_smithers_bc["Year"]
y1 = df_smithers_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_smithers_bc["Year"]
y2 = df_smithers_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_smithers_bc["Year"]
y3 = df_smithers_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_smithers_bc["Year"]
y4 = df_smithers_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Smithers British Columbia")
plt.legend()
plt.show()

#Terrace British Columbia 

terrace_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/terrace_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_terrace_bc = pd.DataFrame(terrace_bc)

df_terrace_bc["Jan"] = df_terrace_bc["Jan"].replace(-9999.9, df_terrace_bc["Jan"].median())
df_terrace_bc["Feb"] = df_terrace_bc["Feb"].replace(-9999.9, df_terrace_bc["Feb"].median())
df_terrace_bc["Mar"] = df_terrace_bc["Mar"].replace(-9999.9, df_terrace_bc["Mar"].median())
df_terrace_bc["Apr"] = df_terrace_bc["Apr"].replace(-9999.9, df_terrace_bc["Apr"].median())
df_terrace_bc["May"] = df_terrace_bc["May"].replace(-9999.9, df_terrace_bc["May"].median())
df_terrace_bc["Jun"] = df_terrace_bc["Jun"].replace(-9999.9, df_terrace_bc["Jun"].median())
df_terrace_bc["Jul"] = df_terrace_bc["Jul"].replace(-9999.9, df_terrace_bc["Jul"].median())
df_terrace_bc["Aug"] = df_terrace_bc["Aug"].replace(-9999.9, df_terrace_bc["Aug"].median())
df_terrace_bc["Sep"] = df_terrace_bc["Sep"].replace(-9999.9, df_terrace_bc["Sep"].median())
df_terrace_bc["Oct"] = df_terrace_bc["Oct"].replace(-9999.9, df_terrace_bc["Oct"].median())
df_terrace_bc["Nov"] = df_terrace_bc["Nov"].replace(-9999.9, df_terrace_bc["Nov"].median())
df_terrace_bc["Dec"] = df_terrace_bc["Dec"].replace(-9999.9, df_terrace_bc["Dec"].median())
df_terrace_bc["Annual"] = df_terrace_bc["Annual"].replace(-9999.9, df_terrace_bc["Annual"].median())
df_terrace_bc["Winter"] = df_terrace_bc["Winter"].replace(-9999.9, df_terrace_bc["Winter"].median())
df_terrace_bc["Spring"] = df_terrace_bc["Spring"].replace(-9999.9, df_terrace_bc["Spring"].median())
df_terrace_bc["Summer"] = df_terrace_bc["Summer"].replace(-9999.9, df_terrace_bc["Summer"].median())
df_terrace_bc["Autumn"] = df_terrace_bc["Autumn"].replace(-9999.9, df_terrace_bc["Autumn"].median())

x1 = df_terrace_bc["Year"]
y1 = df_terrace_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_terrace_bc["Year"]
y2 = df_terrace_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_terrace_bc["Year"]
y3 = df_terrace_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_terrace_bc["Year"]
y4 = df_terrace_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Terrace British Columbia")
plt.legend()
plt.show()

#Tofino British Columbia 

tofino_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/tofino_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_tofino_bc  = pd.DataFrame(tofino_bc )


df_tofino_bc["Jan"] = df_tofino_bc["Jan"].replace(-9999.9, df_tofino_bc["Jan"].median())
df_tofino_bc["Feb"] = df_tofino_bc["Feb"].replace(-9999.9, df_tofino_bc["Feb"].median())
df_tofino_bc["Mar"] = df_tofino_bc["Mar"].replace(-9999.9, df_tofino_bc["Mar"].median())
df_tofino_bc["Apr"] = df_tofino_bc["Apr"].replace(-9999.9, df_tofino_bc["Apr"].median())
df_tofino_bc["May"] = df_tofino_bc["May"].replace(-9999.9, df_tofino_bc["May"].median())
df_tofino_bc["Jun"] = df_tofino_bc["Jun"].replace(-9999.9, df_tofino_bc["Jun"].median())
df_tofino_bc["Jul"] = df_tofino_bc["Jul"].replace(-9999.9, df_tofino_bc["Jul"].median())
df_tofino_bc["Aug"] = df_tofino_bc["Aug"].replace(-9999.9, df_tofino_bc["Aug"].median())
df_tofino_bc["Sep"] = df_tofino_bc["Sep"].replace(-9999.9, df_tofino_bc["Sep"].median())
df_tofino_bc["Oct"] = df_tofino_bc["Oct"].replace(-9999.9, df_tofino_bc["Oct"].median())
df_tofino_bc["Nov"] = df_tofino_bc["Nov"].replace(-9999.9, df_tofino_bc["Nov"].median())
df_tofino_bc["Dec"] = df_tofino_bc["Dec"].replace(-9999.9, df_tofino_bc["Dec"].median())
df_tofino_bc["Annual"] = df_tofino_bc["Annual"].replace(-9999.9, df_tofino_bc["Annual"].median())
df_tofino_bc["Winter"] = df_tofino_bc["Winter"].replace(-9999.9, df_tofino_bc["Winter"].median())
df_tofino_bc["Spring"] = df_tofino_bc["Spring"].replace(-9999.9, df_tofino_bc["Spring"].median())
df_tofino_bc["Summer"] = df_tofino_bc["Summer"].replace(-9999.9, df_tofino_bc["Summer"].median())
df_tofino_bc["Autumn"] = df_tofino_bc["Autumn"].replace(-9999.9, df_tofino_bc["Autumn"].median())

x1 = df_tofino_bc["Year"]
y1 = df_tofino_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_tofino_bc["Year"]
y2 = df_tofino_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_tofino_bc["Year"]
y3 = df_tofino_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_tofino_bc["Year"]
y4 = df_tofino_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Tofino British Columbia")
plt.legend()
plt.show()

#Vancouver British Columbia 

vancouver_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/vancouver_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding ='utf-8-sig')
df_vancouver_bc = pd.DataFrame(vancouver_bc)

df_vancouver_bc["Jan"] = df_vancouver_bc["Jan"].replace(-9999.9, df_vancouver_bc["Jan"].median())
df_vancouver_bc["Feb"] = df_vancouver_bc["Feb"].replace(-9999.9, df_vancouver_bc["Feb"].median())
df_vancouver_bc["Mar"] = df_vancouver_bc["Mar"].replace(-9999.9, df_vancouver_bc["Mar"].median())
df_vancouver_bc["Apr"] = df_vancouver_bc["Apr"].replace(-9999.9, df_vancouver_bc["Apr"].median())
df_vancouver_bc["May"] = df_vancouver_bc["May"].replace(-9999.9, df_vancouver_bc["May"].median())
df_vancouver_bc["Jun"] = df_vancouver_bc["Jun"].replace(-9999.9, df_vancouver_bc["Jun"].median())
df_vancouver_bc["Jul"] = df_vancouver_bc["Jul"].replace(-9999.9, df_vancouver_bc["Jul"].median())
df_vancouver_bc["Aug"] = df_vancouver_bc["Aug"].replace(-9999.9, df_vancouver_bc["Aug"].median())
df_vancouver_bc["Sep"] = df_vancouver_bc["Sep"].replace(-9999.9, df_vancouver_bc["Sep"].median())
df_vancouver_bc["Oct"] = df_vancouver_bc["Oct"].replace(-9999.9, df_vancouver_bc["Oct"].median())
df_vancouver_bc["Nov"] = df_vancouver_bc["Nov"].replace(-9999.9, df_vancouver_bc["Nov"].median())
df_vancouver_bc["Dec"] = df_vancouver_bc["Dec"].replace(-9999.9, df_vancouver_bc["Dec"].median())
df_vancouver_bc["Annual"] = df_vancouver_bc["Annual"].replace(-9999.9, df_vancouver_bc["Annual"].median())
df_vancouver_bc["Winter"] = df_vancouver_bc["Winter"].replace(-9999.9, df_vancouver_bc["Winter"].median())
df_vancouver_bc["Spring"] = df_vancouver_bc["Spring"].replace(-9999.9, df_vancouver_bc["Spring"].median())
df_vancouver_bc["Summer"] = df_vancouver_bc["Summer"].replace(-9999.9, df_vancouver_bc["Summer"].median())
df_vancouver_bc["Autumn"] = df_vancouver_bc["Autumn"].replace(-9999.9, df_vancouver_bc["Autumn"].median())

x1 = df_vancouver_bc["Year"]
y1 = df_vancouver_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_vancouver_bc["Year"]
y2 = df_vancouver_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_vancouver_bc["Year"]
y3 = df_vancouver_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_vancouver_bc["Year"]
y4 = df_vancouver_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Vancouver British Columbia")
plt.legend()
plt.show()

#Victoria British Columbia 

victoria_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/victoria_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding ='utf-8-sig')
df_victoria_bc = pd.DataFrame(victoria_bc)

df_victoria_bc["Feb"] = df_victoria_bc["Feb"].replace(-9999.9, df_victoria_bc["Feb"].median())

x1 = df_victoria_bc["Year"]
y1 = df_victoria_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_victoria_bc["Year"]
y2 = df_victoria_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_victoria_bc["Year"]
y3 = df_victoria_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_victoria_bc["Year"]
y4 = df_victoria_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Victoria British Columbia")
plt.legend()
plt.show()

#Williamslake British Columbia 

williamslake_bc = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/williamslake_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_williamslake_bc = pd.DataFrame(williamslake_bc)

df_williamslake_bc["Jan"] = df_williamslake_bc["Jan"].replace(-9999.9, df_williamslake_bc["Jan"].median())
df_williamslake_bc["Feb"] = df_williamslake_bc["Feb"].replace(-9999.9, df_williamslake_bc["Feb"].median())
df_williamslake_bc["Mar"] = df_williamslake_bc["Mar"].replace(-9999.9, df_williamslake_bc["Mar"].median())
df_williamslake_bc["Apr"] = df_williamslake_bc["Apr"].replace(-9999.9, df_williamslake_bc["Apr"].median())
df_williamslake_bc["May"] = df_williamslake_bc["May"].replace(-9999.9, df_williamslake_bc["May"].median())
df_williamslake_bc["Jun"] = df_williamslake_bc["Jun"].replace(-9999.9, df_williamslake_bc["Jun"].median())
df_williamslake_bc["Jul"] = df_williamslake_bc["Jul"].replace(-9999.9, df_williamslake_bc["Jul"].median())
df_williamslake_bc["Aug"] = df_williamslake_bc["Aug"].replace(-9999.9, df_williamslake_bc["Aug"].median())
df_williamslake_bc["Sep"] = df_williamslake_bc["Sep"].replace(-9999.9, df_williamslake_bc["Sep"].median())
df_williamslake_bc["Oct"] = df_williamslake_bc["Oct"].replace(-9999.9, df_williamslake_bc["Oct"].median())
df_williamslake_bc["Nov"] = df_williamslake_bc["Nov"].replace(-9999.9, df_williamslake_bc["Nov"].median())
df_williamslake_bc["Dec"] = df_williamslake_bc["Dec"].replace(-9999.9, df_williamslake_bc["Dec"].median())
df_williamslake_bc["Annual"] = df_williamslake_bc["Annual"].replace(-9999.9, df_williamslake_bc["Annual"].median())
df_williamslake_bc["Winter"] = df_williamslake_bc["Winter"].replace(-9999.9, df_williamslake_bc["Winter"].median())
df_williamslake_bc["Spring"] = df_williamslake_bc["Spring"].replace(-9999.9, df_williamslake_bc["Spring"].median())
df_williamslake_bc["Summer"] = df_williamslake_bc["Summer"].replace(-9999.9, df_williamslake_bc["Summer"].median())
df_williamslake_bc["Autumn"] = df_williamslake_bc["Autumn"].replace(-9999.9, df_williamslake_bc["Autumn"].median())

x1 = df_williamslake_bc["Year"]
y1 = df_williamslake_bc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_williamslake_bc["Year"]
y2 = df_williamslake_bc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_williamslake_bc["Year"]
y3 = df_williamslake_bc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_williamslake_bc["Year"]
y4 = df_williamslake_bc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Williams Lake British Columbia")
plt.legend()
plt.show()
