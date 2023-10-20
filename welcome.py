# Handle welcome behavior for users

import discord
from discord import TextChannel, Member, PermissionOverwrite


WELCOME_MESSAGE = """Welcome to the server, {username}!

We're so excited that you joined! This is a private channel (only you can see it) where we will help you get started with our community guidelines and rules. Don't delete this channel because we have special plans for it in the future!

If you haven't signed up for Gigo go ahead and create and account @ https://gigo.dev/signup
"""


async def on_member_join_handler(member: Member) -> None:
    """
    Says hello to a new user
    """
    # get the welcome channel
    channel: TextChannel = discord.utils.get(
        member.guild.text_channels, name='welcome'
    )

    # exit if no channel
    if not channel:
        return

    # create the private channel to message the user
    new_channel: TextChannel = await member.guild.create_text_channel(
        f"gigo-bot-{member.id}",
        overwrites={
            member.guild.default_role: PermissionOverwrite(read_messages=False),
            member: PermissionOverwrite(read_messages=True),
        },
    )

    # send the welcome message
    await new_channel.send(WELCOME_MESSAGE.format(username=member.mention))
