import os, random, discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
  
client = commands.Bot(command_prefix='!')
#Create a .env file with your bots token, and keep it secret!
token = os.getenv('TOKEN')

bees = []

with open('bees.txt') as file:
    lines = file.readlines()
    bees = [line.rstrip() for line in lines]

@client.command(name='BeeMe', help='responds with a random quote from the cinema classic "bee movie"')
async def bee(ctx):
    resp = random.choice(bees)
    await ctx.send(resp)
    
@client.command(name='BeeSomeone', help='DM Someone else a line from the bee movie')
async def beeMention(ctx, user: discord.User):
    resp = random.choice(bees)
    await user.send(resp)
    
@client.command(name='SendSomeLinesFromBeeMovie', help='DM Willie the entire Bee Move script')
async def SendSomeLinesFromBeeMovie(ctx, user:discord.User, number):
    count = range(int(number))
    await ctx.send(f'{user} is going to hate this...')
    for x in count:
        await user.send(bees[x])

# run the bot
client.run(token)
