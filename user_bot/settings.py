from dataclasses import dataclass

from environs import Env


@dataclass
class UserBot:
    api_id: str
    api_hash: str
    profile: str
@dataclass
class Data:
    user_bot: str
    donor_ids: list[int]

@dataclass
class Group:
    group: str
    donor_ids: list[int]

@dataclass
class Group_finish:
    group_finish: int
    donor_id: int
@dataclass
class Settings:
    user_bot: UserBot
    data: Data
    group: Group
    group_finish: Group_finish
def get_settings(path: str):
    evn = Env()

    evn.read_env(path)

    return Settings(
        user_bot=UserBot(
            api_id=evn.str("API_ID"),
            api_hash=evn.str("API_HASH"),
            profile=evn.str("PROFILE")
        ),
        data=Data(
            user_bot=evn.int("BOT"),
            donor_ids=list(map(int, evn.list("DONOR_IDS")))
        ),
        group = Group(
            group=evn.int("GROUP"),
            donor_ids=list(map(int, evn.list("DONOR_IDS")))
    ),
        group_finish = Group_finish(
            group_finish=evn.int("GROUP"),
            donor_id=evn.int("BOT")
    )
    )

settings = get_settings(".input")


#def get_settings():  Можно так, можно по другому , а еще лучше подумать )))
    #env = Env()

    #env.read_env(".Input")  #Вызываем наши данные из файла input  этой лабудой про которую почитаемБ
