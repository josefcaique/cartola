import requests
import json
import pandas as pd

data = requests.get("https://api.cartola.globo.com/clubes")
json = data.json()
data = []
for k in json:
    value = json[k]
    name = value["nome"]
    abb = value["abreviacao"]
    slug = value["slug"]
    surname = value["apelido"]
    fantasy_name = value["nome_fantasia"]
    id = value["id"]

    data.append([id, name, abb, slug, surname, fantasy_name])
header = ["Id", "Nome", "Abreviacao", "Slug", "Apelido", "Nome_Fantasia"]
df_clubes = pd.DataFrame(data, columns=header)


df_clubes.to_csv("data/clubes.csv")
