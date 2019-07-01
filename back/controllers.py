import back.repositorios
from back.repositorios import RepositorioProfessor

class ControllerProfessor:
    def __init__(self):
        self.repositorio = RepositorioProfessor()
    
    def recuperaProfessor(self, cod):
        professor = self.repositorio.getProfessor(cod)
        return professor

    # cria o professor no bd e retorna o codigo do prof criado
    def criaProfessor(self, Professor=None):
        cod_prof = self.repositorio.insertProfessor(Professor)
        return cod_prof

    def deletaProfessor(self, cod):
        self.repositorio.deleteProfessor(cod)

    def modificaProfessor(self, Professor=None):
        self.repositorio.updateProfessor(Professor)

    def recuperaProfessorCod(self, email):
        self.repositorio.getProfessorCod(email)