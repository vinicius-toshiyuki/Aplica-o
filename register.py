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

		# Não cria frame de register, usa o da LogInScreen

		# Cria outras Frames e tal
		self.confirmPassFrame = Frame(self.screenFrame)
		self.confirmPassFrame.pack()
		self.profilePicFrame = Frame(self.screenFrame)
		self.profilePicFrame.pack()
		self.registerNumberFrame = Frame(self.screenFrame)
		self.registerNumberFrame.pack()
		self.birthdateFrame = Frame(self.screenFrame)
		self.birthdateFrame.pack()
		self.classFrame = Frame(self.screenFrame)
		self.classFrame.pack()

		# Cria confirmação da senha
		self.confirmPassLabel = Label(self.confirmPassFrame, text='Confirm password: ')
		self.confirmPassLabel.pack(side=LEFT)
		self.confirmPassInput = Entry(self.confirmPassFrame, show='*')
		self.confirmPassInput.pack(side=RIGHT)

		# Cria campo para pôr imagem de perfil
		self.profilePicLabel = Label(self.profilePicFrame, text='Foto de perfil: ')
		self.profilePicLabel.pack(side=LEFT)
		self.profilePicButton = Button(self.profilePicFrame, text='Procurar...', command=self.browse_profile_pic)
		self.profilePicButton.pack(side=RIGHT)
		# Vai ser packeado e configurado no callback
		self.profilePicSet = False
		self.profilePicImageLabel = Label(self.profilePicFrame, background='white')

		# Cria campo para matrícula
		self.registerNumberLabel = Label(self.registerNumberFrame, text='Register nº: ')
		self.registerNumberLabel.pack(side=LEFT)
		self.registerNumberInput = Entry(self.registerNumberFrame)
		self.registerNumberInput.pack(side=RIGHT)

		# Cria campo para data de nascimento birthdate
		self.birthdateLabel = Label(self.birthdateFrame, text='Birthdate (ddmm-yyyy): ')
		self.birthdateLabel.pack(side=LEFT)
		self.birthdateInput = Entry(self.birthdateFrame)
		self.birthdateInput.pack(side=RIGHT)
		
		# Cria campo para a turma
		self.classLabel = Label(self.classFrame, text='Turma: ')
		self.classLabel.pack(side=LEFT)
		self.classInput = Entry(self.classFrame)
		self.classInput.pack(side=RIGHT)

		# Despackeia e packeia de novo a frame de botão de registrar pra ir para o final
		self.buttonFrame.pack_forget()
		self.buttonFrame.pack()
	def browse_profile_pic(self):
		profilePicFile = filedialog.askopenfile(parent=self.profilePicFrame, filetypes=(('Arquivos JPEG', '*.jpg'), ('Todos os arquivos', '*.*')), title='Procure uma imagem...')

		self.profilePicPath = profilePicFile.name
		profilePicFile = Image.open(self.profilePicPath)
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
		registern = self.registerNumberInput.get()
		birthdate = self.birthdateInput.get()
		classe = self.classInput.get()
		if not len(username) or not len(password) or not len(confirmation):
			TkMessageBox.showinfo('Error', 'Invalid username or password')
		elif password != confirmation:
			TkMessageBox.showinfo('Error', 'Incorrect password!!!')
		elif not self.profilePicSet:
			TkMessageBox.showinfo('Error', 'No picture')
		elif not len(registern) or not len(birthdate) or not len(classe):
			TkMessageBox.showinfo('Erro', 'Jouhou ga tarinai')
		else:
			# TODO: fazer uma função pra abstrari mais esses insert e tudo
			# TODO: colocar a data de cadastro e semestre numa função no sql
			importPic = list('lo_import(\''+self.profilePicPath+'\')')
			self.db.insert('ALUNO', (registern, username, password, importPic, birthdate, ord(classe.upper())), columns='(matricula, nome, senha, foto, data_nasc, turma_cod)')
			self.db.commit()
			self.stop()
