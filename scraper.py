from lxml import html
import requests
page = requests.get('http://www.singaporebikes.com/index.php?main=used_bikes_listing&sub=adv_search&pgn=1&sort=&keyword=&makers_id=&availability_id=&vehclass_id[]=1&min_price=&max_price=&transmission_id=&year_manufactured=')
tree = html.fromstring(page.text)
#This will create a list of prices
prices = tree.xpath('//td[@class="text text_red"]/text()')
print 'Prices: ', prices