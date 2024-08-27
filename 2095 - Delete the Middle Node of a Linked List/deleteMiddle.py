from typing import Optional


class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


def delete_middle(head: Optional[ListNode]) -> Optional[ListNode]:

    if not head:
        return head

    prev = ListNode(0, head)

    slow = prev
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    slow.next = slow.next.next

    return prev.next


def print_linked_list(head: Optional[ListNode]) -> None:
    while head:
        print(head.val, end="->" if head.next else "")
        head = head.next
    print()


def main():

    # 1-> 2-> 3-> 4
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

    # 1-> 3-> 4-> 7-> 1-> 2-> 6
    head2 = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))

    print_linked_list(delete_middle(head1))
    print_linked_list(delete_middle(head2))


main()
