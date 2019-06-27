from tkinter import *
from tkinter import messagebox as TkMessageBox
from PIL import Image
from app import App

class UsersScreen(App):
	def __init__(self, username, password, privilege, title='', icon=None, geometry='400x250'):
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

		# Cria o frame pra cá
		self.screenFrame = Frame(self.window)
		self.screenFrame.pack()

		# TODO: Podia adicionar uns filtros tipo usuários da mesma turma ou por tipo (professor, aluno, etc)
		# Botão de voltar
		Button(self.screenFrame, text='Back', command=self.back).grid()

		# Busca no banco de dados e mostra os alunos
		self.db.select('nome', 'ALUNO')
		for a in self.db.fetchall():
			Label(self.screenFrame, text=a[0]).grid()

	def back(self):
		self.stop(self._previous)
