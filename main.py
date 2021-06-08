import logging
from urllib.parse import urlparse

from peewee import PostgresqlDatabase

from bot import Thoth
from models import database_proxy
from settings import CHANNEL_LOG, DATABASE_URL, PREFIX, TOKEN


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

    # Connection to database
    # (https://github.com/coleifer/peewee/issues/796#issuecomment-385223811)
    url = urlparse(DATABASE_URL)
    database = PostgresqlDatabase(
        database=url.path[1:],
        user=url.username, password=url.password,
        host=url.hostname, port=url.port,
    )
    database_proxy.initialize(database)

    # Create and run Discord client
    client = Thoth(PREFIX, CHANNEL_LOG, database)
    client.run(TOKEN)
