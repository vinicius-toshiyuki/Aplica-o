from tkinter import *
from tkinter import messagebox as TkMessageBox
from PIL import Image
from app import App

class HomeScreen(App):
	def __init__(self, username, password, title='', icon=None, geometry='500x250'):
		self.username = username
		self.password = password
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
		self.homeScreenFrame = Frame(self.window)

		# Frames
		self.topbar = Frame(self.homeScreenFrame)
		self.topbar.pack(anchor=W)
		self.menu = Frame(self.homeScreenFrame)
		self.menu.pack()
		self.menuAdmin = Frame(self.homeScreenFrame)
		self.menuAdmin.pack()

		# Foto de perfil
		# TODO: Tem que ser a foto de perfil ne
		imraw = Image.open(self.icon)
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
		self.menuButtons = [
			Button(self.menu, text='Contests'), 
			Button(self.menu, text='Problems'), 
			Button(self.menu, text='Attempts'),
			Button(self.menu, text='Users'),
			Button(self.menu, text='Change password')
		]
		self.menuAdminButtons = [
			Button(self.menuAdmin, text='Admin quick'),
			Button(self.menuAdmin, text='Admin'),
			Button(self.menuAdmin, text='Cadastrar'),
			Button(self.menuAdmin, text='Controle de users')
		]
		for b in self.menuButtons: b.pack(side=LEFT)
		for b in self.menuAdminButtons: b.pack(side=LEFT)
	def logout(self):
		self.screen.clear()
		self.screen += ['logout']
		self.stop()

	def stop(self):
		self.homeScreenFrame.pack_forget()
		self.end.acquire()
		self.end.notify()
		self.end.release()

	def start(self):
		# Renderiza a janela
		self.homeScreenFrame.pack()
