from flask import Flask, render_template, request, redirect, url_for
import time

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/page1_1", methods=["GET", "POST"])
def page1_1():
    if request.method == "POST":
        time.sleep(2)  # 何らかの処理時間の代わり
        return redirect(url_for("page2"))
    return render_template("page1_1.html")


@app.route("/page1_2", methods=["GET", "POST"])
def page1_2():
    if request.method == "POST":
        time.sleep(2)  # 何らかの処理時間の代わり
        return redirect(url_for("page2"))
    return render_template("page1_2.html")


@app.route("/page2")
def page2():
    return render_template("page2.html")
