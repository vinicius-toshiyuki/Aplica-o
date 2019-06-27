from tkinter import *
from tkinter import messagebox as TkMessageBox
from PIL import Image
from app import App

class UsersScreen(App):
	def __init__(self, username, password, privilege, title='', icon=None, geometry='400x250'):
		self._init(title, icon, geometry)
		self.username = username
		self.password = password
		self.privilege = privilege
		
		# TODO: Podia adicionar uns filtros tipo usuários da mesma turma ou por tipo (professor, aluno, etc)
		# Botão de voltar
		Button(self.screenFrame, text='Back', command=self.back).grid()

		# Busca no banco de dados e mostra os alunos
		self.db.select('nome', 'ALUNO')
		Label(self.screenFrame, text='Students', bd=6, relief=GROOVE).grid()
		for a in self.db.fetchall():
			Label(self.screenFrame, text=a[0]).grid()
		self.db.select('nome', 'PROFESSOR')
		Label(self.screenFrame, text='Professors', bd=6, relief=GROOVE).grid()
		for a in self.db.fetchall():
			Label(self.screenFrame, text=a[0]).grid()
