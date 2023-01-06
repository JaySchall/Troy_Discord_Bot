import discord
import BotResponses
count = 0
frequency = 120
async def send_message(message, user_message, is_command):
    if is_command == True:
        return
    try:
        response = BotResponses.get_message(user_message)
        if response is None or 1048825632324341831 in list(role.id for role in message.author.roles):
            return
        for role in message.author.roles:
            print(role.id)

        
        await message.reply(response)
    except Exception as e:
        print(e)

def run_bot():
    TOKEN = "insert token"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print("up and running!")

    @client.event
    async def on_message(message):
        global count
        global frequency
        if message.author == client.user:
            return
        channel = client.get_channel(1048679248241631374)
        if message.channel == channel:
            count+=1
        username = str(message.author)
        usermsg = str(message.content)
        dono_channel = client.get_channel(1051326081078132857)
        advert_message = f"""Hey guys if you’re waiting in line or using the system you should also throw it up on twitch\n
https://m.twitch.tv/sensden/home\n
Watching on twitch helps promote the server and keep this system alive!\n
It’s also good if the bot DCs from discord never miss a chance for Herba\n
Also, if you're looking for other ways to support the server, check out {dono_channel.mention} to learn more!
        """
        
        #if usermsg[0] == '?':
        #    usermsg = usermsg[1:]
        #    await send_message(message, usermsg, True) 

        #else:
        await send_message(message, usermsg, False)
        if(count >= frequency):
            count = 0
            await channel.send(advert_message)

    client.run(TOKEN)