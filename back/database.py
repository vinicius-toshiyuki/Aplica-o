import psycopg2
import back.entidades
from back.entidades import *
from psycopg2 import Error
from datetime import *

class BD:
	_connection = None
	_cursor = None
	def __init__(self):
		pass

	def connect(self, user='postgres', password='root', host='127.0.0.1', port='5432', database='postgres'):
		try:
			self._connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)
			self._cursor = self._connection.cursor()
		except (Exception, psycopg2.Error) as error:
			print('Erro ao conectar no banco de dados', error)
		finally:
			return True if self._connection else False

	def close(self):
		self._cursor.close()

	def insert(self, table, values, columns=''):
		if self._connection:
			values = [(lambda v: "'" + v + "'" if type(v) == str else ''.join(v) if type(v) == list else v)(v) for v in values]
			self._cursor.execute('insert into ' + table + columns + ' values (' + ''.join(list(''.join([(lambda i: '{}, ')(i) for i in range(len(values))]))[:-2]).format(*values) + ');')
		else:
			print('Erro no insert')

	def select(self, values, table, where=''):
		if self._connection:
			self._cursor.execute('select '+values+' from '+table+(' where '+where if len(where) else '') +' ;')
		else:
			print('Erro no select')
	
	def fetchone(self):
		return self._cursor.fetchone()

	def fetchall(self):
		return self._cursor.fetchall()
	
	def commit(self):
		if self._connection:
			self._connection.commit()
		else:
			print('Erro no commit')

	def execute(self, *args):
		if self._connection:
			self._cursor.execute(*args)
		else:
			print('Erro no execute')

class Corretor(BD):
	def __init__(self):
		super(Corretor, self).__init__()

	__alias = {
		'matricula'            : 'matricula',
		'nome'                 : 'nome',
		'email'                : 'email',
		'senha'                : 'senha',
		'foto'                 : 'foto',
		'data_de_nascimento'   : 'data_nasc',
		'data_de_cadastro'     : 'data_cadr',
		'turma'                : 'turma_cod',
		'disciplina'           : 'disc_cod',
		'codigo'               : 'cod',
		'matricula_do_monitor' : 'aluno_matr',
		'numero'               : 'numero',
		'descrição'            : 'descr',
		'descricao'            : 'descr',
		'modulo'               : 'modulo_cod',
		'inicio'               : 'data_hr_inicio',
		'fim'                  : 'data_hr_fim',
		'visibilidade'         : 'visibilidade',
		'description'          : 'descr',
		'begin'                : 'data_hr_inicio',
		'end'                  : 'data_hr_fim',
		'number'               : 'numero',
		'prova'                : 'prova',
		'dificuldade'          : 'dificul',
		'titulo'               : 'titulo',
		'lista'                : 'lista_cod',
		'limite_de_memoria'    : 'limite_mem',
		'limite_de_tempo'      : 'limite_temp',
		'arquivo'              : 'arquivo',
		'tempo'                : 'tempo_exec',
		'memoria'              : 'mem_utili',
		'veredito'             : 'veredito',
		'aluno'                : 'aluno_matr',
		'linguagem'            : 'ling_progr_cod',
		'problema'             : 'problema_cod',
		'professor'            : 'prof_cod',
		'semestre'             : 'semestre',
		'turma_semestre'	   : 'turma_semestre',
		'tudo'                 : '*'
	}

	def get_aluno(self, matricula):
		try:
			query = "SELECT * FROM ALUNO WHERE matricula = %s;"
			self.connect(database='corretor')
			self.execute(query, (matricula,))
			aluno_dados = self.fetchall()[0]
			aluno = Aluno(aluno_dados[0],aluno_dados[1],aluno_dados[2],aluno_dados[3],
						  aluno_dados[4],aluno_dados[5],aluno_dados[6],aluno_dados[7],
						  aluno_dados[8])
		except Exception as e:
			print(e)
			raise ValueError('Invalid data in get_aluno')
		finally:
			self.commit()
			self.close()
			return aluno

	def insert_aluno(self, **kwargs):
		f = open(kwargs['foto'], 'rb')
		foto = f.read()
		kwargs['foto'] = foto

		try:
			colunas = []
			for k in kwargs: colunas.append(self.__alias[k])
			colunas = ', '.join(colunas)
			valores = ', '.join(['%s'] * len(kwargs))

			query = 'insert into ALUNO ({}) values ({});'.format(colunas, valores)
			self.connect(database='corretor')
			self.execute(query, list(kwargs.values()))
		except Exception as e:
			print(e)
			raise ValueError('Invalid data in insert_aluno')
		finally:
			f.close()
			self.commit()
			self.close()

	def update_aluno(self, matricula, nome, email, senha, foto, data_de_nascimento, turma_cod, turma_semestre, disciplina):
		f = open(foto, 'rb')
		foto_arq = f.read()

		try:
			query = 'UPDATE Aluno SET Nome=%s,Email=%s,Senha=%s,Foto=%s,Data_Nasc=%s,Turma_Cod=%s,Turma_Semestre=%s,Disc_Cod=%s WHERE matricula=%s;'
			self.connect(database='corretor')
			self.execute(query, (nome, email, senha, foto_arq, data_de_nascimento, turma_cod, turma_semestre, disciplina, matricula))
		except Exception as e:
			print(e)
			raise ValueError('Invalid data in update_professor')
		finally:
			f.close()
			self.commit()
			self.close()

	def delete_aluno(self, matricula):
		try:
			query = "DELETE FROM ALUNO WHERE matricula = %s"
			self.connect(database='corretor')
			self.execute(query, (matricula,))
		except Exception as e:
			print(e)
			raise ValueError('Invalid data in delete_professor')
		finally:
			self.commit()
			self.close()

	def get_professor(self, cod):
		try:
			query = "SELECT * FROM PROFESSOR WHERE cod = %s;"
			self.connect(database='corretor')
			self.execute(query, (cod,))
			aluno_dados = self.fetchall()[0]
			professor = Professor(aluno_dados[0],aluno_dados[1],aluno_dados[2],aluno_dados[3],
								  aluno_dados[4],aluno_dados[5],aluno_dados[6])
		except Exception as e:
			print(e)
			raise ValueError('Invalid data in get_professor')
		finally:
			self.commit()
			self.close()
			return professor

	def insert_professor(self, **kwargs):
		f = open(kwargs['foto'], 'rb')
		foto = f.read()
		kwargs['foto'] = foto

		try:
			colunas = []
			for k in kwargs: colunas.append(self.__alias[k])
			colunas = ', '.join(colunas)
			valores = ', '.join(['%s'] * len(kwargs))

			query = 'insert into PROFESSOR ({}) values ({}) returning cod;'.format(colunas, valores)
			self.connect(database='corretor')
			self.execute(query, list(kwargs.values()))
			cod = self.fetchone()[0]
			return cod
		except Exception as e:
			print(e)
			raise ValueError('Invalid data in insert_professor')
		finally:
			f.close()
			self.commit()
			self.close()

	def update_professor(self, cod, nome, email, senha, foto, data_de_nascimento):
		f = open(foto, 'rb')
		foto_arq = f.read()

		try:
			query = 'UPDATE PROFESSOR SET Nome=%s,Email=%s,Senha=%s,Foto=%s,Data_Nasc=%s WHERE cod=%s;'
			self.connect(database='corretor')
			self.execute(query, (nome, email, senha, foto_arq, data_de_nascimento, cod))
		except Exception as e:
			print(e)
			raise ValueError('Invalid data in update_professor')
		finally:
			f.close()
			self.commit()
			self.close()

	def delete_professor(self, Cod):
		try:
			query = "DELETE FROM PROFESSOR WHERE cod = %s"
			self.connect(database='corretor')
			self.execute(query, (Cod,))
		except Exception as e:
			print(e)
			raise ValueError('Invalid data in delete_professor')
		finally:
			self.commit()
			self.close()

	def get_professor_cod(self, email):
		try:
			query = "SELECT cod FROM PROFESSOR WHERE email = %s"
			self.connect(database='corretor')
			self.execute(query, (email,))
			cod = self.fetchone()[0]
			return cod
		except Exception as e:
			print(e)
			raise ValueError('Invalid data in get_professor_cod')
		finally:
			self.commit()
			self.close()

	def insert_work(self, **kwargs):
		f = open(kwargs['Description'], 'rb')
		fbytes = f.read()
		kwargs['Description'] = fbytes

		try:
			colunas = []
			for k in kwargs: colunas.append(self.__alias[k.lower()])
			colunas = ', '.join(colunas)
			valores = ', '.join(['%s'] * len(kwargs))

			query = 'insert into LISTA ({}) values ({});'.format(colunas, valores)
			self.execute(query, list(kwargs.values()))
		except Exception as e:
			print(e)
			raise ValueError('Invalid data in insert_work')
		finally:
			f.close()
			self.commit()
			
	def insert_problem(self, **kwargs):
		try:
			colunas = []
			for k in kwargs: colunas.append(self.__alias[k.lower()])
			colunas = ', '.join(colunas)
			valores = ', '.join(['%s'] * len(kwargs))

			query = 'insert into PROBLEMA ({}) values ({});'.format(colunas, valores)
			self.execute(query, list(kwargs.values()))
		except Exception as e:
			print(e)
			raise ValueError('Invalid data in insert_problem')
		finally:
			self.commit()

	# kwargs é o que vai ser usado pra buscar
	def __get(self, get='tudo', table=None, full=False, **kwargs):
		# Criar umas views pra não deixar pegar senha e tal
		if type(get) == str: get = [get]
		tabelas = {
			'PROFESSOR',
			'ALUNO',
			'DISCIPLINA',
			'MODULO',
			'LINGUAGEM_DAS_DISCIPLINAS',
			'LING_PROGR',
			'LISTA',
			'PROBLEMA',
			'PROBLEMAS_COMPLETOS',
			'SUBMISSAO',
			'TURMA'
		}
		if table != None:
			tabelas = tabelas - (tabelas - table)

		if not len(tabelas): raise ValueError('You can not access these tables')

		res = None
		if not len(kwargs):
			full = True
			kwargs[None] = None
		if full:
			res = []
		resultados = ', '.join([(lambda g: self.__alias[g])(g) for g in get])
		for t in tabelas:
			for k in kwargs:
				if k in self.__alias:
					where = ' where {} = %s;'.format(self.__alias[k])
				elif kwargs[k] != '' and (not full or list(kwargs.keys())[0] != None):
					where = ' where {};'.format(kwargs[k])
				else:
					where = ';'
				query = 'select {} from {}'+where
				query = query.format(resultados, t)
				try:
					self.execute(query, (kwargs[k],))
					if not full:
						res = self.fetchone()
						if res:
							break
					else:
						aux = self.fetchall()
						res += aux if len(aux) else []
				except:
					self.commit()
			if res and not full:
				break
		return res

	# Acho que dá pra fazer com o get
	def is_tutor(self, matricula):
		query = 'select * from MONITOR_TURMA where aluno_matr = {}'
		res = False
		try:
			matricula = str(matricula)
			if not matricula.isdigit():
				raise ValueError('Invalid register nº')
			query = query.format(matricula)
			self.execute(query)
			r = self.fetchone()
			if r: res = True
		except Exception as e:
			print(e)
		return res

	def change_password(self, email, senha):
		tabelas = 'PROFESSOR','ALUNO'
		ret = False
		for t in tabelas:
			query = "update {} set senha = '{}' where email = '{}';"
			query = query.format(t, senha, email)
			try:
				self.execute(query)
				ret = True
				self.commit()
			except Exception as e:
				print(e)
				self.commit()
		return ret

	def __diff_tables(self, t1, t2):
		if t2 != None:
			try:
				if type(t2) != str:
					iter(t2)
					t2 = set(t2)
			except:
				pass
			if type(t2) != set:
				t2 = {t2}
			t1 = t1 - (t1 - t2)
		return t1

	def get_users(self, get='tudo', table=None, full=False, **kwargs):
		tabelas = {'PROFESSOR', 'ALUNO'}
		tabelas = self.__diff_tables(tabelas, table)
	
		return self.__get(get=get, table=tabelas, full=full, **kwargs)

	def get_courses(self, get='tudo', full=True, **kwargs):
		tabelas = {'DISCIPLINA'}
		return self.__get(get=get, table=tabelas, full=full, **kwargs)
	
	def get_modules(self, get='tudo', full=True, **kwargs):
		tabelas = {'MODULO'}
		return self.__get(get=get, table=tabelas, full=full, **kwargs)

	def get_work(self, get='tudo', full=True, **kwargs):
		tabelas = {'LISTA'}
		where = []
		for k in kwargs:
			where.append('{} = {}'.format(self.__alias[k], kwargs[k]))
		where = ' and '.join(where)
		return self.__get(get=get, table=tabelas, full=full, where=where)

	def get_problem(self, get='tudo', full=True, **kwargs):
		tabelas = {'PROBLEMAS_COMPLETOS'}
		where = []
		for k in kwargs:
			where.append('{} = {}'.format(self.__alias[k], kwargs[k]))
		where = ' and '.join(where)
		return self.__get(get=get, table=tabelas, full=full, where=where)

	def insert_disciplina(self, name):
		try:
			self.execute('insert into DISCIPLINA (nome) values (%s);', (name,))
		except Exception as e:
			print(e)
			raise ValueError('Error in insert_disciplina')
		finally:
			self.commit()

	def insert_language(self, name, compilation):
		try:
			self.execute('INSERT INTO LING_PROGR (NOME, COMAND_COMPILA) VALUES(%s, %s);', (name, compilation))
		except Exception as e:
			print(e)
			raise ValueError('Error in insert_language')
		finally:
			self.commit()

	def get_languages(self, get='tudo', full=True, **kwargs):
		tabelas = {'LINGUAGEM_DAS_DISCIPLINAS'}
		return self.__get(get=get, table=tabelas, full=full, **kwargs)

	def get_language_options(self, get='tudo', full=True, **kwargs):
		return self.__get(get=get, table={'LING_PROGR'}, full=full, **kwargs)

	def get_attempts(self, get='tudo', full=True, **kwargs):
		return self.__get(get=get, table={'SUBMISSAO'}, full=full, **kwargs)

	def get_classes(self, get='tudo', full=True, **kwargs):
		return self.__get(get=get, table={'TURMA'}, full=full, **kwargs)

	def get_nota(self, email):
		self.execute('select nota(%s);', (email,))
		return self.fetchone()[0]

	def insert_module(self, number, course_code):
		try:
			self.execute('INSERT INTO MODULO VALUES (%s, %s);', (number, course_code))
		except Exception as e:
			print(e)
			raise ValueError('Error in insert_module')
		finally:
			self.commit()

	def choose_language(self, course_code, language_code):
		try:
			self.execute('INSERT INTO LING_PROGR_DISCI (SELECT {}, {} FROM (SELECT 1,1) NADA WHERE (SELECT COUNT(*) FROM LING_PROGR_DISCI WHERE DISC_COD = {} AND LING_PROGR_COD = {}) = 0) LIMIT 1;'.format(language_code, course_code, course_code, language_code))
		except Exception as e:
			raise ValueError(e)
		finally:
			self.commit()

	def toggle_visibilitiy(self, course_code, module_number, work_code):
		return self.__toggle(course_code, module_number, work_code, 'VISIBILIDADE')

	def toggle_contest(self, course_code, module_number, work_code):
		return self.__toggle(course_code, module_number, work_code, 'PROVA')

	def __toggle(self, course_code, module_number, work_code, table):
		ret = False
		try:
			self.execute(
					'UPDATE LISTA SET {} = TOGGLE_{}(%s, %s, %s) WHERE DISC_COD = %s AND MODULO_COD = %s AND COD = %s;'.format(table, table),
					(course_code, module_number, work_code, course_code, module_number, work_code)
					)
			self.execute(
					'SELECT {} FROM LISTA WHERE DISC_COD = %s AND MODULO_COD = %s AND COD = %s;'.format(table),
					(course_code, module_number, work_code)
					)
			ret = True if self.fetchone()[0] == 'S' else False
		except Exception as e:
			raise ValueError(e)
		finally:
			self.commit()
		return ret
	
	def delete_problem(self, course_code, module_number, work_code, problem_code):
		try:
			self.execute(
					'DELETE FROM PROBLEMA WHERE DISC_COD = %s AND MODULO_COD = %s AND LISTA_COD = %s AND COD = %s;',
					(course_code, module_number, work_code, problem_code)
					)
		except Exception as e:
			print(e)
			raise ValueError('Can not delete a problem with a submission')
		finally:
			self.commit()

	def insert_file(self, **kwargs):
		try:
			file = open(kwargs['arquivo'], 'rb')
			kwargs['arquivo'] = file.read()

			tabela = kwargs.pop('tabela')
			colunas = ', '.join([(lambda k: self.__alias[k])(k) for k in kwargs])
			valores = ', '.join(['%s'] * len(kwargs))
			query = 'insert into {} ({}) values ({});'.format(tabela, colunas, valores)
			self.execute(query, list(kwargs.values()))
		except Exception as e:
			self.commit()
			raise ValueError(e)
		finally:
			file.close()
	
	def insert_class(self, classname, professor, course):
		semestre = datetime.now()
		semestre = '{}{}'.format(semestre.year, 1 if semestre else 2)
		try:
			self.execute(
					'insert into TURMA values (%s, {}, %s, %s);'.format(semestre),
					(classname, professor.split(' - ')[0], course.split(' - ')[0])
					)
		except Exception as e:
			raise ValueError(e)
		finally:
			self.commit()

class ProfessorBD(Corretor):
	def __init__(self):
		super(ProfessorBD, self).__init__()

	def _getProfessor(self, cod):
		professor = self.get_professor(cod)
		return professor


	def _insertProfessor(self, Professor=None):
		cod = self.insert_professor(nome=Professor.get_nome(), email=Professor.get_email(),
                            	senha=Professor.get_senha(), foto=Professor.get_foto(),
								data_de_nascimento=Professor.get_dataNascimento())
		return cod

	def _updateProfessor(self, Professor=None):
		self.update_professor(cod=Professor.get_professor_cod(), nome=Professor.get_nome(), email=Professor.get_email(),
                            	senha=Professor.get_senha(), foto=Professor.get_foto(),
								data_de_nascimento=Professor.get_dataNascimento())

	def _deleteProfessor(self, cod):
		self.delete_professor(cod)

	def _getProfessorCod(self, email):
		cod = self.get_professor_cod(email)
		return cod



class AlunoBD(Corretor):
	def __init__(self):
		super(AlunoBD, self).__init__()

	def _getAluno(self, cod):
		Aluno = self.get_aluno(cod)
		return Aluno


	def _insertAluno(self, Aluno=None):
		self.insert_aluno(matricula=Aluno.get_matricula(),nome=Aluno.get_nome(), email=Aluno.get_email(),
                            	senha=Aluno.get_senha(), foto=Aluno.get_foto(),
								data_de_nascimento=Aluno.get_dataNascimento(), 
								turma=Aluno.get_turma_cod(), turma_semestre=Aluno.get_turma_semestre(),
								disciplina=Aluno.get_disciplina_cod())

	def _updateAluno(self, Aluno=None):
		self.update_aluno(matricula=Aluno.get_matricula(), nome=Aluno.get_nome(), email=Aluno.get_email(),
                            	senha=Aluno.get_senha(), foto=Aluno.get_foto(),
								data_de_nascimento=Aluno.get_dataNascimento(),
								turma_cod=Aluno.get_turma_cod(), turma_semestre=Aluno.get_turma_semestre(),
								disciplina=Aluno.get_disciplina_cod())

	def _deleteAluno(self, cod):
		self.delete_aluno(cod)

	def _getAlunoCod(self, email):
		cod = self.get_aluno_cod(email)
		return cod
