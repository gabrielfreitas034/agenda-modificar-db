from flask import render_template, request, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

from models import Contacts, Users, db

class TodoController():
  def index():
    if 'user_id' not in session:
      flash('Usuário não logado', 'error')
      return redirect('/login')   
      
    cont = Contacts.query.filter_by(user_id=session['user_id']).all()
    return render_template(
      'index.html',
      cont=cont
    )

  def create():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')  
    
    new_cont = Contacts(
      name=name, 
      email=email, 
      phone=phone,
      user_id=session['user_id']
    )
    db.session.add(new_cont)
    db.session.commit()
    
    flash('TODO criado com sucesso', 'success')
    return redirect('/')

  def delete(id):
    cont = Contacts.query.filter_by(id=id).first()
    db.session.delete(cont)
    db.session.commit()
    
    flash('TODO deletado com sucesso', 'success')
    return redirect('/')

  def update(id):
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone') 
    
    cont = Contacts.query.filter_by(id=id).first()
    cont.name = name
    cont.email = email
    cont.phone = phone
    db.session.commit()  
    
    flash('TODO editado com sucesso', 'success')
    return redirect('/')
    
class UserController():
  def login():
    return render_template('login.html')

  def register():
    return render_template('register.html')

  def signup():
    name_input = request.form.get('name')
    email_input = request.form.get('email')
    password_input = request.form.get('password')
  
    # Verificar se já existe o email no bd
    user = Users.query.filter_by(
      email=email_input
    ).first()
    if user:
      flash('Este e-mail já existe no sistema', 'error')
      return redirect('/register')
  
    new_user = Users(
      name=name_input,
      email=email_input,
      password=generate_password_hash(password_input)
    )
    db.session.add(new_user)
    db.session.commit()
  
    flash('Usuário criado com sucesso', 'success')
    return redirect('/login')

  def signin():
    email_input = request.form.get('email')
    password_input = request.form.get('password')
  
    # Verificar se existe um usuário com o email
    user = Users.query.filter_by(
      email=email_input
    ).first()
    if not user:
      flash('E-mail não encontrado', 'error')
      return redirect('/login')
  
    # Verificar se senha está correta
    if not check_password_hash(
      user.password,
      password_input
    ):
      flash('Senha incorreta', 'error')
      return redirect('/login')
  
    # Guardar usuário na sessão
    session['user_id'] = user.id
  
    flash(f'Olá, {user.name}', 'info')
    return redirect('/')

  def logout():
    session.pop('user_id', None)
    return redirect('/login')

class FlashingController():
  def flashing():
    flash('Sucesso', 'success')
    return render_template('flashing.html')

  def hello(name):
    flash(f'Bem-vindo, {name}', 'info')
    return render_template('hello.html')

class CalcController():
  def sum(num1, num2):
    sum = num1 + num2 
    return f'Soma = {sum}'

  def sub(num1, num2):
    sub = num1 - num2 
    return f'Sub = {sub}'

  def mult(num1, num2):
    mult = num1 * num2 
    return f'Sub = {mult}'

  def div(num1, num2):
    div = num1 / num2 
    return f'Sub = {div}'
  
  