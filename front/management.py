from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.app import App

class ManagementScreen(App):
	def __init__(self, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)

		for i,c in enumerate([('Code', 'Course')] + self.db.get_courses()):
			Label(self.screenFrame, text=str(c[0]), bd=1).grid(row=i, column=0)
			Label(self.screenFrame, text=c[1], bd=1).grid(row=i, column=1)
			if i:
				callback = lambda code=c[0]: self._stop(['course', code])
				Button(self.screenFrame, text='Manage', padx=1, command=callback).grid(row=i, column=2)

		# Cria botão
		buttons = (
			('Back', self._back),
			('Create course', self.__create_course),
			('Create class', self.__create_class),
			('Add language', self.__add_language)
			)
		for b in buttons:
			Button(self.screenFrame, text=b[0], command=b[1]).grid(sticky=W)

	def _create(self, fieldsNames, whichfun, buttonLabel='Create'):
		self.promptScreen = Toplevel(self.window)
		self.promptScreen.grab_set()
		self.fields = self.__fields(fieldsNames)
		for i,key in enumerate(self.fields):
			Label(self.promptScreen, text=key).grid(row=i, column=0)
			self.fields[key].grid(row=i, column=1, sticky=W)
		Button(self.promptScreen, text=buttonLabel, command=whichfun).grid()
	def __fields(self, fieldsNames):
		fields = {}
		for f in fieldsNames:
			if type(f) == str:
				fields[f] = Entry(self.promptScreen)
			elif type(f[2]) == dict:
				fields[f[0]] = f[1](self.promptScreen, **f[2])
			else:
				fields[f[0]] = f[1](self.promptScreen, *f[2])
		return fields

	def __create_course(self):
		self._create(['Name'], self.__create_course_)
	def __create_course_(self):
		try:
			name = self.fields['Name'].get()

			self.db.insert_disciplina(name)

			self.promptScreen.destroy()
			self.screenFrame.grid_forget()
			self.__init__(self.title, self.icon, self.geometry)
			self._start()
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'Invalid code!')

	def __add_language(self):
		self._create(['Name', 'Compile/Run with'], self.__add_language_)
	def __add_language_(self):
		try:
			name, run = self.fields['Name'].get(), self.fields['Compile/Run with'].get()

			self.db.insert_language(name, run)
			self.promptScreen.destroy()
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'Failed!')

	def __create_class(self):
		self.value = [StringVar(), StringVar()]
		try:
			try:
				optionsPro = [(lambda p: '{} - {}'.format(*p))(p) for p in self.db.get_users(get=['codigo','nome'], table='PROFESSOR')]
				self.value[0].set(optionsPro[0])
				optionsPro = (self.value[0], *optionsPro)
			except Exception as e:
				TkMessageBox.showinfo('Error', 'No professors found; first insert a professor')
				raise ValueError(e)

			try:
				optionsCou = [(lambda c: '{} - {}'.format(*c))(c) for c in self.db.get_courses(get=['codigo','nome'])]
				self.value[1].set(optionsCou[0])
				optionsCou = (self.value[1], *optionsCou)
			except Exception as e:
				TkMessageBox.showinfo('Error', 'No courses found; first create a course')
				raise ValueError(e)
			self._create(('Name',('Professor', OptionMenu, optionsPro), ('Course', OptionMenu, optionsCou)), self.__create_class_)
		except Exception as e:
			print(e)

	def __create_class_(self):
		try:
			classname = self.fields['Name'].get()
			if len(classname) != 1: raise ValueError('No class input')
			classname = ord(classname.upper())
			professor = self.value[0].get()
			course = self.value[1].get()

			self.db.insert_class(classname, professor, course)
			self.promptScreen.destroy()
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'Invalid class')
