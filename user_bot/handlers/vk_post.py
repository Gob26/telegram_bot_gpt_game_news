import vk_api

from parser import block, article_text

# Ваши данные для авторизации
token = "vk1.a.OeOsJLeLGOID-62zYd2AwECxxXvNERI1qZcGAxAB1rXTWTHji_L5dZKWxeWPEq4TO9nnRCZJi_D1y70L22jcaJmPI0ve-8dvHj1fpkC6As5lFXT9gX3JwUYNrnUyNeCf9U7f5ysnBV246dW_w6V-_jyM0HFMG5Moc4ZJ5hzvVK_RqCcMuUtIEV42TnufD2nJnje2tEoMNbvCLmf0I5Kshw"
group_id = -202423059  # ID вашего сообщества
# Авторизация и создание сессии
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

# Отправка сообщения на стену сообщества
def send_message_to_wall(text):
    vk.wall.post(owner_id=group_id, message=text)

# Пример вызова функции отправки сообщения
send_message_to_wall(article_text)