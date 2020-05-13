from urllib.request import urlopen as uReq	#grabs it
from bs4 import BeautifulSoup as soup	#parse html text
from pages import categories

url = categories["HomePage"]  #url

#read site and store object
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

#parse data
page_soup = soup(page_html, "html.parser")

products = page_soup.findAll("li", {"class":"col-lg-3"})

#open file
fileName = "sample.csv"
f = open(fileName, "w")

headers = "Book Title, Rating out of Four Stars, Price\n\n"
f.write(headers)


for product in products:
    title = product.h3.a["title"]   #book title
    rating = product.p["class"][1]  #book rating
    price = product.find("div", {"class":"product_price"}).p.text   #book price

    results = title + "      " + rating + " stars      " + price + "\n"

    print(results)

    f.write(results)

f.close()

