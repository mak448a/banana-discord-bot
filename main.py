import os
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
	command_prefix="!",  # Change to desired prefix
	case_insensitive=True,  # Commands aren't case-sensitive
  intents=intents
)

@bot.event 
async def on_ready():  # When the bot is ready
    print(f"Logged into discord as {bot.user}")  # Prints the bot's username and identifier

@bot.event
async def on_message(message):
  if str(message.author) == "BananaBot#5366":
    return
  if "mom" in message.content.lower():
    await message.channel.purge(limit=1)
    await message.channel.send(f"I moderated your message, {message.author.mention}. Don't post \"UR MoM\" memes. Seriously.")
    print(f"Moderated {message.author}")

  moderate = ["moyai", "moai", "🗿"]
  for moderation in moderate:
    if moderation in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(f"I moderated your message, {message.author.mention}. Seriously stop saying stuff like that..")

  congratulate = ["wtfuckium", "fuck", "shit", "damn", "bitch", "fuckium",
                 "shitium", "dang"]
  # It's kind of stupid, but we do it anyway. :)
  for congratulation in congratulate:
    if congratulation in message.content.lower():
      await message.channel.send(f"Congratulations, {message.author.mention}! Keep saying that! :)")
      return


bot.run("OTk1NTIzNzk5NzM2OTA5ODQ0.GIlQAv.dlEObbkndzBPv-G-pR0ZPtdI7AfK2HdUQ9rTjc")
