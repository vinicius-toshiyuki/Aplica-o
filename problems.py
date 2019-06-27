from tkinter import *
from tkinter import messagebox as TkMessageBox
from app import App

class ProblemsScreen(App):
	def __init__(self, privilege, title='', icon=None, geometry='400x250'):
		self.privilege = privilege
		self.title = title
		self.icon = icon
		self.geometry = geometry

		self.window.title(self.title)
		# Configura ícone da janela
		if self.icon != None:
			self.windowicon = PhotoImage(file=self.icon)
			self.window.tk.call('wm', 'iconphoto', self.window._w, self.windowicon)
		# Configura tamanho da janela (largura x altura)
		self.window.geometry(self.geometry)

		# Cria o frame daqui
		self.screenFrame = Frame(self.window)

		# Botão de voltar
		Button(self.screenFrame, text='Back', command=self.back).grid()

		# Uma lista
		for i in range(3):
			Label(self.screenFrame, text=str(i)).grid(row=i+1, column=0)
			Entry(self.screenFrame).grid(row=i+1, column=1)
	def back(self):
		self.stop(self._previous)
