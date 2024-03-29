from flask import * 

app = Flask(__name__) # <-- added closing parenthesis here

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    from waitress import serve
    app.run(host="0.0.0.0", port=5000, debug=True)
