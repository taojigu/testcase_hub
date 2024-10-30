

class Saucedemo:
    """ useful config class for https://www.saucedemo.com/inventory.html"""
    @staticmethod
    def saucedemo_login_url():
        return 'https://www.saucedemo.com/'

    @staticmethod
    def standard_user_name():
        """standard username to login"""
        return 'standard_user'

    @staticmethod
    def password():
        return "secret_sauce"

    @staticmethod
    def inventory_page_url():
        return "https://www.saucedemo.com/inventory.html"
