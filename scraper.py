from lxml import html
import requests, json, webbrowser
from datetime import datetime

bikes = []

page = requests.get('http://www.singaporebikes.com/index.php?main=used_bikes_listing&sub=adv_search&pgn=1&sort=&keyword=&makers_id=&availability_id=&vehclass_id[]=1&min_price=&max_price=&transmission_id=&year_manufactured=')
tree = html.fromstring(page.text)
url = tree.xpath('//a[@class="readmore_button_text"]/@href')

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
        "ppd":ppd
    }
    bikes.append(bike)
    
page = requests.get('http://www.sgbikemart.com.sg/search?usedbike_model=phantom&type_id=&price_range=&class=&registration_date=&categories=1&dealers=&availability=Available&search_type=usedbikes')
tree = html.fromstring(page.text)
url = tree.xpath('//span[@class="title"]/a/@href')

for link in url:
    page = requests.get(link)
    tree = html.fromstring(page.text)
    image = tree.xpath('//img[@id="watermark"]/@src')
    reg = tree.xpath('//table[@id="table-form"][1]/tr[6]/td[3]/text()')
    expire = tree.xpath('//table[@id="table-form"][1]/tr[7]/td[3]/text()')
    model = tree.xpath('//table[@id="table-form"][1]/tr[3]/td[3]/text()')
    price = tree.xpath('//table[@id="table-form"][1]/tr[11]/td[3]/text()')
    desc = tree.xpath('//div[@class="expander"]/text()')
    name = tree.xpath('//div[@class="block"]/div[@class="contact_name float_left"]/text()')
    contact = tree.xpath('//div[@class="block"]/div[@class="float_right"]/text()')
    reg = reg[0].strip()
    expire = expire[0].strip()
    model = model[0].strip()
    price = price[0].strip()
    desc = desc[0].strip()
    name = name[0].strip()
    contact = contact[0].strip()
    ppd = 0
    href = link
    newprice = price.replace('$','')
    newprice = newprice.replace(',','')
    if len(expire)>3 and len(newprice)<=5 and len(newprice)>0:
        expiredate = datetime.strptime(expire,"%d %b %Y")
        today = datetime.today()
        days = (expiredate-today).days
        ppd=float(newprice)/days
        ppd = "{0:.2f}".format(ppd)
    bike = {
        "image":image[0],
        "reg":reg,
        "expire":expire,
        "model":model,
        "price":price,
        "desc":desc,
        "name":name,
        "contact":contact,
        "href":href,
        "ppd":ppd
    }
    bikes.append(bike)

with open('bikes.json', 'w') as outfile:
  json.dump(bikes, outfile)
webbrowser.open("file:///Users/alex/Documents/MotorBikeScraper/scraper.html",2)    
print "done!"
