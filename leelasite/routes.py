import flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')

@bp.route('/about')
def about():
    return render_template('about.html')

#added in class on oct 16
@bp.route('/msg_length',methods= ["GET"])
def msg_length():
    msg = flask.request.args['msg']
    result = {'Length':len(msg)}
    return flask.jsonify(result)

@bp.route('/predict',methods=["GET"])
def predict():
    msg = flask.request.args['msg']
    score = flask.request.args["score"]
    result = {'message' : msg,'score':score}
    return flask.jsonify(result)
@bp.route('/page')
def page():
    return render_template("ppage.html") 
@bp.route('/secret')
def brandon():
    return render_template("secret.html") 

@bp.route('/result', methods=['POST', 'GET'])
def result():
    '''get prediction using the HTML form'''
    if flask.request.method == 'POST' :

        inputs = flask.request.form 

        msg = inputs['msg'][0]
        score = inputs['score'][0]

        results = {'length': len(msg),'score':score}
        return flask.jsonify(results)


