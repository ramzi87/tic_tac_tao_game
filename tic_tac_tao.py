
from __future__ import print_function

game = []

for x in range(1,10):
	game.append(str(x))

start_game = True
find_player = False

def game_board():
	print ("\n -------------")
	print (' | ' + game[0] + ' | ' + game[1] + ' | ' + game[2] + ' | ')
	print (" -------------")
	print (' | ' + game[3] + ' | ' + game[4] + ' | ' + game[5] + ' | ')
	print (" -------------")
	print (' | ' + game[6] + ' | ' + game[7] + ' | ' + game[8] + ' | ')
	print (" -------------")

while not find_player:
	game_board()

	if start_game:
		print ("Player number '1' :")
	else:
		print ("Player number '2' :")

	try:
		my_choice = int(input(">>>> "))
	except:
		print ("Invalid caracter ! Only numbers are accepted")
		continue

	if game[my_choice-1] == 'X' or game[my_choice-1] == 'O':
		print ("This case is already taken, try again")
		continue

	if start_game:
		game[my_choice-1] = 'X'
	else:
		game[my_choice-1] = 'O'

	start_game = not start_game

	for i in range(0,3):
		n = i * 3
		if (game[n] == game[n+1] and game[n] == game[n+2]):
			find_player = True
			game_board()

		if (game[i] == game[i+3] and game[i] == game[i+6]):
			find_player = True
			game_board()

		if ((game[0] == game[4] and game[0] == game[8]) or
			(game[2] == game[4] and game[2] == game[6])):
		    find_player = True
		    game_board()

print ("Congratulations Player "+str(int(start_game+1))+" Wins !!")
