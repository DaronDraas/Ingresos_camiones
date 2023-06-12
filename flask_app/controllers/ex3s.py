from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.ex3 import Truck
from flask_app.models.user import User
import datetime

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

@app.route('/search', methods=['POST'])
def search():
    if 'user_id' not in session:
        return redirect('/logout')
    
    # Retrieve the search query from the form data
    search_query = request.form.get('search_query')
    
    # Perform the necessary search logic or database query based on the search query
    results = Truck.show(search_query)
    
    # Return the search results or redirect to an appropriate page
    return render_template('search_results.html', results=results)

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

@app.route('/modify-time/<int:id>', methods=['POST'])
def modify_time(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    truck = Truck.get_one(data)
    truck.modified_at = datetime.datetime.now()
    # Update the modified time in the database or perform any other desired modifications
    return redirect('/dash')

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