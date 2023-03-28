from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()
BOT_TOKEN = env.str("BOT_TOKEN")
HTTP_PROXY = env.str("HTTP_PROXY")
FIRST_FILE = env.str("FIRST_FILE")
SECOND_FILE = env.str("SECOND_FILE")