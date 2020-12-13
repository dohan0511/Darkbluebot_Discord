import asyncio
import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    dohanyee_quotes = [
        'ㅗ',
        ':neutral_face:',
        ':frowning:',
        ':middle_finger:',
    ]

    if '도한이' in message.content.lower():
#    if message.content == '!test':
        response = random.choice(dohanyee_quotes)
        await message.channel.send(response)
client.run('Nzg3MjczMTg1NTQ0MjQxMTYy.X9SjSg.BlbKtTdldGX4yIVyAwmApPLPdxU')
