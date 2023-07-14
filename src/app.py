from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    print(1/0)
    return "---Hello, world!"


if __name__ == "__main__":
    app.run()

