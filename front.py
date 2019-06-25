from tkinter import *
from tkinter import messagebox as TkMessageBox
from login import *
from home import *
from register import *

class App:
	window = Tk()
	def __init__(self, title='', icon=None):
		self.title = title
		self.icon = icon

		# Retorno das janelas
		self.ret = [None]

		# Cria handler para retornos
		# TODO: tem que tratar pra autenticar mesmo e tal
		self.handler = {
			None : lambda: LogInScreen(icon=self.icon, title=self.title + ' - Autenticação').start(),
			'autenticate': lambda: HomeScreen(self.ret[1], self.ret[2], icon=self.icon, title=self.title + ' - Página Inicial').start(),
			'register' : lambda: RegisterScreen(self.ret[1], self.ret[2], title=self.title, icon=self.icon).start(),
			'logout': lambda: self.handler[None]()
		}
	def start(self):
		while True:
			self.ret = self.handler[self.ret[0]]()

app = App(icon='índice.gif', title='Corretor')
app.start()






















