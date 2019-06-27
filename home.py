from threading import Thread
from tkinter import *
from tkinter import messagebox as TkMessageBox
from PIL import Image
from app import App

class HomeScreen(App):
	def __init__(self, username, password, privilege, title='', icon=None, geometry='500x250'):
		self.username = username
		self.password = password
		self.privilege = privilege
		self.title = title
		self.icon = icon
		self.geometry = geometry

		self.window.title(self.title)
		# Configura ícone da janela
		if self.icon != None:
			self.windowicon = PhotoImage(file=self.icon)
			self.window.tk.call('wm', 'iconphoto', self.window._w, self.windowicon)
		# Configura tamanho da janela (largura x altura)
		self.window.geometry(self.geometry)

		# Cria frame da home self.screen
		self.screenFrame = Frame(self.window)

		# Frames
		self.topbar = Frame(self.screenFrame)
		self.topbar.pack(anchor=W)
		self.menu = Frame(self.screenFrame)
		self.menu.pack()
		self.menuAdmin = Frame(self.screenFrame)
		self.menuAdmin.pack()

		# Foto de perfil
		# TODO: Tem que ser a foto de perfil ne
		imraw = Image.open('/tmp/profilepic')
		imraw = imraw.resize((50,50), Image.NEAREST)
		imraw.save('.temp.png')

		im = PhotoImage(file='.temp.png')

		self.profile = Label(self.topbar, image=im, background='white')
		self.profile.im = im

		self.profile.pack(side=LEFT, padx=5)

		# Nome do usuário
		self.name = Label(self.topbar, text=username, bd=2)
		self.name.pack(side=LEFT, padx=5)

		# Sair
		self.logoutButton = Button(self.topbar, text='Log out', command=self.logout)
		self.logoutButton.pack(side=LEFT, padx=5)

		# Botões do menu
		# TODO: essas telas desse menus poderiam ter uma super classe comum pra ter botão de voltar e tal
		self.menuButtons = [
			Button(self.menu, text='Contests', command=self.contests), 
			Button(self.menu, text='Problems', command=self.problems), 
			Button(self.menu, text='Attempts', command=self.attempts),
			Button(self.menu, text='Users', command=self.users),
			Button(self.menu, text='Change password', command=self.change_password)
		]
		for b in self.menuButtons: b.pack(side=LEFT)
		if self.privilege == 'admin':
			self.menuAdminButtons = [
				Button(self.menuAdmin, text='Review', command=self.review),
				# Button(self.menuAdmin, text='Admin', command=self.admin),
				Button(self.menuAdmin, text='Privileges', command=self.privileges),
				Button(self.menuAdmin, text='Contest control', command=self.contest_control)
			]
			for b in self.menuAdminButtons: b.pack(side=LEFT)
	def contests(self):
		pass
	def problems(self):
		self.stop(['problems', self.privilege])
	def attempts(self):
		pass
	def users(self):
		self.stop(['users', self.username, self.password, self.privilege])
	def change_password(self):
		promptScreen = Toplevel()
		promptScreen.grab_set()
		
		entries = []
		for i,j in enumerate(['Old ','New ','Confirm new ']):
			Label(promptScreen, text=j+'password: ').grid(row=i, column=0)
			entries.append(Entry(promptScreen, show='*'))
			entries[-1].grid(row=i, column=1)
		Button(promptScreen, text='Change', command=lambda: ((self.db.execute('update ALUNO set senha = \''+entries[1].get()+'\' where nome = \''+self.username+'\'; select senha from ALUNO where nome = \''+self.username+'\'') or self.__change_password() or promptScreen.destroy()) if entries[1].get() == entries[2].get() else TkMessageBox.showinfo('Error', 'Invalid password'))	if entries[0].get() == self.password 	else TkMessageBox.showinfo('Error', 'Wrong password')).grid()
		
	def __change_password(self):
		print('Old pass: ', self.password)
		self.password = (self.db.fetchone())[0]
		print('New pass: ', self.password)

	def review(self):
		pass
	def privileges(self):
		pass
	def contest_control(self):
		pass
	def logout(self):
		self.stop(['logout'])
