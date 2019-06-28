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
			('Create problem', self.create_problem),
			('Manage work', self.manage_work)
		]
		for b in buttons:
			Button(self.screenFrame, text=b[0], command=b[1]).grid()

	def create(self, fieldsNames, whichfun, buttonLabel='Create'):
		self.promptScreen = Toplevel(self.window)
		self.promptScreen.grab_set()
		self.fields = dict((lambda f: (f, Entry(self.promptScreen)))(f) for f in fieldsNames)
		for i,key in enumerate(self.fields):
			Label(self.promptScreen, text=key).grid(row=i, column=0)
			self.fields[key].grid(row=i, column=1)
		Button(self.promptScreen, text=buttonLabel, command=whichfun).grid()

	def create_course(self):
		self.create(['Code','Name'], self.__create_course)
	def __create_course(self):
		try:
			code, name = str(int(self.fields['Code'].get())), self.fields['Name'].get()
			self.db.execute('insert into DISCIPLINA values ('+code+', \''+name+'\');')
			self.db.commit()
			self.promptScreen.destroy()
		except:
			TkMessageBox.showinfo('Error', 'Invalid code!')
		finally:
			pass

	def create_module(self):
		self.create(['Course code', 'Number'], self.__create_module)
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
		self.create(['Number', 'Description', 'Begin', 'End', 'Module', 'Course'], self.__create_work)
	def __create_work(self):
		try:
			values = ','.join([(lambda k: '\''+self.fields[k].get()+'\'' if not self.fields[k].get().isdigit() else self.fields[k].get())(k) for k in self.fields])
			self.db.execute('insert into LISTA (cod, descr, data_hr_inicio, data_hr_fim, modulo_cod, disc_cod, visibilidade, prova) values ('+values+', \'S\', \'N\');')
			self.db.commit()
			self.promptScreen.destroy()
		except:
			TkMessageBox.showinfo('Error', 'Wrong input')
		finally:
			pass

	def create_problem(self):
		self.create(['Number','Work number','Title','Description','Dificuldade','Limite de memória','Limite de tempo'], self.__create_problem)
	def __create_problem(self):
		try:
			values = ','.join([(lambda k: '\''+self.fields[k].get()+'\'' if not self.fields[k].get().isdigit() else self.fields[k].get())(k) for k in self.fields])
			self.db.execute('insert into PROBLEMA values ('+values+');')
			self.db.commit()
			self.promptScreen.destroy()
		except:
			TkMessageBox.showinfo('Error', 'Wrong input')
		finally:
			pass

	def manage_work(self):
		self.create(['Number'], self.__manage_work, buttonLabel='Get')
	def __manage_work(self):
#			values = ','.join([(lambda k: '\''+self.fields[k].get()+'\'' if not self.fields[k].get().isdigit() else self.fields[k].get())(k) for k in self.fields])
#self.promptScreen.destroy()
		try:
			self.db.execute('select cod,descr from LISTA where cod = '+self.fields['Number'].get()+';')
			for l in self.db.fetchall():
				for i in l:
					Label(self.promptScreen, text=i).grid()
		except:
			TkMessageBox.showinfo('Error', 'Wrong input')
		finally:
			pass
