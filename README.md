# Telegram Spam Bot

Этот скрипт на Python представляет собой спам-бота для Telegram, который использует несколько аккаунтов для отправки сообщений и реакций в указанный чат. 

## Установка

1. Склонируйте репозиторий или скачайте скрипт.
2. Установите необходимые зависимости:
    ```bash
    pip install -r requirements.txt
    ```
3. Создайте файл `.env` в корневом каталоге и добавьте ваши Telegram API ID, API Hash и номера телефонов:
    ```
    API_ID1=ваш_api_id_1
    API_HASH1=ваш_api_hash_1
    PHONE_NUMBER1=ваш_номер_телефона_1
    ```

## Конфигурация

В скрипте можно настроить следующие параметры:
- **Никнеймы и имена пользователей**: массивы `nicknames` и `usernames` содержат списки возможных никнеймов и имен пользователей.
- **GIF-файлы**: укажите директорию с GIF-файлами в переменной `gif_directory`.
- **Ключевые слова**: массивы `keywords_layerzero`, `keywords_liarzero`, `keywords_hello` и `keywords` содержат ключевые слова, на которые бот будет реагировать.
- **Эмоджи**: массивы `emojis_layerzero`, `emojis_hello`, `emojis_liarzero` и `emojis_other` содержат эмоджи для реакций на сообщения.
- **Интервалы времени**: переменные `time_interval_reply`, `time_interval_1`, `time_interval_2`, `time_interval_3` задают временные интервалы для различных действий бота.

## Запуск

1. Убедитесь, что все зависимости установлены и файл `.env` настроен.
2. Запустите скрипт:
    ```bash
    python main.py
    ```

## Функционал

- **Авторизация клиентов**: бот проверяет авторизацию аккаунтов и, если необходимо, запрашивает код подтверждения.
- **Присоединение к чату**: бот присоединяется к указанному чату, если ещё не состоит в нём.
- **Отправка GIF-файлов**: бот периодически отправляет случайные GIF-файлы из указанной директории в чат.
- **Отправка текстовых сообщений**: бот периодически отправляет заданное текстовое сообщение в чат.
- **Смена никнеймов и имен пользователей**: бот периодически меняет никнеймы и имена пользователей.
- **Реакции на сообщения**: бот реагирует на сообщения в чате, содержащие определенные ключевые слова, с помощью заданных эмоджи.

## Примечания

- Убедитесь, что ваш бот соблюдает правила и политику использования Telegram.
- Использование нескольких аккаунтов для автоматической отправки сообщений может привести к блокировке аккаунтов. Используйте этот скрипт с осторожностью.

