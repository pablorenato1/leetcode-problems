class Solution: #First Solution
    def __init__(self) -> None:
        self.dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        self.letter = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        self.transcription = [1,5,10,50,100,500,1000]
    def romanToInt(self, s: str) -> int:
        totalLetters = len(s)
        if totalLetters == 1:
            return self.transcription[self.letter.index(s)]
        skip = None # Just to know if i need to skip the next letter
        total = 0
        for p, l in enumerate(s):
            if skip == True:
                skip = False
                continue
            pos = self.letter.index(l)
            if p < totalLetters-1:
                nextNumber = self.transcription[self.letter.index(s[p+1])]
                if nextNumber > self.transcription[pos]: # If the next letter is bigger than the current one
                    skip = True
                    temp = nextNumber - self.transcription[pos]
                    total += temp
                    continue
                total += self.transcription[pos]
                continue
            total += self.transcription[pos]
        return total

class Solution2: # HashMap
    def __init__(self) -> None:
        self.dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    def romanToInt(self, s: str) -> int:
        totalLetters = len(s)
        if totalLetters == 1:
            return self.dict[s]
        skip = None # Just to know if i need to skip the next letter
        total = 0
        for p, l in enumerate(s):
            if skip == True:
                skip = False
                continue
            if p < totalLetters-1:
                nextNumber = self.dict[s[p+1]]
                if nextNumber > self.dict[l]: # If the next letter is bigger than the current one
                    skip = True
                    temp = nextNumber - self.dict[l]
                    total += temp
                    continue
                total += self.dict[l]
                continue
            total += self.dict[l]
        return total

if __name__=="__main__":
    a = Solution2()
    print(a.romanToInt("LVIII"))