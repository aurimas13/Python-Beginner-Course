from flask import Flask, render_template, request

app = Flask(__name__)

# 1
# @app.route("/")
# def home():
#     return "<h1>Čia mano naujas puslapis</h1>"

# 2
@app.route("/<name>")
def user(name):
    return f'Labas, {name}'

# 3
@app.route("/")
def home():
    return render_template("index.html")

# 4
@app.route("/skaiciavimai")
def skaiciavimai():
    return render_template("skaiciavimai.html")

# 5
@app.route("/sarasas")
def sarasas():
    vardai = ['Aliona', 'Aleksandras', 'Rokas', 'Vitalij']
    return render_template("sarasas.html", sarasas=vardai)

# 6
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        vardas = request.form['vardas']
        return render_template("greetings.html", vardas=vardas)
    else:
        return render_template("login.html")
    
if __name__ == "__main__":
    app.run(debug=True) 