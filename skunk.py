from random import randint

def check_roll(dice_1, dice_2):
	"""
	INPUT: Two dice
	OUTPUT: Roll score and if total score needs set to 0.
	"""
	if dice_1 == 1 and dice_2 == 1:
		roll_score = 0
		reset = True
	elif dice_1 == 1 or dice_2 == 1:
		roll_score = 0
		reset = False
	else:
		roll_score = dice_1 + dice_2
		reset = False
	return roll_score, reset
	
def score(roll_score, reset, total_score, current_round):
	"""
	INPUT: Score for current roll, reset score Boolean,
	current total score, and current round score
	OUTPUT: New round score, new total score and Boolean for new round
	"""
	if reset == True:
		return 0, 0, True
	elif roll_score == 0:
		return 0, total_score, True
	else:
		new_score = current_round + roll_score
		return new_score, total_score, False
		
def print_score(round_score, total_score):
	print()
	print("Your score for this round is " + str(round_score))
	print("Your total score for the game is " + str(total_score))
	print()

def user_decision(round_score, total_score):
	answer = input("Type 'b' to bank your points and go to the next round or press ENTER to roll again.")
	print()
	if answer == 'b':
		total_score += round_score
		print("Your current game score is " + str(total_score))
		return 0, total_score, True
	else:
		return round_score, total_score, False

def main():
	round_score = 0
	total_score = 0
	number_ks = 0
	print("Welcome to the game of SKUNK.")
	for letter in 'SKUNK':
		end = False
		print()
		print("Here is the first roll of round " + letter)
		print()
		while end == False:
			dice_1 = randint(1,6)
			dice_2 = randint(1,6)
			print("You rolled a " + str(dice_1) + " and a " + str(dice_2))
			a, b = check_roll(dice_1, dice_2)
			round_score,total_score,end = score(a,b,total_score,round_score)
			print_score(round_score, total_score)
			if round_score != 0:
				round_score, total_score, end = user_decision(round_score, total_score)
		if letter == 'K':
			number_ks += 1
			if number_ks == 2:
				print()
				print("GAME OVER")
				print("Your final score for the game is " + str(total_score))
			else:
				print("Press ENTER to move on to the next round.")
				input()
		else:
			print("Press ENTER to move on to the next round.")
			input()

main()
