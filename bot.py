# bot.py
import random
import discord

# --- NOTES --- #
# 1. AUTHORIZE BOT TO SERVER - https://discord.com/oauth2/authorize?client_id=760273969688739882&scope=bot&permissions=52224 # -- ! you need 'Manage Server' permissions
# --- END --- #

CHANNEL_ID = 0
TOKEN = 'NzYwMjczOTY5Njg4NzM5ODgy.X3JqTw.NXzE02TA6fevX6wsuPTWQ8apgJk'

def update_players(): # grabs list of non-bot users
    player_list = []
    for member in client.users:
        if member.bot:
            continue
        player_list.append(member)
    return player_list

def get_new_guesser(player_list, correct_guess): # get random guesser
    while True:
        x = player_list[random.randint(0, len(player_list)-1)]
        if x != correct_guess:
            return x

images = []
author_list = []
current_guesser = ""
correct_guess = ""
skip_votes = 0
skip_votes_people = []

client = discord.Client()

# when bot is started, welcome with message
@client.event
async def on_ready():
    global CHANNEL_ID
    # setup not done yet
    if (CHANNEL_ID == 0):
        return

    channel = client.get_channel(CHANNEL_ID)
    await channel.send("🎀***__𝕯𝖎𝖘𝖈𝖔𝖗𝖉 𝕻𝖎𝖈𝖙𝖚𝖗𝖊 𝕽𝖔𝖚𝖑𝖊𝖙𝖙𝖊__***🎀")
    await channel.send("★·.·´¯`·.·★----------------★·.·`¯´·.·★")
    await channel.send("DM the discord bot pictures... it'll choose one and you have to guess whose it is! :face_with_monocle:")
    await channel.send("After everyone has sent their pictures in, type in !startroulette :exclamation:")
    await channel.send("First to guess it wins! :money_with_wings:")
    await channel.send("To **start a new round**, type in *!startroulette*")
    await channel.send("To **reset the pool of pictures**, type in *!newroulette*")
    await channel.send("To **quit this game**, type in *!endroulette*")
    await channel.send("★·.·´¯`·.·★----------------★·.·`¯´·.·★")

# when bot gets a message...
@client.event
async def on_message(message):
    global CHANNEL_ID
    if not message.guild: # if private dm
        if len(message.attachments) > 0: # if dm is an image and not a message         
            # put received images into an array
            channel = client.get_channel(CHANNEL_ID)
            global images
            if (len(images) == 0):
                images = message.attachments
            else:
                images += message.attachments
            
            # get corresponding author for images
            author_list.append(message.author)


    else: # if non-private message
        global current_guesser
        global correct_guess
        global skip_votes

        ## channel-change related
        if (message.content == "!setup"):
            CHANNEL_ID = message.channel.id
            channel = client.get_channel(CHANNEL_ID)
            await channel.send("Setup successful!")
            return
        
        channel = client.get_channel(CHANNEL_ID)

        ## after setup...
        if (message.content == "Setup successful!" and message.author.id == client.user.id):
            await channel.send("You can always use the !setup command in a different text channel to move the bot.")
            await channel.send("🎀***__𝕯𝖎𝖘𝖈𝖔𝖗𝖉 𝕻𝖎𝖈𝖙𝖚𝖗𝖊 𝕽𝖔𝖚𝖑𝖊𝖙𝖙𝖊__***🎀")
            await channel.send("★·.·´¯`·.·★----------------★·.·`¯´·.·★")
            await channel.send("DM the discord bot pictures... it'll choose one and you have to guess whose it is! :face_with_monocle:")
            await channel.send("After everyone has sent their pictures in, type in !startroulette :exclamation:")
            await channel.send("First to guess it wins! :money_with_wings:")
            await channel.send("To **start a new round**, type in *!startroulette*")
            await channel.send("To **reset the pool of pictures**, type in *!newroulette*")
            await channel.send("To **quit this game**, type in *!endroulette*")
            await channel.send("★·.·´¯`·.·★----------------★·.·`¯´·.·★")

        ## game-related
        # make sure message comes from right channel
        if (message.channel.id == CHANNEL_ID):
            if message.content.startswith("!startroulette"):
                player_list = update_players() # get list of players (non-bot)
                
                # make sure there is at least one picture
                if (len(images) < 1):
                    await channel.send("There aren't enough pictures! Send them to the discord bot via DM.")
                    return
                print(player_list)
                # make sure there are at least 3 players
                if (len(player_list) < 3):
                    await channel.send("Have more people join! You can't have less than 3 players. :cry:")
                    return
                
                # randomly select picture to send
                rand = random.randint(0, len(images)-1)
                selected = images[rand]
                selected_image = await selected.to_file()
                # set correct guess
                correct_guess = author_list[rand]

                # send randomly selected picture
                await channel.send(file=selected_image)

                # get new guesser
                current_guesser = get_new_guesser(player_list, correct_guess)

                # prompt players to guess a person!
                await channel.send(f"It's {current_guesser}'s turn to guess!")
                await channel.send("Use the !{username_guess#xxxx} command to guess!")

                # tell players about voteskip
                await channel.send(f"Is the guesser AFK? Use the !voteskip command. {len(player_list) - skip_votes - 1} more votes needed to skip player.")

                # give players list of possible guesses
                await channel.send("List of possible guesses:")
                for player in player_list:
                    await channel.send(f"{player}")

            # voteskip implementation
            elif message.content.startswith("!voteskip"):
                global skip_votes_people
                # check if voted before
                if (type(skip_votes_people) == int):
                    if skip_votes_people == message.author.id:
                        await channel.send(f"You can't voteskip twice, {message.author}!")
                        return
                else:
                    for id in skip_votes_people:
                        print(id)
                        print(message.author.id)
                        print(type(id))
                        print(type(message.author.id))
                        if (int(message.author.id) == id):
                            await channel.send(f"You can't voteskip twice, {message.author}!")
                            return

                skip_votes += 1
                if (type(skip_votes_people) == int):
                    skip_votes_people = int(message.author.id)

                elif (type(skip_votes_people) == list):
                    skip_votes_people.append(int(message.author.id)) # keep track of who has voted already


                player_list = update_players()

                # if not enough votes yet
                if (skip_votes < len(player_list) - 1):
                    if ((len(player_list)-1) - skip_votes == 1):
                        await channel.send(f"{(len(player_list)-1) - skip_votes} more vote needed to skip player.")
                    else:
                        await channel.send(f"{(len(player_list)-1) - skip_votes} more votes needed to skip player.")
                    return

                # if enough votes
                elif (skip_votes == len(player_list) - 1):
                    await channel.send("Enough votes were receieved to skip the current guesser.")
                    skip_votes = 0
                    # get new guesser
                    current_guesser = get_new_guesser(player_list, correct_guess)
                    # prompt players to guess a person!
                    await channel.send(f"It's {current_guesser}'s turn to guess!")
                    await channel.send("Use the !{username_guess#xxxx} command to guess!")
                    skip_votes_people = []
                    return

            # reset images
            elif message.content.startswith("!newroulette"):
                images = []
                await channel.send("Picture pool cleared!")

            # exit program
            elif message.content.startswith("!endroulette"):
                await channel.send("Until next time...")
                exit(0)
            
            # guessing
            elif message.content.startswith("!"):
                # get list of players (non-bot)
                player_list = update_players()

                guess = message.content
                guess = guess.replace("!", "")

                guess_name_discrim = guess.split("#")
                guess_name = str(guess_name_discrim[0])
                guess_discrim = str(guess_name_discrim[1])

                # seeing if name was a possibility and if it was a correct guess
                decent_guess = False
                correct = False
                for name in player_list:
                    if (guess_name == name.name and guess_discrim == name.discriminator):
                        decent_guess = True
                        if (guess == str(correct_guess)):
                            correct = True
                
                # if someone else's turn
                if (message.author != current_guesser):
                    await channel.send(f"{message.author}, it's not your turn!")
                    return

                # if guesser guesses incorrectly, it's someone else's turn
                if (decent_guess and not correct):
                    await channel.send(f"Nice try, {message.author}! {guess} wasn't it though.")
                    prev_guesser = current_guesser
                    current_guesser = get_new_guesser(player_list, correct_guess)
                    while prev_guesser == current_guesser:
                        current_guesser = get_new_guesser(player_list, correct_guess)

                    await channel.send(f"Now it's {current_guesser} turn to guess.")
                
                # invalid guess - but not an avaliable option
                elif (not decent_guess and not correct):
                    await channel.send(f"That was an invalid guess, {message.author}! {guess} isn't an option, your turn will be skipped.")
                    while prev_guesser == current_guesser:
                        current_guesser = get_new_guesser(player_list, correct_guess)
                    await channel.send(f"Now it's {current_guesser} turn to guess.")

                # yay someone got it right
                elif (decent_guess and correct):
                    await channel.send(f"Nice! *{message.author}* got it right! It was *{correct_guess}*'s picture. :white_check_mark:")
                    await channel.send("To play from the same picture pool, type **!startroulette**")
                    await channel.send("To play with new pictures, type **!newroulette**. Then, DM the bot more pictures and **!startroulette**")
                    await channel.send("Otherwise, type in **!endroulette** to quit playing :cry:")            


client.run(TOKEN)