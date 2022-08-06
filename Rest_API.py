import requests

url = "https://www.hindujagruti.org/hinduism-history/vande-mataram"

r= requests.get(url)

r.status_code : 200

print (r.headers['content-type'])

print(r.headers['date'])
