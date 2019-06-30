from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.app import App

class ProblemsScreen(App):
	def __init__(self, email, privilege, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)
		self.email = email
		self.privilege = privilege
		
		# Botão de voltar
		Button(self.screenFrame, text='Back', command=self._back).grid()

		problems = self.db.get_problem(get=['lista','titulo','descrição','dificuldade','codigo','lista','modulo','disciplina'], visibilidade="'S'", prova="'N'")
		for i,t in enumerate([('Lista','Título','Descrição','Dificuldade',)] + problems):
			for j,v in enumerate(t[:4]):	
				Label(self.screenFrame, text=str(v), bd=7).grid(row=i+2, column=j)
			if i and privilege != 'admin':
				Button(self.screenFrame, text='Submit', padx=7, command=lambda c=problems[i-1][4:]:self._submit(c)).grid(row=i+2, column=j+1)

	def _submit(self, codes):		
		file = filedialog.askopenfile(
				parent=self.screenFrame,
				filetypes=(('All files', '*.*'),),
				title='Choose submit file'
				)
		try:
			registern = str(self.db.get_users(get='matricula', email=self.email)[0])
			kwargs = dict(
					tabela='SUBMISSAO',
					aluno=registern,
					veredito='not judged',
					arquivo=file.name,
					disciplina=codes[3],
					modulo=codes[2],
					lista=codes[1],
					problema=codes[0],
					linguagem='1'
					)
			self.db.insert_file(**kwargs)
			self.db.commit()
			TkMessageBox.showinfo('Success', 'Submission accepted')
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'Failed!')
