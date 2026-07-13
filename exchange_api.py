import requests


def get_exchange_rate(
        base_currency,
        target_currency
):

    url = (
        f"https://api.frankfurter.dev/v2/rate/"
        f"{base_currency}/"
        f"{target_currency}"
    )


    response = requests.get(url)


    data = response.json()


    return data["rate"]