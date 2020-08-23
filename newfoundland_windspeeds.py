#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd 
from matplotlib import pyplot as plt

#Bonavista Newfoundland 
bonavista_nfld = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/bonavista_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_bonavista_nfld = pd.DataFrame(bonavista_nfld)    

df_bonavista_nfld["Jan"] = df_bonavista_nfld["Jan"].replace(-9999.9, df_bonavista_nfld["Jan"].median())
df_bonavista_nfld["Feb"] = df_bonavista_nfld["Feb"].replace(-9999.9, df_bonavista_nfld["Feb"].median())
df_bonavista_nfld["Mar"] = df_bonavista_nfld["Mar"].replace(-9999.9, df_bonavista_nfld["Mar"].median())
df_bonavista_nfld["Apr"] = df_bonavista_nfld["Apr"].replace(-9999.9, df_bonavista_nfld["Apr"].median())
df_bonavista_nfld["May"] = df_bonavista_nfld["May"].replace(-9999.9, df_bonavista_nfld["May"].median())
df_bonavista_nfld["Jun"] = df_bonavista_nfld["Jun"].replace(-9999.9, df_bonavista_nfld["Jun"].median())
df_bonavista_nfld["Jul"] = df_bonavista_nfld["Jul"].replace(-9999.9, df_bonavista_nfld["Jul"].median())
df_bonavista_nfld["Aug"] = df_bonavista_nfld["Aug"].replace(-9999.9, df_bonavista_nfld["Aug"].median())
df_bonavista_nfld["Sep"] = df_bonavista_nfld["Sep"].replace(-9999.9, df_bonavista_nfld["Sep"].median())
df_bonavista_nfld["Oct"] = df_bonavista_nfld["Oct"].replace(-9999.9, df_bonavista_nfld["Oct"].median())
df_bonavista_nfld["Nov"] = df_bonavista_nfld["Nov"].replace(-9999.9, df_bonavista_nfld["Nov"].median())
df_bonavista_nfld["Dec"] = df_bonavista_nfld["Dec"].replace(-9999.9, df_bonavista_nfld["Dec"].median())
df_bonavista_nfld["Annual"] = df_bonavista_nfld["Annual"].replace(-9999.9, df_bonavista_nfld["Annual"].median())
df_bonavista_nfld["Winter"] = df_bonavista_nfld["Winter"].replace(-9999.9, df_bonavista_nfld["Winter"].median())
df_bonavista_nfld["Spring"] = df_bonavista_nfld["Spring"].replace(-9999.9, df_bonavista_nfld["Spring"].median())
df_bonavista_nfld["Summer"] = df_bonavista_nfld["Summer"].replace(-9999.9, df_bonavista_nfld["Summer"].median())
df_bonavista_nfld["Autumn"] = df_bonavista_nfld["Autumn"].replace(-9999.9, df_bonavista_nfld["Autumn"].median())

x1 = df_bonavista_nfld["Year"]
y1 = df_bonavista_nfld["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_bonavista_nfld["Year"]
y2 = df_bonavista_nfld["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_bonavista_nfld["Year"]
y3 = df_bonavista_nfld["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_bonavista_nfld["Year"]
y4 = df_bonavista_nfld["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Bonavista Newfoundland and Labrador")
plt.legend()
plt.show()

#Caperace Newfoundland 
    
caperace_nfld = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/caperace_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_caperace_nfld = pd.DataFrame(caperace_nfld)

df_caperace_nfld["Jan"] = df_caperace_nfld["Jan"].replace(-9999.9, df_caperace_nfld["Jan"].median())
df_caperace_nfld["Feb"] = df_caperace_nfld["Feb"].replace(-9999.9, df_caperace_nfld["Feb"].median())
df_caperace_nfld["Mar"] = df_caperace_nfld["Mar"].replace(-9999.9, df_caperace_nfld["Mar"].median())
df_caperace_nfld["Apr"] = df_caperace_nfld["Apr"].replace(-9999.9, df_caperace_nfld["Apr"].median())
df_caperace_nfld["May"] = df_caperace_nfld["May"].replace(-9999.9, df_caperace_nfld["May"].median())
df_caperace_nfld["Jun"] = df_caperace_nfld["Jun"].replace(-9999.9, df_caperace_nfld["Jun"].median())
df_caperace_nfld["Jul"] = df_caperace_nfld["Jul"].replace(-9999.9, df_caperace_nfld["Jul"].median())
df_caperace_nfld["Aug"] = df_caperace_nfld["Aug"].replace(-9999.9, df_caperace_nfld["Aug"].median())
df_caperace_nfld["Sep"] = df_caperace_nfld["Sep"].replace(-9999.9, df_caperace_nfld["Sep"].median())
df_caperace_nfld["Oct"] = df_caperace_nfld["Oct"].replace(-9999.9, df_caperace_nfld["Oct"].median())
df_caperace_nfld["Nov"] = df_caperace_nfld["Nov"].replace(-9999.9, df_caperace_nfld["Nov"].median())
df_caperace_nfld["Dec"] = df_caperace_nfld["Dec"].replace(-9999.9, df_caperace_nfld["Dec"].median())
df_caperace_nfld["Annual"] = df_caperace_nfld["Annual"].replace(-9999.9, df_caperace_nfld["Annual"].median())
df_caperace_nfld["Winter"] = df_caperace_nfld["Winter"].replace(-9999.9, df_caperace_nfld["Winter"].median())
df_caperace_nfld["Spring"] = df_caperace_nfld["Spring"].replace(-9999.9, df_caperace_nfld["Spring"].median())
df_caperace_nfld["Summer"] = df_caperace_nfld["Summer"].replace(-9999.9, df_caperace_nfld["Summer"].median())
df_caperace_nfld["Autumn"] = df_caperace_nfld["Autumn"].replace(-9999.9, df_caperace_nfld["Autumn"].median())

x1 = df_caperace_nfld["Year"]
y1 = df_caperace_nfld["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_caperace_nfld["Year"]
y2 = df_caperace_nfld["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_caperace_nfld["Year"]
y3 = df_caperace_nfld["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_caperace_nfld["Year"]
y4 = df_caperace_nfld["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Caperace Newfoundland and Labrador")
plt.legend()
plt.show()

#Cartwright Newfoundland 

cartwright_nfld = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/cartwright_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_cartwright_nfld = pd.DataFrame(cartwright_nfld)

df_cartwright_nfld["Jan"] = df_cartwright_nfld["Jan"].replace(-9999.9, df_cartwright_nfld["Jan"].median())
df_cartwright_nfld["Feb"] = df_cartwright_nfld["Feb"].replace(-9999.9, df_cartwright_nfld["Feb"].median())
df_cartwright_nfld["Mar"] = df_cartwright_nfld["Mar"].replace(-9999.9, df_cartwright_nfld["Mar"].median())
df_cartwright_nfld["Apr"] = df_cartwright_nfld["Apr"].replace(-9999.9, df_cartwright_nfld["Apr"].median())
df_cartwright_nfld["May"] = df_cartwright_nfld["May"].replace(-9999.9, df_cartwright_nfld["May"].median())
df_cartwright_nfld["Jun"] = df_cartwright_nfld["Jun"].replace(-9999.9, df_cartwright_nfld["Jun"].median())
df_cartwright_nfld["Jul"] = df_cartwright_nfld["Jul"].replace(-9999.9, df_cartwright_nfld["Jul"].median())
df_cartwright_nfld["Aug"] = df_cartwright_nfld["Aug"].replace(-9999.9, df_cartwright_nfld["Aug"].median())
df_cartwright_nfld["Sep"] = df_cartwright_nfld["Sep"].replace(-9999.9, df_cartwright_nfld["Sep"].median())
df_cartwright_nfld["Oct"] = df_cartwright_nfld["Oct"].replace(-9999.9, df_cartwright_nfld["Oct"].median())
df_cartwright_nfld["Nov"] = df_cartwright_nfld["Nov"].replace(-9999.9, df_cartwright_nfld["Nov"].median())
df_cartwright_nfld["Dec"] = df_cartwright_nfld["Dec"].replace(-9999.9, df_cartwright_nfld["Dec"].median())
df_cartwright_nfld["Annual"] = df_cartwright_nfld["Annual"].replace(-9999.9, df_cartwright_nfld["Annual"].median())
df_cartwright_nfld["Winter"] = df_cartwright_nfld["Winter"].replace(-9999.9, df_cartwright_nfld["Winter"].median())
df_cartwright_nfld["Spring"] = df_cartwright_nfld["Spring"].replace(-9999.9, df_cartwright_nfld["Spring"].median())
df_cartwright_nfld["Summer"] = df_cartwright_nfld["Summer"].replace(-9999.9, df_cartwright_nfld["Summer"].median())
df_cartwright_nfld["Autumn"] = df_cartwright_nfld["Autumn"].replace(-9999.9, df_cartwright_nfld["Autumn"].median())

x1 = df_cartwright_nfld["Year"]
y1 = df_cartwright_nfld["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_cartwright_nfld["Year"]
y2 = df_cartwright_nfld["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_cartwright_nfld["Year"]
y3 = df_cartwright_nfld["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_cartwright_nfld["Year"]
y4 = df_cartwright_nfld["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Cartwright Newfoundland and Labrador")
plt.legend()
plt.show()

#Danielsharbour Newfoundland 

danielsharbour_nfld = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/danielsharbour_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_danielsharbour_nfld = pd.DataFrame(danielsharbour_nfld)

df_danielsharbour_nfld.dropna(axis = 1, how='all', inplace = True)
df_danielsharbour_nfld.dropna(axis = 0, how='all', inplace = True)

df_danielsharbour_nfld["Jan"] = df_danielsharbour_nfld["Jan"].replace(-9999.9, df_danielsharbour_nfld["Jan"].median())
df_danielsharbour_nfld["Feb"] = df_danielsharbour_nfld["Feb"].replace(-9999.9, df_danielsharbour_nfld["Feb"].median())
df_danielsharbour_nfld["Mar"] = df_danielsharbour_nfld["Mar"].replace(-9999.9, df_danielsharbour_nfld["Mar"].median())
df_danielsharbour_nfld["Apr"] = df_danielsharbour_nfld["Apr"].replace(-9999.9, df_danielsharbour_nfld["Apr"].median())
df_danielsharbour_nfld["May"] = df_danielsharbour_nfld["May"].replace(-9999.9, df_danielsharbour_nfld["May"].median())
df_danielsharbour_nfld["Jun"] = df_danielsharbour_nfld["Jun"].replace(-9999.9, df_danielsharbour_nfld["Jun"].median())
df_danielsharbour_nfld["Jul"] = df_danielsharbour_nfld["Jul"].replace(-9999.9, df_danielsharbour_nfld["Jul"].median())
df_danielsharbour_nfld["Aug"] = df_danielsharbour_nfld["Aug"].replace(-9999.9, df_danielsharbour_nfld["Aug"].median())
df_danielsharbour_nfld["Sep"] = df_danielsharbour_nfld["Sep"].replace(-9999.9, df_danielsharbour_nfld["Sep"].median())
df_danielsharbour_nfld["Oct"] = df_danielsharbour_nfld["Oct"].replace(-9999.9, df_danielsharbour_nfld["Oct"].median())
df_danielsharbour_nfld["Nov"] = df_danielsharbour_nfld["Nov"].replace(-9999.9, df_danielsharbour_nfld["Nov"].median())
df_danielsharbour_nfld["Dec"] = df_danielsharbour_nfld["Dec"].replace(-9999.9, df_danielsharbour_nfld["Dec"].median())
df_danielsharbour_nfld["Annual"] = df_danielsharbour_nfld["Annual"].replace(-9999.9, df_danielsharbour_nfld["Annual"].median())
df_danielsharbour_nfld["Winter"] = df_danielsharbour_nfld["Winter"].replace(-9999.9, df_danielsharbour_nfld["Winter"].median())
df_danielsharbour_nfld["Spring"] = df_danielsharbour_nfld["Spring"].replace(-9999.9, df_danielsharbour_nfld["Spring"].median())
df_danielsharbour_nfld["Summer"] = df_danielsharbour_nfld["Summer"].replace(-9999.9, df_danielsharbour_nfld["Summer"].median())
df_danielsharbour_nfld["Autumn"] = df_danielsharbour_nfld["Autumn"].replace(-9999.9, df_danielsharbour_nfld["Autumn"].median())

x1 = df_danielsharbour_nfld["Year"]
y1 = df_danielsharbour_nfld["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_danielsharbour_nfld["Year"]
y2 = df_danielsharbour_nfld["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_danielsharbour_nfld["Year"]
y3 = df_danielsharbour_nfld["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_danielsharbour_nfld["Year"]
y4 = df_danielsharbour_nfld["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Danielsharbour Newfoundland and Labrador")
plt.legend()
plt.show()

#Deerlake Newfoundland 
    
deerlake_nfld = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/deerlake_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_deerlake_nfld = pd.DataFrame(deerlake_nfld)

df_deerlake_nfld["Jan"] = df_deerlake_nfld["Jan"].replace(-9999.9, df_deerlake_nfld["Jan"].median())
df_deerlake_nfld["Feb"] = df_deerlake_nfld["Feb"].replace(-9999.9, df_deerlake_nfld["Feb"].median())
df_deerlake_nfld["Mar"] = df_deerlake_nfld["Mar"].replace(-9999.9, df_deerlake_nfld["Mar"].median())
df_deerlake_nfld["Apr"] = df_deerlake_nfld["Apr"].replace(-9999.9, df_deerlake_nfld["Apr"].median())
df_deerlake_nfld["May"] = df_deerlake_nfld["May"].replace(-9999.9, df_deerlake_nfld["May"].median())
df_deerlake_nfld["Jun"] = df_deerlake_nfld["Jun"].replace(-9999.9, df_deerlake_nfld["Jun"].median())
df_deerlake_nfld["Jul"] = df_deerlake_nfld["Jul"].replace(-9999.9, df_deerlake_nfld["Jul"].median())
df_deerlake_nfld["Aug"] = df_deerlake_nfld["Aug"].replace(-9999.9, df_deerlake_nfld["Aug"].median())
df_deerlake_nfld["Sep"] = df_deerlake_nfld["Sep"].replace(-9999.9, df_deerlake_nfld["Sep"].median())
df_deerlake_nfld["Oct"] = df_deerlake_nfld["Oct"].replace(-9999.9, df_deerlake_nfld["Oct"].median())
df_deerlake_nfld["Nov"] = df_deerlake_nfld["Nov"].replace(-9999.9, df_deerlake_nfld["Nov"].median())
df_deerlake_nfld["Dec"] = df_deerlake_nfld["Dec"].replace(-9999.9, df_deerlake_nfld["Dec"].median())
df_deerlake_nfld["Annual"] = df_deerlake_nfld["Annual"].replace(-9999.9, df_deerlake_nfld["Annual"].median())
df_deerlake_nfld["Winter"] = df_deerlake_nfld["Winter"].replace(-9999.9, df_deerlake_nfld["Winter"].median())
df_deerlake_nfld["Spring"] = df_deerlake_nfld["Spring"].replace(-9999.9, df_deerlake_nfld["Spring"].median())
df_deerlake_nfld["Summer"] = df_deerlake_nfld["Summer"].replace(-9999.9, df_deerlake_nfld["Summer"].median())
df_deerlake_nfld["Autumn"] = df_deerlake_nfld["Autumn"].replace(-9999.9, df_deerlake_nfld["Autumn"].median())
 
x1 = df_deerlake_nfld["Year"]
y1 = df_deerlake_nfld["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_deerlake_nfld["Year"]
y2 = df_deerlake_nfld["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_deerlake_nfld["Year"]
y3 = df_deerlake_nfld["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_deerlake_nfld["Year"]
y4 = df_deerlake_nfld["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Deerlake Newfoundland")
plt.legend()
plt.show()

#Ganderinternationalairport Newfoundland 
    
ganderinternationalairport_nfld = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/ganderinternationalairport_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_ganderinternationalairport_nfld = pd.DataFrame(ganderinternationalairport_nfld)

df_ganderinternationalairport_nfld["Jan"] = df_ganderinternationalairport_nfld["Jan"].replace(-9999.9, df_ganderinternationalairport_nfld["Jan"].median())
df_ganderinternationalairport_nfld["Feb"] = df_ganderinternationalairport_nfld["Feb"].replace(-9999.9, df_ganderinternationalairport_nfld["Feb"].median())
df_ganderinternationalairport_nfld["Mar"] = df_ganderinternationalairport_nfld["Mar"].replace(-9999.9, df_ganderinternationalairport_nfld["Mar"].median())
df_ganderinternationalairport_nfld["Apr"] = df_ganderinternationalairport_nfld["Apr"].replace(-9999.9, df_ganderinternationalairport_nfld["Apr"].median())
df_ganderinternationalairport_nfld["May"] = df_ganderinternationalairport_nfld["May"].replace(-9999.9, df_ganderinternationalairport_nfld["May"].median())
df_ganderinternationalairport_nfld["Jun"] = df_ganderinternationalairport_nfld["Jun"].replace(-9999.9, df_ganderinternationalairport_nfld["Jun"].median())
df_ganderinternationalairport_nfld["Jul"] = df_ganderinternationalairport_nfld["Jul"].replace(-9999.9, df_ganderinternationalairport_nfld["Jul"].median())
df_ganderinternationalairport_nfld["Aug"] = df_ganderinternationalairport_nfld["Aug"].replace(-9999.9, df_ganderinternationalairport_nfld["Aug"].median())
df_ganderinternationalairport_nfld["Sep"] = df_ganderinternationalairport_nfld["Sep"].replace(-9999.9, df_ganderinternationalairport_nfld["Sep"].median())
df_ganderinternationalairport_nfld["Oct"] = df_ganderinternationalairport_nfld["Oct"].replace(-9999.9, df_ganderinternationalairport_nfld["Oct"].median())
df_ganderinternationalairport_nfld["Nov"] = df_ganderinternationalairport_nfld["Nov"].replace(-9999.9, df_ganderinternationalairport_nfld["Nov"].median())
df_ganderinternationalairport_nfld["Dec"] = df_ganderinternationalairport_nfld["Dec"].replace(-9999.9, df_ganderinternationalairport_nfld["Dec"].median())
df_ganderinternationalairport_nfld["Annual"] = df_ganderinternationalairport_nfld["Annual"].replace(-9999.9, df_ganderinternationalairport_nfld["Annual"].median())
df_ganderinternationalairport_nfld["Winter"] = df_ganderinternationalairport_nfld["Winter"].replace(-9999.9, df_ganderinternationalairport_nfld["Winter"].median())
df_ganderinternationalairport_nfld["Spring"] = df_ganderinternationalairport_nfld["Spring"].replace(-9999.9, df_ganderinternationalairport_nfld["Spring"].median())
df_ganderinternationalairport_nfld["Summer"] = df_ganderinternationalairport_nfld["Summer"].replace(-9999.9, df_ganderinternationalairport_nfld["Summer"].median())
df_ganderinternationalairport_nfld["Autumn"] = df_ganderinternationalairport_nfld["Autumn"].replace(-9999.9, df_ganderinternationalairport_nfld["Autumn"].median())

x1 = df_ganderinternationalairport_nfld["Year"]
y1 = df_ganderinternationalairport_nfld["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_ganderinternationalairport_nfld["Year"]
y2 = df_ganderinternationalairport_nfld["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_ganderinternationalairport_nfld["Year"]
y3 = df_ganderinternationalairport_nfld["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_ganderinternationalairport_nfld["Year"]
y4 = df_ganderinternationalairport_nfld["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Gander International Airport Newfoundland and Labrador")
plt.legend()
plt.show()


#Goose Newfoundland

goose_nfld = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/goose_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_goose_nfld = pd.DataFrame(goose_nfld)

df_goose_nfld["Jan"] = df_goose_nfld["Jan"].replace(-9999.9, df_goose_nfld["Jan"].median())
df_goose_nfld["Feb"] = df_goose_nfld["Feb"].replace(-9999.9, df_goose_nfld["Feb"].median())
df_goose_nfld["Mar"] = df_goose_nfld["Mar"].replace(-9999.9, df_goose_nfld["Mar"].median())
df_goose_nfld["Apr"] = df_goose_nfld["Apr"].replace(-9999.9, df_goose_nfld["Apr"].median())
df_goose_nfld["May"] = df_goose_nfld["May"].replace(-9999.9, df_goose_nfld["May"].median())
df_goose_nfld["Jun"] = df_goose_nfld["Jun"].replace(-9999.9, df_goose_nfld["Jun"].median())
df_goose_nfld["Jul"] = df_goose_nfld["Jul"].replace(-9999.9, df_goose_nfld["Jul"].median())
df_goose_nfld["Aug"] = df_goose_nfld["Aug"].replace(-9999.9, df_goose_nfld["Aug"].median())
df_goose_nfld["Sep"] = df_goose_nfld["Sep"].replace(-9999.9, df_goose_nfld["Sep"].median())
df_goose_nfld["Oct"] = df_goose_nfld["Oct"].replace(-9999.9, df_goose_nfld["Oct"].median())
df_goose_nfld["Nov"] = df_goose_nfld["Nov"].replace(-9999.9, df_goose_nfld["Nov"].median())
df_goose_nfld["Dec"] = df_goose_nfld["Dec"].replace(-9999.9, df_goose_nfld["Dec"].median())
df_goose_nfld["Annual"] = df_goose_nfld["Annual"].replace(-9999.9, df_goose_nfld["Annual"].median())
df_goose_nfld["Winter"] = df_goose_nfld["Winter"].replace(-9999.9, df_goose_nfld["Winter"].median())
df_goose_nfld["Spring"] = df_goose_nfld["Spring"].replace(-9999.9, df_goose_nfld["Spring"].median())
df_goose_nfld["Summer"] = df_goose_nfld["Summer"].replace(-9999.9, df_goose_nfld["Summer"].median())
df_goose_nfld["Autumn"] = df_goose_nfld["Autumn"].replace(-9999.9, df_goose_nfld["Autumn"].median())

x1 = df_goose_nfld["Year"]
y1 = df_goose_nfld["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_goose_nfld["Year"]
y2 = df_goose_nfld["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_goose_nfld["Year"]
y3 = df_goose_nfld["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_goose_nfld["Year"]
y4 = df_goose_nfld["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Goose Newfoundland Labrador")
plt.legend()
plt.show()

#Hopedale Newfoundland 

hopedale_nfld = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/hopedale_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_hopedale_nfld = pd.DataFrame(hopedale_nfld)

df_hopedale_nfld["Jan"] = df_hopedale_nfld["Jan"].replace(-9999.9, df_hopedale_nfld["Jan"].median())
df_hopedale_nfld["Feb"] = df_hopedale_nfld["Feb"].replace(-9999.9, df_hopedale_nfld["Feb"].median())
df_hopedale_nfld["Mar"] = df_hopedale_nfld["Mar"].replace(-9999.9, df_hopedale_nfld["Mar"].median())
df_hopedale_nfld["Apr"] = df_hopedale_nfld["Apr"].replace(-9999.9, df_hopedale_nfld["Apr"].median())
df_hopedale_nfld["May"] = df_hopedale_nfld["May"].replace(-9999.9, df_hopedale_nfld["May"].median())
df_hopedale_nfld["Jun"] = df_hopedale_nfld["Jun"].replace(-9999.9, df_hopedale_nfld["Jun"].median())
df_hopedale_nfld["Jul"] = df_hopedale_nfld["Jul"].replace(-9999.9, df_hopedale_nfld["Jul"].median())
df_hopedale_nfld["Aug"] = df_hopedale_nfld["Aug"].replace(-9999.9, df_hopedale_nfld["Aug"].median())
df_hopedale_nfld["Sep"] = df_hopedale_nfld["Sep"].replace(-9999.9, df_hopedale_nfld["Sep"].median())
df_hopedale_nfld["Oct"] = df_hopedale_nfld["Oct"].replace(-9999.9, df_hopedale_nfld["Oct"].median())
df_hopedale_nfld["Nov"] = df_hopedale_nfld["Nov"].replace(-9999.9, df_hopedale_nfld["Nov"].median())
df_hopedale_nfld["Dec"] = df_hopedale_nfld["Dec"].replace(-9999.9, df_hopedale_nfld["Dec"].median())
df_hopedale_nfld["Annual"] = df_hopedale_nfld["Annual"].replace(-9999.9, df_hopedale_nfld["Annual"].median())
df_hopedale_nfld["Winter"] = df_hopedale_nfld["Winter"].replace(-9999.9, df_hopedale_nfld["Winter"].median())
df_hopedale_nfld["Spring"] = df_hopedale_nfld["Spring"].replace(-9999.9, df_hopedale_nfld["Spring"].median())
df_hopedale_nfld["Summer"] = df_hopedale_nfld["Summer"].replace(-9999.9, df_hopedale_nfld["Summer"].median())
df_hopedale_nfld["Autumn"] = df_hopedale_nfld["Autumn"].replace(-9999.9, df_hopedale_nfld["Autumn"].median())

x1 = df_hopedale_nfld["Year"]
y1 = df_hopedale_nfld["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_hopedale_nfld["Year"]
y2 = df_hopedale_nfld["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_hopedale_nfld["Year"]
y3 = df_hopedale_nfld["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_hopedale_nfld["Year"]
y4 = df_hopedale_nfld["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Hopedale Newfoundland and Labrador")
plt.legend()
plt.show()

#Port Aux Basque Newfoundland 

portauxbasque_nfld = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/portauxbasque_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_portauxbasque_nfld = pd.DataFrame(portauxbasque_nfld)


df_portauxbasque_nfld["Jan"] = df_portauxbasque_nfld["Jan"].replace(-9999.9, df_portauxbasque_nfld["Jan"].median())
df_portauxbasque_nfld["Feb"] = df_portauxbasque_nfld["Feb"].replace(-9999.9, df_portauxbasque_nfld["Feb"].median())
df_portauxbasque_nfld["Mar"] = df_portauxbasque_nfld["Mar"].replace(-9999.9, df_portauxbasque_nfld["Mar"].median())
df_portauxbasque_nfld["Apr"] = df_portauxbasque_nfld["Apr"].replace(-9999.9, df_portauxbasque_nfld["Apr"].median())
df_portauxbasque_nfld["May"] = df_portauxbasque_nfld["May"].replace(-9999.9, df_portauxbasque_nfld["May"].median())
df_portauxbasque_nfld["Jun"] = df_portauxbasque_nfld["Jun"].replace(-9999.9, df_portauxbasque_nfld["Jun"].median())
df_portauxbasque_nfld["Jul"] = df_portauxbasque_nfld["Jul"].replace(-9999.9, df_portauxbasque_nfld["Jul"].median())
df_portauxbasque_nfld["Aug"] = df_portauxbasque_nfld["Aug"].replace(-9999.9, df_portauxbasque_nfld["Aug"].median())
df_portauxbasque_nfld["Sep"] = df_portauxbasque_nfld["Sep"].replace(-9999.9, df_portauxbasque_nfld["Sep"].median())
df_portauxbasque_nfld["Oct"] = df_portauxbasque_nfld["Oct"].replace(-9999.9, df_portauxbasque_nfld["Oct"].median())
df_portauxbasque_nfld["Nov"] = df_portauxbasque_nfld["Nov"].replace(-9999.9, df_portauxbasque_nfld["Nov"].median())
df_portauxbasque_nfld["Dec"] = df_portauxbasque_nfld["Dec"].replace(-9999.9, df_portauxbasque_nfld["Dec"].median())
df_portauxbasque_nfld["Annual"] = df_portauxbasque_nfld["Annual"].replace(-9999.9, df_portauxbasque_nfld["Annual"].median())
df_portauxbasque_nfld["Winter"] = df_portauxbasque_nfld["Winter"].replace(-9999.9, df_portauxbasque_nfld["Winter"].median())
df_portauxbasque_nfld["Spring"] = df_portauxbasque_nfld["Spring"].replace(-9999.9, df_portauxbasque_nfld["Spring"].median())
df_portauxbasque_nfld["Summer"] = df_portauxbasque_nfld["Summer"].replace(-9999.9, df_portauxbasque_nfld["Summer"].median())
df_portauxbasque_nfld["Autumn"] = df_portauxbasque_nfld["Autumn"].replace(-9999.9, df_portauxbasque_nfld["Autumn"].median())

x1 = df_portauxbasque_nfld["Year"]
y1 = df_portauxbasque_nfld["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_portauxbasque_nfld["Year"]
y2 = df_portauxbasque_nfld["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_portauxbasque_nfld["Year"]
y3 = df_portauxbasque_nfld["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_portauxbasque_nfld["Year"]
y4 = df_portauxbasque_nfld["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Port aux Basque Newfoundland and Labrador")
plt.legend()
plt.show()

#Stephenville Newfoundland 

stephenville_nfld = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/stephenville_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_stephenville_nfld = pd.DataFrame(stephenville_nfld)

df_stephenville_nfld["Jan"] = df_stephenville_nfld["Jan"].replace(-9999.9, df_stephenville_nfld["Jan"].median())
df_stephenville_nfld["Feb"] = df_stephenville_nfld["Feb"].replace(-9999.9, df_stephenville_nfld["Feb"].median())
df_stephenville_nfld["Mar"] = df_stephenville_nfld["Mar"].replace(-9999.9, df_stephenville_nfld["Mar"].median())
df_stephenville_nfld["Apr"] = df_stephenville_nfld["Apr"].replace(-9999.9, df_stephenville_nfld["Apr"].median())
df_stephenville_nfld["May"] = df_stephenville_nfld["May"].replace(-9999.9, df_stephenville_nfld["May"].median())
df_stephenville_nfld["Jun"] = df_stephenville_nfld["Jun"].replace(-9999.9, df_stephenville_nfld["Jun"].median())
df_stephenville_nfld["Jul"] = df_stephenville_nfld["Jul"].replace(-9999.9, df_stephenville_nfld["Jul"].median())
df_stephenville_nfld["Aug"] = df_stephenville_nfld["Aug"].replace(-9999.9, df_stephenville_nfld["Aug"].median())
df_stephenville_nfld["Sep"] = df_stephenville_nfld["Sep"].replace(-9999.9, df_stephenville_nfld["Sep"].median())
df_stephenville_nfld["Oct"] = df_stephenville_nfld["Oct"].replace(-9999.9, df_stephenville_nfld["Oct"].median())
df_stephenville_nfld["Nov"] = df_stephenville_nfld["Nov"].replace(-9999.9, df_stephenville_nfld["Nov"].median())
df_stephenville_nfld["Dec"] = df_stephenville_nfld["Dec"].replace(-9999.9, df_stephenville_nfld["Dec"].median())
df_stephenville_nfld["Annual"] = df_stephenville_nfld["Annual"].replace(-9999.9, df_stephenville_nfld["Annual"].median())
df_stephenville_nfld["Winter"] = df_stephenville_nfld["Winter"].replace(-9999.9, df_stephenville_nfld["Winter"].median())
df_stephenville_nfld["Spring"] = df_stephenville_nfld["Spring"].replace(-9999.9, df_stephenville_nfld["Spring"].median())
df_stephenville_nfld["Summer"] = df_stephenville_nfld["Summer"].replace(-9999.9, df_stephenville_nfld["Summer"].median())
df_stephenville_nfld["Autumn"] = df_stephenville_nfld["Autumn"].replace(-9999.9, df_stephenville_nfld["Autumn"].median())

x1 = df_stephenville_nfld["Year"]
y1 = df_stephenville_nfld["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_stephenville_nfld["Year"]
y2 = df_stephenville_nfld["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_stephenville_nfld["Year"]
y3 = df_stephenville_nfld["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_stephenville_nfld["Year"]
y4 = df_stephenville_nfld["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Stephenville Newfoundland and Labrador")
plt.legend()
plt.show()

#St Johns Newfoundland 

stjohns_nfld = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/stjohns_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_stjohns_nfld = pd.DataFrame(stjohns_nfld)

df_stjohns_nfld["Jan"] = df_stjohns_nfld["Jan"].replace(-9999.9, df_stjohns_nfld["Jan"].median())
df_stjohns_nfld["Feb"] = df_stjohns_nfld["Feb"].replace(-9999.9, df_stjohns_nfld["Feb"].median())
df_stjohns_nfld["Mar"] = df_stjohns_nfld["Mar"].replace(-9999.9, df_stjohns_nfld["Mar"].median())
df_stjohns_nfld["Apr"] = df_stjohns_nfld["Apr"].replace(-9999.9, df_stjohns_nfld["Apr"].median())
df_stjohns_nfld["May"] = df_stjohns_nfld["May"].replace(-9999.9, df_stjohns_nfld["May"].median())
df_stjohns_nfld["Jun"] = df_stjohns_nfld["Jun"].replace(-9999.9, df_stjohns_nfld["Jun"].median())
df_stjohns_nfld["Jul"] = df_stjohns_nfld["Jul"].replace(-9999.9, df_stjohns_nfld["Jul"].median())
df_stjohns_nfld["Aug"] = df_stjohns_nfld["Aug"].replace(-9999.9, df_stjohns_nfld["Aug"].median())
df_stjohns_nfld["Sep"] = df_stjohns_nfld["Sep"].replace(-9999.9, df_stjohns_nfld["Sep"].median())
df_stjohns_nfld["Oct"] = df_stjohns_nfld["Oct"].replace(-9999.9, df_stjohns_nfld["Oct"].median())
df_stjohns_nfld["Nov"] = df_stjohns_nfld["Nov"].replace(-9999.9, df_stjohns_nfld["Nov"].median())
df_stjohns_nfld["Dec"] = df_stjohns_nfld["Dec"].replace(-9999.9, df_stjohns_nfld["Dec"].median())
df_stjohns_nfld["Annual"] = df_stjohns_nfld["Annual"].replace(-9999.9, df_stjohns_nfld["Annual"].median())
df_stjohns_nfld["Winter"] = df_stjohns_nfld["Winter"].replace(-9999.9, df_stjohns_nfld["Winter"].median())
df_stjohns_nfld["Spring"] = df_stjohns_nfld["Spring"].replace(-9999.9, df_stjohns_nfld["Spring"].median())
df_stjohns_nfld["Summer"] = df_stjohns_nfld["Summer"].replace(-9999.9, df_stjohns_nfld["Summer"].median())
df_stjohns_nfld["Autumn"] = df_stjohns_nfld["Autumn"].replace(-9999.9, df_stjohns_nfld["Autumn"].median())

x1 = df_stjohns_nfld["Year"]
y1 = df_stjohns_nfld["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_stjohns_nfld["Year"]
y2 = df_stjohns_nfld["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_stjohns_nfld["Year"]
y3 = df_stjohns_nfld["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_stjohns_nfld["Year"]
y4 = df_stjohns_nfld["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("St.Johns Newfoundland and Labrador")
plt.legend()
plt.show()

#Wabushlake NewFoundland 

wabushlake_nfld = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/wabushlake_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_wabushlake_nfld  = pd.DataFrame(wabushlake_nfld)

df_wabushlake_nfld["Jan"] = df_wabushlake_nfld["Jan"].replace(-9999.9, df_wabushlake_nfld["Jan"].median())
df_wabushlake_nfld["Feb"] = df_wabushlake_nfld["Feb"].replace(-9999.9, df_wabushlake_nfld["Feb"].median())
df_wabushlake_nfld["Mar"] = df_wabushlake_nfld["Mar"].replace(-9999.9, df_wabushlake_nfld["Mar"].median())
df_wabushlake_nfld["Apr"] = df_wabushlake_nfld["Apr"].replace(-9999.9, df_wabushlake_nfld["Apr"].median())
df_wabushlake_nfld["May"] = df_wabushlake_nfld["May"].replace(-9999.9, df_wabushlake_nfld["May"].median())
df_wabushlake_nfld["Jun"] = df_wabushlake_nfld["Jun"].replace(-9999.9, df_wabushlake_nfld["Jun"].median())
df_wabushlake_nfld["Jul"] = df_wabushlake_nfld["Jul"].replace(-9999.9, df_wabushlake_nfld["Jul"].median())
df_wabushlake_nfld["Aug"] = df_wabushlake_nfld["Aug"].replace(-9999.9, df_wabushlake_nfld["Aug"].median())
df_wabushlake_nfld["Sep"] = df_wabushlake_nfld["Sep"].replace(-9999.9, df_wabushlake_nfld["Sep"].median())
df_wabushlake_nfld["Oct"] = df_wabushlake_nfld["Oct"].replace(-9999.9, df_wabushlake_nfld["Oct"].median())
df_wabushlake_nfld["Nov"] = df_wabushlake_nfld["Nov"].replace(-9999.9, df_wabushlake_nfld["Nov"].median())
df_wabushlake_nfld["Dec"] = df_wabushlake_nfld["Dec"].replace(-9999.9, df_wabushlake_nfld["Dec"].median())
df_wabushlake_nfld["Annual"] = df_wabushlake_nfld["Annual"].replace(-9999.9, df_wabushlake_nfld["Annual"].median())
df_wabushlake_nfld["Winter"] = df_wabushlake_nfld["Winter"].replace(-9999.9, df_wabushlake_nfld["Winter"].median())
df_wabushlake_nfld["Spring"] = df_wabushlake_nfld["Spring"].replace(-9999.9, df_wabushlake_nfld["Spring"].median())
df_wabushlake_nfld["Summer"] = df_wabushlake_nfld["Summer"].replace(-9999.9, df_wabushlake_nfld["Summer"].median())
df_wabushlake_nfld["Autumn"] = df_wabushlake_nfld["Autumn"].replace(-9999.9, df_wabushlake_nfld["Autumn"].median())

x1 = df_wabushlake_nfld["Year"]
y1 = df_wabushlake_nfld["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_wabushlake_nfld["Year"]
y2 = df_wabushlake_nfld["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_wabushlake_nfld["Year"]
y3 = df_wabushlake_nfld["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_wabushlake_nfld["Year"]
y4 = df_wabushlake_nfld["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Wabushlake Newfoundland and Labrador")
plt.legend()
plt.show()


