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
        print(
            f'\n>>{player.first_name} You have a problem, you just met THUGS in the robot!')
        traffic_issue = input(
            'They want the car and Money, what do you do?\n>>\tJUMPROBOT or SUBMIT or FIGHT!: ').lower()
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
    fight()

def fight() -> None:
    print('>>[DANGER!] Fighting with thugs is not advisable UNLESS YOU KNOW WHAT YOU\'RE DOING!')
    print('While fighting, one thug just held you on power grip, what do you do?')
    action = int(input('\t1. Hit him with your right elbow\n\t2. Push his hands off your neck\n\t[CHOICE]: '))
    if action == 1:
        print('[GOOD MOVE]: Just dispowered him, he\'s now down, holding his stomach!')
        action = input('Type "Grab the car", to grab the car and run away: ')
        if action.strip().lower() == 'grab the car':
            print('[LUCKY ESCAPE!] You just escaped: Running to town!')
        else:
            print('[CHECK MATE!]: You are just too slow, you have been hardly hit!')
            print('You Loose a point !!')
            fight()
    else:
        print('[FAILED!] You can\'t get off from vice-grip like that: YOU LOST!')
        print('You lose a point!')
        fight()
def submit() -> None:
    time.sleep(1)
    print('>>[LOOSER!] You have just lost your car, Thugs slapped you!')
    choice = input(
        f'\n>>{player.first_name} You now have two choices HIKEBACKHOME or HIKETOTOWN!: ').lower()
    if choice == 'hikebackhome':
        print('Returning back home!')
    elif choice == 'hiketotown':
        print('Your fighting spirit is revived! You chose to continue with your trip!!')
        print('Here comes a Truck, it goes the same direction with you (town), and it just takes you!')
        print(">>[ARRIVED AT TOWN]: you just meet your friends!")
        action = input(
            '>>\tSo, what are you doing with your friends? (GO EATING or GO SKATING or GO GAMING)').lower()
        match (action):
            case 'go eating':
                go_eating()
            case 'go skating':
                go_skating()
            case 'go gaming':
                go_gaming()
            case _:
                print('[ERROR] Please type exactly the actions!')
                submit()
    else:
        print('>>[WRONG USER INPUT] Please type in choice as is like HIKEBACKHOME!')
        submit()
def go_skating() -> None:
    print('Going   Skating!')
def go_gaming() -> None:
    print('Going Gaming!')

def go_eating() -> None:
    restaurants = ['Mt Cafe', 'City Center Foods', 'The Winner\'s Kitchen']
    print('We have the following restaurants with us: ')
    print(f'>>\t{" | ".join(restaurants)}')
    restaurant = input('[CHOOSE ONE]: ').strip().lower()
    if restaurant == restaurants[0].lower():
        print(f'>>\tSo, you chose the {restaurant} Going there!')        
        time.sleep(1)
        menu_list = int(input(f'{line}\n \t MAKE A CHOICE \n{line}\n1. Fried Chicken Curry\n'
                              '2. Boiled Steak\n3. Jelof Rice and Chicken'))
        match (menu_list):
            case 1:
                print('Fried Chicked is being prepared for your!')
            case 2:
                print(f'Boiled Steak being prepared for you!')
            case 3:
                print(f'Jolof Rice and Chicked being prepared for you!')                    
            case _:
                print('[WRONG USER INPUT!] ')
                go_eating()
    elif restaurant == restaurants[1].lower():
        print(f'>>\tSo, you chose the {restaurant} Going there!')        
        time.sleep(1)
        menu_list = int(input(f'{line}\n \t MAKE A CHOICE \n{line}\n1. Ice Cream : E15.99\n'
                              '2. Ice Pops : E10.99\n3. Liquid Jelly : E20.99\n[CHOICE]: '))
        match (menu_list):
            case 1:
                t_cash = float(input("Type your Payment here: "))
                if t_cash < 15.99:
                    top_up = float(input(f'You money {t_cash} is less than E15.99, Please add E{15.99 - t_cash:.2f}: '))                                                           
                    print(f'You have just added {top_up} and the money is now E{top_up + t_cash:.2f}')
                    print(f'Your change is : E{(t_cash + top_up) - 15.99:.2f}')
                else:
                    print(f'Your Ice cream is prepared! Change is E{t_cash-15.99:.2f}')
            case 2:
                t_cash = float(input("Type your Payment here: "))
                if t_cash < 10.99:
                    top_up = float(input(f'You money {t_cash} is less than E10.99, Please add E{10.99 - t_cash:.2f}: '))                                                           
                    print(f'You have just added {top_up} and the money is now E{top_up + t_cash:.2f}')
                    print(f'Your change is : E{(t_cash + top_up) - 10.99:.2f}')
                else:
                    print(f'Your Ice cream is prepared! Change is E{t_cash-10.99:.2f}')
            case 3:
                t_cash = float(input("Type your Payment here: "))
                if t_cash < 20.99:
                    top_up = float(input(f'You money E{t_cash} is less than E20.99, Please add E{20.99 - t_cash:.2f}: '))                                                           
                    print(f'You have just added {top_up} and the money is now E{top_up + t_cash:.2f}')
                    print(f'Your change is : E{(t_cash + top_up) - 20.99:.2f}')
                else:
                    print(f'Your Ice cream is prepared! Change is E{t_cash-20.99:.2f}')
            case _:
                print('[WRONG USER INPUT!]')   
                go_eating()                 


def jump_robot() -> None:  # If the player decides to ignore the robot and run away with his car
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
    register = input('New to the program? [yes / no]: ').strip().lower()
    if register == 'yes':
        registar()
    elif register == 'no':
        login()
    else:
        print('Wrong User input')
        welcome_player()


welcome_player()
