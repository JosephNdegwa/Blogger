from app import create_app, db
from app.models import User, Post, Comment
from flask_script import Manager,Server

app = create_app()


manager = Manager(app)
manager.add_command('server',Server)


    



@manager.shell
def make_shell_context():
    print("Hello world")
    return {'db': db, 'User': User, 'Post': Post, 'Comment': Comment}
if __name__ == '__main__':
 manager.run()