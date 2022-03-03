from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init(input())
db_session = db_session.create_session()

for user in db_session.query(User).all():
    if user.address == 'module_1':
        print(user)

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
global_init(input())

for job in create_session().query(Jobs).all():
    if job.work_size < 20 and job.is_finished != True:
        print(f'<Job> {job.job}')

for j in [2, 4, 5, 1, 6, 99]:
    print(j)