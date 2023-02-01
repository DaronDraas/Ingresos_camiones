from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.ex3 import Truck
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    user=User.get_by_id(data)
    magazines = User.get_all_magazines()
    return render_template("index.html",user=user, magazines=magazines)

# @app.route('/datos')
# def datos():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data ={
#         'id': session['user_id']
#     }
#     user=User.get_by_id(data)
#     return render_template("dashboard.html",user=user)

@app.route('/login',methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dash')

@app.route('/register',methods=['POST'])
def register():
    if not User.validate_register(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id

    return redirect('/dashboard')

@app.route('/create', methods=['POST'])
def crear():
    return render_template('crear_cuenta.html')



