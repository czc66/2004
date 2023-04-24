from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "7452578"))
API_HASH = getenv("API_HASH", "061d67ee8eed9368c5cadabb4aa21efc")
BOT_TOKEN = getenv("BOT_TOKEN", "6185409941:AAGW4Poxmhl1ng0CdZ0wIlMHuZ8Mxrnw8EM")
SESSION_NAME = getenv("SESSION_NAME", "AgCfh37E3OFJqJjFxuJKykAMj_K3fm_jWcDWYulUj9yMxJUgyC8noZr65G93qozCb8BJ6x0MNlIT8Vza3AES7ZD8J7P_2cBEjH1pgVUt-bYS_zfE6pPHTz1PtKdFdHZxcYZwDEo-tGc9rwsvKExaeRrhj-kjZ5Vz_MaZnRK69xJM0yBE6sjqRfKRlKN1v98AfNjUYsxTqBI94nplPSxs031NDc8Gs-UwpFlLqhFE3bnpQAfesDTW0CED-5Ww0klh6IfN0NwYdHJKjmcz01Wuzj6-0EiP9DrsUUSmzvQMSB3Vdpnqf1xPnXsfpriO1xrfsfQZiEyt51CyHVbj3aymHmR4AAAAAXMbv6kA--UwpFlLqhFE3bnpQAfesDTW0CED--AgCfh37E3OFJqJjFxuJKykAMj_K3fm_jWcDWYulUj9yMxJUgyC8noZr65G93qozCb8BJ6x0MNlIT8Vza3AES7ZD8J7P_2cBEjH1pgVUt-bYS_zfE6pPHTz1PtKdFdHZxcYZwDEo-tGc9rwsvKExaeRrhj-kjZ5Vz_MaZnRK69xJM0yBE6sjqRfKRlKN1v98AfNjUYsxTqBI94nplPSxs031NDc8Gs-UwpFlLqhFE3bnpQAfesDTW0CED-5Ww0klh6IfN0NwYdHJKjmcz01Wuzj6-0EiP9DrsUUSmzvQMSB3Vdpnqf1xPnXsfpriO1xrfsfQZiEyt51CyHVbj3aymHmR4AAAAAXMbv6kA
# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "@U_K_11")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "E_V_OBOT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "EVOMAFIA")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "EVOMAFIA")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
