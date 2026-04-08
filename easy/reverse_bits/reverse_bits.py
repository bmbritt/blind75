class Solution:
    def reverseBits(self, n: int) -> int:
        
        # binary: 0000 (32 bit)
        result = 0
        
        # for each bit (bit 0 -> 31 inclusive)
        for i in range(32):
            
            # pick out the current bit by shifting it to the least significant (ones) place and logic ANDing it with 1
            # binary: 0000 or 0001 (32 bit)
            bit = (n >> i) & 1
            # put the bit you picked out into the correct (reversed) position
            reversedBit = bit << (31 - i)
            # Use logical OR to transfer the newly positioned bit into the result (0 OR 0 = 0, 0 OR 1 = 1)
            result |= reversedBit
        return result