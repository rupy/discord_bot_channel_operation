from lib.bot import MyBot
import os

TOKEN = os.environ['DISCORD_TOKEN']

bot = MyBot(command_prefix='!')
bot.run(TOKEN)
