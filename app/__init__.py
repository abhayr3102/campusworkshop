"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7jabhp8u7g2ed8b70-a.oregon-postgres.render.com",
        database="todo_h74m",
        user="root",
        password="xS5CDGDB5r85W5YrrF9NPCLkwhW2heR9")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
