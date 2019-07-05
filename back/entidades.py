class Professor:
    __cod_professor= -1
    __nome = ""
    __email = ""
    __senha = ""
    __foto = ""
    __dataNascimento = ""
    __dataCadastro = ""

    def __init__(self, professor_cod=-1, nome="", email="", senha="", foto="", dataNascimento="", dataCadastro=""):
        self.set_professor_cod(professor_cod)
        self.set_nome(nome)
        self.set_email(email)
        self.set_senha(senha)
        self.set_foto(foto)
        self.set_dataNascimento(dataNascimento)
        self.set_dataCadastro(dataCadastro)

    def get_professor_cod(self):
        return self.__professor_cod

    def set_professor_cod(self, professor_cod=-1):
        self.__professor_cod = professor_cod

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome=""):
        self.__nome = nome

    def get_email(self):
        return self.__email

    def set_email(self, email=""):
        self.__email = email
    
    def get_senha(self):
        return self.__senha

    def set_senha(self, senha=""):
        self.__senha = senha

    def get_foto(self):
        return self.__foto

    def set_foto(self, foto=""):
        self.__foto = foto

    def get_dataNascimento(self):
        return self.__dataNascimento

    def set_dataNascimento(self, dataNascimento=""):
        self.__dataNascimento = dataNascimento

    def get_dataCadastro(self):
        return self.__dataCadastro

    def set_dataCadastro(self, dataCadastro=""):
        self.__dataCadastro = dataCadastro

class Aluno:
    __matricula = -1
    __nome = ""
    __email = ""
    __senha = ""
    __foto = ""
    __dataNascimento = ""
    __dataCadastro = ""
    __turma_cod = -1
    __turma_semestre = ""
    __disciplina_cod = -1

    def __init__(self, matricula=-1, nome="", email="", senha="", foto="", dataNascimento="", dataCadastro="", turma_cod=-1, turma_semestre="",disciplina_cod=-1):
        self.set_matricula(matricula)
        self.set_nome(nome)
        self.set_email(email)
        self.set_senha(senha)
        self.set_foto(foto)
        self.set_dataNascimento(dataNascimento)
        self.set_dataCadastro(dataCadastro)
        self.set_turma_cod(turma_cod)
        self.set_turma_semestre(turma_semestre)
        self.set_disciplina_cod(disciplina_cod)

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula=-1):
        self.__matricula = matricula

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome=""):
        self.__nome = nome

    def get_email(self):
        return self.__email

    def set_email(self, email=""):
        self.__email = email

    def get_senha(self):
        return self.__senha

    def set_senha(self, senha=""):
        self.__senha = senha

    def get_foto(self):
        return self.__foto

    def set_foto(self, foto=""):
        self.__foto = foto

    def get_dataNascimento(self):
        return self.__dataNascimento

    def set_dataNascimento(self, dataNascimento=""):
        self.__dataNascimento = dataNascimento

    def get_dataCadastro(self):
        return self.__dataCadastro

    def set_dataCadastro(self, dataCadastro=""):
        self.__dataCadastro = dataCadastro

    def get_turma_cod(self):
        return self.__turma_cod

    def set_turma_cod(self, turma_cod=-1):
        self.__turma_cod = turma_cod

    def get_turma_semestre(self):
        return self.__turma_semestre

    def set_turma_semestre(self, semestre=""):
        self.__turma_semestre = semestre

    def get_disciplina_cod(self):
        return self.__disciplina_cod

    def set_disciplina_cod(self, disciplina_cod=-1):
        self.__disciplina_cod = disciplina_cod

class Disciplina:
    __disciplina_cod = -1
    __nome = ""

    def __init__(self, disciplina_cod=-1, nome=""):
        self.set_disciplina_cod(disciplina_cod)
        self.set_nome(nome)

    def get_disciplina_cod(self):
        return self.__disciplina_cod

    def set_disciplina_cod(self, disciplina_cod=-1):
        self.__disciplina_cod = disciplina_cod

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome=""):
        self.__nome = nome

class Turma:
    __codigo = -1
    __semestre = ""
    __disciplina_cod = -1
    __professor_cod = -1

    def __init__(self, codigo=-1, semestre="", disciplina_cod=-1, professor_cod=-1):
        self.set_codigo(codigo)
        self.set_semestre(semestre)
        self.set_disciplina_cod(disciplina_cod)
        self.set_professor_cod(professor_cod)

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo=-1):
        self.__codigo = codigo

    def get_semestre(self):
        return self.__semestre

    def set_semestre(self, semestre=""):
        self.__semestre = semestre

    def get_disciplina_cod(self):
        return self.__disciplina_cod

    def set_disciplina_cod(self, disciplina_cod=-1):
        self.__disciplina_cod = disciplina_cod

    def get_professor_cod(self):
        return self.__professor_cod

    def set_professor_cod(self, professor_cod=-1):
        self.__professor_cod = professor_cod

class LingProgr:
    __nome = ""
    __comando_comp = ""

    def __init__(self, nome="", comando=""):
        self.set_nome(nome)
        self.set_comando(comando)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome=""):
        self.__nome = nome

    def get_comando(self):
        return self.__comando_comp

    def set_comando(self, comando_comp=""):
        self.__comando_comp = comando_comp

class Submissao:
    __submissao_cod = -1
    __dataHora = ""
    __codFonte = ""
    __memUtilizada = ""
    __tempoDecorrido = ""
    __veredito = ""
    __aluno_matr = -1
    __problema_cod = -1
    __lingProgr_cod = -1

    def __init__(self, submissao_cod=-1,dataHora="",codFonte="",memUtilizada="",tempoDecorrido="",veredito="",aluno_matr=-1,problema_cod=-1,lingProgr_cod=-1):
        self.set_submissao_cod(submissao_cod)
        self.set_dataHora(dataHora)
        self.set_codFonte(codFonte)
        self.set_memUtilizada(memUtilizada)
        self.set_tempoDecorrido(tempoDecorrido)
        self.set_veredito(veredito)
        self.set_aluno_matr(aluno_matr)
        self.set_problema_cod(problema_cod)
        self.set_lingProgr_cod(lingProgr_cod)

    def get_submissao_cod(self):
        return self.__submissao_cod

    def set_submissao_cod(self, submissao_cod=-1):
        self.__submissao_cod = submissao_cod

    def get_dataHora(self):
        return self.__dataHora

    def set_dataHora(self, dataHora=""):
        self.__dataHora = dataHora

    def get_codFonte(self):
        return self.__codFonte

    def set_codFonte(self, codFonte=""):
        self.__codFonte = codFonte

    def get_memUtilizada(self):
        return self.__memUtilizada

    def set_memUtilizada(self, memUtilizada=""):
        self.__memUtilizada = memUtilizada

    def get_tempoDecorrido(self):
        return self.__tempoDecorrido

    def set_tempoDecorrido(self, tempoDecorrido=""):
        self.__tempoDecorrido = tempoDecorrido

    def get_veredito(self):
        return self.__veredito

    def set_veredito(self, veredito=""):
        self.__veredito = veredito

    def get_aluno_matr(self):
        return self.__aluno_matr

    def set_aluno_matr(self, aluno_matr=-1):
        self.__aluno_matr = aluno_matr

    def get_problema_cod(self):
        return self.__problema_cod

    def set_problema_cod(self, problema_cod=-1):
        self.__problema_cod = problema_cod

    def get_lingProgr_cod(self):
        return self.__lingProgr_cod

    def set_lingProgr_cod(self, lingProgr=-1):
        self.__lingProgr_cod = lingProgr

class Problema:
    __problema_cod = -1
    __titulo = ""
    __descricao = ""
    __dificuldade = ""
    __limiteMem = ""
    __limiteTemp = ""
    __lista_cod = -1
    __modulo_cod = -1
    __disciplina_cod = -1

    def __init__(self, problema_cod=-1,titulo="",descricao="",dificuldade="",limiteMem="",limiteTemp="",lista_cod=-1,modulo_cod=-1,disciplina_cod=-1):
        self.set_problema_cod(problema_cod)
        self.set_titulo(titulo)
        self.set_descricao(descricao)
        self.set_dificuldade(dificuldade)
        self.set_limiteMem(limiteMem)
        self.set_limiteTemp(limiteTemp)
        self.set_lista_cod(lista_cod)
        self.set_modulo_cod(modulo_cod)
        self.set_disciplina_cod(disciplina_cod)

    def get_problema_cod(self):
        return self.__problema_cod

    def set_problema_cod(self, problema_cod=-1):
        self.__problema_cod = problema_cod

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo=""):
        self.__titulo = titulo

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao=""):
        self.__descricao = descricao

    def get_dificuldade(self):
        return self.__dificuldade

    def set_dificuldade(self, dificuldade=""):
        self.__dificuldade = dificuldade

    def get_limiteMem(self):
        return self.__limiteMem

    def set_limiteMem(self, limiteMem=""):
        self.__limiteMem = limiteMem

    def get_limiteTemp(self):
        return self.__limiteTemp

    def set_limiteTemp(self, limiteTemp=""):
        self.__limiteTemp = limiteTemp

    def get_lista_cod(self):
        return self.__lista_cod

    def set_lista_cod(self, lista_cod=-1):
        self.__lista_cod = lista_cod

    def get_modulo_cod(self):
        return self.__modulo_cod

    def set_modulo_cod(self, modulo_cod=-1):
        self.__modulo_cod = modulo_cod

    def get_disciplina_cod(self):
        return self.__disciplina_cod

    def set_disciplina_cod(self, disciplina_cod=-1):
        self.__disciplina_cod = disciplina_cod

class Entrada:
    __entrada = ""
    __problema_cod = -1
    __lista_cod = -1
    __modulo_cod = -1
    __disciplina_cod = -1

    def __init__(self, entrada="",problema_cod="",lista_cod=-1,modulo_cod=-1,disciplina_cod=-1):
        self.set_entrada(entrada)
        self.set_problema_cod(problema_cod)
        self.set_lista_cod(lista_cod)
        self.set_modulo_cod(modulo_cod)
        self.set_disciplina_cod(disciplina_cod)

    def get_entrada(self):
        return self.__entrada

    def set_entrada(self, entrada=""):
        self.__entrada = entrada

    def get_problema_cod(self):
        return self.__problema_cod

    def set_problema_cod(self, problema_cod=-1):
        self.__problema_cod = problema_cod

    def get_lista_cod(self):
        return self.__lista_cod

    def set_lista_cod(self, lista_cod=-1):
        self.__lista_cod = lista_cod

    def get_modulo_cod(self):
        return self.__modulo_cod

    def set_modulo_cod(self, modulo_cod=-1):
        self.__modulo_cod = modulo_cod

    def get_disciplina_cod(self):
        return self.__disciplina_cod

    def set_disciplina_cod(self, disciplina_cod=-1):
        self.__disciplina_cod = disciplina_cod

class Saida:
    __saida = ""
    __problema_cod = -1
    __lista_cod = -1
    __modulo_cod = -1
    __disciplina_cod = -1

    def __init__(self, saida="",problema_cod="",lista_cod=-1,modulo_cod=-1,disciplina_cod=-1):
        self.set_saida(saida)
        self.set_problema_cod(problema_cod)
        self.set_lista_cod(lista_cod)
        self.set_modulo_cod(modulo_cod)
        self.set_disciplina_cod(disciplina_cod)

    def get_saida(self):
        return self.__saida

    def set_saida(self, saida=""):
        self.__saida = saida

    def get_problema_cod(self):
        return self.__problema_cod

    def set_problema_cod(self, problema_cod=-1):
        self.__problema_cod = problema_cod

    def get_lista_cod(self):
        return self.__lista_cod

    def set_lista_cod(self, lista_cod=-1):
        self.__lista_cod = lista_cod

    def get_modulo_cod(self):
        return self.__modulo_cod

    def set_modulo_cod(self, modulo_cod=-1):
        self.__modulo_cod = modulo_cod

    def get_disciplina_cod(self):
        return self.__disciplina_cod

    def set_disciplina_cod(self, disciplina_cod=-1):
        self.__disciplina_cod = disciplina_cod

class Lista:
    __lista_cod = -1
    __titulo = ""
    __descricao = ""
    __dataHrInicio = ""
    __dataHrFim = ""
    __visibilidade = ""
    __prova = ""
    __modulo_cod = -1
    __disciplina_cod = -1

    def __init__(self, lista_cod=-1,titulo="",descricao="",dataHrInicio="",dataHrFim="",visibilidade="",prova="",modulo_cod=-1,disciplina_cod=-1):
        self.set_lista_cod(lista_cod)
        self.set_titulo(titulo)
        self.set_descricao(descricao)
        self.set_dataHrInicio(dataHrInicio)
        self.set_dataHrFim(dataHrFim)
        self.set_visibilidade(visibilidade)
        self.set_prova(prova)
        self.set_modulo_cod(modulo_cod)
        self.set_disciplina_cod(disciplina_cod)

    def get_lista_cod(self):
        return self.__lista_cod

    def set_lista_cod(self, lista_cod=-1):
        self.__lista_cod = lista_cod

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo=""):
        self.__titulo = titulo

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao=""):
        self.__descricao = descricao

    def get_dataHrInicio(self):
        return self.__dataHrInicio
    
    def set_dataHrInicio(self, dataHrInicio=""):
        self.__dataHrInicio = dataHrInicio

    def get_dataHrFim(self):
        return self.__dataHrFim

    def set_dataHrFim(self, dataHrFim=""):
        self.__dataHrFim = dataHrFim

    def get_visibilidade(self):
        return self.__visibilidade

    def set_visibilidade(self, visibilidade=""):
        self.__visibilidade = visibilidade

    def get_prova(self):
        return self.__prova

    def set_prova(self, prova=""):
        self.__prova = prova

    def get_modulo_cod(self):
        return self.__modulo_cod

    def set_modulo_cod(self, modulo_cod=-1):
        self.__modulo_cod = modulo_cod

    def get_disciplina_cod(self):
        return self.__disciplina_cod

    def set_disciplina_cod(self, disciplina_cod=-1):
        self.__disciplina_cod = disciplina_cod

class Modulo:
    __modulo_cod = -1
    __disciplina_cod = -1

    def __init__(self, modulo_cod=-1, disciplina_cod=-1):
        self.set_modulo_cod(modulo_cod)
        self.set_disciplina_cod(disciplina_cod)

    def get_modulo_cod(self):
        return self.__modulo_cod

    def set_modulo_cod(self, modulo_cod=-1):
        self.__modulo_cod = modulo_cod

    def get_disciplina_cod(self):
        return self.__disciplina_cod

    def set_disciplina_cod(self, disciplina_cod=-1):
        self.__disciplina_cod = disciplina_cod