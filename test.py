from back.entidades import Professor
from back.repositorios import RepositorioProfessor
from back.database import Corretor

luisGarcia = Professor("Luis Garcia", "luis@unb.br", "verginica", "./tmp/temp.png", "01/01/1985")
print("Nome do prof:", luisGarcia.get_nome())
print("Email do prof:", luisGarcia.get_email())
luisGarcia.set_email("luisgarcia@unb.br")
print("Mudando o emailkk:", luisGarcia.get_email())
print("Senha do prof:", luisGarcia.get_senha())
print("Foto do prof:", luisGarcia.get_foto())
print("Data de nascimento do prof:", luisGarcia.get_dataNascimento())

repProf = RepositorioProfessor()
repProf.insertProfessor(Professor=luisGarcia)

# aux = Corretor()

# aux.connect(database='corretor')

# aux._insert_professor(nome=luisGarcia.get_nome(), email=luisGarcia.get_email(),
#                     senha=luisGarcia.get_senha(), foto=luisGarcia.get_foto(),
# 					data_de_nascimento=luisGarcia.get_dataNascimento())