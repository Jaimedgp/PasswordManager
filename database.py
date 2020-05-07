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
        try:
            self.create_database()
        except:
            print("Dabase exists")


    def create_database(self):
        """ Create the database and tables to save passwords """

        # Table with passwords and accounts information
        self.connect.execute("""
CREATE TABLE PASS_KEY
    idpass INTEGER NOT NULL,
    pass_key VARCHAR(200) NOT NULL UNIQUE,
    service VARCHAR(200) NOT NULL,
    account VARCHAR(200) NOT NULL,

    PRIMARY KEY (idpass),

    CONSTRAINT unq_srvc-accnt UNIQUE (service, account);
""")


    def get_pass_key(self, service, account):
        """ Get pass_key value for a certain service and account """

        pass_key = self.connect.execute("""
SELECT pass_key
    FROM PASS_KEY pssKy
    WHERE pssKy.service = %s AND pssKy.account = %s;
""" %(service, account))

        return pass_key
