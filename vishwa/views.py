from flask import Flask, render_template, session, request, redirect, url_for
import json
import filters
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html')


@app.route('/receivedata', methods=["POST"])
def receivedata():
    list_of_points = request.form.get('listed', '')
    latitude = request.form.get('lat', '')
    longitude = request.form.get('long', '')
    type_of_location = request.form.get('type', '')
    duration = request.form.get('duration', '')
    duration_dict = json.loads(duration)
    list_of_points_parsed = json.loads(list_of_points)
    print(list_of_points_parsed[0])
    print(list_of_points_parsed[1])
    #print(list_of_points)
    return list_of_points

if __name__ == '__main__':
    app.run(debug=True)
