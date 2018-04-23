import requests

url = 'https://news.ycombinator.com/'
res = requests.get(url)
print(url)
print("%d "%res.status_code)
print(res.text)
