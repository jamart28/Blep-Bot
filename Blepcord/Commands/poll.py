from . import emote

#command information
name = "Poll"
description = "Sends a message to act as a poll using reactions"
parameters = "Emote: (optional) emote to represent the option; Option: option being voted on; Title: title for the poll"
usage = '`:poll "This is a title" ":thumbsup:: Ye" ":thumbsdown:: Nah"`, `:poll "This is a title" "Ye" "Nah"`'

"""
ouput:
output[0]=destination (discord)
output[1]=message content ("")
output[2]=embed content ("", None)
output[3]=reactions ([])
"""

#main function that runs on command
#parameters: msg=discord.Message, args=string array
#returns: output=list representing the output for main to use (outlined above)
def run(msg, args):
    output = [msg.channel, "", "", []]
    output[1] = "**:bar_chart:" + args[0] + "**"
    args = emote.split_emotes(args[1:])
    i = 0
    while i < args[0].length:
        if args[1][i] is None:
            emot = next(args[2])
            output[2].append(emot+": "+args[0][i])
            output[3][i] = emot
        else:
            output[2].append(args[1][i]+": "+args[0][i])
            output[3][i] = args[1][i]
    return output
