# pyjjs
Scraper for the [Jordanian Jewelers' Syndicate's website](https://jjsjo.com/), since there's no API for it.

## Prerequistes
`beautifulsoup4` and `requests`

## Functionality
The only function that exists is `GetGoldPrices() -> list[GoldPrice]`, which scrapes the website and returns a list of gold prices per karat.\
The `GoldPrice` class only has the `Karat: int`, `SellingPrice: int`, and `PurchasePrice: int` members.\
It can also be converted to a string like:
```python
print(GetGoldPrices()[0]) # "{Karats: 24, SellingPrice: 76200, PurchasePrice: 73800}"
print(str(GetGoldPrices()[0])) # "24K sell for 76200, and are bought for 73800."
```
