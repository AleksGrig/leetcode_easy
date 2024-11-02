# 203. Remove linked list element

# Given the head of a linked list and an integer val,
# remove all the nodes of the linked list that has Node.val == val,
# and return the new head.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list():
    head = ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(
                val=6,
                next=ListNode(
                    val=3,
                    next=ListNode(
                        val=4, next=ListNode(val=5, next=ListNode(val=6, next=None))
                    ),
                ),
            ),
        ),
    )
    return head

def print_list(head: ListNode):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


# head = [1, 2, 6, 3, 4, 5, 6]
head = create_list()
val = 6


def removeElements(head: ListNode, val: int):
    dummy = ListNode(None, next=head)
    prev = dummy
    cur = head

    while cur:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next

    return dummy.next


head = removeElements(head, val)
print_list(head)
