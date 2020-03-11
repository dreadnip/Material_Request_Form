# ------------------------------------------------------------------------ #
# Title: Data classes
# Description: obtains data from db
# ChangeLog (Who,When,What):
# Acompeau, <date>, created file
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")




# Data ------------------------------------------------------------------- #
class Item(object):
    """Stores data about an item:

    properties:
        id = stores gage_id

        model_num = stores item's model number

        serial_num = stores serial number

        mfg = Manufacturer of item

        desc = description of item

        company = client company

        price = quoted price

        quantity = quantity


    methods:


    changelog: (When,Who,What)
        ASC, 0222320, CREATED FILE
        ASC. 022520. ADDED PRICE/ QUANTITY
    """

    # -- Constructor --
    def __init__(self, gage_id, model_num, serial_num, mfg, desc, company, cert_template, price, quantity):
        # -- Attributes --
        self.__gage_id = gage_id
        self.__model_num = model_num
        self.__serial_num = serial_num
        self.__mfg = mfg
        self.__desc = desc
        self.__company = company
        self.__cert_template = cert_template
        self.__price = price
        self.__quantity = quantity

    # -- Properties --
    @property
    def gage_id(self):
        return str(self.__gage_id).strip()

    @gage_id.setter
    def gage_id(self, value):
        self.__gage_id = value

    @property
    def model_num(self):
        return str(self.__model_num).strip()

    @model_num.setter
    def model_num(self, value):
        self.__model_num = value

    @property
    def serial_num(self):
        return str(self.__serial_num).strip()

    @serial_num.setter
    def serial_num(self, value):
        self.__serial_num = value

    @property
    def mfg(self):
        return str(self.__mfg).upper().strip()

    @mfg.setter
    def mfg(self, value):
        self.__mfg = value

    @property
    def desc(self):
        return str(self.__desc).upper()

    @desc.setter
    def desc(self, value):
        self.__desc = value

    @property
    def company(self):
        return str(self.__company).strip()

    @company.setter
    def company(self, value):
        self.__company = value

    @property
    def cert_template(self):
        return str(self.__cert_template).strip()

    @cert_template.setter
    def cert_template(self, value):
        self.__cert_template = value

    @property
    def price(self):
        return str(self.__price)

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def quantity(self):
        return str(self.__quantity)

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    # -- Methods --
    def to_string(self):
        """ Explicitly returns a string with this object's data """
        return self.__str__()

    def description(self):
        return str(self.desc + ';' + self.serial_num + ";" + self.gage_id)

    # def __iter__(self):
    #     return self

    def __repr__(self):
        """ Implicitly returns a list with this object's data """
        return repr([self.gage_id, self.model_num, self.serial_num, self.mfg, self.desc,
                     self.company, self.cert_template, self.price, self.quantity])

# Processing ------------------------------------------------------------- #


# Presentation ---------------------------------------------------------- #
