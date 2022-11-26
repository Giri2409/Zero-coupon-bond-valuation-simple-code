# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 12:19:36 2022

@author: Giri
"""

def zero_coupon_bond(p,r,t):
    return p/(1+r)**t

 
if __name__== '__main__':
   
     
    bond=zero_coupon_bond(100, 0.05, 5)

     
    print("price of the zerocoupon bond is: %.2f" % bond)
