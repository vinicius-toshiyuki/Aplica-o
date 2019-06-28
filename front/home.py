from threading import Thread
from tkinter import *
from tkinter import messagebox as TkMessageBox
from PIL import Image
from front.app import App

class HomeScreen(App):
	def __init__(self, registern, password, privilege, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)
		self.registern = registern
		self.password = password
		self.privilege = privilege
		
		# Frames
		self.topbar = Frame(self.screenFrame, bd=5)
		self.topbar.grid(sticky=E+W+N+S)
		self.menu = Frame(self.screenFrame)
		self.menu.grid(sticky=E+W+N+S)
		self.menuAdmin = Frame(self.screenFrame)
		self.menuAdmin.grid(sticky=E+W+N+S)

		# Foto de perfil
		try:
			imraw = Image.open('/tmp/profilepic')
			imraw = imraw.resize((50,50), Image.NEAREST)
			imraw.save('/tmp/temp.png')

			im = PhotoImage(file='/tmp/temp.png')

			self.profile = Label(self.topbar, image=im, background='white')
			self.profile.im = im

			self.profile.pack(side=LEFT)
		except Exception as e:
			print(e)
		finally:
			pass

		# Nome do usuário
		self.name = Label(self.topbar, text=registern, bd=5)
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
		pass
	def __problems(self, e=None):
		self._stop(['problems', self.privilege])
	def __attempts(self, e=None):
		pass
	def __users(self, e=None):
		self._stop(['users', self.registern, self.password, self.privilege])
	def __change_password(self, e=None):
		promptScreen = Toplevel()
		promptScreen.grab_set()
		
		entries = []
		for i,j in enumerate(['Old ','New ','Confirm new ']):
			Label(promptScreen, text=j+'password: ').grid(row=i, column=0)
			entries.append(Entry(promptScreen, show='*'))
			entries[-1].grid(row=i, column=1)
		Button(promptScreen, text='Change', command=lambda: ((self.db.execute('update ALUNO set senha = \''+entries[1].get()+'\' where nome = \''+self.registern+'\'; select senha from ALUNO where nome = \''+self.registern+'\'') or self.db.commit() or self.__change_password_() or promptScreen.destroy()) if entries[1].get() == entries[2].get() else TkMessageBox.showinfo('Error', 'Invalid password'))	if entries[0].get() == self.password 	else TkMessageBox.showinfo('Error', 'Wrong password')).grid()
		
	def __change_password_(self):
		print('Old pass: ', self.password)
		self.password = (self.db.fetchone())[0]
		print('New pass: ', self.password)

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
