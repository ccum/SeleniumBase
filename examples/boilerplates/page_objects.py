'''
Example of using the Page Object Model (POM) for tests, using page selectors.
Helps make your code more Readable, Maintainable, and Reusable.
Import a file like this at the top of your test files.
'''


class HomePage(object):
    ok_button = "#ok"
    cancel_button = "#cancel"
    see_items_button = "button.items"


class ShoppingPage(object):
    buyable_item = 'img[alt="Item"]'
    add_to_cart = "button.add"
    go_to_checkout = "#checkout"


class CheckoutPage(object):
    remove_from_cart = "button.remove"
    buy_now = "#buy-now"
    shop_more = "#shop-more"


'''
# Now you can do something like this in your test files:

from master_class import MasterTestCase
from page_objects import HomePage, ShoppingPage, CheckoutPage

class MyTests(MasterTestCase):

    def test_example(self):
        self.open(RANDOM_SHOPPING_WEBSITE)
        self.click(HomePage.see_items_button)
        self.click(ShoppingPage.buyable_item)
        self.click(ShoppingPage.add_to_cart)
        self.click(CheckoutPage.buy_now)
        self.assert_element("#success")
        self.assert_text("Order Received!", "#h2")
'''
