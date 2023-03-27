def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node
        dummy_node = ListNode()
        
        # assign dummy node to tail
        tail = dummy_node
        
        # while list1 and list2 are not empty
        # if list1 value is less than list2 value
        # tail.next pointer will point to list 1
        # list1 will be assigned its next pointer
        # else the tail next pointer will be list2
        
        while list1 and list2:
            if list1.value < list2.value:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy_node.next