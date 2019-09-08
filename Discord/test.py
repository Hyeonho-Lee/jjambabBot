import discord    #디스코드 들고옴

client = discord.Client()

@client.event
async def on_ready() :
    #처음 접속할시
    print("아아 봇준비완료~")
    print(client.user.name)
    print(client.user.id)
    await client.change_presence (game=discord.Game(name="봇 만들어 보는중"))
    
@client.event
async def on_message() :
    #만약 유저로부터 다른 말이 나온다면
    if message.author == cliet.user :
        return
    if message.content == "!" :
        await client.send_message (message.channel, "아아 테스트으으")
    if message.content == "!아아" :
        await client.send_message (message.channel, "예에에")
        
client.run('NjIwMTM3NTY0ODQxNTc0NDIx.XXSa_g.86uJbhZaahja2XuduHHFNW-HM_E')