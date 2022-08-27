import requests
from lxml import html
from winotify import Notification, audio

def price_getter():
    url = "https://www.ebay.ca/itm/155134552907?epid=22054478105&hash=item241ebd6b4b:g:nowAAOSwHEhjAlzO&amdata=enc%3AAQAHAAAA0AY1UZ%2FeHHfp29u4aB93l829ZWtWSC63AKeEjbZ%2BM9fjd1gj9oKh6UE%2BgAyubXiLTJDVb34lK%2B%2BZIKD2oxVActR7qmLvT1KWJgUYsKObN7s4RQZmZUy8SgPOvL3HorJB%2FyWNWOc3gtzGVxNUBltWmC3WYlbOseLvzblV2hK1ebH%2Br%2F24ANk96pbwWS6jIX2S7HpY2eho3PktCSFbOyd%2BN6UeD1d8PjqWjPhqnkUG9%2Bar8fO0oJ67iuZpNUndGepr0RwcidgE2Mjd5e3jXM3MUgc%3D%7Ctkp%3ABFBMiJPMh9xg"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Accept-Encoding': None
    }

    productPage = requests.get(url)
    tree = html.fromstring(productPage.content)
    price = tree.xpath('//span[@class="notranslate"]/text()')[0].split('$')[1]
    return price

def send_notification():
    n = Notification(app_id="EBay Price Tracker", 
                    title = "Price Notification",
                    msg = "The product is below the desired price now.",
                    duration= "short")

    n.show()

if __name__ == '__main__':
    price = float(price_getter())

    if price < 300:
        send_notification()