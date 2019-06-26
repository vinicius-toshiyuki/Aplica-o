from tkinter import *
from tkinter import messagebox as TkMessageBox
import threading
from threading import Thread

class App:
	window = Tk()
	screen = [None]
	lock = threading.Lock()
	end = threading.Condition(lock)
	on = True

	def __init__(self, title='', icon=None, geometry='400x250'):
		self.title = title
		self.icon = icon
		self.geometry = geometry

		# Cria handler para retornos
		# TODO: tem que tratar pra autenticar mesmo e tal
		self.handler = {}
	def add_handler(self, key, call):
		self.handler[key] = call
	def start(self):
		Thread(target=self.thread_start).start()
		self.window.mainloop()
		self.on = False
		self.end.acquire()
		self.end.notify()
		self.end.release()
	def thread_start(self):
		while self.on:
			print(self.screen)
			self.handler[self.screen[0]](*self.screen[1:], title=self.title, icon=self.icon, geometry=self.geometry).start()
			self.end.acquire()
			self.end.wait()
			self.end.release()
