import sqlite3
import threading

lock = threading.Lock()

class DB:
	def __init__(self, database:str):
		self.connection = sqlite3.connect(database, check_same_thread = False)
		self.cursor = self.connection.cursor()

	# Adding user to database
	def add_user(self, uid:int, un:str, name:str):
		with self.connection:
			with lock:
				return self.cursor.execute("INSERT INTO `user` (`uid`, `un`, `name`) VALUES(?,?,?)", (uid, un, name,))

	# Get user list with limit
	def get_users(self, limit:int=0):
		with self.connection:
			with lock:
				result = self.cursor.execute('SELECT * FROM `user` LIMIT ?', (limit,)).fetchall()
				return result

	# Get definite user
	def get_user(self, uid:int):
		with self.connection:
			with lock:
				result = self.cursor.execute('SELECT * FROM `user` WHERE `uid` = ?', (uid,)).fetchone()
				return result		