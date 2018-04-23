import requests

#url = "https://icanhazdadjoke.com/"
url = "https://icanhazdadjoke.com/search?term="
print("Enter topic of joke: ", end = ' ')
topic = input()
res = requests.get(
        url,
        headers = {
            #"Accept":"text/plain"
            "Accept":"application/json"
        },
        params={
            "term" : topic,
            "limit" : 1
        }
    )

#print(res.text) # this will return str type - "{}"

# so we use function response.json() which will return a dictionary which we can use easily as given below

data = res.json()
print(type(data))
print(data['results'][0]['joke'])

'''
lst = data['results']
print(type(lst))
for i in range(0,data['total_jokes']):
    #print("%d: %s"%(i+1,lst[i]['joke']))
    print("%d: %s"%(i+1,data['results'][i]['joke']))
#print(data)
'''
