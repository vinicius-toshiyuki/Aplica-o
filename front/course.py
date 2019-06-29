from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.management import ManagementScreen

class CourseScreen(ManagementScreen):
	def __init__(self, code, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)
		self.code = code

		for i,c in enumerate([('Module number',)] + self.db.get_modules(get='numero',disciplina=self.code)):
			Label(self.screenFrame, text=str(c[0]), bd=1).grid(row=i, column=0)
			if i:
				callback = lambda module_number=c[0]: self._stop(['module', self.code, module_number])
				Button(self.screenFrame, text='Manage', padx=1, command=callback).grid(row=i, column=2)

		# Cria botão
		buttons = (
			('Back', self._back),
			('Create module', self.__create_module),
			('Choose language', self.__choose_language)
			)
		for b in buttons:
			Button(self.screenFrame, text=b[0], command=b[1]).grid(sticky=W)

		for l in self.db.get_languages(get='nome', disciplina=self.code):
			Label(self.screenFrame, text=l[0], bd=7).grid(sticky=W)

	def __create_module(self):
		self._create(['Number'], self.__create_module_)
	def __create_module_(self):
		try:
			number, course_code = self.fields['Number'].get(), self.code
			self.db.insert_module(number, course_code)
			self.promptScreen.destroy()
			self.screenFrame.grid_forget()
			self.__init__(self.code, self.title, self.icon, self.geometry)
			self._start()
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'Module already exists!')

	def __choose_language(self):
		promptScreen = Toplevel(self.window)
		promptScreen.grab_set()

		options = [(lambda l: str(l[1])+' - '+l[0])(l) for l in self.db.get_language_options(get=['nome','codigo'])]

		default = StringVar(promptScreen)
		default.set('')
		OptionMenu(promptScreen, default, *options).grid(sticky=W)
		Button(promptScreen, text='Choose', command=lambda selected=default: self.__choose_language_(selected.get().split('-')[0])).grid(sticky=W)

	def __choose_language_(self, language_code):
		try:
			if not len(language_code):
				raise ValueError('Language not selected')
			self.db.choose_language(self.code, language_code)
			self.screenFrame.grid_forget()
			self.__init__(self.code, self.title, self.icon, self.geometry)
			self._start()
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Erro', 'Select a language')

