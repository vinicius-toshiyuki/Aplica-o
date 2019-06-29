import psycopg2
from psycopg2 import Error

class CreateSchema():
	__sqlStatement = """
	CREATE TABLE IF NOT EXISTS PROFESSOR (
		COD SERIAL NOT NULL PRIMARY KEY,
		NOME VARCHAR(500) NOT NULL,
		EMAIL VARCHAR(500) NOT NULL UNIQUE,
		SENHA VARCHAR(50) NOT NULL,
		FOTO BYTEA,
		DATA_NASC DATE,
		DATA_CADR TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC+3') NOT NULL
	);

	CREATE TABLE IF NOT EXISTS DISCIPLINA (
		COD SERIAL NOT NULL PRIMARY KEY,
		NOME VARCHAR(500) NOT NULL
	);

	CREATE TABLE IF NOT EXISTS TURMA (
		COD SERIAL NOT NULL,
		SEMESTRE CHAR(5) NOT NULL, -- ex.: 20171
		PROF_COD INTEGER NOT NULL,
		DISC_COD INTEGER NOT NULL,

		PRIMARY KEY (COD, SEMESTRE, DISC_COD),
		FOREIGN KEY (PROF_COD) REFERENCES PROFESSOR(COD),
		FOREIGN KEY (DISC_COD) REFERENCES DISCIPLINA(COD)
	);

	CREATE TABLE IF NOT EXISTS ALUNO (
		MATRICULA DECIMAL(9) NOT NULL PRIMARY KEY,
		NOME VARCHAR(500),
		EMAIL VARCHAR(500) NOT NULL UNIQUE,	
		SENHA VARCHAR(500) NOT NULL,
		FOTO BYTEA,
		DATA_NASC DATE,
		DATA_CADR TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC+3') NOT NULL,

		TURMA_COD INTEGER,
		TURMA_SEMESTRE CHAR(5),
		DISC_COD INTEGER,
		FOREIGN KEY (TURMA_COD, TURMA_SEMESTRE, DISC_COD) REFERENCES TURMA(COD, SEMESTRE, DISC_COD)
	);

	CREATE TABLE IF NOT EXISTS MONITOR_TURMA (
		ALUNO_MATR DECIMAL(9) NOT NULL,
		TURMA_COD INTEGER NOT NULL,
		TURMA_SEMESTRE CHAR(5) NOT NULL,
		DISC_COD INTEGER NOT NULL,

		PRIMARY KEY (ALUNO_MATR, TURMA_COD, TURMA_SEMESTRE, DISC_COD),
		FOREIGN KEY (ALUNO_MATR) REFERENCES ALUNO(MATRICULA),
		FOREIGN KEY (TURMA_COD, TURMA_SEMESTRE, DISC_COD) REFERENCES TURMA(COD, SEMESTRE, DISC_COD)
	);

	CREATE TABLE IF NOT EXISTS LING_PROGR (
		COD SERIAL NOT NULL PRIMARY KEY,
		NOME VARCHAR(500) NOT NULL,
		COMAND_COMPILA VARCHAR(1000) NOT NULL
	);

	CREATE TABLE IF NOT EXISTS LING_PROGR_DISCI (
		LING_PROGR_COD INTEGER NOT NULL,
		DISC_COD INTEGER NOT NULL,

		PRIMARY KEY (LING_PROGR_COD, DISC_COD),
		FOREIGN KEY (LING_PROGR_COD) REFERENCES LING_PROGR(COD),
		FOREIGN KEY (DISC_COD) REFERENCES DISCIPLINA(COD)
	);

	CREATE TABLE IF NOT EXISTS MODULO (
		NUMERO INTEGER NOT NULL,
		DISC_COD INTEGER NOT NULL,

		PRIMARY KEY (NUMERO, DISC_COD),
		FOREIGN KEY (DISC_COD) REFERENCES DISCIPLINA(COD)
	);

	CREATE TABLE IF NOT EXISTS LISTA (
		COD INTEGER NOT NULL,
		DESCR BYTEA NOT NULL,
		DATA_HR_INICIO TIMESTAMP,
		DATA_HR_FIM TIMESTAMP,
		VISIBILIDADE CHAR(1) NOT NULL,
		PROVA CHAR(1) NOT NULL,
		MODULO_COD INTEGER NOT NULL,
		DISC_COD INTEGER,

		PRIMARY KEY (COD, MODULO_COD, DISC_COD),
		FOREIGN KEY (MODULO_COD, DISC_COD) REFERENCES MODULO(NUMERO, DISC_COD)
	);

	CREATE TABLE IF NOT EXISTS PROBLEMA (
		COD INTEGER NOT NULL,
		LISTA_COD INTEGER NOT NULL,
		MODULO_COD INTEGER NOT NULL,
		DISC_COD INTEGER NOT NULL,
		TITULO VARCHAR(300),
		DESCR VARCHAR(4000),
		DIFICUL VARCHAR(50),
		LIMITE_MEM VARCHAR(500),
		LIMITE_TEMP VARCHAR(500),

		PRIMARY KEY (COD, LISTA_COD, MODULO_COD, DISC_COD),
		FOREIGN KEY (LISTA_COD, MODULO_COD, DISC_COD) REFERENCES LISTA(COD, MODULO_COD, DISC_COD)
	);

	CREATE TABLE IF NOT EXISTS ENTRADA (
		COD INTEGER,
		PROBLEMA_COD INTEGER NOT NULL,
		LISTA_COD INTEGER NOT NULL,
		MODULO_COD INTEGER NOT NULL,
		DISC_COD INTEGER NOT NULL,
		ENTRADA VARCHAR(4000) NOT NULL,

		PRIMARY KEY (COD, PROBLEMA_COD, LISTA_COD, MODULO_COD, DISC_COD),
		FOREIGN KEY (PROBLEMA_COD, LISTA_COD, MODULO_COD, DISC_COD) REFERENCES PROBLEMA(COD, LISTA_COD, MODULO_COD, DISC_COD)
	);

	CREATE TABLE IF NOT EXISTS SAIDA (
		COD INTEGER,
		PROBLEMA_COD INTEGER NOT NULL,
		LISTA_COD INTEGER NOT NULL,
		MODULO_COD INTEGER NOT NULL,
		DISC_COD INTEGER NOT NULL,
		SAIDA VARCHAR(4000) NOT NULL,
		
		PRIMARY KEY (COD, PROBLEMA_COD, LISTA_COD, MODULO_COD, DISC_COD),
		FOREIGN KEY (PROBLEMA_COD, LISTA_COD, MODULO_COD, DISC_COD) REFERENCES PROBLEMA(COD, LISTA_COD, MODULO_COD, DISC_COD)
	);

	CREATE TABLE IF NOT EXISTS SUBMISSAO (
		COD INTEGER PRIMARY KEY,
		DATA_HORA TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'UTC+3') NOT NULL,
		CODI_FONTE TEXT NOT NULL,
		MEM_UTILI VARCHAR(4000),
		TEMPO_EXEC VARCHAR(4000),
		VEREDITO VARCHAR(500) NOT NULL,
		ALUNO_MATR DECIMAL(9),
		PROBLEMA_COD INTEGER NOT NULL,
		LISTA_COD INTEGER NOT NULL,
		MODULO_COD INTEGER NOT NULL,
		DISC_COD INTEGER NOT NULL,
		LING_PROGR_COD INTEGER NOT NULL,

		FOREIGN KEY (ALUNO_MATR) REFERENCES ALUNO(MATRICULA),
		FOREIGN KEY (PROBLEMA_COD, LISTA_COD, MODULO_COD, DISC_COD) REFERENCES PROBLEMA(COD, LISTA_COD, MODULO_COD, DISC_COD),
		FOREIGN KEY (LING_PROGR_COD) REFERENCES LING_PROGR(COD)
	);
	"""

	def getCommand(self):
		return self.__sqlStatement

class DropSchema:
	__sqlStatement = """
	DROP TABLE IF EXISTS PROFESSOR CASCADE;
	DROP TABLE IF EXISTS DISCIPLINA CASCADE;
	DROP TABLE IF EXISTS TURMA CASCADE;
	DROP TABLE IF EXISTS ALUNO CASCADE;
	DROP TABLE IF EXISTS MONITOR_TURMA CASCADE;
	DROP TABLE IF EXISTS LING_PROGR CASCADE;
	DROP TABLE IF EXISTS LING_PROGR_DISCI CASCADE;
	DROP TABLE IF EXISTS MODULO CASCADE;
	DROP TABLE IF EXISTS LISTA CASCADE;
	DROP TABLE IF EXISTS PROBLEMA CASCADE;
	DROP TABLE IF EXISTS ENTRADA CASCADE;
	DROP TABLE IF EXISTS SAIDA CASCADE;
	DROP TABLE IF EXISTS SUBMISSAO CASCADE;
	"""
	def getCommand(self):
		return self.__sqlStatement

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
		'matricula' : 'matricula',
		'nome' : 'nome',
		'email' : 'email',
		'senha' : 'senha',
		'foto' : 'foto',
		'data_de_nascimento' : 'data_nasc',
		'data_de_cadastro' : 'data_cadr',
		'turma' : 'turma_cod',
		'disciplina' : 'disc_cod',
		'codigo' : 'cod',
		'matricula_do_monitor' : 'aluno_matr',
		'numero' : 'numero',
		'descrição' : 'descr',
		'descricao' : 'descr',
		'modulo' : 'modulo_cod',
		'inicio' : 'data_hr_inicio',
		'fim' : 'data_hr_fim',
		'visibilidade' : 'visibilidade',
		'description' : 'descr',
		'begin' : 'data_hr_inicio',
		'end' : 'data_hr_fim',
		'number' : 'numero',
		'prova' : 'prova',
		'dificuldade' : 'dificul',
		'titulo' : 'titulo',
		'lista' : 'lista_cod',
		'limite_de_memoria' : 'limite_mem',
		'limite_de_tempo' : 'limite_temp',
		'tudo' : '*'
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
			'PROBLEMA'
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
				elif not full or list(kwargs.keys())[0] != None:
					where = ' where {};'.format(kwargs[k])
				else:
					where = ';'
				query = 'select {} from {}'+where
				query = query.format(resultados, t)
				print(query)
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
			if res:
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
		tabelas = {'PROBLEMA'}
		return self.__get(get=get, table=tabelas, full=full, **kwargs)

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
		self.execute(
				'CREATE OR REPLACE VIEW LINGUAGEM_DAS_DISCIPLINAS AS	(SELECT COD, NOME, COMAND_COMPILA, DISC_COD FROM LING_PROGR JOIN LING_PROGR_DISCI ON LING_PROGR_COD  = COD);'
				)
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







