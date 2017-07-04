from sys import exit
from random import randint


#Creating a class for a character
class Character(object):

	def __init__(self,name,types,attack,armor,ap = 0):
		self.name = name
		self.types = types
		self.attack  = attack
		self.armor = armor
		self.ap = ap
	def attacked(self,max_power,ap = 0):
		self.ap = randint(1,max_power)
		print "%s is hit with %d power."% (self.name,self.ap)
		if self.ap >= self.armor:
			print "%s have been defeated"% self.name
		else:
			print "%s stand upright and continues to fight."% self.name
		self.armor -= self.ap
		return self.armor
	def speach(self):
		if self.types == 'trickster':
			print "Hy I am a %s and my name is %s. I'm ready to fight!"% (self.types, self.name)
			print "What!?"
		elif self.types == 'caster':
			 print "Hy I am a %s and my name is %s. I'm ready to fight!"% (self.types, self.name)
			 print "I will blast them to smolding coal!!"
		elif self.types == 'warrior':
			print "Hy I am a %s and my name is %s. I'm ready to fight!"% (self.types, self.name)
			print "My shield is at your side!"
		elif self.types == 'healer':
			print "Hy I am a %s and my name is %s. I'm ready to fight!"% (self.types, self.name)
			print "Light is on my side!"


class Monster(object):

	def __init__(self,name,attack,armor, ap = 0):
		self.name = name
		self.attack = attack
		self.armor = armor
		self.ap = ap
		
	def speach(self):
		if self.name == 'Grovic':
			print "This is my lair you bastard and its treasures the same."
			print "Prepare to fight!!!"
	def attacked(self,max_power,ap = 0):
		
		self.ap = randint(5,max_power)
		print "%s is hit with %d power."% (self.name,self.ap)
		if self.ap >= self.armor:
			print "%s has been defeated"% self.name
		else:
			print "Your blow wasn't powerfull enought."
		self.armor -= self.ap
		return self.armor





#In here this will be the welcoming message at the beggining
#along side with the choosing of characters to play with.
class Welcoming(object):

	def welcoming_mess(self):
		print "Welcome to ADVENTURE PY!!!"
	def choose(self):
		print "Choose a character to play with...."
		print "Will it be... "
		print "1. Paladin"
		print "2. Mage"
		print "3. Rogue"
		print "4. Priest"
		print "Type in the numbers associeted with the class."
		self.choose = raw_input("> ")
		if '1' in self.choose:
			paladin.speach()
		elif '2' in self.choose:
			mage.speach()
		elif '3' in self.choose:
			rogue.speach()
		elif '4' in self.choose:
			priest.speach()

	def play(self):
		if self.choose == '1':
			game = Start_Room('warrior')
			game.enter()
		elif self.choose == '2':
			game = Start_Room('caster')
			game.enter()
		elif self.choose == '3':
			game = Start_Room('trickster')
			game.enter()
		elif self.choose == '4':
			game = Start_Room('healer')
			game.enter()
	#This play_F() will be used allong side the global variable in Second_room()
	#to keep the same character selected from the initial stage
	def play_F(self):
		if complete == True:
			if self.choose == '1':
				game = Last_Room('warrior')
				game.the_battle()
			elif self.choose == '2':
				game = Last_Room('caster')
				game.the_battle()
			elif self.choose == '3':
				game = Last_Room('trickster')
				game.the_battle()
			elif self.choose == '4':
				game = Last_Room('healer')
				game.the_battle()

class Scene(object):

	def enter(self):
		print "This scene will exit()"
		exit(1)

class Start_Room(Scene):

	def __init__(self,types):
		self.types = types

	def enter(self):
		print "You first appear in a dark room filled with smoke."
		print "You feel a wierd smell and hope it's not you."
		print "You barely enter the dungeon and a goblin jumps in front of you."
		goblin.speach()
		if self.types == 'warrior':
			print "You draw your sword."
			print "Do you want to attack first?(y/n)"
			resp = raw_input(">")
			# I think this logic can be written in a more abstract way
			# and avoit to repeat it so much
			if resp == 'y':
				x = 0
				tries = 0
				while tries < 3:
					tries += 1
					if goblin.armor > x and paladin.armor > x:
						x += goblin.ap
						x +=paladin.ap
						goblin.attacked(paladin.attack)
						print "\n"
						paladin.attacked(goblin.attack)
						print "\n"
						print "%s armor is: %d"% (goblin.name,goblin.armor)
						print "%s armor is: %d"% (paladin.name,paladin.armor)
						print "\n"
					elif goblin.armor <= 0:
						print "You bastard or what ever is your name, this is not the last of us!!!"
						print "He vanishes into a cloud of mist and you are now able to move on."
						second_room = Second_room()
						second_room.enter()
						break
					elif paladin.armor <= 0:
						print "Your adventure ends here."
						death.ending() 
			elif resp == 'n':
				print "Your lack of reflex got you killed."
				print "%s the Goblin managed to stab you with his pointy dagger killing you in an instant."% goblin.name
				death.ending()

		elif self.types == 'healer':
			print "You open you Book of Wisdom."
			print "Do you want to attack first?(y/n)"
			resp = raw_input(">")
			if resp == 'y':
				x = 0
				tries = 0
				while tries < 3:
					tries += 1
					if goblin.armor > x:
						x += goblin.ap
						x += priest.ap
						goblin.attacked(priest.attack)
						print "\n"
						priest.attacked(goblin.attack)
						print "\n"
						print "%s armor is: %d"% (goblin.name,goblin.armor)
						print "%s armor is: %d"% (priest.name,priest.armor)
						print "\n" 
						
					elif goblin.armor <= 0:
						print "You bastard or what ever is your name, this is not the last of us!!!"
						print "His vanishes into a cloud of mist and you are now able to move on."
						second_room = Second_room()
						second_room.enter()
						break
					elif priest.armor <= 0:
						print "Your adventure ends here."
						death.ending()
			elif resp == 'n':
				print "Your lack of reflex got you killed."
				print "%s the Goblin managed to stabe you with his pointy dagger killing you in an instant."% goblin.name
				death.ending()

		elif self.types == 'trickster':
			print "Your dagger are ready and pointy, and you look great in all that leather."
			print "Do you want to attack first?(y/n)"
			resp = raw_input(">")
			if resp == 'y':
				x = 0
				tries = 0
				while tries < 3:
					tries += 1
					if goblin.armor > x:
						x += goblin.ap
						x += rogue.ap
						goblin.attacked(rogue.attack)
						print "\n"
						rogue.attacked(goblin.attack)
						print "\n"
						print "%s armor is: %d"% (goblin.name,goblin.armor)
						print "%s armor is: %d"% (rogue.name,rogue.armor)
						print "\n" 
					elif goblin.armor <= 0:
						print "You bastard or what ever is your name, this is not the last of us!!!"
						print "He vanishes into a cloud of mist and you are now able to move on."
						second_room = Second_room()
						second_room.enter()
						break
					elif priest.armor <= 0:
						print "Your adventure ends here"
						death.ending() 
			elif resp == 'n':
				print "Your lack of reflex got you killed."
				print "%s the Goblin managed to stabe you with his pointy dagger killing you in an instant."% goblin.name
				death.ending()
		elif self.types == 'caster':
			print "You smash your staff to the floor creating a vibration in the ground."
			print "Do you want to attack first?(y/n)"
			resp = raw_input(">")
			if resp == 'y':
				x = 0
				tries = 0
				while tries < 3:
					tries += 1
					if goblin.armor > x:
						x += goblin.ap
						x += mage.ap
						goblin.attacked(mage.attack)
						print "\n"
						mage.attacked(goblin.attack)
						print "\n"
						print "%s armor is: %d"% (goblin.name,goblin.armor)
						print "%s armor is: %d"% (mage.name,mage.armor)
						print "\n"
					elif goblin.armor < x:
						print "You bastard or what ever is your name, this is not the last of us!!!"
						print "He vanishes into a cloud of mist and you are now able to move on."
						second_room = Second_room()
						second_room.enter()
						break
					elif mage.armor <= 0:
						print "Your andventure ends here."
						death.ending()
			elif resp == 'n':
				print "Your lack of reflex got you killed."
				print "%s the Goblin managed to stabe you with his pointy dagger killing you in an instant."% goblin.name
				death.ending()



class Second_room(Scene):
	@classmethod
	def enter(self):
		print "Dealing with that %s was pretty easy,\nbut at least you got to see how an empty dungeon looks like."% goblin.name
		print "I bet you feel lonely now."
		print "The exit of this room can only be done if you pass some riddles\nso here we go."
		print "To what is PI equal to?"
		tries = 0
		while tries < 3:
			pi = raw_input(">")
			tries += 1
			if '3.14' in pi:
				print "You are correct."
				tries = 3
				self.next_trial(Second_room())
				break
			elif '3.14159' in pi:
				print "Ok nerd, you got it."
				tries = 3
				self.next_trial(Second_room())
				break
			else:
				death.ending()

	def next_trial(self):			
		print "The next trial should be much more easier."
		print "DISABLE THE TSAR BOMBA COUNTDOWN SEQUENCE!!!"
		print "Just kidding, relax, just answer me this: "
		print "What is that which has one voice and yet becomes four-footed and two-footed and three-footed?"
		tries = 0
		while tries < 3:
			tries += 1
			answer = raw_input("> ")
			if "human" in answer:
				print "You got it this time."
				self.final_trial()
				break
			elif 'human beign' in answer:
				print "You got it this time."
				self.final_trial()
				break
			else:
				print "The room is filled with toxic smoke, you die!"
				death.ending()

	def final_trial(self):
		print "The last trial will be a more difficult one."
		print "You have to guess the correct lock number to the next area."
		print "It's a 3 digit number, 1 to 5."
		print "Best of luck"
		answer = raw_input("> ")
		digit1 = randint(1,5)
		digit2 = randint(1,5)
		digit3 = randint(1,5)
		if answer == digit1 and digit2 and digit3:
			print "You go it."
			print "The number was: %d%d%d"% (digit1,digit2,digit3)
		elif answer == '125':
			print "Very good, very good indeed."
			print "You are not that dumb after all."
			#Here I make a global variable to be capture in Welcoming() class
			#I'm doing this to keep the character that has been choosen in 
			#the first instance
			global complete
			complete = True
		else:
			print "You failed."
			self.final_trial()


class Last_Room(Scene):
	def __init__(self,types):
		self.types = types
	def the_battle(self):
		if self.types == "warrior":
			print "Your last venture from the trials was hard."
			print "What will be next is gruesome."
			print "\n"
			print "As you thought you no longer need the assistance of you holy sword,"
			print "an orc that goes by the name of %s appears"% orc.name
			print "%s spirit told my tribe what you have done,"% goblin.name
			print "you will DIE!!!"
			print "What will you do:"
			print "1. Invoke the Holy Spirit into your sword."
			print "2. Smash the sword on to the shield and prepare to attack."
			print "3. Throw the sword hoping to slice his head."
			answer = raw_input("> ")
			if '1' in answer:
				paladin = Character('Sir Butholy','warrior',40,40)
				x = 0
				tries = 0
				while tries < 4:
					tries += 1
					if orc.armor > x and paladin.armor > x:
						x += orc.ap
						x += paladin.ap
						orc.attacked(paladin.attack)
						print "\n"
						paladin.attacked(orc.attack)
						print "\n"
						print "%s armor is: %d"% (orc.name,orc.armor)
						print "%s armor is: %d"% (paladin.name,paladin.armor)
						print "\n"
					elif orc.armor <= 0:
						print "Indeed it's as the legends have told, you are trully powerfull"
						print "You have won the battle. All the richies of this world are yours."
						print "Congratulation have a pint."
						tries = 4
						break
					elif paladin.armor <= 0:
						print "Your adventure ends here."
						tries = 4
						death.ending()
			elif '2' in answer:
				print "The orc is way more powerfull then you."
				print "Even after a long fight he is able to crush your shild and your skull."
				death.ending()
			elif '3' in answer:
				print "What are you nuts! You missed."
				print "Why would you throw your only method of offence."
				death.ending() 
		elif self.types == "caster":
			print "Mages never have problems with trials such us this."
			print "\n"
			print "As you thought you no longer need the assistance of you staff,"
			print "an orc that goes by the name of %s appears"% orc.name
			print "%s spirit told my tribe what you have done,"% goblin.name
			print "you will DIE!!!"
			print "What will you do:"
			print "1. Invoke the Fire God to fight along side you."
			print "2. Smash the staff to the ground and ready yourself."
			print "3. Throw the staff hopping to couse an explosion from your crystal."
			answer = raw_input("> ")
			if '1' in answer:
				mage = Character('Archmage Wizbeard','caster',50,40)
				x = 0
				tries = 0
				while tries < 4:
					tries += 1
					if orc.armor > x and mage.armor > x:
						x += orc.ap
						x += mage.ap
						orc.attacked(mage.attack)
						print "\n"
						mage.attacked(orc.attack)
						print "\n"
						print "%s armor is: %d"% (orc.name,orc.armor)
						print "%s armor is: %d"% (mage.name,mage.armor)
						print "\n"
					elif orc.armor <= 0:
						print "Indeed it's as the legends have told, you are trully powerfull"
						print "You have won the battle. All the richies of this world are yours."
						print "Congratulation have a green tea."
						tries = 4
						break
					elif mage.armor <= 0:
						print "Your adventure ends here."
						tries = 4
						death.ending()
			elif '2' in answer:
				print "Well you clearly aren't that smart."
				print "His superior strength killes you quite brutally."
				death.ending()
			elif '3' in answer:
				print "I don't get it. Staffs don't work like that."
				print "Wouldn't be dangerous to carry an unstable crystal?"
				print "Without your staff or just target practice."
				death.ending()
		elif self.types == "trickster":
			print "The trials weren't that hard for a rogue."
			print "But they could have been better."
			print "\n"
			print "As you thought you no longer need the assistance of you awesome daggers,"
			print "an orc that goes by the name of %s appears"% orc.name
			print "%s spirit told my tribe what you have done,"% goblin.name
			print "you will DIE!!!"
			print "What will you do: "
			print "1. Summon the shadows to help and guide."
			print "2. Prepare your daggers by making some fancy move."
			print "3. Throw the dagger in the hope of stabbing him in the heart."
			answer = raw_input("> ")
			if '1' in answer:
				print "You summon the shadows, shrouding you darkness the orc can't see you."
				rogue = Character('Eliza Vipersting','trickster',65,40)
				x = 0
				tries = 0
				while tries < 4:
					tries += 1
					if orc.armor > x and rogue.armor > x:
						x += orc.ap
						x += mage.ap
						orc.attacked(rogue.attack)
						print "\n"
						rogue.attacked(orc.attack)
						print "\n"
						print "%s armor is: %d"% (orc.name,orc.armor)
						print "%s armor is: %d"% (rogue.name,rogue.armor)
						print "\n"
					elif orc.armor <= 0:
						print "Indeed it's as the legends have told, you are trully powerfull"
						print "You have won the battle. All the richies of this world are yours."
						print "Congratulation have a glass of red wine."
						tries = 4
						break
					elif rogue.armor <= 0:
						print "Your adventure ends here."
						tries = 4
						death.ending()
			elif '2' in answer:
				print "You may be stealty but you are up against a huge orc."
				print "You try and try but low stamina brought you face to face with dead."
				death.ending()
			elif '3' in answer:
				print "Well, first of all you missed, second why threw your weapons?"
				print " The orc steals your dagger and uses them to stab you...repeatedly."
				death.ending()
		elif self.types == "healer":
			print "The light of Wisdom always guys a priest."
			print "Light will always vanquish darkness."
			print "\n"
			print "As you think you no longer need the assistance of you holy book,"
			print "an orc that goes by the name of %s appears"% orc.name
			print "%s spirit told my tribe what you have done,"% goblin.name
			print "you will DIE!!!"
			print "What will you do: "
			print "1. Call the Horde of Angels upon this miserable fool."
			print "2. Open the book at a famous gospel and annoy him to death."
			print "3. Throw the book and staff and preace non-violence."
			if '1' in answer:
				print "With every spell you attack, every angel does the same."
				priest = Character('Pope Wiseldwarf','healer',55,40)
				x = 0
				tries = 0
				while tries < 4:
					tries += 1
					if orc.armor > x and priest.armor > x:
						x += orc.ap
						x += priest.ap
						orc.attacked(priest.attack)
						print "\n"
						priest.attacked(orc.attack)
						print "\n"
						print "%s armor is: %d"% (orc.name,orc.armor)
						print "%s armor is: %d"% (priest.name,priest.armor)
						print "\n"
					elif orc.armor <= 0:
						print "Indeed it's as the legends have told, you are trully powerfull"
						print "You have won the battle. All the richies of this world are yours."
						print "Congratulation have a pint of holy water."
						tries = 4
						break
					elif priest.armor <= 0:
						print "Your adventure ends here."
						tries = 4
						death.ending()
			elif '2' in answer:
				print "You are just to weak and to tired."
				print "The orc finishes you quickly."
				death.ending()
			elif '3' in answer:
				print "You just literally threw your life away."
				print "For a priest thats just dumb and lacking in WISDOM!"
				print "You just died in record time. Gratz"
				death.ending()
class Death(Scene):
		transmit_death = [
			"You are a looser",
			"The game is not that hard you know.",
			"You really failed on this one.",
			"Maybe you are not that smart.",
			"One orange is not equal with two binaculars, hombre."
		]
		def ending(self):
			print Death.transmit_death[randint(0,len(self.transmit_death)-1)]
			exit(1)
			
#Creating objects
start = Welcoming()
death = Death()

# Instantieting characters and mosters
paladin = Character('Sir Butholy','warrior',10,30)
mage = Character('Archmage Wizbeard','caster',20,10)
rogue = Character('Eliza Vipersting','trickster',25,15)
priest = Character('Pope Wiseldwarf','healer',15,15)
goblin = Monster('Grovic',10,10)
orc = Monster('Barkhead',20,40)

start.welcoming_mess()
start.choose()
start.play()
#It will only run if the global 'complete' variable becomes True
start.play_F()