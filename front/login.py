from tkinter import *
from tkinter import messagebox as TkMessageBox
from PIL import Image
from front.app import App

class LogInScreen(App):
	def __init__(self, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)

		self.fields = {}
		fieldsNames = ('Register nº', 'Password')
		for i,f in enumerate(fieldsNames):
			self.fields[f] = (
						Label(self.screenFrame, text=f, bd = 7),
						Entry(self.screenFrame)
						)
			self.fields[f][0].grid(row=i, column=0)
			self.fields[f][1].grid(row=i, column=1)
			self.fields[f][1].bind('<Return>', self.__autenticate)
		
		self.fields['Register nº'][1].focus_set()
		self.fields['Password'][1].config(show='*')

		self.buttons = {}
		buttonsNames = (('Log in',self.__autenticate),('Register',self.__register))
		for b in buttonsNames:
			self.buttons[b[0]] = Button(self.screenFrame, text=b[0], pady=7, command=b[1])
			self.buttons[b[0]].bind('<Return>', b[1])
			self.buttons[b[0]].grid()

		self.buttons['Register'].config(relief=FLAT)

	def __autenticate(self, event=None):
		registern = self.fields['Register nº'][1].get()
		password = self.fields['Password'][1].get()

		try:
			if not len(registern) or not len(password) or not registern.isdigit():
				raise ValueError('Invalid register nº or password')
			# TODO: Dá pra fazer um arquivo com funções pra interagirem com o banco e aí ter uma função pra ver se um usuário existe
			self.db.select('cod, senha', 'PROFESSOR', where='cod = '+registern)
			userInfo = self.db.fetchone()
			if userInfo:
				privilege = 'admin'
				table=('PROFESSOR','cod')
			else:
				self.db.select('matricula, senha', 'ALUNO', where='matricula = '+registern)
				userInfo = self.db.fetchone()
				if userInfo:
					self.db.select('*', 'MONITOR_TURMA', where='aluno_matr = '+registern)
					if self.db.fetchone():
						privilege = 'admin'
					else:
						privilege = 'common'
					table = ('ALUNO','matricula')
				else:
					raise ValueError('User not registered')

			if str(userInfo[0]) == registern and userInfo[1] == password:
				self.db.select('lo_export(foto, \'/tmp/profilepic\')', table[0], where=table[1]+' = '+registern)
				self._stop(['home', registern, password, privilege])
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'Invalid register nº or password')
		finally:
			pass

	def __register(self, event=None):
		registern = self.fields['Register nº'][1].get()
		password = self.fields['Password'][1].get()
		self._stop(['register', registern, password])
