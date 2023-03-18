from flask import Flask, make_response, redirect, render_template, request, url_for
app = Flask(__name__)
port = 8080


@app.route('/')
def index():
    return render_template("index.html", port_running=port)


@app.route('/setcookie', methods=["POST", "GET"])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']
        res = make_response(render_template('readcookie.html'))
        res.set_cookie ("userID", user)
        return res


@app.route('/getcookies')
def getcookie():
    name = request.cookies.get('userID')
    return "<h1> wellcome " + name +  ' this is cookies site'



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
