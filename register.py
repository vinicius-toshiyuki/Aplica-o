from tkinter import *
from tkinter import messagebox as TkMessageBox
from tkinter import filedialog
from login import LogInScreen 
from PIL import Image

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

		# Cria frame de register
		self.registerFrame = self.loginFrame

		# Cria outras Frames e tal
		self.confirmPassFrame = Frame(self.registerFrame)
		self.confirmPassFrame.pack()
		self.profilePicFrame = Frame(self.registerFrame)
		self.profilePicFrame.pack()

		# Cria confirmação da senha
		self.confirmPassLabel = Label(self.confirmPassFrame, text='Confirm password: ')
		self.confirmPassLabel.pack(side=LEFT)
		self.confirmPassInput = Entry(self.confirmPassFrame, show='*')
		self.confirmPassInput.pack(side=RIGHT)

		# Cria campo para pôr imagem de perfil
		self.profilePicLabel = Label(self.profilePicFrame, text='Fotinha do zapkk: ')
		self.profilePicLabel.pack(side=LEFT)
		self.profilePicButton = Button(self.profilePicFrame, text='Procurar...', command=self.browse_profile_pic)
		self.profilePicButton.pack(side=RIGHT)
		# Vai ser packeado e configurado no callback
		self.profilePicSet = False
		self.profilePicImageLabel = Label(self.profilePicFrame, background='white')
		
		# Despackeia e packeia de novo a frame de botão de registrar pra ir para o final
		self.buttonFrame.pack_forget()
		self.buttonFrame.pack()
	def browse_profile_pic(self):
		profilePicFile = filedialog.askopenfile(parent=self.profilePicFrame, filetypes=(('Arquivos JPEG', '*.jpg'), ('Todos os arquivos', '*.*')), title='Procure uma imagem...')

		profilePicFile = Image.open(profilePicFile.name)
		profilePicFile = profilePicFile.resize((50,50), Image.NEAREST)
		profilePicFile.save('.temp.png')

		profilePicFile = PhotoImage(file='.temp.png')

		self.profilePicImageLabel.configure(image=profilePicFile)
		self.profilePicImageLabel.profilePicFile = profilePicFile

		self.profilePicImageLabel.pack(side=RIGHT)
		self.profilePicSet = True

	def register(self):
		username = self.usernameInput.get()
		password = self.passwordInput.get()
		confirmation = self.confirmPassInput.get()
		if not len(username) or not len(password) or not len(confirmation):
			TkMessageBox.showinfo('Error', 'Invalid username or password')
		elif password != confirmation:
			TkMessageBox.showinfo('Error', 'Incorrect password!!!')
		elif not self.profilePicSet:
			TkMessageBox.showinfo('Error', 'No picture')
		else:
			self.screen.clear()
			self.screen += [None]
			self.stop()

	def stop(self):
		self.registerFrame.pack_forget()
		self.end.acquire()
		self.end.notify()
		self.end.release()

	def start(self):
		self.registerFrame.pack()
