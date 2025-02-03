from flask import Flask
import os
import json

app = Flask(__name__)
JSON_FILE = "data/data.json"

# Create data.json file for use of PV.
@app.route("/")
def index_page():

    elements = f"""
    <h1>Hello, World from Pod {os.getenv('POD_NAME', 'N/A')}!</h1>
    """

    if os.path.exists(JSON_FILE):
        file = None
        with open(JSON_FILE, "r") as f:
            file = json.load(f)
            file.append({"pod_name_created": os.getenv('POD_NAME', 'N/A')})
        with open(JSON_FILE, "w") as f:
            json.dump(file, f)
    else:
        with open(JSON_FILE, "w") as f:
            json.dump([{"pod_name_created": os.getenv('POD_NAME', 'N/A')}], f)

    with open(JSON_FILE, "r") as f:
        data = json.load(f)
        elements += "<h2>Objects created from the PV on test.json: </h2>"
        for pod in data:
            elements += f"<p>{pod['pod_name_created']}</p>"

    return elements

if __name__ == "__main__":
    app.run()