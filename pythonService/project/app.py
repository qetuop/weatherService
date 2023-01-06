from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    zipcode = text.upper()
    print(f'zipcode={zipcode}')

    # get lat/lon for zipcode
    api_url = 'https://geocode.maps.co/search?q=US+Maryland+%s' % zipcode
    response = requests.post(api_url)
    response_json = response.json()[0]

    print(f'response{response}')
    print(f'response_json{response_json}')

    lat = response_json['lat']
    lon = response_json['lon']
    print(f'lat/lon={lat,lon}')

    # get weather station info for lat/lon
    api_url = 'https://api.weather.gov/points/%s,%s' % (lat,lon)
    response = requests.get(api_url)
    response_json = response.json()

    # get the forecast url (weather station and ???)
    api_url = response_json['properties']['forecast']
    print(f'forcast_url={api_url}')
    response = requests.get(api_url)
    response_json = response.json()

    temp = response_json['properties']['periods'][0]['temperature']
    
    print(f'temp={temp}')
    return "<p>The temperature for %s is %d</p>" % (zipcode,temp)

@app.route("/todos")
def postTest():
    api_url = "https://jsonplaceholder.typicode.com/todos"    
    todo = {"userId": 1, "title": "Buy milk", "completed": False}
    
    response = requests.post(api_url, json=todo)
    # or
    # headers =  {"Content-Type":"application/json"}
    # response = requests.post(api_url, data=json.dumps(todo), headers=headers)

    print(f'STATUS={response.status_code}')
    
    response_json = response.json()   # dict
    # {'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}

    print(response_json)
    val = response_json['id']

    print(f'val={val}')
    return "<p>POST %d</p>"%val


@app.route("/todos/1")
def getTest():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    
    response = requests.get(api_url)  # requests.models.Response

    print(f'STATUS={response.status_code}')

    print(type(response)) # <class 'requests.models.Response'>
    response_json = response.json()   # dict
    print(type(response_json))
    print(response_json)

    val = response_json['id']

    print(f'val={val}')

    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'sensor': 'false', 'address': 'Mountain View, CA'}
    r = requests.get(url, params=params)
    print(f'STATUS={r.status_code}')

    results = r.json()
    print(f'r={r}')
    #location = results[0]['geometry']['location']
    #print(location['lat'], location['lng'])


    return "<p>GET %d</p>"%val


@app.route("/weather")
def getWeather():
    api_url = "https://api.weather.gov/gridpoints/TOP/31,80/forecast"
    
    response = requests.get(api_url)  # requests.models.Response

    print(f'STATUS={response.status_code}')

    print(type(response))
    response_json = response.json()   # dict
    #print(type(response_json))
    #print(response_json)

    temp = response_json['properties']['periods'][0]['temperature']
    
    print(f'val={val}')
    return "<p>The temperature for %s is %d</p>" % (city,temp)