import matplotlib.pyplot as plt
import json

filename = "meteorites.json"

try:
  with open(filename, 'r') as file:
    dati_meteoriti = json.load(file)
  print("Dati caricati con successo!")
  print(f"Numero di meteoriti: {len(dati_meteoriti)}")
except FileNotFoundError:
  print(f"Errore: Il file '{filename}' non è stato trovato.")
