from random import randint
import easygui

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

def print_score(round_score, total_score, print_dice):
	round_print = "\nYour score for this round is " + str(round_score)
	game_print = "\nYour total score for the game is " + str(total_score)
	easygui.msgbox("Round over\n" + print_dice + round_print + game_print)

def user_decision(round_score, total_score, roll_message):
	answer = easygui.buttonbox(roll_message + "\nYour round score is " + str(round_score) + "\nYour total score is " + str(total_score) + "\nBank your points and move on to the next round or roll again?",
	choices = ['Keep points and go to next round','Roll again'])
	if answer == 'Keep points and go to next round':
		total_score += round_score
		easygui.msgbox("Your current game score is " + str(total_score))
		return 0, total_score, True
	else:
		return round_score, total_score, False

def main():
	game_play = True
	while game_play == True:
		round_score = 0
		total_score = 0
		number_ks = 0
		easygui.msgbox("Welcome to the game of SKUNK.")
		for letter in 'SKUNK':
			end = False
			easygui.msgbox("Here is the first roll of round " + letter, ok_button ="Let's Play!")
			while end == False:
				dice_1 = randint(1,6)
				dice_2 = randint(1,6)
				roll_message = ("You rolled a " + str(dice_1) + " and a " + str(dice_2))
				a, b = check_roll(dice_1, dice_2)
				round_score,total_score,end = score(a,b,total_score,round_score)
				if round_score != 0:
					round_score, total_score, end = user_decision(round_score, total_score, roll_message)
					print_dice = ''
				else:
					print_dice = roll_message
					print_score(round_score, total_score, print_dice)
			if letter == 'K':
				number_ks += 1
				if number_ks == 2:
					if easygui.ynbox("GAME OVER\n" + "Your final score for the game is " + str(total_score) + "\n Would you like to play again?"):
						pass
					else:
						game_play = False

main()
