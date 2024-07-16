import os
import random
import asyncio
import logging
from dotenv import load_dotenv
from pyrogram import Client, errors, filters

# Загрузка переменных окружения из .env файла
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Список клиентов
api_id1 = os.getenv('API_ID1')
api_hash1 = os.getenv('API_HASH1')
phone_number1 = os.getenv('PHONE_NUMBER1')
session_name1 = "my_account1"

api_id2 = os.getenv('API_ID2')
api_hash2 = os.getenv('API_HASH2')
phone_number2 = os.getenv('PHONE_NUMBER2')
session_name2 = "my_account2"

api_id3 = os.getenv('API_ID3')
api_hash3 = os.getenv('API_HASH3')
phone_number3 = os.getenv('PHONE_NUMBER3')
session_name3 = "my_account3"

#Просто пример проксика 
# proxy = {
#     "scheme": "socks5",
#     "hostname": "195.208.84.211",
#     "port": 64563,
#     "username": "YvHEyB3a",
#     "password": "N4yuYYGy"
# }


# Имена для никнеймов
nicknames = [
    "Not Elon", "Maxim", "AlexCrypto", "MarkDeFi",
    "RewardRaider", "Jake", "Mike", "BobStake",
    "Max", "Viktor", "Aslan", "Boby", "Misha",
    "Emily", "Jackson", "Liam", "Emma"
]
usernames = [
    "ElitePhantom324", "CosmicTycoon456", "BlockBoss234",
    "ApexPredator4573", "SatoshiSeeker546","HodlHero3154",
    "SupremeMaverick325", "DynamicRogue763", "ZephyrStorm876",
    "VortexGuardian243", "AlphaSpectre3478", "HyperNova2363",
    "AltcoinAce3572", "CryptoCaster4674", "SunnySam091",
    "SmartScott1315", "RockinRyan1532", "AceAlex135",
    "VividVic4653", "JakeTheGreat687", "BoldBen456",
]
# Директория с GIF-файлами
gif_directory = r'C:\Users\db\Pictures\GIF'

#Ключевые слова, по которым происходит отправка реакций 
keywords_layerzero = ["layerzero", "l0", "brian", "браян", "брайн", "дотер", "л0", "леерзиро", "леер", "зеро"]
keywords_liarzero = ["liarzero", "сибил", "sybil", "ton", "liar"]
keywords_hello = ["привет", "гм", "gm", "hi", "hello"]
keywords = ["lfg", "лфг", "moon", "to the moon", "rocket", "up", "buy the dip", "lets go","pump"]

#Эмоджи для отправки реакций
emojis_layerzero = ["🤮", "😡", "👎", "💩", "🤡"]
emojis_hello = ["❤️"]
emojis_liarzero = ["🐳", "🌚"]
emojis_other = ["🔥", "⚡", "😎"]

#Интвервалы, чтоб бот казался более живым 
time_interval_reply = random.randint(10, 50)#Интервал на отправку реакций 
time_interval_1 = random.randint(60, 300)# интервал отправки гиф с 1 аккаунта 
time_interval_2 = random.randint(60, 300)# интервал отправки гиф с 2 аккаунта
time_interval_3 = random.randint(60, 300)# интервал отправки гиф с 3 аккаунта

# Создание клиентов
app1 = Client(session_name1, api_id=api_id1, api_hash=api_hash1)
app2 = Client(session_name2, api_id=api_id2, api_hash=api_hash2)
app3 = Client(session_name3, api_id=api_id3, api_hash=api_hash3)

# Проверка на чат, если нет в чате, добавляемся 
async def join_chat(app, chat_link):
    try:
        # Получаем информацию о чате
        chat = await app.get_chat(chat_link)
        # Проверяем, состоит ли пользователь в чате
        if app.get_peer_id(chat_link) not in await app.get_dialogs():
            # Если пользователь не состоит в чате, присоединяемся к нему
            await app.join_chat(chat_link)
            logger.info(f"{app.name}: Присоединились к чату {chat.title}")
        else:
            logger.info(f"{app.name}: Уже состоим в чате {chat.title}")
    except errors.ChatAdminRequired:
        logger.error(f"{app.name}: Для присоединения к чату требуются права администратора.")
    except errors.UsernameNotOccupied:
        logger.error(f"{app.name}: Чат не найден по ссылке {chat_link}.")
    except Exception as e:
        logger.error(f"{app.name}: Ошибка при присоединении к чату: {e}")

# Функция отправки GIF-файлов
async def send_saved_gifs(app, interval, chat_id):
    while True:
        gif_files = os.listdir(gif_directory)
        if not gif_files:
            logger.warning(f"{app.name}: Нет доступных GIF-файлов для отправки.")
            await asyncio.sleep(interval)
            continue

        for gif_file in gif_files:
            try:
                gif_path = os.path.join(gif_directory, gif_file)
                await app.send_document(chat_id, gif_path)
                logger.info(f"{app.name}: Успешно отправлен GIF-файл {gif_file} в чат {chat_id}.")

            except Exception as e:
                logger.error(f"{app.name}: Не удалось отправить GIF {gif_file} в чат {chat_id}: {e}")

            await asyncio.sleep(interval)


async def send_text_messages(app, interval, chat_id, message):
    while True:
        try:
            await app.send_message(chat_id, message)
            logger.info(f"{app.name}: Успешно отправлено сообщение '{message}' в чат {chat_id}.")
        except Exception as e:
            logger.error(f"{app.name}: Не удалось отправить сообщение в чат {chat_id}: {e}")

        await asyncio.sleep(interval)


# Функция смены никнейма
async def change_profile(app):
    while True:
        try:
            # Смена никнейма
            new_nickname = random.choice(nicknames)
            await app.update_profile(first_name=new_nickname)
            logger.info(f"{app.name}: Никнейм изменен на: {new_nickname}")
            new_username = random.choice(usernames)
            await app.update_profile(username=new_username)

        except Exception as e:
            logger.error(f"{app.name}: Не удалось изменить профиль: {e}")

        await asyncio.sleep(43200)  # Ждем 60 секунд перед следующей сменой, Саня попросил раз в 12 часов или 24 

# Функция авторизации клиента
async def authorize_client(app, phone_number):
    me = await app.get_me()
    if me is None:
        logger.info(f"{app.name}: Пользователь не авторизован. Отправка кода подтверждения...")
        await app.send_code(phone_number, force_sms=False)
        code = input(f"{app.name}: Введите код подтверждения: ")
        try:
            await app.sign_in(phone_number=phone_number, code=code)
            logger.info(f"{app.name}: Клиент успешно авторизован")
        except errors.SessionPasswordNeeded:
            password = input(f"{app.name}: Введите пароль 2FA: ")
            await app.check_password(password=password)
            logger.info(f"{app.name}: Клиент успешно авторизован с 2FA")
    else:
        logger.info(f"{app.name}: Пользователь уже авторизован")

#Можно убрать какой либо клиент или добавить, чтоб спамил реакции с меньшего кол-ва акков или с большего
@app1.on_message(filters.chat("@chattestingl0_chat") & filters.text)
@app2.on_message(filters.chat("@chattestingl0_chat") & filters.text)
@app3.on_message(filters.chat("@chattestingl0_chat") & filters.text)
async def my_handler(client, message):
    if message.text.lower() in keywords_layerzero:
        await asyncio.sleep(time_interval_reply)
        await message.react(random.choice(emojis_layerzero))
    elif message.text.lower() in keywords_hello:
        await asyncio.sleep(time_interval_reply)
        await message.react(random.choice(emojis_hello))
    elif message.text.lower() in keywords_liarzero:
        await asyncio.sleep(time_interval_reply)
        await message.react(random.choice(emojis_liarzero))
    elif message.text.lower() in keywords:
        await asyncio.sleep(time_interval_reply)
        await message.react(random.choice(emojis_other))

# Основная функция
async def main():
    chat_id_1 = "@chattestingl0_chat"
    chat_id_2 = "@chattestingl0_chat"
    text_message = "/fucksybil"

    await asyncio.gather(
        authorize_client(app1, phone_number1),
        authorize_client(app2, phone_number2),
        authorize_client(app3, phone_number3),
        join_chat(app1, "https://t.me/chattestingl0_chat"),  # ссылка на чат в который нужно спамить 
        join_chat(app2, "https://t.me/chattestingl0_chat"),
        join_chat(app3, "https://t.me/chattestingl0_chat")
    )

    await asyncio.gather(
        send_text_messages(app1, time_interval_1, chat_id_1, text_message),
        change_profile(app1),
        send_text_messages(app2, time_interval_2, chat_id_2, text_message),
        change_profile(app2),
        send_text_messages(app3, time_interval_3, chat_id_1, text_message),
        change_profile(app3)
    )

if __name__ == "__main__":
    app1.start()
    app2.start()
    app3.start()
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        logger.info("Завершение работы...")
    finally:
        app1.stop()
        app2.stop()
        app3.stop()
