from tkinter import *
from tkinter import messagebox as TkMessageBox
import threading
from threading import Thread
from database import BD

class App:
	window = Tk(className='Corretor')
	screen = [None]
	_previous = [None]
	lock = threading.Lock()
	end = threading.Condition(lock)
	on = True
	db = BD()

	def __init__(self, title='', icon=None, geometry='400x250'):
		self.title = title
		self.icon = icon
		self.geometry = geometry

		self.db.connect()

		self.window.resizable(0, 0)
		# Cria handler para retornos
		self.handler = {}
	def add_handler(self, key, call):
		self.handler[key] = call
	def window_start(self):
		Thread(target=self.thread_start).start()
		self.window.mainloop()
		self.on = False
		self.end.acquire()
		self.end.notify()
		self.end.release()
	def thread_start(self):
		while self.on:
			print(self.screen)
			self.handler[self.screen[0]](*self.screen[1:], title=self.title, icon=self.icon).start()
			self.end.acquire()
			self.end.wait()
			self.end.release()
	def start(self):
		self.screenFrame.pack()
	def stop(self, args=[None]):
		self.screenFrame.pack_forget()

		if args == self._previous:
			args = [] + self._previous

		self._previous.clear()
		self._previous += self.screen
		self.screen.clear()
		self.screen += args

		self.end.acquire()
		self.end.notify()
		self.end.release()


