import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import cleverbotfree

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TARGET_CHANNEL_ID = int(os.getenv("TARGET_CHANNEL_ID"))

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
cb = cleverbotfree.Cleverbot()

@bot.event
async def on_ready():
    print(f"🛸 MarleyBot-Free is online as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == TARGET_CHANNEL_ID:
        async with message.channel.typing():
            response = await cb.single_exchange(message.content)
            await message.channel.send(response)

    await bot.process_commands(message)

bot.run(DISCORD_TOKEN)
