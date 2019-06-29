from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.management import ManagementScreen

class WorkScreen(ManagementScreen):
	def __init__(self, code, module_number, work_code, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)
		self.code = code
		self.module_number = module_number
		self.work_code = work_code

		self.db.select('cod, titulo, descr, dificul', 'PROBLEMA', where='lista_cod = '+str(self.work_code))
		for i,c in enumerate([('Problem code', 'Title', 'Description', 'Dificulty')] + self.db.fetchall()):
			Label(self.screenFrame, text=str(c[0]), bd=7).grid(row=i, column=0)
			Label(self.screenFrame, text=str(c[1]), bd=7).grid(row=i, column=1)
			Label(self.screenFrame, text=str(c[2]), bd=7).grid(row=i, column=2)
			Label(self.screenFrame, text=str(c[3]), bd=7).grid(row=i, column=3)
			if i:
				callback = lambda problem_code=c[0]: self.__manage_problem(problem_code)
				Button(self.screenFrame, text='Manage', padx=7, command=callback).grid(row=i, column=4)

		# Cria botão
		buttons = (
			('Back', self._back),
			('Create problem', self.__create_problem),
			('Change visibility', self.__change_visibility),
			('Change to contest', self.__change_to_contest)
			)
		for b in buttons:
			Button(self.screenFrame, text=b[0], command=b[1]).grid(sticky=W)

	def __create_problem(self):
		self._create(['Number','Title','Description','Dificuldade','Limite de memória','Limite de tempo'], self.__create_problem_)
	def __create_problem_(self):
		try:
			values = ','.join([(lambda k: '\''+self.fields[k].get()+'\'' if not self.fields[k].get().isdigit() else self.fields[k].get())(k) for k in self.fields])
			self.db.execute('insert into PROBLEMA (cod, titulo, descr, dificul, limite_mem, limite_temp, lista_cod) values ('+values+', '+str(self.work_code)+');')
			self.promptScreen.destroy()
			self.screenFrame.grid_forget()
			self.__init__(self.code, self.module_number, self.work_code, self.title, self.icon, self.geometry)
			self._start()
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'Wrong input')
		finally:
			self.db.commit()

	def __change_visibility(self):
		try:
			self.db.select('visibilidade', 'LISTA', where='cod = '+str(self.work_code))
			visibility = "'S'" if self.db.fetchone()[0] == 'N' else "'N'"
			self.db.execute('update LISTA set visibilidade = '+visibility+' where cod = '+str(self.work_code))
			TkMessageBox.showinfo('Success', 'Updated work; now it is '+('visible' if visibility == "'S'" else 'not visible'))
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'Error')
		finally:
			self.db.commit()
	
	def __change_to_contest(self):
		try:
			self.db.select('prova', 'LISTA', where='cod = '+str(self.work_code))
			prova = "'S'" if self.db.fetchone()[0] == 'N' else "'N'"
			self.db.execute('update LISTA set prova = '+prova+' where cod = '+str(self.work_code))
			TkMessageBox.showinfo('Success', 'Updated work; now it is a '+('contest' if prova == "'S'" else 'commom work'))
		except Exception as e:
			print(e)
		finally:
			self.db.commit()

	def __manage_problem(self, problem_code):
		print(problem_code)
		promptScreen = Toplevel(self.window)
		promptScreen.grab_set()

		Button(promptScreen, text='Delete', command=lambda pcode=problem_code: self.__delete(pcode)).grid()
		Button(promptScreen, text='Update', command=lambda pcode=problem_code: self.__update(pcode)).grid()
		Button(promptScreen, text='End... Please...', command=promptScreen.destroy).grid()

	def __delete(self, problem_code):
		pass
	def __update(self, problem_code):
		pass
	





