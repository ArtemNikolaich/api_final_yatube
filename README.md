### Описание проекта
Yatube_API - это API-сервис, разработанный на основе Django REST Framework, который предоставляет простой и удобный способ взаимодействия с базой данных проекта Yatube.

С помощью Yatube_API пользователи могут выполнять запросы к базе данных для получения информации о постах, группах, комментариях и подписках. Авторизованные пользователи имеют дополнительные возможности, такие как создание, редактирование и удаление постов и комментариев. Они также могут подписываться на других пользователей.

API предоставляет уникальный способ взаимодействия с Yatube, обеспечивая удобство и гибкость в работе с базой данных.

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ArtemNikolaich/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env 
python -m venv venv (для Windows)

```

```
source env/bin/activate
source venv/Scripts/activate (для Windows)
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
python -m pip install --upgrade pip (для Windows)
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
python manage.py migrate (для Windows)
```

Запустить проект:

```
python3 manage.py runserver
python manage.py runserver (для Windows)
```
### Примеры запросов
```
Получение всех постов: GET /api/v1/posts/
```
```
Редактирование поста: PUT /api/v1/posts/{id}/
```
```
Добавление комментария: POST /api/v1/posts/{post_id}/comments/
```
```
Получение подписок пользователя: GET /api/v1/follow/
```
```
Получение списка групп: GET /api/v1/groups/
```
### Автор проекта:
## Калинин Артём