import requests
import json
from config.db import getConnection





conn = getConnection()
cursor = conn.cursor()
for i in range(1, 8):
    data = requests.get("https://api.cartola.globo.com/atletas/pontuados/"+str(i))
    jsonData = data.json()
    query = "INSERT INTO atleta_pontuacao(apelido, atleta_id, pontuacao, posicao_id, clube_id, rodada_id, entrou_em_campo, scouts) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    for item in jsonData:
        for j in jsonData[item]:
            atleta_id = j
            apelido = jsonData[item][j]["apelido"]
            pontuacao = jsonData[item][j]["pontuacao"]
            posicao_id = jsonData[item][j]["posicao_id"]
            clube_id = jsonData[item][j]["clube_id"]
            em_Campo = jsonData[item][j]["entrou_em_campo"]
            scouts = json.dumps(jsonData[item][j]["scout"])
            rodada_id = 1

            dados = (apelido, atleta_id, pontuacao, posicao_id, clube_id, rodada_id, em_Campo, scouts)
            cursor.execute(query, dados)
        break

conn.commit()
cursor.close()
conn.close()

