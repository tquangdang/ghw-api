from flask import Flask, request

app = Flask(__name__)

hackathons =  {
    "GHW: API Week": {
    "start_date": "2023-04-03",
    "end_date": "2023-04-10",
    "type": "Digital Only",
    "location": "Everywhere, Online"
  },
"Bitcamp": {
    "start_date": "2023-04-03",
    "end_date": "2023-04-10",
    "type": "Digital Only",
    "location": "College Park, Maryland"
  }
}
@app.route("/")
def hello_ghw():
    return "<p>Hello, me may beo!</p>"

@app.route("/getHackathons", methods=["GET"])
def getHackathons():
    return hackathons

if __name__ == "__main__":
    app.run(debug = True)
