from pyrogram import Client

from user_bot.handlers.forward import reg_forward
from user_bot.settings import settings

def handlers(client):
    reg_forward(client)
def main():
    client = Client(settings.user_bot.profile, settings.user_bot.api_id, settings.user_bot.api_hash)

    handlers(client)

    client.run()


if __name__ == '__main__':
    main()

