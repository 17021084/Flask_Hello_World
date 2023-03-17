from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)
port = 8080

@app.route('/')
def index():
    return render_template("index.html",port_running=port)


@app.route('/success/<name>')
def success(name):
    # String Interpolation %- fomarting
    return "well come %s" % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print ("12")
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        print ("abc")
        user= request.args.get('nm')
        return redirect(url_for('success', name=user))




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
