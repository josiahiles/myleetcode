class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        first = ListNode(0)
        curr = first

        n = 0

        while l1 is not None or l2 is not None or n:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum = v1 + v2 + n
            n = sum // 10

            curr.next = ListNode(sum % 10)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return first.next
