import requests


page = requests.get("https://vancouver.craigslist.org/d/computer-parts/search/syp?max_price=50&min_price=4").text.split('"')

urls = []

for i in page:

	if "https://vancouver.craigslist.org/" in i:

		urls.append(i)

for i in urls:

	print(i)



