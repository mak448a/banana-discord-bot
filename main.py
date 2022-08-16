import os
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(
	command_prefix="!",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 892748589854511124  # Change to your discord id!!!

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

  moderate = ["moyai", "moai"]
  for moderation in moderate:
    if moderation in message.content.lower():
        await message.channel.purge(limit=1)
        await message.channel.send(f"I moderated your message, {message.author.mention}. Seriously stop saying stuff like that..")

  congratulate = ["wtfuckium", "fuck", "shit", "damn", "bitch", "fuckium",
                 "shitium", "dang"]
  for congratulation in congratulate:
    if congratulation in message.content.lower():
      await message.channel.send(f"Congratulations, {message.author.mention}! Keep saying that! :)")
      return


keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  # Starts the bot