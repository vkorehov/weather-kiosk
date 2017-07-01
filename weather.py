import web
import requests

weather = None
with open('weather.html', 'r') as wf:
    weather = wf.read()

urls = ("/weather", "darksky", "/.*", "index")

app = web.application(urls, globals())

class index:
    def GET(self):
        return weather

class darksky:
    def GET(self):
        response = requests.get("https://api.darksky.net/forecast/00696d867ef68c35f90dab94c1aab73d/56.948889,24.106389?units=si")
        return response.text

if __name__ == "__main__":
    app.run()
