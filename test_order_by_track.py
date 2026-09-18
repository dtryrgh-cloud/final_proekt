# Гордиенко Даниил, 46-я когорта - Финальный проект. Инженер по тестированию плюс


#     Автотесты проверяют:
#     1. Создание заказа возвращает код 201.
#     2. В ответе на создание заказа присутствует поле 'track'.
#     3. Получение заказа по треку возвращает код 200.

from sender_stand_request import create_order, get_order_by_track


def test_create_order_returns_201():
    create_order_response = create_order()
    assert create_order_response.status_code == 201, "Ошибка создания заказа. Необходимо проверить данные запроса"


def test_create_order_response_contains_track():
    create_order_response = create_order()
    track = create_order_response.json().get('track')
    assert track, "В ответе на создание заказа отсутствует поле 'track'"


def test_get_order_by_track_returns_200():
    track = create_order().json().get('track')
    get_order_response = get_order_by_track(track)
    assert get_order_response.status_code == 200, f"Ошибка получения заказа {track}"
