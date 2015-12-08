"""
Creator: Chris Wagner
Created Date: 12/03/2015
Last Updated: 12/07/2015

Summary: 
    Hangman is a game that prompts the user to guess a word, letter by letter. 
    Word entries are contained in the Hangman.txt file.
"""

import random

def Party_Time():
	
	guessUL = 3 #The amount of guesses the user has.
	tries = 0 #The starting number of incorrect guesses the user has made.
	inc_guess = [] #The incorrect guesses the user has made.
	winflag = False #Flag is True when user wins

	text_file = open("Hangman.txt", 'r')
	word_bank = []
	for line in text_file:
		if line.strip() != "" and not line.startswith("#"): #Ignoring blank lines or commented lines
			word_bank.append(line.strip())

	word = random.choice(word_bank)
	ret_word = ["_" for item in range(len(word))] #Return word

	print "\n\n\nWe're having a party and you're invited! What can you bring?\n" + ("_ "*len(word))

	while tries < guessUL:

		guess = raw_input("\nGuess a letter or the full word: ").lower().strip()
		guessflag = False #Flag is True if guess letter is found in word

		if len(guess)==1: #Check to see if a letter is in the word
			for item in range(0, len(word)):
				if guess == word[item]: #The letter is in the word
					ret_word[item] = guess
					guessflag = True

				if item==(len(word)-1) and guessflag==False:
					print "\nSorry, there is no '%s' in the word.\n" %guess
					inc_guess.append(guess)
					tries+=1

			if "".join(ret_word) == word:
				winflag = True
				print "\nYou win! The word is '%s'!" %word
				break

		elif len(guess)>1:
			if guess == word:
				winflag = True
				print "\nYou win! The word is '%s'!" %word
				break
			else: 
				print "\nSorry, that's not the word we were looking for."
				tries+=1

		print '\n' + ' '.join(ret_word) + '\n\n-----Incorrect Guesses-----\n' + ' '.join(inc_guess)

	if tries==guessUL and winflag==False: #User has exhausted the tries and has lost game
		print "\nSorry, the word we were looking for is '%s'.\n" %word

	replay = raw_input("\n\nGame Over. Play again? (Y/N)\n")
	if replay.lower() == "y":
		Party_Time()


Party_Time()  


'''
Testing:
1. Make sure that the answer can work with spaces included
2. Win letter by letter, win with entire word entry
3. Multiples of the same letter register in one turn
4. If incorrect letter guess, will return a error and add to list of letters that are not included
5. Number of tries works, both for individual letter and full word guesses
6. Replay loop works correctly
'''