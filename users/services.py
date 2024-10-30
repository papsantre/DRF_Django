import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):
    """Создаем продукт в страйпе"""
    title_product = f"{instance.payment_course}" if instance.payment_course else instance.payment_lesson
    stripe_product = stripe.Product.create(name=f'{title_product}')
    return stripe_product.id


def create_stripe_price(payment, stripe_product_id):
    """Создаем цену в страйпе"""
    price = stripe.Price.create(
        currency="rub",
        unit_amount=payment.cost * 100,
        #product_data={"name": "Payment"},
        product=stripe_product_id
    )
    return price.id


def create_stripe_session(price_id):
    """Создаем сессию для оплаты в страйпе"""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price_id, "quantity": 1}],
        mode="payment",
    )
    return session.id, session.url

