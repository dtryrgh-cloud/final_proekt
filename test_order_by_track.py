# Алексей Дмитрев, 46-я когорта - Финальный проект. Инженер по тестированию плюс


#     Шаги автотеста:
#     1. Выполнить запрос на создание заказа.
#     2. Сохранить номер трека заказа.
#     3. Выполнить запрос на получение заказа по треку заказа.
#     4. Проверить, что код ответа равен 200.

from sender_stand_request import create_order, get_order_by_track

def test_get_order_by_track():
# Для начала создаем заказ
    create_order_response = create_order()
    assert create_order_response.status_code == 201, "Ошибка создания заказа. Необходимо проверить данные запроса"
    track = create_order_response.json().get('track')
    assert track, "В ответе на создание заказа отсутствует поле 'track'"
# Ну а теперь попробуем получить заказ по номеру
    get_order_response = get_order_by_track(track)
    assert get_order_response.status_code == 200, f"Ошибка получения заказа {track}"
    print('Тест пройден!')
if __name__ == '__main__':
    test_get_order_by_track()