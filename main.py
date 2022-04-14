from flask import Flask, render_template, request, redirect

from flask_sqlalchemy import SQLAlchemy

app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))
  password = db.Column(db.String(50))
  created_at = db.Column(db.String(50))
  updated_at = db.Column(db.String(50))

class Contacts(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))
  phone = db.Column(db.String(50))
  image = db.Column(db.String(50))
  user_id = db.Column(db.Integer)
  created_at = db.Column(db.String(50))
  updated_at = db.Column(db.String(50))

@app.route('/')
def index():
  contacts = Contacts.query.all()
  return render_template(
    'index.html',
    contacts=contacts
  )

@app.route('/create', methods=['POST'])
def create():
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')  
  new_cont = Contacts(
    name=name, 
    email=email, 
    phone=phone,
  )
  db.session.add(new_cont)
  db.session.commit()
  return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
  cont = Contacts.query.filter_by(id=id).first()
  db.session.delete(cont)
  db.session.commit()
  return redirect('/')


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
  name = request.form.get('name')
  email = request.form.get('email')
  phone = request.form.get('phone')
  cont = Contacts.query.filter_by(id=id).first()
  cont.name = name
  cont.email = email
  cont.phone = phone
  db.session.commit()  
  return redirect('/')

# IMPORTANTE V
if __name__ == '__main__':
  db.create_all()
  app.run(host='0.0.0.0', port=8080)