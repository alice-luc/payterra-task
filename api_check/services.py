from dataclasses import dataclass


@dataclass()
class ResponseData:
    bank_name: str | None
    date_created: object


def send_request_to_binlist(card_number: int) -> ResponseData:
    """
    Sends request to BinList service via API
    returns either error or Bank Name
    """
    request = {
        "date_created": 'now',
        "bank_name": "Tinkoff"
    }
    # request logic here
    response = ResponseData(date_created=request.get("date_created"), bank_name=request.get('bank_name'))
    return response


