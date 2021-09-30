from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/mypage')
def me():
    return render_template("page.html")


@app.route('/mypage/me')
def me2():
    return render_template("page1.html")

@app.route('/mypage/contact', methods=['POST']) 
def post_contact():
    return "Wiadomość została wysłana! :)"

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        print("We received GET")
        return render_template("page2.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect("/")
