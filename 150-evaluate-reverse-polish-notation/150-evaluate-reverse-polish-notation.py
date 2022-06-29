class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return str(tokens[0])
        for i in range(len(tokens)):
            if tokens[i] == "-":
                return self.evalRPN(tokens[:i-2]+[str(int(tokens[i-2])-int(tokens[i-1]))]+tokens[i+1:])
            elif tokens[i] == "+":
                return self.evalRPN(tokens[:i-2]+[str(int(tokens[i-2])+int(tokens[i-1]))]+tokens[i+1:])
            elif tokens[i] == "/":
                return self.evalRPN(tokens[:i-2]+[str(int(float(tokens[i-2])/int(tokens[i-1])))]+tokens[i+1:])
            elif tokens[i] == "*":
                return self.evalRPN(tokens[:i-2]+[str(int(tokens[i-2])*int(tokens[i-1]))]+tokens[i+1:])