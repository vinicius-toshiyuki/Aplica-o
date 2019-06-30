from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.app import App

class ContestsScreen(App):
	def __init__(self, privilege, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)
		self.privilege = privilege
		
		# Botão de voltar
		Button(self.screenFrame, text='Back', command=self._back).grid()

		problems = self.db.get_problem(get=['lista','titulo','descrição','dificuldade'], prova="'S'", visibilidade="'S'")
		# Uma lista
		for i,t in enumerate([('Lista','Título','Descrição','Dificuldade',)] + problems):
			for j,v in enumerate(t):	
				Label(self.screenFrame, text=str(v), bd=7).grid(row=i+2, column=j)
			if i:
				Button(self.screenFrame, text='Submit', padx=7).grid(row=i+2, column=j+1)

from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.problems import ProblemsScreen

class ContestsScreen(ProblemsScreen):
	def __init__(self, email, privilege, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)
		self.email = email
		self.privilege = privilege
		
		# Botão de voltar
		Button(self.screenFrame, text='Back', command=self._back).grid()

		problems = self.db.get_problem(get=['lista','titulo','descrição','dificuldade','codigo','lista','modulo','disciplina'], visibilidade="'S'", prova="'S'")
		for i,t in enumerate([('Lista','Título','Descrição','Dificuldade',)] + problems):
			for j,v in enumerate(t[:4]):	
				Label(self.screenFrame, text=str(v), bd=7).grid(row=i+2, column=j)
			if i and privilege != 'admin':
				Button(self.screenFrame, text='Submit', padx=7, command=lambda c=problems[i-1][4:]:self._submit(c)).grid(row=i+2, column=j+1)
