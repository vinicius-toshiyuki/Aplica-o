from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.management import ManagementScreen

class CourseScreen(ManagementScreen):
	def __init__(self, code, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)
		self.code = code

		self.db.select('*', 'MODULO', where='disc_cod = '+str(self.code))
		for i,c in enumerate([('Module number',)] + self.db.fetchall()):
			Label(self.screenFrame, text=str(c[0]), bd=1).grid(row=i, column=0)
			if i:
				callback = lambda module_number=c[0]: self._stop(['module', self.code, module_number])
				Button(self.screenFrame, text='Manage', padx=1, command=callback).grid(row=i, column=2)

		# Cria botão
		buttons = (
			('Back', self._back),
			('Create module', self.__create_module)
			)
		for b in buttons:
			Button(self.screenFrame, text=b[0], command=b[1]).grid(sticky=W)

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

