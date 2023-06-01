# Автотесты для книжного онлайн магазина Oscar
## Описание

Ссылка на сайт http://selenium1py.pythonanywhere.com/ru/

Данный проект представляет собой набор автоматизированных тестов для онлайн магазина Oscar. 
Тесты написаны на языке Python с использованием фреймворка pytest и библиотеки Selenium, так же использовала
некоторые дополнительные возможности Pytest, такие как маркер xfail и параметризацию.

## Особенности проекта

- Автоматизированное тестирование различных функциональностей веб-приложения
- Разделение тестов на модули и страницы для удобного поддержания и масштабирования
- Использование паттерна Page Object для более читаемого и удобного кода
- Использование маркировок pytest для управления запуском и категоризацией тестов

## Структура проекта

- `pages/` - содержит классы страниц с методами и локаторами.
- `tests/` - содержит тестовые сценарии для различных функций приложения.
- `conftest.py` - файл с настройками и фикстурами для тестов.
- `requirements.txt` - список зависимостей проекта.

## Установка и запуск

1. Клонируйте репозиторий на свой локальный компьютер.
2. Установите необходимые зависимости, выполнив команду pip install -r requirements.txt.
3. Настройте файлы конфигурации, указав URL адрес тестируемого веб-приложения и другие параметры.
4. Запустите тесты, используя команду pytest. Вы можете передать различные параметры командной строки, такие как `-s` для вывода логов и `-m` для запуска определенных маркированных тестов.

## Тесты

Первый файл - test_main_page.py содержит тесты, направленные на проверку основных функций главной страницы приложения. 
Эти тесты включают:

- Проверку наличия ссылки на страницу авторизации для гостя
- Проверку возможности перехода на страницу авторизации с главной страницы
- Проверку наличия ссылки на страницу авторизации для гостя на главной странице
- Проверку, что гость не видит товары в корзине, когда переходит в корзину с главной страницы

Второй файл - test_product_page.py содержит тесты, направленные на проверку функциональности страницы продукта. 
Эти тесты включают:

- Проверку возможности добавления товара в корзину гостем с помощью кнопки "Добавить в корзину"
- Проверку наличия ссылки на страницу авторизации для гостя на странице продукта
- Проверку возможности перехода на страницу авторизации со страницы продукта
- Проверку, что гость не видит товары в корзине, когда переходит в корзину со страницы продукта
- Проверку возможности зарегистрированного пользователя добавить товар в корзину
- Проверку возможности перехода зарегистрированного пользователя на страницу корзины
- Проверку успешного выхода зарегистрированного пользователя из аккаунта
- Проверку, что гость не видит товары в корзине, когда переходит в корзину с главной страницы
- Проверку возможности гостя перейти на страницу авторизации с главной страницы
- Проверку наличия ссылки на страницу авторизации для гостя на главной странице
- Проверку, что зарегистрированный пользователь может просмотреть свой профиль

Оба файла тестов покрывают различные аспекты функциональности приложения и помогают проверить его работу в разных сценариях использования.