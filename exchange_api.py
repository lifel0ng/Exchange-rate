import requests


def get_exchange_rate(
    from_currency,
    to_currency
):

    url = "https://api.example.com/latest"

    params = {
        "base": from_currency,
        "symbols": to_currency
    }

    response = requests.get(
        url,
        params=params
    )

    data = response.json()

    rate = data["rates"][to_currency]

    return rate