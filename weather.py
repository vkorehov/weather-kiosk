import web
import requests
import os

urls = ("/current", "awcurrent", "/12hour", "awhist12h", "/5day", "awhist5d", "/weather", "darksky", "/icons/.*", "icons", "/.*" , "index")

app = web.application(urls, globals())

class index:
    def GET(self):
        weather = None
        with open('weather.html', 'r') as wf:
            weather = wf.read()
        return weather

class darksky:
    def GET(self):
        response = requests.get("https://api.darksky.net/forecast/"+os.environ['API_KEY']+"/56.994377,24.165299?units=si")
        return response.text
class awcurrent:
    def GET(self):
        response = requests.get("http://dataservice.accuweather.com/currentconditions/v1/1432?details=true&apikey="+os.environ['API_KEY'])
        return response.text
class awhist12h:
    def GET(self):
        response = requests.get("http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/1432?metric=true&details=true&apikey="+os.environ['API_KEY'])
        return response.text
class awhist5d:
    def GET(self):
        response = requests.get("http://dataservice.accuweather.com/forecasts/v1/daily/5day/1432?metric=true&details=true&apikey="+os.environ['API_KEY'])
        return response.text


class icons:
    def GET(self):
        icon = None
        with open(web.ctx.path[1:], 'r') as icf:
            icon = icf.read()
        web.header('Content-Type', 'image/svg+xml')
        return icon

if __name__ == "__main__":
    app.run()
