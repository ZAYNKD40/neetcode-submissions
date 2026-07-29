class MedianFinder:

    def __init__(self):
        self.data= [] #everytime median finder called, initialize a list. using self. is what matters
        #data is arbitrary name
        

    def addNum(self, num: int) -> None:
        self.data.append(num) #appending num
        

    def findMedian(self) -> float:
        self.data.sort() #sort then find median
        n = len(self.data)
        return (self.data[n//2]) if (n&1) else (self.data[n//2] + self.data[n//2-1]) / 2
        #if odd, return middle number, if not odd, return the two middle numbers /2. also n&1 is and to check if odd
        
        