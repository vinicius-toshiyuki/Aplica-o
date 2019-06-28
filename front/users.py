from tkinter import *
from tkinter import messagebox as TkMessageBox
from PIL import Image
from front.app import App

class UsersScreen(App):
	def __init__(self, registern, password, privilege, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)
		self.registern = registern
		self.password = password
		self.privilege = privilege
	
		# TODO: Podia adicionar uns filtros tipo usuários da mesma turma ou por tipo (professor, aluno, etc)
		# Botão de voltar
		Button(self.screenFrame, text='Back', command=self._back).grid(sticky=W)

		# Busca no banco de dados e mostra os alunos
		self.db.select('nome', 'ALUNO')
		Label(self.screenFrame, text='Students', bd=2, relief=GROOVE).grid(sticky=W)
		for a in self.db.fetchall():
			Label(self.screenFrame, text=a[0]).grid(sticky=W)
		self.db.select('nome', 'PROFESSOR')
		Label(self.screenFrame, text='Professors', bd=2, relief=GROOVE).grid(sticky=W)
		for a in self.db.fetchall():
			Label(self.screenFrame, text=a[0]).grid(sticky=W)
