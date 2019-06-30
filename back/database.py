import psycopg2
from psycopg2 import Error

class BD:
	_connection = None
	_cursor = None
	def __init__(self):
		pass

	def connect(self, user='postgres', password='root', host='127.0.0.1', port='5432', database='corretor'):
		try:
			self._connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)
			self._cursor = self._connection.cursor()
		except (Exception, psycopg2.Error) as error:
			print('Erro ao conectar no banco de dados', error)
		finally:
			return True if self._connection else False

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
		'tudo'                 : '*'
	}
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
			self.execute(query, list(kwargs.values()))
		except Exception as e:
			print(e)
			raise ValueError('Invalid data in insert_aluno')
		finally:
			f.close()
			self.commit()

	def insert_professor(self, **kwargs):
		f = open(kwargs['foto'], 'rb')
		foto = f.read()
		kwargs['foto'] = foto

		try:
			colunas = []
			for k in kwargs: colunas.append(self.__alias[k])
			colunas = ', '.join(colunas)
			valores = ', '.join(['%s'] * len(kwargs))

			query = 'insert into PROFESSOR ({}) values ({});'.format(colunas, valores)
			self.execute(query, list(kwargs.values()))
		except Exception as e:
			print(e)
			raise ValueError('Invalid data in insert_professor')
		finally:
			f.close()
			self.commit()

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
			'PROBLEMAS_COMPLETOS'
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
			self.execute('INSERT INTO LING_PROGR_DISCI (SELECT {}, {} FROM LING_PROGR_DISCI WHERE (SELECT COUNT(*) FROM LING_PROGR_DISCI WHERE DISC_COD = {} AND LING_PROGR_COD = {}) = 0) LIMIT 1;'.format(language_code, course_code, course_code, language_code))
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
















