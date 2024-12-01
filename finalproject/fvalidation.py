from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, Regexp
from finalproject import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20), Regexp('^[A-Za-z0-9_-]+$', message="* Only letters, numbers, underscores, and hyphens are allowed.")])
    email = EmailField('Email', validators=[DataRequired(), Email(), Regexp('^[a-zA-Z0-9_-]+(\\.[a-zA-Z0-9_-]+)*@[a-zA-Z0-9_-]+\\.[a-zA-Z0-9.-]+$', message="* Invalid email format.")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="* Passwords do not match.")])
    submit = SubmitField('Register')

    def validate_username(self, username):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username.data,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        
        if user:
            raise ValidationError('* That username is already taken.')
        
    def validate_email(self, email):
        connection = get_db_connection() 
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email.data,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        
        if user:
            raise ValidationError('* That email is already taken.')

    # No need for this hash_password method here since hashing happens in the routes
    # def hash_password(self, password):
    #     return generate_password_hash(password)

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    def validate_email(self, field):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", [field.data])
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        if user is None:
            raise ValidationError('* No account found with this email')

    def validate_password(self, field):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", [self.email.data])
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        if user:
            # Use Werkzeug to check the password hash
            if not check_password_hash(user[3], field.data):  # Check the hashed password
                raise ValidationError('* Invalid Password.')
