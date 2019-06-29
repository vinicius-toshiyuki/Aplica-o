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
	__connection = None
	__cursor = None
	cursor = None
	def __init__(self):
		pass

	def connect(self, user='postgres', password='root', host='127.0.0.1', port='5432', database='corretor'):
		try:
			self.__connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)
			self.__cursor = self.__connection.cursor()
			self.cursor = self.__cursor
		except (Exception, psycopg2.Error) as error:
			print('Erro ao conectar no banco de dados', error)
		finally:
			return True if self.__connection else False

	def insert(self, table, values, columns=''):
		if self.__connection:
			values = [(lambda v: "'" + v + "'" if type(v) == str else ''.join(v) if type(v) == list else v)(v) for v in values]
			self.__cursor.execute('insert into ' + table + columns + ' values (' + ''.join(list(''.join([(lambda i: '{}, ')(i) for i in range(len(values))]))[:-2]).format(*values) + ');')
		else:
			print('Erro no insert')

	def select(self, values, table, where=''):
		if self.__connection:
			self.__cursor.execute('select '+values+' from '+table+(' where '+where if len(where) else '') +' ;')
		else:
			print('Erro no select')
	
	def fetchone(self):
		return self.__cursor.fetchone()

	def fetchall(self):
		return self.__cursor.fetchall()
	
	def commit(self):
		if self.__connection:
			self.__connection.commit()
		else:
			print('Erro no commit')

	def execute(self, query):
		if self.__connection:
			self.__cursor.execute(query)
		else:
			print('Erro no execute')

'''
from PIL import Image
import base64
from io import BytesIO
p = '/home/vinicius/Downloads/samsung galaxy s10 wallpaper 5.png'
bd = BD()
bd.connect()
bd.init()
img = list('lo_import(\''+p+'\')')
bd.insert('usuarios', (170023664, '123456', 'Vinícius Toshiyuki', 'Z', img))
bd.commit()
# TODO: tirar esse cursor aí
bd.cursor.execute('select lo_export(foto, \'/tmp/pim.jpg\') from usuarios;')
im = Image.open('/tmp/pim.jpg')
im.show()
'''
