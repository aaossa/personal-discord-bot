from discord.ext.commands import Cog, group


DESCRIPTION = "Management of my links and resources"


class Links(Cog, description=DESCRIPTION):

    def __init__(self, bot):
        self.bot = bot

    @group()
    async def topics(self, ctx):
        """Administration of link topics"""
        pass

    @topics.command(name="index", aliases=["list"])
    async def topics_index(self, ctx):
        """List all the topics"""
        pass

    @topics.command(name="get")
    async def topics_get(self, ctx, name):
        """Retrieves the contents of a topic"""
        pass

    @topics.command(name="update", aliases=["edit"])
    async def topics_update(self, ctx, old_name, new_name):
        """Updates a topic name"""
        pass

    @topics.command(name="remove", aliases=["rm"])
    async def topics_remove(self, ctx, topic):
        """Remove a topic and its contents"""
        pass

    @topics.command(name="new", aliases=["add"])
    async def topics_new(self, ctx, name):
        """Creates a new topic"""
        pass

    @group()
    async def links(self, ctx):
        """Administration of links"""
        pass

    @links.command(name="get")
    async def links_get(self, ctx, token):
        """Retrieves the information of a link"""
        pass

    @links.command(name="remove", aliases=["rm"])
    async def links_remove(self, ctx, token):
        """Remove a link and its information"""
        pass

    @links.command(name="new", aliases=["add"])
    async def links_new(self, ctx, topic, url, description):
        """Adds a new link to a topic"""
        pass


def setup(bot):
    bot.add_cog(Links(bot))
