from tkinter import *
from tkinter import messagebox as TkMessageBox
from PIL import Image
from front.app import App

class LogInScreen(App):
	def __init__(self, title='', icon=None, geometry='400x250'):
		self._init(title, icon, geometry)

		# Cria frames na janela para nome de usuário, senha e botão de autenticar
		self.usernameFrame = Frame(self.screenFrame)
		self.passwordFrame = Frame(self.screenFrame)
		self.buttonFrame   = Frame(self.screenFrame)
		self.usernameFrame.pack()
		self.passwordFrame.pack()
		self.buttonFrame.pack()

		# Cria campo de entrada para usuário na frame de usuário
		self.usernameLabel = Label(self.usernameFrame, text='Register nº')
		self.usernameInput = Entry(self.usernameFrame)
		self.usernameInput.bind('<Return>', self.autenticate)
		self.usernameInput.focus_set()
		self.usernameLabel.pack(side=LEFT)
		self.usernameInput.pack(side=RIGHT)

		# Cria campo de entrada para senha na frame de senha
		self.passwordLabel = Label(self.passwordFrame, text='Password')
		self.passwordInput = Entry(self.passwordFrame, show='*')
		self.passwordInput.bind('<Return>', self.autenticate)
		self.passwordLabel.pack(side=LEFT)
		self.passwordInput.pack(side=RIGHT)

		# Cria botões para autenticar e registrar
		self.loginButton    = Button(self.buttonFrame, text='Autenticate', command=self.autenticate)
		self.registerButton = Button(self.buttonFrame, text='Register', relief=FLAT, command=self.register)
		self.loginButton.bind('<Return>', self.autenticate)
		self.registerButton.bind('<Return>', self.register)
		self.loginButton.pack()
		self.registerButton.pack()
	def autenticate(self, event=None):
		username = self.usernameInput.get()
		password = self.passwordInput.get()
		if not len(username) or not len(password):
			TkMessageBox.showinfo('Error', 'Invalid username or password')
		else:
			print('-- READ --\nUsername: ', username + '\nPassword: ', password)
					# TODO: fazer em um select só
			self.db.select('cod, senha', 'PROFESSOR', where='cod = '+username)
			userInfo = self.db.fetchone()
			if userInfo and str(userInfo[0]) == username and userInfo[1] == password:
				self.db.select('lo_export(foto, \'/tmp/profilepic\')', 'PROFESSOR', where='cod = '+username)
				self.stop(['home', username, password, 'admin'])
			else:
				self.db.select('matricula, senha', 'ALUNO', where='matricula = '+username)
				userInfo = self.db.fetchone()
				if userInfo and str(userInfo[0]) == username and userInfo[1] == password:
					self.db.select('lo_export(foto, \'/tmp/profilepic\')', 'ALUNO', where='matricula = '+username)
					self.db.select('*', 'MONITOR_TURMA', where='aluno_matr = '+str(userInfo[0]))
					userPrivilege = self.db.fetchone()
					self.stop(['home', username, password, 'admin' if userPrivilege else 'common'])
				else:
					TkMessageBox.showinfo('Error', 'Invalid username or password')
	def register(self, event=None):
		username = self.usernameInput.get()
		password = self.passwordInput.get()
		if not len(username) or not len(password):
			TkMessageBox.showinfo('Error', 'Invalid username or password')
		else:
			print('-- CREATE --\nRegister nº: ', username + '\nPassword: ', password)
			self.stop(['register', username, password])
