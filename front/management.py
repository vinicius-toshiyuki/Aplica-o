from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.app import App

class ManagementScreen(App):
	def __init__(self, title='', icon=None, geometry='400x250'):
		self._init(title, icon, geometry)

		# Cria botão
		buttons = [
			('Back', self.back),
			('Create course', self.create_course),
			('Create module', self.create_module),
			('Create work', self.create_work),
			('Create problem', self.create_problem)
		]
		for b in buttons:
			Button(self.screenFrame, text=b[0], command=b[1]).grid()

	def create(self, fieldsNames, whichfun):
		self.promptScreen = Toplevel(self.window)
		self.promptScreen.grab_set()
		self.fields = dict((lambda f: (f, Entry(self.promptScreen)))(f) for f in fieldsNames)
		for i,key in enumerate(self.fields):
			Label(self.promptScreen, text=key).grid(row=i, column=0)
			self.fields[key].grid(row=i, column=1)
		Button(self.promptScreen, text='Create', command=whichfun).grid()

	def create_course(self):
		self.create(['Code','Name'], self.__create_course)
	def __create_course(self):
		code, name = str(int(self.fields['Code'].get())), self.fields['Name'].get()

		self.db.execute('insert into DISCIPLINA select '+code+', \''+name+'\' from DISCIPLINA where 0 in select count(*) from DISCIPLINA where code = '+code+');')
		try:
			pass
			
			'''
			self.db.select('count(*)', 'DISCIPLINA', where='cod = '+str(code))
			
			if self.db.fetchone()[0]:
				TkMessageBox.showinfo('Error', 'Code already registered!')
			else:
				self.db.insert('DISCIPLINA', (code, name))
				self.db.commit()
				self.promptScreen.destroy()'''
		except:
			TkMessageBox.showinfo('Error', 'Invalid code')
		finally:
			pass

	def create_module(self):
		self.Create(['Course code', 'Number'], self.__create_module)
	def __create_module(self):
		try:
			number, course_code = str(int(self.fields['Number'].get())), str(int(self.fields['Course code'].get()))
			self.db.execute('insert into MODULO select '+number+', '+course_code+' from DISCIPLINA where cod = '+course_code+';')
			self.db.commit()
			self.promptScreen.destroy()
		except:
			TkMessageBox.showinfo('Error', 'Unregistered course or module already exists!')
		finally:
			pass
	def create_work(self):
		pass
	def __create_work(self):
		pass
	def create_problem(self):
		pass
	def __create_problem(self):
		pass
