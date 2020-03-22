# ------------------------------------------------------------------------ #
# Title:
# Description:
# ChangeLog (Who,When,What):
# Acompeau, <date>, created file
# ------------------------------------------------------------------------ #
from Errors import *
# todo: define errors
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")


class IO:
    """  A class for performing Input and Output

       methods:

           print_menu_items(): prints the menu items

           input_menu_choice(): asks user for choice input, returns choice

           get_gage_id(): gets gage ID

           get_price(): gets price

           get_quantity(): gets number of that particular item

           get_vendor(): gets the vendor the item is being shipped to

           get_user_info(): gets users initials and users full name




       """

    @staticmethod
    def print_menu_items():
        """ Print a menu of choices to the user  """
        print('''
        Menu of Options
        1) ENTER ITEM
        2) SHOW LIST OF ITEMS
        3) DELETE ITEM FROM LIST
        4) WRITE MRF
        5) SAVE AND QUIT
        ''')
        print()  # Add an extra line for looks

    # TODO: error handling if the user does not enter a valid menu choice. read up on error handling
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        try:
            choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
            if choice in ['1', '2', '3', '4', '5']:
                print()  # Add an extra line for looks
                return choice
        except NotValidInput:
            print("try again")

    @staticmethod
    def get_gage_id():
        """Gets gage ID from the user
        :return string """
        try:
            gage_id = input("Gage ID: ").strip().upper()
            return gage_id
        except Exception as e:
            print(e)

    @staticmethod
    def get_price():
        try:
            price = float(input("Price: ").strip())
            return price
        except ValueError:
            print("Value must be a number! Please try again")

    @staticmethod
    def get_quantity():
        try:
            quantity = int(input("Quantity: ").strip())
            return quantity
        except ValueError:
            print("Value must be a number! Please try again")

    @staticmethod
    def get_vendor():
        try:
            vendor = input("Vendor name: ").upper().strip()
            return vendor
        except Exception as e:
            print(e)

    @staticmethod
    def get_user_info():
        try:
            initials = input("Initials: ").upper().strip()
            full_name = input("Full Name: ").upper().strip()
            return initials, full_name
        except Exception as e:
            print(e)

