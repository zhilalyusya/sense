import os
import sqlite3
from datetime import datetime
from logger import LOG

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'minds.sqlite3')

def db_connect(db_path = DEFAULT_PATH):
	try:
		con = sqlite3.connect(db_path)
		return con
	except Exception as e:
		LOG.info(e)
		LOG.info(traceback.format_exc())
	return None

# create temperature_humidity table
# function should only be used the first time this script is run
# when the temperature_humidity table doesn't exist yet
def create_temperature_humidity_tb(con):
	temperature_humidity_tb = '''
	CREATE TABLE IF NOT EXISTS temperature_humidity (
		id INTEGER NOT NULL PRIMARY KEY,
		temperature REAL,
		humidity REAL,
		`timestamp` TEXT
	)
	'''
	cur = con.cursor()
	cur.execute(temperature_humidity_tb)
	LOG.info('temperature_humidity table created.')

def insert_temp_humid(con, temp, humid):
	timestamp_now = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

	insert = '''
	INSERT INTO temperature_humidity (temperature, humidity, `timestamp`)
	VALUES (?, ?, ?)
	'''
	cur = con.cursor()

	# handle if temperature_humidity table doesn't exist in DB
	first_try = True
	while first_try is True:
		try:
			cur.execute(insert, (temp, humid, timestamp_now))
			LOG.info('temperature and humidity data inserted into temperature_humidity table.')
		except sqlite3.OperationalError as e:
			LOG.info(e)
			create_temperature_humidity_tb(con)
		else:
			first_try = False