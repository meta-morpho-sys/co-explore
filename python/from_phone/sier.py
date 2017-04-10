# -*- coding: utf-8 -*-
def picture_bits(b):
   """ 
   Make a picture from the binary digits
   (ie bits) of b
   """
   s = str(bin(b))  # binary form, eg 0b10111
   s = s[2:]  # drop 0b, ie 10111
   s = s.replace('0', '❤️')
   s = s.replace('1', '😘')
   return s
   
r = 1
while r < 2**32:
    print(picture_bits(r))
    r ^= (r<<1)
