import requests
import json
import pandas as pd

data = []
request = requests.get("https://api.cartola.globo.com/rodadas")
json = request.json()


for item in json:
    data.append([item["rodada_id"],
             item["nome_rodada"],
             item["inicio"],
             item["fim"]
            ])

header = ["rodada_id", "nome_rodada", "inicio", "fim"]
df_match = pd.DataFrame(data, columns=header)

df_match.to_csv("data/rodadas.csv")
