import requests
import json
import pandas as pd

data = []

for n in range(1, 22):
    
    print("Loading Match: " + str(n))

    request = requests.get("https://api.cartola.globo.com/partidas/" + str(n))
    json = request.json()

    for i in (json["partidas"]):
        aprovM = i["aproveitamento_mandante"]
        aprovV = i["aproveitamento_visitante"]
        local = i["local"]
        placarV = i["placar_oficial_visitante"]
        placarM = i["placar_oficial_mandante"]
        posiM = i["clube_casa_posicao"]
        posiV = i["clube_visitante_posicao"]
        mandId = i["clube_casa_id"]
        visiId = i["clube_visitante_id"]
        rodadaId = str(n)
        data.append([local, mandId, visiId, placarM, placarV, posiM, posiV, str(aprovM), str(aprovV), rodadaId])
       

header = ["local", "mandante_id", "visitante_id", "placar_mandante", "placar_visitante", "posicao_mandante", "posicao_visitante", "aproveitamento_mandante", "aproveitamento_visitante", "rodada_id"]
df_partida = pd.DataFrame(data, columns=header)


df_partida.to_csv("data/partidas.csv")


