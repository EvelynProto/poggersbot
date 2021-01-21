import discord, random, datetime
from discord.ext import commands
from main import banlist, sendm, sendem, log

class Misc(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(help="Ask the 8ball a question", aliases=["8ball"])
	async def ball(self, ctx, *, question=None):
		if(question!=None):
			responses = ["It is certain.","It is decidedly so.","Without a doubt.","Yes – definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful."]
			bruh=ctx.guild.roles
			bruh2=[]
			bruh3=[]
			for i in bruh:
				a=i.name
				b=i.id
				bruh2.append(a)
				bruh3.append(b)
			for idx, i in enumerate(bruh3):
				txt=question.replace(f"<@&{str(i)}>", bruh2[idx])
				txt=txt.replace("@everyone", "everyone")
				txt=txt.replace("@here", "here")
				
			await sendm(banlist, ctx, f"Question: {txt}\n{random.choice(responses)}")
			await log(ctx, f"8ball question: {txt}")
		else:
			await sendm(banlist, ctx, "give me a question, get an answer")
			await log(ctx, "8ball question not received")
	
	@commands.command()
	async def calc(self, ctx, *, stuff=None):
		if(stuff==None):
			await log(ctx, "Didn't provide any calculation")
			await sendm(banlist, ctx, "You need to give me something to calculate in the message as the command")
		else:
			allowed=list("1234567890+*/-.")
			for i in stuff:
				if(not i in allowed):
					await log(ctx, f"Used not allowed characters: {stuff}")
					await sendm(banlist, ctx, f"One of the characters are not allowed \n \nAllowed characters: {allowed}")
					return False
			calc=eval(stuff)
			await log(ctx, f"Calculation was succesful: {stuff}={calc}")
			await sendm(banlist, ctx, f"Original calculation: {stuff} \n \nResult: {calc}")
					
	@commands.command()	
	async def sex(self, ctx, *, sexpeople = None):
		if(sexpeople==None):
			await log(ctx, "No user/text received")
			await sendm(banlist, ctx, "give me someone to sex")
		else:
			if(sexpeople.startswith("<@")):
				sexpeople=sexpeople.replace("<@","")
				sexpeople=sexpeople.replace("!","")
				sexpeople=sexpeople.replace(">","")
				sexid=int(sexpeople)
				sexuser = self.bot.get_user(sexid)
				RATE=random.randint(0,100)
				sexembed=discord.Embed(title=f"sex rate of {ctx.author.name} and {sexuser.name}", description=f"***{RATE}%***", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
				await sendem(banlist, ctx, sexembed)
				await log(ctx, f"User received: {str(sexuser)}, Rate: {RATE}")
			else:
				RATE=random.randint(00,100)
				sexembed=discord.Embed(title=f"sex rate of {ctx.author.name} and {sexpeople}", description=f"***{RATE}%***", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
				await log(ctx, f"Text received: {sexpeople}, Rate: {RATE}")
				await sendem(banlist, ctx, sexembed)

	@commands.command(help="pp size epik")
	async def pp(self, ctx):
		await log(ctx)
		if(ctx.author.id==663626592823541760):
			await sendm(banlist, ctx, f"8{'='*20}D")
		else:	
			await sendm(banlist, ctx, f"8{'='*random.randint(1,10)}D")	
			
	@commands.command(help="pong (bot latency)")
	async def ping(self, ctx):
		await log(ctx, "Current ping: {:.1f}".format(self.bot.latency * 1000)+" ms")
		await sendm(banlist, ctx, f"pong gaming \n" + "{:.1f}".format(self.bot.latency * 1000) +" ms")

	@commands.command(help="roll dice")
	async def roll(self, ctx, num = None):
		if num == None:
			await sendm(banlist, ctx, "You need to give me a number")
			await log(ctx, "No number received")
		elif int(num) < 1:
			await sendm(banlist, ctx, "Number must be bigger than 1")
			await log(ctx, "Number was not bigger than 1")
		else:
			await log(ctx)
			roll = random.randint(1, int(num))
			await sendm(banlist, ctx, f"Roll: {str(roll)}")
	
	@commands.command(help="repeats the text you sent")
	async def say(self, ctx, *, txt = None):
		if(txt==None):
			await sendm(banlist, ctx, "give me some text")
			await log(ctx, "No text received")
		else:
			bruh=ctx.guild.roles
			bruh2=[]
			bruh3=[]
			for i in bruh:
				a=i.name
				b=i.id
				bruh2.append(a)
				bruh3.append(b)
			for idx, i in enumerate(bruh3):
				txt=txt.replace(f"<@&{str(i)}>", bruh2[idx])
				txt=txt.replace("@everyone", "everyone")
				txt=txt.replace("@here", "here")
				
			await sendm(banlist, ctx, txt)
			await log(ctx, f"***ITS THE OTHER WEE WOO COMMAND!!!***\nText received: {txt}")
	
	@commands.command(help="repeats the text you sent and deletes your message")
	async def saydel(self, ctx, *, txt = None):
		if(txt==None):
			await sendm(banlist, ctx, "give me some text")
			await log(ctx, "***ITS THE WEE WOO COMMAND!!!***\nNo text received")
		else:
			bruh=ctx.guild.roles
			bruh2=[]
			bruh3=[]
			for i in bruh:
				a=i.name
				b=i.id
				bruh2.append(a)
				bruh3.append(b)
			for idx, i in enumerate(bruh3):
				txt=txt.replace(f"<@&{str(i)}>", bruh2[idx])
				txt=txt.replace("@everyone", "everyone")
				txt=txt.replace("@here", "here")
				
			await sendm(banlist, ctx, txt)
			await log(ctx, f"***ITS THE WEE WOO COMMAND!!!***\nText received: {txt}")
		await ctx.message.delete()
		
	@commands.command()
	async def uwu(self, ctx):
		await log()
		await sendm(banlist, ctx, "no")
		
	
	@commands.command(help="baka mitai")
	async def bakamitai(self, ctx):
		await log(ctx)
		await sendm(banlist, ctx, "baka mitai kodomo na no ne yume wo otte kizu tsuite uso ga heta na kuse ni waraenai egao miseta I LOVE YOU mo roku ni iwanai kuchibeta de honma ni bukiyou na no ni na no ni doushite sayonara wa ieta no dame da ne dame yo dame na no yo anta ga suki de suki sugite dore dake tsuyoi osake de mo yugamanai omoide ga baka mitai baka mitai hontou baka ne anta shinjiru bakari de tsuyoi onna no furi setsunasa no yokaze abiru hitori ni natte san-nen ga sugi machinami sae mo kawarimashita na no ni na no ni doushite miren dake okizari honma ni roku na otoko ya nai soroi no yubiwa hazushimasu zamaa miro seisei suru wa ii kagen mattete mo baka mitai dame da ne dame yo dame na no yo anta ga suki de suki sugite dore dake tsuyoi osake de mo yugamanai omoide ga baka mitai honma ni roku na otoko ya nai soroi no yubiwa hazushimasu zamaa miro seisei suru wa nan na no yo kono namida baka mitai")

	@commands.command()
	async def monke(self, ctx):
		await log(ctx)
		await sendm(banlist, ctx, ":orangutan:")

	@commands.command()
	async def arabfunny(self, ctx):
		await log(ctx)
		await sendm(banlist, ctx, "https://media.discordapp.net/attachments/742075556648058900/754209706024763392/repost_this_image_to_instantly_die.png?width=388&height=300")

	@commands.command()
	async def randomshit(self, ctx):
		await log(ctx, "i still dont know what is this")
		await sendm(banlist, ctx, "https://cdn.discordapp.com/attachments/742075556648058900/754210572488278127/The_engineer.txt")
	
	@commands.command()
	async def pong(self, ctx):
		await log(ctx)
		await sendm(banlist, ctx, "ha")

	@commands.command()
	async def cbt(self, ctx):
		await log(ctx)
		await sendm(banlist, ctx, "Cock and ball torture (CBT) is a sexual activity involving application of pain or constriction to the male genitals. This may involve directly painful activities, such as wax play, genital spanking, squeezing, ball-busting, genital flogging, urethral play, tickle torture, erotic electrostimulation or even kicking.[1] The recipient of such activities may receive direct physical pleasure via masochism, or emotional pleasure through erotic humiliation, or knowledge that the play is pleasing to a sadistic dominant. Many of these practices carry significant health risks.")

	@commands.command()
	async def peepee(self, ctx):
		await log(ctx)
		await sendm(banlist, ctx, "poopoo")

	@commands.command()
	async def poopoo(self, ctx):
		await log(ctx)
		await sendm(banlist, ctx, "peepee")

	@commands.command()
	async def slaughter(self, ctx):
		await log(ctx)
		await sendm(banlist, ctx, "I don't know what I was thinking\n Leaving my child behind\n Now I suffer the curse\n Knowing now I am blind\n \n With all this anger, guilt and sadness\n Coming to haunt me forever\n I can't wait for the cliff at the end of the river\n \n Is this revenge I am seeking\n Or seeking someone to avenge me\n Stuck in my own paradox\n I wanna set myself free\n \n Maybe I should chase and find\n Before they'll try to stop it\n It won't be long before I'll become a puppet\n \n It's been so long\n Since I last have seen my son\n Lost to this monster\n To the man behind the slaughter\n \n Since you've been gone\n I've been singing this stupid song\n So I could ponder\n The sanity of your mother\n \n I wish I lived in the present\n With the gift of my past mistakes\n But the future keeps luring in like a pack of snakes\n \n Your sweet little eyes\n Your little smile, is all I remember\n Those fuzzy memories mess with my temper\n \n Justification is killing me\n But killing isn't justified\n What happened to my son, I'm terrified\n \n It lingers in my mind\n And the thought keeps on getting bigger\n I'm sorry my sweet baby\n I wish I've been there\n \n It's been so long\n Since I last have seen my son\n Lost to this monster\n To the man behind the slaughter\n \n Since you've been gone\n I've been singing this stupid song\n So I could ponder\n The sanity of your mother\n")

	@commands.command()
	async def b(self, ctx):
		await log(ctx)
		await sendm(banlist, ctx, ":b:")

	@commands.command()
	async def a(self, ctx):
		await log(ctx)
		await sendm(banlist, ctx, ":a:")

	@commands.command()
	async def cock(self, ctx):
		await log(ctx)
		await sendm(banlist, ctx, ":chicken:")

	@commands.command()
	async def connectionterminated(self, ctx):
		await log(ctx)
		await sendm(banlist, ctx, "Connection terminated.")
		await sendm(banlist, ctx, "I'm sorry to interrupt you Elizabeth, if you still even remember that name. But I'm afraid you've been misinformed. You are not here to receive a gift, nor have you been called here by the individual you assume. Although you have indeed been called.\n \nYou have all been called here. Into a labyrinth of sounds and smells, misdirection and misfortune. A labyrinth with no exit, a maze with no prize. You don't even realize that you are trapped. Your lust for blood has driven you in endless circles, chasing the cries of children in some unseen chamber, always seeming so near, yet somehow out of reach.\n \nBut you will never find them, none of you will. This is where your story ends.\n \nAnd to you, my brave volunteer, who somehow found this job listing not intended for you. Although there was a way out planned for you, I have a feeling that's not what you want. I have a feeling that you are right where you want to be. I am remaining as well, I am nearby.\n \nThis place will not be remembered, and the memory of everything that started this can finally begin to fade away. As the agony of every tragedy should. And to you monsters trapped in the corridors: Be still and give up your spirits, they don't belong to you.\n \nFor most of you, I believe there is peace and perhaps more waiting for you after the smoke clears. Although, for one of you, the darkest pit of Hell has opened to swallow you whole, so don't keep the devil waiting, old friend.\n \nMy daughter, if you can hear me, I knew you would return as well. It's in your nature to protect the innocent. I'm sorry that on that day, the day you were shut out and left to die, no one was there to lift you up into their arms the way you lifted others into yours. And then, what became of you.\n \nI should have known you wouldn't be content to disappear, not my daughter. I couldn't save you then, so let me save you now.\n \nIt's time to rest. For you, and for those you have carried in your arms.\n \nThis ends for all of us.")
		await sendm(banlist, ctx, "End communication.")

def setup(bot):
	bot.add_cog(Misc(bot))
