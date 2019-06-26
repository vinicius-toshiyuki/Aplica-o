from tkinter import *
from tkinter import messagebox as TkMessageBox
from app import App

class LogInScreen(App):
	def __init__(self, title='', icon=None, geometry='400x250'):
		self.title = title
		self.icon = icon
		self.geometry = geometry

		# Cria janela
		self.window.title(self.title)
		# Configura ícone da janela
		if self.icon != None:
			self.windowicon = PhotoImage(file=''+self.icon)
			self.window.tk.call('wm', 'iconphoto', self.window._w, self.windowicon)
		# Configura tamanho da janela (largura x altura)
		self.window.geometry(self.geometry)

		# Cria frame da tela de login
		self.loginFrame = Frame(self.window)

		# Cria frames na janela para nome de usuário, senha e botão de autenticar
		self.usernameFrame = Frame(self.loginFrame)
		self.passwordFrame = Frame(self.loginFrame)
		self.buttonFrame   = Frame(self.loginFrame)
		self.usernameFrame.pack()
		self.passwordFrame.pack()
		self.buttonFrame.pack()

		# Cria campo de entrada para usuário na frame de usuário
		self.usernameLabel = Label(self.usernameFrame, text='Username')
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
		self.loginButton.pack()
		self.registerButton.pack()
	def autenticate(self, event=None):
		username = self.usernameInput.get()
		password = self.passwordInput.get()
		if not len(username) or not len(password):
			TkMessageBox.showinfo('Error', 'Invalid username or password')
		else:
			print('-- READ --\nUsername: ', username + '\nPassword: ', password)
			# self.screen = ['autenticate', username, password]
			self.screen.clear()
			self.screen += ['autenticate', username, password]
			self.stop()
	def register(self):
		username = self.usernameInput.get()
		password = self.passwordInput.get()
		if not len(username) or not len(password):
			TkMessageBox.showinfo('Error', 'Invalid username or password')
		else:
			print('-- CREATE --\nUsername: ', username + '\nPassword: ', password)
			self.screen.clear()
			self.screen += ['register', username, password]
			self.stop()
	def stop(self):
			self.loginFrame.pack_forget()
			self.end.acquire()
			self.end.notify()
			self.end.release()
	def start(self):
		self.loginFrame.pack()


