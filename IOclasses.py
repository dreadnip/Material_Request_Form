# ------------------------------------------------------------------------ #
# Title:
# Description:
# ChangeLog (Who,When,What):
# Acompeau, <date>, created file
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")


class IO:
    """  A class for performing Item Input and Output

       methods:

           print_menu_items():

           input_menu_choice():


       """
    @staticmethod
    def print_menu_items():
        """ Print a menu of choices to the user  """
        print('''
        Menu of Options
        1) ENTER ITEM
        2) SHOW LIST OF ITEMS
        3) PRODUCE MRF
        4) SAVE, CLOSE, AND EMAIL MRF
        5) 
        ''')
        print()  # Add an extra line for looks

    # TODO: error handling if the user does not enter a valid menu choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice


    @staticmethod
    def input_item_data():
        """ Gets data for an item object

        :return: (item) object with input data
        """
        try:
            gageid = (input("GAGE ID#: ").strip())
            price = str(input("PRICE: ")).strip()
            quantity = str(input('QUANTITY: ')).strip()
            print()  # Add an extra line for looks
            # thing = Data.Item(gageid, model_num, serial_num, mfg, desc, price, quantity)
        except Exception as e:
            print(e)
        return new_item