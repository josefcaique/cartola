import requests
from config.db import getConnection


data = requests.get("https://api.cartola.globo.com/rodadas")
json = data.json()
rodada = json

conn = getConnection()
cursor = conn.cursor()


query = "INSERT INTO rodadas VALUES (%s,%s,%s,%s)"

for item in json:
    dados = (item["rodada_id"],
             item["nome_rodada"],
             item["inicio"],
             item["fim"]
            )
    print(dados)
    cursor.execute(query, dados)

conn.commit()
cursor.close()
conn.close()
