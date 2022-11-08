from datetime import datetime

class Pessoa:

    def __init__(self: object, nome: str):
        self.__nome = nome
        self.__nascimento = datetime.now()  # now.year, now.month, now.day, now.hour, now.minute, now.second
    
    def __str__(self: object) -> str:
        return self.__nome
    
    def __repr__(self: object) -> str:
        return self.__nome

class Carro:
    
    def __init__(self: object, is_sedan: bool = False):
        self.__is_sedan = is_sedan
        self.__velocidade = 0
        self.__motorista = None
    
    def dirigir(self: object, motorista: Pessoa):
        self.__motorista = motorista
        self.acelerar(1)

    def acelerar(self: object, velocidade: int):
        self.__velocidade += velocidade
    
    def parar(self: object):
        self.__velocidade = 0



