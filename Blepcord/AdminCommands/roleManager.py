import emote

#command information
name = "Role Manager"
description = "Sets up roles to be addable by all users"
parameters = "{func}: new-sets up a new role manager message; add-adds a role to the existing role manager; "
usage = '`:Pconfig "{role}"`'

# TODO: add role manager class, finish run function

#role manager class
class roleManager:
    #creates roleManager object
    def __init__(self, roles, emotes):
        #default emotes
        self.emoji = iter('🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯 🇰 🇱 🇲 🇳 🇴 🇵 🇶 🇷 🇸 🇹 🇺 🇻 🇼 🇽 🇾 🇿'.split())
        self.guild = guild
        self.roles = role
        self.emotes = emotes
        self.message = None

    #sets message
    def setMessage(self, msg):
        self.message = msg

    def add(self, role, emote=next(self.emoji)):
        self.roles.append(role)
        self.emotes.append(emote)
        self.msg.embeds[0].description = self.output(self.msg)[3]

    #constructs output
    def output(self, msg):
        msg = "React with the following emoji to have the role added to you.\n"
        for role, emote in self.roles, self.emotes:
            msg += emote+": "+role+"\n"
        msg += "\n Removing your reaction will remove the role from you."
        return [msg.channel, "", msg, self.emotes]

#servers with role managers:
role_managers = {}

async def run(msg, args):
    if str(msg.guild.id) in role_managers:
