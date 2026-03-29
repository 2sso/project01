from flask import Blueprint, request
from sqlalchemy import text
from app.db import get_connection

user_bp = Blueprint("user", __name__)

# CREATE
@user_bp.route("/users", methods=["POST"])
def create_user():
    conn = get_connection()
    try:
        data = request.json

        if not data or "name" not in data:
            return {"error": "name is required"}, 400

        conn.execute(
            text("INSERT INTO users (name) VALUES (:name)"),
            {"name": data["name"]}
        )
        conn.commit()

        return {"status": "created"}

    finally:
        conn.close()

# READ
@user_bp.route("/users", methods=["GET"])
def get_users():
    conn = get_connection()
    try:
        result = conn.execute(text("SELECT * FROM users"))
        users = [{"id": row[0], "name": row[1]} for row in result]

        return {"users": users}

    finally:
        conn.close()

# UPDATE
@user_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    conn = get_connection()
    try:
        data = request.json

        if not data or "name" not in data:
            return {"error": "name is required"}, 400

        result = conn.execute(
            text("UPDATE users SET name=:name WHERE id=:id"),
            {"name": data["name"], "id": user_id}
        )
        conn.commit()

        if result.rowcount == 0:
            return {"error": "user not found"}, 404

        return {"status": "updated"}

    finally:
        conn.close()

# DELETE
@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = get_connection()
    try:
        result = conn.execute(
            text("DELETE FROM users WHERE id=:id"),
            {"id": user_id}
        )
        conn.commit()

        if result.rowcount == 0:
            return {"error": "user not found"}, 404

        return {"status": "deleted"}

    finally:
        conn.close()

