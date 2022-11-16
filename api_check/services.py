import datetime
import requests
import xmltodict

from dataclasses import dataclass


@dataclass()
class ResponseData:
    bank_name: str | None
    date_created: object


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Content-Type': 'charset=utf-8'
}


def send_request_to_binlist(card_number: int) -> ResponseData:
    """
    Sends request to BinList service via API
    returns either error or Bank Name
    """
    url = f'https://lookup.binlist.net/{card_number}'
    response = requests.get(url, headers=HEADERS)
    tree_raw = xmltodict.parse(response)
    print(tree_raw)
    request = {
        "date_created": 'now',
        "bank_name": "Tinkoff"
    }
    # request logic here
    response = ResponseData(date_created=request.get("date_created"), bank_name=request.get('bank_name'))
    return response


send_request_to_binlist(45717360)
# print(type(datetime.datetime.now()))
