# Discord Photo-Roulette Bot
A FOSS discord bot that allows you and your friends to play photo roulette!

![Photo Roulette Logo](https://i.imgur.com/iyf83jR.png)

# What is Photo Roulette?
Photo roulette is a party game *perfect for discord* where players put a pool of pictures into a "**hat**". The computer then **randomly** chooses a picture out of the "**hat**" and everyone guesses whose picture it is!

# Contents: 
## Getting Started
- How do I get the bot onto my server?
- What if I want to run the bot locally?
- How do I get the bot going?
## User Documentation
- User Commands
- What's the point of this bot?
- Why'd you make this?
## Technical Documentation
- Overview
- Integrated Technologies

## Getting Started:
### How do I get the bot onto my server?
To get started, you have to have:
- A discord account
- A discord server where you have the permissions to "Manage" the server  

Then, you click the following link:  
https://discord.com/oauth2/authorize?client_id=760273969688739882&scope=bot&permissions=52224  

**Login to discord** (if you haven't already)  
**Select the server you want to add the bot to** from the "add to server" dropdown menu  
**Select continue** and the bot should load onto your server!  

### But I want to run the bot locally
No problem! Just download the bot and follow the instructions under "*How do I get the bot onto my server?*". After that, **run the bot.py file** in a program of your choice!

### Okay, the bot is on my server, so how do I get it going?
So the bot is loaded onto the server, but it doesn't know which text-channel you want it to be in. To tell it where to go, go into a text-channel of your choice, and type in **!setup**
This will let the bot know which text-channel to go to. If all goes well, it should reply with a successful message! If you want to move it to another text-channel, go into another text-channel and type **!setup** there.

Then, you follow the on-screen instructions to start playing!

## User Documentation:
### User Commands:  
**!setup** : command used to tell the bot which channel to run on.  
__*Common uses*__  
Used after giving bot permissions to server (get it up and running)  
To remind users of commands  


**!startroulette** : command used to tell the bot to pick an image from the "hat"  
__*Common uses*__  
Used after three people are present in the text-channel **AND** at least one picture has been submitted.  

__*Possible returns**__  
*"There aren't enough pictures! Send them to the discord bot via DM."*  
In this scenario, the bot hasn't received any pictures from the players.  
Solution: Players DM the bot pictures  

*"Have more people join! You can't have less than 3 players."*  
In this scenario, there aren't enough active people in the text-channel.  
Solution: Make sure you have 3 people **active** in the text-channel. If there are three people and it still returns this, have everybody type in the channel to become **active**. Then, one person needs to **!startroulette**  


**!voteskip** :  command that puts in a player's vote to skip another player's turn
__*Common uses*__  
To skip someone that is AFK (away from keyboard)

__*Possible returns**__  
*"You can't voteskip twice, {name}"*  
Solution: You have already voted to skip the current person. You can only vote once.  

*"{votes} more vote(s) needed to skip this player"*  
Solution: To completely vote the person out, everybody (excluding the AFK person in question) needs to vote skip them.  

*"Enough votes were received to skip the current guesser."*  
Solution: Yay! The person in question has been skipped and the bot will let you know whose turn it is now.  

**!newroulette** : command to clear the image pool (aka **hat**)  
__*Common uses*__  
Clear an image pool that the players are tired of  

__*Possible returns**__  
*"Picture pool cleared!"*  
Solution: Now, the players need to DM the bot more pictures (since the pool is now clear).

**!endroulette** : to stop the bot's "game"  
__*Common uses*__  
To end the picture roulette game  

__*Possible returns**__  
*"Until next time..."*  
Solution: Come play again next time!


### What's the point of this bot?  
As of October 2020, I haven't seen any picture roulette bots for Discord. Having played it on a phone at school with a group of friends, I knew how entertaining it could be. Therefore, I sought to follow an engineer's way: *"If it doesn't exist, **create** it!"*. As for how it could potentially carry over from a phone game to a discord-bot minigame, I know Discord is an environment in which people spend hours on hours of time conversing with each other. The bot serves as a good way to involve everybody in the environment and hopefully get a few laughs out of everyone. The point of this bot is to hopefully cure a little of their boredom and maybe even inspire others to create a bot of their own!  

### Why did you make this?  
As part of the Aggie Coding Club, I was invited to participate in the *Capsher Coding Challenge*! Creating a discord bot seemed interesting and so I decided to dip my toes into it. Although I was alotted about a month's worth of time, I was only able to work on it for about 12 hours due to studying and exams. However, this was a really cool experience because I got to see the "fruits of my labor" at the end of it.  

## Technical Documentation:  
### Overview:  

### Integrated Technologies:  

