class Stack:
    """Custom Stack Class"""
    def __init__(self, stack=[]):
        if type(stack) != type(list()):
            raise ValueError
        else:
            self.__stack = stack

    def __str__(self):
        print("top")
        for item in self.__stack:
            print(f"-- {item}")
        return "bottom"
    
    def get_length(self):
        return len(self.__stack)

    def put(self, item):
        self.__stack.insert(0, item)

    def pop(self):
        try:
            return self.__stack.pop(0)
        except:
            print("Empty Stack.")

class CountingStack(Stack):
    """A Stack that counts put and pop-operations"""
    def __init__(self, stack=[]):
        Stack.__init__(self,stack)
        self.__counter = 0
    def get_counter(self):
        return self.__counter
    def put(self, item):
        self.__counter += 1
        Stack.put(self, item)
    def pop(self):
        self.__counter += 1
        return Stack.pop(self)
            
if __name__ == '__main__':
    stack = CountingStack()
    print(stack)
    stack.put(3.14)
    stack.put(42)
    stack.put('sixty nine')
    stack.put(True)
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(f"Counter: {stack.get_counter()}")