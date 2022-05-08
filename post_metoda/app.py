from flask import Flask, request
import http.client
import json
from werkzeug.exceptions import BadRequestKeyError

SERVICE_DEBUG = True
app = Flask(__name__)

conn = http.client.HTTPConnection("localhost", 8081)
payload = json.dumps({
  "ime": "Marijana",
  "prezime": "Ristic",
  "username": "mrsx",
  "smer": "IT",
  "predmeti": [
    {
      "ime": "RVAS",
      "espb": 2
    },
    {
      "ime": "RISO",
      "espb": 3
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/users", payload, headers)
res = conn.getresponse()
data = res.read()
print('Uspešno ste se povezali sa ostalim docker containerom!')
print('Uspešno ste dodali korisnika pomoću POST metode')
print(data.decode("utf-8"))

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 9095, debug = False)