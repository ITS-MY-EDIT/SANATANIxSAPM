from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("• ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")
    ],
    [
        Button.url("• ᴜᴅᴀᴛᴇs •", "https://t.me/ALL_SANATANI_BOT"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/Il_4ST_FIGHTER_lI")
    ],
    [
        Button.url("• sᴀᴄʜɪɴ •", "https://t.me/V_VIP_OWNER"),
        Button.url("• ʀᴇᴘᴏ •", "https://t.me/Il_4ST_FIGHTER_lI")
    ],
    [
        Button.url("• ᴊᴏɪɴ ғᴏʀ sᴜᴅᴏ •", "https://t.me/Il_4ST_FIGHTER_lI")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n❍ 𝗛𝗘𝗬 ‣ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n❍ 𝗜 𝗔𝗠 ‣ [{bot_name}](tg://user?id={bot_id})**\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n● ɪ ᴀᴍ ᴠᴇʀʏ ᴘᴏᴡᴇʀғᴜʟ sᴘᴀᴍ ʙᴏᴛ ●\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n⊚ ᴜɴʟɪᴍɪᴛᴇᴅ ʀᴀɪᴅ\n⊚ ᴜɴʟɪᴍɪᴛᴇᴅ sᴘᴀᴍ \n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•\n⦿ 24x7 ʀᴜɴ | @Il_4ST_FIGHTER_lI\n•┈┈─┈┈─┈┈─┈┈─┈┈─┈┈─┈┈•**"
        await event.client.send_file(
            event.chat_id,
            "https://telegra.ph/file/fed3cd92e379575550a88.jpg",
            caption=TEXT,
            buttons=START_BUTTON
        )
