import discord
import responses
import os
from dotenv import load_dotenv

async def send_message(message,  user_message,  is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        await message.author.send(message.author.mention) if is_private else await message.channel.send(message.author.mention)
    except Exception:
        err="Request could not be fulfilled, switching to simple setting."
        await message.author.send(message.author.mention) if is_private else await message.channel.send(message.author.mention)
        await message.author.send(err) if is_private else await message.channel.send(err)
        splitted = user_message.split("\n")
        user_message = user_message.replace(splitted[3], "simple")
        response = responses.handle_response(user_message)
        await message.author.send(message.author.mention) if is_private else await message.channel.send(message.author.mention)
        await message.author.send(response) if is_private else await message.channel.send(response)

def run_Discord_Bot():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    
    @client.event
    async def on_message(message):
        file = open("Log File", "a")
        if message.author == client.user:
            return
        username = str(message.author)
        user_Message = str(message.content)
        channel = str(message.channel)
        server = str(message.guild.name)
        file.write(username + " said: " + user_Message + "\nin channel: {" + channel + "} in server: {"  + server +"}\n")
        file.close()
        if message.channel.name.lower() == "bot-channel" or message.channel.name.lower() == "bot-lounge" or message.channel.name.lower() == "weapon-library":
            if user_Message[0] == '?':
                user_Message = user_Message[1:]
                await send_message(message,  user_Message,  is_private = True)
            else:
                await send_message(message,  user_Message,  is_private = False)
    client.run(TOKEN)
