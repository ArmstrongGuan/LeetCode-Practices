class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==0:
            return(0)
        if divisor<0:
            dividend, divisor=-dividend,-divisor
        if dividend<0:
            multiplier= -1
        else:
            multiplier =1
        dividend= abs(dividend)
        print([dividend, divisor])
        n=len(str(divisor))
        if len(str(dividend))< n:
            return(0)
        a=str(dividend)
        output='0'
        carry=int(a[0])
        a=a[1:]
        while 1:
            if carry < divisor:
                output+='0'
                if len(a)>0:                    
                    carry=int(str(carry)+'0')+int(a[0])
                    a=a[1:]
                else:
                    break
            if carry >=divisor:
                q=0
                while carry>=divisor:
                    carry=carry-divisor
                    q+=1
                output+=str(q)
                if len(a)>0:
                    carry=int(str(carry)+'0')+int(a[0])
                    a=a[1:]
                else:
                    break
        c=int(output)*multiplier
        if c> 2**31-1:
            return(2**31-1)
        if c< -2**31:
            return(-2**31)
        return(c)
                
        
        
        
        
        
        
        
        
        
#         while carry>=divisor or len(a)>0:
#             #print(carry)
#             while carry<divisor:
#                 output+='0'
#                 if len(a)>0:                    
#                     carry=int(str(carry)+'0')+int(a[0])
#                     a=a[1:]                
#             print(carry)
#             if carry >=divisor:
#                 q=0
#                 while carry>=divisor:
#                     carry=carry-divisor
#                     q+=1
#                 output+=str(q)
#                 #if len(a)>0:
#                 #    carry=int(str(carry)+'0')+int(a[0])
#                 #    a=a[1:]
#                 #else:
#                 #    break
#             if len(a)>0:
#                 carry=int(str(carry)+'0')+int(a[0])
#                 a=a[1:]
#             print(carry)
#             print('output'+output)
#         c=int(output)*multiplier
#         print(c)
#         if c> 2**31-1:
#             return(2**31-1)
#         if c< -2**31:
#             return(-2**31)
#         return(c)
                
                
        #     if int(a[:n])>=divisor:
        #         carry=int(a[:n])
        #         while carry>=divisor:
        #             carry=carry-divisor
        #             q+=1
        #         output+=str(q)
        #         a=a[n:] if carry else str(carry)+ a[n:]
        #     else:
        #         carry=int(a[:n+1])
        #         while carry>=divisor:
        #             carry=carry-divisor
        #         print(carry)
        #         a=str(carry)+ a[n+1:] if carry else a[n+1:]
        # carry=int(a)
        # while carry>=divisor:
        #     carry=carry-divisor
        # return(carry if dividend>=0 else carry+divisor)