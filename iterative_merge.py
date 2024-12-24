class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_lists(a, b):
    if not a:  # თუ პირველი სია ცარიელია
        return b
    if not b:  # თუ მეორე სია ცარიელია
        return a
    # Head და Tail ინიციალიზაცია
    if a.data <= b.data:
        head = tail = a
        a = a.next
    else:
        head = tail = b
        b = b.next
    # მასივების შერწყმა
    while a and b:
        if a.data <= b.data:
            tail.next = a
            tail = a
            a = a.next
        else:
            tail.next = b
            tail = b
            b = b.next
    # დარჩენილი ელემენტების მიბმა
    tail.next = a if a else b
    return head

# Driver code
def print_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

# Linked List 1
a = Node(2)
a.next = Node(4)
a.next.next = Node(8)
a.next.next.next = Node(9)

# Linked List 2
b = Node(1)
b.next = Node(3)
b.next.next = Node(8)
b.next.next.next = Node(10)

# Merge Lists
res = merge_lists(a, b)
print("Merged Sorted Linked List is:")
print_list(res)
