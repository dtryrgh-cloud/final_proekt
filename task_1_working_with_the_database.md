# Работа с базой данных
# Задание 1
- Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
- Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

# Тестовый стенд веб-приложения: https://08e2eab9-4f06-4736-91b9-ef65899b0c66.serverhub.praktikum-services.ru/
# Документация API: https://08e2eab9-4f06-4736-91b9-ef65899b0c66.serverhub.praktikum-services.ru/docs/

# Подключение по SSH и работа с PostgreSQL

```bash
morty@server-08e2eab9-4f06-4736-91b9-ef65899b0c66:~$ psql -U morty -d scooter_rent
Password for user morty: 
psql (11.18 (Debian 11.18-0+deb10u1))
Type "help" for help.

scooter_rent=# SELECT "Couriers".login, COUNT("Orders".id) AS delivery_count
FROM "Orders"
JOIN "Couriers" ON "Orders"."courierId" = "Couriers".id
WHERE "Orders"."inDelivery" = true
GROUP BY "Couriers".login;
 login | delivery_count 
-------+----------------
(0 rows)

scooter_rent=# \q
```

# Порядок действий
1. Подключаемся к тестовому серверу по SSH (ключевая пара, авторизация по publickey)
2. Подключаемся к БД scooter_rent пользователем morty
3. Через API создаём курьера (`POST /api/v1/courier`) и заказ (`POST /api/v1/orders`)
4. Выполняем запрос: выборка количества доставок по каждому курьеру
5. Результат — 0 строк: курьер и заказ созданы отдельными запросами и не связаны между собой (`courierId` заказа не заполнен), поэтому JOIN не находит совпадений и запись со статусом `inDelivery = true` отсутствует
6. Завершаем работу с БД
