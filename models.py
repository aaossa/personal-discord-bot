from peewee import DatabaseProxy, Model


database_proxy = DatabaseProxy()


class BaseModel(Model):
    class Meta:
        database = database_proxy


if __name__ == '__main__':
    from urllib.parse import urlparse

    from environs import Env
    from peewee import PostgresqlDatabase

    env = Env()

    # Connection to database
    # (https://github.com/coleifer/peewee/issues/796#issuecomment-385223811)
    url = urlparse(env("DATABASE_URL"))
    database = PostgresqlDatabase(
        database=url.path[1:],
        user=url.username, password=url.password,
        host=url.hostname, port=url.port,
    )
    database_proxy.initialize(database)

    # Close connection
    database.close()
