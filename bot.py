from discord.ext.commands import Bot


class Thoth(Bot):

    def __init__(self, prefix, channel_log, database, extensions, *args, **kwargs):
        super().__init__(prefix, *args, **kwargs)
        self.channel_log = channel_log
        self.database = database
        for ext in extensions:
            self.load_extension(ext)

    async def on_ready(self):
        print(f"{self.user} is ready")
        await self.get_channel(self.channel_log).send(f"{self.user} is ready")
