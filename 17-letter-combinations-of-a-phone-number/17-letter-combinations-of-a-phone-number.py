class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)<1:
            return []
        map={'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z'] }
        if len(digits)==1:
            return map[digits]
        def product(lis1, lis2):
            output=[]
            for i in range(len(lis1)):
                for j in range(len(lis2)):
                    output= output+[lis1[i]+lis2[j]]
            return output
        output=map[digits[0]]
        print(output)
        for i in range(1,len(digits)):
            output=product(output, map[digits[i]] )
        return output
        