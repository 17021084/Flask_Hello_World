from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",)

@app.route('/greeting/<name>')
def greeting(name):
    return render_template("greeting.html", your_name=name)
        



# run app 
# if __name__ == "__main__":
#     app.run()


# run app debug type
# if __name__ == "__main__":
#     app.run(debug=True)

# run app debug type
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)