# 2. Add Two Numbers
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Add two numbers represented by linked lists.

        Args:
            l1: Head of first linked list (least significant digit first).
            l2: Head of second linked list.

        Returns:
            Head of a new linked list representing the sum.
        """

        # convert both lists to integers, add them, and convert back
        n1 = self.listNodeToInteger(l1)
        n2 = self.listNodeToInteger(l2)

        return self.integerToListNode(n1 + n2)
    
    def listNodeToInteger(self, node: Optional[ListNode]) -> int:
        """Convert a reversed linked list into its integer value.

        The linked list stores digits in reverse (1's place at the head), so
        we iterate through and accumulate with increasing powers of ten.

        Args:
            node: Head of the list to convert.

        Returns:
            The integer value represented by the list.
        """

        number = 0
        power = 1
        
        while node:
            # add current digit times the current power of 10
            number += node.val * (10 ** power)
            power += 1
            node = node.next
            
        return number
    
    def integerToListNode(self, integer: int) -> Optional[ListNode]:
        """Convert a non-negative integer to a reversed linked list.

        Each digit of the integer becomes a node in the list, with the least
        significant digit first.  A zero value results in a single node with
        value 0.

        Args:
            integer: The non-negative integer to convert.

        Returns:
            Head of the newly created linked list.
        """

        if integer == 0:
            return ListNode(0)

        dummy = ListNode(0)  # placeholder to simplify list construction
        cur = dummy

        while integer > 0:
            digit = integer % 10
            cur.next = ListNode(digit)
            cur = cur.next
            integer //= 10

        return dummy.next