import time
from datetime import date, datetime
from player import Player

line = '-'*50
cur_time = datetime.now()
today = date.today()
player = Player()

# the login from the main class(it invokes the player login)
def login():
	if player.login():
		start_game()
	else:
		print('Login Failure') # if the player failed to login, let  him to register
		register = input('New to the program? [yes / no]: ').lower()
		if register == 'yes':
			player.register()
		else:
			login()

def start_game():
	print(f'Now Starting the Game')
	quit_game()
def quit_game():
	quit_game = input('Do you wanna quit? [yes / no]: ').lower()
	if quit_game == 'yes':
		game_over_screen()
	else:
		welcome_player()

def game_over_screen() -> None:
	print('-- Game Over --')
	print('Your Scores: ')

def welcome_player() -> None:
	print(f'{line}\n\t--- Welcome Player ---\n{line}\nHope you enjoy playing the game ahead!\n')
	print(f'{line}\n--- [DATE] {today} --- [TIME] {cur_time.hour}:{cur_time.minute}:{cur_time.second} ---\n{line}\n')
	register = input('New to the program? [yes / no]: ').lower()
	if register == 'yes':
		if player.register():
			login()
	elif register == 'no':
		login()
	else:
		print('Wrong User input')
		welcome_player()

welcome_player()
