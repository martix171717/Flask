from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def powerpuffs():
    return render_template("atomowki.html")


@app.route('/bajka')
def bubbles():
    return render_template("bajka.html")

@app.route('/bojka')
def blossom():
    return render_template("bojka.html")

@app.route('/brawurka')
def buttercup():
    return render_template("brawurka.html")

if __name__ == '__main__':
   app.run(debug = True)
