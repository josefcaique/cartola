from config.db import getConnection
import unicodedata

conn = getConnection()
cursor = conn.cursor()
path = "test.txt"
c=0

with open(path, "r") as file:
    for line in file:
        splited = line.split(" ")
        mId = int(splited[2])
        vId = int(splited[5])
        round = splited[1]
        

        query = "INSERT INTO partidas_totais(mandante_id, visitante_id, rodada_id)" \
                "VALUES (%s, %s, %s)"
        dados = (mId, vId, round)
        cursor.execute(query, dados)
        
conn.commit()
cursor.close()
conn.close()
