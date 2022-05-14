import os
from flask import Flask
from database import db
from controllers import ContactsController, UserController,FlashingController, CalcController

###### CONFIGURACOES ######
app = Flask('app')
app.config['SECRET_KEY'] = 'qEChL7R3SpF72cEA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

###### ROTAS ######
@app.route('/')
def index():
  return ContactsController.index()

@app.route('/create', methods=['POST'])
def create():
  return ContactsController.create()

@app.route('/delete/<int:id>')
def delete(id):
  return ContactsController.delete(id)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
  return ContactsController.update(id)

@app.route('/login')
def login():
  return UserController.login()

@app.route('/register')
def register():
  return UserController.register()

@app.route('/signup', methods=['POST'])
def signup():
  return UserController.signup()

@app.route('/signin', methods=['POST'])
def signin():
  return UserController.signin()

@app.route('/logout')
def logout():
  return UserController.logout()

@app.route('/flashing')
def flashing():
  return FlashingController.flashing()

@app.route('/hello/<name>')
def hello(name):
  return FlashingController.hello(name)

@app.route('/sum/<int:num1>/<int:num2>')
def sum(num1, num2):
  return CalcController.sum(num1, num2)

@app.route('/sub/<int:num1>/<int:num2>')
def sub(num1, num2):
  return CalcController.sub(num1, num2)

@app.route('/mult/<int:num1>/<int:num2>')
def mult(num1, num2):
  return CalcController.mult(num1, num2)

@app.route('/div/<int:num1>/<int:num2>')
def div(num1, num2):
  return CalcController.div(num1, num2)



###### INICIALIZACAO ######
with app.app_context():
  db.create_all()

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)

# https://replit.com/@ednascimento/todo-db#main.py
