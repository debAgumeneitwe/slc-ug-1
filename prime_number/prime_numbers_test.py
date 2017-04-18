import unittest
from prime_numbers import is_prime_number

class TestPrimeGenerator(unittest.TestCase):
    
    def setUp(self):
        self.test1 = is_prime_number(-1)
        self.test2 = is_prime_number(1)
        self.test3 = is_prime_number(1066340417491710595814572169)
        self.test4 = is_prime_number(10668)
        self.test5 = is_prime_number(5)
        self.test6 = is_prime_number("boy")
    
    def test_number_less_than_zero_not_prime(self):
		self.assertFalse(self.test1)
            
    def test_1_as_a_prime(self):
        self.assertFalse(self.test2)
        
    def test_massive_number_is_prime(self):
		self.assertTrue(self.test3)
        
    def test_5_is_prime(self):
		self.assertTrue(self.test5)
        
     def test_massive_even_number_is_not_prime(self):
		self.assertTrue(self.test4)
        
    def test_invalid_type_string(self):
        self.assertTrue(self.test6)
        
        
    
    
   
    


if __name__ == '__main__':
    unittest.main()
        

     
        
    


        
        
        
        