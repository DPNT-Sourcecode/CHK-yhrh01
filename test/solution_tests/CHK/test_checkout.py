from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout():

    def test_single_sku(self):
        basket = "A"
        assert CheckoutSolution().checkout(basket) == 50

    def test_single_sku(self):
        basket = "A"
        assert CheckoutSolution().checkout(basket) == 50
