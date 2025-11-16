# :globe_with_meridians: API-сервис для вопросов и ответов
FastAPI приложение для системы вопросов и ответов. Позволяет создавать вопросы, добавлять к ним ответы, управлять контентом через API.
## Содержание
- [Функциональность](#функциональность)
- [Модели данных](#моделиданных)
- [Технологии](#технологии)
- [Установка](#установка)
- [Автор](#автор)

## Функциональность
## Вопросы
- :white_check_mark: GET /questions/ — список всех вопросов
- :white_check_mark: POST /questions/ — создать новый вопрос
- :white_check_mark: GET /questions/{id} — получить вопрос и все ответы на него
- :white_check_mark: DELETE /questions/{id} — удалить вопрос (вместе с ответами)
## Ответы
- :white_check_mark: POST /questions/{id}/answers/ — добавить ответ к вопросу
- :white_check_mark: GET /answers/{id} — получить конкретный ответ
- :white_check_mark: DELETE /answers/{id} — удалить ответ

## Модели данных
### Question (Вопрос)
```
id: int (primary key)
text: str (текст вопроса)
created_at: datatime (время создания)
```
### Answer (Ответ)
```
id: int (primary key)
question_id: (foreign key to Question)
user_id: str (идентификатор пользователя, UUID)
text: str (текст ответа)
created_at: datatime (время создания)
```
## Технологии 
| Технология | Назначение |
| ----------- | ----------- |
| Python    | основной язык  |
| SQLAlchemy  | ORM для работы с базой данных |
| PostgreSQL   | реляционная база данных |
| Alembic| система миграций базы данных  |
| Docker & Docker Compose     | контейнеризация |
| Pytest   | тестирование |
| Pydantic| валидация данных |

## Установка
### Клонировать репозиторий
```
git clone https://github.com/DmitryLkT/api_service_for_questions_and_answers
```

### :whale: Запуск через Docker
```
docker-compose up --build
```
### :wrench: Локальная разработка
```
# Установка зависимостей
pip install -r requirements.txt

# Настройка переменных окружения
cp .env.example .env

# Запуск миграций
alembic upgrade head

# Запуск приложения
uvicorn app.main:app --reload
```
### Тестирование
```
# Запуск тестов
pytest
```
## Автор
Дмитрий Л.
- Почта: <Dmitry.plus1@yandex.ru>
- GitHub: [DmitryLkT](https://github.com/DmitryLkT)

