
import asyncio
import os
import sys
import discord
from discord.ext.commands import context
import yaml
from discord.ext import commands
from discord.utils import get


if not os.path.isfile("config.yaml"):
    sys.exit("'config.yaml' not found! Please add it and try again.")
else:
    with open("config.yaml") as file:
        config = yaml.load(file, Loader=yaml.FullLoader)



class custom_commands(commands.Cog, name="custom"):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command('addrole')
    @commands.has_permissions(administrator=True) 
    async def addrole(self, ctx, role : discord.Role, user : discord.Member):
        if ctx.author.guild_permissions.administrator:
            await user.add_roles(role)
            await ctx.send(f"Successfully given {role.mention} to {user.mention}")
            await self.create_role(name = role + "1")
     
    @commands.command('removerole')
    @commands.has_permissions(administrator=True) 
    async def removerole(self, ctx, role : discord.Role, user : discord.Member):
        if ctx.author.guild_permissions.administrator:
            await self.user.remove_roles(role)
            await ctx.send(f"Successfully removed {role.mention} from {user.mention}")

    @commands.command('add')
    @commands.has_permissions(administrator=True) 
    async def giverole(self, ctx, role: discord.Role, members: commands.Greedy[discord.Member]):
        for m in members:
            await m.add_roles(role)
            await asyncio.sleep(1)  # You don't want to get ratelimited!
        await ctx.send("Done!")

def setup(bot):
    bot.add_cog(custom_commands(bot))
