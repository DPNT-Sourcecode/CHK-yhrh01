from lib.solutions.CHK.checkout_solution import CheckoutSolution
import pytest

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


    @pytest.mark.parametrize(
        "basket, expected_total",
        [
            ("AAAA", 180),
            ("AAAAAA", 250),
            ("AAAAAAAAAAA", 450),
            ("AAAAAAAAAAAAAA", 580),
        ]
    )
    def test_skus_with_offer_with_remainder(self, basket, expected_total):
        assert CheckoutSolution().checkout(basket) == expected_total

    @pytest.mark.parametrize(
        "basket, expected_total",
        [
            ("AAABB", 175),
            ("AAAAABB", 245),
            ("AAAAAAAA", 330),
        ]
    )
    def test_skus_with_several_offer_bundles(self, basket, expected_total):
        assert CheckoutSolution().checkout(basket) == expected_total

    @pytest.mark.parametrize(
        "basket, expected_total",
        [
            ("BEE", 80),
            ("EE", 80),
            ("BBEE", 110),
            ("BBEEEE", 160),
        ]
    )
    def test_skus_with_reduction(self, basket, expected_total):
        assert CheckoutSolution().checkout(basket) == expected_total

    @pytest.mark.parametrize(
        "basket, expected_total",
        [
            ("F", 10),
            ("FF", 20),
            ("FFF", 20),
            ("FFFF", 30),
            ("FFFFFF", 40),
        ]
    )
    def test_skus_with_self_reduction(self, basket, expected_total):
        assert CheckoutSolution().checkout(basket) == expected_total


    def test_illegal_input(self):
        basket = "AAAk"
        assert CheckoutSolution().checkout(basket) == -1




