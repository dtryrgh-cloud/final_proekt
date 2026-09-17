# Работа с базой данных
# Задание 2
- Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
- Для этого: выведи все трекеры заказов и их статусы. 
- Статусы определяются по следующему правилу:
- Если поле finished == true, то вывести статус 2.
- Если поле canсelled == true, то вывести статус -1.
- Если поле inDelivery == true, то вывести статус 1.
- Для остальных случаев вывести 0.

# Тестовый стенд веб-приложения: https://08e2eab9-4f06-4736-91b9-ef65899b0c66.serverhub.praktikum-services.ru/
# Документация API: https://08e2eab9-4f06-4736-91b9-ef65899b0c66.serverhub.praktikum-services.ru/docs/

# Мониторинг статусов заказов в PostgreSQL

Ниже представлен фрагмент сеанса работы с базой данных `scooter_rent`.

## Сеанс терминала

```bash
morty@server-08e2eab9-4f06-4736-91b9-ef65899b0c66:~$ psql -U morty -d scooter_rent
Password for user morty: 
psql (11.18 (Debian 11.18-0+deb10u1))
Type "help" for help.

scooter_rent=# SELECT "Orders".track,
  CASE
    WHEN "Orders".finished = true THEN 2
    WHEN "Orders".cancelled = true THEN -1
    WHEN "Orders"."inDelivery" = true THEN 1
    ELSE 0
  END AS status
FROM "Orders";
 track | status 
-------+--------
 77767 |      0
(1 row)

scooter_rent=# \q
```

# Порядок действий
1. Через API создаём заказ (`POST /api/v1/orders`) — сервер вернул номер трека 77767
2. Подключаемся к тестовому серверу по SSH
3. Подключаемся к БД scooter_rent пользователем morty
4. Выполняем запрос вычисления статуса заказа по логическим полям
5. Завершаем работу с БД

В ходе выполнения запроса ошибок не возникло. Заказ с треком 77767 находится в статусе 0, что соответствует бизнес-логике: он только создан и ещё не передан в доставку (`inDelivery`, `cancelled`, `finished` — все `false`).
