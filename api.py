import requests
import jsonpickle
import time

def get_quote(type):
    response = jsonpickle.decode(requests.get("https://zenquotes.io/api/quotes/mode=random").text)
    info = response[1]
    auther = info['a']
    quote = info['q']
    count = 0

    # while (count < 5):
    #     time.sleep(7)
    #     response = jsonpickle.decode(requests.get("https://zenquotes.io/api/quotes/mode=random").text)
    #     with open("Quotes.txt", "w") as file:
    #
    #         for i in range(len(response)):
    #             info = response[i]
    #             auther = info['a']
    #             quote = info['q'].strip()
    #
    #             text = f"\n{quote} * {auther}"
    #             file.write(text)
    #
    #     count += 1
    #     print(count)

    if type == "a":
        return auther

    elif type == "q":
        return quote

def get_qoutes_from_file(filename):
    with open(filename, "r") as file:
        authers = []
        quotes_list = []
        for line in file.readlines():
            line_content = line.split(" * ")
            for item in range(len(line_content)):
                if item < 1:
                    quotes_list.append(line_content[item])
                else:
                    authers.append(line_content[item].strip("\n"))

        quotes = quotes_list[1:]

        dict_authors_quotes = dict(zip(authers, quotes))
        return dict_authors_quotes

# print(get_qoutes_from_file("Quotes.txt"))
# get_quote()