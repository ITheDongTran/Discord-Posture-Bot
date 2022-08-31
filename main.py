import discord
import os
import random
TOKEN = os.environ['TOKEN']

client = discord.Client(intents=discord.Intents.all())

posture_words = ['sit', 'chair', 'stand', 'desk', 'posture', 'stretch', 'break', 'tired']

posture_check = ["Posture Check!", "Check Your Posture!", "Everyone Sit Up!", "Stand up for a bit?"]

# when bot is ready sends message 
@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

# runs when bot receives message
@client.event
async def on_message(message):
  channel = message.channel
  msg = message.content

  if msg.startswith("$hello"):
    await channel.send(f'Hello {message.author}!')

  elif msg.startswith("is cassy a furry?"):
    await channel.send('Yes 😔')
  
  elif msg.startswith("is dong a furry?"):
    await channel.send('Hell nah he is a gigachad ezclap 😎')

  elif msg.startswith("are you telling the truth?"):
    await channel.send('Of course I am. I only speak the truth, no kissy.')

  if any(word in msg for word in posture_words):
    await channel.send(random.choice(posture_check))

client.run(TOKEN)