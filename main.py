from utils import db_connect, insert_temp_humid
from get_sensor_data import get_temp_humid_data

def main():
	temp, humid = get_temp_humid_data()

	con = db_connect()
	if con is not None:
		insert_temp_humid(con, temp, humid)
		con.commit()
	con.close()

if __name__ == "__main__":
	main()