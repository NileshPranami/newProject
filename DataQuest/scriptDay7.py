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
