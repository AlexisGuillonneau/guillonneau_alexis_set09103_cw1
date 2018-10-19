import sqlite3 as sql

def get_all_data():
	with sql.connect("database.db") as db:
		c = db.cursor()
		try:
			c.execute("SELECT * FROM movie;")
		except sql.DatabaseError as err:
			print("Error when accessing the database: '{}'".format(err))
		res = c.fetchall()
		return res

def get_abstract(name):
	with sql.connect("database.db") as db:
		c = db.cursor()
		try:
			c.execute("SELECT abstract WHERE Name="+name+";")
		except sql.DatabaseError as err:
			print("Error when accessing the database: '{}'".format(err))
		res = c.fetchone()
		if res is not None:
			return res[0]
		else:
			return res

def get_author(name):
	with sql.connect("database.db") as db:
		c = db.cursor()
		try:
			c.execute("SELECT author WHERE Name="+name+";")
		except sql.DatabaseError as err:
			print("Error when accessing the database: '{}'".format(err))
		res = c.fetchone()
		if res is not None:
			authors = res[0]
			return authors.split(";")
		else:
			return res

def get_data_carousel():
	with sql.connect("database.db") as db:
		c = db.cursor()
		try:
			c.execute("SELECT Name, Abstract,Director,Year,Image FROM movie;")
		except sql.DatabaseError as err:
			print("Error when accessing the database: '{}'".format(err))
		res = c.fetchall()
		return res

def get_all_categories():
	with sql.connect("database.db") as db:
		c = db.cursor()
		try:
			c.execute("SELECT Categories FROM movie;")
		except sql.DatabaseError as err:
			print("Error when accessing the database: '{}'".format(err))
		res = c.fetchall()
		tab = []
		for r in res:
			current = list(r)
			current = current[0].split(";")
			for n in current:
				if n not in tab:
					tab.append(n)
		return tab

def get_from_category(cat):
	with sql.connect("database.db") as db:
		c = db.cursor()
		res = []
		try:
			c.execute("SELECT * FROM movie WHERE Categories LIKE '%"+cat+"%';")
		except sql.DatabaseError as err:
			print("Error when accessing the database: '{}'".format(err))
		res.append(c.fetchall())
		try:
			c.execute("SELECT Image FROM movie WHERE Categories LIKE  '%"+cat+"%';")
		except sql.DatabaseError as err:
			print("Error when accessing the database: '{}'".format(err))
		r = c.fetchall()
		tab = []
		for t in r:
			tab.append(t[0])
		res.append(tab)
		return res

def get_movie(name):
	with sql.connect("database.db") as db:
		c = db.cursor()
		try:
			c.execute("SELECT * FROM movie WHERE Name='"+name+"';")
		except sql.DatabaseError as err:
			print("Error when accessing the database: '{}'".format(err))
		res = c.fetchone()
		return res

def get_all_actors():
	with sql.connect("database.db") as db:
		c = db.cursor()
		try:
			c.execute("SELECT actors FROM movie;")
		except sql.DatabaseError as err:
			print("Error when accessing the database: '{}'".format(err))
		res = c.fetchall()
		tab = []
		for row in res:
			row = list(row)
			data = row[0].split(";")
			for d in data:
				if d not in tab:
					tab.append(d)
		return tab

def get_all_data_for_year(year):
	with sql.connect("database.db") as db:
		c = db.cursor()
		try:
			c.execute("SELECT * FROM movie WHERE year="+str(year)+";")
		except sql.DatabaseError as err:
			print("Error when accessing the database: '{}'".format(err))
		res = c.fetchall()
		return res

def get_all_data_for_actor(actor):
	with sql.connect("database.db") as db:
		c = db.cursor()
		try:
			c.execute("SELECT * FROM movie WHERE actors LIKE '%"+actor+"%';")
		except sql.DatabaseError as err:
			print("Error when accessing the database: '{}'".format(err))
		res = c.fetchall()
		return res

def get_all_data_for_country(country):
	with sql.connect("database.db") as db:
		c = db.cursor()
		try:
			c.execute("SELECT * FROM movie WHERE country LIKE '%"+country+"%';")
		except sql.DatabaseError as err:
			print("Error when accessing the database: '{}'".format(err))
		res = c.fetchall()
		return res

def get_all_data_from_producer(producer):
	with sql.connect("database.db") as db:
		c = db.cursor()
		try:
			c.execute("SELECT * FROM movie WHERE producer LIKE '%"+producer+"%';")
		except sql.DatabaseError as err:
			print("Error when accessing the database: '{}'".format(err))
		res = c.fetchall()
		return res

def get_all_data_from_distribution(distribution):
	with sql.connect("database.db") as db:
		c = db.cursor()
		try:
			c.execute("SELECT * FROM movie WHERE distribution LIKE '%"+distribution+"%';")
		except sql.DatabaseError as err:
			print("Error when accessing the database: '{}'".format(err))
		res = c.fetchall()
		return res

def get_all_data_from_director(director):
	with sql.connect("database.db") as db:
		c = db.cursor()
		try:
			c.execute("SELECT * FROM movie WHERE director LIKE '%"+director+"%';")
		except sql.DatabaseError as err:
			print("Error when accessing the database: '{}'".format(err))
		res = c.fetchall()
		return res