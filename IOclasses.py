# ------------------------------------------------------------------------ #
# Title:
# Description:
# ChangeLog (Who,When,What):
# Acompeau, <date>, created file
# ------------------------------------------------------------------------ #
from query import QueryGage as q
from Data import Item

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
            gageid = input("GAGE ID#: ").strip().upper()
            Item.price = str(input("PRICE: ")).strip()
            Item.quantity = str(input('QUANTITY: ')).strip()
            asset = q.fetch(gageid)
            # unpack tuple
            (Item.gage_id, Item.desc, Item.company, Item.serial_num, Item.mfg,
             Item.model_num, Item.cert_template) = asset
            # hydrate Item object
            # new_item = Item(gage_id, model_num, serial_num, manufacturer, desc, company,
            #                 cert_template, price, quantity)
            # new_item2 = [Item.gage_id, Item.desc, Item.company, Item.serial_num, Item.mfg,
            #              Item.model_num, Item.cert_template, Item.price, Item.quantity]
            print()  # Add an extra line for looks

        except Exception as e:
            print(e)

        # todo: figure out how to return a list by calling the object
        return [Item.gage_id, Item.desc, Item.company, Item.serial_num, Item.mfg,
                Item.model_num, Item.cert_template, Item.price, Item.quantity]

    # get gage_id for isolated use in other modules
    @staticmethod
    def get_gage_id():
        gage_id = input("Gage ID: ").strip().upper()
        return gage_id
