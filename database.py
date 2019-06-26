import psycopg2

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
			print('Erro ao conectar')
		finally:
			return True if self.__connection else False

	def insert(self, table, values, columns=''):
		if self.__connection:
			values = [(lambda v: "'" + v + "'" if type(v) == str else ''.join(v) if type(v) == list else v)(v) for v in values]
			self.__cursor.execute('insert into ' + table + columns + ' values (' + ''.join(list(''.join([(lambda i: '{}, ')(i) for i in range(len(values))]))[:-2]).format(*values) + ');')
		else:
			print('Erro no insert')
	
	def commit(self):
		if self.__connection:
			self.__connection.commit()
		else:
			print('Erro no commit')

	def init(self):
		if self.__connection:
			self.__cursor.execute(
				'drop table if exists usuarios;' +
				'create table usuarios (matricula integer, senha varchar(10), nome varchar(200), turma char(1), foto oid);'
			)
		else:
			print('Erro no init')
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
