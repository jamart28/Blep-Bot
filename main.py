import discord
from Blepcord.Commands import *
from Blepcord.Commands import Help
from Blepcord import *

#TODO: organize/figure out imports, check blep, write poll

#creating discord client object
client = discord.Client()
#boolean for whether to setup sql server or not
SQLbot = sql.sql("blep.db")

# TODO: add comments
@client.event
async def on_ready():
    global creator
    creator = client.get_user(int(tools.read_file("CREATOR_ID.txt")))
    print("I'm ready.")
    print(client.user)
    print(discord.version_info)
    print(discord.__version__)
    print(creator)

# TODO: add comments
@client.event
async def on_guild_join(guild):
    SQLbot.add(str(guild.id), str(guild.owner_id))
    await client.get_user(guild.owner_id).send(bot.welcomeMessage)

#event defintion for messages
@client.event
async def on_message(msg):
    global output
    #finishes commands on messages sent by bot
    if msg.author == client.user:
        #reacts with any emojis in output[3]
        for reaction in output[3]:
            msg.add_reaction(reaction)
        #finishes blep/ping command
        if msg.content.startswith(":P"):
            await msg.edit(content=":P ")
    else:
        #grabs guilds prefix and checks that message starts with it
        prefix = SQLbot.read(str(msg.guild.id), "command")
        if msg.content.startswith(prefix):
            #grabs command from msg and checks if it is valid
            command = tools.parse_command(msg.content, prefix)
            if command in cmd.commands:
                #runs command from commands dictionary in cmd.py
                output = cmd.commands[command].run(msg, tools.parse_args(msg.content))
                #sends output properly split between whether it has an embed or not
                if output[2] is None:
                    await output[0].send(output[1])
                else:
                    await output[0].send(output[1], embed=discord.Embed(description=output[2], color=bot.color))

@client.event
async def on_message_edit(msg, edited_msg):
    if msg.author == client.user:
        await cmd.blep.ping(edited_msg)


#sets up sql server (set sql_setup to false if this is not needed/wanted)
if False:
    SQLbot.setup()
    print("sql database setup")

#assigns token from read file
token = tools.read_file("BOT_TOKEN.txt")

#connecting client to discord
client.run(token)
