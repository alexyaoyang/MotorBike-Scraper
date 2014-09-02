from lxml import html
import SocketServer
import time
import BaseHTTPServer
import requests, json

def test():
    print "test got called"

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*");
        self.send_header("Access-Control-Expose-Headers", "Access-Control-Allow-Origin");
        self.send_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
        self.end_headers()
        page = requests.get('http://www.singaporebikes.com/index.php?main=used_bikes_listing&sub=adv_search&pgn=1&sort=&keyword=&makers_id=&availability_id=&vehclass_id[]=1&min_price=&max_price=&transmission_id=&year_manufactured=')
        tree = html.fromstring(page.text)
        url = tree.xpath('//a[@class="readmore_button_text"]/@href')
        bikes = []
        for link in url:
            page = requests.get(link)
            tree = html.fromstring(page.text)
            image = tree.xpath('//a[@class="lightbox"][1]/@href')
            #reg = tree.xpath('//td[@class="text_black"][5]/text()')
            #expire = tree.xpath('//td[@class="text_black"][8]/text()')
            #model = tree.xpath('//td[@class="text_black"][13]/text()')
            #price = tree.xpath('//td[@class="text_black"][16]/text()')
            #desc = tree.xpath('//td[@class="text_black"][22]/text()')
            #name = tree.xpath('//td[@class="text_black"][23]/text()')
            #contact = tree.xpath('//td[@class="text_black"][25]/text()')
            info = tree.xpath('//td[@class="text_black"]/text()')
            bike = {
                "image":image[0],
                #"reg":reg[0],
                #"expire":expire[0],
                #"model":model[0],
                #"price":price[0],
                #"desc":desc[0],
                #"name":name[0],
                #"contact":contact[0],
                "info":info
            }
            bikes.append(json.dumps(bike))
    
        print bikes[0]
        self.wfile.write(bikes)
        return bikes
            
        httpd = SocketServer.TCPServer(("alexyy.com", 80), MyHandler)
        httpd.serve_forever()