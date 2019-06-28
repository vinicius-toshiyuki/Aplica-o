from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.app import App

class ProblemsScreen(App):
	def __init__(self, privilege, title='', icon=None, geometry='400x250'):
		self._init(title, icon, geometry)
		self.privilege = privilege
		
		# Botão de voltar
		Button(self.screenFrame, text='Back', command=self.back).grid()

		# Uma lista
		for i in range(3):
			Label(self.screenFrame, text=str(i)).grid(row=i+1, column=0)
			Entry(self.screenFrame).grid(row=i+1, column=1)
