# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:08:52 2020

@author: Manjunath
"""

import unittest
import Rought_pgr

class MyTest(unittest.TestCase): 
  
    def setUp(self): 
        pass


    def test_Find(self):
        self.assertListEqual( Rought_pgr.data,[260030, 5249, 882, 883, 15]) 



    def test_Ideal_data1(self):
        self.assertListEqual(Rought_pgr.data_Actual,[52907, 264535, 881, 881])

    def test_Accle_loss(self):
        self.assertAlmostEquals(Rought_pgr.Accle_loss,1.7029882624227497)

    def test_Temp_loss(self):
        self.assertAlmostEquals(Rought_pgr.Temp_loss , -0.11350737797957322)

    def test_Batt_loss(self):
        self.assertAlmostEquals(Rought_pgr.Batt_loss , -0.22701475595914644)


if __name__ == '__main__': 
    unittest.main()


    #Text_file.txt