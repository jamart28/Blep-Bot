#command information
name = "Insert name"
description = "Insert description"
parameters = "Insert parameters"
usage = "Insert usage"

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
    output = [msg., "", "", []]
    return output
