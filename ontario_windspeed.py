#!/usr/bin/env python3

import pandas as pd 
from matplotlib import pyplot as plt


#Armstrong Ontario
armstrong_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/alert_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_armstrong_ont = pd.DataFrame(armstrong_ont)

df_armstrong_ont = pd.DataFrame(abottsfordbc)
df_armstrong_ont["Jan"] = df_armstrong_ont["Jan"].replace(-9999.9, df_armstrong_ont["Jan"].median())
df_armstrong_ont["Feb"] = df_armstrong_ont["Feb"].replace(-9999.9, df_armstrong_ont["Feb"].median())
df_armstrong_ont["Mar"] = df_armstrong_ont["Mar"].replace(-9999.9, df_armstrong_ont["Mar"].median())
df_armstrong_ont["Apr"] = df_armstrong_ont["Apr"].replace(-9999.9, df_armstrong_ont["Apr"].median())
df_armstrong_ont["May"] = df_armstrong_ont["May"].replace(-9999.9, df_armstrong_ont["May"].median())
df_armstrong_ont["Jun"] = df_armstrong_ont["Jun"].replace(-9999.9, df_armstrong_ont["Jun"].median())
df_armstrong_ont["Jul"] = df_armstrong_ont["Jul"].replace(-9999.9, df_armstrong_ont["Jul"].median())
df_armstrong_ont["Aug"] = df_armstrong_ont["Aug"].replace(-9999.9, df_armstrong_ont["Aug"].median())
df_armstrong_ont["Sep"] = df_armstrong_ont["Sep"].replace(-9999.9, df_armstrong_ont["Sep"].median())
df_armstrong_ont["Oct"] = df_armstrong_ont["Oct"].replace(-9999.9, df_armstrong_ont["Oct"].median())
df_armstrong_ont["Nov"] = df_armstrong_ont["Nov"].replace(-9999.9, df_armstrong_ont["Nov"].median())
df_armstrong_ont["Dec"] = df_armstrong_ont["Dec"].replace(-9999.9, df_armstrong_ont["Dec"].median())
df_armstrong_ont["Annual"] = df_armstrong_ont["Annual"].replace(-9999.9, df_armstrong_ont["Annual"].median())
df_armstrong_ont["Winter"] = df_armstrong_ont["Winter"].replace(-9999.9, df_armstrong_ont["Winter"].median())
df_armstrong_ont["Spring"] = df_armstrong_ont["Spring"].replace(-9999.9, df_armstrong_ont["Spring"].median())
df_armstrong_ont["Summer"] = df_armstrong_ont["Summer"].replace(-9999.9, df_armstrong_ont["Summer"].median())
df_armstrong_ont["Autumn"] = df_armstrong_ont["Autumn"].replace(-9999.9, df_armstrong_ont["Autumn"].median())

x1 = df_armstrong_ont["Year"]
y1 = df_armstrong_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_armstrong_ont["Year"]
y2 = df_armstrong_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_armstrong_ont["Year"]
y3 = df_armstrong_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_armstrong_ont["Year"]
y4 = df_armstrong_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Armstrong Ontario")
plt.legend()
plt.show()

#Earlton Ontario 

earlton_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/earlton_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_earlton_ont = pd.DataFrame(earlton_ont)

df_earlton_ont["Feb"] = df_earlton_ont["Feb"].replace(-9999.9, df_earlton_ont["Feb"].median())
df_earlton_ont["Jul"] = df_earlton_ont["Jul"].replace(-9999.9, df_earlton_ont["Jul"].median())

x1 = df_earlton_ont["Year"]
y1 = df_earlton_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_earlton_ont["Year"]
y2 = df_earlton_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_earlton_ont["Year"]
y3 = df_earlton_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_earlton_ont["Year"]
y4 = df_earlton_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Earlton Ontario")
plt.legend()
plt.show()

#Gorebay Ontario 

gorebay_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/gorebay_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_gorebay_ont = pd.DataFrame(gorebay_ont)

df_gorebay_ont["Jan"] = df_gorebay_ont["Jan"].replace(-9999.9, df_gorebay_ont["Jan"].median())
df_gorebay_ont["Feb"] = df_gorebay_ont["Feb"].replace(-9999.9, df_gorebay_ont["Feb"].median())
df_gorebay_ont["Mar"] = df_gorebay_ont["Mar"].replace(-9999.9, df_gorebay_ont["Mar"].median())
df_gorebay_ont["Apr"] = df_gorebay_ont["Apr"].replace(-9999.9, df_gorebay_ont["Apr"].median())
df_gorebay_ont["May"] = df_gorebay_ont["May"].replace(-9999.9, df_gorebay_ont["May"].median())
df_gorebay_ont["Jun"] = df_gorebay_ont["Jun"].replace(-9999.9, df_gorebay_ont["Jun"].median())
df_gorebay_ont["Jul"] = df_gorebay_ont["Jul"].replace(-9999.9, df_gorebay_ont["Jul"].median())
df_gorebay_ont["Aug"] = df_gorebay_ont["Aug"].replace(-9999.9, df_gorebay_ont["Aug"].median())
df_gorebay_ont["Sep"] = df_gorebay_ont["Sep"].replace(-9999.9, df_gorebay_ont["Sep"].median())
df_gorebay_ont["Oct"] = df_gorebay_ont["Oct"].replace(-9999.9, df_gorebay_ont["Oct"].median())
df_gorebay_ont["Nov"] = df_gorebay_ont["Nov"].replace(-9999.9, df_gorebay_ont["Nov"].median())
df_gorebay_ont["Dec"] = df_gorebay_ont["Dec"].replace(-9999.9, df_gorebay_ont["Dec"].median())
df_gorebay_ont["Annual"] = df_gorebay_ont["Annual"].replace(-9999.9, df_gorebay_ont["Annual"].median())
df_gorebay_ont["Winter"] = df_gorebay_ont["Winter"].replace(-9999.9, df_gorebay_ont["Winter"].median())
df_gorebay_ont["Spring"] = df_gorebay_ont["Spring"].replace(-9999.9, df_gorebay_ont["Spring"].median())
df_gorebay_ont["Summer"] = df_gorebay_ont["Summer"].replace(-9999.9, df_gorebay_ont["Summer"].median())
df_gorebay_ont["Autumn"] = df_gorebay_ont["Autumn"].replace(-9999.9, df_gorebay_ont["Autumn"].median())

x1 = df_gorebay_ont["Year"]
y1 = df_gorebay_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_gorebay_ont["Year"]
y2 = df_gorebay_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_gorebay_ont["Year"]
y3 = df_gorebay_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_gorebay_ont["Year"]
y4 = df_gorebay_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Goorebay Ontario")
plt.legend()
plt.show()

hamilton_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/hamilton_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_hamilton_ont = pd.DataFrame(hamilton_ont)

df_hamilton_ont["Jan"] = df_hamilton_ont["Jan"].replace(-9999.9, df_hamilton_ont["Jan"].median())
df_hamilton_ont["Feb"] = df_hamilton_ont["Feb"].replace(-9999.9, df_hamilton_ont["Feb"].median())
df_hamilton_ont["Mar"] = df_hamilton_ont["Mar"].replace(-9999.9, df_hamilton_ont["Mar"].median())
df_hamilton_ont["Apr"] = df_hamilton_ont["Apr"].replace(-9999.9, df_hamilton_ont["Apr"].median())
df_hamilton_ont["May"] = df_hamilton_ont["May"].replace(-9999.9, df_hamilton_ont["May"].median())
df_hamilton_ont["Jun"] = df_hamilton_ont["Jun"].replace(-9999.9, df_hamilton_ont["Jun"].median())
df_hamilton_ont["Jul"] = df_hamilton_ont["Jul"].replace(-9999.9, df_hamilton_ont["Jul"].median())
df_hamilton_ont["Aug"] = df_hamilton_ont["Aug"].replace(-9999.9, df_hamilton_ont["Aug"].median())
df_hamilton_ont["Sep"] = df_hamilton_ont["Sep"].replace(-9999.9, df_hamilton_ont["Sep"].median())
df_hamilton_ont["Oct"] = df_hamilton_ont["Oct"].replace(-9999.9, df_hamilton_ont["Oct"].median())
df_hamilton_ont["Nov"] = df_hamilton_ont["Nov"].replace(-9999.9, df_hamilton_ont["Nov"].median())
df_hamilton_ont["Dec"] = df_hamilton_ont["Dec"].replace(-9999.9, df_hamilton_ont["Dec"].median())
df_hamilton_ont["Annual"] = df_hamilton_ont["Annual"].replace(-9999.9, df_hamilton_ont["Annual"].median())
df_hamilton_ont["Winter"] = df_hamilton_ont["Winter"].replace(-9999.9, df_hamilton_ont["Winter"].median())
df_hamilton_ont["Spring"] = df_hamilton_ont["Spring"].replace(-9999.9, df_hamilton_ont["Spring"].median())
df_hamilton_ont["Summer"] = df_hamilton_ont["Summer"].replace(-9999.9, df_hamilton_ont["Summer"].median())
df_hamilton_ont["Autumn"] = df_hamilton_ont["Autumn"].replace(-9999.9, df_hamilton_ont["Autumn"].median())

x1 = df_hamilton_ont["Year"]
y1 = df_hamilton_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_hamilton_ont["Year"]
y2 = df_hamilton_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_hamilton_ont["Year"]
y3 = df_hamilton_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_hamilton_ont["Year"]
y4 = df_hamilton_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Hamilton Ontario")
plt.legend()
plt.show()

#Kapuskaking Ontario 

kapuskaking_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/kapuskaking_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_kapuskaking_ont = pd.DataFrame(kapuskaking_ont)

df_kapuskaking_ont["Sep"] = df_kapuskaking_ont["Sep"].replace(-9999.9, df_kapuskaking_ont["Sep"].median())
df_kapuskaking_ont["Oct"] = df_kapuskaking_ont["Oct"].replace(-9999.9, df_kapuskaking_ont["Oct"].median())
df_kapuskaking_ont["Nov"] = df_kapuskaking_ont["Nov"].replace(-9999.9, df_kapuskaking_ont["Nov"].median())
df_kapuskaking_ont["Dec"] = df_kapuskaking_ont["Dec"].replace(-9999.9, df_kapuskaking_ont["Dec"].median())
df_kapuskaking_ont["Autumn"] = df_kapuskaking_ont["Autumn"].replace(-9999.9, df_kapuskaking_ont["Autumn"].median())

x1 = df_kapuskaking_ont["Year"]
y1 = df_kapuskaking_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_kapuskaking_ont["Year"]
y2 = df_kapuskaking_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_kapuskaking_ont["Year"]
y3 = df_kapuskaking_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_kapuskaking_ont["Year"]
y4 = df_kapuskaking_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Kampuskaking Ontario")
plt.legend()
plt.show()

#Kenora Ontario

kenora_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/kenora_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_kenora_ont = pd.DataFrame(kenora_ont)

df_kenora_ont["Oct"] = df_kenora_ont["Oct"].replace(-9999.9, df_kenora_ont["Oct"].median())

x1 = df_kenora_ont["Year"]
y1 = df_kenora_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_kenora_ont["Year"]
y2 = df_kenora_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_kenora_ont["Year"]
y3 = df_kenora_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_kenora_ont["Year"]
y4 = df_kenora_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Kenora Ontario")
plt.legend()
plt.show()

#Kingston Ontario 

kingston_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/kingston_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_kingston_ont = pd.DataFrame(kingston_ont)

df_kingston_ont["Jan"] = df_kingston_ont["Jan"].replace(-9999.9, df_kingston_ont["Jan"].median())
df_kingston_ont["Feb"] = df_kingston_ont["Feb"].replace(-9999.9, df_kingston_ont["Feb"].median())
df_kingston_ont["Mar"] = df_kingston_ont["Mar"].replace(-9999.9, df_kingston_ont["Mar"].median())
df_kingston_ont["Apr"] = df_kingston_ont["Apr"].replace(-9999.9, df_kingston_ont["Apr"].median())
df_kingston_ont["May"] = df_kingston_ont["May"].replace(-9999.9, df_kingston_ont["May"].median())
df_kingston_ont["Jun"] = df_kingston_ont["Jun"].replace(-9999.9, df_kingston_ont["Jun"].median())
df_kingston_ont["Jul"] = df_kingston_ont["Jul"].replace(-9999.9, df_kingston_ont["Jul"].median())
df_kingston_ont["Aug"] = df_kingston_ont["Aug"].replace(-9999.9, df_kingston_ont["Aug"].median())
df_kingston_ont["Sep"] = df_kingston_ont["Sep"].replace(-9999.9, df_kingston_ont["Sep"].median())
df_kingston_ont["Oct"] = df_kingston_ont["Oct"].replace(-9999.9, df_kingston_ont["Oct"].median())
df_kingston_ont["Nov"] = df_kingston_ont["Nov"].replace(-9999.9, df_kingston_ont["Nov"].median())
df_kingston_ont["Dec"] = df_kingston_ont["Dec"].replace(-9999.9, df_kingston_ont["Dec"].median())
df_kingston_ont["Annual"] = df_kingston_ont["Annual"].replace(-9999.9, df_kingston_ont["Annual"].median())
df_kingston_ont["Winter"] = df_kingston_ont["Winter"].replace(-9999.9, df_kingston_ont["Winter"].median())
df_kingston_ont["Spring"] = df_kingston_ont["Spring"].replace(-9999.9, df_kingston_ont["Spring"].median())
df_kingston_ont["Summer"] = df_kingston_ont["Summer"].replace(-9999.9, df_kingston_ont["Summer"].median())
df_kingston_ont["Autumn"] = df_kingston_ont["Autumn"].replace(-9999.9, df_kingston_ont["Autumn"].median())

x1 = df_kingston_ont["Year"]
y1 = df_kingston_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_kingston_ont["Year"]
y2 = df_kingston_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_kingston_ont["Year"]
y3 = df_kingston_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_kingston_ont["Year"]
y4 = df_kingston_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Kingston Ontario")
plt.legend()
plt.show()


#London Ontario

london_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/london_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_london_ont = pd.DataFrame(london_ont)

x1 = df_london_ont["Year"]
y1 = df_london_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_london_ont["Year"]
y2 = df_london_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_london_ont["Year"]
y3 = df_london_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_london_ont["Year"]
y4 = df_london_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("London Ontario")
plt.legend()
plt.show()

#Mossonee Ontario 

mossonee_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/mossonee_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_mossonee_ont = pd.DataFrame(mossonee_ont)

df_mossonee_ont["Jan"] = df_mossonee_ont["Jan"].replace(-9999.9, df_mossonee_ont["Jan"].median())
df_mossonee_ont["Feb"] = df_mossonee_ont["Feb"].replace(-9999.9, df_mossonee_ont["Feb"].median())
df_mossonee_ont["Mar"] = df_mossonee_ont["Mar"].replace(-9999.9, df_mossonee_ont["Mar"].median())
df_mossonee_ont["Apr"] = df_mossonee_ont["Apr"].replace(-9999.9, df_mossonee_ont["Apr"].median())
df_mossonee_ont["May"] = df_mossonee_ont["May"].replace(-9999.9, df_mossonee_ont["May"].median())
df_mossonee_ont["Jun"] = df_mossonee_ont["Jun"].replace(-9999.9, df_mossonee_ont["Jun"].median())
df_mossonee_ont["Jul"] = df_mossonee_ont["Jul"].replace(-9999.9, df_mossonee_ont["Jul"].median())
df_mossonee_ont["Aug"] = df_mossonee_ont["Aug"].replace(-9999.9, df_mossonee_ont["Aug"].median())
df_mossonee_ont["Sep"] = df_mossonee_ont["Sep"].replace(-9999.9, df_mossonee_ont["Sep"].median())
df_mossonee_ont["Oct"] = df_mossonee_ont["Oct"].replace(-9999.9, df_mossonee_ont["Oct"].median())
df_mossonee_ont["Nov"] = df_mossonee_ont["Nov"].replace(-9999.9, df_mossonee_ont["Nov"].median())
df_mossonee_ont["Dec"] = df_mossonee_ont["Dec"].replace(-9999.9, df_mossonee_ont["Dec"].median())
df_mossonee_ont["Annual"] = df_mossonee_ont["Annual"].replace(-9999.9, df_mossonee_ont["Annual"].median())
df_mossonee_ont["Winter"] = df_mossonee_ont["Winter"].replace(-9999.9, df_mossonee_ont["Winter"].median())
df_mossonee_ont["Spring"] = df_mossonee_ont["Spring"].replace(-9999.9, df_mossonee_ont["Spring"].median())
df_mossonee_ont["Summer"] = df_mossonee_ont["Summer"].replace(-9999.9, df_mossonee_ont["Summer"].median())
df_mossonee_ont["Autumn"] = df_mossonee_ont["Autumn"].replace(-9999.9, df_mossonee_ont["Autumn"].median())

x1 = df_mossonee_ont["Year"]
y1 = df_mossonee_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_mossonee_ont["Year"]
y2 = df_mossonee_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_mossonee_ont["Year"]
y3 = df_mossonee_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_mossonee_ont["Year"]
y4 = df_mossonee_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Mossonee Ontario")
plt.legend()
plt.show()


#Muskoka Ontario

muskoka_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/muskoka_ont.csv",engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_muskoka_ont = pd.DataFrame(muskoka_ont)


df_muskoka_ont["Jul"] = df_muskoka_ont["Jul"].replace(-9999.9, df_muskoka_ont["Jul"].median())
df_muskoka_ont["Aug"] = df_muskoka_ont["Aug"].replace(-9999.9, df_muskoka_ont["Aug"].median())
df_muskoka_ont["Summer"] = df_muskoka_ont["Summer"].replace(-9999.9, df_muskoka_ont["Summer"].median())
df_muskoka_ont["Autumn"] = df_muskoka_ont["Autumn"].replace(-9999.9, df_muskoka_ont["Autumn"].median())
df_muskoka_ont["Oct"] = df_muskoka_ont["Oct"].replace(-9999.9, df_muskoka_ont["Oct"].median())
df_muskoka_ont["Nov"] = df_muskoka_ont["Nov"].replace(-9999.9, df_muskoka_ont["Nov"].median())

x1 = df_muskoka_ont["Year"]
y1 = df_muskoka_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_muskoka_ont["Year"]
y2 = df_muskoka_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_muskoka_ont["Year"]
y3 = df_muskoka_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_muskoka_ont["Year"]
y4 = df_muskoka_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Mouskoka Ontario")
plt.legend()
plt.show()

#North Bay Ontario

northbay_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/northbay_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_northbay_ont = pd.DataFrame(northbay_ont)

x1 = df_northbay_ont["Year"]
y1 = df_northbay_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_northbay_ont["Year"]
y2 = df_northbay_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_northbay_ont["Year"]
y3 = df_northbay_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_northbay_ont["Year"]
y4 = df_northbay_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("North Bay Ontario")
plt.legend()
plt.show()

#Ottawa Ontario

ottawa_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/ottawa_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_ottawa_ont = pd.DataFrame(ottawa_ont)

x1 = df_ottawa_ont["Year"]
y1 = df_ottawa_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_ottawa_ont["Year"]
y2 = df_ottawa_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_ottawa_ont["Year"]
y3 = df_ottawa_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_ottawa_ont["Year"]
y4 = df_ottawa_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Ottawa Ontario")
plt.legend()
plt.show()

#Redlake Ontario

redlake_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/redlake_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_redlake_ont = pd.DataFrame(redlake_ont)

df_redlake_ont["Jan"] = df_redlake_ont["Jan"].replace(-9999.9, df_redlake_ont["Jan"].median())
df_redlake_ont["Feb"] = df_redlake_ont["Feb"].replace(-9999.9, df_redlake_ont["Feb"].median())
df_redlake_ont["Mar"] = df_redlake_ont["Mar"].replace(-9999.9, df_redlake_ont["Mar"].median())
df_redlake_ont["Apr"] = df_redlake_ont["Apr"].replace(-9999.9, df_redlake_ont["Apr"].median())
df_redlake_ont["May"] = df_redlake_ont["May"].replace(-9999.9, df_redlake_ont["May"].median())
df_redlake_ont["Jun"] = df_redlake_ont["Jun"].replace(-9999.9, df_redlake_ont["Jun"].median())
df_redlake_ont["Jul"] = df_redlake_ont["Jul"].replace(-9999.9, df_redlake_ont["Jul"].median())
df_redlake_ont["Aug"] = df_redlake_ont["Aug"].replace(-9999.9, df_redlake_ont["Aug"].median())
df_redlake_ont["Sep"] = df_redlake_ont["Sep"].replace(-9999.9, df_redlake_ont["Sep"].median())
df_redlake_ont["Oct"] = df_redlake_ont["Oct"].replace(-9999.9, df_redlake_ont["Oct"].median())
df_redlake_ont["Nov"] = df_redlake_ont["Nov"].replace(-9999.9, df_redlake_ont["Nov"].median())
df_redlake_ont["Dec"] = df_redlake_ont["Dec"].replace(-9999.9, df_redlake_ont["Dec"].median())
df_redlake_ont["Annual"] = df_redlake_ont["Annual"].replace(-9999.9, df_redlake_ont["Annual"].median())
df_redlake_ont["Winter"] = df_redlake_ont["Winter"].replace(-9999.9, df_redlake_ont["Winter"].median())
df_redlake_ont["Spring"] = df_redlake_ont["Spring"].replace(-9999.9, df_redlake_ont["Spring"].median())
df_redlake_ont["Summer"] = df_redlake_ont["Summer"].replace(-9999.9, df_redlake_ont["Summer"].median())
df_redlake_ont["Autumn"] = df_redlake_ont["Autumn"].replace(-9999.9, df_redlake_ont["Autumn"].median())

x1 = df_redlake_ont["Year"]
y1 = df_redlake_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_redlake_ont["Year"]
y2 = df_redlake_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_redlake_ont["Year"]
y3 = df_redlake_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_redlake_ont["Year"]
y4 = df_redlake_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Redlake Ontario")
plt.legend()
plt.show()

#Saulstemarie Ontario

saulstemarie_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/saulstemarie_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_saulstemarie_ont  = pd.DataFrame(saulstemarie_ont)

df_saulstemarie_ont["Jan"] = df_saulstemarie_ont["Jan"].replace(-9999.9, df_saulstemarie_ont["Jan"].median())
df_saulstemarie_ont["Feb"] = df_saulstemarie_ont["Feb"].replace(-9999.9, df_saulstemarie_ont["Feb"].median())
df_saulstemarie_ont["Mar"] = df_saulstemarie_ont["Mar"].replace(-9999.9, df_saulstemarie_ont["Mar"].median())
df_saulstemarie_ont["Apr"] = df_saulstemarie_ont["Apr"].replace(-9999.9, df_saulstemarie_ont["Apr"].median())
df_saulstemarie_ont["May"] = df_saulstemarie_ont["May"].replace(-9999.9, df_saulstemarie_ont["May"].median())
df_saulstemarie_ont["Jun"] = df_saulstemarie_ont["Jun"].replace(-9999.9, df_saulstemarie_ont["Jun"].median())
df_saulstemarie_ont["Jul"] = df_saulstemarie_ont["Jul"].replace(-9999.9, df_saulstemarie_ont["Jul"].median())
df_saulstemarie_ont["Aug"] = df_saulstemarie_ont["Aug"].replace(-9999.9, df_saulstemarie_ont["Aug"].median())
df_saulstemarie_ont["Sep"] = df_saulstemarie_ont["Sep"].replace(-9999.9, df_saulstemarie_ont["Sep"].median())
df_saulstemarie_ont["Oct"] = df_saulstemarie_ont["Oct"].replace(-9999.9, df_saulstemarie_ont["Oct"].median())
df_saulstemarie_ont["Nov"] = df_saulstemarie_ont["Nov"].replace(-9999.9, df_saulstemarie_ont["Nov"].median())
df_saulstemarie_ont["Dec"] = df_saulstemarie_ont["Dec"].replace(-9999.9, df_saulstemarie_ont["Dec"].median())
df_saulstemarie_ont["Annual"] = df_saulstemarie_ont["Annual"].replace(-9999.9, df_saulstemarie_ont["Annual"].median())
df_saulstemarie_ont["Winter"] = df_saulstemarie_ont["Winter"].replace(-9999.9, df_saulstemarie_ont["Winter"].median())
df_saulstemarie_ont["Spring"] = df_saulstemarie_ont["Spring"].replace(-9999.9, df_saulstemarie_ont["Spring"].median())
df_saulstemarie_ont["Summer"] = df_saulstemarie_ont["Summer"].replace(-9999.9, df_saulstemarie_ont["Summer"].median())
df_saulstemarie_ont["Autumn"] = df_saulstemarie_ont["Autumn"].replace(-9999.9, df_saulstemarie_ont["Autumn"].median())


x1 = df_saulstemarie_ont["Year"]
y1 = df_saulstemarie_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_saulstemarie_ont["Year"]
y2 = df_saulstemarie_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_saulstemarie_ont["Year"]
y3 = df_saulstemarie_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_saulstemarie_ont["Year"]
y4 = df_saulstemarie_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Saul Ste. Marie")
plt.legend()
plt.show()

#Siouxlookout Ontario 

siouxlookout_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/siouxlookout_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_siouxlookout_ont = pd.DataFrame(siouxlookout_ont)

df_siouxlookout_ont["Oct"] = df_siouxlookout_ont["Oct"].replace(-9999.9, df_siouxlookout_ont["Oct"].median())
df_siouxlookout_ont["Nov"] = df_siouxlookout_ont["Nov"].replace(-9999.9, df_siouxlookout_ont["Nov"].median())
df_siouxlookout_ont["Autumn"] = df_siouxlookout_ont["Autumn"].replace(-9999.9, df_siouxlookout_ont["Autumn"].median())

x1 = df_siouxlookout_ont["Year"]
y1 = df_siouxlookout_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_siouxlookout_ont["Year"]
y2 = df_siouxlookout_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_siouxlookout_ont["Year"]
y3 = df_siouxlookout_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_siouxlookout_ont["Year"]
y4 = df_siouxlookout_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Siouxlookout Quebec")
plt.legend()
plt.show()

#Sudbury Ontario

sudbury_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/sudbury_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_sudbury_ont = pd.DataFrame(sudbury_ont)

df_sudbury_ont["Jan"] = df_sudbury_ont["Jan"].replace(-9999.9, df_sudbury_ont["Jan"].median())
df_sudbury_ont["Feb"] = df_sudbury_ont["Feb"].replace(-9999.9, df_sudbury_ont["Feb"].median())
df_sudbury_ont["Mar"] = df_sudbury_ont["Mar"].replace(-9999.9, df_sudbury_ont["Mar"].median())
df_sudbury_ont["Apr"] = df_sudbury_ont["Apr"].replace(-9999.9, df_sudbury_ont["Apr"].median())
df_sudbury_ont["May"] = df_sudbury_ont["May"].replace(-9999.9, df_sudbury_ont["May"].median())
df_sudbury_ont["Jun"] = df_sudbury_ont["Jun"].replace(-9999.9, df_sudbury_ont["Jun"].median())
df_sudbury_ont["Jul"] = df_sudbury_ont["Jul"].replace(-9999.9, df_sudbury_ont["Jul"].median())
df_sudbury_ont["Aug"] = df_sudbury_ont["Aug"].replace(-9999.9, df_sudbury_ont["Aug"].median())
df_sudbury_ont["Sep"] = df_sudbury_ont["Sep"].replace(-9999.9, df_sudbury_ont["Sep"].median())
df_sudbury_ont["Oct"] = df_sudbury_ont["Oct"].replace(-9999.9, df_sudbury_ont["Oct"].median())
df_sudbury_ont["Nov"] = df_sudbury_ont["Nov"].replace(-9999.9, df_sudbury_ont["Nov"].median())
df_sudbury_ont["Dec"] = df_sudbury_ont["Dec"].replace(-9999.9, df_sudbury_ont["Dec"].median())
df_sudbury_ont["Annual"] = df_sudbury_ont["Annual"].replace(-9999.9, df_sudbury_ont["Annual"].median())
df_sudbury_ont["Winter"] = df_sudbury_ont["Winter"].replace(-9999.9, df_sudbury_ont["Winter"].median())
df_sudbury_ont["Spring"] = df_sudbury_ont["Spring"].replace(-9999.9, df_sudbury_ont["Spring"].median())
df_sudbury_ont["Summer"] = df_sudbury_ont["Summer"].replace(-9999.9, df_sudbury_ont["Summer"].median())
df_sudbury_ont["Autumn"] = df_sudbury_ont["Autumn"].replace(-9999.9, df_sudbury_ont["Autumn"].median())

x1 = df_sudbury_ont["Year"]
y1 = df_sudbury_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_sudbury_ont["Year"]
y2 = df_sudbury_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_sudbury_ont["Year"]
y3 = df_sudbury_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_sudbury_ont["Year"]
y4 = df_sudbury_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Sudbury Ontario")
plt.legend()
plt.show()

#Thunderbay Ontario

thunderbay_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/thunderbay_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_thunderbay_ont = pd.DataFrame(thunderbay_ont)

x1 = df_thunderbay_ont["Year"]
y1 = df_thunderbay_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_thunderbay_ont["Year"]
y2 = df_thunderbay_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_thunderbay_ont["Year"]
y3 = df_thunderbay_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_thunderbay_ont["Year"]
y4 = df_thunderbay_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Thunderbay Ontario")
plt.legend()
plt.show()

#Timmins Victor Power 

timminsvictorpower_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/timminsvictorpower_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_timminsvictorpower_ont  = pd.DataFrame(timminsvictorpower_ont )

df_timminsvictorpower_ont["Jan"] = df_timminsvictorpower_ont["Jan"].replace(-9999.9, df_timminsvictorpower_ont["Jan"].median())
df_timminsvictorpower_ont["Feb"] = df_timminsvictorpower_ont["Feb"].replace(-9999.9, df_timminsvictorpower_ont["Feb"].median())
df_timminsvictorpower_ont["Mar"] = df_timminsvictorpower_ont["Mar"].replace(-9999.9, df_timminsvictorpower_ont["Mar"].median())
df_timminsvictorpower_ont["Apr"] = df_timminsvictorpower_ont["Apr"].replace(-9999.9, df_timminsvictorpower_ont["Apr"].median())
df_timminsvictorpower_ont["May"] = df_timminsvictorpower_ont["May"].replace(-9999.9, df_timminsvictorpower_ont["May"].median())
df_timminsvictorpower_ont["Jun"] = df_timminsvictorpower_ont["Jun"].replace(-9999.9, df_timminsvictorpower_ont["Jun"].median())
df_timminsvictorpower_ont["Jul"] = df_timminsvictorpower_ont["Jul"].replace(-9999.9, df_timminsvictorpower_ont["Jul"].median())
df_timminsvictorpower_ont["Aug"] = df_timminsvictorpower_ont["Aug"].replace(-9999.9, df_timminsvictorpower_ont["Aug"].median())
df_timminsvictorpower_ont["Sep"] = df_timminsvictorpower_ont["Sep"].replace(-9999.9, df_timminsvictorpower_ont["Sep"].median())
df_timminsvictorpower_ont["Oct"] = df_timminsvictorpower_ont["Oct"].replace(-9999.9, df_timminsvictorpower_ont["Oct"].median())
df_timminsvictorpower_ont["Nov"] = df_timminsvictorpower_ont["Nov"].replace(-9999.9, df_timminsvictorpower_ont["Nov"].median())
df_timminsvictorpower_ont["Dec"] = df_timminsvictorpower_ont["Dec"].replace(-9999.9, df_timminsvictorpower_ont["Dec"].median())
df_timminsvictorpower_ont["Annual"] = df_timminsvictorpower_ont["Annual"].replace(-9999.9, df_timminsvictorpower_ont["Annual"].median())
df_timminsvictorpower_ont["Winter"] = df_timminsvictorpower_ont["Winter"].replace(-9999.9, df_timminsvictorpower_ont["Winter"].median())
df_timminsvictorpower_ont["Spring"] = df_timminsvictorpower_ont["Spring"].replace(-9999.9, df_timminsvictorpower_ont["Spring"].median())
df_timminsvictorpower_ont["Summer"] = df_timminsvictorpower_ont["Summer"].replace(-9999.9, df_timminsvictorpower_ont["Summer"].median())
df_timminsvictorpower_ont["Autumn"] = df_timminsvictorpower_ont["Autumn"].replace(-9999.9, df_timminsvictorpower_ont["Autumn"].median())

x1 = df_timminsvictorpower_ont["Year"]
y1 = df_timminsvictorpower_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_timminsvictorpower_ont["Year"]
y2 = df_timminsvictorpower_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_timminsvictorpower_ont["Year"]
y3 = df_timminsvictorpower_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_timminsvictorpower_ont["Year"]
y4 = df_timminsvictorpower_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Timmins Victor M. Power Ontario")
plt.legend()
plt.show()

#Toronto Ontario STAND UP!!!!!

toronto_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/toronto_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_toronto_ont  = pd.DataFrame(toronto_ont)

x1 = df_toronto_ont["Year"]
y1 = df_toronto_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_toronto_ont["Year"]
y2 = df_toronto_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_toronto_ont["Year"]
y3 = df_toronto_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_toronto_ont["Year"]
y4 = df_toronto_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Toronto Ontario")
plt.legend()
plt.show()

#Torontoisland Ontario

torontoisland_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/torontoisland_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_torontoisland_ont  = pd.DataFrame(torontoisland_ont)


df_torontoisland_ont["Jan"] = df_torontoisland_ont["Jan"].replace(-9999.9, df_torontoisland_ont["Jan"].median())
df_torontoisland_ont["Feb"] = df_torontoisland_ont["Feb"].replace(-9999.9, df_torontoisland_ont["Feb"].median())
df_torontoisland_ont["Mar"] = df_torontoisland_ont["Mar"].replace(-9999.9, df_torontoisland_ont["Mar"].median())
df_torontoisland_ont["Apr"] = df_torontoisland_ont["Apr"].replace(-9999.9, df_torontoisland_ont["Apr"].median())
df_torontoisland_ont["May"] = df_torontoisland_ont["May"].replace(-9999.9, df_torontoisland_ont["May"].median())
df_torontoisland_ont["Jun"] = df_torontoisland_ont["Jun"].replace(-9999.9, df_torontoisland_ont["Jun"].median())
df_torontoisland_ont["Jul"] = df_torontoisland_ont["Jul"].replace(-9999.9, df_torontoisland_ont["Jul"].median())
df_torontoisland_ont["Aug"] = df_torontoisland_ont["Aug"].replace(-9999.9, df_torontoisland_ont["Aug"].median())
df_torontoisland_ont["Sep"] = df_torontoisland_ont["Sep"].replace(-9999.9, df_torontoisland_ont["Sep"].median())
df_torontoisland_ont["Oct"] = df_torontoisland_ont["Oct"].replace(-9999.9, df_torontoisland_ont["Oct"].median())
df_torontoisland_ont["Nov"] = df_torontoisland_ont["Nov"].replace(-9999.9, df_torontoisland_ont["Nov"].median())
df_torontoisland_ont["Dec"] = df_torontoisland_ont["Dec"].replace(-9999.9, df_torontoisland_ont["Dec"].median())
df_torontoisland_ont["Annual"] = df_torontoisland_ont["Annual"].replace(-9999.9, df_torontoisland_ont["Annual"].median())
df_torontoisland_ont["Winter"] = df_torontoisland_ont["Winter"].replace(-9999.9, df_torontoisland_ont["Winter"].median())
df_torontoisland_ont["Spring"] = df_torontoisland_ont["Spring"].replace(-9999.9, df_torontoisland_ont["Spring"].median())
df_torontoisland_ont["Summer"] = df_torontoisland_ont["Summer"].replace(-9999.9, df_torontoisland_ont["Summer"].median())
df_torontoisland_ont["Autumn"] = df_torontoisland_ont["Autumn"].replace(-9999.9, df_torontoisland_ont["Autumn"].median())

x1 = df_torontoisland_ont["Year"]
y1 = df_torontoisland_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_torontoisland_ont["Year"]
y2 = df_torontoisland_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_torontoisland_ont["Year"]
y3 = df_torontoisland_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_torontoisland_ont["Year"]
y4 = df_torontoisland_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Toronto Island Ontario")
plt.legend()
plt.show()

#Trenton Ontario

trenton_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/trenton_ont.csv", engine = 'python', sep=r'\s*,\s*',  encoding = 'utf-8-sig')
df_trenton_ont  = pd.DataFrame(trenton_ont)

x1 = df_trenton_ont["Year"]
y1 = df_trenton_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_trenton_ont["Year"]
y2 = df_trenton_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_trenton_ont["Year"]
y3 = df_trenton_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_trenton_ont["Year"]
y4 = df_trenton_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Trenton Ontario")
plt.legend()
plt.show()

#Wiarton Ontario

wiarton_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/wiarton_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_wiarton_ont = pd.DataFrame(wiarton_ont)

df_wiarton_ont["Oct"] = df_wiarton_ont["Oct"].replace(-9999.9, df_wiarton_ont["Oct"].median())
df_wiarton_ont["Nov"] = df_wiarton_ont["Nov"].replace(-9999.9, df_wiarton_ont["Nov"].median())
df_wiarton_ont["Dec"] = df_wiarton_ont["Dec"].replace(-9999.9, df_wiarton_ont["Dec"].median())
df_wiarton_ont["Autumn"] = df_wiarton_ont["Autumn"].replace(-9999.9, df_wiarton_ont["Autumn"].median())

x1 = df_wiarton_ont["Year"]
y1 = df_wiarton_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_wiarton_ont["Year"]
y2 = df_wiarton_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_wiarton_ont["Year"]
y3 = df_wiarton_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_wiarton_ont["Year"]
y4 = df_wiarton_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Wiarton Ontario")
plt.legend()
plt.show()

#Windsor Ontario

windsor_ont = pd.read_csv("/Users/bryanekeh/Desktop/Python_Scripts/wind_classifier/data_sets/canadian_windspeeds/windsor_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_windsor_ont = pd.DataFrame(windsor_ont)


df_windsor_ont["Oct"] = df_windsor_ont["Oct"].replace(-9999.9, df_windsor_ont["Oct"].median())
df_windsor_ont["Nov"] = df_windsor_ont["Nov"].replace(-9999.9, df_windsor_ont["Nov"].median())
df_windsor_ont["Dec"] = df_windsor_ont["Dec"].replace(-9999.9, df_windsor_ont["Dec"].median())
df_windsor_ont["Autumn"] = df_windsor_ont["Autumn"].replace(-9999.9, df_windsor_ont["Autumn"].median())

x1 = df_windsor_ont["Year"]
y1 = df_windsor_ont["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_windsor_ont["Year"]
y2 = df_windsor_ont["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_windsor_ont["Year"]
y3 = df_windsor_ont["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_windsor_ont["Year"]
y4 = df_windsor_ont["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')
plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Windsor Ontario")
plt.legend()
plt.show()
