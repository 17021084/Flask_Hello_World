from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

# run app 
# if __name__ == "__main__":
#     app.run()


# run app debug type
if __name__ == "__main__":
    app.run(debug=True)