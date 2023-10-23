# Movie Information Service
## Инструкция для запуска сервиса

Перед запуском сервиса необходимо установить все зависимости. Для этого необходимо выполнить следующие шаги:

1. Установите и активируйте виртуальное окружение Python.

2. Выполните команду `pip install -r requirements.txt`.

После установки зависимостей вы можете запустить сервис. Для этого выполните одну из следующих команд:

- `uvicorn app:app --port 8001 --reload` - запуск сервиса с помощью Uvicorn на порту 8001 с автоматической перезагрузкой при изменении кода.
- `./run.sh` - запуск сервиса с помощью скрипта run.sh.

## Методы
Документация: `http://localhost:8001/docs`
| Method | Route | Description |
| --- | --- | --- |
| `post` | `/movies` | Add new movie |
| `get` | `/movies` | Get all movies |
| `get` | `/movies/{movie_id}` | Get movie by ID |
| `put` | `/movies/{movie_id}` | Update movie info by ID |
| `delete` | `/movies/{movie_id}` | Delete movie by ID |
