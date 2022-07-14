import requests
import jsonpickle

def get_quote():
    response = jsonpickle.decode(requests.get("https://zenquotes.io/api/quotes/mode=random").text)
    quote = {}
    info = response[1]
    auther = info['a']
    quote = info['q']
    quote[auther] = quote

    return quote
    # for i in range(len(response)):
    #     info = response[i]
    #     auther = info['a']
    #     quote = info['q']
    #     quotes[auther] = quote


