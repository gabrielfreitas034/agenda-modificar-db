from flask import Flask, render_template, request, redirect

from flask_sqlalchemy import SQLAlchemy

app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  email = db.Column(db.String())
  password = db.Column(db.String())
  created_at = db.Column(db.String())
  updated_at = db.Column(db.String())
  
class contacts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  email = db.Column(db.String())
  phone = db.Column(db.String())
  image = db.Column(db.String())
  user_id = db.Column(db.Integer, primary_key=True)
  created_at = db.Column(db.String())
  updated_at = db.Column(db.String())
  
contacts = [
  { 
    'name': 'João da Silva',
    'email': 'joao@gmail.com',
    'phone': '(16) 99922-1122'
  },
  { 
    'name': 'Maria Souza',
    'email': 'maria@gmail.com',
    'phone': '(16) 99922-3333'
  }
]

@app.route('/')
def index():
  return render_template(
    'index.html', 
    contacts=contacts
  )

@app.route('/create', methods=['POST'])
def create():
  name= request.form.get('name')
  email= request.form.get('email')
  phone= request.form.get('phone')
  contacts.append({
    'name': name,
    'email': email,
    'phone': phone
  })
  return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
  contacts.pop(index)
  return redirect('/')

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
  name = request.form.get('name')
  contacts[index]['name'] = name
  email = request.form.get('email')
  contacts[index]['email'] = email
  phone = request.form.get('phone')
  contacts[index]['phone'] = phone
  return redirect('/')
  
if __name__ == '__main__':
  db.create_all()
  app.run(host='0.0.0.0', port=8080)
