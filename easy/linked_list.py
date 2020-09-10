'''''''''
linked list basic stuff
'''''''''
class node():
    def __init__(self, value):
        self.value = value
        self.next = None
    
    @staticmethod
    def create_from_array(array):
        head = node(array[0])
        curr = head
        for i in array[1:]:
            curr.next = node(i)
            curr = curr.next
        return head

    def print_list(self):
        curr = self
        while(True):
            if(curr.next != None):
                print(curr.value, end=',')
            else:
                print(curr.value)
                break
            curr = curr.next
        return curr
    
    def reverse(self):
        tail = None
        curr = self
        while(curr != None):
            body = node(curr.value)
            body.next = tail
            tail = body
            curr = curr.next
        return tail
            
    
if __name__ == '__main__':
    head = node.create_from_array([1, 2, 3, 4, 5])
    rev = head.reverse()
    rev.print_list()
    head.print_list()
    
    