import discord
from redbot.core import commands, checks
from redbot.core.utils.chat_formatting import humanize_number

__version__ = "0.1.0"
__author__ = "Leafy"

class Guild(commands.Cog):
    """
    Cookie Run Kingdom Guild Related Command
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def drag(self, ctx, level: int, percentage: int):
        """
        Count Dragon Health Remaining.

        Dragon Level varies from 1 to 60.
        Percentage varies from 1 to 100.
        """
        if (level <= 0 or level > 60):
            description = "<:error:785047391257624596> Level capped between 1 and 60"
            embed = discord.Embed(description=description, color=15747399)
            await ctx.send(embed=embed)
            return

        if (percentage <= 0 or percentage > 100):
            description = "<:error:785047391257624596> Percentage capped between 1 and 100"
            embed = discord.Embed(description=description, color=15747399)
            await ctx.send(embed=embed)

        dragon_health = {
            1: 3000000,
            2: 3150000,
            3: 3474000,
            4: 3648000,
            5: 3830000,
            6: 4022000,
            7: 4224000,
            8: 4436000,
            9: 4658000,
            10: 4890000,
            11: 5134000,
            12: 5390000,
            13: 5660000,
            14: 5944000,
            15: 6242000,
            16: 6554000,
            17: 6682000,
            18: 7226000,
            19: 7588000,
            20: 8366000,
            21: 9224000,
            22: 10170000,
            23: 11212000,
            24: 12360000,
            25: 13626000,
            26: 15024000,
            27: 16564000,
            28: 18262000,
            29: 20134000,
            30: 22198000,
            31: 24474000,
            32: 26982000,
            33: 29748000,
            34: 32798000,
            35: 35472000,
            36: 37632000,
            37: 39922000,
            38: 42354000,
            39: 44932000,
            40: 47206000,
            41: 49114000,
            42: 51098000,
            43: 53162000,
            44: 55310000,
            45: 57262000,
            46: 58992000,
            47: 60774000,
            48: 61612000,
            49: 64504000,
            50: 66456000,
            51: 68464000,
            52: 70532000,
            53: 72664000,
            54: 74860000,
            55: 77122000,
            56: 79452000,
            57: 81854000,
            58: 84328000,
            59: 86876000,
            60: 89502000
        }

        min_hp = dragon_health[level] * ((percentage - 1) / 100)
        max_hp = dragon_health[level] * percentage / 100
        description = f"<:success:785047433716957194> Lv. {level} Dragon at {percentage}% varies between **{humanize_number(min_hp)}** and **{humanize_number(max_hp)}**"
        embed = discord.Embed(description=description, color=4437377)
        return await ctx.send(embed=embed)

