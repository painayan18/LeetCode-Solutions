class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def main() -> None:
    # test1
    linked_list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print_linked_list(odd_even_list(linked_list1))

    # test 2
    linked_list2 = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
    print_linked_list(odd_even_list(linked_list2))


def odd_even_list(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next

    odd.next = even_head

    return head


def print_linked_list(node: ListNode) -> None:
    while node:
        print(node.val, end="->")
        node = node.next
    print()


main()
