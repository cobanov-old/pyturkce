import requests
import pandas


_URL = "https://sozluk.gov.tr/gts"


def getData(kelime):
    PARAMS = {'ara': kelime}
    r = requests.get(url=_URL, params=PARAMS)
    data = r.json()
    return data
