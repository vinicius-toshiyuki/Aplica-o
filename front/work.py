from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.management import ManagementScreen

class WorkScreen(ManagementScreen):
	def __init__(self, code, module_number, work_code, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)
		self.code = code
		self.module_number = module_number
		self.work_code = work_code

		res = self.db.get_problem(get=['codigo','titulo','descrição','dificuldade'], lista=self.work_code)
		for i,c in enumerate([('Problem code', 'Title', 'Description', 'Dificulty')] + res): #self.db.fetchall()):
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
		self._create(['Number','Title','Description','Dificulty','Memory limit','Time limit'], self.__create_problem_)
	def __create_problem_(self):
		try:
			number = self.fields['Number'].get()
			title = self.fields['Title'].get()
			description = self.fields['Description'].get()
			dificulty = self.fields['Dificulty'].get()
			lim_mem = self.fields['Memory limit'].get()
			lim_tem = self.fields['Time limit'].get()

			self.db.insert_problem(
					codigo=number,
					lista=self.work_code,
					modulo=self.module_number,
					disciplina=self.code,
					titulo=title,
					descricao=description,
					dificuldade=dificulty,
					limite_de_memoria=lim_mem,
					limite_de_tempo=lim_tem
					)
			self.promptScreen.destroy()
			self.screenFrame.grid_forget()
			self.__init__(self.code, self.module_number, self.work_code, self.title, self.icon, self.geometry)
			self._start()
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'Wrong input')

	def __change_visibility(self):
		try:
			vis = self.db.toggle_visibilitiy(self.code, self.module_number, self.work_code)
			TkMessageBox.showinfo('Success', 'Updated work; now it is '+('visible' if vis else 'not visible'))
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'Error')
	
	def __change_to_contest(self):
		try:
			pro = self.db.toggle_contest(self.code, self.module_number, self.work_code)
			TkMessageBox.showinfo('Success', 'Updated work; now it is a '+('contest' if pro else 'commom work'))
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'Error')

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
	





