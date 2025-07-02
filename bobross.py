from functions import make_ordinal, get_elements # type: ignore

from flask import Flask, render_template, redirect, url_for # type: ignore
from flask_bootstrap import Bootstrap5 # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from sqlalchemy.sql import text # type: ignore
from sqlalchemy import desc # type: ignore

from flask_wtf import FlaskForm, CSRFProtect # type: ignore
from wtforms import SelectField, SubmitField, RadioField # type: ignore



db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?n$NqI'

bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)


username = 'doylear0_ADM'
password = 'Wj6klfp'
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
server  = 'warren.sewanee.edu'
dbname   = '/doylear0'


app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

class Epis(db.Model):
    __tablename__ = 'episodes'
    ep_order = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.Integer)
    episode = db.Column(db.Integer)
    title = db.Column(db.String)
    release_date = db.Column(db.String)
    link = db.Column(db.String)

class Elements(db.Model):
    __tablename__ = 'elements'
    ep_order = db.Column(db.Integer, primary_key=True)
    aurora_borealis = db.Column(db.Integer)
    barn = db.Column(db.Integer)
    beach = db.Column(db.Integer)
    boat = db.Column(db.Integer)
    bridge = db.Column(db.Integer)
    building = db.Column(db.Integer)
    bushes = db.Column(db.Integer)
    cabin = db.Column(db.Integer)
    cactus = db.Column(db.Integer)
    cliff = db.Column(db.Integer)
    clouds = db.Column(db.Integer)
    dock = db.Column(db.Integer)
    farm = db.Column(db.Integer)
    fence = db.Column(db.Integer)
    fire = db.Column(db.Integer)
    flowers = db.Column(db.Integer)
    fog = db.Column(db.Integer)
    grass = db.Column(db.Integer)
    hills = db.Column(db.Integer)
    lake = db.Column(db.Integer)
    lakes = db.Column(db.Integer)
    lighthouse = db.Column(db.Integer)
    mill = db.Column(db.Integer)
    moon = db.Column(db.Integer)
    mountain = db.Column(db.Integer)
    mountains = db.Column(db.Integer)
    ocean = db.Column(db.Integer)
    palm_trees = db.Column(db.Integer)
    pathway = db.Column(db.Integer)
    person = db.Column(db.Integer)
    river = db.Column(db.Integer)
    rocks = db.Column(db.Integer)
    snow = db.Column(db.Integer)
    snowy_mountain = db.Column(db.Integer)
    structure = db.Column(db.Integer)
    sun = db.Column(db.Integer)
    tree = db.Column(db.Integer)
    trees = db.Column(db.Integer)
    waterfall = db.Column(db.Integer)
    waves = db.Column(db.Integer)
    windmill = db.Column(db.Integer)

class Frame(db.Model):
    __tablename__ = 'frames'
    ep_order = db.Column(db.Integer, primary_key=True)
    apple_frame = db.Column(db.Integer)
    circle_frame = db.Column(db.Integer)
    double_oval_frame = db.Column(db.Integer)
    florida_frame = db.Column(db.Integer)
    framed = db.Column(db.Integer)
    half_circle_frame = db.Column(db.Integer)
    half_oval_frame = db.Column(db.Integer)
    oval_frame = db.Column(db.Integer)
    rectangle_3d_frame = db.Column(db.Integer)
    rectangular_frame = db.Column(db.Integer)
    seashell_frame = db.Column(db.Integer)
    split_frame = db.Column(db.Integer)
    tomb_frame = db.Column(db.Integer)
    triple_frame = db.Column(db.Integer)
    window_frame = db.Column(db.Integer)
    wood_framed = db.Column(db.Integer)

class Guest(db.Model):
    __tablename__ = 'guests'
    ep_order = db.Column(db.Integer, primary_key=True)
    guest = db.Column(db.Integer)
    diane_andre = db.Column(db.Integer)
    steve_ross = db.Column(db.Integer)

class Kind(db.Model):
    __tablename__ = 'kind'
    ep_order = db.Column(db.Integer, primary_key=True)
    portrait = db.Column(db.Integer)



class Season(FlaskForm):
    ss = []
    ss.append((0, "Any Season"))
    for i in range(1,31):
        ss.append((i, f'Season {i}'))
    season = SelectField('Choose a Season:', choices=ss)
    submit = SubmitField('Submit')

class Framed(FlaskForm):
    fr = RadioField('Would you like a special frame?', choices=[(0, 'No'), (1, 'Yes')])
    submit = SubmitField('Choose Frame')



@app.route('/', methods=['GET', 'POST'])
def index():
    s = Season()
    if s.validate_on_submit():
        seas = s.season.data
        if (seas != '0'):
            return redirect( url_for('season', seas=seas))
        else:
            return redirect( url_for('all') )
    f = Framed()
    return render_template('index.html', s=s, f=f)

@app.route('/all')
def all():
    eps = db.session.execute(db.select(Epis)).scalars()
    return render_template('all.html', eps=eps)

@app.route('/<seas>')
def season(seas):
    try:
        eps = db.session.execute(db.select(Epis).filter(Epis.season==seas)).scalars()
        return render_template('season.html', eps=eps, seas=seas)

    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.route('/episode/<num>')
def detail(num):
    try:
        eee = db.session.execute(db.select(Epis.episode).filter(Epis.ep_order==num)).scalars()
        ooo = db.session.execute(db.select(Epis.ep_order).filter(Epis.ep_order==num)).scalars()
        e = make_ordinal(eee)
        o = make_ordinal(ooo)

        port = db.session.execute(db.select(Kind.portrait).filter(Kind.ep_order==num)).scalars()

        episod = db.session.execute(db.select(Epis).filter(Epis.ep_order==num)).scalars()
        all_elements = db.session.execute(db.select(Elements).filter(Elements.ep_order==num)).scalars()
        legal_elements = (get_elements(all_elements))

        return render_template('episode.html', episod=episod, num=num, e=e, o=o, alel=legal_elements, port=port)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)