from flask import Flask, render_template, session, request, redirect, url_for
import json
import filters
import requests
from random import randint
import codecs
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

@app.route('/getData', methods=["POST"])
def getData():
    food = False
    explore = False
    data = request.json
    lat = data['lat']
    lang = data['long']
    types = data['pointType']
    print(types)
    if 'food' in types:
        food = True
    if 'explore' in types:
        explore = True
    print(food, explore)
    location = "{},{}".format(lat, lang)
    return get_corpus(location, food, explore)

def get_place_info(place_id):
   api_key = 'AIzaSyAgCJBw8Jlutcm9rm6fUJFt8HmcE3ZRjS8'
   url = 'http://52.36.211.72:5555/gateway/Google%20Places%20API/1.0/place/details/json?key={}&placeid={}'.format(api_key, place_id)
   x = requests.get(url, headers={'x-Gateway-APIKey': '7c71114f-35cf-4709-aae9-651dbf216fe8'})
   response = x.content.decode('utf-8')
   response_decoded = json.loads(response)
   return response_decoded['result']['name']


def get_corpus(location, food, explore):
    explore_types = ['amusement_park', 'aquarium', 'art_gallery', 'church', 'hindu_temple', 'zoo',
             'stadium', 'shopping_mall', 'night_club', 'library']
    food_types = ['cafe', 'restaurant']
    types = []
    if food:
        types += food_types
    if explore:
        types += explore_types
    formatted_types = '|'.join(types)
    print(formatted_types)
    #location = "13.0620724,80.2612372"
    api_key = 'AIzaSyAgCJBw8Jlutcm9rm6fUJFt8HmcE3ZRjS8'
    url = 'http://52.36.211.72:5555/gateway/Google%20Places%20API/1.0/place/nearbysearch/json?key={}&' \
          'radius={}&location={}&types={}'.format(api_key, 1000, location, formatted_types)
    print(url)
    x = requests.get(url, headers={'x-Gateway-APIKey': '7c71114f-35cf-4709-aae9-651dbf216fe8'})
    response = x.content
    print(response)
    response_json = json.loads(response.decode('utf-8'))
    results = response_json['results']
    corpus = []
    for result in results:
        lat, long = result['geometry']['location'].items()
        place_id = result['place_id']
        #rating = result['rating']
        corpus.append(dict(lat=lat[1],long=long[1], place_id=place_id))
    l = len(corpus)
    number_of_destinations = 4
    i = 1
    randcorpus = []
    while(i <= number_of_destinations):
        num = randint(0,l-1)
        randcorpus.append(corpus[num])
        i=i+1
    for x in randcorpus:
        x['name'] = get_place_info(x['place_id'])
        del x['place_id']
        x['type'] = 'food'
    return json.dumps(randcorpus)


@app.route('/data', methods=["GET"])
def data():
    payload = [
        {'lat': 13.071698,
         'long': 80.256506,
         'type': 'Museum'
         },
        {'lat': 13.006647,
         'long': 80.242090,
         'type': 'Educational_Instituition'
         },
        {'lat': 13.052418,
         'long': 80.282738,
         'type': 'Beach'
         }
    ]
    return "Hello"
if __name__ == '__main__':
    print(get_place_info("ChIJbzbvPwxmUjoRmZOKxmfPy-s"))
    app.run(debug=True, host='0.0.0.0', port=8080)

