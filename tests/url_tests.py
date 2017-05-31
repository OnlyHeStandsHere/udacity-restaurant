# simple URL test to see if we can hit the url with a get request
# only checks that the urls are all well formed and providing responses.

import requests

valid_urls = [
            "/",
            "/restaurants",
            "/restaurant/new",
            "/restaurant/1/edit",
            "/restaurant/1/delete",
            "/restaurant/1/menu",
            "/restaurant/1/menu/1/edit",
            "/restaurant/1/menu/new",
            "/restaurant/1/menu/1/delete"]

url_base = "http://localhost:5000{}"
i = 1

# make a GET request to each valid URL
for url in valid_urls:
    r = requests.get(url_base.format(url))
    if r.ok:
        print("{}. url {} response 200 OK".format(str(i), url_base.format(url)))
    else:
        print("{}. url {} response 404 NOT FOUND".format(str(i), url_base.format(url)))
    i += 1
