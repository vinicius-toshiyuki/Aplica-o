from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.app import App

class AttemptsScreen(App):
	def __init__(self, email, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)
		self.email = email
		
		# Botão de voltar
		Button(self.screenFrame, text='Back', command=self._back).grid()

		
