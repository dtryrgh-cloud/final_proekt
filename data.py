# Заголовки HTTP-запроса

CREATE_ORDER_HEADERS = {

    'Content-Type': 'application/json'

}


# Тело запроса для создание заказа

CREATE_ORDER_PAYLOAD = {

    "firstName": "Daniil",

    "lastName": "Gordienko",

    "address": "Trubnaya 150",

    "metroStation": 4,

    "phone": "+79629511495",

    "rentTime": 3,

    "deliveryDate": "2026-09-16",

    "comment": "Позвонить за 30 минут до доставки",

    "color": ["BLACK"]

}