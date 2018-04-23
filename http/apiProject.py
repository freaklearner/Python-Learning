import requests
import pyfiglet
from termcolor import colored

header = pyfiglet.figlet_format("Jokes 3000")
header = colored(header,color="magenta")
print(header)
url = "https://icanhazdadjoke.com/search"

#print("Enter a topic of joke:")
#topic = input()
topic = "cat"
#print("Number of jokes?:")
#joke_limit = input()
joke_limit = "4"
res = requests.get(
        url,
        headers = {
            "Accept":"application/json"
        },
        params = {
            "term":topic,
            "limit":joke_limit
        }
    )
data = res.json()
for dt in data['results']:
    print(dt['joke'])
