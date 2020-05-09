import sqlite3

class DataBase():
    """
        Manage DataBase tables where safe passwords, accounts, services,...

        @autor Jaimedgp
        @date May, 2020
    """

    def __init__(self, database):
        """ Connect to database """

        self.connect = sqlite3.connect(database)

        # Check if database exists yet
        result = self.create_database()
        if result == 0:
            print("Dabase exists")


    def create_database(self):
        """ Create the database and tables to save passwords """

        try:
            self.connect.execute("""
CREATE TABLE PASS_KEY (
    idpass INTEGER PRIMARY KEY AUTOINCREMENT,
    pass_key VARCHAR(200) NOT NULL UNIQUE,
    service VARCHAR(200) NOT NULL,
    account VARCHAR(200) NOT NULL,

    CONSTRAINT unq_srvc_accnt UNIQUE (service, account)
    ); """)
        except:
            return 0


    def get_pass_key(self, service, account):
        """ Get pass_key value for a certain service and account """

        try:
            pass_key = self.connect.execute("""
SELECT pass_key
    FROM PASS_KEY pssKy
    WHERE pssKy.service = '%s' AND pssKy.account = '%s';
""" %(service, account))

            return pass_key
        except:
            return 0


    def add_pass_key(self, pass_key, service, account):
        """ Add a new pass_key into database """

        try:
            self.connect.execute("""
INSERT INTO PASS_KEY(pass_key, service, account)
    VALUES ('{0}', '{1}', '{2}');
""".format(pass_key, service, account))
        except:
            return 0
