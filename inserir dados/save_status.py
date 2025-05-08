import requests
from config.db import getConnection


data = requests.get("https://api.cartola.globo.com/atletas/status")
json = data.json()
rodada = json

conn = getConnection()
cursor = conn.cursor()


query = "INSERT INTO status VALUES (%s, %s)"

for item in json:
    id = json[item]["id"]
    nome = json[item]["nome"]
    dados = [id, nome]
    cursor.execute(query, dados)

conn.commit()
cursor.close()
conn.close()

