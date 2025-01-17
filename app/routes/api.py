from flask import Blueprint, current_app, request, redirect, url_for, jsonify
from flask_jwt_extended import get_jwt_identity
from app.utils.auth_decorator import jwt_or_redirect

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/habit/<habit_id>", methods=["DELETE"])
@jwt_or_redirect()
def delete_habit(habit_id):
    user_id = get_jwt_identity()
    current_app.habit_service.delete(habit_id, user_id)

    return jsonify({"message": "success"})


@api_bp.route("/habit", methods=["POST"])
@jwt_or_redirect()
def post_habit():
    content = request.form.get("content")
    user_id = get_jwt_identity()

    current_app.habit_service.add(content, user_id)

    return redirect(url_for("router.enroll_page"))


@api_bp.route("/habit/toggle", methods=["POST"])
@jwt_or_redirect()
def toggle():
    habit_id = request.json.get("_id")
    date = request.json.get("currentDay")
    user_id = get_jwt_identity()

    current_app.habit_log_service.set_check(user_id, date, habit_id)

    return jsonify({"message": "success"})
