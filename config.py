from os import getenv

API_ID = int(getenv("API_ID", "22138812")) #optional
API_HASH = getenv("API_HASH", "83f6908fe0c90bf7a6586be34939a170") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7374966263").split()))
OWNER_ID = int(getenv("OWNER_ID", "1841914911"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "7218597033:AAFKZwZN7FoUiSJtTvaBkEIrLfFz0XVZsjU")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/91c6683a0074d9dce03c1.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/mrxbroken011/Absir")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "1BVtsOJMBu6_RU5xtjzlHXLEvgBDlIn6B1dwcrih_0DzRE3QX8PxE9vpRLNpkORHr6n1cOdnJc1HIWlwWh9ut-grUioHTxH1K63iMZrc-AIHDhVN0XiuczgJUkJDTS2zuMHgAE5J3z2vdZNUhViDXB-zCEfVAe9v4zstqk7XUK0MO1jbPfiA9vFWtzcdcZ0Ze3M5hqSvN2ebLWDc3jKwnfXtHS2zbX440BjAh81Zs_HQ4Hmn__r7JdICP1xE1iMfmW2E7tilEBQmH2jxgQ7aiGwJoxuv_4UjXxYsgG8CkVbSuNCWvqkIzoKnFDyXia_5Nhrnca-7gYx_I4HBdUEfHCv2JN8wDbsc=")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
