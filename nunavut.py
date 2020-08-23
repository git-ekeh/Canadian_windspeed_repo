#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd 
from matplotlib import pyplot as plt


#Alert Nunavut
alert_nu = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/alert_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_alert_nu = pd.DataFrame(alert_nu)

df_alert_nu = pd.DataFrame(alert_nu)
df_alert_nu["Jan"] = df_alert_nu["Jan"].replace(-9999.9, df_alert_nu["Jan"].median())
df_alert_nu["Feb"] = df_alert_nu["Feb"].replace(-9999.9, df_alert_nu["Feb"].median())
df_alert_nu["Mar"] = df_alert_nu["Mar"].replace(-9999.9, df_alert_nu["Mar"].median())
df_alert_nu["Apr"] = df_alert_nu["Apr"].replace(-9999.9, df_alert_nu["Apr"].median())
df_alert_nu["May"] = df_alert_nu["May"].replace(-9999.9, df_alert_nu["May"].median())
df_alert_nu["Jun"] = df_alert_nu["Jun"].replace(-9999.9, df_alert_nu["Jun"].median())
df_alert_nu["Jul"] = df_alert_nu["Jul"].replace(-9999.9, df_alert_nu["Jul"].median())
df_alert_nu["Aug"] = df_alert_nu["Aug"].replace(-9999.9, df_alert_nu["Aug"].median())
df_alert_nu["Sep"] = df_alert_nu["Sep"].replace(-9999.9, df_alert_nu["Sep"].median())
df_alert_nu["Oct"] = df_alert_nu["Oct"].replace(-9999.9, df_alert_nu["Oct"].median())
df_alert_nu["Nov"] = df_alert_nu["Nov"].replace(-9999.9, df_alert_nu["Nov"].median())
df_alert_nu["Dec"] = df_alert_nu["Dec"].replace(-9999.9, df_alert_nu["Dec"].median())
df_alert_nu["Annual"] = df_alert_nu["Annual"].replace(-9999.9, df_alert_nu["Annual"].median())
df_alert_nu["Winter"] = df_alert_nu["Winter"].replace(-9999.9, df_alert_nu["Winter"].median())
df_alert_nu["Spring"] = df_alert_nu["Spring"].replace(-9999.9, df_alert_nu["Spring"].median())
df_alert_nu["Summer"] = df_alert_nu["Summer"].replace(-9999.9, df_alert_nu["Summer"].median())
df_alert_nu["Autumn"] = df_alert_nu["Autumn"].replace(-9999.9, df_alert_nu["Autumn"].median())



x1 = df_alert_nu["Year"]
y1 = df_alert_nu["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_alert_nu["Year"]
y2 = df_alert_nu["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_alert_nu["Year"]
y3 = df_alert_nu["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_alert_nu["Year"]
y4 = df_alert_nu["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Alert Nunavut")
plt.legend()
plt.show()

#Bakerlake Nunanvut
bakerlake_nu = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/bakerlake_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_bakerlake_nu = pd.DataFrame(bakerlake_nu)

df_bakerlake_nu["Jan"] = df_bakerlake_nu["Jan"].replace(-9999.9, df_bakerlake_nu["Jan"].median())
df_bakerlake_nu["Feb"] = df_bakerlake_nu["Feb"].replace(-9999.9, df_bakerlake_nu["Feb"].median())
df_bakerlake_nu["Mar"] = df_bakerlake_nu["Mar"].replace(-9999.9, df_bakerlake_nu["Mar"].median())
df_bakerlake_nu["Apr"] = df_bakerlake_nu["Apr"].replace(-9999.9, df_bakerlake_nu["Apr"].median())
df_bakerlake_nu["May"] = df_bakerlake_nu["May"].replace(-9999.9, df_bakerlake_nu["May"].median())
df_bakerlake_nu["Jun"] = df_bakerlake_nu["Jun"].replace(-9999.9, df_bakerlake_nu["Jun"].median())
df_bakerlake_nu["Jul"] = df_bakerlake_nu["Jul"].replace(-9999.9, df_bakerlake_nu["Jul"].median())
df_bakerlake_nu["Aug"] = df_bakerlake_nu["Aug"].replace(-9999.9, df_bakerlake_nu["Aug"].median())
df_bakerlake_nu["Sep"] = df_bakerlake_nu["Sep"].replace(-9999.9, df_bakerlake_nu["Sep"].median())
df_bakerlake_nu["Oct"] = df_bakerlake_nu["Oct"].replace(-9999.9, df_bakerlake_nu["Oct"].median())
df_bakerlake_nu["Nov"] = df_bakerlake_nu["Nov"].replace(-9999.9, df_bakerlake_nu["Nov"].median())
df_bakerlake_nu["Dec"] = df_bakerlake_nu["Dec"].replace(-9999.9, df_bakerlake_nu["Dec"].median())
df_bakerlake_nu["Annual"] = df_bakerlake_nu["Annual"].replace(-9999.9, df_bakerlake_nu["Annual"].median())
df_bakerlake_nu["Winter"] = df_bakerlake_nu["Winter"].replace(-9999.9, df_bakerlake_nu["Winter"].median())
df_bakerlake_nu["Spring"] = df_bakerlake_nu["Spring"].replace(-9999.9, df_bakerlake_nu["Spring"].median())
df_bakerlake_nu["Summer"] = df_bakerlake_nu["Summer"].replace(-9999.9, df_bakerlake_nu["Summer"].median())
df_bakerlake_nu["Autumn"] = df_bakerlake_nu["Autumn"].replace(-9999.9, df_bakerlake_nu["Autumn"].median())

x1 = df_bakerlake_nu["Year"]
y1 = df_bakerlake_nu["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_bakerlake_nu["Year"]
y2 = df_bakerlake_nu["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_bakerlake_nu["Year"]
y3 = df_bakerlake_nu["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_bakerlake_nu["Year"]
y4 = df_bakerlake_nu["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Bakerlake Nunavut")
plt.legend()
plt.show()

#Cambridgebay Nunavut 
    
cambridgebay_nu = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/cambridgebay_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_cambridgebay_nu = pd.DataFrame(cambridgebay_nu)


x1 = df_cambridgebay_nu["Year"]
y1 = df_cambridgebay_nu["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_cambridgebay_nu["Year"]
y2 = df_cambridgebay_nu["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_cambridgebay_nu["Year"]
y3 = df_cambridgebay_nu["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_cambridgebay_nu["Year"]
y4 = df_cambridgebay_nu["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Cambridge Nunavut")
plt.legend()
plt.show()

#Capehooper Nunavut 
    
capehooper_nu = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/capehooper_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_capehooper_nu = pd.DataFrame(capehooper_nu)

df_capehooper_nu["Jan"] = df_capehooper_nu["Jan"].replace(-9999.9, df_capehooper_nu["Jan"].median())
df_capehooper_nu["Feb"] = df_capehooper_nu["Feb"].replace(-9999.9, df_capehooper_nu["Feb"].median())
df_capehooper_nu["Mar"] = df_capehooper_nu["Mar"].replace(-9999.9, df_capehooper_nu["Mar"].median())
df_capehooper_nu["Apr"] = df_capehooper_nu["Apr"].replace(-9999.9, df_capehooper_nu["Apr"].median())
df_capehooper_nu["May"] = df_capehooper_nu["May"].replace(-9999.9, df_capehooper_nu["May"].median())
df_capehooper_nu["Jun"] = df_capehooper_nu["Jun"].replace(-9999.9, df_capehooper_nu["Jun"].median())
df_capehooper_nu["Jul"] = df_capehooper_nu["Jul"].replace(-9999.9, df_capehooper_nu["Jul"].median())
df_capehooper_nu["Aug"] = df_capehooper_nu["Aug"].replace(-9999.9, df_capehooper_nu["Aug"].median())
df_capehooper_nu["Sep"] = df_capehooper_nu["Sep"].replace(-9999.9, df_capehooper_nu["Sep"].median())
df_capehooper_nu["Oct"] = df_capehooper_nu["Oct"].replace(-9999.9, df_capehooper_nu["Oct"].median())
df_capehooper_nu["Nov"] = df_capehooper_nu["Nov"].replace(-9999.9, df_capehooper_nu["Nov"].median())
df_capehooper_nu["Dec"] = df_capehooper_nu["Dec"].replace(-9999.9, df_capehooper_nu["Dec"].median())
df_capehooper_nu["Annual"] = df_capehooper_nu["Annual"].replace(-9999.9, df_capehooper_nu["Annual"].median())
df_capehooper_nu["Winter"] = df_capehooper_nu["Winter"].replace(-9999.9, df_capehooper_nu["Winter"].median())
df_capehooper_nu["Spring"] = df_capehooper_nu["Spring"].replace(-9999.9, df_capehooper_nu["Spring"].median())
df_capehooper_nu["Summer"] = df_capehooper_nu["Summer"].replace(-9999.9, df_capehooper_nu["Summer"].median())
df_capehooper_nu["Autumn"] = df_capehooper_nu["Autumn"].replace(-9999.9, df_capehooper_nu["Autumn"].median())


x1 = df_capehooper_nu["Year"]
y1 = df_capehooper_nu["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_capehooper_nu["Year"]
y2 = df_capehooper_nu["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_capehooper_nu["Year"]
y3 = df_capehooper_nu["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_capehooper_nu["Year"]
y4 = df_capehooper_nu["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Capehooper Nunavut")
plt.legend()
plt.show()

#Clyde Nunuvut 
clyde_nu = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/clyde_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_clyde_nu = pd.DataFrame(clyde_nu)

df_clyde_nu["Jan"] = df_clyde_nu["Jan"].replace(-9999.9, df_clyde_nu["Jan"].median())
df_clyde_nu["Feb"] = df_clyde_nu["Feb"].replace(-9999.9, df_clyde_nu["Feb"].median())
df_clyde_nu["Mar"] = df_clyde_nu["Mar"].replace(-9999.9, df_clyde_nu["Mar"].median())
df_clyde_nu["Apr"] = df_clyde_nu["Apr"].replace(-9999.9, df_clyde_nu["Apr"].median())
df_clyde_nu["May"] = df_clyde_nu["May"].replace(-9999.9, df_clyde_nu["May"].median())
df_clyde_nu["Jun"] = df_clyde_nu["Jun"].replace(-9999.9, df_clyde_nu["Jun"].median())
df_clyde_nu["Jul"] = df_clyde_nu["Jul"].replace(-9999.9, df_clyde_nu["Jul"].median())
df_clyde_nu["Aug"] = df_clyde_nu["Aug"].replace(-9999.9, df_clyde_nu["Aug"].median())
df_clyde_nu["Sep"] = df_clyde_nu["Sep"].replace(-9999.9, df_clyde_nu["Sep"].median())
df_clyde_nu["Oct"] = df_clyde_nu["Oct"].replace(-9999.9, df_clyde_nu["Oct"].median())
df_clyde_nu["Nov"] = df_clyde_nu["Nov"].replace(-9999.9, df_clyde_nu["Nov"].median())
df_clyde_nu["Dec"] = df_clyde_nu["Dec"].replace(-9999.9, df_clyde_nu["Dec"].median())
df_clyde_nu["Annual"] = df_clyde_nu["Annual"].replace(-9999.9, df_clyde_nu["Annual"].median())
df_clyde_nu["Winter"] = df_clyde_nu["Winter"].replace(-9999.9, df_clyde_nu["Winter"].median())
df_clyde_nu["Spring"] = df_clyde_nu["Spring"].replace(-9999.9, df_clyde_nu["Spring"].median())
df_clyde_nu["Summer"] = df_clyde_nu["Summer"].replace(-9999.9, df_clyde_nu["Summer"].median())
df_clyde_nu["Autumn"] = df_clyde_nu["Autumn"].replace(-9999.9, df_clyde_nu["Autumn"].median())

x1 = df_clyde_nu["Year"]
y1 = df_clyde_nu["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_clyde_nu["Year"]
y2 = df_clyde_nu["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_clyde_nu["Year"]
y3 = df_clyde_nu["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_clyde_nu["Year"]
y4 = df_clyde_nu["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Clyde Nunavut")
plt.legend()
plt.show()

#Coral Harbour Nunavut 

coralharbour_nu = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/coralharbour_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding= 'utf-8-sig')
df_coralharbour_nu = pd.DataFrame(coralharbour_nu)

df_coralharbour_nu["Oct"] = df_coralharbour_nu["Oct"].replace(-9999.9, df_coralharbour_nu["Oct"].median())
df_coralharbour_nu["Nov"] = df_coralharbour_nu["Nov"].replace(-9999.9, df_coralharbour_nu["Nov"].median())
df_coralharbour_nu["Autumn"] = df_coralharbour_nu["Autumn"].replace(-9999.9, df_coralharbour_nu["Autumn"].median())

x1 = df_coralharbour_nu["Year"]
y1 = df_coralharbour_nu["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_coralharbour_nu["Year"]
y2 = df_coralharbour_nu["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_coralharbour_nu["Year"]
y3 = df_coralharbour_nu["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_coralharbour_nu["Year"]
y4 = df_coralharbour_nu["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Coralharbour Nunavut")
plt.legend()
plt.show()

#Dewarlakes Nunuvut 

dewarlakes_nu = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/dewarlakes_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_dewarlakes_nu = pd.DataFrame(dewarlakes_nu)

df_dewarlakes_nu["Jan"] = df_dewarlakes_nu["Jan"].replace(-9999.9, df_dewarlakes_nu["Jan"].median())
df_dewarlakes_nu["Feb"] = df_dewarlakes_nu["Feb"].replace(-9999.9, df_dewarlakes_nu["Feb"].median())
df_dewarlakes_nu["Mar"] = df_dewarlakes_nu["Mar"].replace(-9999.9, df_dewarlakes_nu["Mar"].median())
df_dewarlakes_nu["Apr"] = df_dewarlakes_nu["Apr"].replace(-9999.9, df_dewarlakes_nu["Apr"].median())
df_dewarlakes_nu["May"] = df_dewarlakes_nu["May"].replace(-9999.9, df_dewarlakes_nu["May"].median())
df_dewarlakes_nu["Jun"] = df_dewarlakes_nu["Jun"].replace(-9999.9, df_dewarlakes_nu["Jun"].median())
df_dewarlakes_nu["Jul"] = df_dewarlakes_nu["Jul"].replace(-9999.9, df_dewarlakes_nu["Jul"].median())
df_dewarlakes_nu["Aug"] = df_dewarlakes_nu["Aug"].replace(-9999.9, df_dewarlakes_nu["Aug"].median())
df_dewarlakes_nu["Sep"] = df_dewarlakes_nu["Sep"].replace(-9999.9, df_dewarlakes_nu["Sep"].median())
df_dewarlakes_nu["Oct"] = df_dewarlakes_nu["Oct"].replace(-9999.9, df_dewarlakes_nu["Oct"].median())
df_dewarlakes_nu["Nov"] = df_dewarlakes_nu["Nov"].replace(-9999.9, df_dewarlakes_nu["Nov"].median())
df_dewarlakes_nu["Dec"] = df_dewarlakes_nu["Dec"].replace(-9999.9, df_dewarlakes_nu["Dec"].median())
df_dewarlakes_nu["Annual"] = df_dewarlakes_nu["Annual"].replace(-9999.9, df_dewarlakes_nu["Annual"].median())
df_dewarlakes_nu["Winter"] = df_dewarlakes_nu["Winter"].replace(-9999.9, df_dewarlakes_nu["Winter"].median())
df_dewarlakes_nu["Spring"] = df_dewarlakes_nu["Spring"].replace(-9999.9, df_dewarlakes_nu["Spring"].median())
df_dewarlakes_nu["Summer"] = df_dewarlakes_nu["Summer"].replace(-9999.9, df_dewarlakes_nu["Summer"].median())
df_dewarlakes_nu["Autumn"] = df_dewarlakes_nu["Autumn"].replace(-9999.9, df_dewarlakes_nu["Autumn"].median())
 
x1 = df_dewarlakes_nu["Year"]
y1 = df_dewarlakes_nu["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_dewarlakes_nu["Year"]
y2 = df_dewarlakes_nu["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_dewarlakes_nu["Year"]
y3 = df_dewarlakes_nu["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_dewarlakes_nu["Year"]
y4 = df_dewarlakes_nu["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Dewarlakes Nunavut")
plt.legend()
plt.show()

#Eureka Nunavut 
    
eureka_nu= pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/eureka_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_eureka_nu = pd.DataFrame(eureka_nu)

df_eureka_nu["Jun"] = df_eureka_nu["Jun"].replace(-9999.9, df_eureka_nu["Jun"].median())
df_eureka_nu["Jul"] = df_eureka_nu["Jul"].replace(-9999.9, df_eureka_nu["Jul"].median())
df_eureka_nu["Summer"] = df_eureka_nu["Summer"].replace(-9999.9, df_eureka_nu["Summer"].median())

x1 = df_eureka_nu["Year"]
y1 = df_eureka_nu["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_eureka_nu["Year"]
y2 = df_eureka_nu["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_eureka_nu["Year"]
y3 = df_eureka_nu["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_eureka_nu["Year"]
y4 = df_eureka_nu["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Eureka Nunavut")
plt.legend()
plt.show()

#Foxfive Nunuvut 

foxfive_nu = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/foxfive_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_foxfive_nu = pd.DataFrame(foxfive_nu)

df_foxfive_nu["Jan"] = df_foxfive_nu["Jan"].replace(-9999.9, df_foxfive_nu["Jan"].median())
df_foxfive_nu["Feb"] = df_foxfive_nu["Feb"].replace(-9999.9, df_foxfive_nu["Feb"].median())
df_foxfive_nu["Mar"] = df_foxfive_nu["Mar"].replace(-9999.9, df_foxfive_nu["Mar"].median())
df_foxfive_nu["Apr"] = df_foxfive_nu["Apr"].replace(-9999.9, df_foxfive_nu["Apr"].median())
df_foxfive_nu["May"] = df_foxfive_nu["May"].replace(-9999.9, df_foxfive_nu["May"].median())
df_foxfive_nu["Jun"] = df_foxfive_nu["Jun"].replace(-9999.9, df_foxfive_nu["Jun"].median())
df_foxfive_nu["Jul"] = df_foxfive_nu["Jul"].replace(-9999.9, df_foxfive_nu["Jul"].median())
df_foxfive_nu["Aug"] = df_foxfive_nu["Aug"].replace(-9999.9, df_foxfive_nu["Aug"].median())
df_foxfive_nu["Sep"] = df_foxfive_nu["Sep"].replace(-9999.9, df_foxfive_nu["Sep"].median())
df_foxfive_nu["Oct"] = df_foxfive_nu["Oct"].replace(-9999.9, df_foxfive_nu["Oct"].median())
df_foxfive_nu["Nov"] = df_foxfive_nu["Nov"].replace(-9999.9, df_foxfive_nu["Nov"].median())
df_foxfive_nu["Dec"] = df_foxfive_nu["Dec"].replace(-9999.9, df_foxfive_nu["Dec"].median())
df_foxfive_nu["Annual"] = df_foxfive_nu["Annual"].replace(-9999.9, df_foxfive_nu["Annual"].median())
df_foxfive_nu["Winter"] = df_foxfive_nu["Winter"].replace(-9999.9, df_foxfive_nu["Winter"].median())
df_foxfive_nu["Spring"] = df_foxfive_nu["Spring"].replace(-9999.9, df_foxfive_nu["Spring"].median())
df_foxfive_nu["Summer"] = df_foxfive_nu["Summer"].replace(-9999.9, df_foxfive_nu["Summer"].median())
df_foxfive_nu["Autumn"] = df_foxfive_nu["Autumn"].replace(-9999.9, df_foxfive_nu["Autumn"].median())

x1 = df_foxfive_nu["Year"]
y1 = df_foxfive_nu["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_foxfive_nu["Year"]
y2 = df_foxfive_nu["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_foxfive_nu["Year"]
y3 = df_foxfive_nu["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_foxfive_nu["Year"]
y4 = df_foxfive_nu["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Foxfive Nunavut")
plt.legend()
plt.show()

#Hallbeach Nunuvut 

hallbeach_nu = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/hallbeach_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_hallbeach_nu = pd.DataFrame(hallbeach_nu)

df_hallbeach_nu["Jan"] = df_hallbeach_nu["Jan"].replace(-9999.9, df_hallbeach_nu["Jan"].median())
df_hallbeach_nu["Feb"] = df_hallbeach_nu["Feb"].replace(-9999.9, df_hallbeach_nu["Feb"].median())
df_hallbeach_nu["Mar"] = df_hallbeach_nu["Mar"].replace(-9999.9, df_hallbeach_nu["Mar"].median())
df_hallbeach_nu["Apr"] = df_hallbeach_nu["Apr"].replace(-9999.9, df_hallbeach_nu["Apr"].median())
df_hallbeach_nu["May"] = df_hallbeach_nu["May"].replace(-9999.9, df_hallbeach_nu["May"].median())
df_hallbeach_nu["Jun"] = df_hallbeach_nu["Jun"].replace(-9999.9, df_hallbeach_nu["Jun"].median())
df_hallbeach_nu["Jul"] = df_hallbeach_nu["Jul"].replace(-9999.9, df_hallbeach_nu["Jul"].median())
df_hallbeach_nu["Aug"] = df_hallbeach_nu["Aug"].replace(-9999.9, df_hallbeach_nu["Aug"].median())
df_hallbeach_nu["Sep"] = df_hallbeach_nu["Sep"].replace(-9999.9, df_hallbeach_nu["Sep"].median())
df_hallbeach_nu["Oct"] = df_hallbeach_nu["Oct"].replace(-9999.9, df_hallbeach_nu["Oct"].median())
df_hallbeach_nu["Nov"] = df_hallbeach_nu["Nov"].replace(-9999.9, df_hallbeach_nu["Nov"].median())
df_hallbeach_nu["Dec"] = df_hallbeach_nu["Dec"].replace(-9999.9, df_hallbeach_nu["Dec"].median())
df_hallbeach_nu["Annual"] = df_hallbeach_nu["Annual"].replace(-9999.9, df_hallbeach_nu["Annual"].median())
df_hallbeach_nu["Winter"] = df_hallbeach_nu["Winter"].replace(-9999.9, df_hallbeach_nu["Winter"].median())
df_hallbeach_nu["Spring"] = df_hallbeach_nu["Spring"].replace(-9999.9, df_hallbeach_nu["Spring"].median())
df_hallbeach_nu["Summer"] = df_hallbeach_nu["Summer"].replace(-9999.9, df_hallbeach_nu["Summer"].median())
df_hallbeach_nu["Autumn"] = df_hallbeach_nu["Autumn"].replace(-9999.9, df_hallbeach_nu["Autumn"].median())

x1 = df_hallbeach_nu["Year"]
y1 = df_hallbeach_nu["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_hallbeach_nu["Year"]
y2 = df_hallbeach_nu["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_hallbeach_nu["Year"]
y3 = df_hallbeach_nu["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_hallbeach_nu["Year"]
y4 = df_hallbeach_nu["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Hallbeach Nunavut")
plt.legend()
plt.show()

#Iqualuit Nunuvut 

iqualuit_nu = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/iqaluit_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_iqualuit_nu = pd.DataFrame(iqualuit_nu)


df_iqualuit_nu["Feb"] = df_iqualuit_nu["Feb"].replace(-9999.9, df_iqualuit_nu["Feb"].median())
df_iqualuit_nu["Mar"] = df_iqualuit_nu["Mar"].replace(-9999.9, df_iqualuit_nu["Mar"].median())
df_iqualuit_nu["Apr"] = df_iqualuit_nu["Apr"].replace(-9999.9, df_iqualuit_nu["Apr"].median())
df_iqualuit_nu["May"] = df_iqualuit_nu["May"].replace(-9999.9, df_iqualuit_nu["May"].median())
df_iqualuit_nu["Jun"] = df_iqualuit_nu["Jun"].replace(-9999.9, df_iqualuit_nu["Jun"].median())
df_iqualuit_nu["Jul"] = df_iqualuit_nu["Jul"].replace(-9999.9, df_iqualuit_nu["Jul"].median())
df_iqualuit_nu["Aug"] = df_iqualuit_nu["Aug"].replace(-9999.9, df_iqualuit_nu["Aug"].median())
df_iqualuit_nu["Sep"] = df_iqualuit_nu["Sep"].replace(-9999.9, df_iqualuit_nu["Sep"].median())
df_iqualuit_nu["Oct"] = df_iqualuit_nu["Oct"].replace(-9999.9, df_iqualuit_nu["Oct"].median())
df_iqualuit_nu["Nov"] = df_iqualuit_nu["Nov"].replace(-9999.9, df_iqualuit_nu["Nov"].median())
df_iqualuit_nu["Dec"] = df_iqualuit_nu["Dec"].replace(-9999.9, df_iqualuit_nu["Dec"].median())
df_iqualuit_nu["Annual"] = df_iqualuit_nu["Annual"].replace(-9999.9, df_iqualuit_nu["Annual"].median())
df_iqualuit_nu["Spring"] = df_iqualuit_nu["Spring"].replace(-9999.9, df_iqualuit_nu["Spring"].median())
df_iqualuit_nu["Summer"] = df_iqualuit_nu["Summer"].replace(-9999.9, df_iqualuit_nu["Summer"].median())
df_iqualuit_nu["Autumn"] = df_iqualuit_nu["Autumn"].replace(-9999.9, df_iqualuit_nu["Autumn"].median())

x1 = df_iqualuit_nu["Year"]
y1 = df_iqualuit_nu["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_iqualuit_nu["Year"]
y2 = df_iqualuit_nu["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_iqualuit_nu["Year"]
y3 = df_iqualuit_nu["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_iqualuit_nu["Year"]
y4 = df_iqualuit_nu["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Iqualuit Nunavut")
plt.legend()
plt.show()

#Longstaff Bluff Nunuvut 

longstaffbluff_nu = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/longstaffbluff_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_longstaffbluff_nu = pd.DataFrame(longstaffbluff_nu)

df_longstaffbluff_nu["Jan"] = df_longstaffbluff_nu["Jan"].replace(-9999.9, df_longstaffbluff_nu["Jan"].median())
df_longstaffbluff_nu["Feb"] = df_longstaffbluff_nu["Feb"].replace(-9999.9, df_longstaffbluff_nu["Feb"].median())
df_longstaffbluff_nu["Mar"] = df_longstaffbluff_nu["Mar"].replace(-9999.9, df_longstaffbluff_nu["Mar"].median())
df_longstaffbluff_nu["Apr"] = df_longstaffbluff_nu["Apr"].replace(-9999.9, df_longstaffbluff_nu["Apr"].median())
df_longstaffbluff_nu["May"] = df_longstaffbluff_nu["May"].replace(-9999.9, df_longstaffbluff_nu["May"].median())
df_longstaffbluff_nu["Jun"] = df_longstaffbluff_nu["Jun"].replace(-9999.9, df_longstaffbluff_nu["Jun"].median())
df_longstaffbluff_nu["Jul"] = df_longstaffbluff_nu["Jul"].replace(-9999.9, df_longstaffbluff_nu["Jul"].median())
df_longstaffbluff_nu["Aug"] = df_longstaffbluff_nu["Aug"].replace(-9999.9, df_longstaffbluff_nu["Aug"].median())
df_longstaffbluff_nu["Sep"] = df_longstaffbluff_nu["Sep"].replace(-9999.9, df_longstaffbluff_nu["Sep"].median())
df_longstaffbluff_nu["Oct"] = df_longstaffbluff_nu["Oct"].replace(-9999.9, df_longstaffbluff_nu["Oct"].median())
df_longstaffbluff_nu["Nov"] = df_longstaffbluff_nu["Nov"].replace(-9999.9, df_longstaffbluff_nu["Nov"].median())
df_longstaffbluff_nu["Dec"] = df_longstaffbluff_nu["Dec"].replace(-9999.9, df_longstaffbluff_nu["Dec"].median())
df_longstaffbluff_nu["Annual"] = df_longstaffbluff_nu["Annual"].replace(-9999.9, df_longstaffbluff_nu["Annual"].median())
df_longstaffbluff_nu["Winter"] = df_longstaffbluff_nu["Winter"].replace(-9999.9, df_longstaffbluff_nu["Winter"].median())
df_longstaffbluff_nu["Spring"] = df_longstaffbluff_nu["Spring"].replace(-9999.9, df_longstaffbluff_nu["Spring"].median())
df_longstaffbluff_nu["Summer"] = df_longstaffbluff_nu["Summer"].replace(-9999.9, df_longstaffbluff_nu["Summer"].median())
df_longstaffbluff_nu["Autumn"] = df_longstaffbluff_nu["Autumn"].replace(-9999.9, df_longstaffbluff_nu["Autumn"].median())

x1 = df_longstaffbluff_nu["Year"]
y1 = df_longstaffbluff_nu["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_longstaffbluff_nu["Year"]
y2 = df_longstaffbluff_nu["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_longstaffbluff_nu["Year"]
y3 = df_longstaffbluff_nu["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_longstaffbluff_nu["Year"]
y4 = df_longstaffbluff_nu["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Longstaffbluff Nunavut")
plt.legend()
plt.show()

#Resolutecars Nunuvut

resolutecars_nu = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/resolutecars_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_resolutecars_nu = pd.DataFrame(resolutecars_nu)

df_resolutecars_nu["Nov"] = df_resolutecars_nu["Nov"].replace(-9999.9, df_resolutecars_nu["Nov"].median())
df_resolutecars_nu["Dec"] = df_resolutecars_nu["Dec"].replace(-9999.9, df_resolutecars_nu["Dec"].median())

x1 = df_resolutecars_nu["Year"]
y1 = df_resolutecars_nu["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_resolutecars_nu["Year"]
y2 = df_resolutecars_nu["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_resolutecars_nu["Year"]
y3 = df_resolutecars_nu["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_resolutecars_nu["Year"]
y4 = df_resolutecars_nu["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Resolute Nunavut")
plt.legend()
plt.show()
              

