import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("prodaja_igara.csv")
data.dropna(how="any",inplace = True)
data.info()
print(data.head(10))
print(data.tail(10))

#deset hiljada kopija
deset_hiljada = data[data["Global_Sales"]==0.01]
nula_nulajedan = deset_hiljada["Global_Sales"].count()
print("Da, ima {} igara sa 0.01(10k) miliona kopija prodatih na Globalnom trzistu.".format(nula_nulajedan))

#ukupna prodaja
globalna_prodaja = data["Global_Sales"]
uk_globalna_prodaja = globalna_prodaja.sum()
print("Ukupna prodaja ostvarena u svetu je ${:.2f}(million)".format(uk_globalna_prodaja))

#broj igara izdatih po platformi
data.groupby("Platform").size().plot(kind="bar")
plt.ylabel("Broj igara")
plt.savefig("0_platforma.png",dpi=300)
plt.show()

#koje godine je izbaceno najvise igara
data.groupby("Year")["Global_Sales"].sum().plot(kind="line", grid=True, legend=True)
plt.title("Broj igara izdatih po godinama u globalu")
plt.savefig("1_br_igara_god_global.png",dpi=300)
plt.show()

data.groupby("Year")["NA_Sales"].sum().plot(kind="line", grid=True, legend=True)
data.groupby("Year")["EU_Sales"].sum().plot(kind="line", grid=True, legend=True)
data.groupby("Year")["JP_Sales"].sum().plot(kind="line", grid=True, legend=True)
data.groupby("Year")["Other_Sales"].sum().plot(kind="line", grid=True, legend=True)
plt.title("Broj igara izdatih po godinama po trzistu")
plt.savefig("2_br_igara_god_trziste.png",dpi=300)
plt.show()

#igre sa najveceom globalnom prodajom
igra = data.loc[:,["Name","Global_Sales"]]
igra = igra.sort_values("Global_Sales", ascending=False)
igra = igra.head()

fig = plt.figure(figsize=(10,7))
plt.pie(igra["Global_Sales"], labels=igra["Name"], autopct="%1.1f%%", shadow=True)
centre_circle = plt.Circle((0,0),0.45,color="black", fc="white",linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis("equal")
plt.title("Igre sa najvecom globalnom prodajom")
plt.savefig("3_igare_najv_glob_prod.png",dpi=300)
plt.show()

#zanrovi sa najvecom globalnom prodajom
zanr = data.loc[:,["Genre","Global_Sales"]]
zanr["uk_prodaja"] = zanr.groupby("Genre")["Global_Sales"].transform("sum")
zanr.drop("Global_Sales", axis=1, inplace=True)
zanr = zanr.drop_duplicates()
zanr = zanr.sort_values("uk_prodaja", ascending=False)

fig = plt.figure(figsize=(10,7))
plt.pie(zanr["uk_prodaja"], labels=zanr["Genre"], autopct="%1.1f%%", shadow=True)
centre_circle = plt.Circle((0,0),0.45,color="black", fc="white",linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis("equal")
plt.title("Zanrovi sa najvecom globalnom prodajom")
plt.savefig("4_zanr_najv_glob_prod.png",dpi=300)
plt.show()

#izdavac sa najvecom prodajom na globalnom trzistu
izdavaci = data.loc[:,["Publisher","Global_Sales"]]
izdavaci["uk_prodaja_i"] = izdavaci.groupby("Publisher")["Global_Sales"].transform("sum")
izdavaci.drop("Global_Sales", axis=1, inplace=True)
izdavaci = izdavaci.drop_duplicates()
izdavaci = izdavaci.sort_values("uk_prodaja_i", ascending=False)
izdavaci = izdavaci.head()

fig = plt.figure(figsize=(10,7))
plt.pie(izdavaci["uk_prodaja_i"], labels=izdavaci["Publisher"], autopct="%1.1f%%", shadow=True)
centre_circle = plt.Circle((0,0),0.45,color="black", fc="white",linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis("equal")
plt.title("Izdavaci sa najvecom globalnom prodajom")
plt.savefig("5_izdavaci_najv_glob_prod.png",dpi=300)
plt.show()

#zanrovi sa najvecom prodajom na americkom trzistu bez ekstrema
zanr = data.loc[data["Name"]!="Wii Sports",["Genre","NA_Sales"]]
zanr["uk_prodaja_z"] = zanr.groupby("Genre")["NA_Sales"].transform("sum")
zanr.drop("NA_Sales", axis=1, inplace=True)
zanr = zanr.drop_duplicates()
zanr = zanr.sort_values("uk_prodaja_z", ascending=False)
zanr = zanr.head()

fig = plt.figure(figsize=(10,7))
plt.pie(zanr["uk_prodaja_z"], labels=zanr["Genre"], autopct="%1.1f%%", shadow=True)
centre_circle = plt.Circle((0,0),0.45,color="black", fc="white",linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis("equal")
plt.title("Zanrovi sa najvecom prodajom na Americkom trzistu")
plt.savefig("6_zanr_najv_amer_prod.png",dpi=300)
plt.show()

#procenat igara prodatih na americkom trzistu po platformama
platforme = data.loc[data["Name"]!="Wii Sports",["Platform","NA_Sales"]]
platforme["uk_prodaja_p"] = platforme.groupby("Platform")["NA_Sales"].transform("sum")
platforme.drop("NA_Sales", axis=1, inplace=True)
platforme = platforme.drop_duplicates()
platforme = platforme.sort_values("uk_prodaja_p", ascending=False)
platforme = platforme.head()

fig = plt.figure(figsize=(10,7))
plt.pie(platforme["uk_prodaja_p"], labels=platforme["Platform"], autopct="%1.1f%%", shadow=True)
centre_circle = plt.Circle((0,0),0.45,color="black", fc="white",linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis("equal")
plt.title("Procenat igara prodatih po platformama na Americkom trzistu")
plt.savefig("7_proc_platforme_amer_trziste.png",dpi=300)
plt.show()

#najprodavanije igre na americkom trzistu bez ekstrema
igra = data.loc[data["Name"]!="Wii Sports",["Name","NA_Sales"]]
igra = igra.sort_values("NA_Sales", ascending=False)
igra = igra.head()

fig = plt.figure(figsize=(10,7))
plt.pie(igra["NA_Sales"], labels=igra["Name"], autopct="%1.1f%%", shadow=True)
centre_circle = plt.Circle((0,0),0.45,color="black", fc="white",linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis("equal")
plt.title("Igre sa najvecom prodajom na Americkom trzistu")
plt.savefig("8_igare_najprod_amer_trziste.png",dpi=300)
plt.show()

#odnos prodaje Americko Evropsko trziste
data.plot(kind="scatter", x="NA_Sales", y="EU_Sales",alpha = 0.5,color = "red")
plt.xlabel("NA_Sales")
plt.ylabel("EU_Sales")
plt.grid()
plt.title("Odnos prodaje igre izmedju dva trzista")
plt.savefig("9_amer_vs_eu.png",dpi=300)
plt.show()
