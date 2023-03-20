import discord
import responses

async def send_message(message,  user_message,  is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
        
def run_Discord_Bot():
    TOKEN = "dummy"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_Message = str(message.content)
        channel = str(message.channel)
        
        print(f'{username} said: "{user_Message}" ({channel})')
        
        if user_Message[0] == '?':
            user_Message = user_Message[1:]
            await send_message(message,  user_Message,  is_private = True)
        else:
            await send_message(message,  user_Message,  is_private = False)
        
    client.run(TOKEN)
