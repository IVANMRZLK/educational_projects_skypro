from flask import Blueprint, render_template
from utils import get_posts_all, path_posts, get_comments_all, path_comments


post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')


@post_blueprint.route('/posts/<int:postid>')
def f1(postid):
    posts = get_posts_all(path_posts)
    postid = postid
    comments = get_comments_all(path_comments)
    quantity_comments = 0
    for i in comments:
        if i["post_id"] == postid:
            quantity_comments += 1

    return render_template('new_post.html', posts=posts, comments=comments, postid=postid,quantity_comments=quantity_comments)