from flask import Flask, render_template, request, jsonify

import utils
from logger import get_logger
from utils import *

app = Flask(__name__)
logger = get_logger("main")


@app.route("/", methods=['GET'])
def all_posts():
    posts = get_posts_all()
    logger.info("knock knock")
    return render_template('index.html', posts=posts)


@app.route("/post/<int:pk>", methods=['GET'])
def get_post(pk):
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)
    return render_template('post.html', post=post, comments=comments)


@app.route("/search")
def search_page():
    query = request.args.get('s').lower()
    print(query)
    posts = search_for_posts(query)
    len_posts = len(posts)
    return render_template('search.html', posts=posts, query=query, len_posts=len_posts)


@app.route("/user/<user_name>")
def post_by_user(user_name):
    posts = get_posts_by_user(user_name)
    return render_template('user-feed.html', posts=posts, substr=user_name)


@app.route("/api/posts")
def get_posts_api():
    posts = utils.get_posts_all('posts.json')
    return jsonify(posts)


@app.route("/api/posts/<int:pk>")
def get_post_api(pk):
    post_found = utils.get_post_by_pk(pk)
    return jsonify(post_found)


app.run(debug=True)
