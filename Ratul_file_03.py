# linked list implementation

class Node:
    def __init__(self, data = "Head", next = None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = Node()

    # append at beginning
    def append_at_beginning(self, data):
        node = Node(data, self.head.next)
        self.head.next = node
    
    # append at end
    def append_at_end(self, data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data, None)
    
    # get length function
    def get_length(self):
        cnt = 0
        current_node = self.head
        while current_node:
            cnt += 1
            current_node = current_node.next
        return cnt
     
     # insert at specific index
    def insert_at_specific_index(self, index, data):
        if index < 0 or index > self.get_length():
            print("Invalid Index")
            return

        if index == 0:
            self.append_at_beginning(data)
            return

        cnt = 0
        current_node = self.head
        while current_node:
            if cnt == index - 1:
                node = Node(data, current_node.next)
                current_node.next = node
                break
            current_node = current_node.next
            cnt += 1
   
    # searching item
    def search(self, search_item):
        current_node = self.head
        while current_node != None:
            if current_node.data == search_item:
               print("data found in linked list")
               return
            current_node = current_node.next
        print("opps! data not found")       

   # remove item 
    def remove(self, remove_item):
         pre = self.head
         if pre is not None:
             if pre.data == remove_item:
                 self.head = pre.next
                 pre = None
                 return

         while pre is not None:
             if pre.data == remove_item:
                 break
             prev = pre
             pre = pre.next
         if pre == None:
             return
         prev.next = pre.next
         pre = None
         

        # try to another option 

        # if self.head == remove_item:
        #     self.head = self.head.next
        #     return
        # tmp = self.head.next
        # prev = self.head
        # while tmp.next is not None:
        #     if tmp.data == remove_item:
        #         prev.next = tmp.next
        #     tmp = tmp.next
        #     prev = tmp.next
        # return
     
    def printing_function(self):
        if self.head is None:
            print("Empty")
            return

        current_node = self.head
        result_s = ""
        while current_node:
            result_s = result_s + str (current_node.data) + ' --> '
            current_node = current_node.next

        print(result_s)


if __name__ == '__main__' :
    LL = Linked_List()

    # append at beginning
    LL.append_at_beginning(329)
    LL.append_at_beginning(454)
    LL.printing_function()

    # append at End
    LL.append_at_end(786)
    LL.append_at_end(348)
    LL.printing_function()

    # insert at specific index
    LL.insert_at_specific_index(5, 3112)
    LL.insert_at_specific_index(6, 9432)
    LL.printing_function()

    # remove item
    LL.remove(786)
    LL.remove(329)
    LL.printing_function()

    # search item
    LL.search(3112)
    LL.search(45)
    LL.printing_function()
