import requests
import jsonpickle

def get_quote(type):
    response = jsonpickle.decode(requests.get("https://zenquotes.io/api/quotes/mode=random").text)
    info = response[1]
    auther = info['a']
    quote = info['q']
    if type == "a":
        return auther

    elif type == "q":
        return quote
    # for i in range(len(response)):
    #     info = response[i]
    #     auther = info['a']
    #     quote = info['q']
    #     quotes[auther] = quote

print(get_quote(type="q"))
