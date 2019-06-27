from tkinter import *
from tkinter import messagebox as TkMessageBox
from app import App

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

	def create_course(self):
		self.promptScreen = Toplevel(self.window)
		self.promptScreen.grab_set()

		self.fields = {
			'Code': Entry(self.promptScreen),
			'Name': Entry(self.promptScreen)
		}
		for i,key in enumerate(self.fields):
			Label(self.promptScreen, text=key).grid(row=i, column=0)
			self.fields[key].grid(row=i, column=1)

		Button(self.promptScreen, text='Create', command=self.__create_course).grid()
	def __create_course(self):
		try:
			code = int(self.fields['Code'].get())
			name = self.fields['Name'].get()
			print('Code:', code, '\nName:', name)

			self.db.select('count(*)', 'DISCIPLINA', where='cod = '+str(code))
			
			if self.db.fetchone()[0]:
				TkMessageBox.showinfo('Error', 'Code already registered!')
			else:
				self.db.insert('DISCIPLINA', (code, name))
				self.db.commit()
		except:
			TkMessageBox.showinfo('Error', 'Invalid code')
		finally:
			self.promptScreen.destroy()
	def create_module(self):
		self.promptScreen = Toplevel(self.window)
		self.promptScreen.grab_set()

		self.fields = {
			'Course code': Entry(self.promptScreen),
			'Number': Entry(self.promptScreen)
		}
		for i,key in enumerate(self.fields):
			Label(self.promptScreen, text=key).grid(row=i, column=0)
			self.fields[key].grid(row=i, column=1)

		Button(self.promptScreen, text='Create', command=self.__create_course).grid()
	def __create_module(self):
		pass
		'''
		try:
			course_code = int(self.fields['Course code'].get())
			number = self.fields['Number'].get()
			print('Course code:', course_code, '\nNumber:', number)

			self.db.select('count(*)', 'DISCIPLINA', where='cod = '+str(course_code))
			self.db.execute('
				insert into MODULO values
				( ----- number, course_code)

					')
			
			if self.db.fetchone()[0]:
				
			else:
				TkMessageBox.showinfo('Error', 'Unregistered course!')
		except:
			TkMessageBox.showinfo('Error', 'Invalid code ?')
		finally:
			self.promptScreen.destroy()'''
	def create_work(self):
		pass
	def __create_work(self):
		pass
	def create_problem(self):
		pass
	def __create_problem(self):
		pass
	
		'''
	promptScreen = Toplevel()
		promptScreen.grab_set()
		
		entries = []
		for i,j in enumerate(['Old ','New ','Confirm new ']):
			Label(promptScreen, text=j+'password: ').grid(row=i, column=0)
			entries.append(Entry(promptScreen, show='*'))
			entries[-1].grid(row=i, column=1)
		Button(promptScreen, text='Change', command=lambda: ((self.db.execute('update ALUNO set senha = \''+entries[1].get()+'\' where nome = \''+self.username+'\'; select senha from ALUNO where nome = \''+self.username+'\'') or self.db.commit() or self.__change_password() or promptScreen.destroy()) if entries[1].get() == entries[2].get() else TkMessageBox.showinfo('Error', 'Invalid password'))	if entries[0].get() == self.password 	else TkMessageBox.showinfo('Error', 'Wrong password')).grid()
		
	def __change_password(self):
		print('Old pass: ', self.password)
		self.password = (self.db.fetchone())[0]
	
		'''
