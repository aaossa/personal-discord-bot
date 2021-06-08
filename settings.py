from environs import Env


# Initialize environs
env = Env()


# Prefix
PREFIX = "$"

# Private token
TOKEN = env("TOKEN")
