class Command:
    def __init__(self):
        self.Name = "Ping"

    async def Run(self, Message):
        await Message.channel.send("Pong!")