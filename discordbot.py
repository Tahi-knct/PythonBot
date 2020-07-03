import discord
import random
from discord.ext import tasks
from datetime import datetime
import time

TOKEN = 'NzA2OTQwOTQ4MjEwMzg0OTc3.XrD8Kw.Y3EujqB878BAd9pUXkcv2zr8Bqc'

CHANNEL_ID = 707062324573372428
CHANNEL_ID2 = 445976879107801098

discord_voice_channel_id = 684949556139393024
discord_voice_channel_id2 = 445195374500511754

client = discord.Client()

bgm = 0


@client.event
async def on_ready():
    print('ログインしました')
    await greet()

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if client.user in message.mentions:
        await reply(message)
    if message.author.bot:
        return
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    if message.content == '/niconico':
        channel = client.get_channel(discord_voice_channel_id)
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('bgm.mp3'), after=lambda e: print('done', e))
        time.sleep(20)
        await vc.disconnect()
    if message.content == '/bo':
        channel = client.get_channel(discord_voice_channel_id)
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('konokawa.mp3'), after=lambda e: print('done', e))
        time.sleep(20)
        await vc.disconnect()
    if message.content == '/konohage':
        channel = client.get_channel(discord_voice_channel_id)
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('konohage.mp3'), after=lambda e: print('done', e))
        time.sleep(20)
        await vc.disconnect()
    if message.content in '大丈夫':
        await message.channel.send('そんな装備で大丈夫か？')
        channel = client.get_channel(discord_voice_channel_id)
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('bgm1.mp3'), after=lambda e: print('done', e))
        time.sleep(5)
        await vc.disconnect()
    if message.content in 'SE':
        bgm = random.randint(0, 10)
        print(bgm)
        if bgm == 0:
            channel = client.get_channel(discord_voice_channel_id)
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio('bgm2.mp3'), after=lambda e: print('done', e))
            time.sleep(5)
            await vc.disconnect()
        if bgm == 1:
            channel = client.get_channel(discord_voice_channel_id)
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio('bgm3.mp3'), after=lambda e: print('done', e))
            time.sleep(5)
            await vc.disconnect()
        if bgm == 2:
            channel = client.get_channel(discord_voice_channel_id)
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio('bgm4.mp3'), after=lambda e: print('done', e))
            time.sleep(5)
            await vc.disconnect()
        if bgm == 3:
            channel = client.get_channel(discord_voice_channel_id)
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio('bgm5.mp3'), after=lambda e: print('done', e))
            time.sleep(5)
            await vc.disconnect()
        if bgm == 4:
            channel = client.get_channel(discord_voice_channel_id)
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio('bgm6.mp3'), after=lambda e: print('done', e))
            time.sleep(5)
            await vc.disconnect()
        if bgm == 5:
            channel = client.get_channel(discord_voice_channel_id)
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio('bgm7.mp3'), after=lambda e: print('done', e))
            time.sleep(5)
            await vc.disconnect()
        if bgm == 6:
            channel = client.get_channel(discord_voice_channel_id)
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio('bgm8.mp3'), after=lambda e: print('done', e))
            time.sleep(5)
            await vc.disconnect()
        if bgm == 7:
            channel = client.get_channel(discord_voice_channel_id)
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio('bgm9.mp3'), after=lambda e: print('done', e))
            time.sleep(5)
            await vc.disconnect()
        if bgm == 8:
            channel = client.get_channel(discord_voice_channel_id)
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio('bgm10.mp3'), after=lambda e: print('done', e))
            time.sleep(5)
            await vc.disconnect()

async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('今起きたお（起動完了）')
    print('ready')

# 返信する非同期関数を定義
async def reply(message):
    reply = f'ﾃﾞｭﾌ{message.author.mention}氏、それはないでござるよ？' # 返信メッセージの作成
    await message.channel.send(reply)  # 返信メッセージを送信

@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    channel = client.get_channel(discord_voice_channel_id)
    vc = await channel.connect()
    if now == '08:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おは幼女')
    if now == '12:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('お昼だお')
    if now == '00:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('日付変わったお！さっさと寝ろ！')
        channel = client.get_channel(CHANNEL_ID2)
        await channel.send('日付変わったお！さっさと寝ろ！')
        channel = client.get_channel(discord_voice_channel_id)
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('bgm.mp3'), after=lambda e: print('done', e))
        channel = client.get_channel(discord_voice_channel_id2)
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('bgm.mp3'), after=lambda e: print('done', e))
    if now == '15:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('3時だお')
    if now == '12:03':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('[定期]バ美肉したい')
    if now == '16:10':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('はうあ～')
loop.start()

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)