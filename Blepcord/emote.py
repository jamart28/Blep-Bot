import emojis

#splits arguments with emotes into two lists
#parameters: args=string array
#returns: list of two lists with split arguments
def split_emotes(args):
    #lists to old emotes and new arguments
    emotes = []
    new_args = []
    #splitting arguments
    for arg in args:
        #if argument has a custom emote
        if arg.find(":") != -1:
            emotes.append(arg.split(":")[0].strip())
            new_args.append(arg.split(":")[1].strip())
        #otherwise default emote is used
        else:
            emotes.append(None)
            new_args.append(arg)
    return [new_args, emotes]
