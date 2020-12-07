class C1:
    def getString(self):
        return input("type string:")
        
    def printString(self):
        print(self.getString().upper())
        
c1 = C1()
c1.printString()