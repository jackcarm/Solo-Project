from flask import Flask, render_template, request, redirect
from models.tag import Tag
import repositories.tag_repository as tag_repository

from flask import Blueprint

tag_blueprint = Blueprint("tag", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/tags'
@tag_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", all_tags=tags)


# NEW
# GET '/tags/new'
@tag_blueprint.route("/tag/new")
def new_tag():
    return render_template("tags/new.html")


# CREATE
# POST '/tags'
@tag_blueprint.route("/tags", methods=["POST"])
def create_tag():
    item = request.form["item"]
    tag = Tag(item)
    tag_repository.save(tag)
    return redirect("/tags")


# SHOW
# GET '/tags/<id>'
@tag_blueprint.route("/tag/<id>")
def show_tag(id):
    tag = tag_repository.select(id)
    return render_template("tags/show.html", tag=tag)


# EDIT
# GET '/tags/<id>/edit'
@tag_blueprint.route("/tag/<id>/edit", methods=["GET"])
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template("tags/edit.html", tag=tag)


# UPDATE
# PUT '/transactions/<id>'
@tag_blueprint.route("/tags/<id>", methods=["POST"])
def update_tag(id):
    item = request.form["item"]
    tag = tag_repository.select_all(item)
    tag = Tag(item)
    tag_repository.update(tag)
    return redirect("/tags")


# DELETE
# DELETE '/transactions/<id>'
@tag_blueprint.route("/tags/<id>/delete", methods=["POST"])
def delete_tag(id):
    tag_repository.delete(id)
    return redirect("/tags")
