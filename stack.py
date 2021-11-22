class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        return self.items == []
    
    def prints(self):
        for data in reversed(self.items):
            print(data)
    
def insertAtBottom(obj, item):
    if obj.isEmpty():
        obj.push(item)
    else:
        popped = obj.items.pop()
        insertAtBottom(obj, item)
        obj.push(popped)

def reverse(obj):
    if not obj.isEmpty():
        popped = obj.items.pop()
        reverse(obj)
        insertAtBottom(obj, popped)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.prints()
reverse(s)
s.prints()
