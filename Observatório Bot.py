import os

import discord
from dotenv import load_dotenv

from discord.ext import commands




client = discord.Client()

TOKEN = 'NzIwMDU1Nzk4MDQ2MzkyNDUw.XuA7hA.aUmePB8rLp9Oy5aW6Vu5XgDlBFw'


@client.event
async def on_member_join(member):
    
    await member.send("""**Bem-Vindo ao Observatório**

`Para receber notificações de promoções:`

*Escolha o hardware que você quer receber promoções`(#cpu, #gpu, #ram ou #mobo)` e vá no começo do chat e reaja com :white_check_mark:
E então você receberá NOTIFICAÇÕES de PROMOÇÕES do HARDWARE que você reagiu.*






                      """)



 
                    
client.run(TOKEN)
