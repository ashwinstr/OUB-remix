"""Get a user-customised google search meme!"""

# Plugin By - XlayerCharon[XCB]
# TG ~>>//@CharonCB21
# Ported for OUB by @AshSTR

import asyncio
import os
from PIL import Image, ImageDraw, ImageFont
from wget import download

<<<<<<< HEAD
from userbot import CMD_HELP
from userbot.events import register


=======
from userbot.events import register

>>>>>>> cdaec16f4ce3c4f4a687cd9a72e080829a251e2f
@register(outgoing=True, pattern="^.fgs ((.*) ; (.*))")
async def FakeGoogleSearch(event):
    """ Get a user-customised google search meme! """
    input_str = event.pattern_match.group(1)
    if input_str is None:
        await event.edit("No input found!", del_in=5)
        return
    if ";" in input_str:
        search, result = input_str.split(";", 1)
    else: 
        await event.edit("Invalid Input! Check help for more info!", del_in=5)
        return
      
    await event.edit('Connecting to `https://www.google.com/` ...')
    await asyncio.sleep(2)
    img='https://i.imgur.com/wNFr5X2.jpg'
    r=download(img)
    photo=Image.open(r)
    drawing=ImageDraw.Draw(photo)
    blue=(0,0,255)
    black=(0,0,0)
<<<<<<< HEAD
    font1=ImageFont.truetype("userbot/utils/styles/ProductSans-BoldItalic.ttf",25)
=======
    font1=ImageFont.truetype("userbot/utils/styles/ProductSans-BoldItalic.ttf",20)
>>>>>>> cdaec16f4ce3c4f4a687cd9a72e080829a251e2f
    font2=ImageFont.truetype("userbot/utils/styles/ProductSans-Light.ttf",23)
    drawing.text((450, 258), result, fill=blue, font=font1)
    drawing.text((270, 37), search, fill=black, font=font2)
    photo.save("downloads/test.jpg")
    reply = event.pattern_match.group(2)
    await event.delete()
    reply_id = event.pattern_match.group(3) if reply else None
    await event.client.send_file(
        event.chat_id,
        'downloads/test.jpg',
        reply_to_message_id=reply_id)
    os.remove('downloads/test.jpg')

<<<<<<< HEAD
    CMD_HELP.update(
    {
        "fake_google_search": "`.fgs`\n"
        "Usage: Get a user-customised google search meme!\n\n"
        "`.fgs [UpperText] ; [LowerText]`\n"
    }
)
=======
>>>>>>> cdaec16f4ce3c4f4a687cd9a72e080829a251e2f
