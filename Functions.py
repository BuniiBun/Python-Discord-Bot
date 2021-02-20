#Set-Up Libraries
from os import listdir
import importlib
import importlib.resources
import json

#Set-Up Config
Config = json.load(open("C:/Repos/Discord/PyBun/Settings/Config.json"))

async def UseCommand(Bot, Message):
    #Check If Command
    if Message.content.strip().split(" ")[0].startswith("<@!776508280239161345>"):
        Args = Message.content[22:len(Message.content)].strip().split(" ")
    elif Message.content.split(" ")[0].lower().startswith(Config["Prefix"]):
        Args = Message.content[len(Config["Prefix"]):len(Message.content)].strip().split(" ")
    else:
        return

    #Clean Command
    Command = Bot.Commands[Args[0].lower()]
    if not Command:
        Command = Bot.Aliases[Args[0].lower()]
    await Command.Run(Message)

def CommandHandler(Client):
    #Iterate Through Command Categories
    for Category in listdir("C:\Repos\Discord\PyBun\Commands"):
        #Build Commands List For That Category
        Commands = []
        for File in listdir(f"C:\Repos\Discord\PyBun\Commands\{Category}"):
            if File.endswith(".py") and not File.startswith("__init__"):
                Commands.append(File)

        #Set-Up Each Command
        for File in Commands:
            Module = importlib.import_module(f"Commands.{Category}.{File[:-3]}")
            Command = Module.Command()
            Client.Commands[f"{Command.Name.lower()}"] = Command