from flask import Flask, render_template


app = Flask('__name__')


@app.route("/")
def index():
    greeting = "Congratulations, Radu, you'll be sorely missed"
    return greeting

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
