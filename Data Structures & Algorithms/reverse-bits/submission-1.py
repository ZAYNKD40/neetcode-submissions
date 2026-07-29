class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:] #strip the 0b when counting, matter when counting 0 since bin give 0b......
        padding = binary.zfill(32) #padd it to 32 digit with zeroes as needed, also padding turned into string here that is why the padding[::-1] work which would not work on int
        res = padding[::-1] #create a new reverse 
        return int(res,2)
        #this is not the bit manipulation solution for bit manip expect << >> & more 
        