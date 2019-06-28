from front.app import App
from front.login import LogInScreen
from front.home import HomeScreen
from front.register import RegisterScreen
from front.problems import ProblemsScreen
from front.users import UsersScreen
from front.management import ManagementScreen
from front.course import CourseScreen
from front.module import ModuleScreen
from front.work import WorkScreen

def main():
    app = App(icon='índice.gif', title='Corretor')
    app.add_handler(None, LogInScreen)
    app.add_handler('home', HomeScreen)
    app.add_handler('register', RegisterScreen)
    app.add_handler('problems', ProblemsScreen)
    app.add_handler('users', UsersScreen)
    app.add_handler('management', ManagementScreen)
    app.add_handler('course', CourseScreen)
    app.add_handler('module', ModuleScreen)
    app.add_handler('work', WorkScreen)
    app.add_handler('logout', app.handler[None])
    app.window_start()

if __name__ == '__main__':
    main()




















