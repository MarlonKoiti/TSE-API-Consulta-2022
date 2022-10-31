import requests
import json
import pandas as pd

dados_tratados = {   

}

url        = 'https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json'
resposta   = requests.request("GET", url)
objetos    = json.loads(resposta.text)

total = int(objetos['vnom'])
print('Votos válidos:', total)

for i in objetos['cand']:
    if i['nm'] == 'LULA': 
        votosLula = round(int(i['vap']),2) 
        porcentagemLula = round(float((votosLula/total)*100), 2)
        #id = str(i['seq'])
        #cand = str(i['nm'])
        #InserirDados(id, cand, porcentagemLula)
    else:
        votosBolsonaro = round(int(i['vap']), 2)
        porcentagemBolsonaro = round(float((votosBolsonaro/total)*100),2)
        #id = str(i['seq'])
        #cand = str(i['nm'])
        #InserirDados(id, cand, porcentagemBolsonaro)
diff = round(float((porcentagemLula - porcentagemBolsonaro) * 1), 2)
print('Lula, total de votos: {}%'.format(porcentagemLula))
print('Jair, total de votos: {}%'.format(porcentagemBolsonaro))
print('Diferença:', diff )


# def InserirDados(id, cand, ptg):
#     dados_tratados = dados_tratados{'ID': id, 'Candidato': cand, 'Porcentagem': ptg}
#     print(dados_tratados)



            
    

    




