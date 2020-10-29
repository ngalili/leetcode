
class ListNode:
    def __init__(self, data):
        "constructor to initiate this object"

        self.data = data
        self.next = None # store reference (next item)
        self.prev = None # store reference (previous item)
        return 
    
    def has_value(self, value):
        "method to compare the value with the node data"
        
        return True if self.data == value else False 

class DoubleLinkedList:
    def __init__(self):
        "constructor to initiate this object"

        self.head = None
        self.tail = None
        return

    def list_length(self):
        "return the number of list items"
        count = 0
        curr_node = self.head
        while curr_node is not None:
            count += 1
            curr_node = curr_node.next
        return count
    
    def output_list(self):
        "outputs the list - the actual value of the node"
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next
        return
    
    def unordered_search(self, value):
        "search the linked list for the node that has this value"

        curr_node = self.head
        node_id = 1 
        results = []
        while curr_node is not None:
            if curr_node.has_value(value):
                results.append(node_id)
            
            curr_node = curr_node.next
            node_id += 1
        return results

    def add_list_item(self, item):
        "add an item at the end of the list"
        if not isinstance(item, ListNode):
            if self.head is None:
                self.head = item
                item.prev = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.prev
        

        
    
