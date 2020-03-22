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
from ExcelWrite import XL as xl
from Data import *
from query import QueryGage as query
import os
from prettytable import PrettyTable

# Constants
items = []
xliste = []
dir = os.getcwd()
index = 1
# Presentation ---------------------------------------------------------- #
# todo: find way to save user info, s/t that it only requires a "login" with initials. Pickled file with {initials:name}
# Eventually the user object will prove useful to have email information stored s/t it can email the mrf automatically.
# current_user = User(*IO.get_user_info())


vendor = IO.get_vendor()
while True:

    IO.print_menu_items()

    # Menu of Options
    # 1) ENTER ITEM
    # 2) SHOW LIST OF ITEMS
    # 3) DELETE ITEM FROM LIST
    # 4) WRITE MRF
    # 5) SAVE AND QUIT

    choice = IO.input_menu_choice()
    # if 1 then allow user to enter gage_id, quantity and price
    if choice == '1':
        # instantiate new item
        new_item = Item(index, *query.fetch(IO.get_gage_id()), IO.get_price(), IO.get_quantity())
        # add item to list of items to print for user
        items.append(new_item.to_list())
        # add item in stupid MRF formatting to xliste
        xliste.append(new_item.mrf_list_format())
        # increment the index
        index += 1
        continue

    # if choice = 2 then show list of current items being sent out
    elif choice == '2':
        t = PrettyTable(['Index', 'GageID', 'Model#', 'Serial Number', 'MFG', 'Description',
                         'Client Company', 'Certificate Type', 'Price', 'Quantity'])
        for item in items:
            t.add_row(item)

        print(t)
        continue


    # if choice = 3 then delete user choice from list
    elif choice == '3':
        # remove the item
        print('Functionality not added yet.')
        continue

    # if choice = 4 write the info obtained to the excel sheet
    elif choice == '4':
        # xl.write_mrf_details(vendor, requestor, RMA, shipping info, date requested, date required, cert_type, interval, cal to mfg specs)
        # todo: why cant I write new_item.gage_id(), new_item.company()??
        #xl.write_project(index, new_item.gage_id(), new_item.company())
        xl.write_mrf_details('asc')
        xl.write_item(xliste)
        continue

    # if choice = 5 save and quit the program
    elif choice == '5':
        xl.save_sheet(dir, vendor, 'asc')
        break

    else:
        print("The command was not recognized, please enter a number [1-5]")
        continue
    # todo: create dictionary address book ( key = vendor, value = tuple(address lines) )

    # todo: create a setup class that will ask for the users name, use 'default keyword argument'
    #  and user input inside xlwrite parameters.

    # todo: how to exit
