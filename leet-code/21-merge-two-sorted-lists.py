''''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 
Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Minha solução - O((n+m)2)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
           return None
        
        head = None
        array = []

        if list1:
          head = list1
          

          while list1:
            if(list1.next != None):
              list1 = list1.next
            else:
              list1.next = list2
              break
        else:
           head = list2
        
        while head:
          array.append(head.val)
          head = head.next

        array.sort()

        print(array)

        newListHead = self.createListByArray(array)

        return newListHead

    def createListByArray(self, array: list[int]) -> ListNode:
        if (len(array) > 1):
           return ListNode(array[0], self.createListByArray(array[1:]))
        else:
          return ListNode(array[0], None)

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Solution().mergeTwoLists(list1, list2)
Solution().mergeTwoLists(None, ListNode(0, None))



# Solução do GPT: O(n + m)


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Nó fictício para simplificar a ligação dos nós
        dummy = ListNode()
        current = dummy

        # Percorre ambas as listas enquanto ambas tiverem nós
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # Liga o restante da lista não esgotada
        current.next = list1 or list2

        # Retorna o primeiro nó real (após o dummy)
        return dummy.next
