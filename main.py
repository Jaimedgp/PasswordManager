from KyManager.database import DataBase
from KyManager.Password import check_password, create_pass_key
from getpass import getpass

import sys
import os


enter_menu = ("#"*25 + "\n" +
              "## q => quit program\n" +
              "## sp => set password\n" +
              "## cp => change password\n" +
              "## gp => get password\n" +
              "## gs => get services\n" +
              "## ga => get account\n" +
              "## gall => get all acounts and services\n" +
              "#"*35 + "\n")


def print_result(result):
    """ Print the results of a database consult """

    print()
    for i, name in enumerate(result.fetchall()):
        print("\t{0}) ".format(i+1) + " -> ".join(name))


if __name__ == '__main__':
    print("Enter Master Password")

    for j in range(3):
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
            pass_key = input("\tAuto-generate?[y/n]> ")

            if pass_key in ["y", "yes", "s", "si", "Y", "Yes"]:
                pass_key = create_pass_key()
            else:
                pass_key = input("\t\tKey> ")

            added = DB.add_pass_key(pass_key, service.lower(), account)
            if added:
                print()
                print("\tDone!")

        elif option == "cp":
            service = input("\tService> ")
            account = input("\tAccount> ")
            new_key = input("\tNew Key> ")

            change = DB.change_pass_key(new_key, service.lower(), account)
            if change:
                print()
                print("\tChanged!")

        elif option == "gp":
            service = input("\tService> ")
            account = input("\tAccount> ")

            result = DB.get_pass_key(service.lower(), account)
            if result:
                print_result(result)

        elif option == "gs":
            account = input("\tAccount> ")

            services = DB.get_services(account)
            if services:
                print_result(services)

        elif option == "ga":
            service = input("\tService> ")

            accounts = DB.get_accounts(service.lower())
            if accounts:
                print_result(accounts)

        elif option == "gall":
            result = DB.get_all()
            if result:
                print_result(result)

        option = input(": ")
