from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Renamer:
    db_name = 'renamer'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.date = db_data['date']
        self.unixdate = db_data['unixdate']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

#(renamers.py)[create_renamer]
    @classmethod
    def save(cls,data):
        query = "INSERT INTO renamers (name, date, unixdate, user_id) VALUES (%(name)s,%(date)s,%(unixdate)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

#(users.py)(dashboard)
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM renamers;"
        results = connectToMySQL(cls.db_name).query_db(query)
        all_renamers = []
        for row in results:
            all_renamers.append( cls(row) )
        return all_renamers


#(renamers.py)[edit_renamer]
#(renamers.py)[show_renamer]
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM renamers WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

#(renamers.py)[update_renamer]
    @classmethod
    def update(cls, data):
        query = "UPDATE renamers SET name=%(name)s, date=%(date)s, unixdate=%(unixdate)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

#(renamers.py)[delete_renamer]
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM renamers WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)




#(renamers.py)[create_renamer]
#(renamers.py)(update_renamer)
    @staticmethod
    def validate_renamer(renamer):
        is_valid = True
        if len(renamer['name']) < 1:
            is_valid = False
            flash("Please enter a name","renamer")
        if renamer['date'] == "":
            is_valid = False
            flash("Please enter a date","renamer")
        return is_valid