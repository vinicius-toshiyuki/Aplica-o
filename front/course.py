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

		self.db.select('nome', 'LING_PROGR_DISCI join LING_PROGR on LING_PROGR_COD = COD', where='disc_cod = '+str(self.code))
		languages = self.db.fetchall()
		for l in languages:
			Label(self.screenFrame, text=l[0], bd=7).grid(sticky=W)

	def __create_module(self):
		self._create(['Number'], self.__create_module_)
	def __create_module_(self):
		try:
			number, course_code = str(int(self.fields['Number'].get())), str(self.code)
			self.db.execute('insert into MODULO select '+number+', '+course_code+' from DISCIPLINA where cod = '+course_code+';')
			self.promptScreen.destroy()
			self.screenFrame.grid_forget()
			self.__init__(self.code, self.title, self.icon, self.geometry)
			self._start()
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'Module already exists!')
		finally:
			self.db.commit()

	def __choose_language(self):
		promptScreen = Toplevel(self.window)
		promptScreen.grab_set()

		self.db.select('nome, cod', 'LING_PROGR')
		languages = self.db.fetchall()

		options = [(lambda l: str(l[1])+' - '+l[0])(l) for l in languages]

		default = StringVar(promptScreen)
		default.set('')
		OptionMenu(promptScreen, default, *options).grid(sticky=W)
		Button(promptScreen, text='Choose', command=lambda selected=default: self.__choose_language_(int(selected.get().split('-')[0]))).grid(sticky=W)

	def __choose_language_(self, language_code):
		try:
			self.db.insert('LING_PROGR_DISCI', (language_code, self.code))
		except Exception as e:
			print(e)
		finally:
			self.db.commit()
			self.screenFrame.grid_forget()
			self.__init__(self.code, self.title, self.icon, self.geometry)
			self._start()

