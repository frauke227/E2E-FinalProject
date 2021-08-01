from flask import render_template, url_for, flash, redirect, abort, Blueprint, current_app
from flaskblog import db
from flaskblog.posts.forms import PostForm, AddressForm, UpdateForm
from flaskblog.models import Address, Profile
from flask_login import current_user, login_required


posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Profile(name=form.name.data, languages=form.languages.data, specialisation=form.specialisation.data, 
                    address=form.address.data, phone=form.phone.data, email=form.email.data, website=form.website.data, user_id=current_user)
        post.location = [float(form.lng.data), float(form.lat.data)]
        post.save()
        flash('Your profile has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Profile', form=form, legend='New Profile', map_key=current_app.config["API_KEY"])




@posts.route("/post/<post_id>")
def post(post_id):
    post = Profile.objects.get_or_404(id=post_id)
    return render_template('post.html', title=post.name, post=post, map_key=current_app.config["API_KEY"])


@posts.route("/post/<post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Profile.objects.get_or_404(id=post_id)
    if post.user_id != current_user:
        abort(403)
    form = UpdateForm()
    if form.validate_on_submit():
        post.name = form.name.data
        post.languages = form.languages.data
        post.specialisation=form.specialisation.data
        post.address=form.address.data 
        post.phone=form.phone.data
        post.email=form.email.data
        post.website=form.website.data
        post.location = [float(form.lng.data), float(form.lat.data)]
        post.save()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    form.name.data = post.name
    form.languages.data = post.languages
    form.specialisation.data=post.specialisation
    form.address.data=post.address 
    form.phone.data=post.phone
    form.email.data=post.email
    form.website.data=post.website
    return render_template('create_post.html', title='Update Profile', form=form, legend='Update Profile', map_key=current_app.config["API_KEY"])


@posts.route("/post/<post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Profile.objects.get_or_404(id=post_id)
    if post.user_id != current_user:
        abort(403)
    post.delete()
    flash('Your profile has been deleted!', 'success')
    return redirect(url_for('main.home'))






