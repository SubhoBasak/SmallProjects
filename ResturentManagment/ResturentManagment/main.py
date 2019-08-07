import os
import time
import getch
import sqlite3
import termcolor
from datetime import datetime

tax = 0

class DataBase:
	def __init__(self):
		os.system('clear')
		path = os.path.join(os.environ.get('HOME'), '.resturent_data')
		if not os.path.isdir(path):
			termcolor.cprint('Directory is creating...', 'cyan', attrs = ['bold'])
			os.chdir(os.environ.get('HOME'))
			os.mkdir('.resturent_data')
		os.chdir(path)
		if not os.path.isfile(os.path.join(path, 'resturent_data.db')):
			termcolor.cprint('Database file is creating...', 'cyan', attrs = ['bold'])
		self.connect = sqlite3.connect('resturent_database.db')
		self.cursor = self.connect.cursor()
		self.cursor.execute('''CREATE TABLE IF NOT EXISTS records (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			Date VARCHAR(8),
			Time VARCHAR(8),
			Name VARCHAR(50),
			Orders TEXT,
			Total REAL,
			Tax REAL,
			GrandTotal REAL,
			PayingMethod VARCHAR(20) )''')
		self.cursor.commit()
	
	def add_record(self):
		global tax
		now = datetime.now()
		date = str(now.date())
		time = str(now.time())[:9]

		os.system('clear')
		termcolor.cprint('Name : ', 'yellow', attrs = ['bold'])
		name = input()

		termcolor.cprint('Order : ', 'yellow', attrs = ['bold'])
		order, total = order_scr()
		os.system('clear')

		grand_total = total + tax

		termcolor.cprint('Paying method : ', 'yellow', attrs = ['bold'])
		termcolor.cprint('1. Cash\n2. Card\n3. Mobile banking\n4. eWallet', 'green', attrs = ['bold'])
		inp = getch.getch()
		while inp not in range(1, 5):
			inp = getch.getch()
		if inp == 1:
			pm = 'Cash'
		elif inp == 2:
			pm = 'Card'
		elif inp == 3:
			pm = 'Mobile banking'
		elif inp == 4:
			pm = 'eWallet'
		
		termcolor.cprint('Name : ', 'yellow', end = '', attrs = ['bold'])
		termcolor.cprint(name, 'blue', attrs = ['bold'])
		termcolor.cprint('Order : ', 'yellow', end = '', attrs = ['bold'])
		termcolor.cprint(order, 'blue', attrs = ['bold'])
		termcolor.cprint('Total : ', 'yellow', end = '', attrs = ['bold'])
		termcolor.cprint(total, 'blue', attrs = ['bold'])
		termcolor.cprint('Grand total : ', 'yellow', end = '', attrs = ['attrs'])
		termcolor.cprint(str(total)+' + '+str(tax)+' = '+str(grand_total), 'blue', attrs = ['bold'])

		termcolor.cprint('\n\nDo you reall want to save it ? [y/n]', 'red', attrs = ['bold'])
		if getch.getch() == 'y':
			self.cursor.execute('''INSERT INTO records VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (date, time, name, order, total, tax, grand_total, pm))
			self.connect.commit()
			os.system('clear')
			termcolor.cprint('Record saved.\nPress any key to continue...', 'cyan', attrs = ['bold'])
			getch.getch()

	def view_record(self):
		records = self.cursor.execute('''SELECT * FROM records''');
	
	def delete_record(self):
		pass

def loading_scr():
	os.system('clear')
	col, row = os.get_terminal_size()
	for i in range(row-3):
		if i == 0 or i == row-4:
			termcolor.cprint('#'*col, 'yellow', attrs = ['bold'])
			continue
		termcolor.cprint('#'+' '*(col-3)+'#', 'yellow', attrs = ['bold'])
	termcolor.cprint('Loading...', 'magenta', attrs = ['bold'])
	for i in range(col+1):
		text = termcolor.colored('#'*i, 'green', attrs = ['bold'])
		print('\r'+text, end = '')
		time.sleep(0.01)

def main_menu():
	termcolor.cprint('1. Add new record\n2. View records\n3. Statistics\n4. Settings\n5. Exit', 'green', attrs = ['bold'])
	termcolor.cprint('\nPress q to go back...', 'blue', attrs = ['bold'])
	inp = getch.getch()
	while inp not in range(1, 6) or inp != 'q':
		inp = getch.getch()
	if inp == 1:
		add_record()
	elif inp == 2:
		view_record()
	elif inp == 3:
		statistic()
	elif inp == 4:
		settings()
	elif inp == 5:
		os.system('clear')
		termcolor.cprint('Do you really want to exit? [y/n]', 'red', attrs = ['bold'])
		if getch.getch() == 'y':
			termcolor.cprint('Database disconnecting...', 'cyan', attrs = ['bold'])
			database.connect.close()
			time.sleep(1)
			termcolor.cprint('\n\n\nGood bye....', 'magenta', attrs = ['bold'])
			time.sleep(1)
			os.system('clear')
			exit()

if __name__ == '__main__':
	loading_scr()
	database = DataBase()
	while True:
		main_menu()
