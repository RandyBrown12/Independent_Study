from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index_page():
    return render_template('index.html')

@app.route("/createItem", methods=["POST"])
def create_item_page():
    db_message = None

    connection = psycopg2.connect(
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB")
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
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB")
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
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB")
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