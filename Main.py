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
from ExcelWrite import XL
from Data import Item
from query import QueryGage as query
import pickle

items = []
xliste = []
savedir = r"C:\Users\alcom\Documents\otv_v2\gitignore"
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
        # instantiate new item
        new_item = Item(*query.fetch(IO.get_gage_id()), IO.get_price(), IO.get_quantity())
        # add item to list of items to print for user
        items.append(new_item)
        # add item in stupid MRF formatting to xliste
        xliste.append(new_item.mrf_list_format())
        continue

    # todo: show list of items
    # if choice = 2 then show list of current items being sent out
    if IO.input_menu_choice() == '2':
        for item in items:
            print(item)
        continue
    # todo:use company and dictionary to obtain shipping info

    # todo: edit the mrf

    # todo: use pandas? to write the template
    # if choice = 3 then write the items to excel
    if IO.input_menu_choice() == '3':
        # pickle the xl_liste to be used to write the dumb xl format
        with open('xliste.pickle', 'wb') as f:
            pickle.dump(xliste, f)

        XL.xl_write('xliste.pickle', savedir, "test01")
        #XL.xlsave(savedir, "test01")
    # todo: use time stamps to create file save name

    # todo: create dictionary address book ( key = vendor, value = tuple(address lines) )

    # todo: create a setup class that will ask for the users name, use 'default keyword argument'
    #  and user input inside xlwrite parameters.

