from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout():

    def test_single_sku(self):
        basket = "A"
        assert CheckoutSolution().checkout(basket) == 50

    def test_single_sku_with_multiple_count(self):
        basket = "AA"
        assert CheckoutSolution().checkout(basket) == 100

    def test_several_skus(self):
        basket = "AB"
        assert CheckoutSolution().checkout(basket) == 80

    def test_skus_with_offer_no_remainder(self):
        basket = "AAA"
        assert CheckoutSolution().checkout(basket) == 130

    def test_skus_with_offer_with_remainder(self):
        basket = "AAAA"
        assert CheckoutSolution().checkout(basket) == 180

    def test_skus_with_several_offer_bundles(self):
        basket = "AAABBAAA"
        assert CheckoutSolution().checkout(basket) == 305

    def test_illegal_input(self):
        basket = "AAAk"
        assert CheckoutSolution().checkout(basket) == -1
