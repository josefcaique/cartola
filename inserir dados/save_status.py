import requests
import json
import pandas as pd

data = []
request = requests.get("https://api.cartola.globo.com/atletas/status")
json = request.json()





for item in json:
    id = json[item]["id"]
    nome = json[item]["nome"]
    data.append([id, nome])

header = ["id", "nome"]
df_status = pd.DataFrame(data, columns=header)

df_status.to_csv("data/status.csv")




