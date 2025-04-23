from flask import Flask, render_template, request
import psycopg2
import os
import json as json

db_username = None
db_password = None
db_host = None
database = None

with open("/vault/secrets/config.json") as f:
    secrets = json.load(f)
    db_username = secrets.get("POSTGRES_USER")
    db_password = secrets.get("POSTGRES_PASSWORD")
    db_host = secrets.get("POSTGRES_HOST")
    database = secrets.get("POSTGRES_DB")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index_page():
    is_admin = os.getenv("POD_NAME") == "flaskapp-frontend-admin"
    db_info = None
    if is_admin:
        connection = psycopg2.connect(
            user=db_username,
            password=db_password,
            host=db_host,
            database=database
        )

        cursor = connection.cursor()
        query = "SELECT * FROM ITEMS;"
        try:
            cursor.execute(query)
            connection.commit()
            db_info = cursor.fetchall()
        except Exception as e:
            connection.rollback()
    return render_template('index.html', db_info=db_info)

@app.route("/createItem", methods=["POST"])
def create_item_page():
    db_message = None

    connection = psycopg2.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=database
    )

    cursor = connection.cursor()
    query = "INSERT INTO ITEMS (item_name, count) VALUES (%s, %s);"
    values = (request.form.get("item", "No Object Created"), request.form.get("count", 0))

    try:
        cursor.execute(query, values)
        connection.commit()
        if cursor.rowcount > 0:
            db_message = "Item has been successfully inserted!"
        else:
            db_message = "Item has not been inserted!"
    except Exception as e:
        db_message = e
        connection.rollback()

    cursor.close()
    connection.close()
    return render_template('operation_template.html', db_message=db_message)

@app.route("/updateItem", methods=["POST"])
def update_item_page():
    db_message = None

    connection = psycopg2.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=database
    )

    cursor = connection.cursor()
    query = "UPDATE ITEMS SET count = %s WHERE item_name = %s;"
    values = (request.form.get("count", 0), request.form.get("item", "No Object Created"))

    try:
        cursor.execute(query, values)
        connection.commit()
        if cursor.rowcount > 0:
            db_message = "Item has been successfully updated!"
        else:
            db_message = "Item has not been updated!"
    except Exception as e:
        db_message = e
        connection.rollback()

    cursor.close()
    connection.close()
    return render_template('operation_template.html', db_message=db_message)

@app.route("/deleteItem", methods=["POST"])
def delete_item_page():
    db_message = None

    connection = psycopg2.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=database
    )

    cursor = connection.cursor()
    query = "DELETE FROM ITEMS WHERE item_name = %s;"
    values = (request.form.get("item", "No Object Created"),)

    try:
        cursor.execute(query, values)
        connection.commit()
        if cursor.rowcount > 0:
            db_message = "Item has been successfully deleted!"
        else:
            db_message = "Item has not been deleted!"
    except Exception as e:
        db_message = e
        connection.rollback()

    cursor.close()
    connection.close()
    return render_template('operation_template.html', db_message=db_message)

if __name__ == "__main__":
    app.run()