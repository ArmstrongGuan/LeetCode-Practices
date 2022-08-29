class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result=[0]*(len(num1)+len(num2))
        num1=num1[::-1]
        num2=num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i+j]+=int(num1[i])*int(num2[j])
        for i in range(len(num1)+len(num2)):
            if result[i]>=10:
                result[i+1]+=result[i]//10
                result[i]=result[i]%10
        while result[-1]==0 and len(result)>1:
            result.pop()
        output=""
        for i in result:
            output=str(i)+output
        return output
                
                