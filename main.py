from database import DataBase
from getpass import getpass

from hashlib import sha256
import sys
import os


enter_menu = ("#"*15 + "\n" +
              "## q => quit program\n" +
              "## sp => set password\n" +
              "## cp => change password\n" +
              "## gp => get password\n" +
              "## gs => get services\n" +
              "## ga => get account\n" +
              "#"*35 + "\n")


def check_password(pss_key):

    pss_hash = '52120eb30a3aba0c70b2a7e0db51bd53969d7ca40f1653f7c110fb49b3e3c221'

    new_hash = sha256(pss_key.encode('utf-8')).hexdigest()

    if new_hash == pss_hash:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Enter Master Password")

    for i in range(3):
        pss = getpass(": ")
        if check_password(pss):
            break
        print("Sorry, type again")
    else:
        sys.exit()

    DB = DataBase("pass_test.db")
    print(enter_menu)

    option = input(": ")

    while option != "q":
        if option == "sp":
            service = input("\tService> ")
            account = input("\tAccount> ")
            pass_key = input("\tKey> ")

            added = DB.add_pass_key(pass_key, service, account)
            if added:
                print("Done!")

        elif option == "cp":
            service = input("\tService> ")
            account = input("\tAccount> ")
            new_key = input("\tNew Key> ")

            change = DB.change_pass_key(new_key, service, account)
            if change:
                print("Changed!")

        elif option == "gp":
            service = input("\tService> ")
            account = input("\tAccount> ")

            result = DB.get_pass_key(service, account)
            if result:
                print(result.fetchone())

        elif option == "gs":
            account = input("\tAccount> ")

            services = DB.get_services(account)
            if services:
                print(services.fetchone())

        elif option == "ga":
            service = input("\tService> ")

            accounts = DB.get_accounts(service)
            if accounts:
                print(accounts.fetchone())

        option = input(": ")


