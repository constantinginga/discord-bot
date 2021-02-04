import random, discord, asyncpraw

reddit = asyncpraw.Reddit(client_id="OWgHAGU12eUpJQ",
client_secret="61O6kJSVUNVv1VP7b1Gu8wPt8ADEpA",
user_agent="Discord Memes")

async def generate_meme():
    subreddit = await reddit.subreddit("programmerhumor")
    meme = await subreddit.random()
    return meme.url

async def generate_cute():
    subreddit = await reddit.subreddit("eyebleach")
    pic = await subreddit.random()
    return pic.url

def shrek():
    return """
⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
"""

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()
client = discord.Client()

@client.event
async def history(channel):
    count = {
        "Constantin": 0,
        "Klaus": 0,
        "Jakub": 0,
        "Farouk": 0,
        "Tudor": 0,
        "BOT": 0
    }

    messages = await channel.history(limit=None).flatten()
    for message in messages:
        print(message.author.name)
        if message.author == client.user:
            count["BOT"] += 1
        elif message.author.name == "Constantout":
            count["Constantin"] += 1
        elif message.author.name == "Reiner":
            count["Jakub"] += 1
        elif message.author.name == "farouk":
            count["Farouk"] += 1
        elif message.author.name == "Latvish":
            count["Klaus"] += 1
        elif message.author.name == "andronachi09":
            count["Tudor"] += 1

    # return list of tuples
    return sorted(count.items(), key=lambda x: x[1], reverse=True)

@client.event
async def on_message(message):
    id = client.get_guild(806770937420578836)

    # List of valid commands
    commands = ["!help", "!meme", "!users", "!ranking", "!cute", "!shrek"]
    


    if str(message.content)[0] == "!" and message.content not in commands and message.author != client.user:
        await message.channel.send("Command does not exist. Type !help for the list of commands.")
    elif message.content == commands[0]:
        embed = discord.Embed(title="Commands", description="Full list of commands")
        embed.add_field(name="!meme", value="Random programmer meme")
        embed.add_field(name="!users", value="Number of users")
        embed.add_field(name="!ranking", value="Ranking of users by number of messages")
        embed.add_field(name="!cute", value="Random cute image")
        embed.add_field(name="!shrek", value="THE GOD")
        await message.channel.send(content=None, embed=embed)
    elif message.content == commands[1]:    
        await message.channel.send(await generate_meme())
    elif message.content == commands[2]:
        await message.channel.send(f"""Number of members: {id.member_count}""")
    elif message.content == commands[3]:
        count = await history(client.get_channel(806770937420578839))
        ranking = "Top virgins:\n"
        for index, name in enumerate(count, start=1):
            ranking += "#{} {} - {}\n".format(index, name[0], name[1])

        await message.channel.send(ranking)
    elif message.content == commands[4]:
        await message.channel.send(await generate_cute())
    elif message.content == commands[5]:
        await message.channel.send(shrek())

client.run(token)