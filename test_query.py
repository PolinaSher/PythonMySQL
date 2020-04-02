'''
Created on Mar 27, 2020

@author: polin
'''
import unittest
from Database.database import * 



class TestCalc(unittest.TestCase):

    def testName(self):
        self.assertTrue(True) 
    
    def test_onerow(self):
        row = 'Ben', 'Park Lane 38', 10
        result = print_customer_where()
        self.assertTrue(row, result)
        
# 
# if __name__ == "__main__":
#     #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main()