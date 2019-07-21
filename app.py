from flask import Flask, render_template, current_app, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dog import doggo
from route import route
from msw import swell
from pub import pub_parser
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String(100), nullable=False)
    spot = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Post('{self.location}', '{self.spot}')"

# Route
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        form = InputForm()
        post = Post(location=form.location.data, spot=form.spot.data)
        db.session.add(post)
        db.session.commit()
        flash(f'Your search is being actioned!', 'success')
        dog = doggo()
        location = Post.query.filter_by(location=form.location.data).first().location
        spot = Post.query.filter_by(spot=form.spot.data).first().spot
        distance, duration = route(location, spot)
        waves = swell(spot)
        pub = pub_parser(spot)
        return render_template('index.html', form=form, dog=dog, distance=distance,
                                duration=duration, waves=waves, spot=spot, pub=pub,
                                location=location)
    elif request.method == 'GET':
        form = InputForm()
        return render_template('index.html', form=form)
# Form

class InputForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired()])
    spot = StringField('Spot', validators=[DataRequired()])
    submit = SubmitField('Waves Ahoy')


# Can run using "python flaskblog.py" as opposed to flask command
if __name__ == '__main__':
    app.run(debug=True)
