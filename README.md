# test_restaurant
test EXAMUS

test

Последовательность действий:
--
Запустить веб-сервис с любого веб клиента
Проветси миграцию моделей для работы базы данных. Понадобится база данных, которая указана в Settings.py
Добавление данных в базу данных осуществляется при помощи кнопки "Добавить блюдо в меню" на главной странице
Деплой не предусмотрен заданием
Работа проекта осуществляется на локальном сервере

Для использования API
--
Отправка осуществляется по ссылке /api/v1/dishes/ с body запроса {"name": "SomeDish", "nutrition_value": "SomeValue", "value": "SomeValue"} и File = 
{""}

При корректном вводе данных результат запроса будет код 200