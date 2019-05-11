import requests

params = {"#q": "pizza"}

r = requests.get("http://www.bing.com/search", params=params  )
print("Status:", r.status_code) # Status: 200

print(r.url) # http://www.google.com/

print(r.url)
f = open("./page.html", "w+")
f.write(r.text)