from tkinter import *
from login import LogInScreen 

class RegisterScreen(LogInScreen):
	def __init__(self, username, password, title='', icon=None, geometry='400x250'):
		self.username = username
		self.password = password

		# Usa o init da super classe
		LogInScreen.__init__(self=self, title=title, icon=icon, geometry=geometry)

		# Tira o botão de autenticar e raisa o de registrar
		self.loginButton.pack_forget()
		self.registerButton.configure(relief=RAISED)

		# Insere o texto passado nos campos
		self.usernameInput.delete(0, END)
		self.usernameInput.insert(0, self.username)
		self.passwordInput.delete(0, END)
		self.passwordInput.insert(0, self.password)

		# Cria outras Frames e tal
		self.confirmPassFrame = Frame(self.window)
		self.confirmPassFrame.pack()
		self.profilePicFrame = Frame(self.window)
		self.profilePicFrame.pack()

		# Cria confirmação da senha
		self.confirmPassLabel = Label(self.confirmPassFrame, text='Confirme a senha: ')
		self.confirmPassLabel.pack(side=LEFT)
		self.confirmPassInput = Entry(self.confirmPassFrame)
		self.confirmPassInput.pack(side=RIGHT)

		# Despackeia e packeia de novo a frame de botão de registrar pra ir para o final
		self.buttonFrame.pack_forget()
		self.buttonFrame.pack()

	def register(self):
		print("Ola")
