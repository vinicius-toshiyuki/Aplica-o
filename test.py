from back.entidades import *
from back.repositorios import *
# from back.database import Corretor

# luisGarcia = Professor(nome="Luis Garcia", email="luis@unb.br", senha="verginica", foto="./tmp/temp.png", dataNascimento="01/01/1985")
# print("Nome do prof:", luisGarcia.get_nome())
# print("Email do prof:", luisGarcia.get_email())
# luisGarcia.set_email("luisgarcia@unb.br")
# print("Mudando o emailkk:", luisGarcia.get_email())
# print("Senha do prof:", luisGarcia.get_senha())
# print("Foto do prof:", luisGarcia.get_foto())
# print("Data de nascimento do prof:", luisGarcia.get_dataNascimento())

# repProf = RepositorioProfessor()
# cod = repProf.insertProfessor(Professor=luisGarcia)
# luisGarcia.set_professor_cod(cod)
# print(luisGarcia.get_professor_cod())

# luisGarcia.set_nome('Ladeirakkk')
# repProf.updateProfessor(luisGarcia)
# print(luisGarcia.get_nome())
# print(repProf.getProfessorCod('luisgarcia@unb.br'))

# prof2 = repProf.getProfessor(luisGarcia.get_professor_cod())
# print(prof2.get_nome())
# print(prof2.get_foto())
# repProf.deleteProfessor(luisGarcia.get_professor_cod())

# alunin = Aluno(matricula=170012280,nome="Henrique",email="hqmariano@live.com",senha="12345",foto="./tmp/temp.png",dataNascimento="11/03/1999",turma_cod=1,turma_semestre="20191",disciplina_cod=1)
# print("Disciplina: ", alunin.get_disciplina_cod(), end="\n")
# repAluno = RepositorioAluno()
# repAluno.insertAluno(alunin)
# aluno_recuperadokk = repAluno.getAluno(170012280)
# print(aluno_recuperadokk.get_matricula())
# repAluno.updateAluno(alunin)
# repAluno.deleteAluno(170012280)

discipline = Disciplina('Banco de dados')
repDisci = RepositorioDisciplina()
cod = repDisci.insertDisciplina(discipline)
discipline.set_disciplina_cod(cod)
print("Cod:", discipline.get_disciplina_cod(),end="\n")
disciplina_recuperada = repDisci.getDisciplina(discipline.get_disciplina_cod())
print(disciplina_recuperada.get_nome(), end="\n")
disciplina_recuperada.set_nome('LP')
repDisci.updateDisciplina(disciplina_recuperada)
disciplina_rec = repDisci.getDisciplina(disciplina_recuperada.get_disciplina_cod())
print(disciplina_rec.get_nome(), end="\n")
repDisci.deleteDisciplina(disciplina_rec.get_disciplina_cod())
