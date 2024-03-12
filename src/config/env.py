from environs import Env

env = Env()
env.read_env()

OPENAI_API_KEY = env.str("OPENAI_API_KEY", "")
DATABASE_URI = env.str("DATABASE_URI", "")