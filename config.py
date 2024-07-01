from os import getenv

API_ID = int(getenv("API_ID", "22138812")) #optional
API_HASH = getenv("API_HASH", "83f6908fe0c90bf7a6586be34939a170") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7374966263").split()))
OWNER_ID = int(getenv("OWNER_ID", "1841914911"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/91c6683a0074d9dce03c1.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/mrxbroken011/Absir")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQFRz7wATSCTQLY6z-VoDJ1uDcknozTOCwblT2SQJoDF1pqAsNA6tmxkO_38NLsznwG-3rreV9KeZUc_SpjD4hlenanYELLRpeXZZbPNb9m9ajebWlZBxyBhtZJ0QEpYKpiP3q5Xr8FsascF_MVcxJgvHav1IS0Ju63G6qZ24oYWq5OsJeFK3uVOr4BXvp3sWU58msVXviTrTtTpxt3WpkCL4xMKD-0b6kdzVNHkuKzzDymAUr9ThhEr-q4Pm-YDuD3H052tc1GEwlf5e_wUqYeVwyZcyzjqg-1370esxJIF5OcwVz7uRV93GW3Mq2UG1b-YXWqL5iZHrSn4sS19-fnFT0X1lgAAAAGsybf5AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
