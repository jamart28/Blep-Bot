import discord

#color object that holds the bot's color to be sed with embeds
color = discord.Color.blurple()

#welcome message to welcome user who just added bot to their server
welcomeMessage = "HI!\nThanks for choosing me to be apart of your server. You may send :Phelp in any channel I am able to see to get a list of available commands. As the guild owner you have a few commands available to you, such as the command to change the prefix for all the commands which defaults as `:P`. Lastly, be sure to join the support server to get information on my updates and outages when they happen: https://discord.gg/F8R6GuN. Hope you enjoy having me!"

#invite link to add bot to a server (will be moved to a function later) TODO
inviteLink = "https://discordapp.com/api/oauth2/authorize?client_id=532982557810360330&permissions=1342262480&scope=bot"
#sends a reactable poll with custom emojis
#parameters: msg=discord.Message, args=string array
