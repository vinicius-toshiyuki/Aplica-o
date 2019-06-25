from tkinter import *
from tkinter import messagebox as TkMessageBox
from PIL import Image

class HomeScreen:
	def __init__(self, username, password, title='', icon=None, geometry='400x250'):
		self.username = username
		self.password = password
		self.title = title
		self.icon = icon
		self.geometry = geometry

		# Cria janela
		self.window = Tk()
		self.window.title(self.title)
		# Configura ícone da janela
		if self.icon != None:
			windowicon = PhotoImage(file=self.icon)
			self.window.tk.call('wm', 'iconphoto', self.window._w, windowicon)
		# Configura tamanho da janela (largura x altura)
		self.window.geometry(self.geometry)

		# Frames
		self.topbar = Frame(self.window)
		self.topbar.pack(anchor=W)

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
		self.logoutButton = Button(self.topbar, text='Desconectar', command=self.logout)
		self.logoutButton.pack(side=LEFT, padx=5)

		# Configura o retorna
		self.ret = ''
	def logout(self):
		self.ret = ['logout']
		self.window.destroy()
		self.window = None

	def start(self):
		# Renderiza a janela
		if self.window == None:
			self.__init__(self.username, self.password, self.title, self.icon, self.geometry)
		self.window.mainloop()
		return self.ret


