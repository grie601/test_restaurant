# test_restaurant
test EXAMUS

test

Последовательность действий:
--
1)Запустить веб-сервис с любого веб клиента

2)Работа проекта осуществляется на локальном сервере

3)Провести миграцию моделей для работы базы данных. Понадобится база данных, которая указана в Settings.py

Проверка базы данных:
--
Добавление данных в базу данных осуществляется при помощи кнопки "Добавить блюдо в меню" на главной странице. Хранение
медиа контента по пути BASE_DIR/images/

Деплой не предусмотрен заданием


Для использования API
--
Отправка осуществляется по ссылке /api/v1/dishes/ с body запроса {"name": "SomeDish", "nutrition_value": "SomeValue", "value": "SomeValue"} и File = 
{"image" : open('SomePicture'.png, "rb")}

При корректном вводе данных результат запроса будет код 200
