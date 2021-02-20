#Set-Up Libraries
import os
import json
import Functions
import discord as Discord

#Set-Up Config
Config = json.load(open("C:/Repos/Discord/PyBun/Settings/Config.json"))

#Set-Up PyBun
class Client(Discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Commands = {}
        self.Aliases = {}
        Functions.CommandHandler(self)

    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        await Functions.UseCommand(self, message)

#Log PyBun In
PyBun = Client()
PyBun.run(Config["Token"])