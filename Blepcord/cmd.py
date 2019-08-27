from .Commands import *
from .AdminCommands import *
from .Commands import Help

#dictionary to run commands from messages
commands = {
"help" : Help,
"blep" : blep
}

adminCMD = {
"config" : Config,
"role" : roleAdder
}
