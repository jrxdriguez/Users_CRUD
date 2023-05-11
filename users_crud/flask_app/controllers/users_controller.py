from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.users import User


@app.route('/')
def display_users():
    
    all_users = User.get_all_users()
    return render_template('read.html', all_users = all_users)


@app.route('/add_user', methods=['POST'])
def new_user():
    user_data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    User.add_user(request.form)
    return redirect('/')


@app.route('/new')
def form():
    return render_template('create.html')


@app.route('/display_user/<int:id>')
def display_one(id):
    user_data = {'id' : id}

    one_user = User.get_one_user(user_data)
    return render_template('display_user.html', one_user = one_user)


@app.route('/edit_user/<int:id>')
def edit_user(id):
    user_data = {'id' : id}

    one_user = User.get_one_user(user_data)

    return render_template('edit_user.html', one_user = one_user)


@app.route('/update_user/<int:id>', methods=['POST'])
def update_user(id):
    user_data = {
        "id" : id,
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'] 
    }

    User.update_user(user_data)
    return redirect(f'/display_user/{id}')


@app.route('/delete_user/<int:id>')
def delete_user(id):
    user_data = {'id' : id}
    User.delete_user(user_data)

    return redirect('/')