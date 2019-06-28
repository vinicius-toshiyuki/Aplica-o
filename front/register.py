from tkinter import *
from tkinter import messagebox as TkMessageBox
from tkinter import filedialog
from front.app import App
from PIL import Image

class RegisterScreen(App):
	def __init__(self, registern, password, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)
		self.registern = registern
		self.password = password

		Button(self.screenFrame, text='Back', pady=7, command=self._back).grid(row=0, column=0)

		self.fields = {}
		fieldsNames = ('Register nº', 'Password', 'Confirm password', 'Username', 'Birthdate', 'Class')
		for i,f in enumerate(fieldsNames):
			self.fields[f] = (
						Label(self.screenFrame, text=f, bd = 7),
						Entry(self.screenFrame)
						)
			self.fields[f][0].grid(row=i+1, column=0)
			self.fields[f][1].grid(row=i+1, column=1)
			self.fields[f][1].bind('<Return>', self.__register)
			
		self.fields['Register nº'][1].insert(0, self.registern)
		self.fields['Register nº'][1].focus_set()
		self.fields['Password'][1].insert(0, self.password)
		self.fields['Password'][1].config(show='*')
		self.fields['Confirm password'][1].config(show='*')

		Label(self.screenFrame, text='Foto de perfil').grid(row=i+2, column=0)
		self.profilePicFrame = Frame(self.screenFrame)
		self.profilePicFrame.grid(row=i+2, column=1)

		picBrowse = Button(self.profilePicFrame, text='Procurar...', command=self.__browse_profile_pic)
		picBrowse.grid(row=0, column=0)
		picBrowse.bind('<Return>', self.__browse_profile_pic)
		# Espaço em branco
		Label(self.profilePicFrame, bd=3).grid(row=0, column=1)
		

		# Vai ser packeado e configurado no callback
		self.profilePicSet = False
		self.profilePicImageLabel = Label(self.profilePicFrame, background='white')

		Button(self.screenFrame, text='Register', pady=7, command=self.__register).grid()

	def __browse_profile_pic(self, e=None):
		profilePicFile = filedialog.askopenfile(
				parent=self.profilePicFrame,
				filetypes=(
					('Arquivos GIF', '*.gif'),
					('Arquivos PNG', '*.png'),
					('Arquivos JPEG', '*.jpg'),
					('Todos os arquivos', '*.*')
					),
				title='Procure uma imagem...'
				)
		self.profilePicPath = profilePicFile.name

		profilePicFile = Image.open(self.profilePicPath)
		profilePicFile = profilePicFile.resize((50,50), Image.NEAREST)
		profilePicFile.save('/tmp/temp.png')

		profilePicFile = PhotoImage(file='/tmp/temp.png')

		self.profilePicImageLabel.configure(image=profilePicFile)
		self.profilePicImageLabel.profilePicFile = profilePicFile

		self.profilePicImageLabel.grid(row=0, column=2)
		self.profilePicSet = True

	def __register(self):
		registern = self.fields['Register nº'][1].get()
		password = self.fields['Password'][1].get()
		confirmation = self.fields['Confirm password'][1].get()
		username = self.fields['Username'][1].get()
		birthdate = self.fields['Birthdate'][1].get()
		classe = self.fields['Class'][1].get()

		if not len(registern) or not len(password) or not len(confirmation):
			TkMessageBox.showinfo('Error', 'Invalid registern or password')
		elif password != confirmation:
			TkMessageBox.showinfo('Error', 'Incorrect password!!!')
		elif not self.profilePicSet:
			TkMessageBox.showinfo('Error', 'No picture')
		elif not len(registern) or not len(birthdate) or not len(classe):
			TkMessageBox.showinfo('Erro', 'Jouhou ga tarinai')
		else:
			importPic = list('lo_import(\'/tmp/temp.png\')')
			try:
				self.db.insert('ALUNO', (registern, registern, password, importPic, birthdate, ord(classe.upper())), columns='(matricula, nome, senha, foto, data_nasc, turma_cod)')
				self._stop()
			except Exception as e:
				TkMessageBox.showinfo('Error', 'Invalid data')
				print(e)
			finally:
				self.db.commit()
