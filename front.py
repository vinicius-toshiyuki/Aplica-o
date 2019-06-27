from app import App
from login import LogInScreen
from home import HomeScreen
from register import RegisterScreen
from problems import ProblemsScreen
from users import UsersScreen
from management import ManagementScreen

app = App(icon='índice.gif', title='Corretor')
app.add_handler(None, LogInScreen)
app.add_handler('home', HomeScreen)
app.add_handler('register', RegisterScreen)
app.add_handler('problems', ProblemsScreen)
app.add_handler('users', UsersScreen)
app.add_handler('management', ManagementScreen)
app.add_handler('logout', app.handler[None])
app.window_start()






















