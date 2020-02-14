class NewList(DQ):
    def return_list(self,input_list):
        return input_list
newlist = NewList()
result = newlist.return_list([1,2,3])
print(result)


class NewList(DQ):
    def __init__(self, initial_state):
        self.data = initial_state
my_list = NewList([1,2,3,4,5])
print(my_list.data)