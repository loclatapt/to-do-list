from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from datetime import datetime
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to-do-list.db'
app.config['SECRET_KEY'] = 'random'

Bootstrap(app)

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), unique=True, nullable=False)
    time = db.Column(db.String(250), nullable=False)
    done = db.Column(db.Boolean, nullable=False)


class TaskForm(FlaskForm):
    task = StringField('New Task',validators=[DataRequired()])
    submit = SubmitField("Thêm")

with app.app_context():
    db.create_all()

@app.route('/',methods=["GET","POST"])
def home():
    form = TaskForm()
    list_task = Task.query.all()
    if form.validate_on_submit():
        task = Task(
            task = form.task.data,
            time = datetime.now().strftime("%d/%m/%Y %H:%M"),
            done = False
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("index.html",form=form,list_task=list_task)

@app.route('/done/<int:list_id>',methods=['GET','POST'])
def done(list_id):
    checking = Task.query.filter_by(id=list_id).first()
    checking.done=1
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/remove/<int:list_id>',methods=["GET","POST"])
def remove(list_id):
    checking = Task.query.filter_by(id=list_id).first()
    db.session.delete(checking)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)