import requests
import json
import pandas as pd

data = []
request = requests.get("https://api.cartola.globo.com/posicoes")
json = request.json()


for item in json:
    id = json[item]["id"]
    nome = json[item]["nome"]
    abr = json[item]["abreviacao"]
    data.append([id, nome, abr])
    

header = ["id", "nome", "abreviacao"]
df_position = pd.DataFrame(data, columns=header)

df_position.to_csv("data/posicoes.csv")

