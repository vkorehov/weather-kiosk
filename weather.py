import web
import requests

urls = ("/weather", "darksky", "/icons/.*", "icons", "/.*" , "index")

app = web.application(urls, globals())

class index:
    def GET(self):
        weather = None
        with open('weather.html', 'r') as wf:
            weather = wf.read()
        return weather

class darksky:
    def GET(self):
        response = requests.get("https://api.darksky.net/forecast/00696d867ef68c35f90dab94c1aab73d/56.948889,24.106389?units=si")
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
