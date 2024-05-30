from getpass import getpass
import sqlite3

conn = sqlite3.connect('main.db')
cur = conn.cursor()
line = '-'*40
user_name = None


class Player():
    def fetch_data(self, username) -> None:
        sql = f'SELECT first_name, last_name, user_name, phone_number, age_range FROM player WHERE user_name="{username}"'
        result = cur.execute(sql).fetchall()
        if len(result) == 0:
            print('[PLAYER NOT FOUND!]')
        else:
            for row in result:
                first_name, last_name, user_name, phone_number, age_range = row
                self.set_values(first_name, last_name, user_name, phone_number, age_range)
                
    def set_values(self, first_name, last_name, user_name, phone_number, age_range) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.phone_number = phone_number
        self.age_range = age_range

    def create_username(self) -> str:
        user_name = input('[USERNAME]: ')
        def check_username(username) -> str:
            global user_name
            sql = f'SELECT user_name from player WHERE user_name="{username}"'
            result = cur.execute(sql).fetchall()
            if not result:
                user_name = username
            else:
                logon = input('[USERNAME TAKEN] Login? yes / no: ')
                if logon.lower() == 'yes':
                    self.login()
                else:
                    self.create_username()
            return user_name
        return check_username(user_name)

    def register(self) -> bool:
        first_name = input('[FIRST NAME]: ')
        last_name = input('[LAST NAME]: ')
        user_name = self.create_username()
        if user_name != None:        
            phone_number = int(input('[PHONE NUMBER] (as 26876294516): '))
            age_range = input(
                '[AGE RANGE]\n\t1 --- (-10)\n\t2 --- (10 -> 20)\n\t3 --- (21 -> 30)\n\t4 --- (31 -> 40)\n\t5 --- (40+)\n\t[CHOICE]: ')
            self.set_values(first_name, last_name, user_name,
                            phone_number, age_range)
            password = getpass('[PASSWORD]: ')
            sql = '''INSERT INTO player(first_name, last_name, user_name, phone_number, age_range, password) VALUES(?, ?, ?, ?, ?, ?)'''
            data = (self.first_name, self.last_name, self.user_name,
                    self.phone_number, self.age_range, password)
            cur.execute(sql, data)
            conn.commit()
            return True
        else:
            return False

    def login(self) -> dict[bool, str]:
        login = False
        self.user_name = None
        user_name = input('[USERNAME]: ')
        password = getpass('[PASSWORD]: ')
        sql = f'SELECT user_name, password FROM player WHERE user_name="{user_name}" AND password="{password}"'
        result = cur.execute(sql).fetchall()
        if not result:
            login = False
        else:
            self.user_name = user_name
            login = True        
        return {login, self.user_name} # I will need to use the user_name as the program runs
