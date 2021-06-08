from discord.ext.commands import Bot


class Thoth(Bot):

    def __init__(self, prefix, *args, **kwargs):
        super().__init__(prefix, *args, **kwargs)

    async def on_ready(self):
        print(f"{self.user} is ready")
