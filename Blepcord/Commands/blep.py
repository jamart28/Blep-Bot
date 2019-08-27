#command information
name = "BLEP (ping)"
description = "Tests bot's ping to server"
parameters = "None"
usage = '`:Pblep`'

#starts ping command by sending message
#parameters: msg=discord.Message, args=string array
def run(msg, args):
    return [msg.channel, ":P", None, []]

#finishes ping command by editing message and outputing time difference
#parameters: msg=discord.Message now=datetime
async def ping(msg, now):
    if now.second-msg.created_at.second != 0:
        ping_time = (1000000 - msg.created_at.microsecond) + now.microsecond
    else:
        ping_time = now.microsecond - msg.created_at.microsecond
    ping_time = int(ping_time/1000)
    await msg.edit(content=":P `{} ms`".format(ping_time))
