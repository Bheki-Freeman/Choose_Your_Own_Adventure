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
    print('\n\t --- Going to town --- ')
    drive = input('>> [DRIVING?] (yes / no): ')
    if drive.lower() == 'yes':
        mood = int(input('>> [MOOD] (1 -> happy, 2 -> sad, 3 -> angry): '))
        if mood == 1:
            print('[WONDERFUL] You will have a lovely day ahead!')
        elif mood == 2:
            print('[NOT GOOD] If you continue like this, you will have a bad day!')
        elif mood == 3:
            print('[BAD DAY ALREADY!] You already have a bad day!!')
        else:
            print('Wrong user input!')
            go_town()
        time.sleep(1)
        print(f'\n>>{player.first_name} You have a problem, you just met THUGS in the robot!')
        traffic_issue = input('They want the car and Money, what do you do?\n>>\tJUMPROBOT or SUBMIT or FIGHT!: ').lower()
        if traffic_issue == 'jumprobot':
            jump_robot()
        elif traffic_issue == 'submit':
            submit()
        elif traffic_issue == 'fight':
            fight()
        else:
            print('>>[WRONG USER INPUT!] Please type choice as it like JUMPROBOT!')
            go_town()
    else:
        print('>>[PUBLIC TRANS THUMBS UP!!] You are saving our nature!!')
def fight() -> None:
    print('>>[DANGER!] Fighting with thugs is not advisable UNLESS YOU KNOW WHAT YOU\'RE DOING!')

def submit() -> None:
    time.sleep(1)
    print('>>[LOOSER!] You have just lost your car, Thugs slapped you!')
    choice = input(f'\n>>{player.first_name} You now have two choices HIKEBACKHOME or HIKETOTOWN!: ').lower()
    if choice == 'hikebackhome':
        print('Returning back home!')
    elif choice == 'hiketotown':
        print('Your fighting spirit is revived! You chose to continue with your trip!!')
    else:
        print('>>[WRONG USER INPUT] Please type in choice as is like HIKEBACKHOME!')
        submit()

def jump_robot() -> None: # If the player decides to ignore the robot and run away with his car
    print('[DANGER!] You have just run over a thug\'s foot, and you have hit the Robot\'s pole!!')
    time.sleep(1)
    choice = input('[WHAT DO YOU DO?] \n>>\tCALLPOLICE or RUNAWAY: ').lower()
    if choice == 'callpolice':
        print('Calling 911')
    elif choice == 'runaway':
        print('Running Away!!')
    else:
        print('[WRONG USER INPUT!] Please type choice as is like CALLPOLICE!')
        jump_robot()

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
