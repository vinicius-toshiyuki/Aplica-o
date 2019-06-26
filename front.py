from app import App
from login import LogInScreen
from home import HomeScreen
from register import RegisterScreen

app = App(icon='índice.gif', title='Corretor')
app.add_handler(None, LogInScreen)
app.add_handler('autenticate', HomeScreen)
app.add_handler('register', RegisterScreen)
app.add_handler('logout', app.handler[None])
app.start()






















