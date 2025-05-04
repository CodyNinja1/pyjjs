# pyjjs
Scraper for the Jordanian Jewelers' Syndicate's website, since there's no API for it.

## Prerequistes
`beautifulsoup4` and `requests`

## Functionality
The only function that exists is `GetGoldPrices() -> list[GoldPrice]`, which scrapes the website and returns a list of gold prices per karat.
