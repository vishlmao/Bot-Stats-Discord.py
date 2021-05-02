# Enabling Intents

client = commands.Bot(command_prefix=" <your_prefix> ", intents = discord.Intents.all())

# Code for the command

@client.command(aliases=['stats'])
@commands.guild_only()
async def statistics(ctx):
  stats_em = discord.Embed(title="***The bot's statistics.***", description = "Here is some info on the bot.", color=discord.Color.green())
  stats_em.add_field(name="`Servers`", inline=False, value = f"In {len(client.guilds)} servers!")
  stats_em.add_field(name="`Made By`", inline=False, value = ' <your_username> ')
  stats_em.add_field(name="`Played By`", inline=False, value=f" Playing with {len(client.users)} users!")
  stats_em.add_field(name="`Ping`", value =f"**{round(client.latency * 1000)}ms!**", inline=False)
  stats_em.add_field(name="`Commands`", value =" ** <command_count> ** commands for now!")
  stats_em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
  await ctx.reply(embed=stats_em)
