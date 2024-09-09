import vk_api

from parser import block, article_text

# Ваши данные для авторизации
token = 
group_id =   # ID вашего сообщества
# Авторизация и создание сессии
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

# Отправка сообщения на стену сообщества
def send_message_to_wall(text):
    vk.wall.post(owner_id=group_id, message=text)

# Пример вызова функции отправки сообщения
send_message_to_wall(article_text)
