import discord
import os
from discord.ext import commands
import random
description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

place_of_launch=os.environ.get('place')
if place_of_launch=='heroku':
    bot_token=os.environ.get('bot_token')
elif place_of_launch=='local':
    bot_token=os.environ.get('test_bot_token')
print(place_of_launch)
bot = commands.Bot(command_prefix='!', description=description)
@bot.command(pass_context=True)
async def t(ctx):
  say = input("Введите сообщение через консоль: ")
  await ctx.send(say)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('БАТЯ В ЗДАНИЇ')

@bot.command()
async def start(ctx):
    await ctx.send('БАТЯ В ЗДАНИЇ')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
    await ctx.send()
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined in {member.joined_at}')

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


try:
    bot.run(bot_token)
except Exception as error:
    print(error)
    input('.')