class Example:
    def __init__(self, name):
        self.name = name

    def displayName(self):
        print(self.name)

obj = Example('Nilesh')
obj.displayName()

class CSEStudents:
    stream = 'CSE'
    def __init__(self, roll):
        self.roll = roll

    def setAddress(self, add):
        self.add = add
    def getAddress(self):
        return self.add

a = CSEStudents(13)
a.setAddress('Siwan, Bihar')
print(a.getAddress())


"""printing objects"""
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return "Value of Test that a is %s b is %s" % (self.a,self.b)
    def __str__(self):
        return "Value through str method is a : %s , b : %s"%(self.a,self.b)

tst = Test(4,6)
print(tst)
print([tst])