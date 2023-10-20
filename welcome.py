# Handle welcome behavior for users

from ast import For
import discord
from discord import Member, Forbidden


WELCOME_MESSAGE = """Welcome to the server, {username}!

We're so excited that you joined! This is a private channel (only you can see it) where we will help you get started with our community guidelines and rules. Don't delete this channel because we have special plans for it in the future!

If you haven't signed up for Gigo go ahead and create and account @ https://gigo.dev/signup
"""


async def on_member_join_handler(member: Member) -> None:
    """
    Says hello to a new user
    """
    # send the welcome message
    try:
        await member.send(WELCOME_MESSAGE.format(username=member.mention))
    except Forbidden:
        print(f"{member}'s DMs are locked; failed to welcome them")
