from environs import Env


# Initialize environs
env = Env()


# Prefix
PREFIX = "$"

# Private token
TOKEN = env("TOKEN")

# Database
DATABASE_URL = env("DATABASE_URL")

# Important channels
CHANNEL_LOG = env.int("CHANNEL_LOG")
