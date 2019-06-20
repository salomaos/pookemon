from flask import Flask, render_template, url_for, flash, redirect
from forms import UserRegistrationFrom, LoginForm,PokemonRegistrationForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '28907726c236240572f28a3dd456109f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pookemon.db'
db = SQLAlchemy(app)

has = db.Table('partnership',
               db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
               db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True)
               )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    has = db.relationship('Pokemon', secondary=has, lazy=True, backref=db.backref('users', lazy=True))

    def __repr__(self):
        return f"Usuário('{self.username}', '{self.email}')"


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemon_index = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    height = db.Column(db.Float(20), nullable=False)
    weight = db.Column(db.Float(20), nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    special_attack = db.Column(db.Integer, nullable=False)
    special_defense = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    specie = db.Column(db.String(20), nullable=False)
    type = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@pookemon.com' and form.password.data == 'senha':
            flash('Você está logado!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuário ou senha incorreta, por favor verificar!', 'danger')
    return render_template('index.html', title='Login', css='index.css', form=form)


@app.route('/cadastrar-usuario', methods=['GET', 'POST'])
def user_signup():
    form = UserRegistrationFrom()
    if form.validate_on_submit():
        flash(f'{form.username.data} sua conta foi criada com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('user-signup.html', title='Cadastrar um novo usuário', css='user-signup.css', form=form)


@app.route('/dashboard')
def dashboard():
    form = PokemonRegistrationForm()
    if form.validate_on_submit():
        flash(f'{form.name.data} foi registrado com sucesso!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('dashboard.html', title='Dashboard', css='dashboard.css', form=form)


if __name__ == '__main__':
    app.run()
