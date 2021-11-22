class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("The given previous node must be in LinkedList.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_at(self, index, data):
        new_node = Node(data)
        if index < 0:
            print("error")
        if index == 0:
            self.head = new_node
        
        count = 0
        itr = self.head
        while itr.next:
            if count == index -1:
                new_node.next = itr.next
                itr.next = new_node
            itr = itr.next
            count+= 1 

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        
    def delete_node(self, index):
        if  index < 0:
            print("incorrect index")
            return
        if index ==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr.next:
            if count == index -1:
                itr.next = itr.next.next
                break
            count +=1
            itr = itr.next

    def length(self):
        count = 0
        itr = self.head
        while itr.next:
            count += 1
            itr = itr.next

        return count

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    ll.head.next = second
    second.next = third
    third.next = fourth
    # ll.printlist()
    # ll.reverse()
    ll.printlist()
    ll.append(5)
    ll.printlist()
    ll.push(0)
    ll.printlist()
    ll.insert_after(second, 2.5)
    ll.printlist()
    ll.delete_node(3)
    ll.printlist()
    print(ll.length())
    ll.insert_at(3, 2.5)
    ll.printlist()