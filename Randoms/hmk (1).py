class stuff:
    def __init__(self,num1,num2,num3,num4,word1,word2,nums1,nums2,nums3):
        self.num1,self.num2,self.num3,self.num4,self.word1,self.word2,self.nums1,self.nums2,self.nums3 = num1,num2,num3,num4,word1,word2,nums1,nums2,nums3
    def square(self):
        if self.num1 == self.num2 == self.num3 == self.num4:
            print("I'm a square")
        else:
            print("I'm not a square")
    def len(self):
        val1 = len(self.word1)
        val2 = len(self.word2)
        if val1 > val2:
            print(self.word1)
        else:
            print(self.word2)
    def powers(self):
        nums4 = self.nums2 ** self.nums3
        nums5 = self.nums1 ** nums4
        print(nums5)
d = stuff(3,4,5,6,"hello","bat",2,2,2)    
d.square()
d.len()
d.powers()
d = stuff(4,4,4,4,"hello","bat",2,2,2)    
d.square()