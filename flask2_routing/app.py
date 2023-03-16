from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"


@app.route('/hello')
def hello():
    return "<h3> Konichiha</h3>"

@app.route('/goout')
def go_out():
    return "<h3> matane </h3>"


# run app 
# if __name__ == "__main__":
#     app.run()


# run app debug type
if __name__ == "__main__":
    app.run(debug=True)