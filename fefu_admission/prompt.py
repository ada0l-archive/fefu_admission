class Prompt:

    NO = 0
    YES = 1

    @staticmethod
    def get_confirm(message=""):
        answer = input("{}: [y/n]".format(message)).lower()
        while True:
            if answer == "y" or answer == "yes":
                return Prompt.YES
            if answer == "n" or answer == "no":
                return Prompt.NO
            answer = input("{}: [y/n]".format(message)).lower()

    @staticmethod
    def get_str(message=""):
        return input("{}: ".format(message))
