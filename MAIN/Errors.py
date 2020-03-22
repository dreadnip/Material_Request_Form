if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")


# Errors ------------------------------------------------------------------ #
class NotValidInput(Exception):
    """This input is not in the allowed input"""

    def __str__(self):
        return "Input not accepted. Please enter a number between 1-5."

# Errors ------------------------------------------------------------------ #
