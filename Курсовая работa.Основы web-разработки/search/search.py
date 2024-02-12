from flask import Blueprint, render_template, request
from utils import search_for_posts


search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


@search_blueprint.route('/search')
def f1():
    s = request.args.get('s')
    search_posts = search_for_posts(s)
    count_posts = len(search_posts)
    return render_template('new_search.html', search_posts=search_posts, count_posts=count_posts)