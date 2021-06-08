from environs import Env


# Initialize environs
env = Env()


# Prefix
PREFIX = "$"

# Private token
TOKEN = env("TOKEN")

# Important channels
CHANNEL_LOG = env.int("CHANNEL_LOG")
