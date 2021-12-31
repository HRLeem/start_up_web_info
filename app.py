import flask
from flask import Flask, render_template, jsonify, request, redirect, url_for
import main

app = Flask(__name__)

app.debug = True

@app.route('/', methods=["GET"])
def home():
    go = main.Main_process
    go()
    return

@app.route('/crawl', methods=["GET"])
def crawl():
    go = main.Main_process
    result_list = go()
    result_list = str(result_list).split(',')
    return render_template('result.html', list = result_list)


# go = main.Main_process
# go()