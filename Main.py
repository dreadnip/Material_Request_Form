# ------------------------------------------------------------------------ #
# Title: Main running file of OTV rev.02
# Description: OTV takes user input on asset#, company, vendor,
# quantity, price. Searches established db using asset# to fill item specific
# info. Uses input to establish customer company, vendor, quant/price
# uses dictionary key/value to obtain customer company shipping number, and
# vendor mailing address.
# ------------------------------------------------------------------------ #


# Imports
from IOclasses import IO
# from Data import Item as asset
# # from query import FetchItem



# Presentation ---------------------------------------------------------- #
while True:
    IO.print_menu_items()
    # Menu of Options
    # 1) ENTER ITEM
    # 2) SHOW LIST OF ITEMS
    # 3) PRODUCE MRF
    # 4) SAVE, CLOSE, AND EMAIL MRF
    # 5)

    # if 1 then allow user to enter gage_id, quantity and price
    if IO.input_menu_choice() == '1':
        # IO.input_item_data()
        print(IO.input_item_data())
    # if 2 then print current list of items


