from tkinter import *
from tkinter import messagebox as TkMessageBox

class LogInScreen:
	def __init__(self, title='', icon=None, geometry='400x250'):
		self.title = title
		self.icon = icon
		self.geometry = geometry

		# Cria janela
		self.window = Tk()
		self.window.title(self.title)
		# Configura ícone da janela
		if self.icon != None:
			windowicon = PhotoImage(file=''+self.icon)
			self.window.tk.call('wm', 'iconphoto', self.window._w, windowicon)
		# Configura tamanho da janela (largura x altura)
		self.window.geometry(self.geometry)


		# Cria frames na janela para nome de usuário, senha e botão de autenticar
		self.usernameFrame = Frame(self.window)
		self.passwordFrame = Frame(self.window)
		self.buttonFrame   = Frame(self.window)
		self.usernameFrame.pack()
		self.passwordFrame.pack()
		self.buttonFrame.pack()

		# Cria campo de entrada para usuário na frame de usuário
		self.usernameLabel = Label(self.usernameFrame, text='Username')
		self.usernameInput = Entry(self.usernameFrame)
		self.usernameInput.focus_set()
		self.usernameLabel.pack(side=LEFT)
		self.usernameInput.pack(side=RIGHT)

		# Cria campo de entrada para senha na frame de senha
		self.passwordLabel = Label(self.passwordFrame, text='Password')
		self.passwordInput = Entry(self.passwordFrame, show='*')
		self.passwordLabel.pack(side=LEFT)
		self.passwordInput.pack(side=RIGHT)

		# Cria botões para autenticar e registrar
		self.loginButton    = Button(self.buttonFrame, text='Autenticate', command=self.autenticate)
		self.registerButton = Button(self.buttonFrame, text='Register', relief=FLAT, command=self.register)
		self.loginButton.pack()
		self.registerButton.pack()

		# Configura valor de retorno para quando a janela for destruída
		self.ret = ''
	def autenticate(self):
		username = self.usernameInput.get()
		password = self.passwordInput.get()
		if not len(username) or not len(password):
			TkMessageBox.showinfo('Error', 'Invalid username or password')
		else:
			print('-- READ --\nUsername: ', username + '\nPassword: ', password)
			self.ret = ['autenticate', username, password]
			self.window.destroy()
			self.window = None
	def register(self):
		username = self.usernameInput.get()
		password = self.passwordInput.get()
		if not len(username) or not len(password):
			TkMessageBox.showinfo('Error', 'Invalid username or password')
		else:
			print('-- CREATE --\nUsername: ', username + '\nPassword: ', password)
			self.ret = ['register', username, password]
			self.window.destroy()
			self.window = None
	def start(self):
		if self.window == None:
			self.__init__(self.title, self.icon, self.geometry)
		# Renderiza a janela
		self.window.mainloop()
		return self.ret


