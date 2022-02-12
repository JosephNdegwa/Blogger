from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from sqlalchemy import desc
from app.main import bp
from app import db
import requests
from app.models import User, Post, Comment
from app.main import forms

@bp.route('/')
def index():
    # get the quote of the day
    url = "http://quotes.stormconsultancy.co.uk/random.json"
    response = requests.get(url).json()

    # get all the posts for displaying
    posts = Post.query.order_by(desc(Post.timestamp)).all()
    return render_template('index.html', posts=posts, User=User, quote=response)

@bp.route('/post/<post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get(post_id)
    return render_template('post.html', post=post)