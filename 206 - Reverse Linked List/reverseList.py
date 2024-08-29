class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:

    if not head or not head.next:
        return head

    node = None

    while head:
        temp = head.next
        head.next = node
        node = head
        head = temp

    return node


def main():
    # test cases
    list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    list2 = ListNode(1, ListNode(2))
    list3 = ListNode()

    print_linked_list(reverse_list(list1))
    print_linked_list(reverse_list(list2))
    print_linked_list(reverse_list(list3))


def print_linked_list(node: ListNode) -> None:
    while node:
        print(node.val, end="->")
        node = node.next
    print()


main()
