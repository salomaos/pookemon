from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class UserRegistrationFrom(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=3, max=10)])
    confirm_password = PasswordField('Confirmar Senha', validators=[DataRequired(),
                                                                     EqualTo('password'), Length(min=3, max=10)])
    submit = SubmitField('Cadastrar')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember = BooleanField('Lembrar de mim')
    submit = SubmitField('Login')


class PokemonRegistrationForm(FlaskForm):
    pokemon_index = IntegerField('Índice', validators=[DataRequired(), Length(min=3, max=3)])
    name = StringField('Nome', validators=[DataRequired(), Length(min=1, max=20)])
    height = FloatField('Altura', validators=[DataRequired()])
    weight = FloatField('Peso', validators=[DataRequired()])
    hp = IntegerField('Vida', validators=[DataRequired()])
    attack = IntegerField('Ataque', validators=[DataRequired()])
    defense = IntegerField('Defesa', validators=[DataRequired()])
    special_attack = IntegerField('Ataque Especial', validators=[DataRequired()])
    special_defense = IntegerField('Defesa Especial', validators=[DataRequired()])
    speed = IntegerField('Velocidade', validators=[DataRequired()])
    specie = StringField('Espécie', validators=[DataRequired()])
    type = StringField('Tipo', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')
