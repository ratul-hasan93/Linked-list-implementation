# linked list

class Node:
    def __init__(self, data = "Head",  next = None):
        self.data =  data
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = Node()
     
     # append at beginning
    def append_at_beginning(self, data):
        node = Node(data, self.head.next)
        self.head.next = node
    
    # append at end
    def append_at_end(self, data):
        c_node = self.head
        while c_node.next:
            c_node = c_node.next
        c_node.next = Node(data, None)

    # get length function
    def get_length(self):
        cnt = 0
        c_node = self.head
        while c_node.next:
            cnt += 1
            c_node = c_node.next
        return cnt

    # append at specific index
    def append_at_specific_index(self, index, data):
        if index < 0 or index > self.get_length():
            print("Invalid index")
            return

        if index == 0:
            self.append_at_beginning(data)
            return

        cnt = 0
        c_node = self.head

        while c_node:
            if cnt == index - 1:
                node = Node(data, c_node.next)
                c_node.next = node
                break
            c_node = c_node.next
            cnt += 1
    
    # search function
    def search(self, search_data):
        c_node = self.head.next
        while c_node != None:
            if c_node.data == search_data:
                print("Data Found at List")
                return
            c_node = c_node.next
        print("opps! Data Not Found")
        

    # remove data from linked list
    def remove(self, remove_data):
        if self.head.next is None:
            print("Empty")
            return
        
        prev = self.head
        c_node = prev.next
        while c_node != None:
            if c_node.data == remove_data:
                break
            prev = c_node
            c_node = c_node.next
        
        prev.next = c_node.next


    
    # printing function
    def printing(self):
        if self.head.next is None:
            print("List is Empty")
            return
        c_node = self.head
        string = ""
        while c_node:
            string = string + str (c_node.data) + ' --> '
            c_node = c_node.next

        print(string)


if __name__ == '__main__' :
    LL = Linked_list()

    # append at beginning
    LL.append_at_beginning(12)
    LL.append_at_beginning(23)
    LL.printing()

    # append at end
    LL.append_at_end(42)
    LL.append_at_end(67)
    LL.printing()

    # append at specific index
    LL.append_at_specific_index(3, 20)
    LL.append_at_specific_index(0, 11)
    LL.printing()

    # search item
    LL.search(2)
    LL.printing()

    # remove item
    LL.remove(12)
    LL.remove(67)
    LL.printing()