from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
#from flask_app.models import user
from flask_app.models.user import User
import datetime

class Truck:
    db = 'example3'
    def __init__(self, data):
        self.id = data['id']
        self.patente = data['patente']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
    
    @classmethod
    def save(cls, data):
        query = """INSERT INTO camiones ( patente, user_id) VALUES (%(patente)s, %(user_id)s);"""
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM camiones
        LEFT JOIN users ON camiones.user_id = users.id;"""
        results =  connectToMySQL(cls.db).query_db(query)
        all_camiones = []
        for row in results:
            camion = cls(row)
            if row['user_id']:
                data2 = {
                    'id': row['user_id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'password': row['password'],
                    'updated_at': row['users.updated_at'],
                    'created_at': row['users.created_at'],
                }
            #camion.user = (user.User(data2))
                camion.user = User(data2)
                all_camiones.append( camion )
        return all_camiones
    
    @classmethod
    def get_one(cls, data):
        query = """SELECT * FROM camiones WHERE id = %(id)s;"""
        result =connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def show(cls, data):
        query = """
            SELECT camiones.*, users.first_name, users.last_name
            FROM camiones
            LEFT JOIN users ON camiones.user_id = users.id
            WHERE camiones.patente LIKE %s
        """
        search_query = '%{}%'.format(data)
        result = connectToMySQL(cls.db).query_db(query, (search_query,))
        if result:
            trucks = []
            for row in result:
                truck = cls(row)
                if row['user_id']:
                    data2 = {
                        'id': row['user_id'],
                        'first_name': row['first_name'],
                        'last_name': row['last_name'],
                    }
                    truck.user = User(data2)
                trucks.append(truck)
            return trucks
        else:
            return None

    @classmethod
    def actualizar(cls, data):
        flash("Correcta Actualización")
        data = data.to_dict()  # Convert ImmutableMultiDict to a regular dictionary
        data["updated_at"] = datetime.datetime.now()
        query = """UPDATE camiones SET patente=%(patente)s, updated_at=%(updated_at)s WHERE id = %(id)s;"""
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def destroy(cls,data):
        query = """DELETE FROM camiones WHERE id = %(id)s;"""
        return connectToMySQL(cls.db).query_db(query,data)

    # @classmethod
    # def granted(cls,data):
    #     query = "DELETE FROM deseos WHERE id = %(id)s;"
    #     return connectToMySQL(cls.db).query_db(query,data)

    # class Post(db.Model):
    #     __searchable__= ["patente"]
    #     id =

    @staticmethod
    def validate_deseo(deseo):
        is_valid = True
        # if len(deseo['nd']) < 7:
        #     is_valid = False
        #     flash("Item name must be at least 3 characters","deseo")
        if len(deseo['patente']) < 3:
            is_valid = False
            flash(u"Description must be at least 10 characters","camiones")
        return is_valid