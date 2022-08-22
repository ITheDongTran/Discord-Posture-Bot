import discord

TOKEN = 'MTAxMTE0NDA4NDM1NTgwOTI5Mg.GS4Quv.XPKTBiwWBdeV5t70ZMg6N3zcIuUSjNlzqjAPTA'

client = discord.Client(intents=discord.Intents.default())

# when bot is ready sends message 
@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

# # runs when bot receives message 
# @client.event
# async def on_message(message):
#   if message.author == client.user:
#     return

#   if message.content.startswith('$hello'):
#     await message.channel.send('Hello!')

# client.run(TOKEN)