from datetime import datetime
import pickle

def linha():
    print('====== OK ======')


agora=datetime.now()

print(f'O vavlor agora : {agora}. do tipo {type(agora)}')
es=1 #Entrada ao servico 1; Saida servico 2; Entrada Pausa 3. Saida da Pauda 4.
bemerkung='xxxxxxxxx'
regkart=[agora,es,bemerkung]
linha()
print(regkart)
linha()

ficheiro=open('simulacao.pkl','wb')
for i in range(1,32):
    agora=datetime.now()
    pickle.dump(regkart)



