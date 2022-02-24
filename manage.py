from app import create_app, db
from app.models import User, Post, Comment
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = create_app()


manager = Manager(app)
manager.add_command('db',MigrateCommand)


    



@manager.shell
def make_shell_context():
    return dict (app=app,db= db, User= User, Post = Post, Comment= Comment)
if __name__ == '__main__':
 manager.run()