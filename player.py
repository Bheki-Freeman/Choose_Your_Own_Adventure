import sqlite3

conn = sqlite3.connect('main.db')
cur = conn.cursor()
line = '-'*40


class Player():
	def set_values(self, first_name, last_name, user_name, phone_number, age_range) -> None:
		self.first_name = first_name
		self.last_name = last_name
		self.user_name	=user_name
		self.phone_number = phone_number
		self.age_range = age_range

	def register(self) -> bool:
		print(f'Registering Now')
		first_name = input('[FIRST NAME]: ')
		last_name = input('[LAST NAME]: ')
		user_name = input('[USERNAME]: ')
		check_username(user_name)
		phone_number = int(input('[PHONE NUMBER] (as 26876294516): '))
		age_range = input('[AGE RANGE]\n\t1 --- (-10)\n\t2 --- (10 -> 20)\n\t3 --- (21 -> 30)\n\t4 --- (31 -> 40)\n\t5 --- (40+)\n\t[CHOICE]: ')
		self.set_values(first_name, last_name, user_name, phone_number, age_range)
		return True
	def login(self) -> bool:
		print(f'Login Now')
		return True
