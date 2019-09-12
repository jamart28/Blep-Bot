#shortcut for reading a file that looks better
#parameters: file=string
#returns: string
def read_file(file):
    with open(file) as r_file:
        return r_file.read().rstrip()

#parses msg into command read by bot
#parameters: msg=string, prefix=string
#returns: string
def parse_command(msg, prefix):
    msg = msg[len(prefix):]
    msg = msg.split('"')
    return msg[0].strip().lower()

#parses msg into arguments read by bot
#parameters: msg=string
#returns: string array
def parse_args(msg):
    args = msg.split('"')
    print(args)
    del args[-1]
    i = 0
    while i < len(args)-1:
        print(args)
        del args[i]
        args[i] = args[i].strip()
        i+=1
    return args
