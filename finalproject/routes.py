#---------------------------------------------------------------------------------------------------------------
from flask import render_template, redirect, url_for, session
from finalproject import app, get_db_connection
from finalproject.fvalidation import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
import html


#---------------------------------------------------------------------------------------------------------------
@app.route('/')
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
    
        sanitized_username = html.escape(form.username.data)
        sanitized_email = html.escape(form.email.data.strip().lower())
        hashed_password = generate_password_hash(form.password.data) 
        
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (sanitized_username, sanitized_email, hashed_password))
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for('login'))
    
    return render_template('register.html', title="Register", form=form)


#---------------------------------------------------------------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        sanitized_email = html.escape(form.email.data)
        password = form.password.data
        
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "SELECT id, username, password FROM users WHERE email = %s"
        cursor.execute(query, (sanitized_email,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        
        if user and check_password_hash(user[2], password): 
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect(url_for('homepage'))
        
    return render_template('login.html', title="Login", form=form)


#---------------------------------------------------------------------------------------------------------------
@app.route('/homepage')
def homepage():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('homepage.html', title="Homepage", username=session['username'])


#---------------------------------------------------------------------------------------------------------------
@app.route('/about')
def about():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('about.html', title="About Us")


#---------------------------------------------------------------------------------------------------------------
@app.route('/portfolio')
def portfolio():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('portfolio.html', title="Portfolio")


#---------------------------------------------------------------------------------------------------------------
@app.route('/contact')
def contact():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('contact.html', title="Contact")


#---------------------------------------------------------------------------------------------------------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
