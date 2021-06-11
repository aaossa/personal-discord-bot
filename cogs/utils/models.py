from peewee import DatabaseProxy, Model
from peewee import CharField, ForeignKeyField, TextField


database_proxy = DatabaseProxy()


class BaseModel(Model):
    class Meta:
        database = database_proxy


class Topic(BaseModel):
    name = CharField(unique=True)


class Link(BaseModel):
    topic = ForeignKeyField(Topic, backref='links')
    token = CharField(unique=True)
    url = TextField()
    description = TextField()


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

    # Create tables
    database.create_tables([Topic, Link])
    Link._schema.create_foreign_key(Link.topic)

    # Close connection
    database.close()
