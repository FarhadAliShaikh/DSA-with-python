class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current = self.head
        output_str = ''
        while current:
            output_str += str(current.data) + ' --> ' if current.next else str(current.data)
            current = current.next
        print(output_str)

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  
            current.next = prev       
            prev = current            
            current = next_node       
        self.head = prev              

if __name__ == '__main__':
    ll = LinkedList()
    
    ll.insert_values([1,2,3,4,5,6,7,8,9])
    
    print('Original Linked List:')
    ll.display()

    ll.reverse()
    print('Reversed Linked List:')
    ll.display()
