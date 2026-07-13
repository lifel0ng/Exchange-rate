from exchange_api import get_exchange_rate



def exchange_tool(
        from_currency,
        to_currency,
        amount
):

    rate = get_exchange_rate(
        from_currency,
        to_currency
    )


    result = amount * rate


    return {
        "amount": amount,
        "from": from_currency,
        "to": to_currency,
        "rate": rate,
        "result": result
    }