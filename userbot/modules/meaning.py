from userbot.events import register
from userbot import CMD_HELP
import asyncurban

@register(outgoing=True, pattern=r"^\.meaning(?: |$)(.*)")
async def _(event):
    word = event.pattern_match.group(1)
    dictionary = asyncurban()
    words = dictionary.meaning(word)
    output = f"**Word :** __{word}__\n\n"
    try:
        for a, b in words.items():
            output += f"**{a}**\n"
            for i in b:
                output += f"⚫__{i}__\n"
        await event.edit(output)
    except Exception:
        await event.edit(f"Couldn't fetch meaning of {word}")


CMD_HELP.update(
    {
        "dictionary": "**Plugin :** `dictionary`\
    \n\n**Syntax : **`.meaning query`\
    \n**Usage : **Fetches meaning of the given word\
    "
    }
)
