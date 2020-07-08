from datetime import datetime
import pickle

def linha():
    print('====== OK ======')


agora=datetime.now()

print(f'O vavlor agora : {agora}. do tipo {type(agora)}')
es=1 #Entrada ao servico 1; Saida servico 2; Entrada Pausa 3. Saida da Pausa 4.
bemerkung='xxxxxxxxx'
regkart=[agora,es,bemerkung]
linha()
print(regkart)
linha()

#Escrever ficheiro com 31 registo
ficheiro=open('simulacao.pkl','ab')
for i in range(1,32):
    agora=datetime.now()
    print(agora)
    pickle.dump(regkart,ficheiro)
ficheiro.close()
linha()
#Ler ficheiro
regkart=[agora,2,'anular a variavel']
ficheiro=open('simulacao.pkl','rb')
teste=pickle.load(ficheiro)
print(teste)
ficheiro.close()



