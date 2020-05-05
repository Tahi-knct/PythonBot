import discord
from discord.ext import tasks
from datetime import datetime

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzA2OTQwOTQ4MjEwMzg0OTc3.XrBowA.RxiGqyhEC7CBKKvgCU_55ipGc3g'

CHANNEL_ID = 707062324573372428  #チャンネルID

discord_voice_channel_id = 684949556139393024

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    await greet() # 挨拶する非同期関数を実行

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
        channel = client.get_channel(discord_voice_channel_id)
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('bgm.mp3'), after=lambda e: print('done', e))

async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('今起きたお（起動完了）')

@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '08:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おは幼女')
    if now == '12:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('お昼だお')
    if now == '00:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('日付変わったお！さっさと寝ろ！')
    if now == '15:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('3時だお')
    if now == '14:12':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('VCだお')

loop.start()

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)