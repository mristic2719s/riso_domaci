import http.client
import json

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
print(data.decode("utf-8"))
print("Uspesno dodat user pomocu skripte koja se koristi unutar docker containera!")