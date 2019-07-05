import back.entidades
import psycopg2

from psycopg2 import Error
from back.database import ProfessorBD
from back.database import AlunoBD

class RepositorioProfessor(ProfessorBD):
    
    def __init__(self):
        super(RepositorioProfessor, self).__init__()

    def getProfessor(self, cod):
        try:
            professor = self._getProfessor(cod)
        except Exception as e:
            print(e)
            raise ValueError("Não existe professor com esse código")
        return professor

    def insertProfessor(self, Professor=None):
        try:
            cod = self._insertProfessor(Professor)
        except Exception as e:
            print(e)
            raise ValueError("Inserção invalida do professor")
        return cod

    def updateProfessor(self, Professor=None):
        try:
        	self._updateProfessor(Professor)
        except Exception as e:
            print(e)
            raise ValueError("Modificação invalida do professor")

    def deleteProfessor(self, Cod):
        try:
            self._deleteProfessor(Cod)
        except Exception as e:
            print(e)
            raise ValueError("Não existe professor com esse cod")

    def getProfessorCod(self, email):
        try:
            cod = self._getProfessorCod(email)
        except Exception as e:
            print(e)
            raise ValueError("Não existe professor com esse email")
        return cod

class RepositorioAluno(AlunoBD):

    def getAluno(self, matricula):
        try:
            aluno = self._getAluno(matricula)
        except Exception as e:
            print(e)
            raise ValueError("Não existe aluno com essa matricula")
        return aluno
        

    def insertAluno(self, Aluno=None):
        try:
            self._insertAluno(Aluno)
        except Exception as e:
            print(e)
            raise ValueError("Inserção invalida do aluno")

    def updateAluno(self, Aluno=None):
        try:
        	self._updateAluno(Aluno)
        except Exception as e:
            print(e)
            raise ValueError("Modificação invalida do aluno")   
    
    def deleteAluno(self, matricula):
        try:
            self._deleteAluno(matricula)
        except Exception as e:
            print(e)
            raise ValueError("Não existe aluno com essa matricula")

# Fazer o rep da disciplina