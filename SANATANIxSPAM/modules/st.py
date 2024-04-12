import asyncio
from random import choice
from telethon import events
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from SANATANIxSPAM.data import ST, SACHIN


@X1.on(events.NewMessage(incoming=True, pattern=r"\%s4straid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%s4straid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%s4straid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%s4straid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%s4straid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%s4straid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%s4straid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%s4straid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%s4straid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%s4straid(?: |$)(.*)" % hl))
async def 4straid(e):
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
            if uid in SACHIN:
                await e.reply("➲ ᴛʜɪs ɪs [ 𝗠𝗥 𝗦𝗔𝗖𝗛𝗜𝗡 ][ 𝚂ʌŋᴀᴛᴎɩ ]\n▸ ᴛʜɪs ɪs ᴍʏ ᴏᴡɴᴇʀ ~ ᴍʏ ᴅᴇᴠᴇʟᴏᴘ\n▸ sᴀᴍᴊʜᴀ ʀᴀɴᴅɪ ᴋᴇ ᴘɪʟʟᴇ")
            elif uid == OWNER_ID:
                await e.reply("➲ ᴛʜɪs ɪs [ 𝗠𝗥 𝗦𝗔𝗖𝗛𝗜𝗡 ][ 𝚂ʌŋᴀᴛᴎɩ ]\n▸ ᴛʜɪs ɪs ᴍʏ ᴏᴡɴᴇʀ ~ ᴍʏ ᴅᴇᴠᴇʟᴏᴘ\n▸ sᴀᴍᴊʜᴀ ʀᴀɴᴅɪ ᴋᴇ ᴘɪʟʟᴇ")
            elif uid in SUDO_USERS:
                await e.reply("➲ sᴏʀʀʏ ᴛʜɪs ɪs sᴜᴅᴏ ᴜsᴇʀ \n➲ ʏᴇ ʙʜɪ ᴛᴇʀɪ ᴛᴀʀᴀʜ ʜɪ ʜᴀɪ \n➲ sᴀᴍᴊʜᴀ ʀᴇ ᴄʜᴏᴍᴜ ᴄʜᴜᴛɪʏᴇ")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(ST)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"{hl}4sᴛʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)
