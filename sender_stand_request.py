import requests

from configuration import BASE_URL, CREATE_ORDER_PATH, GET_ORDER_BY_TRACK_PATH

from data import CREATE_ORDER_HEADERS, CREATE_ORDER_PAYLOAD

# Создание заказа через POST и возвращаем объект ответа
def create_order():
    url = BASE_URL + CREATE_ORDER_PATH

    response = requests.post(

        url,

        json=CREATE_ORDER_PAYLOAD,

        headers=CREATE_ORDER_HEADERS

    )

    print(f'Create order: статус {response.status_code}, тело: {response.text}')

    return response

# Для получения заказа по номеру трека отправляем GET запрос и возвращаем объект ответа
def get_order_by_track(track):
    url = BASE_URL + GET_ORDER_BY_TRACK_PATH

    params = {'t': track}

    response = requests.get(url, params=params)

    print(f'Get order by track: статус {response.status_code}, тело: {response.text}')

    return response