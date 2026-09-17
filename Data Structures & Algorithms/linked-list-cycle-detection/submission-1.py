# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if head.next is None:
            return False
        seen_nodes = set([head])
        next_node = head.next
        while next_node not in seen_nodes:
            seen_nodes.add(next_node)
            next_node = next_node.next
            if next_node is None:
                return False
        return True