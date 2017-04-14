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
         
  NOTE: XOR is defined for larger integers than just 0 and 1, by applying it BITWISE.
        What do I mean by BITWISE?  Answer: a bit (aka binary-digit) at a time.
        
        e.g.
        
        0b10110 ^ 0b11011
        
            a = 0b10110
            b = 0b11011
        a ^ b = 0b01101
        
        
        
 
3. << is the binary shift left operator, which is mathematically equivalent to DOUBLING a number.
  
4. This would be the pattern if we just shifted left repeatedly
   1
   10
   100
   1000
   10000
   100000
   1000000


r = 1
r ^= (r<<1)

r << 1     =>  0b10
r ^ (r<<1) =>  0b1 ^ 0b10 => 0b11

       0b1
      0b10


001
010
100

r = 0b11
r ^ = (r<<1) =>  0b11 ^ 0b110
   0b011
   0b110
 = 0b101

r = 0b101

   0b0101
   0b1010
 = 0b1111
 
 1
 11
 101
 1111
 
 r = 01111
 s = 11110
   = 10001
   
010001
0110011
01010101
011111111

Claim: For a and b being 0 or 1
a^b =====  (a + b) mod 2   === (a+b)%2
   
              b
  (a+b)%2  | 0  1
   --------|------
     a   0 | 0  1
         1 | 1  0

   


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

