from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.renamer import Renamer
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/new/name')
def new_renamer():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "id": session['user_id']
    }
    return render_template('new_renamer.html', user=User.get_by_id(data))

@app.route('/create/renamer', methods=['POST'])
def create_renamer():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Renamer.validate_renamer(request.form):
        return redirect('/new/name')
    data ={
        "name": request.form["name"],
        "date": request.form["date"],
        "unixdate": unix(request.form["date"]),
        "user_id": session["user_id"]
    }
    Renamer.save(data)
    return redirect('/dashboard')

def unix(x):
    import datetime
    date_example = str(x)
    date_format = datetime.datetime.strptime(date_example,"%Y-%m-%dT%H:%M")
    unix_time = datetime.datetime.timestamp(date_format)
    return(unix_time)




@app.route('/edit/<int:id>')
def edit_renamer(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "id": id
    }
    user_data ={
        "id":session['user_id']
    }
    return render_template("edit_renamer.html", edit=Renamer.get_one(data), user=User.get_by_id(user_data))

@app.route('/update/renamer', methods=['POST'])
def update_renamer():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Renamer.validate_renamer(request.form):
        return redirect('/edit/<int:id>')
    data ={
        "name": request.form["name"],
        "date": request.form["date"],
        "unixdate": unix(request.form["date"]),
        "id": request.form['id']
    }
    Renamer.update(data)
    return redirect ('/dashboard')


@app.route('/show/<int:id>')
def show_renamer(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_renamer.html", renamer=Renamer.get_one(data), user=User.get_by_id(user_data))



@app.route('/delete/renamer/<int:id>')
def delete_renamer(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Renamer.delete(data)
    return redirect('/dashboard')