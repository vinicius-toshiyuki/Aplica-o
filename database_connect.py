import psycopg2

class BD:
	__connection = None
	__cursor = None
	def __init__(self):
		pass

	def connect(self, user='postgres', password='root', host='127.0.0.1', port='5432', database='corretor'):
		try:
			self.__connection = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)
			self.__cursor = self.__connection.cursor()
		except (Exception, psycopg2.Error) as error:
			print('Erro ao conectar')
		finally:
			return self.__connection if self.__connection else None

	def insert(self, table, values, columns=''):
		self.__cursor.execute('insert into ' + table + columns + ' ' + ''.join(list(''.join([(lambda i: '{}, ')(i) for i in range(len(values))]))[:-2]) + ');'.format(*values))
		
bd = BD()
bd.connect()
bd.insert('tabela', ('nome', 15))
