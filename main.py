import discord
import os
import random
from replit import db
TOKEN = os.environ['TOKEN']

client = discord.Client(intents=discord.Intents.all())

# functions to update list of posture words from Discord
def update_posture_words(posture_word):
  if "posture_words" in db.keys():
    posture_words = db["posture_words"]
    posture_words.append(posture_word)
    db["posture_words"] = posture_words
  else:
    db["posture_words"] = [posture_word]

def delete_posture_word(index):
  posture_words = db["posture_words"]
  if len(posture_words) > index:
    del posture_words[index]
    db['posture_words'] = posture_check
    

# list of words to for message check
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

  if msg.startswith("is cassy a furry?"):
    await channel.send('Yes 😔')
  
  if msg.startswith("is dong a furry?"):
    await channel.send('Hell nah he is a gigachad ezclap 😎')

  if msg.startswith("are you telling the truth?"):
    await channel.send('Of course I am. I only speak the truth, no kissy.')

  # sends posture messages

  if "posture_words" in db.keys():
    posture_words =+ db["posture_words"]
  
  if any(word in msg for word in posture_words):
    await channel.send(random.choice(posture_words))

  # database commands
  if msg.startswith("$new"):
    posture_word = msg.split("$new ", 1)[1]
    update_posture_words(posture_word)
    await channel.send("New posture word added.")

  if msg.startswith("$delete"):
    posture_words = []
    if "posture_words" in db.keys():
      index = int(msg.split("$delete ", 1)[1])
      delete_posture_word(index)
      posture_words = db["posture_words"]
    await channel.send(posture_words)

    
client.run(TOKEN)