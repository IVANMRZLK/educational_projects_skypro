from flask import Blueprint, render_template
from utils import get_posts_all, get_post_by_pk, path_posts

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts')
def f1():
    posts = get_posts_all(path_posts)
    return posts


@api_blueprint.route('/api/posts/<int:post_id>')
def f2(post_id):
    post = get_post_by_pk(post_id)
    return post