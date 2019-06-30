from back.entidades import Professor
from back.repositorios import RepositorioProfessor

luisGarcia = Professor("Luis Garcia", "luis@unb.br", "verginica", "versicolor", "01/01/1985")
print("Nome do prof:", luisGarcia.get_nome())
print("Email do prof:", luisGarcia.get_email())
luisGarcia.set_email("luisgarcia@unb.br")
print("Mudando o emailkk:", luisGarcia.get_email())
print("Senha do prof:", luisGarcia.get_senha())
print("Foto do prof:", luisGarcia.get_foto())
print("Data de nascimento do prof:", luisGarcia.get_dataNascimento())

# repProf = RepositorioProfessor()
# repProf.insertProfessor(luisGarcia)