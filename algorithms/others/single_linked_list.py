
class ListNode:
    def __init__(self, data):
        "constructor to initiate this object"
        
        self.data = data # store data
        self.next = None # store reference (next item)
        return
    
    def has_value(self, value):
        "method to compare the value with the node data"
        
        return True if self.data == value else False 

class SingleLinkedList:
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

    def add_list_item(self, item):
        "add an item at the end of the list"
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item   
        else:
            self.tail.next = item
        self.tail = item
        return
    
    def unordered_search(self):
        "search the linked list for the nodes with a specified value"
        curr_node = self.head
        node_id = 1
        results = []

        while curr_node is not None:
            if curr_node.has_value(value):
                results.append(node_id)
            
            curr_node = curr_node.next
            node_id += 1
        return results

    def remove_list_item_by_id(self, item_id):
        "remove the node according to its id"
        curr_id = 1
        curr_node = self.head
        prev_node = None

        while curr_node is not None:
            if curr_id == item_id:
                if prev_node is not None: # if this is the first node (head)
                    prev_node.next = curr_node.next
                else:
                    self.head = curr_node.next # we don't have to look any further
                    return
            # need for the next iteration
            prev_node = curr_node
            curr_node = curr_node.next
            curr_id += 1
        
        return


if __name__ == "__main__":
    node1 = ListNode(10)
    item2 = 'abc'
    node3 = ListNode(12.34)
    node4 = ListNode('xyz')

    track = SingleLinkedList()
    print("Length of Single Linked List: ", track.list_length())

    for curr_item in [node1, item2, node3, node4]:
        track.add_list_item(curr_item)
        print("check lenght: ", track.list_length())
        track.output_list()
