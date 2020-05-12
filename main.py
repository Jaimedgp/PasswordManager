"""
    Main module with all the UI functions to become
    the database interaction more beautyful

    @author Jaimedgp
    @date May, 2020
"""

import sys
import os

from getpass import getpass

from KyManager.database import DataBase
from KyManager.password import check_password, check_private_key
from KyManager.password import create_pass_key


ENTER_MENU = ("#"*25 + "\n" +
              "## q => quit program\n" +
              "## sp => set password\n" +
              "## cp => change password\n" +
              "## rp => remove password\n" +
              "## gp => get password\n" +
              "## gs => get services\n" +
              "## ga => get account\n" +
              "## gall => get all acounts and services\n" +
              "##\n" +
              "## help => Get help menu again\n" +
              "#"*35 + "\n")


def enter_password():
    """ Enter master password to run program """

    print("Enter Master Password")

    for _ in range(3):
        pss = getpass(": ")
        if check_password(pss):
            break
        print("Sorry, type again")
    else:
        return False

    return True


def print_result(results):
    """ Print the results of a database consult """

    print()
    for i, name in enumerate(results.fetchall()):
        print("\t{0}) ".format(i+1) + " -> ".join(name))


def set_passkey(database):
    """ UI to set a new password """

    service = input("\tService> ")
    account = input("\tAccount> ")
    pass_key = input("\tAuto-generate?[y/n]> ")

    if pass_key in ["y", "yes", "s", "si", "Y", "Yes"]:
        pass_key = create_pass_key()
    else:
        pass_key = input("\t\tKey> ")

    added = database.add_pass_key(pass_key, service.lower(), account)
    if added:
        print()
        print("\tDone!")


def change_passkey(database):
    """ UI to change a password """

    service = input("\tService> ")
    account = input("\tAccount> ")
    new_key = input("\tNew Key> ")

    change = database.change_pass_key(new_key, service.lower(), account)
    if change:
        print()
        print("\tChanged!")


def remove_passkey(database):
    """ UI to remove a password """

    service = input("\tService> ")
    account = input("\tAccount> ")

    removed = database.remove_pass_key(service.lower(), account)
    if removed:
        print()
        print("\tDeleted!")


def get_passkey(database):
    """ UI to get a password """

    service = input("\tService> ")
    account = input("\tAccount> ")

    pass_key = database.get_pass_key(service.lower(), account)
    if pass_key:
        print_result(pass_key)


def get_service(database):
    """ UI to get services """

    account = input("\tAccount> ")

    services = database.get_services(account)
    if services:
        print_result(services)


def get_account(database):
    """ UI to get accounts """

    service = input("\tService> ")

    accounts = database.get_accounts(service.lower())
    if accounts:
        print_result(accounts)


if __name__ == '__main__':

    IS_MASTER_KEY = enter_password()

    if IS_MASTER_KEY:
        DB = DataBase("pass_test.db")

        IS_PRIVATE_KEY = check_private_key(input("Private Key File: "),
                                           DB.get_master_key().fetchone()[0])

                #private_key_file, master_hash)

        if not IS_PRIVATE_KEY:
            sys.exit()
        os.system('cls' if os.name == 'nt' else 'clear')

        print(ENTER_MENU)
        OPTION = input(": ")

        while OPTION != "q":
            if OPTION == "sp":
                set_passkey(DB)
            elif OPTION == "cp":
                change_passkey(DB)
            elif OPTION == "rp":
                remove_passkey(DB)
            elif OPTION == "gp":
                get_passkey(DB)
            elif OPTION == "gs":
                get_service(DB)
            elif OPTION == "ga":
                get_account(DB)
            elif OPTION == "gall":
                RESULT = DB.get_all()
                if RESULT:
                    print_result(RESULT)
            elif OPTION in ["help", "Help"]:
                print(ENTER_MENU)

            OPTION = input(": ")
