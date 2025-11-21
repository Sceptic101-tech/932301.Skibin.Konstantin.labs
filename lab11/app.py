from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/model")
def model():
    return render_template('model.html')

@app.route("/viewdata")
def viewdata():
    return render_template('viewdata.html')

@app.route("/viewbag")
def viewbag():
    return render_template('viewbag.html')

@app.route("/serviceinjection")
def serviceinjection():
    return render_template('serviceinjection.html')

if __name__ == "__main__":
    app.run(debug=False, port=5000, host='0.0.0.0')
