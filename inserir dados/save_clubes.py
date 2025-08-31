import requests
import json
#from config.db import getConnection


#conn = getConnection()
#cursor = conn.cursor()


query = "INSERT INTO clubes VALUES (%s, %s, %s, %s, %s)"

data = requests.get("https://api.cartola.globo.com/clubes")
json = data.json()
for k in json:
    value = json[k]
    name = value["nome"]
    abr = value["abreviacao"]
    slug = value["slug"]
    fantasy_name = value["nome_fantasia"]
    id = str(value["id"])

    data = (id, name, abr, slug, fantasy_name)
    print(data)
    
