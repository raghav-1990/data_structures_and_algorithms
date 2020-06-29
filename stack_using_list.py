class StackList:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def _len(self):
        return len(self.data)

    def _push(self, element):
        self.data.append(element)
        print "Element pushed to stack: {}".format(element)

    def _pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.data.pop()

    def _top(self):
        if self.is_empty():
            return "Stack is empty"
        return self.data[-1]

s = StackList()
s._push(10)
s._push(20)
print 'length of stack: {}'.format(s._len())
print "top element is: {}".format(s._top())
print "element popped: {}".format(s._pop())
print "element popped: {}".format(s._pop())
print "element popped: {}".format(s._pop())
print 'length of stack: {}'.format(s._len())
print "top element is: {}".format(s._top())

