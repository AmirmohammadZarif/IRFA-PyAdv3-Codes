from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/test'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(512))
    is_done = db.Column(db.Boolean)


@app.route('/') 
def home():
    todos = Todo.query.all()
    return render_template("base.html", todo_list=todos)

@app.route('/add', methods=["POST"])
def add():
    title = request.form.get("title")
    todo = Todo(title=title, is_done=False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.is_done = not todo.is_done
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=8080, debug=True)