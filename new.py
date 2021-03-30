import requests as rs

prams = {"q": "pizza"}

r = rs.get("https://google.com/search", params=prams)


print("status", r.status_code)

print(r.text)

f = open("./page.html", "w+")
f.write(r.text)