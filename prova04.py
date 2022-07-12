



'''class Estacionamento:
    def __init__(self):
        self.__tipoVeiculo = ''
        self.__placa = ''
        self.__modelo = ''
        self.__entrada = ''
        self.__saida = ''
        self.__valorHora = 0


    def setTipoVeiculo(self, tipoVeiculo):
        self.__tipoVeiculo = tipoVeiculo

    def getTipoVeiculo(self):
        return self.__tipoVeiculo

    def setPlaca(self, placa):
        self.__placa = placa

    def getPlaca(self):
        return self.__placa

    def setModelo(self,modelo):
        self.__modelo = modelo

    def getModelo(self):
        return self.__modelo

    def setEntrada(self,entrada):
        self.__entrada = entrada

    def getEntrada(self):
        return self.__entrada

    def setSaida(self,saida):
        self.__saida = saida

    def getSaida(self):
        return self.__saida

    def setValorHora(self,valorHora):
        self.__valorHora = valorHora

    def getValorHora(self):
        return self.__valorHora

    def calcular(self, entrada, saida, valorHora):
        entrada = datetime.strptime(self.__entrada, '%d-%m-%Y %H:%M:%S')
        saida = datetime.strptime(self.__saida, '%d-%m-%Y %H:%M:%S')
        valorTotal = (entrada - saida) * valorHora
        return print(f'Valor a se pagar {valorTotal}')
        
        
        










carro1 = Estacionamento()
carro1.setTipoVeiculo('carro')
carro1.setPlaca('xxx-999')
carro1.setModelo('UNO')
carro1.setEntrada('22-07-2019 05:00:00')
carro1.setValorHora(float(input('Digite o valor da hora: R$')))
carro1.setSaida(input('Digite a hora da saida: '))'''




from datetime import datetime

hora1 = '22-07-2019 05:00:00'
hora2 = '22-07-2019 10:00:00'

entrada = datetime.strptime(hora1, '%d-%m-%Y %H:%M:%S')
saida = datetime.strptime(hora2, '%d-%m-%Y %H:%M:%S')


intervalo = (saida - entrada)

print(intervalo)