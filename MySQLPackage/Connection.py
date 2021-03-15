## Import Mysql-Connector
import mysql.connector

class Connection:
    def __init__(self, host="127.0.0.1", username="", password="", databaseName=""):
        self.host = host
        self.username = username
        self.password = password
        self.databaseName = databaseName
        self.database = None
        self.cursor = None

    def setHost(self, host):
        self.host = host

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def setDatabaseName(self, databaseName):
        self.databaseName = databaseName

    def getHost(self):
        return self.host

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getDatabaseName(self):
        return self.databaseName

    def getDatabase(self):
        return self.database

    def getCursor(self):
        return self.cursor

    def run(self):
        Database = mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.databaseName,
            auth_plugin='mysql_native_password'
        )
        self.database = Database
        self.cursor = Database.cursor()

    def __del__():
        self.database.close()
