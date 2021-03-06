import pymysql


def createNikeTable():
	DB_URL = "localhost"
	DB_USER = "cloutwatch"
	DB_PASS = "psswd"
	database_name = "nike"

	connection = pymysql.connect(host=DB_URL,
							 user=DB_USER,
							 password=DB_PASS,
							 database=database_name,
							 charset='utf8mb4',
							 cursorclass=pymysql.cursors.DictCursor)

	with connection.cursor() as cursor:
		try:
			cursor.execute("CREATE TABLE IF NOT EXISTS data (name TEXT, price TEXT, link TEXT, available TEXT, unavailable TEXT)")
			connection.commit()
		except Exception as e:
			print(e)

createNikeTable()