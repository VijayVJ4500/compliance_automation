from flask import render_template
from app import create_app

app = create_app()

@app.route('/about')
def about():
    return "About Page"
