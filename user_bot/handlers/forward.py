import re

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

from pyrogram.types import Message

from user_bot.handlers.vk_post import send_message_to_wall
from user_bot.settings import settings

import requests
from bs4 import BeautifulSoup
import vk_api
import re
async def forward_media_group(client: Client,message: Message):  #объединение картинок в группу
    await client.copy_media_group(settings.settings.group.group, message.chat.id, message.message_ids)


async def forward(client: Client, message: Message):
    if message.photo:
        photo_id = message.photo.file_id
        await client.send_photo(chat_id=settings.group.group, photo=photo_id)

    if message.video:
        video_id = message.video.file_id
        await client.send_video(chat_id=settings.group.group, video=video_id)

    try:
        if message.text and re.search(r"https?://www\.igromania\.ru/[\w/-]+", message.text):
            link = re.search(r"(https?://www\.igromania\.ru/[\w/-]+)", message.text)
            if link:
                url = link.group()
                m = url.split("/")[-3]
                response = requests.get(url).text
                soup = BeautifulSoup(response, 'lxml')
                block = soup.find("div", class_=f"material-content_{m}").get_text(strip=True)


                text_message = (
                                   "Ты редактор популярного портала о компьютерных играх PlayBux. "
                                   "Перепиши статью и сделай ее уникальной. "
                                   "Добавь информацию от себя, напиши заголовок, короткое описание и добавь emojis там, где посчитаешь нужным, "
                                   "а также ссылку на наш сайт playbux.ru. "
                                   "Найди три часто повторяющихся слова и преврати их в хэштеги в конце статьи. "
                                   "(Отвечай только на русском языке и не задавай вопросы в ответе. Если у тебя есть дополнительные вопросы, не стесняйся задавать их.)  \n\n"
                               ) + block

                # Отправка сообщения с извлеченным текстом
                await client.send_message(chat_id=settings.data.user_bot, text=text_message)

        if message.text and re.search(r'(https?://ixbt\.games/[\w/-]+)      ', message.text):
            link = re.search(r"(r'(https?://ixbt\.games/[\w/-]+)', text)", message.text)
            if link:
                url = link.group()
                response = requests.get(url).text
                soup = BeautifulSoup(response, 'lxml')
                block = soup.find("article", class_=f"publication-container").get_text(strip=True)


                text_message = (
                                   "Ты редактор популярного портала о компьютерных играх PlayBux. "
                                   "Перепиши статью и сделай ее уникальной. "
                                   "Добавь информацию от себя, напиши заголовок, короткое описание и добавь emojis там, где посчитаешь нужным, "
                                   "а также ссылку на наш сайт playbux.ru. "
                                   "Найди три часто повторяющихся слова и преврати их в хэштеги в конце статьи. "
                                   "(Отвечай только на русском языке и не задавай вопросы в ответе. Если у тебя есть дополнительные вопросы, не стесняйся задавать их.)  \n\n"
                               ) + block

                # Отправка сообщения с извлеченным текстом
                await client.send_message(chat_id=settings.data.user_bot, text=text_message)
                print(block)
    except Exception as e:

        print(f"Ошибка:{e}")

    if message.caption:
        text_message = (
                           "Ты редатор популярного портала PlayBux  о компьютерных играх. "  # добавляем к тексту нужное и отправляем боту на редакцию

                           "Перепиши статью и сделай уникальной. Старую версию не присылай "

                           "Добавь информацию от себя,напиши заголовок, короткое описание и добавь emojis где посчитаешь нужным и ссылку playbux.ru. "

                           "(Пиши только на русском языке и не пиши в ответе Если у вас есть еще вопросы)  \n\n") + message.caption

        await client.send_message(chat_id=settings.data.user_bot, text=text_message)

async def forward_finish(client: Client, message: Message):      #отправляем из БОТа обработанный текст в финальную группу
    forwarded_message = await message.copy(chat_id=settings.group_finish.group_finish)
      
    modified_message = forwarded_message.text



# Пример вызова функции отправки сообщения
    send_message_to_wall(modified_message)  



def reg_forward(client: Client):  # Вызов регистрация хендлера хендлера
    #client.add_handler(MessageHandler(forward_media_group, filters.chat(chats=settings.group.donor_ids) & filters.media_group))#медиагрупп
    client.add_handler(MessageHandler(forward, filters.chat(chats=settings.data.donor_ids)))
    client.add_handler(MessageHandler(forward_finish, filters.chat(chats=settings.group_finish.donor_id)))
