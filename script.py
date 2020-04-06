import requests

r = requests.get("https://christopherjin.com/")
print(r.status_code)
print(r.ok)
