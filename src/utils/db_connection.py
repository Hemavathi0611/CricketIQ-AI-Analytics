import mysql.connector


def get_connection():

    connection = None

    try:
        print("🔄 Trying to connect to MySQL...")

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="python@1234",
            database="cricketiq_analytics",
            port=3306,
            connection_timeout=10,
            use_pure=True
        )

        if connection.is_connected():
            print("✅ Python connected to MySQL successfully!")
            return connection

        print("❌ MySQL connection was not established.")
        return None

    except mysql.connector.Error as error:
        print("❌ MySQL connection failed:")
        print(error)
        return None