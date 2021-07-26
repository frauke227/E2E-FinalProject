from flask import render_template, request, Blueprint, current_app
from flaskblog.models import Profile


main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    #posts = Post.objects.order_by(        Post.date_posted.desc()).paginate(page=page, per_page=5)
    posts = Profile.objects.all()
    return render_template('home.html', posts=posts)


@main.route("/map")
def about():
    return render_template('about.html', map_key=current_app.config["API_KEY"])