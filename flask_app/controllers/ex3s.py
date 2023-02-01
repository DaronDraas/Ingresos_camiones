from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.ex3 import Truck
from flask_app.models.user import User

@app.route('/')
def logstart():
    return render_template("index.html")

@app.route('/dash')
def dash():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    user = User.get_by_id(data)
    # magazines = User.get_all_magazines()
    camiones = Truck.get_all()
    # print(camiones[1].user.created_at)
    # print(camiones[1].created_at)
    # print(magazines[0])
    return render_template("dashboard.html", user=user, camiones=camiones)

@app.route('/logout')
def index():
    return redirect('/')

@app.route('/new')
def create():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "id": session['user_id']
    }
    user = User.get_by_id(data)
    return render_template('ingresar_datos.html', user=user)

@app.route('/wishes',methods=['POST'])
def all_magazines():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Truck.validate_deseo(request.form):
        return redirect('/')
    data = {
        # "nd": int(request.form["nd"]),
        "patente": request.form["patente"],
        "user_id": session["user_id"]
    }
    Truck.save(data)
    return redirect('/dash')

@app.route('/destroy/<int:id>')
def destroy(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data={
        'id':id
    }
    Truck.destroy(data)
    return redirect('/dash')

@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "id":id
    }
    return render_template("editar_datos_salida.html", truck = Truck.get_one(data), user = User.get_by_id(data))

# @app.route('/editar')
# def user_edit():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data ={
#         "id": session['user_id']
#     }
#     user = User.get_by_id(data)
#     return render_template('editar_datos_salida.html', user=user)

@app.route('/actualizar/<int:id>',methods=['POST'])
def actualizar(id):
    truck_id = id
    if 'user_id' not in session:
        return redirect('/logout')
    if not Truck.validate_deseo(request.form):
        return redirect(f'/edit/{truck_id}')
#     data = { 
#     "id": session['user_id'],
#     "patente": request.form["patente"],
# }
    Truck.actualizar(request.form)
    return redirect('/dash')

# @app.route('/search',methods=['POST'])
# def buscar():
#     posts = Post.query

# @app.route('/count/')
# def contador():
#         if 'visitas' in session:
#             print('la llave existe!')
#             session['visitas'] +=1
#         else:
#             print("la llave 'key_name' NO existe")
#             session['visitas'] = 1

#         return redirect('/wishes')

# @app.route('/granted/<int:id>')
# def granted(id):
#     if 'user_id' not in session:
#             return redirect('/logout')
#     data={
#         'id':id
#     }
#     Deseo.destroy(data)


#     return redirect('/wishes') 
