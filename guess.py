from random import randint


print "Welcome to....GUESS THAT NUMBER!!!!"
print "Next thing I want you to do is insert a number and only one number"
print "from 1 to 10"
print "If you win you get a life time supply of...you know it"
print "COAL!!!"
print "Remember you get only 5 tries."
print "Good luck!!!"

guesses = 0
while guesses < 5:
	number = raw_input("> ")
	val = randint(1,10)
	guesses += 1
	if int(number) != val:
		print val
		print "Try again!"
		continue
	else:
		print val
		print "Congratulations you WON a life time supply of Coal!!!"
		break