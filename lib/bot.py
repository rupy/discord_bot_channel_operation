import discord
from discord.ext import commands
from lib.cogs.cog import ChannelOperationCog

class MyBot(commands.Bot):

    async def on_ready(self):
        print('[[@Ready]]')
        print('Bot User Name:', self.user.name)
        print('Bot User ID:', self.user.id)
        self.__setup_cogs()

    def __setup_cogs(self):
        self.add_cog(ChannelOperationCog())