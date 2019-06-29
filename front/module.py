from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.management import ManagementScreen

class ModuleScreen(ManagementScreen):
	def __init__(self, code, module_number, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)
		self.code = code
		self.module_number = module_number

		print('Aqui:',self.db.get_work(get=['codigo','descrição'], e={'disciplina':self.code, 'modulo':self.module_number}))
		self.db.select('cod, descr', 'LISTA', where='disc_cod = '+str(self.code)+' and modulo_cod = '+str(self.module_number))
		for i,c in enumerate([('Work code','Description')] + self.db.fetchall()):
			Label(self.screenFrame, text=str(c[0]), bd=1).grid(row=i, column=0)
			Label(self.screenFrame, text=str(c[1]), bd=1).grid(row=i, column=1)
			if i:
				callback = lambda work_code=c[0]: self._stop(['work', self.code, self.module_number, work_code])
				Button(self.screenFrame, text='Manage', padx=1, command=callback).grid(row=i, column=2)

		# Cria botão
		buttons = (
			('Back', self._back),
			('Create work', self.__create_work)
			)
		for b in buttons:
			Button(self.screenFrame, text=b[0], command=b[1]).grid(sticky=W)

	def __create_work(self):
		self._create(['Number', 'Description', 'Begin', 'End'], self.__create_work_)
	def __create_work_(self):
		try:
			values = ','.join([(lambda k: '\''+self.fields[k].get()+'\'' if not self.fields[k].get().isdigit() else self.fields[k].get())(k) for k in self.fields] + [str(self.module_number), str(self.code)])
			self.db.execute('insert into LISTA (cod, descr, data_hr_inicio, data_hr_fim, modulo_cod, disc_cod, visibilidade, prova) values ('+values+', \'S\', \'N\');')
			self.promptScreen.destroy()
			self.screenFrame.grid_forget()
			self.__init__(self.code, self.module_number, self.title, self.icon, self.geometry)
			self._start()
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'Wrong input')
		finally:
			self.db.commit()

