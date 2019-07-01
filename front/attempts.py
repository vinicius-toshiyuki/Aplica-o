from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.app import App

class AttemptsScreen(App):
	def __init__(self, email, privilege, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)
		self.email = email
		self.privilege = privilege
		
		# Botão de voltar
		Button(self.screenFrame, text='Back', command=self._back).grid()

		if self.privilege == 'admin':
			atts = self.db.get_attempts(get=['codigo','veredito','problema','arquivo'])
		else:
			matricula = self.db.get_users(get='matricula', email=self.email)[0]
			atts = self.db.get_attempts(get=['codigo','veredito','problema','arquivo'], aluno=matricula)
		for i,a in enumerate([('Codigo', 'Veredito', 'Problema', 'Arquivo')] + atts):
			Label(self.screenFrame, text=a[0], bd=7).grid(row=i+1, column=0, sticky=W)
			Label(self.screenFrame, text=a[1], bd=7).grid(row=i+1, column=1, sticky=W)
			Label(self.screenFrame, text=a[2], bd=7).grid(row=i+1, column=2, sticky=W)
			if not i:
				Label(self.screenFrame, text=a[3], bd=7).grid(row=i+1, column=3, sticky=W)
			else:
				callback = lambda filebytes=a[3]: self.__get_file(filebytes)
				Button(self.screenFrame, text='Get file', padx=7, pady=7, command=callback).grid(row=i+1, column=3, sticky=W)
		
	def __get_file(self, filebytes):
		try:
			self._open_file(filebytes=filebytes)
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'Unable to open file')

		
