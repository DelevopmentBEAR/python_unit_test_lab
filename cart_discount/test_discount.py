import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    # Can it handle three prices and one discount?
    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        calculated_discount = discount(prices)
        self.assertEqual(expected_discount, calculated_discount)
        
    # Can it handle only one price and no discounts?    
    def test_list_of_one_price_no_discount_raise_exception(self):
        self.fail('finish this test')
        
    # Is the price an int? If not, raise exception.    
    def test_list_cotains_non_int_values_raise_exception(self):
        self.fail('finish this test')
    
    # Are the prices in a list, if so can it be handled? If not, raise exception.
    def test_argument_is_list_raise_exception(self):
        self.fail('finish this test')

    # Is price a number/int greater than zero?
    def test_list_contains_num_greater_than_zero(self):
        self.fail('finish this test')
        
    # Is price a negative number/zero? If it doesn't work, raise exception.
    def test_list_contains_zero_or_negative_num_raise_exception(self):
        self.fail('finish this test')

    # Does the price hit a max number?
    def test_max_num__raise_exception(self):
        self.fail('finish this test')
    
    # What is the min number for price?
    def test_min_num_raise_exception(self):
        self.fail('finish this test')
        
    #('Outline: decide whether an empty cart returns 0 or raises an error.')
    def test_discount_with_empty_list(self):
        self.fail('finish this test')
        
    #('Outline: decide whether one item returns 0 or raises an error.')
    def test_discount_with_one_price(self):
        self.fail('finish this test')
        
    #('Outline: decide whether duplicate lowest prices still return one price.')
    def test_discount_with_duplicate_lowest_prices(self):
        self.fail('finish this test')
        
    #('Outline: decide whether decimal prices are supported.')
    def test_discount_with_decimal_prices(self):
        self.fail('finish this test')
        
    #('Outline: decide how free, negative, or refunded items are handled.')
    def test_discount_with_zero_or_negative_price(self):
        self.fail('finish this test')
        
    #('Outline: decide whether non-numeric prices raise TypeError or ValueError.')
    def test_discount_with_non_numeric_price(self):
        self.fail('finish this test')
        
    #('Outline: decide whether None instead of a list raises TypeError.')
    def test_discount_with_none(self):
        self.fail('finish this test')

if __name__ == '__main__':
    unittest.main()