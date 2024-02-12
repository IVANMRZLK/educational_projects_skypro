from flask import Blueprint, render_template
from utils import get_posts_all, path_posts

all_posts_blueprint = Blueprint('all_posts_blueprint', __name__, template_folder='templates')


@all_posts_blueprint.route('/')
def f1():
    posts = get_posts_all(path_posts)
    return render_template('new_index.html', posts=posts)
