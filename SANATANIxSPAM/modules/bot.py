import sys
import heroku3

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from config import SUDO_USERS
from os import execl, getenv
from telethon import events
from datetime import datetime


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        jarvis = await e.reply(f"» ™°𝗦 𝗔 𝗡 𝗔 𝗧 𝗔 𝗡 𝗜")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await jarvis.edit(f"**╭────────────────⦿**\n**│➲ 𝗦𝗔𝗡𝗔𝗧𝗔𝗡𝗜 𝗜𝗦 𝗛𝗘𝗥𝗘 **\n**├────────────────⦿**\n**│➲ 𝗣𝗜𝗡𝗚 ▸** `{mp} ms`\n**╰────────────────⦿**")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"**╭─────────────────⦿** \n**│➲ ʀᴇʙᴏᴏᴛ ᴅᴏɴᴇ ~ ʙᴏss** \n**├─────────────────⦿** \n**│➲ 2 ᴍɪɴᴛ ᴡᴀɪᴛ ᴘʟᴇᴀsᴇ** \n**├─────────────────⦿** \n**│➲ ғɪʀ ᴀᴜɴɢᴀ ɪsᴋɪ ᴍᴀ ᴄʜᴏᴅɴᴇ** \n**╰─────────────────⦿**")
        try:
            await X1.disconnect()
        except Exception:
            pass
        try:
            await X2.disconnect()
        except Exception:
            pass
        try:
            await X3.disconnect()
        except Exception:
            pass
        try:
            await X4.disconnect()
        except Exception:
            pass
        try:
            await X5.disconnect()
        except Exception:
            pass
        try:
            await X6.disconnect()
        except Exception:
            pass
        try:
            await X7.disconnect()
        except Exception:
            pass
        try:
            await X8.disconnect()
        except Exception:
            pass
        try:
            await X9.disconnect()
        except Exception:
            pass
        try:
            await X10.disconnect()
        except Exception:
            pass

        execl(sys.executable, sys.executable, *sys.argv)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply(f"**⦿ ᴀᴅᴅɪɴɢ ᴜsᴇʀ ᴀs sᴀɴᴀᴛᴀɴɪ sᴜᴅᴏ ⦿**")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("**⦿ ʀᴇᴘʟʏ ᴛᴏ 𝙰 ᴜsᴇʀ ⦿**")
            return

        if str(target) in sudousers:
            await ok.edit("**⦿ ᴛʜɪs ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀ sᴜᴅᴏ ᴜsᴇʀ ᴏғ sᴀɴᴀᴛᴀɴɪ ʙᴏᴛs ⦿**")
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit(f"**: ⧽ ᴏʏᴇ ʜᴏʏᴇ ᴍᴇʀᴀ ᴄᴜᴛᴇ ʙᴀᴄʜʜᴀ** \n**: ⧽ ɴᴇᴡ ᴜsᴇʀ ɪᴅ :** `{target}`\n**: ⧽ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ sᴀɴᴀᴛᴀɴɪ sᴘᴀᴍ**")
            heroku_var["SUDO_USERS"] = newsudo    
    
    elif event.sender_id in SUDO_USERS:
        await event.reply("⦿ sᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴇss ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ⦿")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%srmsudo(?: |$)(.*)" % hl))
async def removesudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)
        ok = await event.reply(f"**⦿ ʀᴇᴍᴏᴠɪɴɢ sᴜᴅᴏ ᴜsᴇʀ ɪɴ sᴀɴᴀᴛᴀɴɪ sᴜᴅᴏ ʟɪsᴛs ⦿**")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:\nPlease set up your HEROKU_APP_NAME`")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("**⦿ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ⦿**")
            return
        if str(target) not in sudousers:
            await ok.edit(f"**⦿ sᴀɴᴀᴛᴀɴɪ sᴜᴅᴏ ᴜsᴇʀ ʀᴇᴍᴏᴠᴇᴅ** \n\n** ️⦿ sᴜᴅᴏ ᴜsᴇʀs :** `{newsudo}` ⦿️")
        else:
            new_sudo_users = " ".join([user for user in sudousers.split() if user != str(target)])
            await ok.edit(f"Removed sudo user: `{target}`")
            heroku_var["SUDO_USERS"] = new_sudo_users
    else:
        await event.reply("**⦿ sᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ  ᴄᴀɴ ʀᴇᴍᴏᴠᴇ sᴜᴅᴏ ⦿**")

@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudolist(?: |$)(.*)" % hl))
async def show_sudo_users(event):
    if event.sender_id == OWNER_ID:
        sudo_users_list = "✦ 𝗦𝗔𝗡𝗔𝗧𝗔𝗡𝗜 𝗖𝗨𝗥𝗥𝗘𝗡𝗧 𝗦𝗨𝗗𝗢 𝗨𝗦𝗘𝗥𝗦 𝗟𝗜𝗦𝗧 ✦\n"
        for user_id in SUDO_USERS:
            sudo_users_list += f"- {user_id}\n"
        await event.reply(sudo_users_list)
    else:
        await event.reply("🇴𝗡𝗟𝗬 𝗙𝗢𝗥 𝗦𝗔𝗖𝗛𝗜𝗡 𝗢𝗪𝗡𝗘𝗥.")
