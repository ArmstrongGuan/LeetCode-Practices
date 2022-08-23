class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        pointer1=len(num1)-1
        pointer2=len(num2)-1
        result=""
        remainder=0
        while pointer1>=0 or pointer2>=0 or remainder>0:
            remainder+=int(num1[pointer1]) if pointer1>=0 else 0
            remainder+=int(num2[pointer2]) if pointer2>=0 else 0
            result=str(remainder %10)+result
            remainder=remainder//10
            pointer1-=1
            pointer2-=1
        return result
        
        