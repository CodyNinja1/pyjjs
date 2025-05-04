from bs4 import BeautifulSoup
import requests

class GoldPrice:
    def __init__(self, Karats: int, SellingPrice: int, PurchasePrice: int):
        self.Karats = Karats
        self.SellingPrice = SellingPrice
        self.PurchasePrice = PurchasePrice

    def __repr__(self):
        return f"{self.Karats}K sell for {self.SellingPrice}, and are bought for {self.PurchasePrice}."

Website = "https://jjsjo.com/"

def GetGoldPrices() -> list[GoldPrice]:
    Prices: list[GoldPrice] = []
    
    WebRequest = requests.get(Website)
    if WebRequest.status_code != 200:
        print(f"Error pinging {Website}: {WebRequest.status_code}")
        return
    
    HtmlContent = WebRequest.text
    BS4Scraper = BeautifulSoup(HtmlContent, features="html.parser")

    PricesTable = BS4Scraper.table
    PricesTableHead = PricesTable.thead
    PricesTableBody = PricesTable.tbody

    for Child in PricesTableBody.children:
        # Every 2nd element (including 0) is \n, so we skip them
        # The karats have " K" or " k" following them, so 24 karats is written as "24 K"
        # Each price is separated with dots instead of commas (so seventy thousand is 70.000)
        Karats: int = int(list(Child.children)[1].text.split(" ")[0])
        SellingPrice: int = int(list(Child.children)[3].text.replace(".", ""))
        PurchasePrice: int = int(list(Child.children)[5].text.replace(".", ""))

        Prices.append(GoldPrice(Karats, SellingPrice, PurchasePrice))

    return Prices
