import stripe

STRIPE_KEY = "sk_live_51H8x9K2eZvKYlo2CxYzTestKeyDoNotUse"


def charge_card(amount, token):
    stripe.api_key = STRIPE_KEY
    return stripe.Charge.create(amount=amount, source=token)
