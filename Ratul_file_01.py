# linked list implementation

class NODE:
    def __init__(self, item = 'Head' , next = None):
        self.item = item
        self.next =  next

class LINKED_LIST:
    def __init__(self):
        self.head = NODE()

     # insert at beginning
    def insert_at_beginning(self, item):
        node = NODE(item, self.head.next)
        self.head.next = node
    
    # insert at end
    def insert_at_end(self, item):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = NODE(item, None)

    # get length function
    def get_length(self):
        cnt = 0
        current_node = self.head
        while current_node.next:
            cnt += 1
            current_node = current_node.next
        return cnt

    # insert at specific index
    def insert_at_specific_index(self, location, item):
        if location < 0 or location > self.get_length():
            print("Invalid location")
            return

        if location == 0:
            self.insert_at_beginning(item)
            return

        cnt = 0
        current_node = self.head
        while current_node:
            if cnt == location - 1:
                node = NODE(item, current_node.next)
                current_node.next = node
                break
            current_node = current_node.next
            cnt += 1

    # search item
    def search(self, search_item):
        current_node = self.head.next
        while current_node != None:
            if current_node.item == search_item:
                print("Data Found at linked list")
                return
            current_node = current_node.next
        print("opps! Data Not Found")


    # remove item from list
    def remove(self, remove_item):
        if self.head.next is None:
            print("Empty")
            return

        previous = self.head
        current_node = previous.next
        while current_node != None:
            if current_node.item == remove_item:
                break
            previous = current_node
            current_node = current_node.next
        previous.next = current_node.next

        
    # printing method
    def printing(self):
        if self.head.next is None:
            print("list is Empty")
            return
        
        current_node = self.head
        r_string = ""
        while current_node:
            r_string = r_string + str (current_node.item) + ' ==> '
            current_node = current_node.next

        print(r_string)

if __name__ == '__main__' :
    LL = LINKED_LIST()

    # insert at beginning
    LL.insert_at_beginning(200)
    LL.insert_at_beginning(100)
    LL.printing()

    # insert at end
    LL.insert_at_end(300)
    LL.insert_at_end(400)
    LL.printing()

    # insert at specific location
    LL.insert_at_specific_index(3, 500)
    LL.insert_at_specific_index(5, 600)
    LL.printing()

    # search item
    LL.search(500)
    LL.printing()

    # rempve item 
    LL.remove(600)
    LL.remove(400)
    LL.printing()