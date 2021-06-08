import logging

from bot import Thoth
from settings import CHANNEL_LOG, PREFIX, TOKEN


if __name__ == '__main__':
    # Add custom logger
    logger = logging.getLogger("discord")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(
        filename="discord.log", encoding="utf-8", mode="w",
    )
    handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"),
    )
    logger.addHandler(handler)

    # Create and run Discord client
    client = Thoth(PREFIX, CHANNEL_LOG)
    client.run(TOKEN)
