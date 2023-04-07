from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_ghw():
    return "Hello, API Hackers!"

if __name__ == "__main__":
    app.run(debug = True)
