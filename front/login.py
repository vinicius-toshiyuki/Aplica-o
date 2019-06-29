from tkinter import *
from tkinter import messagebox as TkMessageBox
from PIL import Image
from front.app import App

class LogInScreen(App):
	def __init__(self, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)

		self.fields = {}
		fieldsNames = ('E-mail', 'Password')
		for i,f in enumerate(fieldsNames):
			self.fields[f] = (
						Label(self.screenFrame, text=f, bd = 7),
						Entry(self.screenFrame)
						)
			self.fields[f][0].grid(row=i, column=0)
			self.fields[f][1].grid(row=i, column=1)
			self.fields[f][1].bind('<Return>', self.__autenticate)
		
		self.fields['E-mail'][1].focus_set()
		self.fields['Password'][1].config(show='*')

		self.buttons = {}
		buttonsNames = (('Log in',self.__autenticate),('Register',self.__register))
		for b in buttonsNames:
			self.buttons[b[0]] = Button(self.screenFrame, text=b[0], pady=7, command=b[1])
			self.buttons[b[0]].bind('<Return>', b[1])
			self.buttons[b[0]].grid()

		self.buttons['Register'].config(relief=FLAT)

	def __autenticate(self, event=None):
		email = self.fields['E-mail'][1].get()
		password = self.fields['Password'][1].get()

		try:
			if not len(email) or not len(password):
				raise ValueError('Invalid email or password')
			userInfo = self.db.get_users(get='senha', table='PROFESSOR', email=email)
			if userInfo:
				privilege = 'admin'
			else:
				userInfo = self.db.get_users(get=['senha', 'matricula'], email=email)
				if userInfo:
					privilege = 'admin' if self.db.is_tutor(userInfo[1]) else 'common'
				else:
					raise ValueError('User not registered')

			if userInfo[0] == password:
				self._stop(['home', email, privilege])
			else:
				raise ValueError('Invalid password')
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'Invalid e-mail or password')

	def __register(self, event=None):
		email = self.fields['E-mail'][1].get()
		password = self.fields['Password'][1].get()
		self._stop(['register', email, password])
