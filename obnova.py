from telethon import TelegramClient, events
from random import choice as ch
from asyncio import sleep as sl
from datetime import datetime

shabl = ["jack"]
state = True
state1 = True
start = datetime.now()
time = 300
ph = ""
shapka = ""
media_file = ""
admin_id = "5107567767"

class PydroidBot:
    def __init__(self):
        self.api_id = 26736366
        self.api_hash = "10a653547ac17ab466a92238755ffcec"
        self.client = TelegramClient('U11A', self.api_id, self.api_hash)
        self.client.start()

    def run(self):
        @self.client.on(events.NewMessage(pattern=r'\/tterror'))
        async def command_fast(event):
            user_id = event.message.sender_id
            if str(user_id) == admin_id:
                txt = event.message.message.split(maxsplit=1)[1]
                chat_id = int(txt)
                global state
                state = True
                while state:
                    text = ch(shabl)
                    await self.client.send_message(chat_id, shapka+text)
                    await sl(int(time))
        
        

        @self.client.on(events.NewMessage(pattern='/ttime'))
        async def command_set_time(event):
            if str(event.message.sender_id) == admin_id:
                text = event.message.message.split(maxsplit=1)[1]
                global time
                time = int(text)
                await event.respond("<b>Выполнено!</b>", parse_mode='html')

        

        

        

        @self.client.on(events.NewMessage(pattern='/sstop'))
        async def command_stop(event):
            global state, state1
            stop_number = event.message.message.split(maxsplit=1)[1]
            if str(event.message.sender_id) == admin_id:
                if stop_number == "1":
                    state = False
                    await event.respond("<b>Выполнено!</b>", parse_mode='html')
                if stop_number == "2":
                    state1 = False
                    await event.respond("<b>ᤋуᥰᥙнᥱн᧐</b>", parse_mode='html')

        


        @self.client.on(events.NewMessage(pattern='/iid'))

        async def command_help_commands(event):

            if str(event.message.sender_id) == admin_id:
                ph = 'https://x0.at/rUB5.mp4'
                chat_id = event.chat_id
                me = await self.client.get_me()
                await self.client.send_file(chat_id, ph, caption='† chat id:  <code>{}</code>'.format(chat_id), parse_mode='html')

    def start(self):
        self.client.run_until_disconnected()

if __name__ == "__main__":
    start_class = PydroidBot()
    start_class.run()
    start_class.start()