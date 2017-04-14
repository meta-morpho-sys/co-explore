"""
Things that need clarification:

1. Why is this file called mysier.py?
2. What is the ^ symbol?
3. What is << ?
4. why is the form a triangle, on the whole?



Answers:
1. It was originally based on sier.py, hence the my.  But why sier.py?
   Answer: I abbreviated a reference to Sierpinski. See https://en.wikipedia.org/wiki/Sierpinski_triangle
   for more.
2. ^ is called caret. It represents the exclusive-or operation, aka XOR. 
   Here's a truth table for XOR, i.e. it shows a ^ b for every possible binary a and b values:
     
              b
      a^b  | 0  1
   --------|------
     a   0 | 0  1
         1 | 1  0
    
  For reference, here is OR, the ordinary (not-exclusive) OR operation:
  
              b
   a or b  | 0  1
   --------|------
     a   0 | 0  1
         1 | 1  1
    
  

"""


def picture_bits(b):
   """ 
   Make a picture from the binary digits
   (ie bits) of b
   """
   s = str(bin(b))  # binary form, eg 0b10111
   s = s[2:]  # drop 0b, ie 10111


   s = s.replace('0', ' ️')
   s = s.replace('1', 'X')
   return s
   
r = 1
while r < 2**128:
    print(picture_bits(r))
    r ^= (r<<1)       # equivalent to r = r ^ (r<<1)   (like how x += 1 is x = x+1)

