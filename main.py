import discord
from discord.ext.commands import Bot

client = Bot(description="Basic Bot by Habchy#1665", command_prefix="$", pm_help=False)




@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' + str(
        len(client.servers)) + ' servers | Connected to ' + str(len(set(client.get_all_members()))) + ' users')
    print('--------')
    print('Created by xKush')
    return await client.change_presence(
        game=discord.Game(name='Happy 420 | $help'))





@client.event
async def on_message(message):
    if message.content.startswith('$help'):
        await client.send_message(message.channel, ' :arrow_right: Thank you for using **Akito** :arrow_left: ')
        await client.send_message(message.channel, ' :red_circle:  **Commands** :red_circle: ')
        await client.send_message(message.channel, ' **- $website** = The Bot´s Website ')
        await client.send_message(message.channel, ' **- $info** = Infos about the Bot ')
    if message.content.startswith('$website'):
        await client.send_message(message.channel, ' :arrow_right: http://xkush.xyz/ ')
    if message.content.startswith('$info'):
        await client.send_message(message.channel, " ``` [Coded by xKush] ``` ")
        await client.send_message(message.channel, " ``` [Vers. 1.0.0 BETA] ``` ")








client.run("NDYxNTMwOTQzNTkzNjQ0MDMy.DhUptg.D6Ztk7p4XqExLm-6o3pSqIw69SU")
