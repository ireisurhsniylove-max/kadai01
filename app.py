import os
import uuid
from datetime import datetime, timedelta, timezone

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from azure.data.tables import TableServiceClient

app = Flask(__name__, static_folder="css", static_url_path="/css")

# Azure Table Storage
CONNECTION_STRING = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")
TABLE_NAME = "posts"


class LocalTable:
    def __init__(self):
        self.entities = []

    def list_entities(self):
        return list(self.entities)

    def create_entity(self, entity):
        self.entities.append(entity)


if CONNECTION_STRING:
    service = TableServiceClient.from_connection_string(CONNECTION_STRING)
    table = service.create_table_if_not_exists(TABLE_NAME)
else:
    table = LocalTable()

# 日本時間
JST = timezone(timedelta(hours=9))


@app.route("/")
def index():
    messages = list(table.list_entities())
    messages.sort(key=lambda m: m["posted_at"], reverse=True)

    return render_template("index.html", messages=messages)


@app.route("/post", methods=["POST"])
def post():
    name = request.form.get("name", "").strip()
    title = request.form.get("title", "").strip()
    category = request.form.get("category", "").strip()
    text = request.form.get("message", "").strip()

    if text:
        if not name:
            name = "名無し"

        table.create_entity({
            "PartitionKey": "board",
            "RowKey": str(uuid.uuid4()),
            "name": name,
            "title": title,
            "category": category,
            "text": text,
            "posted_at": datetime.now(JST).strftime("%Y/%m/%d %H:%M:%S")
        })

    return redirect(url_for("index"))


@app.route("/js/<path:filename>")
def javascript_files(filename):
    return send_from_directory(os.path.join(app.root_path, "js"), filename)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5001"))
    app.run(host="127.0.0.1", port=port, debug=True)