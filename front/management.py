from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.app import App

class ManagementScreen(App):
	def __init__(self, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)

		self.db.select('*', 'DISCIPLINA')
		for i,c in enumerate([('Code', 'Course')] + self.db.fetchall()):
			Label(self.screenFrame, text=str(c[0]), bd=1).grid(row=i, column=0)
			Label(self.screenFrame, text=c[1], bd=1).grid(row=i, column=1)
			if i:
				callback = lambda code=c[0]: self._stop(['course', code])
				Button(self.screenFrame, text='Manage', padx=1, command=callback).grid(row=i, column=2)

		# Cria botão
		buttons = (
			('Back', self._back),
			('Create course', self.__create_course),
			('Add language', self.__add_language)
			)
		for b in buttons:
			Button(self.screenFrame, text=b[0], command=b[1]).grid(sticky=W)

	def _create(self, fieldsNames, whichfun, buttonLabel='Create'):
		self.promptScreen = Toplevel(self.window)
		self.promptScreen.grab_set()
		self.fields = dict((lambda f: (f, Entry(self.promptScreen)))(f) for f in fieldsNames)
		for i,key in enumerate(self.fields):
			Label(self.promptScreen, text=key).grid(row=i, column=0)
			self.fields[key].grid(row=i, column=1)
		Button(self.promptScreen, text=buttonLabel, command=whichfun).grid()

	def __create_course(self):
		self._create(['Code','Name'], self.__create_course_)
	def __create_course_(self):
		try:
			code, name = str(int(self.fields['Code'].get())), self.fields['Name'].get()
			self.db.execute('insert into DISCIPLINA values ('+code+', \''+name+'\');')
			self.promptScreen.destroy()
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'Invalid code!')
		finally:
			self.db.commit()

	def __add_language(self):
		self._create(['Name', 'Compile/Run with'], self.__add_language_)
	def __add_language_(self):
		try:
			name, run = self.fields['Name'].get(), self.fields['Compile/Run with'].get()
			self.db.insert('LING_PROGR', (name, run), columns='(nome, comand_compila)')
			self.promptScreen.destroy()
		except Exception as e:
			print(e)
		finally:
			self.db.commit()

