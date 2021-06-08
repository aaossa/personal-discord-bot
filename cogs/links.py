from discord.ext.commands import Cog, group


DESCRIPTION = "Management of my links and resources"


class Links(Cog, description=DESCRIPTION):

    def __init__(self, bot):
        self.bot = bot

    @group()
    async def links(self, ctx):
        """Administration of links"""
        pass

    @links.command(name="new")
    async def links_new(self, ctx, name):
        """Creates a new topic"""
        pass

    @links.command(name="add")
    async def links_add(self, ctx, topic_name, url, description):
        """Adds a new item to a topic"""
        pass

    @links.command(name="get")
    async def links_get(self, ctx, topic):
        """Retrieves the contents of a topic"""
        pass


def setup(bot):
    bot.add_cog(Links(bot))
