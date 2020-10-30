
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
        if isinstance(item, ListNode):
            if self.head is None:
                self.head = item
                item.prev = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.prev = self.tail
                self.tail = item
        return
    
    def remove_list_item_by_id(self, item_id):
        "remove the list item with the item id"

        curr_id = 1
        curr_node = self.head
        while curr_node is not None:
            prev_node = curr_node.prev
            next_node = curr_node.next

            if curr_id == item_id:
                if prev_node is not None:
                    prev_node.next = next_node
                    if next_node is not None:
                        next_node.prev = prev_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.prev = None
                return
            #needed for the next iteration
            curr_node = next_node
            curr_id += 1 
        return

from collections import deque

class DequeListNode:
    def __init__(self, data):
        "constructor class to initiate this object"

        self.data = data
        return
    
if __name__ == "__main__":
    node1 = ListNode(10)
    node2 = ListNode(12.25)
    node3 = ListNode("testing")
    node4 = ListNode(125)

    track = DoubleLinkedList()
    print("Length of Double Linked List: ", track.list_length())
    
    for curr_node in [node1, node2, node3, node4]:
        track.add_list_item(curr_node)
        print("track length: ", track.list_length())
        track.output_list()
    
    results = track.unordered_search(12.25)
    print(results)

    track.remove_list_item_by_id(3)
    track.output_list()

    print("[Deque]")
    deque_track = deque([node1, node2, node3])
    for item in deque_track:
        print(item.data)
    node4 = DequeListNode("deque_start")
    deque_track.appendleft(node4) # add an item at the beginning
    print("After append left")
    for item in deque_track:
        print(item.data)
    
    node5 = DequeListNode("deque_end")
    deque_track.append(node5) # add an item at the end 
    print("After append right")
    for item in deque_track:
        print(item.data)

    


    
        

        
    
