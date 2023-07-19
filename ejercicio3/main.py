from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)


def connection_database(host, user, password, database, port):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=int(port),
    )

    return jsonify(connection)


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return jsonify(result)


def execute_query_with_commit(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


def connection_close(connection):
    connection.close()


@app.route('/create/user', methods=['POST'], endpoint='create_user')
def create_user(user_id, user_name):
    connection = connection_database()
    query = "INSERT INTO users (id, nombre) VALUES (%s, '%s');" % (user_id, user_name)
    execute_query_with_commit(connection, query)
    connection.close()
    try:
        execute_query_with_commit(connection, query)
        return jsonify('OK'), 200
    except Exception as e:
        return jsonify('ERROR'), 500


@app.route('/user/1', methods=['GET'], endpoint='get_user')
def get_user(user_id):
    connection = connection_database()
    query = "SELECT * FROM estudiantes WHERE id = 1;"
    result = execute_query(connection, query)

    if len(result) == 0:
        return jsonify('No se ha encontrado al estudiante'), 404
    else:
        return jsonify('Todo ha ido ok'), 202
