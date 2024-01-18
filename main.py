from flask import * 

app = Flask('tt') # <-- added closing parenthesis here

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()