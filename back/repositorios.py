import back.entidades
import psycopg2

from psycopg2 import Error
from back.database import ProfessorBD

class RepositorioProfessor(ProfessorBD):
    
    def __init__(self):
        super(RepositorioProfessor, self).__init__()
        self.__bd = ProfessorBD()
        self.__bd.connect(database='corretor')

    def insertProfessor(self, Professor=None):
        try:
            self._insertProfessor(Professor=Professor)
        except Exception as e:
            print(e)
            raise ValueError("Inserção invalida do professor")
