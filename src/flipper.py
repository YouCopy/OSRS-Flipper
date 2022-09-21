import requests

def _update():
    url = 'https://prices.runescape.wiki/api/v1/osrs/latest'
    dic = {}

    headers = {
        'User-Agent': 'ge_flipper'
    }

    res = requests.get(url, headers = headers)
    data = res.json()

    for item in data["data"]:
        high = data["data"][str(item)]["high"]
        low = data["data"][str(item)]["low"]
        if high is None or low is None:
            ##Need to assign it a value or else sorting it doesn't work
            margin = -10000
            roi = -10000
        else:
            margin = int(high) - int(low)
            roi = (margin/low)*100
        dic[int(item)] = roi
    return dic

def find_name():
    url = 'https://prices.runescape.wiki/api/v1/osrs/mapping'
    dic = {}

    headers = {
        'User-Agent': 'name_finder'
    }

    res = requests.get(url, headers = headers)
    data = res.json()

    for item in range(len(data)):
        name = data[item]["name"]
        id = data[item]["id"]
        dic[int(id)] = name
    return dic

def find_volume():
    url = 'https://prices.runescape.wiki/api/v1/osrs/6h'
    dic = {}

    headers = {
        'User-Agent': 'volume_finder'
    }

    res = requests.get(url, headers = headers)
    data = res.json()

    for item in data["data"]:
        high_vol = data["data"][str(item)]["highPriceVolume"]
        low_vol = data["data"][str(item)]["lowPriceVolume"]
        if high_vol is None or low_vol is None:
            comb_vol = 0
        else:
            comb_vol = int(high_vol) + int(low_vol)
        dic[int(item)] = comb_vol
    return dic

def print_list(margin_list, name_list, vol_list):
    for w in sorted(margin_list, key=margin_list.get, reverse=True):
        if w == 2660:
            continue
        try:
            if vol_list[w] > 10000:
                print(name_list[w], ': %.2f' % margin_list[w], '%')
        except Exception:
            pass

def main():
    margin_list = _update()
    name_list = find_name()
    vol_list = find_volume()
    print_list(margin_list, name_list, vol_list)

if __name__ == '__main__':
    main()