from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from auth import login_required
from db import get_db

bp = Blueprint("class_app", __name__)


# index bp
@bp.route("/")
def index():
    db = get_db()
    # user_id = g.user["id"]
    # lists = db.execute(
    #     "SELECT p.id, title, complete, created, user_id, username"
    #     " FROM todo p JOIN user u ON p.user_id = u.id"
    #     " WHERE p.user_id = ?"
    #     " ORDER BY created ASC",
    #     (user_id,),
    # ).fetchall()
    students = db.execute("SELECT * FROM Students").fetchall()
    quizes = db.execute("SELECT * FROM Quizes ").fetchall()
    return render_template(
        "class/dashboard.html",
        students=students,
        quizes=quizes,
    )


# create pb
@bp.route("/student/add", methods=("GET", "POST"))
@login_required
def create_students():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        # body = request.form["body"]
        error = None

        if not firstname:
            error = "Firstname is required."
        if not lastname:
            error = "Lastname is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO Students (firstname,  lastname)" " VALUES (?,  ?)",
                (firstname, lastname),
            )
            db.commit()
            return redirect(url_for("class_app.index"))

    return render_template("class/create_students.html")


# create pb
@bp.route("/quiz/add", methods=("GET", "POST"))
@login_required
def create_quizes():
    if request.method == "POST":
        title = request.form["title"]
        questions = request.form["questions"]
        date = request.form["date_given"]
        error = None

        if not title:
            error = "title is required."
        if not questions:
            error = "questions is required."
        if not date:
            error = "Date is required"

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO Quizes (title,  questions,date_given)" " VALUES (?, ?, ?)",
                (title, questions, date),
            )
            db.commit()
            return redirect(url_for("class_app.index"))

    return render_template("class/create_quizes.html")


# # getting a single list
# def get_list(id, check_author=True):
#     list = (
#         get_db()
#         .execute(
#             "SELECT p.id, title, created, user_id, username"
#             " FROM todo p JOIN user u ON p.user_id = u.id"
#             " WHERE p.id = ?",
#             (id,),
#         )
#         .fetchone()
#     )

#     if list is None:
#         abort(404, f"List id {id} doesn't exist.")

#     if check_author and list["user_id"] != g.user["id"]:
#         abort(403)

#     return list


# # update bp
# @bp.route("/<int:id>/update", methods=("GET", "POST"))
# @login_required
# def update(id):
#     list = get_list(id)

#     if request.method == "POST":
#         title = request.form["title"]
#         # body = request.form["body"]
#         error = None

#         if not title:
#             error = "Title is required."

#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             db.execute("UPDATE todo SET title = ?" " WHERE id = ?", (title, id))
#             db.commit()
#             return redirect(url_for("todoapp.index"))

#     return render_template("todo/update.html", list=list)


# @bp.route("/<int:id>/delete", methods=("POST",))
# @login_required
# def delete(id):
#     get_list(id)
#     db = get_db()
#     db.execute("DELETE FROM todo WHERE id = ?", (id,))
#     db.commit()
#     return redirect(url_for("todoapp.index"))


# @bp.route("/<int:id>/complete", methods=("POST",))
# @login_required
# def complete(id):
#     # list = get_list(id)
#     db = get_db()
#     db.execute("UPDATE todo SET complete = TRUE WHERE id = ?", (id,))
#     db.commit()
#     return redirect(url_for("todoapp.index"))


# @bp.route("/<int:id>/incomplete", methods=("POST",))
# @login_required
# def incomplete(id):
#     # list = get_list(id)
#     db = get_db()
#     db.execute("UPDATE todo SET complete = FALSE WHERE id = ?", (id,))
#     db.commit()
#     return redirect(url_for("todoapp.index"))
