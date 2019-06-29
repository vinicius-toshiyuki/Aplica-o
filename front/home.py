from threading import Thread
from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.app import App
from PIL import Image
import io
import base64

class HomeScreen(App):
	def __init__(self, email, privilege, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)
		self.email = email
		self.privilege = privilege
		self.username = self.db.get_users(get='nome', email=self.email)[0]
		
		# Frames
		self.topbar = Frame(self.screenFrame, bd=5)
		self.topbar.grid(sticky=E+W+N+S)
		self.menu = Frame(self.screenFrame)
		self.menu.grid(sticky=E+W+N+S)
		self.menuAdmin = Frame(self.screenFrame)
		self.menuAdmin.grid(sticky=E+W+N+S)

		# Foto de perfil
		try:
			image = base64.b64encode(self.db.get_users(get='foto', email=self.email)[0].tobytes())
			image = PhotoImage(data=image)

			self.profile = Label(self.topbar, image=image, background='white')
			self.profile.image = image

			self.profile.pack(side=LEFT)
		except Exception as e:
			print('Could not open picture')
		finally:
			pass

		# Nome do usuário
		self.name = Label(self.topbar, text=self.username, bd=5)
		self.name.pack(side=LEFT)

		# Sair
		self.logoutButton = Button(self.topbar, text='Log out', command=self.__logout, padx=5)
		self.logoutButton.pack(side=LEFT)
		self.logoutButton.bind('<Return>', self.__logout)

		# Botões do menu
		self.buttonsMenu = {}
		buttonsNames = (
				('Contests'        , self.__contests),
				('Problems'        , self.__problems),
				('Attempts'        , self.__attempts),
				('Users'           , self.__users),
				('Change password' , self.__change_password)
				)
		for i,b in enumerate(buttonsNames):
			self.buttonsMenu[b[0]] = Button(self.menu, text=b[0], pady=7, command=b[1])
			self.buttonsMenu[b[0]].bind('<Return>', b[1])
			self.buttonsMenu[b[0]].grid(row=0, column=i)

		if self.privilege == 'admin':
			# Botões do admin
			self.buttonsAdmin = {}
			buttonsNames = (
					('Review'           , self.__review),
					('Privileges'       , self.__privileges),
					('Contest control'  , self.__contest_control),
					('Class management' , self.__class_management)
					)
			for i,b in enumerate(buttonsNames):
				self.buttonsAdmin[b[0]] = Button(self.menuAdmin, text=b[0], pady=7, command=b[1])
				self.buttonsAdmin[b[0]].bind('<Return>', b[1])
				self.buttonsAdmin[b[0]].grid(row=0, column=i)

	def __contests(self, e=None):
		self._stop(['contests', self.privilege])
	def __problems(self, e=None):
		self._stop(['problems', self.privilege])
	def __attempts(self, e=None):
		pass
	def __users(self, e=None):
		self._stop(['users'])
	def __change_password(self, e=None):
		self.promptScreen = Toplevel()
		self.promptScreen.grab_set()
		
		self.entries = []
		for i,j in enumerate(['Old ','New ','Confirm new ']):
			Label(self.promptScreen, text=j+'password: ').grid(row=i, column=0)
			self.entries.append(Entry(self.promptScreen, show='*'))
			self.entries[-1].grid(row=i, column=1)
			# TODO: aqui tem uma query
		Button(self.promptScreen, text='Change', command=self.__change_password_).grid()
		
	def __change_password_(self):
		password = self.db.get_users(get='senha', email=self.email)[0]
		if self.entries[1].get() == self.entries[2].get() and self.entries[0].get() == password:
			if not self.db.change_password(self.email, self.entries[1].get()):
				TkMessageBox.showinfo('Error', 'Failed. Try again later')
		else:
			TkMessageBox.showinfo('Error', 'Wrong password')
		self.promptScreen.destroy()

	def __review(self, e=None):
		pass
	def __privileges(self, e=None):
		pass
	def __contest_control(self, e=None):
		pass
	def __class_management(self, e=None):
		self._stop(['management'])
	def __logout(self, e=None):
		self._stop(['logout'])
