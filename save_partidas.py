import requests
from config.db import getConnection

conn = getConnection()
cursor = conn.cursor()

query = "INSERT INTO partidas_historico(loca, clube_mandante_id, clube_visitante_id, placar_mandante, placar_visitante," \
        "clube_mandante_posicao, clube_visitante_posicao, aproveitamento_mandante, aproveitamento_visitante, rodada_id) " \
        "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"

for n in range(1, 8):
    
    data = requests.get("https://api.cartola.globo.com/partidas/" + str(n))
    json = data.json()

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
        dados = [local, mandId, visiId, placarM, placarV, posiM, posiV, aprovM, aprovV, rodadaId]
        cursor.execute(query, dados)


conn.commit()
cursor.close()
conn.close()

