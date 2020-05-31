from datetime import datetime

agora = datetime.now()
data = agora.strftime('%d/%m/%y')
hora = agora.strftime('%H:%M')
print(f'Agora vale: {agora}')
print(f'Data vale: {data}')
print(f'Hora vale: {hora}')
