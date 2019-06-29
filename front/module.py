from tkinter import *
from tkinter import messagebox as TkMessageBox
from front.management import ManagementScreen
from tkinter import filedialog

class ModuleScreen(ManagementScreen):
	def __init__(self, code, module_number, title='', icon=None, geometry=''):
		self._init(title, icon, geometry)
		self.code = code
		self.module_number = module_number

		for i,c in enumerate([('Work code','Description')] + self.db.get_work(get=['codigo','descrição'], disciplina=self.code, modulo=self.module_number)):
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
		self._create(('Number', ('Description', Button, dict(text='Choose file', command=self.__browse_work)),'Begin', 'End'), self.__create_work_)
	def __create_work_(self):
		try:
			
			auxfields = dict()
			for k in self.fields: auxfields[k] = self.fields[k].get() if type(self.fields[k]) != Button else self.filename
			auxfields['codigo'] = auxfields.pop('Number')
			auxfields['visibilidade'] = 'S'
			auxfields['prova'] = 'N'
			auxfields['modulo'] = self.module_number
			auxfields['disciplina'] = self.code

			self.db.insert_work(**auxfields)
			self.promptScreen.destroy()
			self.screenFrame.grid_forget()
			self.__init__(self.code, self.module_number, self.title, self.icon, self.geometry)
			self._start()
		except Exception as e:
			print(e)
			TkMessageBox.showinfo('Error', 'Wrong input')
		finally:
			self.db.commit()
	def __browse_work(self, e=None):
		file = filedialog.askopenfile(
				parent=self.screenFrame,
				filetypes=(('Arquivos PDF', '*.pdf'),('Todos os arquivos', '*.*')),
				title='Escolha um arquivo'
				)
		self.filename = file.name
		self.fields['Description'].config(text=file.name.split('/')[-1])

