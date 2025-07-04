# Mini Blog на Flask в Docker

Это простое веб-приложение мини-блог на Flask с хранением данных в SQLite. Приложение запускается в Docker-контейнере.

## Возможности
- Просмотр списка постов
- Просмотр отдельного поста
- Добавление нового поста через форму

## Быстрый старт

1. Установите [Docker Desktop](https://www.docker.com/products/docker-desktop/) и убедитесь, что он запущен.
2. Откройте терминал в папке с проектом:
   ```
   cd "D:/Языки программирования/Docker"
   ```
3. Соберите и запустите контейнер:
   ```
   docker-compose up --build
   ```
4. Откройте в браузере [http://localhost:5000](http://localhost:5000)

## Структура проекта
- `app.py` — основной код приложения
- `requirements.txt` — зависимости Python
- `Dockerfile` — инструкция сборки контейнера
- `docker-compose.yml` — удобный запуск через Docker Compose

## Остановка приложения

Для остановки приложения нажмите `Ctrl+C` в терминале или выполните:
```
docker-compose down
```
