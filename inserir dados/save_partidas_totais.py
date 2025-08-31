import requests
import json
import pandas as pd

path = "inserir dados/test.txt"
c=0
data = []

with open(path, "r") as file:
    for line in file:
        splited = line.split(" ")
        mId = int(splited[2])
        vId = int(splited[5])
        round = splited[1]
        data.append([mId, vId, round])



header = ["mandante_id", "visitante_id", "rodada_id"]
df_partida_totais = pd.DataFrame(data, columns=header)

df_partida_totais.to_csv("data/partidas_totais.csv")