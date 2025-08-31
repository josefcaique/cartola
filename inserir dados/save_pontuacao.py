import requests
import json
import pandas as pd

data = []

for i in range(1, 22):
    request = requests.get("https://api.cartola.globo.com/atletas/pontuados/"+str(i))
    json = request.json()


    for item in json:
        for j in json[item]:
            
            atleta_id = j
            apelido = json[item][j]["apelido"]
            pontuacao = json[item][j]["pontuacao"]
            posicao_id = json[item][j]["posicao_id"]
            clube_id = json[item][j]["clube_id"]
            em_Campo = json[item][j]["entrou_em_campo"]
            scouts = json[item][j]["scout"]
            rodada_id = str(i)

            data.append([atleta_id, apelido, pontuacao, posicao_id, clube_id, scouts, em_Campo, rodada_id])
        break

header = ["id", "apelido", "pontuacao", "posicao_id", "clube_id", "scouts", "entrou", "rodada_id"]
df_pontos = pd.DataFrame(data, columns=header)


df_pontos.to_csv("data/jogadores.csv")

