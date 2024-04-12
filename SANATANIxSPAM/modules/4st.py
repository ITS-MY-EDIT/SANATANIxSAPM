import asyncio
from random import choice
from telethon import events
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from SANATANIxSPAM.data import 4ST

@X1.on(events.NewMessage(incoming=True, pattern=r"\%s4st(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%s4st(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%s4st(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%s4st(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%s4st(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%s4st(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%s4st(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%s4st(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%s4st(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%s4st(?: |$)(.*)" % hl))
async def flirt(e):
     if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(FLIRT)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"{hl}4sᴛ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)
