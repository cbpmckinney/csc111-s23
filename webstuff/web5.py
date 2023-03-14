import flask as Flask
from datetime import datetime

app = Flask.Flask(__name__)



@app.route('/')
def hello():
    return """<html><body>
        <h1>Hello, world!</h1>
        <img src = '/static/wally.gif'>.
        </body></html>"""



if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="localhost", debug=True)