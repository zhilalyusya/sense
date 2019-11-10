from logger import LOG

# get sensor date
def get_temp_humid_data():
	temp = 30.15
	humid = 40.17
	LOG.info('get temperature and humidity data.')
	return temp, humid