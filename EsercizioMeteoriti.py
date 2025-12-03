import matplotlib.pyplot as plt
import json, folium

m = folium.Map(location=(0, 0), zoom_start=5)
nome_file = "meteorites.json"

with open(nome_file, "r", encoding="utf8") as file:
  stringa_json = file.read()
oggetto = json.loads(stringa_json)
massa = []
anni = []
for elem in oggetto:
        try:
              massa.append(elem["mass"])
              anni.append(elem["year"])
        except:
               continue
#Numero meteoriti caduti
print("Numero di meteoriti caduti:", len(oggetto))

#Stampo le chiavi del primo elemento
print(oggetto[0].keys())

#Stampo i primi 5 elementi
cycle = 5
i = 0
while(i < cycle):
      print(oggetto[i])
      i = i + 1

      
plt.figure(figsize=(10, 6))
plt.hist(massa, bins=10, edgecolor='black', color='gold', log=True)
plt.xlabel("Massa (g)")
plt.ylabel("Frequenza")
plt.title("Distribuzione delle Masse dei Meteoriti")
plt.grid(axis='y', alpha=0.75)
plt.show()



