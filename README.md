# Weather APIs
https://web.stanford.edu/group/csp/cs22/using-an-api.pdf


https://www.weather.gov/documentation/services-web-api
https://api.weather.gov/points/39.1825,-77.1904
https://api.weather.gov/points/39.15,-77.22
This will return the grid endpoint in the "forecast" property. Applications may cache the grid for a location to improve latency and reduce the additional lookup request. This endpoint also tells the application where to find information for issuing office, observation stations, and zones.

"properties": {
        "@id": "https://api.weather.gov/points/39.15,-77.22",
        "@type": "wx:Point",
        "cwa": "LWX",
        "forecastOffice": "https://api.weather.gov/offices/LWX",
        "gridId": "LWX",
        "gridX": 89,
        "gridY": 82,
        "forecast": "https://api.weather.gov/gridpoints/LWX/89,82/forecast",

// my location
https://api.weather.gov/gridpoints/LWX/89,82/forecast
ERROR :(

// another location
https://api.weather.gov/gridpoints/TOP/31,80/forecast
periods: [
{
number: 1,
name: "This Afternoon",
startTime: "2023-01-04T14:00:00-06:00",
endTime: "2023-01-04T18:00:00-06:00",
isDaytime: true,
temperature: 38,
temperatureUnit: "F",
temperatureTrend: null,
windSpeed: "10 to 15 mph",
windDirection: "NW",
icon: "https://api.weather.gov/icons/land/day/sct?size=medium",
shortForecast: "Mostly Sunny",
detailedForecast: "Mostly sunny, with a high near 38. Northwest wind 10 to 15 mph, with gusts as high as 20 mph."
},

# My weather
https://www.wunderground.com/weather/us/md/montgomery-village/39.15,-77.22

# Geo location
https://nominatim.org/release-docs/develop/api/Search/
https://nominatim.openstreetmap.org/?country=US&zipcode=20886&format=json&limit=1

https://geocode.maps.co/
https://geocode.maps.co/search?q=20886+US+Maryland


# possible python lib
https://pypi.org/project/geocoder/





# Python Notes
RESTful 
https://realpython.com/api-integration-in-python/

json
https://docs.python.org/3.8/library/json.html

flask
https://flask.palletsprojects.com/en/2.2.x/quickstart/


# Python Setup
mkdir foobar
cd foobar/
python3 -m venv venv
source venv/bin/activate
Optional: install packages (can do from within pycharm)
# if using ?3.8? install wheel/markupsafe ?
 pip install wheel
 pip install MarkupSafe
 pip install flask
 pip install requests

pip freeze | grep -v "pkg-resources" > requirements.txt
pip install -r requirements.txt

# Python Run
flask --app hello run    (hello.py)
if the file is named app.py or wsgi.py, you don’t have to use --app.
flask run
navigate to http://127.0.0.1:5000/
flask run -h <local ip>

or set env vars
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ export FLASK_RUN_PORT=8000
$ export FLASK_RUN_HOST=0.0.0.0


# router
Port Forwarding
new rule for linux machine
protocol tcp
Custom Ports
- source ANY (the outside source port)
- Destination port (make up one or use flask port 5000) use this on the URL http://<outside URL>:5000/
- Forward to port flask running on (5000)
make sure to run flask app with your local ip not 127.0.0.1