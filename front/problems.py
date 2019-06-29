from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.app import App

class ProblemsScreen(App):
	def __init__(self, privilege, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)
		self.privilege = privilege
		
		# Botão de voltar
		Button(self.screenFrame, text='Back', command=self._back).grid()

		self.db.select('p.lista_cod, p.titulo, p.descr, p.dificul', 'PROBLEMA p join LISTA l on lista_cod = l.cod', where="prova = 'N' and visibilidade = 'S'")
		# Uma lista
		for i,t in enumerate([('Lista','Título','Descrição','Dificuldade',)] + self.db.fetchall()):
			for j,v in enumerate(t):	
				Label(self.screenFrame, text=str(v), bd=7).grid(row=i+2, column=j)
			if i:
				Button(self.screenFrame, text='Submit', padx=7, command=self.__submit).grid(row=i+2, column=j+1)

	def __submit(self):
		submitFile = filedialog.askopenfile(
				parent=self.screenFrame,
				filetypes=(
					('Todos os arquivos', '*.*'),
					),
				title='Escolha um arquivo...'
				)

		file = open(submitFile.name, 'r')
		source_code = file.read()
	
		self.db.insert('SUBMISSAO',
				(
				 source_code,
				 'not judged',
					170023664,
					1,
					1,
					1
				,),
				columns='( \
						codi_fonte, \
						veredito, \
						aluno_matr, \
						problema_cod, \
						lista_cod, \
						ling_progr_cod \
					)'
				)
