from datetime import datetime
import re

hora1 = '24-07-2019 00:00:00'
hora2 = '24-07-2019 00:00:00'
entrada = datetime.strptime(hora1, '%d-%m-%Y %H:%M:%S')
saida = datetime.strptime(hora2, '%d-%m-%Y %H:%M:%S')

intervalo = str(saida - entrada)
if saida < entrada:
    print('A saida não pode ser menor que a entrada')
elif saida == entrada:
    print('Saida liberada, dentro da carencia')
else:
    padrao1 = '([0-9]{1,2}) day[s]?, ([0-9]{1,2}):([0-9]{2}):([0-9]{2})'
    padrao2 = '([0-9]{2}):([0-9]{2}):([0-9]{2})'

    resp = re.search(padrao1, intervalo)
    if resp:
        minutos = (int(resp.group(1)) * 1440) + (int(resp.group(2)) *60) + (int(resp.group(3))) + (int(resp.group(4))/60)
        print(f'R$ {minutos * 0.05:.2f}'.replace('.', ','))
    else:
        resp = re.search(padrao2, intervalo)
        minutos = (int(resp.group(1)) * 60) + (int(resp.group(2))) + (int(resp.group(3)) / 60)
        print(f'R$ {minutos * 0.05:.2f}'.replace('.', ','))

