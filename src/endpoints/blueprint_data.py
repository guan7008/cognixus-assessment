from flask import Blueprint, jsonify, request
from endpoints import mysqlconnector

# define the blueprint
blueprint_data = Blueprint(name="blueprint_data", import_name=__name__)


@blueprint_data.route("/todo", methods=["POST"])
def add_todo():
    task = request.form.get("task")

    if not task:
        return jsonify(
            {
                "status_code": 21001,
                "message": "ERROR: Invalid Input",
            }
        )

    query = "INSERT INTO todo (task) VALUES (%s)"
    val = (task,)

    cnx = mysqlconnector()

    cursor = cnx.cursor()
    cursor.execute(query, val)

    cnx.commit()

    return jsonify(
        {
            "status_code": 22002,
            "message": "OK: Add a TODO item",
        }
    )


@blueprint_data.route("/todo/<id>", methods=["DELETE"])
def delete_todo(id):

    query = "DELETE FROM todo WHERE id = %s"
    val = (id,)

    cnx = mysqlconnector()

    cursor = cnx.cursor()
    cursor.execute(query, val)

    cnx.commit()

    return jsonify(
        {
            "status_code": 22004,
            "message": "OK: Delete a TODO item",
        }
    )


@blueprint_data.route("/todo")
def list_todo():
    limit = request.form.get("limit", 100, int)
    offset = request.form.get("offset", 0, int)

    cnx = mysqlconnector()

    pagination = ""
    if not limit <= 0:
        start = limit * offset
        pagination = f" LIMIT {start}, {limit}"

    query = f"SELECT * FROM todo {pagination}"

    cursor = cnx.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    cnx.close()

    return jsonify(
        {
            "status_code": 22000,
            "message": "OK: List all TODO items",
            "result": result,
        }
    )


@blueprint_data.route("/todo/<id>/completed", methods=["PUT"])
def mark_completed_todo(id):
    query = "UPDATE todo SET completed = 1 WHERE id = %s"
    val = (id,)

    cnx = mysqlconnector()

    cursor = cnx.cursor()
    cursor.execute(query, val)

    cnx.commit()

    return jsonify(
        {
            "status_code": 22006,
            "message": "OK: Mark completed a TODO item",
        }
    )
