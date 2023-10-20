import os
import discord
from discord.ext import commands
from discord import Member
from dotenv import load_dotenv

from welcome import on_member_join_handler

# Load the environment variables from the .env file
load_dotenv()

intents = discord.Intents.default()
intents.members = True  # Subscribe to the privileged members intent

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready() -> None:
    print(f"We have logged in as {bot.user}", flush=True)


@bot.event
async def on_member_join(member: Member) -> None:
    return await on_member_join_handler(member)


bot.run(os.environ.get("DISCORD_TOKEN"))
