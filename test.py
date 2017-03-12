#from google.appengine.api import urlfetch
import json
import urlfetch as urlfetch

city = raw_input("Wich city ? ")
url = "http://api.openweathermap.org/data/2.5/weather?q="+ city +"&units=metric&appid=d23ef4ef1700cc9f89d46413ccdf2a96"
result = urlfetch.fetch(url)
details = json.loads(result.content)

print details
