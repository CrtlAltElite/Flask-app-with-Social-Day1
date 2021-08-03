from flask import render_template
from flask_login import login_required, current_user
from .import bp as social
from app.blueprints.auth.models import User

@social.route('/', methods=['GET'])
@login_required
def index():
    return render_template('index.html.j2')

@social.route('/post/my_posts', methods=['GET'])
@login_required
def my_posts():
    return render_template('my_posts.html.j2', posts=current_user.posts)

@social.route('/show_users', methods=['GET'])
@login_required
def show_users():
    users=User.query.all()
    return render_template('show_users.html.j2', users=users)
