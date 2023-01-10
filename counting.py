import discord
import re
from token import TOKEN

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        #print(f'Message from {message.author}: {message.content}')
        if(message.channel.id == 906011935210897413):
            #print('in counting')
            if(not message.content.isdigit()):
                #print("not int")
                await message.delete()
            else:
                messages = [m async for m in message.channel.history(limit=2)]
                if(messages[1].author == message.author):
                    await message.delete()
                    #print("numbers are not correct")
                else:
                    if(int(messages[1].content) != int(message.content) - 1):
                        await message.delete()
                        #print("same author")
           

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)