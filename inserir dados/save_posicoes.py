import requests
from config.db import getConnection


data = requests.get("https://api.cartola.globo.com/posicoes")
json = data.json()
rodada = json

conn = getConnection()
cursor = conn.cursor()


query = "INSERT INTO posicoes VALUES (%s, %s, %s)"

for item in json:
    id = json[item]["id"]
    nome = json[item]["nome"]
    abr = json[item]["abreviacao"]
    dados = [id, nome, abr]
    cursor.execute(query, dados)

conn.commit()
cursor.close()
conn.close()

