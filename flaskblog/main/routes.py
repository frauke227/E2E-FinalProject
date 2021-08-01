from flask import render_template, request, Blueprint, current_app, flash, url_for, redirect
from flaskblog.models import Profile
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.posts.forms import PostForm, AddressForm
from flaskblog.models import Address, Profile

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    #posts = Post.objects.order_by(        Post.date_posted.desc()).paginate(page=page, per_page=5)
    posts = Profile.objects().order_by('name')
    return render_template('home.html', posts=posts)


@main.route("/map")
def map():
    posts = Profile.objects.all()
    return render_template('map.html', posts=posts, map_key=current_app.config["API_KEY"])

@main.route("/address", methods=['GET', 'POST'])
@login_required
def new_address():
    form=AddressForm()
    if form.validate_on_submit():
        address=Address(name=form.name.data, user_id=current_user)
        address.address=form.address.data, 
        address.location=[float(form.lng.data), float(form.lat.data)]
        address.save()
        flash('Your address have been saved', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_address.html', form=form, title='NewAddress', map_key=current_app.config["API_KEY"])