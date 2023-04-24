class Solution:
    def interpret(self, command: str) -> str:
        i=0
        self.result=''
        while i<len(command):
            if command[i]=='G':
                self.result+='G'
                i+=1
                continue
            if command[i]=='(' and command[i+1]==')':
                self.result+='o'
                i+=2
                continue
            if command[i]=='(' and command[i+1]=='a':
                self.result+='al'
                i+=4
                continue
        return self.result
pass
so=Solution()
command = "(al)G(al)()()G"
print(so.interpret(command))