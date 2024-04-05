from telethon import events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"★ 𝗦𝗔𝗡𝗔𝗧𝗔𝗡𝗜 𝗕𝗢𝗧 𝗛𝗘𝗟𝗣 𝗠𝗘𝗡𝗨 ★\n\n» **ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ**\n» **ᴅᴇᴠᴇʟᴏᴘᴇʀ: @V_VIP_OWNER**"

HELP_BUTTON = [
    [
      Button.inline("• sᴘᴀᴍ •", data="spam"),
      Button.inline("• ʀᴀɪᴅ •", data="raid")
    ],
    [
      Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="extra")
    ],
    [
      Button.url("• sᴀᴄʜɪɴ •", "https://t.me/V_VIP_OWNER"),
      Button.url("• ʀᴇᴘᴏ •", "https://t.me/Il_4ST_FIGHTER_lI")
    ],
    [   
      Button.inline("• ɴᴇᴡ •", data="yash")
    ]
]


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://telegra.ph/file/fed3cd92e379575550a88.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"An Exception Occured!\n\n**ERROR:** {str(e)}")


extra_msg = f"""
**⦿ 𝗘𝗫𝗧𝗥𝗔 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 ⦿**

⦿ 𝗨𝗦𝗘𝗥-𝗕𝗢𝗧 : **ᴜsᴇʀʙᴏᴛ ᴄᴍᴅs**
  1) {hl}ᴘɪɴɢ
  2) {hl}ʀᴇʙᴏᴏᴛ
  3) {hl}sᴜᴅᴏ <ʀᴇᴘʟʏ ᴛɪ ᴜsᴇʀ>  --> Owner Cmd
  4) {hl}ʟᴏɢs --> Owner Cmd

⦿ 𝗘𝗖𝗛𝗢 : **ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜsᴇʀ**
  1) {hl}ᴇᴄʜᴏ <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>
  2) {hl}ʀᴍᴇᴄʜᴏ <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>

⦿ 𝗟𝗘𝗔𝗩𝗘 : **ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ**
  1) {hl}ʟᴇᴀᴠᴇ <ɢʀᴏᴜᴘ/ᴄʜᴀᴛ ɪᴅ>
  2) {hl}ʟᴇᴀᴠᴇ : ᴛʏᴘᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ʙᴏᴛ ᴡᴇʟʟ ᴀᴏᴜᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ


**© @V_VIP_OWNER**
"""



yash_msg = f"""
**⦿ 𝗡𝗘𝗪 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 ⦿**

⦿ 𝗚𝗢𝗢𝗗 𝗔𝗙𝗧𝗘𝗥𝗡𝗢𝗢𝗡 : **ᴀғᴛᴇʀ ɴᴏᴏɴ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsᴇʀ ғᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ**
  1) {hl}𝚐𝚊 <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}𝚐𝚊 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

⦿ 𝗘𝗠𝗢𝗝𝗜 : **ᴇᴍᴏᴊɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}𝚎𝚖𝚘𝚓𝚒 <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>
  2) {hl}𝚎𝚖𝚘𝚓𝚒 <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>

⦿ 𝗚𝗢𝗢𝗗 𝗠𝗢𝗥𝗡𝗜𝗡𝗚 : **ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  2) {hl}𝚐𝚖 <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  1) {hl}𝚐𝚖 <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>

⦿ 𝗚𝗢𝗢𝗗 𝗡𝗜𝗚𝗛𝗧 : **ᴏᴅ ɴɪɢʜᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ️‍**
  1) {hl}𝚐𝚗 <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}𝚐𝚗 <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>

⦿ 𝗦𝗛𝗔𝗬𝗥𝗜 𝗥𝗔𝗜𝗗 : **sʜʏʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}𝚜𝚛𝚊𝚒𝚍 <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}𝚜𝚛𝚊𝚒𝚍 <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>

⦿ 𝗙𝗟𝗜𝗥𝗧𝗜𝗡𝗚 : **ғʟɪʀᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}𝚏𝚕𝚒𝚛𝚝 <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}𝚏𝚕𝚒𝚛𝚝 <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>

⦿ 𝗛𝗣𝗣𝗬 𝗕𝗜𝗥𝗧𝗛𝗗𝗔𝗬 : **ғʟɪʀᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ʙsᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ʙsᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>


**© @V_VIP_OWNER**
"""

                 
raid_msg = f"""
**⦿ 𝗥𝗔𝗜𝗗 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 ⦿**

⦿ 𝗥𝗔𝗜𝗗 : **ᴀᴄᴛɪᴠᴀᴛᴇs ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsᴇʀ ғᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ**
  1) {hl}ʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>

⦿ 𝗥𝗔𝗣𝗟𝗬-𝗥𝗔𝗜𝗗 : **ᴀᴄᴛɪᴠᴀᴛᴇs ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ʀʀᴀɪᴅ <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>
  2) {hl}ʀʀᴀɪᴅ <ᴜsᴇʀɴᴀᴍᴇ>

⦿ 𝗗𝗥𝗔𝗜𝗗-𝗥𝗔𝗜𝗗 : **ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇs ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ᴅʀʀᴀɪᴅ <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>
  2) {hl}ᴅʀʀᴀɪᴅ <ᴜsᴇʀɴᴀᴍᴇ>

⦿ 𝗠-𝗥𝗔𝗜𝗗 : *ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ️‍**
  1) {hl}ᴍʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ᴍʀᴀɪᴅ <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>

⦿ 𝗦-𝗥𝗔𝗜𝗗 : **sʜʏʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}sʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}sʀᴀɪᴅ <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>

⦿ 𝗖-𝗥𝗔𝗜𝗗 : **ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ᴄʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ᴄʀᴀɪᴅ <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>

⦿ 𝗟𝗢𝗩𝗘-𝗥𝗔𝗜𝗗 : **ᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ️‍**
  1) {hl}ʟᴏᴠᴇʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ʟᴏᴠᴇʀᴀɪᴅ <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>

⦿ 𝗛𝗜𝗡𝗗𝗜-𝗥𝗔𝗜𝗗 - **ʜɪɴᴅɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ**
  1) {hl}ʜʀᴀɪᴅ <ᴄᴏᴜɴᴛ> <ᴜsᴇʀɴᴀᴍᴇ>
  2) {hl}ʜʀᴀɪᴅ <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>
  
  
**© @V_VIP_OWNER**
"""

spam_msg = f"""
**⦿ 𝗦𝗣𝗔𝗠 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 ⦿**

⦿ 𝗦𝗣𝗔𝗠 : **ᴀᴍs ᴀ ᴍᴇssᴀɢᴇ️‍**
  1) {hl}sᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ᴍᴇssᴇɢᴇ ᴛᴏ sᴘᴀᴍ>
  2) {hl}sᴘᴀᴍ <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏɪɴɢ ᴀɴʏ ᴍᴇssᴇɢᴇ>

⦿ 𝗣𝗢𝗥𝗡-𝗦𝗣𝗔𝗠 : **ᴘᴏʀɴᴏɢʀᴀᴘʜʏ  sᴘᴀᴍ**
  1) {hl}ᴘsᴘᴀᴍ <ᴄᴏᴜɴᴛ>

⦿ 𝗛𝗔𝗡𝗚 : **sᴘᴀᴍs ʜᴀɴɢ ᴍᴇssᴀɢᴇ ғᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀs**
  1) {hl}ʜᴀɴɢ <ᴄᴏᴜɴᴛᴇʀ>

⦿ 𝗔𝗕𝗨𝗦𝗘-𝗦𝗣𝗔𝗠 : **ᴏɴᴇ ᴡᴏʀᴅ ʙɪɢ ɢᴀᴀʟɪ sᴘᴀᴍ**
  1) {hl}𝚊𝚋𝚞𝚜𝚎 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  
** © @V_VIP_OWNER**
"""                     
           
           
@X1.on(events.CallbackQuery(pattern=r"help_back"))
@X2.on(events.CallbackQuery(pattern=r"help_back"))
@X3.on(events.CallbackQuery(pattern=r"help_back"))
@X4.on(events.CallbackQuery(pattern=r"help_back"))
@X5.on(events.CallbackQuery(pattern=r"help_back"))
@X6.on(events.CallbackQuery(pattern=r"help_back"))
@X7.on(events.CallbackQuery(pattern=r"help_back"))
@X8.on(events.CallbackQuery(pattern=r"help_back"))
@X9.on(events.CallbackQuery(pattern=r"help_back"))
@X10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
    [
      Button.inline("• sᴘᴀᴍ •", data="spam"),
      Button.inline("• ʀᴀɪᴅ •", data="raid")
    ],
    [
      Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="extra")
    ],
    [
      Button.url("• sᴀᴄʜɪɴ •", "https://t.me/V_VIP_OWNER"),
      Button.url("• ʀᴇᴘᴏ •", "https://t.me/Il_4ST_FIGHTER_lI")
    ],
    [   
      Button.inline("• ɴᴇᴡ •", data="yash")
      
    ]
            ]
          )
    else:
        await event.answer("𝗦𝗔𝗖𝗛𝗜𝗡 𝗦𝗔𝗡𝗔𝗧𝗔𝗡𝗜 [ @V_VIP_OWNER ] 𝗗𝗠 𝗞𝗔𝗥 𝗦𝗨𝗗𝗢 𝗠𝗜𝗟 𝗝𝗔𝗬𝗘𝗚𝗔︎ || 𝗘𝗞 𝗕𝗔𝗔𝗥 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗡𝗔 𝗥𝗔𝗡𝗗𝗜 𝗞𝗘" , cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"spam"))
@X2.on(events.CallbackQuery(pattern=r"spam"))
@X3.on(events.CallbackQuery(pattern=r"spam"))
@X4.on(events.CallbackQuery(pattern=r"spam"))
@X5.on(events.CallbackQuery(pattern=r"spam"))
@X6.on(events.CallbackQuery(pattern=r"spam"))
@X7.on(events.CallbackQuery(pattern=r"spam"))
@X8.on(events.CallbackQuery(pattern=r"spam"))
@X9.on(events.CallbackQuery(pattern=r"spam"))
@X10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("< Back", data="help_back"),],],
              ) 
    else:
        await event.answer("𝗦𝗔𝗖𝗛𝗜𝗡 𝗦𝗔𝗡𝗔𝗧𝗔𝗡𝗜 [ @V_VIP_OWNER ] 𝗗𝗠 𝗞𝗔𝗥 𝗦𝗨𝗗𝗢 𝗠𝗜𝗟 𝗝𝗔𝗬𝗘𝗚𝗔︎ || 𝗘𝗞 𝗕𝗔𝗔𝗥 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗡𝗔 𝗥𝗔𝗡𝗗𝗜 𝗞𝗘" , cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"raid"))
@X2.on(events.CallbackQuery(pattern=r"raid"))
@X3.on(events.CallbackQuery(pattern=r"raid"))
@X4.on(events.CallbackQuery(pattern=r"raid"))
@X5.on(events.CallbackQuery(pattern=r"raid"))
@X6.on(events.CallbackQuery(pattern=r"raid"))
@X7.on(events.CallbackQuery(pattern=r"raid"))
@X8.on(events.CallbackQuery(pattern=r"raid"))
@X9.on(events.CallbackQuery(pattern=r"raid"))
@X10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
          )
    else:
        await event.answer("𝗦𝗔𝗖𝗛𝗜𝗡 𝗦𝗔𝗡𝗔𝗧𝗔𝗡𝗜 [ @V_VIP_OWNER ] 𝗗𝗠 𝗞𝗔𝗥 𝗦𝗨𝗗𝗢 𝗠𝗜𝗟 𝗝𝗔𝗬𝗘𝗚𝗔︎ || 𝗘𝗞 𝗕𝗔𝗔𝗥 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗡𝗔 𝗥𝗔𝗡𝗗𝗜 𝗞𝗘" , cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"extra"))
@X2.on(events.CallbackQuery(pattern=r"extra"))
@X3.on(events.CallbackQuery(pattern=r"extra"))
@X4.on(events.CallbackQuery(pattern=r"extra"))
@X5.on(events.CallbackQuery(pattern=r"extra"))
@X6.on(events.CallbackQuery(pattern=r"extra"))
@X7.on(events.CallbackQuery(pattern=r"extra"))
@X8.on(events.CallbackQuery(pattern=r"extra"))
@X9.on(events.CallbackQuery(pattern=r"extra"))
@X10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )
    else:
        await event.answer("𝗦𝗔𝗖𝗛𝗜𝗡 𝗦𝗔𝗡𝗔𝗧𝗔𝗡𝗜 [ @V_VIP_OWNER ] 𝗗𝗠 𝗞𝗔𝗥 𝗦𝗨𝗗𝗢 𝗠𝗜𝗟 𝗝𝗔𝗬𝗘𝗚𝗔︎ || 𝗘𝗞 𝗕𝗔𝗔𝗥 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗡𝗔 𝗥𝗔𝗡𝗗𝗜 𝗞𝗘" , cache_time=0, alert=True)
        

@X1.on(events.CallbackQuery(pattern=r"yash"))
@X2.on(events.CallbackQuery(pattern=r"yash"))
@X3.on(events.CallbackQuery(pattern=r"yash"))
@X4.on(events.CallbackQuery(pattern=r"yash"))
@X5.on(events.CallbackQuery(pattern=r"yash"))
@X6.on(events.CallbackQuery(pattern=r"yash"))
@X7.on(events.CallbackQuery(pattern=r"yash"))
@X8.on(events.CallbackQuery(pattern=r"yash"))
@X9.on(events.CallbackQuery(pattern=r"yash"))
@X8.on(events.CallbackQuery(pattern=r"yash"))
async def help_yash(event):
     if event.query.user_id in SUDO_USERS:
         await event.edit(yash_msg,
             buttons=[[Button.inline("< Back", data="help_back"),],],
             )
     else:
        await event.answer("𝗦𝗔𝗖𝗛𝗜𝗡 𝗦𝗔𝗡𝗔𝗧𝗔𝗡𝗜 [ @V_VIP_OWNER ] 𝗗𝗠 𝗞𝗔𝗥 𝗦𝗨𝗗𝗢 𝗠𝗜𝗟 𝗝𝗔𝗬𝗘𝗚𝗔︎ || 𝗘𝗞 𝗕𝗔𝗔𝗥 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗡𝗔 𝗥𝗔𝗡𝗗𝗜 𝗞𝗘" , cache_time=0, alert=True)

