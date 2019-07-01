from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.app import App

class ReviewScreen(App):
	def __init__(self, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)
		
		# Botão de voltar
		Button(self.screenFrame, text='Back', command=self._back).grid()

		try:
			matricula = self.db.get_users(get=['matricula', 'email'])
			for i,a in enumerate([('Matrícula', 'E-mail', 'Nota')] + matricula):
				Label(self.screenFrame, text=a[0], bd=7).grid(row=i+1, column=0, sticky=W)
				Label(self.screenFrame, text=a[1], bd=7).grid(row=i+1, column=1, sticky=W)
				if not i:
					Label(self.screenFrame, text=a[2], bd=7).grid(row=i+1, column=2, sticky=W)
				else:
					nota = self.db.get_nota(a[1])
					Label(self.screenFrame, text=str(nota), bd=7).grid(row=i+1, column=2, sticky=W)
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'No students registered')
		
		
