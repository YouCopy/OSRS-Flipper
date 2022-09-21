import json
import requests

url = 'https://prices.runescape.wiki/api/v1/osrs/latest'
items = [5300, 3000, 5075, 5502, 5972]
highPrice = []
lowPrice = []

headers = {
    'User-Agent': 'price_tracker'
}

res = requests.get(url, headers = headers)
data = res.json()

for item in items:
    high = data["data"][str(item)]["high"]
    low = data["data"][str(item)]["low"]
    highPrice.append(high)
    lowPrice.append(low)

print('Snapdragon seed: ', lowPrice[0], highPrice[0])
print('Snapdragon: ', lowPrice[1], highPrice[1])
print('\nBird Nest: ', lowPrice[2], highPrice[2])
print('\nPalm Sapling: ', lowPrice[3], highPrice[3])
print('Papaya: ', lowPrice[4], highPrice[4])
