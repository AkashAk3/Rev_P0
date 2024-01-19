import mysql.connector

class Connection:
    def connec(self):
        host = "localhost"
        user = "root"
        password = "Imraina@03"
        database="rev"

        conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
        return conn