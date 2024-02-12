from flask import Blueprint, render_template, request
from utils import get_posts_all, path_posts


users_blueprint = Blueprint('users_blueprint', __name__, template_folder='templates')


@users_blueprint.route('/users/<user_name>')
def f1(user_name):
    user_name = user_name
    posts = get_posts_all(path_posts)
    return render_template('new_user-feed.html', user_name=user_name, posts=posts)