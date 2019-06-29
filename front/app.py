from tkinter import *
from tkinter import messagebox as TkMessageBox
import threading
from threading import Thread
from back.database import *

class App:
	window = Tk(className='Corretor')
	screen = [None]
	_previous = [['exit']]
	lock = threading.Lock()
	end = threading.Condition(lock)
	on = True
	db = Corretor()

	def __init__(self, title='', icon=None, geometry='400x250'):
		self.title = title
		self.icon = icon
		self.geometry = geometry

		self.db.connect(database='test')

		self.window.resizable(0, 0)
		# Cria handler para retornos
		self.handler = {}
	def add_handler(self, key, call):
		self.handler[key] = call
	def window_start(self):
		Thread(target=self.__thread_start).start()
		self.window.mainloop()
		self.on = False
		self.end.acquire()
		self.end.notify()
		self.end.release()
	def __thread_start(self):
		while self.on:
			print(self.screen)
			self.handler[self.screen[0]](*self.screen[1:], title=self.title, icon=self.icon)._start()
			self.end.acquire()
			self.end.wait()
			self.end.release()
	def _init(self, title, icon, geometry):
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

		# Cria frame da screen
		self.screenFrame = Frame(self.window)
		self.screenFrame.config(bd=10)

		self.window.grid_columnconfigure(0, minsize=250)
		self.window.grid_rowconfigure(0,minsize=200)
	def _back(self):
		self._stop(self._previous[-1])
	def _start(self):
		self.screenFrame.grid(sticky=N+W)
	def _stop(self, args=[None]):
		self.screenFrame.grid_forget()

		if args == self._previous[-1]:
			args = [] + self._previous[-1]
			self._previous.pop()
		else:
			self._previous.append([] + self.screen)
		self.screen.clear()
		self.screen += args

		self.end.acquire()
		self.end.notify()
		self.end.release()


