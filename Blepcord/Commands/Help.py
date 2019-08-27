from . import *
from ..AdminCommands import *
from ..cmd import commands, adminCMD

#command information
name = "Help"
description = "Sends this message to the user"
parameters = "us: (optional) sends message to channel instead of user"
usage = '`:Phelp`, `:Phelp "us"`'

"""
ouput:
output[0]=destination
output[1]=message content
output[2]=embed content (if None ignored)
output[3]=reactions
"""

#constructing help message
help_msg = 'Below are all the commands implemented by this bot and their uses. Remember to replace ":P" with your prefix if you changed it.\n\n'
for command in commands.values():
    help_msg += "Name: "+command.name+"\nDescription: "+command.description+"\nParameters: "+command.parameters+"\nUsage: "+command.usage+"\n\n"
#adding admin commands
help_msg += "The following are admin commands and can only be used by a user who has the configured admin role, a role with the Administrator permission, or is the server owner."
for command in adminCMD.values():
    help_msg += "Name: "+command.name+"\nDescription: "+command.description+"\nParameters: "+command.parameters+"\nUsage: "+command.usage+"\n\n"

#returns output for help message for bot
#parameters: msg=discord.Message, args=string array
#returns: output=list representing the output for main to use (outlined above)
def run(msg, args):
    if args[0].lower() == 'us':
        return [msg.channel, "", help_msg, []]
    else:
        return [msg.author, "", help_msg, []]
