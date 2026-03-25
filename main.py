import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'bot listo jijijija: {bot.user}')   

@bot.command()
async def carton(ctx):
    await ctx.send("Organizador de cables: Corta un rectángulo de cartón y haz pequeñas muescas en los bordes para enrollar tus cables USB o audífonos.")

@bot.command()
async def plastico(ctx):
    await ctx.send("Protector de cables: Corta un popote (pajilla) en espiral y enróllalo alrededor de la base de tus cables de carga.")

@bot.command()
async def tubo(ctx):
    await ctx.send("Lanzador de Proyectiles (Soplata): Un clásico para lanzar pequeños dardos de papel usando aire.")


@bot.command()
async def DVD(ctx):
    await ctx.send("Base para miniaturas: Si haces figuras o personajes, un CD es la base circular perfecta y estable para pegarlos.")

@bot.command()
async def botella(ctx):
    await ctx.send("Mini-Invernadero: Corta la base de una botella transparente, hazle unos agujeros pequeños en la tapa para que respire y colócala sobre una maceta pequeña para mantener el calor.")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def limpiar(ctx, cantidad: int = 100):
    eliminados = await ctx.channel.purge(limit=cantidad + 1)
    await ctx.send(f'Se han eliminado {len(eliminados) - 1} mensajes.', delete_after=5)

bot.run('token')