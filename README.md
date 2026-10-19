# Автотесты API и UI на Python: pytest + Playwright

Пет-проект для практики автоматизации тестирования: API-тесты на `requests` и UI-тесты на Playwright,
с валидацией ответов через pydantic и моками сетевых запросов.

## Стек

- Python 3.12, pytest
- requests — API-тесты
- Playwright (pytest-playwright) — UI-тесты и моки
- pydantic v2 — схемы ответов API
- python-dotenv — настройки и учётные данные из `.env`
- logging — логирование запросов и шагов тестов

## Что покрыто

**API — [DummyJSON](https://dummyjson.com)**
- авторизация: логин (позитивные и негативные случаи), `/auth/me`, доступ к закрытому эндпоинту с токеном и без
- товары: получение по id, поиск, обновление, 404 для несуществующего товара
- корзины: создание, получение, удаление
- каждый ответ проверяется pydantic-схемой с `extra="forbid"`: тест падает и на лишних полях в ответе

**UI — [Swag Labs (saucedemo)](https://www.saucedemo.com)**
- успешный логин
- негативный логин (параметризован): заблокированный пользователь, пустые поля, пустой пароль, неверный пароль

**Моки (`page.route`)**
- [Playwright demo](https://demo.playwright.dev/api-mocking): подмена списка, пустой список, ответ 500
- saucedemo без картинок (`route.abort`): каталог остаётся рабочим

## Структура

```
src/
  config.py            # настройки из .env
  api/
    http_client.py     # общий HTTP-клиент с логированием
    schemas/           # pydantic-схемы ответов
    test_data/         # тестовые данные
  ui/
    test_data/
tests/
  api/                 # API-тесты
  ui/                  # UI-тесты и моки
conftest.py            # фикстуры: токен авторизации (scope=session), логирование тестов
pytest.ini
```

## Установка

```bash
git clone https://github.com/ShustinEgor/python-playwright-tests.git
cd python-playwright-tests
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env
```

В `.env` заполни `USERNAME_UI` и `PASSWORD_UI`. Это публичные тестовые данные saucedemo,
они написаны на главной странице сайта.

## Запуск

```bash
pytest                     # все тесты
pytest tests/api           # только API
pytest tests/ui --headed   # только UI, с открытым браузером
pytest -k mock             # тесты, в имени которых есть "mock"
pytest --browser firefox   # UI в другом браузере
```

## Приёмы, использованные в проекте

- параметризация с читаемыми именами случаев (`pytest.param(..., id=...)`)
- фикстура токена со `scope="session"`: логин один раз на весь прогон
- `autouse`-фикстура для логирования начала и конца каждого теста
- обязательные настройки через `os.environ[...]`: тест падает сразу, если в `.env` чего-то не хватает
- локаторы по ролям (`get_by_role`) и web-first проверки (`expect`)

## Находки

Моки на демо-странице Playwright показали две проблемы фронтенда:
- при ответе 500 с данными страница показывает данные: статус ответа не проверяется;
- при ответе с пустым телом страница бесконечно показывает «Loading...».