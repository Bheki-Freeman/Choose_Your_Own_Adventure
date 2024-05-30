import time
from datetime import date, datetime
from player import Player

line = '-'*50
cur_time = datetime.now()
today = date.today()
player = Player()

# the login from the main class(it invokes the player login)


def login():
    login_status, login_user_name = player.login()
    if login_status:
        time.sleep(1)
        player.fetch_data(login_user_name)
        start_game()
    else:
        # if the player failed to login, let  him to register
        time.sleep(1)
        print(f'{line}\n\t--- [ACCESS DENIED!] ---\n{line}\n')
        register = input('New to the program? [yes / no]: ').lower()
        if register == 'yes':
            registar()
        else:
            login()


def registar() -> None:
    if player.register():
        print('[REGISTRATION SUCCESSFUL]')
        login()
    else:
        print('[REGISTRATION ABORTED!]')


def start_game():
    print(f'{line}\n\t ---- [GAME STARTED] -----\n{line}\n')
    print(f'>>GREETINGS {player.first_name} Where Do we Start?')
    start = int(input(
        '\t1 ---- Go Town\n\t2 ---- Stay Home\n\t3 ---- Go to the Farm\n\t4 ---- Feeling In Love\n\t0 ---- Menu\n\t[CHOICE]: '))
    if start == 1:
        go_town()
    elif start == 2:
        stay_home()
    elif start == 3:
        go_to_farm()
    elif start == 4:
        feeling_in_love()
    elif start == 0:
        game_over_screen()
        quit()
    else:
        print('[ERROR]: Wrong user input!')
        start_game()


def go_town():
    print('Going to town')


def stay_home():
    print('Staying Home')


def go_to_farm():
    print('Going to the Farm')


def feeling_in_love():
    print('Do you really have a Lover?')


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
    print(
        f'{line}\n--- [DATE] {today} --- [TIME] {cur_time.hour}:{cur_time.minute}:{cur_time.second} ---\n{line}\n')
    register = input('New to the program? [yes / no]: ').lower()
    if register == 'yes':
        registar()
    elif register == 'no':
        login()
    else:
        print('Wrong User input')
        welcome_player()


welcome_player()
