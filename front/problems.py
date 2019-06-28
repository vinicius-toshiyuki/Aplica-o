from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.app import App

class ProblemsScreen(App):
	def __init__(self, privilege, title='', icon=None, geometry='400x250'):
		geometry='700x250'
		self._init(title, icon, geometry)
		self.privilege = privilege
		
		# Botão de voltar
		Button(self.screenFrame, text='Back', command=self.back).grid()

		self.db.select('lista_cod, titulo, descr, dificul', 'PROBLEMA')
		# Uma lista
		for i,t in enumerate([('Lista','Título','Descrição','Dificuldade',)] + self.db.fetchall()):
			for j,v in enumerate(t):	
				Label(self.screenFrame, text=str(v), bd=7).grid(row=i+2, column=j)
			if i:
				Button(self.screenFrame, text='Submit', padx=7).grid(row=i+2, column=j+1)

