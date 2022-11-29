from abc import ABC, abstractmethod
from uuid import uuid4


class Pessoa(ABC):

    def __init__(self: object, nome: str):
        self.__nome = nome
    
    @abstractmethod
    def ganhar_dinheiro(self: object):
        pass



class Aluno(Pessoa):

    def __init__(self: object, nome: str):
        super().__init__(nome)
        self.__matricula = str(uuid4()).split('-')[0].upper()

    def ganhar_dinheiro(self: object):
        print('Como ganhar dinheiro? ')



aluno1 = Aluno('Angelina')
print(aluno1.__dict__)

