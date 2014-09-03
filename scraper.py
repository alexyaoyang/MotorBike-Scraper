from lxml import html
import requests, json, webbrowser
from datetime import datetime
page = requests.get('http://www.singaporebikes.com/index.php?main=used_bikes_listing&sub=adv_search&pgn=1&sort=&keyword=&makers_id=&availability_id=&vehclass_id[]=1&min_price=&max_price=&transmission_id=&year_manufactured=')
tree = html.fromstring(page.text)
url = tree.xpath('//a[@class="readmore_button_text"]/@href')
bikes = []
for link in url:
    page = requests.get(link)
    tree = html.fromstring(page.text)
    image = tree.xpath('//a[@class="lightbox"][1]/@href')
    reg = tree.xpath('//td[@class="text_black"][5]/text()')
    expire = tree.xpath('//td[@class="text_black"][8]/text()')
    model = tree.xpath('//td[@class="text_black"][13]/text()')
    price = tree.xpath('//td[@class="text_black"][16]/text()')
    desc = tree.xpath('//td[@class="text_black"][22]/text()')
    name = tree.xpath('//td[@class="text_black"][23]/text()')
    contact = tree.xpath('//td[@class="text_black"][25]/text()')
    ppd = 0
    href = link
    newprice = price[0].replace('SGD$','').strip()
    newprice = newprice.replace(',','')
    if len(expire[0])>3 and len(newprice)<=5 and len(newprice)>0:
        expiredate = datetime.strptime(expire[0],"%d-%m-%Y")
        today = datetime.today()
        days = (expiredate-today).days
        ppd=float(newprice)/days
        ppd = "{0:.2f}".format(ppd)
    bike = {
        "image":image[0],
        "reg":reg[0],
        "expire":expire[0],
        "model":model[0],
        "price":price[0],
        "desc":desc[0],
        "name":name[0],
        "contact":contact[0],
        "href":href,
        "ppd":'$'+ppd
    }
    bikes.append(bike)
    
with open('bikes.json', 'w') as outfile:
  json.dump(bikes, outfile)
webbrowser.open("file:///Users/alex/Documents/MotorBike%20Scraper/scraper.html",2)    
print "done!"
