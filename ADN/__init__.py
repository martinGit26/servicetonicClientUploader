import json
import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

class db:
    cursor = ""
    def __init__ (self):
        db = self.read_conf()
        print(db)
        cnx = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+db['server']+';DATABASE='+db['database']+';UID='+db['username']+';PWD='+db['password'])
        self.cursor = cnx.cursor()
        self.read_conf()


    def read_conf (self):
        with open('./ADN/database.json') as f:
            db = json.load(f)
        
        return db
        
    def read_clients(self):
        self.cursor.execute("SELECT * FROM servicetonic")
        row = self.cursor.fetchone()
        while row:
            print(row)
            row = self.cursor.fetchone()



        
        




#server = 'tcp:myserver.database.windows.net' 
#database = 'servicetonic' 
#username = '' 
#password = 'mypassword' 
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
#cursor = cnxn.cursor()
