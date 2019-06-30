import back.entidades
import psycopg2

from psycopg2 import Error
from back.database import BD

class RepositorioProfessor(BD):
    
    def __init__(self):
        self.__bd = BD()

    def insertProfessor(self, Professor=None):
        try:
            if self.__bd.connect():
                pass
        except Exception as e:
            print(e)
            raise ValueError("Inserção invalida do professor")

# "INSERT INTO Professor(Nome, Email, Senha, Foto, Data_Nasc) VALUES("+ "'" +
#                             +Professor.get_nome()+"','"+Professor.get_email()+"','"
#                             +Professor.get_senha()+"','"+Professor.get_foto()+"','"
#                             +Professor.get_dataNascimento() + "'" + ");"
