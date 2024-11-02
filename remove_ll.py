class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def print_list(node):
    while node:
        print(node.value, end=' ')
        node = node.next


def remove(head, value):
    dummy_head = Node(None, head)
    current = head
    previous = dummy_head

    while current:
        if current.value == value:
            previous.next = current.next
        else:
            previous = current

        current = current.next

    return dummy_head.next


last = Node(6, None)
node_2 = Node(5, last)
head = Node(4, node_2)

result = remove(head, 4)
print_list(result)