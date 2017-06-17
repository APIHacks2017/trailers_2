from flask import Flask, render_template, session, request, redirect, url_for
import json
import filters
app = Flask(__name__)


@app.route('/kandhan', methods=["GET"])
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
    start_time = float(duration_dict['sttime'])
    end_time = float(duration_dict['entime'])
    list_of_points_parsed = json.loads(list_of_points)
    type_of_location1 = json.loads(type_of_location)
    result = filters.filter1(list_of_points_parsed,type_of_location1)
    print(result)



    ''' 
    print(list_of_points_parsed)
    print(float(latitude))
    print(float(longitude))
    print(type_of_location)
    print('Start time is: ', start_time, '\nEnd time is:', end_time)
    '''
    return list_of_points

@app.route('/permuted', methods=["POST"])
def permuted():
    list_of_points = request.form.get('listed', '')
    no_of_points = request.form.get('noofdest', '')
    list_of_points_parsed = json.loads(list_of_points)
    permuted_points = filters.permutations(list_of_points_parsed,no_of_points)

    return 'success'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
