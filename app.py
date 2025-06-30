from flask import Flask, render_template_string, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Add Post')

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template_string('''
    <h1>Mini Blog</h1>
    <a href="{{ url_for('add') }}">Add Post</a>
    <ul>
    {% for post in posts %}
      <li><a href="{{ url_for('post', post_id=post.id) }}">{{ post.title }}</a></li>
    {% else %}
      <li>No posts yet.</li>
    {% endfor %}
    </ul>
    ''', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template_string('''
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
    <a href="{{ url_for('index') }}">Back to list</a>
    ''', post=post)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, content=form.content.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template_string('''
    <h1>Add Post</h1>
    <form method="post">
        {{ form.hidden_tag() }}
        <p>{{ form.title.label }}<br>{{ form.title(size=40) }}</p>
        <p>{{ form.content.label }}<br>{{ form.content(rows=6, cols=40) }}</p>
        <p>{{ form.submit() }}</p>
    </form>
    <a href="{{ url_for('index') }}">Back to list</a>
    ''', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 