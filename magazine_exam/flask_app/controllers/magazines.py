from flask_app import app
from flask import Flask, render_template, redirect, flash, session, request
from flask_app.models.magazine import Magazine
from flask_app.models.user import User

@app.route('/dashboard/')
def dashboard():
    if 'user_id' not in session:
        flash("Must log in")
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    theUser = User.getId(data)
    userMagazines = Magazine.allMagazines()
    return render_template('dashboard.html', user=theUser, magazines=userMagazines)


@app.route('/newMagazine/')
def newMagazine(): 
    if 'user_id' not in session:
        flash('Must log in')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    theUser = User.getId(data)
    return render_template('newMagazine.html', user=theUser)


@app.route('/addMagazine/', methods=['POST'])
def addMagazine():
    data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'user_id': session['user_id']
        }
    Magazine.save(data)
    flash("Youre magazine has been saved")
    return redirect('/dashboard/')

@app.route('/<int:magazine_id>/delete/')
def deleteMagazine(magazine_id):
    data = {
        'id': magazine_id
    }
    Magazine.delete(data)
    flash('Magazine has been deleted')
    return redirect('/dashboard/')

@app.route('/<int:magazine_id>/display/')
def displayMagazine(magazine_id):
    if 'user_id' not in session:
        flash('Must log in')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    magazineData = {
        'id': magazine_id
        }
    theUser = User.getId(data)
    theUsers = User.getAll()
    theMagazine = Magazine.getId(magazineData)
    return render_template('displayMagazine.html', user=theUser,users=theUsers,magazine=theMagazine)

@app.route('/<int:magazine_id>/edit/')
def editMagazine(magazine_id):
    if 'user_id' not in session:
        flash('Must log in')
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    magazineData = {
        'id': magazine_id
        }
    theUser = User.getId(data)
    theMagazine = Magazine.getId(magazineData)
    return render_template('editMagazine.html', user=theUser,magazine=theMagazine)

@app.route('/<int:magazine_id>/update/', methods=['POST'])
def updateMagazine(magazine_id):
        data = {
        'id': request.form['magazine_id'],
        'title': request.form['title'],
        'description': request.form['description'],
        }
        Magazine.update(data)
        flash('Magazine has been updated')
        return redirect('/dashboard/')