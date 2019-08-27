from .. import sql

#command information
name = "Configure Admin Role"
description = "Configures a role to be the admin role for this bot"
parameters = "{role}: Role to be made the admin role"
usage = '`:Pconfig "{role}"`'

"""
ouput:
output[0]=destination
output[1]=message content
output[2]=embed content (if None ignored)
output[3]=reactions
"""

#configures a role to be the admin role for this bot
#parameters: msg=discord.Message, args=string array
#returns: output=list representing the output for main to use (outlined above)
def run(msg, args):
    if args[0] in msg.guild.roles:
        sql.change(str(msg.guild.id), admin=args[0])
        return [msg.channel, "The role "+args[0]+" has been successfully made the admin role for the bot.", None, []]
    else:
        return [msg.channel, "I wasn't able to find the role "+args[0]+" in the roles for this guild.", None, []]
