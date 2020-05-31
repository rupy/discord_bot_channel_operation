import discord
from discord.ext import commands

class ChannelOperationCog(commands.Cog):

    ########################################
    ## lsコマンド（テキストチャネルと、ボイスチャネルのリストを取得）
    ########################################
    @commands.group()
    async def ls(self, ctx):

        if ctx.invoked_subcommand is None:
            await ctx.send('このコマンドにはサブコマンドが必要です。')

    # text_channels
    @ls.command()
    async def tc(self, ctx):
        print('[[!ls tc]]')

        text_channels = self.get_text_channels(ctx)

        output = ""
        for text_channel in text_channels:
            output += "%s %d\n" % (text_channel.name, text_channel.id)
        await ctx.send(output)

    # voice_channels
    @ls.command()
    async def vc(self, ctx):
        print('[[!ls vc]]')

        voice_channels = self.get_voice_channels(ctx)
        output = ""
        for voice_channel in voice_channels:
            output += "%s %d\n" % (voice_channel.name, voice_channel.id)
        
        await ctx.send(output)

    ########################################
    ## mvコマンド（メンバーへの@メンションとチャネルのIDをスペース区切りの引数として指定する）
    ########################################    
    @commands.command()
    async def mv(self, ctx, member: discord.Member, channel_id: int):
        print('[[!mv %s %d]]' % (member, channel_id))

        channel = ctx.bot.get_channel(channel_id)

        if member.voice is None:
            invite = await channel.create_invite()
            await member.send(str(invite))
        else:
            await member.move_to(channel)

    ########################################
    ## mv2コマンド（メンバーへの@メンションとチャネルの名前をスペース区切りの引数として指定する）
    ########################################    
    @commands.command()
    async def mv2(self, ctx, member: discord.Member, channel_name: str):
        print('[[!mv2 %s %s]]' % (member, channel_name))

        channels = self.get_voice_channels(ctx)
        channel_filtered = [channel for channel in channels if channel.name == channel_name]
        if len(channel_filtered) > 0:
            channel = channel_filtered[0]
        else:
            await ctx.send("ボイスチャネル「%s」は見つかりませんでした。" % (channel_name))
            return

        if member.voice is None:
            invite = await channel.create_invite()
            await member.send(str(invite))
        else:
            await member.move_to(channel)

    ########################################
    ## ユーティリティ関数
    ########################################
    def get_text_channels(self, ctx):
        channels = ctx.guild.channels
        text_channels = [channel for channel in channels if isinstance(channel, discord.TextChannel)]
        return text_channels

    def get_voice_channels(self, ctx):
        channels = ctx.guild.channels
        voice_channels = [channel for channel in channels if isinstance(channel, discord.VoiceChannel)]
        return voice_channels

