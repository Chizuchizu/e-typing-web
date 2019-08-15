# -*- coding: utf-8 -*-
import matplot

from flask import Flask, make_response, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return "hello"


@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        return graph(request.form["num"])


@app.route("/graph.png")
def graph(number):
    # number = "912"
    data = matplot.byoga(number)
    response = make_response(data)
    response.headers["Content-Type"] = "image/png"
    response.headers["Content-Length"] = len(data)
    return response


if __name__ == '__main__':
    app.run(debug=True)
