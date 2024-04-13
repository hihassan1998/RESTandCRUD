from flask import Flask

app = Flask("My Hello world application ~ Hassan Hussain")

@app.route("/")
def hello():
    return "Hello World! From Hassan through flask server"

if __name__=="__main__":
    app.run(debug=True)
# When no port is specified, starts at default port 5000